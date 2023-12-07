
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
                            position=1,
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


#%% Butterfly Spread

#### Butterfly Spread Call
    ###Precio de compra: X - a y X + a - Precio de venta: X 

class ButterflySpreadCall(Portfolio):
    
    def __init__(self, strike1, strike2, strike3, strike4, maturity, premium1 = 0,
                 premium2 = 0, premium3 = 0, premium4 = 0):
        
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        self._call02 = Call(strike=strike2,
                            maturity=maturity,
                            position=1,
                            premium=premium2)
        self._call03 = Call(strike=strike3,
                            maturity=maturity,
                            position=-1,
                            premium=premium3)
        self._call04 = Call(strike=strike4,
                            maturity=maturity,
                            position=-1,
                            premium=premium4)
        super().__init__(self._call01, self._call02, self._call03, self._call04)
        
    

#### Butterfly Spread Put
class ButterflySpreadPut(Portfolio):
    
    def __init__(self, strike1, strike2, strike3, strike4, maturity, premium1 = 0,
                 premium2 = 0, premium3 = 0, premium4 = 0):
        
        self._put01 = Put(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        self._put02 = Put(strike=strike2,
                            maturity=maturity,
                            position=1,
                            premium=premium2)
        self._put03 = Put(strike=strike3,
                            maturity=maturity,
                            position=-1,
                            premium=premium3)
        self._put04 = Put(strike=strike4,
                            maturity=maturity,
                            position=-1,
                            premium=premium4)
        super().__init__(self._put01, self._put02, self._put03, self._put04)


#%% Straddle
    #### Precios de strike iguales
    
class StraddleSpread(Portfolio):
    
    def __init__(self, strike1, strike2, maturity, premium1 = 0, premium2 = 0):
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        
        self._put01 = Put(strike=strike2,
                            maturity=maturity,
                            position=1,
                            premium=premium2)
        
        super().__init__(self._call01, self._put01)


#%% Strip
    #### Precios de strike iguales

class StripSpread(Portfolio):
    
    def __init__(self, strike1, strike2, strike3, maturity, premium1 = 0, 
                 premium2 = 0, premium3 = 0):
        
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        
        self._put01 = Put(strike=strike2,
                            maturity=maturity,
                            position=1,
                            premium=premium2)
        
        self._put02 = Put(strike=strike3,
                            maturity=maturity,
                            position=1,
                            premium=premium3)
        super().__init__(self._call01, self._put01, self._put02)


#%% Strap
    #### Precios de strike iguales

class StrapSpread(Portfolio):
    
    def __init__(self, strike1, strike2, strike3, maturity, premium1 = 0, 
                 premium2 = 0, premium3 = 0):
        
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        
        self._call02 = Call(strike=strike2,
                            maturity=maturity,
                            position=1,
                            premium=premium2)
        
        self._put01 = Put(strike=strike3,
                            maturity=maturity,
                            position=1,
                            premium=premium3)
        super().__init__(self._call01, self._call02, self._put01)

#%% Strangle
    #### Precios de strike put menor a call
    
class StrangleSpread(Portfolio):
    
    def __init__(self, strike1, strike2, maturity, premium1 = 0, premium2 = 0):
        
        self._call01 = Call(strike=strike1,
                            maturity=maturity,
                            position=1,
                            premium=premium1)
        
        self._put01 = Put(strike=strike2,
                            maturity=maturity,
                            position=1,
                            premium=premium2)
        
        super().__init__(self._call01, self._put01)





#%% Direct execution
if __name__ == '__main__':
    print(' Direct execution ... \n')
    