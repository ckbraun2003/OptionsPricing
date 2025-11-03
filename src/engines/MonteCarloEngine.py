import numpy as np

from typing import Dict, Union

from src._params import OptionParams

class MonteCarloEngine:

    def __init__(self,
                 simulator):

        self._simulator = simulator

    def price(self,
              model,
              payoff,
              strike: Union[float, np.ndarray],
              spot_price: float,
              time_to_expiry: float,
              risk_free_rate: float,
              params: OptionParams) -> Dict[str, Union[float, np.ndarray]]:

        prices = {}

        price_paths = self._simulator.simulate(model, spot_price, time_to_expiry, risk_free_rate, params)
        price_paths = np.asarray(price_paths)

        if price_paths.ndim != 2:
            raise ValueError("Simulator must return array of shape (n_steps, n_paths)")

        terminal_prices = price_paths[-1, :]

        prices['Call'] = payoff.call(terminal_prices,
                                 strike,
                                 time_to_expiry,
                                 risk_free_rate)
        prices['Put'] = payoff.put(terminal_prices,
                               strike,
                               time_to_expiry,
                               risk_free_rate)

        return prices

    def reset(self) -> None:
        self._simulator.reset()