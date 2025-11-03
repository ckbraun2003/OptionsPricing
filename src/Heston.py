import numpy as np

from typing import Tuple

from src.utils.monte_carlo_approximation import monte_carlo_approximation

class Heston:

    @staticmethod
    def get_put_price(S0: float, v0: float, K: float, r: float, q: float,
                        kappa: float, theta: float, sigma_v: float,
                        rho: float, T: float, N: int = 252, num_paths: int = 1) -> float:

        return monte_carlo_approximation(K, r, T, "put",
                                         Heston._simulate_paths(S0, v0, r, q, kappa, theta, sigma_v, rho, T, N, num_paths))

    @staticmethod
    def get_call_price(S0: float, v0: float, K: float, r: float, q: float,
                        kappa: float, theta: float, sigma_v: float,
                        rho: float, T: float, N: int = 252, num_paths: int = 1) -> float:

        return monte_carlo_approximation(K, r, T, "call",
                                         Heston._simulate_paths(S0, v0, r, q, kappa, theta, sigma_v, rho, T, N, num_paths))

    @staticmethod
    def _simulate_paths(S0: float, v0: float, r: float, q: float,
                        kappa: float, theta: float, sigma_v: float,
                        rho: float, T: float, N: int = 252, num_paths: int = 1) -> Tuple[np.ndarray, np.ndarray]:

        dt = T / N
        sqrt_dt = np.sqrt(dt)
        S = np.empty((N, num_paths), dtype=float)
        v = np.empty((N, num_paths), dtype=float)
        S[0] = S0
        v[0] = v0

        for i in range(1, N):
            z1 = np.random.randn(num_paths)
            z2 = np.random.randn(num_paths)
            dW1 = z1 * sqrt_dt
            dW2 = (rho * z1 + np.sqrt(1 - rho ** 2) * z2) * sqrt_dt

            v_prev = v[i - 1]
            sqrt_v_prev = np.sqrt(np.maximum(v_prev, 0.0))
            dv = kappa * (theta - np.maximum(v_prev, 0.0)) * dt + sigma_v * sqrt_v_prev * dW2
            v_new = v_prev + dv
            v_new = np.maximum(v_new, 0.0)

            S_prev = S[i - 1]
            dS = (r - q) * S_prev * dt + sqrt_v_prev * S_prev * dW1
            S_new = S_prev + dS

            S[i] = S_new
            v[i] = v_new

        return S, v