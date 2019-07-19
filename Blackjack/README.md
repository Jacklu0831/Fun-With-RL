# Blackjack

My first dip into reinforcement learning is to calculate whether the AI player should draw a card in the game of blackjack under all combinations of states. 

The Monte Carlo Methods were used (tabular) along with several traditional reinforcement learning techniques, including discounted rewards, Q-values, constant alpha (GLIE) MC control, and the epsilon-greedy strategy.

<p align="center">
  <a>
    <image alt="blackjack" src="https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F1051931270%2F960x0.jpg%3Ffit%3Dscale" width="50%" height="50%"></image>
  </a>
</p>

### Rules

- Blackjack is a card game where the goal is to obtain cards that sum to as near as possible to 21 without going over. They're playing against a fixed dealer.
- Face cards (Jack, Queen, King) have point value 10.
- Aces can either count as 11 or 1, and it's called 'usable' at 11.
- This game is placed with an infinite deck (or with replacement).
- The game starts with each (player and dealer) having one face up and one face down card.
- The player can request additional cards (hit=1) until they decide to stop (stick=0) or exceed 21 (bust).
- After the player sticks, the dealer reveals their facedown card, and draws until their sum is 17 or greater. If the dealer goes bust the player wins.
- If neither player nor dealer busts, the outcome (win, lose, draw) is decided by whose sum is closer to 21. The reward for winning is +1, drawing is 0, and losing is -1.
- The observation of a 3-tuple of: the players current sum, the dealer's one showing card (1-10 where 1 is ace), and whether or not the player holds a usable ace (0 or 1).
