import numpy as np

from scipy.stats import norm
from typing import Dict

from src._params import OptionParams
from src._utils import simulate_geometric_brownian_motion

class BlackScholesMerton:

    @staticmethod
    def closed_form_put(strike: float,
                        spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> float:

        d1 = (np.log(spot_price / strike) + (risk_free_rate + 0.5 * params.volatility ** 2)
              * time_to_expiry) / (params.volatility * np.sqrt(time_to_expiry))

        d2 = d1 - params.volatility * np.sqrt(time_to_expiry)

        put_price = (strike * np.exp(-risk_free_rate * time_to_expiry)
                     * norm.cdf(-d2) - spot_price * norm.cdf(-d1))

        return put_price

    @staticmethod
    def closed_form_call(strike: float,
                         spot_price: float,
                         time_to_expiry: float,
                         risk_free_rate: float,
                         params: OptionParams) -> float:

        d1 = (np.log(spot_price / strike) + (risk_free_rate + 0.5 * params.volatility ** 2)
              * time_to_expiry) / (params.volatility * np.sqrt(time_to_expiry))

        d2 = d1 - params.volatility * np.sqrt(time_to_expiry)

        call_price = (spot_price * norm.cdf(d1) - strike
                      * np.exp(-risk_free_rate * time_to_expiry) * norm.cdf(d2))

        return call_price

    @staticmethod
    def simulate_paths(spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> Dict[str, np.ndarray]:

        paths = {}

        paths['Price'] = simulate_geometric_brownian_motion(spot_price,
                                                            risk_free_rate,
                                                            params.volatility,
                                                            time_to_expiry,
                                                            params.time_step,
                                                            params.num_paths)

        return paths
