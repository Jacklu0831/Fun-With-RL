[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135612-cbff24aa-7d12-11e8-9b6c-2b41e64b3bb0.gif "Trained Agent"

# Deep Q-Network (DQN)

Implementd Deep Q-Learning (DRL) to solve OpenAI Gym's LunarLander environment. The requirement for solving environment is a score of 200, which was achieved in 1672 episodes.

<p align="center">
	<video src="output/result.mov"></video>
</p>

# Model



# Rules

8 states - x, y, x-velo, y-velo, angle, angular-velo, left-leg-contact, right-leg-contact
4 actions - No -ower, left-engine, right-engine, main-engine

Landing pad is always at coordinates (0,0). Coordinates are the first two numbers in state vector. Reward for moving from the top of the screen to landing pad and zero speed is about 100..140 points. If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Solved is 200 points. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt. Four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine. 