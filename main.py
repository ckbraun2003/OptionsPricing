from src._params import OptionParams
from src.BlackScholesMerton import BlackScholesMerton
from src.Heston import Heston

if __name__ == "__main__":
    # Parameters
    options_kwargs = OptionParams

    options_kwargs.variance = 0.1
    options_kwargs.initial_variance = 0.1
    options_kwargs.dividend_yield = 0.0
    options_kwargs.mean_reversion_speed = 1.5
    options_kwargs.long_term_variance = 0.4
    options_kwargs.correlation = -0.3
    options_kwargs.volatility_volatility = 0.2


    spot_price = 100  # Current stock price
    time_to_expiry = 1.0
    risk_free_rate = 0.05
    strike_step = 0.25
    num_strikes = 10

    bsm = BlackScholesMerton()
    heston = Heston()

    # Calculate option prices
    black_scholes_merton_options_grid = bsm.get_options_prices_grid(spot_price,
                                                                    time_to_expiry,
                                                                    risk_free_rate,
                                                                    strike_step,
                                                                    num_strikes,
                                                                    options_kwargs)

    heston_options_grid = heston.get_options_prices_grid(spot_price,
                                                         time_to_expiry,
                                                         risk_free_rate,
                                                         strike_step,
                                                         num_strikes,
                                                         options_kwargs)


    print("Black Scholes Merton Options grid:\n")
    for strike, price in black_scholes_merton_options_grid["calls"].items():
        print(f"Strike: ${strike} | Call Price: ${price:.2f}")

    print("=" * 50)

    for strike, price in black_scholes_merton_options_grid["puts"].items():
        print(f"Strike: ${strike} | Put Price: ${price:.2f}")

    print("\n\n\nHeston Options grid:\n")
    for strike, price in heston_options_grid["calls"].items():
        print(f"Strike: ${strike} | Call Price: ${price:.2f}")

    print("=" * 50)

    for strike, price in heston_options_grid["puts"].items():
        print(f"Strike: ${strike} | Put Price: ${price:.2f}")