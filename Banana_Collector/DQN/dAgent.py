import torch
from DQN import Agent


# inherit agent
class DAgent(Agent):
    def learn(self, experiences, gamma):
        states, actions, rewards, next_states, dones = experiences
        
        # temporary evaluation mode to find target Q
        self.qnetwork_target.eval()
        with torch.no_grad():
            Q_local_next = self.qnetwork_local(next_states)
            Q_target_next = self.qnetwork_target(next_states)
            # get the action index
            Q_local_action = torch.max(Q_local_next, dim=1, keepdim=True)[1]
            # use action index prediction from local to get Q value from target
            Q_target_max = Q_target_next.gather(1, Q_local_action)
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