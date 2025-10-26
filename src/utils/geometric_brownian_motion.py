import numpy as np

from typing import Tuple

def geometric_brownian_motion(S0: float, mu: float, sigma: float, T: float, N: int = 252, num_paths:int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Parameters:
    S0 : float
        Initial value
    mu : float
        Drift coefficient
    sigma : float
        Volatility coefficient
    T : float
        Total time period (in years)
    N : int
        Time step (per year)
    num_paths : int
        Number of paths to simulate (default=1)

    Returns:
    t : numpy.ndarray
        Time points
    S : numpy.ndarray
        Simulated paths (shape: [num_steps, num_paths])
    """
    # Calculate step size
    dt = T / N

    # Create time array
    t = np.linspace(0, T, N)

    # Initialize array to store paths
    S = np.zeros((N, num_paths))
    S[0] = S0

    # Generate random normal increments
    dW = np.random.normal(0, np.sqrt(dt), size=(N - 1, num_paths))

    # Simulate GBM using the exact solution
    for i in range(1, N):
        S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * dW[i-1])

    return t, S