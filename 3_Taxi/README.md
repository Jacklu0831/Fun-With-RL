Competed Sarsa against Expected Sarsa in the [Taxi_v2](https://gym.openai.com/envs/Taxi-v2/) game provided by OpenAI Gym. The rule is slightly long so please refer to the section 3.1 of [this paper](https://arxiv.org/pdf/cs/9905014.pdf) for it. 

### Scores Board

In 100000 episodes (approx 2.5 mins)

Sarsa       Expected Sarsa
9.270           9.390
9.310           9.375
9.330           9.401
9.284           9.341
9.249           9.383

### Try it Yourself

- `agent.py`: the reinforcement learning agent. 
- `monitor.py`: The `interact` function tests how well the agent learns from interaction with the environment.
- `main.py`: Run this file in the terminal to check the performance of the agent.

Begin by running the following command in the terminal:
```
python main.py
```