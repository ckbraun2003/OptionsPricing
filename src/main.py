from src._params import OptionParams
from src.pricing_models.BlackScholesMerton import BlackScholesMerton
from src.pricing_models.Heston import Heston

if __name__ == "__main__":
    # Parameters
    options_kwargs = OptionParams()

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

    heston = Heston()

    calls_price_grid, puts_price_grid, strikes = heston.get_options_prices_grid(spot_price,
                                                         time_to_expiry,
                                                         risk_free_rate,
                                                         strike_step,
                                                         num_strikes,
                                                         options_kwargs)



    print("\n\n\nHeston Options grid:\n")
    for strike in strikes:
        print(f"Strike: ${strike} | Call Price: ${calls_price_grid[strike]:.2f} | Put Price: ${puts_price_grid[strike]:.2f}")
