import numpy as np

from typing import Dict

from src._params import OptionParams

class Heston:

    @staticmethod
    def simulate_paths(spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> Dict[str, np.ndarray]:

        paths = {}

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
                  * dt + params.volatility_variance * sqrt_v_prev * dW2)

            v_new = v_prev + dv
            v_new = np.maximum(v_new, 0.0)

            S_prev = S[i - 1]
            dS = (risk_free_rate - params.dividend_yield) * S_prev * dt + sqrt_v_prev * S_prev * dW1
            S_new = S_prev + dS

            S[i] = S_new
            v[i] = v_new

        paths['Price'] = S
        paths['Variance'] = v
        return paths