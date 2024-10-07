# StandardStockModel
This is my personal hobby project, where I try to model market opinions as a foundation for evaluating stock prices, as well as implementing some tools for statistical analysis.


While I have no formal education in financial markets and capital management they are an interest of mine, which began when I first read the book "Capital in the twenty-first century" by French economist Thomas Piketty. 

![Image1](/scr/figs/probabilities_example.png "Example of market opinion evolution")


![Image2](/scr/figs/stock_example.png "Corrsponding stock evolution with said market opinion")


### Goals
The current goal for this project is to develop tools and methods motivated by the hypothesis that investors and stock prices follow the market opinion of the stock. After all the value of any objects is only as great as what people are willing to pay for it. Hence, being able to model market opinions and how they might impact the stock price is an interesting endeavor.


Another goal is to be able to generate on demand systems to try and utilize statistical and numerical methods to analyze the generated data. It might be possible to create a logistic regression model with the market opinion and price as input to see try and predict if one should buy or sell the financial asset.

### Why develop a data-generation model when there is so much data out there already?
The stock market is vast, and contains a lot of data. So why should the StandardStockModel be developed? There are two answers to this, the first is because I want to, I can both learn a lot from this, in the sense that I can read up on financial theory, statistics and python implementation and gain practical knowledge about it by actually implementing it. The second reason is that the StandardStockModel gives a playground to test out different hypotheses for how market opinions might evolve and how they might influence the stock price.   


## Current methods
The current code is rather new and thus has a very limited number of features. It currently consists of two classes, which will be detailed below.

All current methods work in iterative steps with discrete time. The current model works by updating the market opinion $MO_i$ of the financial asset in question.

$MO_i\rightarrow MO_{i+1}$

### The MarketOpinionModel class

#### Set_mu_by_sigma

#### Init_MarketOpinion

#### set_evolver

#### Gaussian_MarketOpinion_evolver

#### mu_updater

#### Adaptive_Gaussian_MarketOpinion_evolver

#### plot_probs

#### muplot


### The StandardStockModel class


#### price_time_evolve

#### plot_stonks


## Further development

* Implement the GARP strategy and the requirements of the strategy.

* Implement a more realistic event-chain in market opinion models with e.g. quarterly reports and more.

* Update the probability-values in the methods to be more realistic.

* Implement a statistics class for analysis.

* Implement an agent based trading-system for price updates.


