import numpy as np
import matplotlib.pyplot as plt


class MarketOpinionModel:
    def __init__(self,volatility,mu):
        """
        INPUT:
            volatility: "low", "moderate" and "high"
            mu_shift: Any value, shifts the median as a percentage of the standard deviation, 
                      good values are between -1 and 1. Higher values also work.
        
        """
        # To store the probability values
        self.buychanceList = []
        self.NobuychanceList = []
        #volatility parameter should either be "low", "moderate" or "high"
        if volatility == "low":
            self.Market_volatility = 0
        elif volatility == "medium":
            self.Market_volatility = 1
        elif volatility == "high":
            self.Market_volatility = 2
        else:
            raise ValueError("Assigned bad value to volatility. Should be strings low, medium or high.")
        
        #Pick mean and standard deviation for normal distribution
        self.sigma = 0.001 *10**(self.Market_volatility)
        self.mu = mu
        #To store the values of mu if it updates
        self.mulist = [self.mu]
    
    # Function to set mu as a percentage of sigma
    def set_mu_by_sigma(self,percentage) -> None:
        self.mu = percentage*self.sigma

    # Initialises the probability distribution of the investors in the market
    def Init_MarketOpinion(self,positive) -> None:
        #Initialises probability values, bound on positive is 0<= positive <= 1
        if 0>positive or positive >1:
            raise ValueError("Assigned bad value to positive, should be between 0 or 1")
        self.buyprob = positive
        self.nobuyprob = 1-positive

        #Appends values to list
        self.buychanceList.append(self.buyprob)
        self.NobuychanceList.append(self.nobuyprob)

    def set_evolver(self,evolver) -> None:
        if evolver == "G":
            self.Market_evolver = self.Gaussian_MarketOpinion_evolver
        elif evolver == "AG":
            self.Market_evolver = self.Adaptive_Gaussian_MarketOpinion_evolver

    #Updates the probability distribution/opinion of the market 
    def Gaussian_MarketOpinion_evolver(self,nrcycles=1) -> None:

        #Pick mean and standard deviation for normal distribution
        mu, sigma =self.mu,self.sigma
        
        #Run the cycles
        if nrcycles == 1:
            #Picks random variable from normal distribution
            self.randVar = np.random.normal(mu,sigma) 
            
            #If test is to make sure we do not go over 1 or below 0 as this would be non-sensical for a probability
            if self.buyprob + self.randVar <1 and self.buyprob + self.randVar >0:
                #Update values
                self.buyprob += self.randVar
                self.nobuyprob = 1-self.buyprob
            #Append values
            self.buychanceList.append(self.buyprob)
            self.NobuychanceList.append(self.nobuyprob)
        elif nrcycles>1:
            for i in range(nrcycles):
                #Picks random variable from normal distribution
                self.randVar = np.random.normal(mu,sigma)
                if self.buyprob + self.randVar <1 and self.buyprob + self.randVar >0:
                    #Update values 
                    self.buyprob += self.randVar
                    self.nobuyprob = 1-self.buyprob
                #Append values
                self.buychanceList.append(self.buyprob)
                self.NobuychanceList.append(self.nobuyprob)
    
    #Should update the mu value
    def mu_updater(self,regulator = 2) -> None:
        # We first regulate mu,
        self.mu = self.mu/regulator
        #This list contains the percentage of the std that mu is going to move
        mu_list = [0,0.005,0.01,0.015,0.02,0.025,0.1,0.2]
        # This list contains the probability of picking an item in mu_list
        list_prob = [0.50,0.195,0.1,0.1,0.05,0.05,0.0025,0.0025]
        #Picking the element of mu_list
        mu_update = np.random.choice(mu_list,p = list_prob)
        #An if test to reduce numbers of calculations in case 0 is picked
        if mu_update != 0:
            # Picking if it is to go up or down
            updown = np.random.choice([-1,1], p = [0.5,0.5])
            #Updating mu with a fixed percentage of the standard deviation
            self.mu += updown * mu_update*self.sigma
        self.mulist.append(self.mu)



    def Adaptive_Gaussian_MarketOpinion_evolver(self,nrcycles = 1) -> None:
        #Run the cycles
        if nrcycles == 1:
            #Picks random variable from normal distribution
            self.randVar = np.random.normal(self.mu,self.sigma) 
            #If test is to make sure we do not go over 1 or below 0 as this would be non-sensical for a probability
            if self.buyprob + self.randVar <1 and self.buyprob + self.randVar >0:
                #Update values
                self.buyprob += self.randVar
                self.nobuyprob = 1-self.buyprob
            #Append values
            self.buychanceList.append(self.buyprob)
            self.NobuychanceList.append(self.nobuyprob)
            self.mu_updater()
        elif nrcycles>1:
            for i in range(nrcycles):
                #Picks random variable from normal distribution
                self.randVar = np.random.normal(self.mu,self.sigma)
                if self.buyprob + self.randVar <1 and self.buyprob + self.randVar >0:
                    #Update values 
                    self.buyprob += self.randVar
                    self.nobuyprob = 1-self.buyprob
                #Append values
                self.buychanceList.append(self.buyprob)
                self.NobuychanceList.append(self.nobuyprob)
                self.mu_updater()
    def plot_probs(self, save=0,name="1") -> None:
        # Just plots the probabilities
        nrcycles = len(self.buychanceList)
        time = np.arange(0,nrcycles)
        plt.grid()
        plt.plot(time,self.NobuychanceList, label = "NoBuy opinion")
        plt.plot(time,self.buychanceList, label = "Buy opinion")
        plt.xlabel("discrete time")
        plt.ylabel("Probabilities")
        plt.legend()
        if save == 1:
            plt.savefig("figs/"+name+".png")
        plt.show() 

    # Plots the evolution of mu as a function of discrete time
    #Note: Only works for alogirthms that update mu
    def muplot(self,save = 0,name = "1") -> None:
        nrcycles = len(self.mulist)
        time = np.arange(0,nrcycles)
        plt.grid()
        muarray = np.array(self.mulist)
        plt.plot(time,muarray / self.sigma)
        plt.xlabel("discrete time")
        plt.ylabel(r"$\mu/\sigma$")
        if save == 1:
            plt.savefig("figs/"+name+".png")
        plt.show()         


class StandardStockModel(MarketOpinionModel):
    def __init__(self,InitValue,volatility,mu):
        self.Value = InitValue
        self.ValueList = []
        super().__init__(volatility,mu)

    def price_time_evolve(self,priceCycles = 1) -> None:
        self.priceCycles = priceCycles
        for i in range(priceCycles):
            #Pick price change
            self.price_change = np.random.choice([0.01,0.02,0.03,0.04,0.05],p=[0.2,0.3,0.3,0.1,0.1])
            
            #Next pick if stock go up or down based on opinion
            positive = self.buyprob
            #directionFactor is either +1 of -1 and is based on the market opinion
            self.directionFactor = np.random.choice([-1,1],p=[1-positive,positive])
            self.Value += self.directionFactor * self.price_change * self.Value
            
            self.ValueList.append(self.Value)
            self.Market_evolver()

    def plot_stonks(self,save = 0, name = "1") -> None:
        # Plots stock value
        T = len(self.ValueList)
        time = np.arange(0,T)
        plt.grid()
        plt.plot(time,self.ValueList, label = "Test AS")
        plt.xlabel("discrete time")
        plt.ylabel("Stock price")
        plt.legend()
        if save == 1:
            plt.savefig("figs/"+name+".png")
        plt.show() 
