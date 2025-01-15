
# NASDAQ Probability Distributions for Daily Stock Price Changes

This project analyzes a NASDAQ stock price dataset (1999–2020) to determine the probability distributions of percentage price changes across different levels of stock volatility. The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data).

In this analysis, **volatility** refers to **daily volatility**, categorized into three tiers: **low**, **medium**, and **high**. Volatility is measured as the standard deviation of daily stock prices.

---


## Volatility Definition and Calculation
Volatility $V$ is calculated using the formula:

When discussing stock volatility I will from this point out refer to the **daily volatility** as simply **volatility**. Further I will create three categories **Low, medium** and **high volatility**, where the different markers can be found below. In finance when we refer to the volatility what we actually mean is the square root of the variance, hence for a stock $S$, given a dataset $D$ of $n$ subsequent daily stock prices of $S$ the volatility $V$ for the given stock is simply

$$V = \sqrt{Var(D)} = \sqrt{\frac{1}{n-1}\sum_{i=1}^n \left(D_i- \hat D\right)^2},$$

Where again:
- $D$: Dataset of daily stock prices
- $\hat{D}$: Mean of the dataset
- $D_i$: Price on the $i^{th}$ day
- $n$: Number of daily prices in the dataset.





### Volatility thresholds 
The current thresholds are set arbitrarily and could definitely be improved by actual expertise in the field of measures of stock volatility.
*  **Low volatility:** $V \leq 6\%$ volatility of financial asset.
* **Medium volatility:** $6\% < V \leq 12\%$ volatility of financial asset.
* **High volatility:** $12\%<V$ volatility of financial asset.


## Results: NASDAQ Probability Distributions

The following table shows the probability distributions I have obtained from my analysis of the NASDAQ dataset. By the letter $P$ we mean probability distribution. 

Additionally note that these distributions are the distributions for an **absolute change** this means that in each of the bins we count both a positive and negative change of value. This is due to the fact that in the **StandardStockModel** it is the cumulative market opinion which decides if the price goes up or down.

An example of a distribution we achieve with this code, with a binsize $dV$ of $5\%$ and a upper truncation bin set at $100\%$ and above (this means that it contains all the counts of percentage changes above $100\%$ price change) is shown below in the table.

| Absolute price change (%)    |   Low Volatility  $P$ |   Medium Volatility  $P$ |   High Volatility  $P$ |
|------------------------------|-----------------------|--------------------------|------------------------|
| 0.00-0.05                    |           0.921148    |              0.720204    |            0.61449     |
| 0.05-0.10                    |           0.0613311   |              0.165584    |            0.0862324   |
| 0.10-0.15                    |           0.0114103   |              0.0517492   |            0.028652    |
| 0.15-0.20                    |           0.00337276  |              0.0219166   |            0.0138793   |
| 0.20-0.25                    |           0.00117677  |              0.00880191  |            0.00639923  |
| 0.25-0.30                    |           0.000564378 |              0.00607483  |            0.00533768  |
| 0.30-0.35                    |           0.000274221 |              0.0034886   |            0.00371056  |
| 0.35-0.40                    |           0.000147761 |              0.00194831  |            0.00204284  |
| 0.40-0.45                    |           8.43757e-05 |              0.00133673  |            0.00165516  |
| 0.45-0.50                    |           4.87894e-05 |              0.000773325 |            0.00130034  |
| 0.50-0.55                    |           4.15174e-05 |              0.000942348 |            0.00162035  |
| 0.55-0.60                    |           2.34663e-05 |              0.000487985 |            0.000781171 |
| 0.60-0.65                    |           1.70711e-05 |              0.000359855 |            0.000692226 |
| 0.65-0.70                    |           1.28936e-05 |              0.000311693 |            0.00079664  |
| 0.70-0.75                    |           9.48968e-06 |              0.000204463 |            0.000685459 |
| 0.75-0.80                    |           7.94245e-06 |              0.00017084  |            0.0012056   |
| 0.80-0.85                    |           5.41531e-06 |              0.000134491 |            0.000799541 |
| 0.85-0.90                    |           4.0228e-06  |              0.000105412 |            0.000835312 |
| 0.90-0.95                    |           3.09446e-06 |              7.2698e-05  |            0.00156428  |
| 0.95-1.00                    |           2.11455e-06 |              6.54282e-05 |            0.00472473  |
| >1.00                        |           0.000314604 |              0.0152666   |            0.222595    |


This example illustrates well the shift in the probability distributions as the volatility increases. The  distribution which will be use in the **StandardStockModel** will however, be more fine grained and have a larger upper truncation bin. I have not included such a distribution in this README as it would be too large and difficult to read. These distributions are however, for my computer, costly to calculate, and since I only need the distribution once, I will not optimize the code.

Having found the current distributions the next question is how do we deal with picking which value the financial asset should move by? After all we only have the probability that the asset price $V $  should move in between some value in the interval of the percentage change chosen. So if we from the probability distribution pick that it should change by a percentage within some interval $[p_i,p_i+ dp]$   where $dp$ is the binsize then the new value of the asset could move to a value within the interval $$\mathcal V =[V(1-p_i-dp),V(1-p_i)]\cup[V(1+p_i),V(1+p_i+dp)].$$

 * **Problem** We have however, at this point no current method for finding what value the new asset price actually moves to. There are however, multiple solutions to this problem, and we present one of them here:
 
 * **Solution** If we go with the Bayesian perspective, since we have no information on what the new asset price should actually be, expect that it should be in the interval $\mathcal V$ we argue that any value in the interval is as good as any other, hence we can pick the new value from a uniform distribution of the aforementioned interval. However, as the StandardStockModel already contains a method for deciding if the price goes up or down, we should simply pick a value change using a uniform distribution from the interval
 
   $$\mathcal{P_+} =[p_i,p_i+dp]$$
 
    and find the new asset price $V_{i+1}$ as 
 
    $$V_{i+1} = V_i(1+\eta dV),$$ 
 
    where:

    * $V_i$ is the current asset price,
    *  $\eta$ is either $\pm1$ and is drawn from the cumulative market opinion,
    * $dV$ is the percentage drawn from the interval $\mathcal P_+$ which itself is drawn from the NASDAQ probability distribution shown in the tables above.


There are some notes on the probability distributions which I would like to mention before we proceed to the actual README section.

---
### Notes and Observations
1. **Volatility Measurement:** 
    - The current thresholds are arbitrary and can benefit from domain expertise for refinement.
    - Adjusting thresholds would require recalculating the distributions.

2. **Data Irregularities:**
    - Anomalies such as assets with only a single price point may cause errors in variance calculation.

3. **High Volatility Distributions:**
    - Contrary to expectations, the high volatility distribution suggests a behavior that might either reflect the dataset's reality or issues in data preprocessing.





## How I obtained these results
For any programmers reading this, this is essentially the true README as I will explain how to run the python programs as well as what is needed to do manually in order to obtain the same probability distributions as I have. There are four steps as follows:

1. First and foremost you need to run ``` Kaggle_Data_import.py ``` as this imports the NASDAQ dataset. 

2. Then secondly, as I was lazy I simply copy/pasted the data from where Kaggle imports it to locally on my computer to the folder DATA in this repository. 

3. Thirdly you must run ``` Data_format.py ``` to extract the open prices for each asset and write it to a .txt file, reducing the time it takes to actually extract and do something useful with this data. 

4. Then we are finally ready to run ``` Percentage_finder.py ```, after running this it will output the probability distributions for the different levels of volatility. These are all the steps really needed. When running this program an error message will appear, this is due to the irregularity of the data, in the sense that there is one asset which only contains one open price. Thus calculating the variance really makes little sense. 




