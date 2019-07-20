# Banana Collector (DQN)

In this project, the goal is to train an agent to navigate a virtual world and collect as many yellow bananas as possible while avoiding blue bananas. This game is in the [Unity ML-agents](https://github.com/Unity-Technologies/ml-agents). Solved by a **Value Based method** called **Double Q-Networks**. While the requirement is suggested to be met within 1800 training episodes, I was able to do it in 388 episodes with the double Q-network from [this paper](https://arxiv.org/abs/1509.06461).

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"
![Trained Agent][image1]

# Results

The average score at every 100 episodes of training

<image src="output/success"></image>

The Score vs. Episode graph

<image src="output/stats"></image>

# Rules

__37 states__

Coordinates\
Velocities\
Other ray-based perception of objects in forward direction

__4 actions__

0 - move forward\
1 - move backward\
2 - turn left\
3 - turn right

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. 

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes. 