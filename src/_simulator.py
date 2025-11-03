import numpy as np

from src._params import OptionParams

class Simulator:

    def __init__(self):

        self._cached_paths = None

    def simulate(self,
                 model,
                 spot_price: float,
                 time_to_expiry: float,
                 risk_free_rate: float,
                 params: OptionParams) -> np.ndarray:

        if self._cached_paths is not None:
            return self._cached_paths['Price']

        self._cached_paths = model.simulate_paths(spot_price, time_to_expiry, risk_free_rate, params)
        return self._cached_paths['Price']

    def reset(self) -> None:
        self._cached_paths = None