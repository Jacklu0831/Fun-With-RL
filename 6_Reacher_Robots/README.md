Actor - policy-based approach, agent learning to act
Critic - value-based approach, agent estimates situations and actions

Actor-critic agents leverage the best from both policy and value-based approaches. In practice, actor and critic are two neural networks that generate data for training each other. [This slide](http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf.pdf) has helped me ton in understanding the math of how it works. 

Here is a simple outline:

- Critic estimates the current state value
- Actor chooses an action
- Take action and receive the new SARS' collection
- Input S' into the TD estimate equation to get original state value
- Use this state value to train the critic
- Use the critic's current state value and the TD estimate to find the Advantage value
- Use the advantage value to train the Actor
- Repeat all steps above

# Double-Jointed Reacher


The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm

Trained the classic Atari Pong game on OpenAI Gym with Proximal Policy Optimization, an "upgrade" to the REINFORCE algorithm I used for the cart pole project. Due to having 4 conv and 3 fc layers, the DRL network took almost an hour to train on a mid-tier GPU for 1000 episodes. However, if taken a closer look at the pong-PPO file, the performance of my trained policy is already maxmized (0.0) before the training finished, which was a pleasant surprise as I did not think it could achieve optimality in 1000 episodes.

**Proximal Policy Optimization**\
Solves a major issue of the REINFORCE algorithm by making use of old trajectories that were generated with old policies instead of simply discarding them. PPO is built upon REINFORCE and it uses the clipped surrogate function for better training efficiency. This state-of-the-art algorithm is also used to train the OpenAI Five system (Dota).

### Results (PPO)

<video src="output/result.mp4"></video>