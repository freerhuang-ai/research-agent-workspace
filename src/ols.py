import numpy as np


def estimate_beta(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """OLS estimator using a linear solve of the normal equations."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    if X.ndim != 2:
        raise ValueError("X must be a 2D matrix")
    if y.ndim != 1:
        raise ValueError("y must be a 1D vector")
    if X.shape[0] != y.shape[0]:
        raise ValueError("X and y must have the same number of observations")

    gram = X.T @ X
    rhs = X.T @ y
    return np.linalg.solve(gram, rhs)
