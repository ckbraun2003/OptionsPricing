import numpy as np

from scipy.stats import norm

from src._params import OptionParams
from src.utils.BaseModel import BaseModel
from src.utils.geometric_brownian_motion import simulate_geometric_brownian_motion

class BlackScholesMerton(BaseModel):

    @staticmethod
    def _get_put_price(strike: float,
                        spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> float:

        d1 = (np.log(spot_price / strike) + (risk_free_rate + 0.5 * params.variance ** 2)
              * time_to_expiry) / (params.variance * np.sqrt(time_to_expiry))

        d2 = d1 - params.variance * np.sqrt(time_to_expiry)

        put_price = (strike * np.exp(-risk_free_rate * time_to_expiry)
                     * norm.cdf(-d2) - spot_price * norm.cdf(-d1))

        return put_price

    @staticmethod
    def _get_call_price(strike: float,
                        spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> float:

        d1 = (np.log(spot_price / strike) + (risk_free_rate + 0.5 * params.variance ** 2)
              * time_to_expiry) / (params.variance * np.sqrt(time_to_expiry))

        d2 = d1 - params.variance * np.sqrt(time_to_expiry)

        call_price = (spot_price * norm.cdf(d1) - strike
                      * np.exp(-risk_free_rate * time_to_expiry) * norm.cdf(d2))

        return call_price

    @staticmethod
    def _simulate_paths(spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> np.ndarray:

        return  simulate_geometric_brownian_motion(spot_price,
                                                   risk_free_rate,
                                                   params.variance,
                                                   time_to_expiry,
                                                   params.time_step,
                                                   params.num_paths)
