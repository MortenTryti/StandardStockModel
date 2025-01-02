import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv
sns.set_theme()
minI = 0
maxI  = 182498394112.0

metaDataPath = "Data/symbols_valid_meta.csv"
dataPath = "Data/stocks/"
directory = os.fsencode(dataPath)
open_list = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    df = pd.read_csv(dataPath+filename)
    open_price_col = np.asarray(df["Open"])

    # Uncomment this to get the max and min values of the open stockprice, not made into if test for performance   
    
    """if np.max(open_price_col)>= maxI:
        maxI = np.max(open_price_col)
        name = filename
    if np.min(open_price_col)<= minI:
        minI = np.min(open_price_col)
        """
    
    open_list.append(open_price_col)
#print(open_list)
#print(minI)
#print(name)
#print(maxI)

# Write the extracted opening prices to file
with open("price_open.txt", "w") as f:
    csv.writer(f, delimiter=' ').writerows(open_list)


 
