import numpy as np
import random

from model import ActorNN

import torch
import torch.nn.functional as F
import torch.optim as optim

class Actor:

    def __init__(self, device, state_size, action_size, random_seed, 
                 memory, noise, lr):   

        self.DEVICE = device
        self.state_size = state_size        
        self.action_size = action_size
        self.seed = random.seed(random_seed)

        # hyperparameters
        self.LR = lr        

        # Actor Network (local + target)
        self.local = ActorNN(state_size, action_size, random_seed).to(self.DEVICE)
        self.target = ActorNN(state_size, action_size, random_seed).to(self.DEVICE)
        self.optimizer = optim.Adam(self.local.parameters(), lr=self.LR)

        # replay memory        
        self.memory = memory

        # noise process
        self.noise = noise

    def act(self, state, add_noise=True):
        """Returns actions for given state as per current policy."""
        state = torch.from_numpy(state).float().to(self.DEVICE)

        # temporary eval mode for getting action
        self.local.eval()
        with torch.no_grad():
            action = self.local(state).cpu().data.numpy()
        self.local.train()        

        # add OU process for exploration
        if add_noise:
            action += self.noise.sample()
    
        return np.clip(action, -1, 1)

    def step(self, state, action, reward, next_state, done):
        """Save experience in replay memory, and use random sample to learn."""
        # save experience / reward
        self.memory.add(state, action, reward, next_state, done)

    def reset(self):
        # reset noise to original parameters
        self.noise.reset()