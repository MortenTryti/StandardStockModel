import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.special


class StatEx:
    def __init__(self,var) -> None:
        self.var = var


    def finite_uniform_dist(self,input_array) -> np.array:
        # For a finite array, this function assigns a probability for each array element which is equally large
        return np.ones_like(input_array)/len(input_array)

    def Poisson_dist(self,lam,k_max) -> np.array:
        # Should return a Poisson distribution
        poisson = []
        
        # Fills the empty list with a Poisson distribution
        for k in range(k_max):
            P_k = lam**k *np.exp(-lam)/scipy.special.factorial(k) 
            poisson.append(P_k)

        return np.array(poisson)

