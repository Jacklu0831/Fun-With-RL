import numpy as np
import random
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent."""
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.epsilon = 0.003
        self.gamma = 0.9
        self.alpha = 0.1

    def get_probs(self, Q_s):
        '''obtains action probabilities with the epsilon-greedy policy'''
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        best_a = np.argmax(Q_s)
        policy_s[best_a] = 1 - self.epsilon + self.epsilon / self.nA
        return policy_s
        
    def select_action(self, state):
        """ Given the state, select an action. This function is used for Sarsa"""
        act_space = [i for i in range(0, self.nA)]
        # send in array of actions and array of probabilities
        action = np.random.choice(np.arange(self.nA), p = self.get_probs(self.Q[state])) if state in self.Q else random.choice(act_space)
        return action
    
    def get_Q(self, state):
        """Given the state, calculate the expected q value. This function is used for Expected Sarsa"""
        policy_s = self.get_probs(self.Q[state])
        Q_next = np.dot(self.Q[state], policy_s)
        return Q_next

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple."""

        # next_action = self.select_action(next_state)  #  <- Sarsa
        # Q_next = self.Q[next_state][next_action]  # <- Sarsa
        Q_next = self.get_Q(next_state) # <- Max Sarsa
        delta = reward + self.gamma * Q_next - self.Q[state][action] 
        self.Q[state][action] = self.Q[state][action] + self.alpha * delta
        