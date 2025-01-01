# README

Current attempt to take a database of stock prices from NASDAQ from about 1999 to 2020 from [here](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data) and find reasonable percentage price changes for different levels of stock volatility.



### Volatility markers
The current markers are set arbitrarily and could definitely be improved by actual expertise in the field of measures of stock volatility.
*  **Low volatility:** $<2.5\%$ avg price change of financial asset.
* **Medium volatility:** Between $2.5\%$ to $5.0\%$ avg price change of financial asset.
* **High volatility:** Above $5.0\%$ avg price change of financial asset.

The following table shows the probability distributions I have obtained from my analysis of the NASDAQ dataset.


| Price change %      | Low volatility      |   Medium volatility        |     High volatility |
| ------------- | ------------- |    -------------  | -----    |
| 0.0 |9.99272949e-01  | 9.69457014e-01 | 5.57712487e-01 |
| 0.5 | 4.79808944e-04 | 8.20135747e-03   | 3.63551570e-03|
| 1.0 |  9.39519508e-05 |  2.87518854e-03   |2.76638367e-03|
| 1.5 | 3.07856138e-05 |  1.31975867e-03  | 1.28249971e-03 |
| 2.0 |1.54725624e-05  |  7.07013575e-04 | 1.01222084e-03 |
| 2.5 |6.85897094e-06  |2.35671192e-04 | 8.58532863e-04  |
| 3.0 |  4.62581761e-06 | 1.88536953e-04  |1.09701421e-03|
| 3.5 | 2.55217523e-06 |  1.41402715e-04  | 7.89638250e-04|
| 4.0 | 1.11657667e-06 |  2.82805430e-04 |5.40557728e-04|
| 4.5 | 9.57065713e-07 | 0.00000000e+00 | 7.52541151e-04|
| 5.0 |  1.75462047e-06 | 0.00000000e+00 | 4.61063945e-04|
| 5.5 |  6.38043809e-07 |9.42684766e-05 |3.07375963e-04|
| 6.0 |  7.97554761e-07 | 2.35671192e-04  |3.39173477e-04|
| 6.5 | 9.57065713e-07 |4.71342383e-05 | 2.64979279e-04|
| 7.0 | 6.38043809e-07 |  1.41402715e-04  |3.76270576e-04 |
| 7.5 | 3.19021904e-07 | 4.71342383e-05 |2.80878035e-04|
| 8.0 | 7.97554761e-07 | 0.00000000e+00 |  2.33181765e-04|
| 8.5 | 1.27608762e-06 | 4.71342383e-05  | 2.86177621e-04 |
| 9.0 |6.38043809e-07  | 4.71342383e-05  | 3.07375963e-04 |
| 9.5 | 0.00000000e+00 |0.00000000e+00 |2.38481351e-04|
| 10.0 | 4.78532857e-07 | 0.00000000e+00  | 1.96084666e-04 |
| 10.5 |0.00000000e+00 | 0.00000000e+00  |2.49080522e-04 |
| 11.0 |6.38043809e-07  | 9.42684766e-05 | 2.54380107e-04 |
| 11.5 | 3.19021904e-07 | 0.00000000e+00 | 2.86177621e-04 |
| 12.0 | 1.59510952e-07 | 0.00000000e+00 | 8.47933692e-04 |
| 12.5 | 4.78532857e-07 |0.00000000e+00 |2.22582594e-04|
| 13.0 | 4.78532857e-07 |  0.00000000e+00 |2.11983423e-04|
| 13.5 |  1.59510952e-07 | 0.00000000e+00 |2.43780936e-04|
| <14.0 | 8.03935199e-05 | 1.58371041e-02 | 4.23945647e-01 |




### Notes
* I am not sure that this is a good way of gauging volatility of some financial asset, but as of now it is good enough. 
* It is a bit strange that there is a range of zero values at the tail of the medium volatility distribution, but at this point I simply have to trust the data. Additionally, it is reassuring to see that the $<14\%$ probability goes up for higher volatility. 