# Double-Jointed Reacher

<video src="output/result.mp4"></video>

In this environment, a double-jointed arm of each [reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md) has to move to the constantly moving target locations. 

**Actor-Critic Agent**

Actor - policy-based approach, agent learning to act\
Critic - value-based approach, agent estimates situations and actions

Actor-critic agents leverage the best from both policy and value-based approaches. In practice, actor and critic are two neural networks that generate data for training each other. [This slide](http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf.pdf) has helped me ton in understanding the math of how it works. 

- Critic estimates the current state value
- Actor chooses an action
- Take action and receive the new SARS' collection
- Input S' into the TD estimate equation to get original state value
- Use this state value to train the critic
- Use the critic's current state value and the TD estimate to find the Advantage value
- Use the advantage value to train the Actor
- Repeat all steps above

# Rules

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.