
from finderivatives import validations as val

class UnderlyingAsset():
    
    def __init__(self, spot):
        self._spot = val.validate_spot(spot)
        self._payoff = self._spot
        self._profit = self._spot
        self._pricing = self._spot
        
    
    def payoff(self):
        """
        🚧 ¡Under construction! 🚧

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self._payoff
    
    
    def profit(self):
        """
        🚧 ¡Under construction! 🚧

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self._profit
    
    
    def pricing_bs(self):
        """
        🚧 ¡Under construction! 🚧

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self._pricing




