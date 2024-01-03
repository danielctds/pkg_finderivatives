
from finderivatives import validations as val

class UnderlyingAsset():
    
    def __init__(self, spot, position):
        self._spot = val.validate_spot(spot)
        self._position = val.validate_position(position)
        self._payoff = self._spot * self._position
        self._profit = self._spot * self._position
        self._pricing = self._spot * self._position
        
    
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




