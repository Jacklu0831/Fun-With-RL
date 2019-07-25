<h1 align="center">Banana Collector (DDQN)</h1>

<p align="center">
  <image src="output/result.gif">
    </p>

In this project, the goal is to train an agent to navigate a virtual world and collect as many yellow bananas as possible while avoiding blue bananas. This game is in the [Unity ML-agents](https://github.com/Unity-Technologies/ml-agents). I solved this envionment with a **Value Based method** called **Double Q-Networks**. While the requirement is suggested to be met within 1800 training episodes, I was able to do it in only 388 episodes with the double Q-network from [this paper](https://arxiv.org/abs/1509.06461). Both my implementation for the single and double deep Q-learning agents are included in the output folder. 

### Double Q-Networks

Why use **Double Q-Networks**? Because it is better than (single) Q-Networks, allow me to explain.

A deep Q network (DQN) is a multi-layered neural network that for a given state s outputs a vector of action values. However, talented minds in Google Deepmind figured out that the max operator in standard Q-learning and DQN use the same weight values both to select and to evaluate an action. This makes it more likely to select overestimated values, resulting in overestimated values. To prevent that, Double Q-Networks was used to decouple the selection from the evaluation. In practice, the local network and target network as far enough to be used for decoupling. Therefore, I used the local weights for determining actions and target to evaluate values. 

# Results

**The average score at every 100 episodes of training**

<image src="output/success.png" height="70%" width="70%"></image>

**Score vs. Episode plot**

<image src="output/stats"></image>

# Rules

__37 states__\
Coordinates\
Velocities\
Other ray-based perception of objects in forward direction

__4 actions__\
0 - move forward\
1 - move backward\
2 - turn left\
3 - turn right

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of agent is to collect as many yellow bananas as possible while avoiding blue bananas. The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes. 

# Paper

[Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461)