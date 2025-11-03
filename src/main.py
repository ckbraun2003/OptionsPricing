import numpy as np

from src._params import OptionParams
from src._simulator import Simulator

from src.models.BlackScholesMerton import BlackScholesMerton
from src.models.Heston import Heston

from src._payoffs import EuropeanPayoff

from src.engines.AnalyticalEngine import AnalyticalEngine
from src.engines.MonteCarloEngine import MonteCarloEngine

if __name__ == "__main__":
    # Parameters
    options_kwargs = OptionParams()

    options_kwargs.variance = 0.1
    options_kwargs.initial_variance = 0.1**2
    options_kwargs.dividend_yield = 0.0
    options_kwargs.mean_reversion_speed = 100
    options_kwargs.long_term_variance = 0.1**2
    options_kwargs.correlation = 0.0
    options_kwargs.volatility_volatility = 0.0


    spot_price = 100  # Current stock price
    strike_price = np.array([105, 110, 115], dtype=float)
    time_to_expiry = 1.0
    risk_free_rate = 0.05

    simulator = Simulator()
    engine = MonteCarloEngine(simulator)

    bsm_simulated_prices = engine.price(BlackScholesMerton, EuropeanPayoff, strike_price, spot_price, time_to_expiry, risk_free_rate, options_kwargs)
    engine.reset()
    heston_simulated_prices = engine.price(Heston, EuropeanPayoff, strike_price, spot_price, time_to_expiry, risk_free_rate, options_kwargs)

    print("Black Scholes Merton")
    for i in range(len(bsm_simulated_prices['Call'])):
        print(f"Simulated: || Strike: {strike_price[i]} | Call Price: {bsm_simulated_prices['Call'][i]:.2f} | Put Price: {bsm_simulated_prices['Put'][i]:.2f}")

    print()

    print("Heston")
    for i in range(len(heston_simulated_prices['Call'])):
        print(f"Simulated: || Strike: {strike_price[i]} | Call Price: {heston_simulated_prices['Call'][i]:.2f} | Put Price: {heston_simulated_prices['Put'][i]:.2f}")

