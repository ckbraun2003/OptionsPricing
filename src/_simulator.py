import numpy as np
import matplotlib.pyplot as plt

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

    def plot_paths(self,
                   title_prefix: str = 'Paths -- ',
                   xlabel: str = 'Time Steps',
                   ylabel: str = 'Value') -> None:

        if self._cached_paths is None:
            raise ValueError("No paths to plot. Run simulate() first.")

        for key, paths in self._cached_paths.items():
            plt.figure(figsize=(10, 6))
            for i in range(paths.shape[1]):
                plt.plot(self._cached_paths[key][:, i], alpha=0.7, label=f'Path {i + 1}')

            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(title_prefix + key)
            plt.grid(True)