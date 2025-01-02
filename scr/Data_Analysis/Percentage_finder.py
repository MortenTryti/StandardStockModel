import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
"""
In this code we find the discrete probability distribution for percentage asset changes
for three levels of volatility. The data is gathered from the NASDAQ stocks.

"""



dp = 0.5 # Binsizes
pUpper = 14 # Upper value of bin
npoints = int(pUpper/dp) # Number of bins - 1, true number of bins is this and one more truncation bin
binsss = [i*dp for i in range(npoints+1)]
Lowcounter = np.zeros(npoints+1) # Use this if avg % change is below 2.5
Lowhisto = []
Mediumcounter = np.zeros_like(Lowcounter+1) # Use this if avg % change is between 2.5 and 5.0
Mediumhisto = []
Highcounter = np.zeros_like(Lowcounter+1) # Use this if avg % change is above  5.0
Highhisto = []

def percentage_converter(floatList):
    """
    This function converts the raw value data to percentage changes in the asset,
    we need the if test to avoid a division of zero in case of the asset price being zero
    at some time.
    """

    for i in range(len(floatList)-1):
        if floatList[i] == 0:
            p_asset_change = 0
        else:
            p_asset_change = floatList[i+1]/floatList[i]-1
        p_change.append(p_asset_change)
    return p_change 

def historgram_categoriser(number_list, histo_list):
    """
    This function categorises the percentage data into historgram bins so get a discrete probability
    distribution of price changes for an asset
    
    """

    #for loop going through the list of asset percentage change
    for number in number_list:
        # Sorts selected element into the correct bin
        for i in range(npoints):
            if i*dp <= number <= (i+1)*dp:
                histo_list[i] += 1
            elif number > pUpper: # This if test sorts into the upper cap truncation bin
                histo_list[-1] +=1
#TODO make plot of the different stock distributions separatd by volatility

# This is a terrible way to do this, I am so sorry for anyone reading this :)
i = 0
with open("price_open.txt", "r") as f:
    size=len([0 for _ in f])
    
with open("price_open.txt", "r") as infile:
    
    for line in infile:#tqdm(infile,total=size, desc="Loading..." ):
        i+=1
        p_change = []
        #line = infile.readline() 
        floatList = list(map(float,line.split()))
        p_change = percentage_converter(floatList)
        p_change_avg = np.sqrt(np.var(np.array(p_change)))
        """
        Here we separate the stocks into low, medium or high volatility
        """
        if p_change_avg <=0.06:
            historgram_categoriser(p_change,Lowcounter)
            #plt.figure(1)
            #plt.plot(p_change)
            Lowhisto.append(p_change)
        elif 0.06<p_change_avg <=0.12:
            historgram_categoriser(p_change,Mediumcounter)
            #plt.figure(2)
            #plt.plot(p_change)
            Mediumhisto.append(p_change)
        elif 0.12<p_change_avg:
            historgram_categoriser(p_change,Highcounter)
            #plt.figure(3)
            #plt.plot(p_change)
            Highhisto.append(p_change)
#plt.show()
"""
While the three following assets are not used they could be later if we wish to explore the
true distiributions futher as they contain all the percentage changes for each levels. 
"""
plotLowHisto = list(np.concatenate(Lowhisto)) 
plotMediumHisto = list(np.concatenate(Mediumhisto))
plotHighHisto = list(np.concatenate(Highhisto))
plt.hist(Lowhisto,bins=[i*dp for i in range(pUpper)]+[1e37])

print(np.array(Lowcounter)/np.sum(np.array(Lowcounter)))
print(np.array(Mediumcounter)/np.sum(np.array(Mediumcounter)))
print(np.array(Highcounter)/np.sum(np.array(Highcounter)))

        
    