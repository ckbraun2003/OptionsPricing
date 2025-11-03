from dataclasses import dataclass

@dataclass
class OptionParams:

    # Black Scholes Merton Specific
    variance: float

    # Heston Specific
    initial_variance : float # v_0
    dividend_yield: float # q
    mean_reversion_speed: float # kappa
    long_term_variance: float # theta
    correlation: float # rho
    volatility_volatility: float # sigma_v

    # Optional
    num_paths: int = 100
    time_step: float = 252
