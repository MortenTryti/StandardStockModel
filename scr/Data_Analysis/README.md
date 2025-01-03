
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

An example of a distribution we achieve with this code, with a binsize $dV$ of $0.5$ and a upper truncation bin set at $14\%$ and above (this means that it contains all the counts of percentage changes above $14\%$) is shown below in the table.


| Absolute price change (%)    |   Low Volatility  $P$ |   Medium Volatility  $P$ |   High Volatility  $P$ |
|------------------------------|-----------------------|--------------------------|------------------------|
| 0.0-0.5                      |           0.999649    |              0.989509    |            0.890454    |
| 0.5-1.0                      |           0.000231965 |              0.00577546  |            0.0247491   |
| 1.0-1.5                      |           0.000115058 |              0.00456269  |            0.0191302   |
| 1.5-2.0                      |           2.74614e-06 |              7.36341e-05 |            0.000252447 |
| 2.0-2.5                      |           1.23296e-06 |              3.24341e-05 |            0.000212765 |
| 2.5-3.0                      |           2.24175e-07 |              2.19149e-05 |            0.000260046 |
| 3.0-3.5                      |           1.12087e-07 |              7.88937e-06 |            0.000266378 |
| 3.5-4.0                      |           1.12087e-07 |              6.57447e-06 |            0.000138044 |
| 4.0-4.5                      |           0           |              3.50639e-06 |            9.20291e-05 |
| 4.5-5.0                      |           0           |              1.31489e-06 |            9.20291e-05 |
| 5.0-5.5                      |           0           |              1.75319e-06 |            7.30323e-05 |
| 5.5-6.0                      |           0           |              8.76597e-07 |            6.54335e-05 |
| 6.0-6.5                      |           0           |              1.31489e-06 |            7.5143e-05  |
| 6.5-7.0                      |           0           |              8.76597e-07 |            4.89696e-05 |
| 7.0-7.5                      |           0           |              0           |            5.78348e-05 |
| 7.5-8.0                      |           0           |              0           |            4.22152e-05 |
| 8.0-8.5                      |           0           |              4.38298e-07 |            3.25057e-05 |
| 8.5-9.0                      |           0           |              4.38298e-07 |            4.39038e-05 |
| 9.0-9.5                      |           0           |              0           |            3.92601e-05 |
| 9.5-10.0                     |           0           |              0           |            3.29278e-05 |
| 10.0-10.5                    |           0           |              0           |            3.20835e-05 |
| 10.5-11.0                    |           0           |              0           |            3.29278e-05 |
| 11.0-11.5                    |           0           |              0           |            3.92601e-05 |
| 11.5-12.0                    |           0           |              0           |            3.25057e-05 |
| 12.0-12.5                    |           0           |              0           |            7.97867e-05 |
| 12.5-13.0                    |           0           |              0           |            3.50386e-05 |
| 13.0-13.5                    |           0           |              0           |            3.96823e-05 |
| 13.5-14.0                    |           0           |              0           |            5.23468e-05 |
| >14.0                        |           0           |              0           |            0.0634984   |



A more fine detail analysis with an upper cap of $20$ and a binsize of $dp=0.1$ gives the following table rather long table. 
| Absolute price change (%)    |   Low Volatility  $P$ |   Medium Volatility  $P$ |   High Volatility  $P$ |
|------------------------------|-----------------------|--------------------------|------------------------|
| 0.00-0.10                    |           0.983466    |              0.935513    |            0.634877    |
| 0.10-0.20                    |           0.0139604   |              0.04203     |            0.0207607   |
| 0.20-0.30                    |           0.00167849  |              0.00789807  |            0.00458972  |
| 0.30-0.40                    |           0.000403959 |              0.00279163  |            0.00210048  |
| 0.40-0.50                    |           0.000138203 |              0.00125119  |            0.00119335  |
| 0.50-0.60                    |           6.59629e-05 |              0.000709959 |            0.000828491 |
| 0.60-0.70                    |           2.9871e-05  |              0.000333067 |            0.000493194 |
| 0.70-0.80                    |           1.80459e-05 |              0.000188446 |            0.000629389 |
| 0.80-0.90                    |           9.19109e-06 |              0.00011745  |            0.000535971 |
| 0.90-1.00                    |           0.000110685 |              0.0044482   |            0.0159794   |
| 1.00-1.10                    |           0.000108836 |              0.00443286  |            0.0140284   |
| 1.10-1.20                    |           2.80216e-06 |              3.50597e-05 |            5.72457e-05 |
| 1.20-1.30                    |           1.62525e-06 |              3.37449e-05 |            6.32219e-05 |
| 1.30-1.40                    |           1.00878e-06 |              2.89242e-05 |            5.18986e-05 |
| 1.40-1.50                    |           8.40648e-07 |              3.46214e-05 |            5.59876e-05 |
| 1.50-1.60                    |           8.40648e-07 |              2.14741e-05 |            4.65515e-05 |
| 1.60-1.70                    |           8.96691e-07 |              1.79681e-05 |            4.40352e-05 |
| 1.70-1.80                    |           3.36259e-07 |              1.22709e-05 |            2.92519e-05 |
| 1.80-1.90                    |           3.36259e-07 |              7.45018e-06 |            2.64211e-05 |
| 1.90-2.00                    |           3.36259e-07 |              1.49004e-05 |            4.2148e-05  |
| 2.00-2.10                    |           3.92302e-07 |              1.35856e-05 |            4.24625e-05 |
| 2.10-2.20                    |           2.80216e-07 |              6.57369e-06 |            2.17031e-05 |
| 2.20-2.30                    |           2.24173e-07 |              4.82071e-06 |            2.67356e-05 |
| 2.30-2.40                    |           2.24173e-07 |              3.94421e-06 |            3.45991e-05 |
| 2.40-2.50                    |           1.12086e-07 |              3.94421e-06 |            3.36555e-05 |
| 2.50-2.60                    |           0           |              5.6972e-06  |            3.11392e-05 |
| 2.60-2.70                    |           5.60432e-08 |              3.94421e-06 |            2.48484e-05 |
| 2.70-2.80                    |           5.60432e-08 |              6.57369e-06 |            4.34061e-05 |
| 2.80-2.90                    |           0           |              2.62948e-06 |            2.39048e-05 |
| 2.90-3.00                    |           1.12086e-07 |              3.06772e-06 |            7.10854e-05 |
| 3.00-3.10                    |           5.60432e-08 |              3.50597e-06 |            0.00011921  |
| 3.10-3.20                    |           0           |              4.38246e-07 |            1.95013e-05 |
| 3.20-3.30                    |           0           |              1.75298e-06 |            1.91868e-05 |
| 3.30-3.40                    |           5.60432e-08 |              8.76492e-07 |            1.98158e-05 |
| 3.40-3.50                    |           0           |              1.31474e-06 |            2.07594e-05 |
| 3.50-3.60                    |           5.60432e-08 |              2.62948e-06 |            1.95013e-05 |
| 3.60-3.70                    |           0           |              0           |            2.29612e-05 |
| 3.70-3.80                    |           0           |              4.38246e-07 |            1.47832e-05 |
| 3.80-3.90                    |           5.60432e-08 |              1.75298e-06 |            1.00652e-05 |
| 3.90-4.00                    |           0           |              1.75298e-06 |            3.55427e-05 |
| 4.00-4.10                    |           0           |              1.31474e-06 |            2.04449e-05 |
| 4.10-4.20                    |           0           |              8.76492e-07 |            1.41542e-05 |
| 4.20-4.30                    |           0           |              4.38246e-07 |            1.13233e-05 |
| 4.30-4.40                    |           0           |              8.76492e-07 |            1.38396e-05 |
| 4.40-4.50                    |           0           |              0           |            9.12157e-06 |
| 4.50-4.60                    |           0           |              0           |            9.43611e-06 |
| 4.60-4.70                    |           0           |              0           |            1.13233e-05 |
| 4.70-4.80                    |           0           |              8.76492e-07 |            1.2896e-05  |
| 4.80-4.90                    |           0           |              4.38246e-07 |            7.23435e-06 |
| 4.90-5.00                    |           0           |              0           |            2.76793e-05 |
| 5.00-5.10                    |           0           |              4.38246e-07 |            1.50978e-05 |
| 5.10-5.20                    |           0           |              4.38246e-07 |            7.23435e-06 |
| 5.20-5.30                    |           0           |              4.38246e-07 |            1.22669e-05 |
| 5.30-5.40                    |           0           |              0           |            9.12157e-06 |
| 5.40-5.50                    |           0           |              4.38246e-07 |            1.06943e-05 |
| 5.50-5.60                    |           0           |              0           |            1.06943e-05 |
| 5.60-5.70                    |           0           |              0           |            9.12157e-06 |
| 5.70-5.80                    |           0           |              0           |            1.06943e-05 |
| 5.80-5.90                    |           0           |              0           |            9.75065e-06 |
| 5.90-6.00                    |           0           |              8.76492e-07 |            8.4925e-06  |
| 6.00-6.10                    |           0           |              1.31474e-06 |            1.60414e-05 |
| 6.10-6.20                    |           0           |              0           |            9.43611e-06 |
| 6.20-6.30                    |           0           |              0           |            9.43611e-06 |
| 6.30-6.40                    |           0           |              0           |            1.06943e-05 |
| 6.40-6.50                    |           0           |              0           |            1.03797e-05 |
| 6.50-6.60                    |           0           |              4.38246e-07 |            5.03259e-06 |
| 6.60-6.70                    |           0           |              0           |            8.4925e-06  |
| 6.70-6.80                    |           0           |              0           |            8.17796e-06 |
| 6.80-6.90                    |           0           |              4.38246e-07 |            5.66167e-06 |
| 6.90-7.00                    |           0           |              0           |            9.12157e-06 |
| 7.00-7.10                    |           0           |              0           |            1.19524e-05 |
| 7.10-7.20                    |           0           |              0           |            8.4925e-06  |
| 7.20-7.30                    |           0           |              0           |            8.17796e-06 |
| 7.30-7.40                    |           0           |              0           |            9.75065e-06 |
| 7.40-7.50                    |           0           |              0           |            4.71806e-06 |
| 7.50-7.60                    |           0           |              0           |            5.03259e-06 |
| 7.60-7.70                    |           0           |              0           |            7.86343e-06 |
| 7.70-7.80                    |           0           |              0           |            7.86343e-06 |
| 7.80-7.90                    |           0           |              0           |            5.9762e-06  |
| 7.90-8.00                    |           0           |              0           |            5.03259e-06 |
| 8.00-8.10                    |           0           |              0           |            3.77444e-06 |
| 8.10-8.20                    |           0           |              0           |            5.34713e-06 |
| 8.20-8.30                    |           0           |              0           |            4.08898e-06 |
| 8.30-8.40                    |           0           |              0           |            4.08898e-06 |
| 8.40-8.50                    |           0           |              4.38246e-07 |            6.91981e-06 |
| 8.50-8.60                    |           0           |              0           |            8.17796e-06 |
| 8.60-8.70                    |           0           |              0           |            6.29074e-06 |
| 8.70-8.80                    |           0           |              0           |            2.83083e-06 |
| 8.80-8.90                    |           0           |              4.38246e-07 |            3.14537e-06 |
| 8.90-9.00                    |           0           |              0           |            1.22669e-05 |
| 9.00-9.10                    |           0           |              0           |            6.91981e-06 |
| 9.10-9.20                    |           0           |              0           |            6.91981e-06 |
| 9.20-9.30                    |           0           |              0           |            4.40352e-06 |
| 9.30-9.40                    |           0           |              0           |            3.45991e-06 |
| 9.40-9.50                    |           0           |              0           |            7.54889e-06 |
| 9.50-9.60                    |           0           |              0           |            7.86343e-06 |
| 9.60-9.70                    |           0           |              0           |            4.08898e-06 |
| 9.70-9.80                    |           0           |              0           |            4.40352e-06 |
| 9.80-9.90                    |           0           |              0           |            4.08898e-06 |
| 9.90-10.00                   |           0           |              0           |            4.08898e-06 |
| 10.00-10.10                  |           0           |              0           |            3.14537e-06 |
| 10.10-10.20                  |           0           |              0           |            4.71806e-06 |
| 10.20-10.30                  |           0           |              0           |            5.34713e-06 |
| 10.30-10.40                  |           0           |              0           |            5.66167e-06 |
| 10.40-10.50                  |           0           |              0           |            5.03259e-06 |
| 10.50-10.60                  |           0           |              0           |            4.08898e-06 |
| 10.60-10.70                  |           0           |              0           |            5.34713e-06 |
| 10.70-10.80                  |           0           |              0           |            5.34713e-06 |
| 10.80-10.90                  |           0           |              0           |            5.03259e-06 |
| 10.90-11.00                  |           0           |              0           |            4.71806e-06 |
| 11.00-11.10                  |           0           |              0           |            6.29074e-06 |
| 11.10-11.20                  |           0           |              0           |            4.71806e-06 |
| 11.20-11.30                  |           0           |              0           |            5.9762e-06  |
| 11.30-11.40                  |           0           |              0           |            7.54889e-06 |
| 11.40-11.50                  |           0           |              0           |            4.71806e-06 |
| 11.50-11.60                  |           0           |              0           |            4.71806e-06 |
| 11.60-11.70                  |           0           |              0           |            3.14537e-06 |
| 11.70-11.80                  |           0           |              0           |            4.08898e-06 |
| 11.80-11.90                  |           0           |              0           |            5.9762e-06  |
| 11.90-12.00                  |           0           |              0           |            6.29074e-06 |
| 12.00-12.10                  |           0           |              0           |            3.20828e-05 |
| 12.10-12.20                  |           0           |              0           |            3.45991e-06 |
| 12.20-12.30                  |           0           |              0           |            8.4925e-06  |
| 12.30-12.40                  |           0           |              0           |            1.16379e-05 |
| 12.40-12.50                  |           0           |              0           |            3.77444e-06 |
| 12.50-12.60                  |           0           |              0           |            5.66167e-06 |
| 12.60-12.70                  |           0           |              0           |            5.9762e-06  |
| 12.70-12.80                  |           0           |              0           |            6.29074e-06 |
| 12.80-12.90                  |           0           |              0           |            4.08898e-06 |
| 12.90-13.00                  |           0           |              0           |            4.08898e-06 |
| 13.00-13.10                  |           0           |              0           |            1.16379e-05 |
| 13.10-13.20                  |           0           |              0           |            4.71806e-06 |
| 13.20-13.30                  |           0           |              0           |            6.29074e-06 |
| 13.30-13.40                  |           0           |              0           |            1.88722e-06 |
| 13.40-13.50                  |           0           |              0           |            5.03259e-06 |
| 13.50-13.60                  |           0           |              0           |            3.14537e-06 |
| 13.60-13.70                  |           0           |              0           |            5.34713e-06 |
| 13.70-13.80                  |           0           |              0           |            3.77444e-06 |
| 13.80-13.90                  |           0           |              0           |            1.76141e-05 |
| 13.90-14.00                  |           0           |              0           |            9.12157e-06 |
| 14.00-14.10                  |           0           |              0           |            5.66167e-06 |
| 14.10-14.20                  |           0           |              0           |            3.77444e-06 |
| 14.20-14.30                  |           0           |              0           |            9.43611e-07 |
| 14.30-14.40                  |           0           |              0           |            2.5163e-06  |
| 14.40-14.50                  |           0           |              0           |            2.20176e-06 |
| 14.50-14.60                  |           0           |              0           |            2.5163e-06  |
| 14.60-14.70                  |           0           |              0           |            2.83083e-06 |
| 14.70-14.80                  |           0           |              0           |            1.25815e-06 |
| 14.80-14.90                  |           0           |              0           |            4.08898e-06 |
| 14.90-15.00                  |           0           |              0           |            3.45991e-06 |
| 15.00-15.10                  |           0           |              0           |            3.45991e-06 |
| 15.10-15.20                  |           0           |              0           |            3.45991e-06 |
| 15.20-15.30                  |           0           |              0           |            2.5163e-06  |
| 15.30-15.40                  |           0           |              0           |            9.43611e-07 |
| 15.40-15.50                  |           0           |              0           |            1.57269e-06 |
| 15.50-15.60                  |           0           |              0           |            2.20176e-06 |
| 15.60-15.70                  |           0           |              0           |            1.2896e-05  |
| 15.70-15.80                  |           0           |              0           |            9.43611e-07 |
| 15.80-15.90                  |           0           |              0           |            2.5163e-06  |
| 15.90-16.00                  |           0           |              0           |            1.88722e-06 |
| 16.00-16.10                  |           0           |              0           |            4.40352e-06 |
| 16.10-16.20                  |           0           |              0           |            2.83083e-06 |
| 16.20-16.30                  |           0           |              0           |            1.88722e-06 |
| 16.30-16.40                  |           0           |              0           |            2.20176e-06 |
| 16.40-16.50                  |           0           |              0           |            4.08898e-06 |
| 16.50-16.60                  |           0           |              0           |            3.14537e-06 |
| 16.60-16.70                  |           0           |              0           |            4.71806e-06 |
| 16.70-16.80                  |           0           |              0           |            2.83083e-06 |
| 16.80-16.90                  |           0           |              0           |            3.77444e-06 |
| 16.90-17.00                  |           0           |              0           |            4.08898e-06 |
| 17.00-17.10                  |           0           |              0           |            5.34713e-06 |
| 17.10-17.20                  |           0           |              0           |            2.83083e-06 |
| 17.20-17.30                  |           0           |              0           |            3.77444e-06 |
| 17.30-17.40                  |           0           |              0           |            2.20176e-06 |
| 17.40-17.50                  |           0           |              0           |            2.83083e-06 |
| 17.50-17.60                  |           0           |              0           |            2.83083e-06 |
| 17.60-17.70                  |           0           |              0           |            1.57269e-06 |
| 17.70-17.80                  |           0           |              0           |            4.08898e-06 |
| 17.80-17.90                  |           0           |              0           |            3.45991e-06 |
| 17.90-18.00                  |           0           |              0           |            2.5163e-06  |
| 18.00-18.10                  |           0           |              0           |            2.20176e-06 |
| 18.10-18.20                  |           0           |              0           |            5.03259e-06 |
| 18.20-18.30                  |           0           |              0           |            3.14537e-06 |
| 18.30-18.40                  |           0           |              0           |            4.08898e-06 |
| 18.40-18.50                  |           0           |              0           |            5.9762e-06  |
| 18.50-18.60                  |           0           |              0           |            1.88722e-06 |
| 18.60-18.70                  |           0           |              0           |            3.77444e-06 |
| 18.70-18.80                  |           0           |              0           |            1.88722e-06 |
| 18.80-18.90                  |           0           |              0           |            1.57269e-06 |
| 18.90-19.00                  |           0           |              0           |            1.88722e-06 |
| 19.00-19.10                  |           0           |              0           |            4.08898e-06 |
| 19.10-19.20                  |           0           |              0           |            2.5163e-06  |
| 19.20-19.30                  |           0           |              0           |            2.83083e-06 |
| 19.30-19.40                  |           0           |              0           |            2.83083e-06 |
| 19.40-19.50                  |           0           |              0           |            1.25815e-06 |
| 19.50-19.60                  |           0           |              0           |            1.88722e-06 |
| 19.60-19.70                  |           0           |              0           |            2.20176e-06 |
| 19.70-19.80                  |           0           |              0           |            2.20176e-06 |
| 19.80-19.90                  |           0           |              0           |            2.20176e-06 |
| 19.90-20.00                  |           0           |              0           |            1.88722e-06 |
| >20.00                       |           0           |              0           |            0.301956    |


Having found the current distributions the next question is how do we deal with picking which value the financial asset should move by? After all we only have the probability that the asset price $V $  should move in between some value in the interval of the percentage change chosen. So if we from the probability distribution pick that it should change by a percentage within some interval $[p_i,p_i+ dp]$   where $dp$ is the binsize then the new value of the asset could move to a value within the interval $$\mathcal V =[V(1-p_i-dp),V(1-p_i)]\cup[V(1+p_i),V(1+p_i+dp)].$$

 * **Problem** We have however, at this point no current method for finding what value the new asset price actually moves to. There are however, multiple solutions to this problem, and we present one of them here:
 
 * **Solution** If we go with the Bayesian perspective, since we have no information on what the new asset price should actually be, expect that it should be in the interval $\mathcal V$ we argue that any value in the interval is as good as any other, hence we can pick the new value from a uniform distribution of the aforementioned interval. However, as the StandardStockModel already contains a method for deciding if the price goes up or down, we should simply pick a value chang using a uniform distribution from the interval $$ \mathcal P_+ =[p_i,p_i+dp],$$
    and find the new asset price $V_{i+1}$ as 
    $$V_{i+1} = V_i(1+\eta dV),$$
    where:
    * $V_i$ is the current asset price,
    * $\eta$ is either $\pm1$ and is drawn from the cumulative market opinion,
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




