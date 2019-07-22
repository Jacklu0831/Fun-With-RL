# Cliff Walking

Implemented 3 different Temporal-Difference control methods in this lesson: Sarsa, Sarsamax (Q-learning), Expected Sarsa to solve the classic cliff walking game. The bot has start at 36 and move to 47 with the optimal path.

## Rules

<p align="center">
  <image src="output/rule.png" width="80%" height="80%">  
</p>

## Sarsa, Sarsamax(Q-learning), and Expected Sarsa

<br> 

<table>
  <tr>
    <th>
      Average Reward
    </th>
    <th>
      State Value Function
    </th>
  </tr>
  <tr>
    <th>
      <p>
        Sarsa
        <image src="output/sarsa.png"></image>
      </p>
    </th>
    <th>
      <p>
        <image src="output/sarsa_policy.png"></image>
      </p>
    </th>
  </tr>
  <tr>
    <th>
      <p>
        Sarsa-Max
        <image src="output/qlearning.png"></image>
      </p>
    </th>
    <th>
      <p>
        <image src="output/qlearning_policy.png"></image>
      </p>
    </th>
  </tr>
  <tr>
    <th>
      <p>
        Expected Sarsa
        <image src="output/expsarsa.png"></image>
      </p>
    </th>
    <th>
      <p>
        <image src="output/expsarsa_policy.png"></image>
      </p>
    </th>
  </tr>
</table>

<br>

Since the cliff walking problem is very simplistic, all three Temporal Difference methods were able to achieve the maximum reward of -13.0. However, by observing the reward vs. epoch graph of each, it could be seen that Expected Sarsa has a kink that the other two do not have. This means that it was able to find the optimal solution faster than the others. The reason why its performance is higher is because instead of taking the e-greedy action or selecting the max value, Expected Sarsa is able to take into account all of the possible next actions and weight their value with respect to the policy.


### Similarities
- Due to the simplicity of the game, all TD control methods converge to the optimal action-value function q* as long as epsilon decays in accordance to GLIE (Greedy in the Limit of Infinite Exploration) conditions and the step-size constant parameter alpha is sufficiently small.

### Differences:
- Sarsa and Expected Sarsa are both **on-policy** TD control algorithms, meaning the same e-greedy policy as the one being improved is also used to select the actions.
- On-policy TD control methods have better online performance than off-policy like Sarsamax.
- Taken in the account of all action-values and the policy of their state, the Expected Sarsa was able to achieve better performance than Sarsa by finding the optimal action-value function q* faster.
