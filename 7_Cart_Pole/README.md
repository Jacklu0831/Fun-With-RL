<h1 align="center">Cart Pole</h1>

<p align="center">
  <image src="output/result.gif" height="50%" width="50%"></image>
</p>

Solved the [cart pole](https://gym.openai.com/envs/CartPole-v0/) game on OpenAI Gym with two different **stochastic policy search** techniques: **adaptive noise scaling** and the **REINFORCE algorithm**. The goal is to prevent a stick on the car from falling due to torque. 

**Adaptive Noise Scaling**
The noise scaling factor is decreased by half every iteration for better **exploitation** (more precise maximum). However, if the reward did not increase (the hill climbing did not climb higher), the noise scaling factor is doubled to favor more **exploration** (explore other hills). It is a simple yet robust way to balance exploitation and exploration.

**REINFORCE / Monte Carlo Policy Gradients**
Estimate gradient of stochastic policy search (hill climbing algorithm) by considering multiple gradients. Sum their policy with probability weight to update the policy and maximize the expected return. 

# Rules

A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center. 

# Links
[A nice blog on REINFORCE](https://medium.com/@thechrisyoon/deriving-policy-gradients-and-implementing-reinforce-f887949bd63)