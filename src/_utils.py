import numpy as np

def simulate_geometric_brownian_motion(S0: float, mu: float, sigma: float, T: float, N: int = 252, num_paths:int = 1) -> np.ndarray:

    dt = T / N

    S = np.zeros((N, num_paths))
    S[0] = S0

    dW = np.random.normal(0, np.sqrt(dt), size=(N - 1, num_paths))

    for i in range(1, N):
        S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * dW[i-1])

    return S