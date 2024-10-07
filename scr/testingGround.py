import numpy as np
import matplotlib.pyplot as plt
from Mainframe import *

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
Stonk.Init_MarketOpinion(0.5)
Stonk.set_evolver("G")
Stonk.price_time_evolve(cycles)
Stonk.plot_probs()
plt.savefig("figs/probabilities_example.pdf")
Stonk.plot_stonks()
plt.savefig("figs/stock_example.pdf")


