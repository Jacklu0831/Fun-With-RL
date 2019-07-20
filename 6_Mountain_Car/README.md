# Mountain Car

Trained the classic mountain car game on OpenAI Gym with **stochastic policy search** with **cross-entropy method**. It tries 50 random weights with noise, selects the weights with top 20% outcome and average them all, this allows the AI to climb the hill in more precise direction and leverage the extra computation of different weights instead of just choosing the max. 

### Results

<video src="output/result.mp4"></video>