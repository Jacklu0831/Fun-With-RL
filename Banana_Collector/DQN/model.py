import torch
import torch.nn as nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    '''model'''

    def __init__(self, state_size, action_size, seed, hidden_layers):
        '''initialize parameters and build model'''
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        # first layer and initialize ModuleList
        fc1 = nn.Linear(state_size, hidden_layers[0])
        self.hidden_layers = nn.ModuleList([fc1])

        # pair up parameters in list hidden_layers
        layer_sizes = zip(hidden_layers[:-1], hidden_layers[1:])
        
        # ModuleList.extend() is convenient for making model dynamic
        self.hidden_layers.extend([nn.Linear(h1, h2) for h1, h2 in layer_sizes])
                                   
        self.output = nn.Linear(hidden_layers[-1], action_size)

    def forward(self, x):
    
        for linear in self.hidden_layers:
            x = F.leaky_relu(linear(x))

        x = self.output(x)
        return x