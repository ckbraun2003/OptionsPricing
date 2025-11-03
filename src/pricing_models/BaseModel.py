from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from src._params import OptionParams

class BaseModel(ABC):

    def get_options_prices_grid(self,
                                spot_price: float,
                                strike_step: float,
                                time_to_expiry: float,
                                risk_free_rate: float,
                                num_strikes: int,
                                params: OptionParams) -> Tuple[Dict[float, float], Dict[float, float], List[float]]:

        calls_prices_grid = {}
        puts_prices_grid = {}
        strikes = []

        for i in range(-num_strikes, num_strikes + 1):
            strike = spot_price + (i * strike_step)
            calls_prices_grid[strike] = self._get_call_price(strike = strike,
                                                             spot_price = spot_price,
                                                             time_to_expiry = time_to_expiry,
                                                             risk_free_rate = risk_free_rate,
                                                             params = params)
            puts_prices_grid[strike] = self._get_put_price(strike = strike,
                                                             spot_price = spot_price,
                                                             time_to_expiry = time_to_expiry,
                                                             risk_free_rate = risk_free_rate,
                                                             params = params)
            strikes.append(strike)

        return calls_prices_grid, puts_prices_grid, strikes

    def _get_calls_price_grid(self,
                             spot_price: float,
                             time_to_expiry: float,
                             risk_free_rate: float,
                             strike_step: float,
                             num_strikes: int,
                             params: OptionParams) -> Dict[float, float]:

        options_price_grid = {}

        for i in range(-num_strikes, num_strikes + 1):
            strike = spot_price + i * strike_step
            options_price_grid[strike] = self._get_call_price(strike = strike,
                                                             spot_price = spot_price,
                                                             time_to_expiry = time_to_expiry,
                                                             risk_free_rate = risk_free_rate,
                                                             params = params)

        return options_price_grid

    def _get_puts_price_grid(self,
                            spot_price: float,
                            time_to_expiry: float,
                            risk_free_rate: float,
                            strike_step: float,
                            num_strikes: int,
                            params: OptionParams) -> Dict[float, float]:

        options_price_grid = {}

        for i in range(-num_strikes, num_strikes + 1):
            strike = spot_price + i * strike_step
            options_price_grid[strike] = self._get_put_price(strike = strike,
                                                             spot_price = spot_price,
                                                             time_to_expiry = time_to_expiry,
                                                             risk_free_rate = risk_free_rate,
                                                             params = params)

        return options_price_grid

    @staticmethod
    @abstractmethod
    def _get_call_price(strike: float,
                        spot_price: float,
                        time_to_expiry: float,
                        risk_free_rate: float,
                        params: OptionParams) -> float:

        """Compute price of a single call option"""
        pass

    @staticmethod
    @abstractmethod
    def _get_put_price(strike: float,
                       spot_price: float,
                       time_to_expiry: float,
                       risk_free_rate: float,
                       params: OptionParams) -> float:

        """Compute price of a single put option"""
        pass
