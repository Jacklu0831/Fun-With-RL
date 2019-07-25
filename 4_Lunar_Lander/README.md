# Lunar Lander

<p align="center">
	<image src="output/result.gif"></image>
</p>

Implemented Deep Q-Learning (DRL) to solve OpenAI Gym's LunarLander environment. The requirement for solving environment is a score of 200, which was achieved in ~1600 episodes. The agent's goal is to land inside the center area with a left, right, and down propulsiion system. In this project, I got to learn and successfully implement **Deep Q-Learning, Deep Neural Networks, and the Replay Buffer method**. I learned these from blogs and paper, links in below.

# Model

The neural network has 8 input neurons (size of state), 4 output neurons (size of actions), and two fully-connected hidden layers each with 64 neurons.

# Rules

8 states - x, y, x-velo, y-velo, angle, angular-velo, left-leg-contact, right-leg-contact
4 actions - No -ower, left-engine, right-engine, main-engine

Landing pad is always at coordinates (0,0). Coordinates are the first two numbers in state vector. Reward for moving from the top of the screen to landing pad and zero speed is about 100..140 points. If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Solved is 200 points. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt. Four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine. 

# Papers
- [Human-Level Control through Deep Reinforcement Learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)
- [Deep Reinforcement Learning with Double Q-Learning](https://arxiv.org/abs/1509.06461)