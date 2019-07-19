Implemented 3 different TD control methods in this lesson: Sarsa, Sarsamax (Q-learning), Expect Sarsa. Here is what I found.

Similarities:
- Due to the simplicity of the game, all TD control methods converge to the optimal action-value function q* as long as epsilon decays in accordance to GLIE (Greedy in the Limit of Infinite Exploration) conditions and the step-size constant parameter alpha is sufficiently small.

Differences:
- Sarsa and Expected Sarsa are both **on-policy** TD control algorithms, meaning the same e-greedy policy as the one being improved is also used to select the actions.
- On-policy TD control methods have better online performance than off-policy like Sarsamax (more dynamic Q).
- Taken in the account of all action-values and the policy of their state, the Expected Sarsa was able to achieve better performance than Sarsa by finding the optimal action-value function q* faster.