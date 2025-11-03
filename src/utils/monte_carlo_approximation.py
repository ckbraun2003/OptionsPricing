import numpy as np

def monte_carlo_approximation(K: float, r: float, T: float, call_or_put: str, paths: np.ndarray) -> float:
    ST = paths[-1, :]
    discount = np.exp(-r*T)

    if call_or_put == 'put':
        return _expected_put(ST, K) * discount

    elif call_or_put == 'call':
        return _expected_call(ST, K) * discount

    else:
        return 0.0

def _expected_put(ST: float, K:float) -> float:
    return np.maximum(K - ST, 0).mean()

def _expected_call(ST: float, K:float) -> float:
    return np.maximum(ST - K, 0).mean()