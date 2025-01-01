import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv
sns.set_theme()

upper_asset_cap = 5*10e3

minI = 0
maxI  = 182498394112.0
dataPath = "Data/stocks/"
directory = os.fsencode(dataPath)
open_list = []
percentag_list = []
for file in os.listdir(directory):
    percentage_per_stock = []
    filename = os.fsdecode(file)

    df = pd.read_csv(dataPath+filename)
    open_price_col = np.asarray(df["Open"])
    # Upper cutoff on asset considered
    if np.max(open_price_col) < upper_asset_cap:
        plt.plot(open_price_col)
    for i in range(len(open_price_col)-1):
        if open_price_col[i] ==0:
            p_change = 0
        elif open_price_col[i] !=0:    
            p_change = open_price_col[i+1]/open_price_col[i] - 1
        percentage_per_stock.append(p_change)
    percentag_list.append(percentage_per_stock)

plt.ylabel("Asset value [$]")
plt.xlabel("Time [days]")
plt.title(f"Nasdaq asset price evolution 1999-2000, upper asset cap: {upper_asset_cap} $ ")
plt.show()

for elem in percentag_list:
    plt.plot(elem)
plt.title(f"Nasdaq prcentage price change 1999-2000, upper asset cap: {upper_asset_cap} $ ")
plt.ylabel("Percentage price change [$]")
plt.xlabel("Time [days]")
plt.show()

nBins = 100
counter = np.zeros(nBins)
