
from finderivatives.european_call import Call
from finderivatives.european_put import Put
from finderivatives.portfolio import Portfolio


#%% Covered Call


#%% Reverse Covered Call



#%% Protective Put



#%% Revers Protective Put



#%% Bull Spread

#### Bull Spread Call
class BullSpreadCall(Portfolio):
    
    def __init__(self, strike1, strike2, maturity, premium1=0, premium2=0):
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        self._call02 = Call(strike=strike2,
                            maturity=maturity,
                            position=-1,
                            premium=premium2)
        super().__init__(self._call01, self._call02)
        

#### Bull Spread Put
class BullSpreadPut(Portfolio):
    
    def __init__(self, strike1, strike2, maturity, premium1=0, premium2=0):
        self._put01 = Put(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        self._put02 = Put(strike=strike2,
                            maturity=maturity,
                            position=-1,
                            premium=premium2)
        super().__init__(self._put01, self._put02)
        
        

#%% Bear Spread

#### Bear Spread Call
class BearSpreadCall(Portfolio):
    
    def __init__(self, strike1, strike2, maturity, premium1=0, premium2=0):
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        self._call02 = Call(strike=strike2,
                            maturity=maturity,
                            position=-1,
                            premium=premium2)
        super().__init__(self._call01, self._call02)
        

#### Bear Spread Put
class BearSpreadPut(Portfolio):
    
    def __init__(self, strike1, strike2, maturity, premium1=0, premium2=0):
        self._put01 = Put(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        self._put02 = Put(strike=strike2,
                            maturity=maturity,
                            position=-1,
                            premium=premium2)
        super().__init__(self._put01, self._put02)


#%% Butterfly

class ButterflySpread(Portfolio):
    
    def __init__(self, *derivatives):
        super().__init__(*derivatives)


#%% Straddle

class StraddleSpread(Portfolio):
    
    def __init__(self, *derivatives):
        super().__init__(*derivatives)


#%% Strip

class StripSpread(Portfolio):
    
    def __init__(self, *derivatives):
        super().__init__(*derivatives)


#%% Strap

class StrapSpread(Portfolio):
    
    def __init__(self, *derivatives):
        super().__init__(*derivatives)


#%% Strangle

class StrangleSpread(Portfolio):
    
    def __init__(self, *derivatives):
        super().__init__(*derivatives)





#%% Direct execution
if __name__ == '__main__':
    print(' Direct execution ... \n')
    