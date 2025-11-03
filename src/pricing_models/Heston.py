import numpy as np

from typing import Tuple

from src._params import OptionParams
from src.pricing_models.BaseModel import BaseModel
from src.utils.monte_carlo_approximation import monte_carlo_approximation

class Heston(BaseModel):

    @staticmethod
    def _get_put_price(strike: float,
                        spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> float:

        spot_price_paths, _ = Heston._simulate_paths(spot_price=spot_price,
                                                     time_to_expiry=time_to_expiry,
                                                     risk_free_rate=risk_free_rate,
                                                     params=params)

        return monte_carlo_approximation(K = strike,
                                         r = risk_free_rate,
                                         T = time_to_expiry,
                                         call_or_put = "put",
                                         paths = spot_price_paths)

    @staticmethod
    def _get_call_price(strike: float,
                        spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> float:

        spot_price_paths, _ = Heston._simulate_paths(spot_price = spot_price,
                                                    time_to_expiry = time_to_expiry,
                                                    risk_free_rate = risk_free_rate,
                                                    params = params)

        return monte_carlo_approximation(K = strike,
                                         r = risk_free_rate,
                                         T = time_to_expiry,
                                         call_or_put = "call",
                                         paths = spot_price_paths)

    @staticmethod
    def _simulate_paths(spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> Tuple[np.ndarray, np.ndarray]:

        dt = time_to_expiry / params.time_step
        sqrt_dt = np.sqrt(dt)
        S = np.empty((params.time_step, params.num_paths), dtype=float)
        v = np.empty((params.time_step, params.num_paths), dtype=float)
        S[0] = spot_price
        v[0] = params.initial_variance

        for i in range(1, params.time_step):
            z1 = np.random.randn(params.num_paths)
            z2 = np.random.randn(params.num_paths)
            dW1 = z1 * sqrt_dt
            dW2 = (params.correlation * z1 + np.sqrt(1 - params.correlation ** 2) * z2) * sqrt_dt

            v_prev = v[i - 1]
            sqrt_v_prev = np.sqrt(np.maximum(v_prev, 0.0))
            dv = (params.mean_reversion_speed * (params.long_term_variance - np.maximum(v_prev, 0.0))
                  * dt + params.volatility_volatility * sqrt_v_prev * dW2)

            v_new = v_prev + dv
            v_new = np.maximum(v_new, 0.0)

            S_prev = S[i - 1]
            dS = (risk_free_rate - params.dividend_yield) * S_prev * dt + sqrt_v_prev * S_prev * dW1
            S_new = S_prev + dS

            S[i] = S_new
            v[i] = v_new

        return S, v