# Tennis 

<p align="center">
	<image src="output/result.gif"></image>
</p>

As shown above this project is about making two agents collaborate and make the ball not fall on the table while bouncing over the net, and this causes the environment to appear non-stationary from the viewpoint of any one agent. Instead of a single agnet deep reinforment learning algorithm, I looked into **Multi-Agent Deep Deterministic Policy Gradient algorithm (MADDPG)**, which is based on single agent **DDPG** and the **Actor-Critic** method. While the actor networks of the agents are trained separately, I chose to use the same critic and memory (replay buffer) for both of the agents to achieve better learning efficiency. 

For more detail on the actor-critic method, since it is very popular, just a search in google should yield a list of nice results. [Here](http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf.pdf) is the one I used. I recommand this [paper](https://arxiv.org/pdf/1706.02275.pdf?source=post_page---------------------------) for learning about the MADDPG algorithm. 

# Implementation Details

For each agent’s actor, I used a two-layer neural network with 256 units in the first hidden layer and 128 units in the second hidden layer. For each agent’s critic, I used 256 units in the first hidden layer (and both agents’ actions are concatenated with the output of the input layer) and 128 units in the second hidden layer. 

Hyperparameters caused quite a bit of trouble in this project due to having to decide it for both the actor and the critic network. I started with setting them as the same number, which caused very slow learning. In the end, I settled down with 0.0001 for the actor and 0.0003 for the critic. They are intentionally low for the agents to reach nearer to the optimal policy and value.

# Rules 

In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.

The observation space is 24-dimensional consisting of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation.

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents).

After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially different) scores. We then take the maximum of these 2 scores. This yields a single score for each episode.

The environment is considered solved, when the average (over 100 episodes) of those scores is at least +0.5.

# Try it Yourself

- Download any unity simulator [here](https://github.com/Unity-Technologies/ml-agents).
- Create a new conda environment (optional)
- Download the dependencies in Python by running the first cell of Tennis.ipynb
- Play with the hyperparameters to see if you can achieve the benchmark in less episodes!

# Paper

[Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)
[Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/pdf/1706.02275.pdf?source=post_page---------------------------)