import numpy as np

from scipy.stats import norm

from src.utils.geometric_brownian_motion import simulate_geometric_brownian_motion

class BlackScholesMerton:

    @staticmethod
    def get_put_price(S: float, K: float, T: float, r: float, sigma: float) -> float:

        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

        return put_price

    @staticmethod
    def get_call_price(S: float, K: float, T: float, r: float, sigma: float) -> float:

        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

        return call_price

    @staticmethod
    def _simulate_paths(S0: float, r: float, sigma: float, T: float, N: int = 252, num_paths:int = 1) -> np.ndarray:
        return simulate_geometric_brownian_motion(S0, r, sigma, T, N, num_paths)