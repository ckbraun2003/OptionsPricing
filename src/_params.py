from dataclasses import dataclass

@dataclass
class OptionParams:

    # Black-Scholes-Merton Specific
    variance: float = 0.0

    # Heston Specific
    initial_variance : float = 0.0 # v_0
    dividend_yield: float  = 0.0 # q
    mean_reversion_speed: float = 0.0 # kappa
    long_term_variance: float = 0.0 # theta
    correlation: float = 0.0 # rho
    volatility_volatility: float = 0.0 # sigma_v

    # Simulation Specific
    num_paths: int = 10000
    time_step: int = 252
