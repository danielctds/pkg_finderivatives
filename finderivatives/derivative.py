

import pandas as pd
import math as mt
import numpy as np
import random as rd
from scipy.stats import norm


#%%
class Derivative():
    
    def __init__(self, strike, maturity, position):
        self._strike = strike
        self._maturity = maturity
        self._position = position
        self._flows = {}
        
    def get_strike(self):
        return self._strike


#%% Call
class Call(Derivative):
    
    def __init__(self, strike, maturity, position):
        super().__init__(strike, maturity, position)
        
    
    def payoff(self, spot, premium=0):
        
        if self._position == 1:
            self._payoff = max([0, spot - self._strike]) - premium
        
        elif self._position == -1:
            self._payoff = min([0, self._strike - spot]) + premium
        
        return self._payoff
        
        
    
    
    def valuation_bs(self, spot, vol, rf, b, t):
        d1 = (mt.log(spot/self._strike) + (rf - b - (vol**2)/2)/t) \
            / (vol * mt.sqrt(t))
        d2 = d1 - vol * (t)**(1/2)
        
        v = spot * np.exp(-t) * norm.cdf(d1)\
            - self._strike * np.exp(-rf) * norm.cdf(d2)
        
        return v
    


#%%  Put
class Put(Derivative):
    
    def __init__(self, strike, maturity, position):
        super().__init__(strike, maturity, position)
        
    
    def payoff(self, spot, premium=0):
        
        if self._position == 1:
            self._payoff = max([0, self._strike - spot]) - premium
        
        elif self._position == -1:
            self._payoff = min([0, spot - self._strike]) + premium
        
        return self._payoff

    
# browniano
mu = 0.05
sigma = 0.02
s_0 = 100
dt = 1/12
s_1 = s_0 * mt.exp((mu - (sigma**2)*0.5)*dt \
                   + sigma * mt.sqrt(dt) * rd.normalvariate(0,1))

print(s_1)





if __name__ == '__main__':
    print(' Ejecucion directa ...')
    
    derivado = Derivative(strike=100, maturity=2, position=1)
    print(derivado.get_strike())
    
    put = Put(strike=150, maturity=3, position=1)
    print(put.get_strike())

    call = Call(strike=180, maturity=4, position=1)
    print(call.get_strike())
    
    call_valuation = call.valuation_bs(180, 0.05, 0.01, 0, 1)
    print(call_valuation)