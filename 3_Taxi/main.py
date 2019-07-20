from agent import Agent
from monitor import interact
import gym
import numpy as np
import time
import datetime

env = gym.make('Taxi-v2')
agent = Agent()

# set timer
tick = time.time()
avg_rewards, best_avg_reward, scores = interact(env, agent, 100000)
tock = time.time()
elapsed = tock - tick
print(str(datetime.timedelta(seconds=elapsed)))

for score in scores:
    print(score)
