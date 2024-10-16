import numpy as np
import matplotlib.pyplot as plt
from Mainframe import *
#from StatisticalExpansion import StatEx
import StatisticalExpansion as STT
#script_dir = os.path.dirname(os.path.realpath(__file__))
#parent_dir = os.path.dirname(script_dir)
#sys.path.append(parent_dir)



print(STT.StatEx(2).Poisson_dist(1,6))





cycles = 700

"""
MarketOpinions = MarketOpinionModel("low",mu= 0)

MarketOpinions.Init_MarketOpinion(0.5)

MarketOpinions.set_evolver("AG")

MarketOpinions.Market_evolver(cycles)

MarketOpinions.muplot()
MarketOpinions.plot_probs()
#Opinions.plot_probs()
"""


"""MarketOpinions = MarketOpinionModel("low",mu= 0)

MarketOpinions.Init_MarketOpinion(0.5)

MarketOpinions.Gaussian_MarketOpinion_evolver(cycles)

MarketOpinions.muplot()
MarketOpinions.plot_probs()
#Opinions.plot_probs()
"""

Stonk = StandardStockModel(200,"low",0)
Stonk.Init_MarketOpinion(1/2)
Stonk.set_evolver("AG")
Stonk.set_asset_evolver("TPTE")



cyc = 365*4-1
datanr = 5
A = Stonk.generate_data(200,-1,datanr,cyc)

t = np.arange(0,cyc+1)

fig, axs = plt.subplots(2)

for i in range(datanr):
    axs[0].plot(t,A[i,:,0], label = f"{i}")

axs[0].grid()
axs[0].legend()

for i in range(datanr):
    axs[1].plot(t,A[i,:,1], label = f"{i}")

plt.legend()
plt.grid()
plt.show()



