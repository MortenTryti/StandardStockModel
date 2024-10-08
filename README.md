# StandardStockModel
This is my personal hobby project, where I try to model market opinions as a foundation for evaluating stock prices, as well as implementing some tools for statistical analysis.


While I have no formal education in financial markets and capital management they are an interest of mine, which began when I first read the book "Capital in the twenty-first century" by French economist Thomas Piketty. I am actually educated as a theoretical physicist, but find economics to be very interesting! 


## Model example
Examples of what the code currently can produce is shown below in the following two figures. But before we discuss the figures I will briefly mention parts of the motivation behind the model. A well-founded assumption is that when the market opinion goes up it is because investors assume that the financial asset will appreciate in value. Thus, the expectation that the asset will increase in value makes the investors purchase it with the expectation of profit. While this does not necessarily always happen, there are multiple examples of an asset having a high market expectation, but falling short, it still happens most of the time. This discussed behavior has been implemented in my model by the use of stochastic processes. And the asset falling short of expectations is still possible in the model, however, it only happens due to variance and is thus improbable. There are many more behaviors one can discuss, and a great question is if they emerge from the model. An example of what kind of my model has produced is shown below, in the first of the two following images we can see the evolution of the asset market opinion and in the second we can observe the evolution of the market value. This figure displays the behavior we expect most of the time, with an increase in market value



<img src= "scr/figs/probabilities_example.png" width=60% height=60%>

<img src= "scr/figs/stock_example.png" width=60% height=60%>


## Goals
The current goal for this project is to develop tools and methods motivated by the hypothesis that investors and stock prices follow the market opinion of the stock. After all the value of any objects is only as great as what people are willing to pay for it. Hence, being able to model market opinions and how they might impact the stock price is an interesting endeavor.


Another goal is to be able to generate on demand systems to try and utilize statistical and numerical methods to analyze the generated data. It might be possible to create a logistic regression model with the market opinion and price as input to see try and predict if one should buy or sell the financial asset.

## Why develop a data-generation model when there is so much data out there already?
The stock market is vast, and contains a lot of data. So why should the StandardStockModel be developed? There are two answers to this, the first is because I want to, I can both learn a lot from this, in the sense that I can read up on financial theory, statistics and python implementation and gain practical knowledge about it by actually implementing it. The second reason is that the StandardStockModel gives a playground to test out different hypotheses for how market opinions might evolve and how they might influence the stock price.   


## Current methods
The current code is rather new and thus has a very limited number of features. It currently consists of two classes, which will be detailed below.

All current methods work in iterative steps with discrete time. The current model works by updating the market opinion $MO_i$ of the financial asset in question. All member functions of the relevant classes are explained below, but here we give a brief introduction to how the model evolves with time-steps. Note that some assumptions which might not be totally realistic have been made, and these will have to be reviewed as more complexity is added to the model.


At time $t=i$ we have a cumulative market opinion (CMO) $O_i$ of the financial asset which is based on the market's belief on whether the asset will increase in price or not. Then at time-step $t=i+1$ we assume that the CMO changes or stays near constant, in essence this model some real world event/news, which impacts the stock. Examples of such events might be the change of the Baltic Dry Index (BDI), which would impact the market's opinion on a shipping asset, or a very bad event would be Elon Musk tweeting about your company. The impact of this event is then agnostically modelled as us picking a value $X$ from a probability distribution $X\sim P(\vec\theta)$ and updating the opinion as

$$O_{i+1} = O_i + X.$$
As CMO's usually only change slowly and usually continuously one challenge is to find a suitible probability distribution. Where there is a low, but non-zero, probability of picking large values. Elon Musk has tweeted about stocks before, and with the rise of Nvidia and with special cases like GameStop we see clear evidence that rapid CMO change can happen. 

The price is then updated in the following scheme, at $t=i$ we have an asset price $\mathcal V_i$. We then pick from a probability distriubution what the change in price $d\mathcal V$ should be $d\mathcal V\sim P_c(\rho)$. The next step consists of picking if the price should go up and down with the multiplicative factor $\eta$. The probability $P_u$ that $\eta=1$ is directly associatd to the CMU as we set $P_u=O_i$. Then the probability of $\eta=-1$ is $P_d=1-O_i$ as we all know probabilities sum to one. Then we update the asset price as, 

$$\mathcal V_{i+1} = \mathcal V_{i} + \eta d\mathcal V. $$

Finally, after this step we repeat the whole process anew for as many cycles as specified.  

For now, I have modelled the change in price to be a simple probability distribution as there are many factors which can impact this. One is that there might be a limited volume being traded. Perhaps the owners wish to keep the asset and wait for a better price, forcing the buyers to increase the bid if they wish to secure the asset. There are multiple other situations which might impact the change, hence I have chosen for now to put some values which seemed reasonable. A point on the TODO list is to find better values grounded in real life for this. Another point I would like to improve is to combine $C$ and $\eta$ into a single parameter which would be drawn from a probability distribution dependent on $O_i$.   

## Classes

Currently, there are two classes **The MarketOpinionModel class** and **The StandardStockModel class**. The former is used to model the CMO and the latter is used to model the evolution of the asset value. It might be to no surprise that the latter class is actually a daughter class of the former. Thus, it inherits all the methods from the former.

### The MarketOpinionModel class
* Input: (volatility, mu)
    * volatility - Takes values "0", "1" and "2" which signify how volatile the market is by setting the variance of the Gaussian used to update the CMO to a higher value.
    * mu - Sets the median of the Gaussian distribution used to update CMO

As mentioned earlier this class is used to model the cumulative market opinion. In it the two moments $\mu,\sigma^2$ of the Gaussian distribution are set. 

#### Set_mu_by_sigma
* Input: (percentage) - Sets the median of a Gaussian distribution to a percentage of the standard distribution

#### Init_MarketOpinion
* Input: (positive) - Sets the positive opinion of the CMO, should be between 1 and 0.

This method initializes the CMO $O_0$ at $t=0$.  

#### set_evolver
* Input: (evolver) - sets the method function used to evolve the asset value.
    * "G" sets the method as Gaussian_MarketOpinion_evolver
    * "AG" sets the method as Adaptive_Gaussian_MarketOpinion_evolver

This is a member function which sets which method should be used to evolve the asset value.

#### Gaussian_MarketOpinion_evolver
* Input: (nrcycles): This is by default set to one, and this input denotes how many cycles the method should run. It works as,

1. Pick value $X$ from Gaussian $X\sim P(\mu,\sigma)$.
2. If $0<O_i + X<1$ let $O_{i+1}=O_i + X$, else let $O_{i+1} = O_i$.

#### mu_updater
* Input: (regulator) - Default set to two.

This method is a part of the Adaptive_Gaussian_MarketOpinion_evolver function, which is based on having an adaptive value for the median. **Need to explain the motivation for this either here or somewhere else.**

It works with these steps,

1. $\mu = \mu/2$
2. Pick $\Delta\mu\sim P(\theta)$, where $P(\theta)$ is a pre-fixed probability distribution. $\Delta\mu$ signifies the percentage of $\sigma$ our $\mu$ should be linearly shifted by.
3. $\eta\sim P(\{1,-1\})$, where $P(\{1\})=\frac{1}{2}$ and $P(\{-1\}) = \frac{1}{2}$. 
4. $\mu = \mu +\eta \Delta\mu \sigma$.

Main points of improvement is to improve the distribution which $\eta$ is picked from. Should also try to improve the distribution $P(\theta)$.

**Is it obvious what an adaptive $\mu$ actually does in this model or should I explain it? As well as the motivation why it is reasonable and what behavior it tries to model?**

* Tries to model human behavior w.r.t. memory and opinion changes, positive news will increase our opinion over a short amount of time before the improvement stops and the opinion flattens out until the next piece of news arrive. 

#### Adaptive_Gaussian_MarketOpinion_evolver
* Input: (nrcycles) - Default set to one, input is the number of cycles the method runs over. 


1. Pick value $X$ from Gaussian $X\sim P(\mu,\sigma)$.
2. If $0<O_i + X<1$ let $O_{i+1}=O_i + X$, else let $O_{i+1} = O_i$.
3. Updates $\mu$ with **mu_updater** function.

#### plot_probs
* Input: (save,name)
    * Save: Default set to 0, if $\text{save} =1$ then it will save the figure in figs folder as name + ".png".
    * name: Default set to "1". Enter the name you wish to save file as.

This function plots the CMO as a function of discrete time. 


#### muplot
* Input: (save,name)
    * Save: Default set to 0, if $\text{save} =1$ then it will save the figure in figs folder as name + ".png".
    * name: Default set to "1". Enter the name you wish to save file as.

This function plots $\mu$ as a function of discrete time. Only works if using AGMOE.

### The StandardStockModel class
* Input: (InitValue,volatility,mu)
    * InitValue: Sets initial value of financial asset.
    * volatility: Sets volatility in the MarketOpinionModel class.
    * mu: Sets median of the Gaussian used in the MarketOpinionModel class.  

#### price_time_evolve
* Input: (priceCycles) - How many cycles the method should run. Default set to 1.

Method works iteratively as follows,
1. Pick value-change $dV\sim P(\{0.01,0.02,0.03,0.04,0.05\})$, where $P(\{0.01\}) = 0.2,P(\{0.02\}) = 0.3,P(\{0.03\}) = 0.3,P(\{0.04\}) = 0.1,P(\{0.05\}) = 0.1$.
3. Pick $\eta$ factor as $\eta\sim P(\{1,-1\})$ with equal probability for both.
2. $\mathcal V_{i+1} = \mathcal V_i + \eta d\mathcal V$.




Improvements to method: Find some better distribution for picking $d\mathcal V$. Perhaps try a Poisson distribution or exponential decay? Also combine $\eta$ and $d\mathcal V$ such that the value $\eta d\mathcal V$ is taken from one distribution.

#### plot_stonks
* Input: (save,name)
    * Save: Default set to 0, if $\text{save} =1$ then it will save the figure in figs folder as name + ".png".
    * name: Default set to "1". Enter the name you wish to save file as.

Plots asset value as function of discrete time

## Further development

* Implement the GARP strategy and the requirements of the strategy.

* Implement a more realistic event-chain in market opinion models with e.g. quarterly reports and more.

* Update the probability-values in the methods to be more realistic. Should be done by finding proper values from large data-sets of real world financial assets.

* Implement a statistics class for analysis.

* Implement an agent based trading-system for price updates.


