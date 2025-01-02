
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

The following table shows the probability distributions I have obtained from my analysis of the NASDAQ dataset. By the letter $P$ we mean probability distribution.


| Price change (%)      | Low Volatility  $P$     |   Medium Volatility $P$        |     High Volatility $P$ |
| ------------- | ------------- |    -------------  | -----    |
| 0.0 |9.99860713e-01  | 9.97729350e-01 | 9.01952363e-01 |
| 0.5 | 1.22894428e-04 | 1.77354594e-03   | 2.24995760e-03|
| 1.0 |  1.17987004e-05 |  3.08367025e-04   |8.62646433e-04|
| 1.5 | 2.71474522e-06 |   9.64009910e-05  |  3.80076894e-04 |
| 2.0 |1.25295933e-06  |  4.00702914e-05 | 3.16629066e-04 |
| 2.5 |3.13239833e-07  |2.26484256e-05 | 3.83127270e-04  |
| 3.0 |  2.08826556e-07 | 9.29166178e-06  |3.86177647e-04|
| 3.5 | 1.04413278e-07 |  7.54947520e-06  | 2.01324839e-04|
| 4.0 | 0.00000000e+00 |  4.06510203e-06 |1.33606484e-04|
| 4.5 | 0.00000000e+00 | 1.16145772e-06 | 1.33606484e-04|
| 5.0 |  0.00000000e+00 | 2.32291544e-06 | 1.05543022e-04|
| 5.5 |  0.00000000e+00 |1.16145772e-06 |9.45616670e-05|
| 6.0 |  0.00000000e+00 | 1.74218658e-06  |1.08593398e-04|
| 6.5 | 0.00000000e+00 |1.16145772e-06 | 7.07687314e-05|
| 7.0 | 0.00000000e+00 |  0.00000000e+00  |8.35803121e-05 |
| 7.5 | 0.00000000e+00 | 0.00000000e+00 |6.10075271e-05|
| 8.0 | 0.00000000e+00 | 5.80728861e-07 |  4.69757959e-05|
| 8.5 | 0.00000000e+00 | 5.80728861e-07  | 6.34478282e-05 |
| 9.0 |0.00000000e+00  |  0.00000000e+00  | 5.67370002e-05 |
| 9.5 | 0.00000000e+00 |0.00000000e+00 |4.75858711e-05|
| 10.0 | 0.00000000e+00 | 0.00000000e+00  | 4.63657206e-05 |
| 10.5 |0.00000000e+00 | 0.00000000e+00  |4.75858711e-05 |
| 11.0 |0.00000000e+00  |  0.00000000e+00 | 5.67370002e-05 |
| 11.5 | 0.00000000e+00 | 0.00000000e+00 | 4.69757959e-05 |
| 12.0 | 0.00000000e+00 | 0.00000000e+00 | 1.15304226e-04 |
| 12.5 | 0.00000000e+00 |0.00000000e+00 |5.06362475e-05|
| 13.0 | 0.00000000e+00 |  0.00000000e+00 |5.73470755e-05|
| 13.5 |  0.00000000e+00 | 0.00000000e+00 |7.56493336e-05|
| <14.0 | 0.00000000e+00 |  0.00000000e+00 | 9.17650820e-02 |




### Notes and Observations
1. **Volatility Measurement:** 
    - The current thresholds are arbitrary and can benefit from domain expertise for refinement.
    - Adjusting thresholds would require recalculating the distributions.

2. **Data Irregularities:**
    - Anomalies such as assets with only a single price point may cause errors in variance calculation.

3. **High Volatility Distributions:**
    - Contrary to expectations, the high volatility distribution suggests a behavior that might either reflect the dataset's reality or issues in data preprocessing.

---



## How I obtained these results
For any programmers reading this, this is essentially the true README as I will explain how to run the python programs as well as what is needed to do manually in order to obtain the same probability distributions as I have. There are four steps as follows:

1. First and foremost you need to run ``` Kaggle_Data_import.py ``` as this imports the NASDAQ dataset. 

2. Then secondly, as I was lazy I simply copy/pasted the data from where Kaggle imports it to locally on my computer to the folder DATA in this repository. 

3. Thirdly you must run ``` Data_format.py ``` to extract the open prices for each asset and write it to a .txt file, reducing the time it takes to actually extract and do something useful with this data. 

4. Then we are finally ready to run ``` Percentage_finder.py ```, after running this it will output the probability distributions for the different levels of volatility. These are all the steps really needed. When running this program an error message will appear, this is due to the irregularity of the data, in the sense that there is one asset which only contains one open price. Thus calculating the variance really makes little sense. 




