import numpy as np
import random

from model import CriticNN

import torch
import torch.nn.functional as F
import torch.optim as optim

class Critic:        

    def __init__(self, device, state_size, action_size, random_seed, gamma, TAU, lr):        
        self.DEVICE = device

        self.state_size = state_size        
        self.action_size = action_size
        self.seed = random.seed(random_seed)

        # hyperparameters
        self.GAMMA = gamma
        self.TAU = TAU
        self.LR = lr
        
        # Critic Network (local + target)
        self.local = CriticNN(state_size, action_size, random_seed).to(self.DEVICE)
        self.target = CriticNN(state_size, action_size, random_seed).to(self.DEVICE)
        self.optimizer = optim.Adam(self.local.parameters(), lr=self.LR)

    def step(self, actor, memory):
        # learn, when memory is large enough
        experiences = memory.sample()        
        if not experiences:
            return
        
        self.learn(actor, experiences)

    def learn(self, actor, experiences):
        """Update policy and value parameters using given batch of experience tuples.
        Params
        ======
            experiences (Tuple[torch.Tensor]): tuple of (s, a, r, s', done) tuples 
            gamma (float): discount factor
        """

        states, actions, rewards, next_states, dones = experiences

        # ---------------------------- update critic ---------------------------- #
        # get predicted next-state actions and Q values from target models
        actions_next = actor.target(next_states)
        Q_targets_next = self.target(next_states, actions_next)
        # compute Q targets for current states (y_i)
        Q_targets = rewards + (self.GAMMA * Q_targets_next * (1 - dones))
        # compute critic loss
        Q_expected = self.local(states, actions)
        critic_loss = F.mse_loss(Q_expected, Q_targets)
        # minimize the loss
        self.optimizer.zero_grad()
        critic_loss.backward()
        # torch.nn.utils.clip_grad_norm(self.local.parameters(), 1)
        self.optimizer.step()

        # ---------------------------- update actor ---------------------------- #
        # compute actor loss
        actions_pred = actor.local(states)
        actor_loss = - self.local(states, actions_pred).mean()
        # minimize the loss
        actor.optimizer.zero_grad()
        actor_loss.backward()
        actor.optimizer.step()

        # ----------------------- update target networks ----------------------- #
        self.soft_update(self.local, self.target)
        self.soft_update(actor.local, actor.target)

    def soft_update(self, local_model, target_model):
        """Soft update model parameters.
        Params
        ======
            local_model: PyTorch model (weights will be copied from)
            target_model: PyTorch model (weights will be copied to)
            tau (float): interpolation parameter 
        """
        tau = self.TAU
        for target_param, local_param in zip(target_model.parameters(), local_model.parameters()):
            target_param.data.copy_(tau*local_param.data + (1.0-tau)*target_param.data)