<h1 align="center">Atari Pong</h1>

<p align="center">
  <image src="output/result.gif" height="25%" width="25%">
</p>

<p align="center">Green is the trained agent with conv layers.</p>

Trained a [Atari Pong](https://gym.openai.com/envs/Pong-v0/) player in OpenAI Gym with **Proximal Policy Optimization (PPO)**, an improvement to the REINFORCE algorithm I used for the [Cart Pole project](https://github.com/Jacklu0831/Reinforcement-Learning-Simulation-Solving/tree/master/7_Cart_Pole). 

Due to having 4 convolutional and 3 fully-connected layers, the DRL network took almost an hour to train on a mid-tier GPU for 1000 episodes. However, if taken a closer look at the pong-PPO file, the performance of my trained policy is already maxmized (0.0) before the training finished, which was a pleasant surprise as I did not think it could achieve it within 1000 episodes. This makes a good demonstration of the effciency of reusing trajectories (explained below).

**Proximal Policy Optimization**

Solves a major issue of the REINFORCE algorithm by making use of trajectories that were generated with old policies instead of simply discarding them. PPO is built upon REINFORCE and it uses the clipped surrogate function for better training efficiency. To put simply, despite each iteration only being an estimation of what would be produced by the REINFORCE algorithm, PPO ultimates achieves better performance by making use of all trajectories collected. 

This state-of-the-art algorithm is also used to train the OpenAI Five system (Dota). For more details on PPO, refer to [this paper](https://arxiv.org/abs/1707.06347), it is shorter than most papers, quite enjoyable to read. 

# Rules

Atari 2600 game Pong. In this environment, the state input is an RGB image of the screen, which is an array of shape (210, 160, 3) Each action is repeatedly performed for a duration of kk frames, where kk is uniformly sampled {2, 3, 4}. 

# Papers

[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
