# Atari Pong

<video src="output/result.mp4"></video>

Trained the classic Atari Pong game on OpenAI Gym with Proximal Policy Optimization, an "upgrade" to the REINFORCE algorithm I used for the cart pole project. Due to having 4 conv and 3 fc layers, the DRL network took almost an hour to train on a mid-tier GPU for 1000 episodes. However, if taken a closer look at the pong-PPO file, the performance of my trained policy is already maxmized (0.0) before the training finished, which was a pleasant surprise as I did not think it could achieve optimality in 1000 episodes.

**Proximal Policy Optimization**\
Solves a major issue of the REINFORCE algorithm by making use of old trajectories that were generated with old policies instead of simply discarding them. PPO is built upon REINFORCE and it uses the clipped surrogate function for better training efficiency. This state-of-the-art algorithm is also used to train the OpenAI Five system (Dota).

# Rules

You have to know the rules. 