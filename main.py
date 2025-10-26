from src.BlackScholesMerton import BlackScholesMerton

if __name__ == "__main__":
    # Parameters
    S = 100  # Current stock price
    K = 110  # Strike price
    T = 1.0  # 1 year to maturity
    r = 0.05  # 5% risk-free rate
    sigma = 0.1  # 20% volatility

    # Calculate option prices
    call_price = BlackScholesMerton.get_call_price(S, K, T, r, sigma)
    put_price = BlackScholesMerton.get_put_price(S, K, T, r, sigma)

    print("=" * 50)
    print("BLACK-SCHOLES OPTION PRICING")
    print("=" * 50)
    print(f"\nParameters:")
    print(f"  Stock Price (S):    ${S:.2f}")
    print(f"  Strike Price (K):   ${K:.2f}")
    print(f"  Time to Maturity:   {T:.2f} years")
    print(f"  Risk-free Rate:     {r * 100:.1f}%")
    print(f"  Volatility:         {sigma * 100:.1f}%")

    print(f"\nOption Prices:")
    print(f"  Call Price: ${call_price:.4f}")
    print(f"  Put Price:  ${put_price:.4f}")