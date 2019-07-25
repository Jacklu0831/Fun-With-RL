<h1 align="center">Mountain Car</h1>

<p align="center">
  <image src="output/result.gif" width="80%" height="80%"></image>
</p>

Trained the [mountain car game](https://gym.openai.com/envs/MountainCar-v0/) in OpenAI Gym with **stochastic policy search** with **cross-entropy method**. The goal is to drive up the hill on the right with built-up momentum. The simple **Deep Q-Network** maps 2 states to 3 actions with one 16-neuron fully-connected hidden layer. 

The agent tries 50 random weights with noise, selects the weights with top 20% outcome and average them all, this allows the AI to climb the hill in more accurate direction and leverage the extra computation of different weights instead of just choosing the max yielded value. The environment was solved in just 47 iterations/episodes. 

# Rules

A car is on a one-dimensional track, positioned between two "mountains". The goal is to drive up the mountain on the right; however, the car's engine is not strong enough to scale the mountain in a single pass. Therefore, the only way to succeed is to drive back and forth to build up momentum. For more details, visit [here](https://github.com/openai/gym/wiki/MountainCar-v0).