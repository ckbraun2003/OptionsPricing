import numpy as np

from typing import Union

class EuropeanPayoff:

    @staticmethod
    def call(terminal_price: np.ndarray,
             strike_price: Union[float, np.ndarray],
             time_to_expiry: Union[float, np.ndarray],
             risk_free_rate: float) -> Union[float, np.ndarray]:

        strike_price = np.atleast_1d(strike_price)

        discount = np.exp(-risk_free_rate * time_to_expiry)
        payoff = np.maximum(terminal_price[:, None] - strike_price[None, :], 0)
        price = payoff.mean(axis=0) * discount

        return price if isinstance(strike_price, np.ndarray) else price.item()

    @staticmethod
    def put(terminal_price: np.ndarray,
            strike_price: Union[float, np.ndarray],
            time_to_expiry: float,
            risk_free_rate: float) -> Union[float, np.ndarray]:

        strike_price = np.atleast_1d(strike_price)

        discount = np.exp(-risk_free_rate * time_to_expiry)
        payoff = np.maximum(strike_price[None, :] - terminal_price[:, None], 0)
        price = payoff.mean(axis=0) * discount

        return price if isinstance(strike_price, np.ndarray) else price.item()
