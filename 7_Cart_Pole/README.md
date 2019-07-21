# Cart Pole

<video src="output/result.mp4"></video>

Solved the classic cart pole game on OpenAI Gym with two different **stochastic policy search** techniques: **adaptive noise scaling** and **REINFORCE algorithm**. 

**Adaptive Noise Scaling**
The noise scaling factor is decreased by half every iteration for **exploitation**. However, if the reward did not increase (the hill climbing did not climb higher), then double the noise scaling factor to favor more **exploration**. It is a simple yet robust way to balance exploitation and exploration.

**REINFORCE / Monte Carlo Policy Gradients**
Estimate gradient of stochastic policy search (hill climbing algorithm) by considering multiple gradients. Sum their policy with probability weight to update the policy and maximize the expected return. 