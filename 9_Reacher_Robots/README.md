[//]: # (Image References)
[image1]: https://user-images.githubusercontent.com/10624937/43851024-320ba930-9aff-11e8-8493-ee547c6af349.gif "Trained Agent"

# Double-Jointed Reacher Robot

![Trained Agent][image1]

In this environment, a double-jointed arm of each [reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md) has to move to the constantly moving target locations. Used [**deep deterministic policy gradients continuous control method**](https://arxiv.org/abs/1509.02971) with the **Ornstein-Uhlenbeck process** for noise aided exploration. Achieved the "solved" benchmark of average score >= 30 over 100 consecutive episodes over all agents. One problem that I encountered is when trying to train 20 agents at the same time under synchronized time steps, I accidentally only trained one and never let the others learn, resulting in extremely slow learning and 0 result. 

### Actor-Critic Agent

Actor - policy-based approach, agent learning to act\
Critic - value-based approach, agent estimates situations and actions

Actor-critic agents leverage the best from both policy and value-based approaches. In practice, actor and critic are two neural networks that generate data for training each other. [This slide](http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf.pdf) has helped me ton in understanding the math of how it works. 

**Pipeline**
- Critic estimates current state value, Actor chooses an action
- Take action and receive the new SARS' collection
- Input S' into the TD estimate equation to get original state value
- Use this state value to train the critic
- Use the critic's current state value and the TD estimate to find the Advantage value
- Use the advantage value to train the Actor
- Repeat all steps above

### Deep Deterministic Policy Gradients

Althought DDPG was first proposed to be actor-critic. However, it is classified by a lot of researcher as a DQN method for continuous spaces along with [NAF](https://arxiv.org/abs/1603.00748) due to its deterministic behavior. 

**Difference from Plain Actor-Critic Agent**
- use actor as an approximate maximizer to calculate action value
- the critic learns to evaluate the optimal value function using the action value

# Rules

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

https://github.com/SIakovlev/Continuous-Control