import numpy as np

from scipy.stats import norm

class BlackScholesMerton:

    @staticmethod
    def get_put_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
        """
        Parameters:
        S : float
            Current stock price
        K : float
            Strike price
        T : float
            Time to maturity (in years)
        r : float
            Risk-free interest rate (annual)
        sigma : float
            Volatility (annual)

        Returns:
        float : Put option price
        """
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return put_price

    @staticmethod
    def get_call_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
        """
        Parameters:
        S : float
            Current stock price
        K : float
            Strike price
        T : float
            Time to maturity (in years)
        r : float
            Risk-free interest rate (annual)
        sigma : float
            Volatility (annual)

        Returns:
        float : Call option price
        """

        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        return call_price