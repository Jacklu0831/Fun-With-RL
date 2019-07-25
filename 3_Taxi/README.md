# Taxi

<p align="center">
  <image src="output/taxi_visual.gif" height="15%" width="15%"></image>
</p>

In this [Taxi_v2](https://gym.openai.com/envs/Taxi-v2/) game provided by OpenAI Gym, the taxi learns to navigate toward the passenger at a randomly generated spot, pick the passenger up, navigate to a randomly assigned destination, then put down the passenger. While training the agent, I competed **Sarsa** against **Expected Sarsa**. Below are the scores achieved by each **on-policy methods**, instructions on running the project yourself, and rules of the game.

### Scores Board

100000 episodes.

<pre>
Trial      Sarsa    Expected Sarsa
  1        9.270        9.390
  2        9.310        9.375
  3        9.330        9.401
  4        9.284        9.341
  5        9.249        9.383
</pre>

As can be seen, Expected Sarsa is able to consistently achieve higher scores than Sarsa. This is because instead of randomly choosing one action with the **Epsilon-Greedy** policy then estimate the respective value (V), Expected Sarsa estimates the state value (V) by taking the dot product of different action values (Q) and the probability of taking each action from the policy. This way, it is able get more information of the result in taking different actions, thus making each episode more "valuable" and achieve higher scores in the same given time. 

### Try it Yourself

- `agent.py`: the reinforcement learning agent. 
- `monitor.py`: The `interact` function tests how well the agent learns from interaction with the environment.
- `main.py`: Run this file in the terminal to check the performance of the agent.

Begin by running the following command in the terminal:
```
python main.py
```

### Rules 

From [this paper](https://arxiv.org/pdf/cs/9905014.pdf):

a 5-by-5 grid world inhabited by a taxi agent. There are 4 specially-designated locations in this world, marked as R(ed), B(lue), G(reen), and Y(ellow). The taxi problem is episodic. In each episode, the taxi starts in a randomly-chosen square. There is a passenger at 1 of the 4 locations (chosen randomly), and that passenger wishes to be transported to 1 of the 4 locations (also chosen randomly). The taxi must go to the passenger’s location (the “source”), pick up the passenger, go to the destination location (the “destination”), and put down the passenger there. (To keep things uniform, the taxi must pick up and drop off the passenger even if he/she is already located at the destination!) The episode ends when the passenger is deposited at the destination location.

There are six primitive actions in this domain: (a) 4 navigation actions that move the taxi 1 square North, South, East, or West, (b) a Pickup action, and (c) a Putdown action. Each action is deterministic. There is a reward of −1 for each action and an additional reward of +20 for successfully delivering the passenger. There is a reward of −10 if the taxi attempts to execute the Putdown or Pickup actions illegally. If a navigation action would cause the taxi to hit a wall, the action is a no-op, and there is only the usual reward of −1. We seek a policy that maximizes the total reward per episode. There are 500 possible states: 25 squares, 5 locations for the passenger (counting the 4 starting locations and the taxi), and 4 destinations.

This task has a simple hierarchical structure in which there are two main sub-tasks: Get
the passenger and Deliver the passenger. Each of these subtasks in turn involves the subtask
of navigating to 1 of the 4 locations and then performing a Pickup or Putdown action