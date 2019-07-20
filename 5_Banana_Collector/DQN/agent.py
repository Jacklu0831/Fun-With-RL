import numpy as np
import random
import torch
import torch.nn.functional as F
import torch.optim as optim

from DQN import QNetwork
from DQN import ReplayBuffer

class Agent():
    '''interacts with environment and learns'''
    
    # hyperparameters initialized here
    def __init__(self, state_size, action_size, seed, hidden_layers=[64,64], buffer_size=int(100000), 
                 batch_size=64, gamma=0.99, tau=0.001, learning_rate=0.0005, update_every=4):
        '''initialize agent'''
        
#         state_size (int): dimension of each state
#         action_size (int): dimension of each action
#         seed (int): random seed
#         hidden_layers (list of int ; optional): number of each layer nodes
#         buffer_size (int ; optional): replay buffer size
#         batch_size (int; optional): minibatch size
#         gamma (float; optional): discount factor
#         tau (float; optional): for soft update of target parameters
#         learning_rate (float; optional): learning rate
#         update_every (int; optional): how often to update the network
            
        self.state_size = state_size
        self.action_size = action_size
        self.seed = random.seed(seed)
        self.buffer_size = buffer_size
        self.batch_size = batch_size
        self.gamma = gamma
        self.tau = tau
        self.lr = learning_rate
        self.update_every = update_every

        # try using GPU
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        
        # Q model/network
        self.qnetwork_local = QNetwork(state_size, action_size, seed, hidden_layers).to(self.device)
        self.qnetwork_target = QNetwork(state_size, action_size, seed, hidden_layers).to(self.device)
        self.optimizer = optim.Adam(self.qnetwork_local.parameters(), lr=self.lr)
        
        # replay buffer
        self.memory = ReplayBuffer(action_size, self.buffer_size, self.batch_size, seed, self.device)
        
        # time step to know when to learn
        self.t_step = 0
        
    def step(self, state, action, reward, next_state, done):
        '''add experience to memory and trigger learn'''
        self.memory.add(state, action, reward, next_state, done)
        self.t_step += 1
        self.t_step = self.t_step % self.update_every
        if self.t_step == 0:
            # enough samples in memory
            if len(self.memory) > self.batch_size:
                experiences = self.memory.sample()
                self.learn(experiences, self.gamma)
                
    def act(self, state, eps=0.0):
        '''get action'''
        state = torch.from_numpy(state).float().unsqueeze(0).to(self.device)
        self.qnetwork_local.eval()
        with torch.no_grad():
            action_values = self.qnetwork_local(state)
        self.qnetwork_local.train()
        
        # e-greedy selection
        if random.random() > eps:
            return np.argmax(action_values.cpu().data.numpy())
        else:
            return random.choice(np.arange(self.action_size))
    
    def learn(self, experiences, gamma):
        '''update q network through backpropagation engine'''
        states, actions, rewards, next_states, dones = experiences
        
        # temporary evaluation mode to find target Q
        self.qnetwork_target.eval()
        with torch.no_grad():
            Q_target_next = self.qnetwork_target(next_states)
            Q_target_max = torch.max(Q_target_next, dim=1, keepdim=True)[0]
            y = rewards + gamma * Q_target_max * (1 - dones)
        self.qnetwork_target.train()
        
        # predict Q in local
        self.optimizer.zero_grad()
        Q = self.qnetwork_local(states)
        y_pred = Q.gather(1, actions)
        
        # error
        loss = torch.sum((y - y_pred) ** 2)
        
        # backprop
        loss.backward()
        self.optimizer.step()
        
        # update network
        self.soft_update(self.qnetwork_local, self.qnetwork_target, self.tau)
        
    def soft_update(self, local_model, target_model, tau):
        '''soft update model params'''
        for target_param, local_param in zip(target_model.parameters(), local_model.parameters()):
            target_param.data.copy_(tau * local_param.data + (1 - tau) * target_param.data)