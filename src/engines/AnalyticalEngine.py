import numpy as np

from typing import Tuple, Union

from src._params import OptionParams

class AnalyticalEngine:

    def price(self,
              model,
              strike: Union[float, np.ndarray],
              spot_price: float,
              time_to_expiry: float,
              risk_free_rate: float,
              params: OptionParams) -> Tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:

        if type(strike) is np.ndarray:
            return np.zeroes(strike.shape), np.zeroes(strike.shape) # ADD LATER

        call_price = model.closed_form_call(strike, spot_price, time_to_expiry, risk_free_rate, params)
        put_price = model.closed_form_put(strike, spot_price, time_to_expiry, risk_free_rate, params)

        # Call, Put
        return call_price, put_price



