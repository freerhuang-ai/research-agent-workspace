import numpy as np

from src.ols import estimate_beta


SEED = 20260928
N = 2000
P = 3
BETA_TRUE = np.array([1.0, -2.0, 0.5])
SIGMA = 0.5


def make_data():
    rng = np.random.default_rng(SEED)
    X = rng.normal(size=(N, P))
    eps = rng.normal(scale=SIGMA, size=N)
    y = X @ BETA_TRUE + eps
    return X, y


def test_shape():
    X, y = make_data()
    beta_hat = estimate_beta(X, y)
    assert beta_hat.shape == (P,)


def test_matches_lstsq():
    X, y = make_data()
    beta_hat = estimate_beta(X, y)
    beta_ref = np.linalg.lstsq(X, y, rcond=None)[0]
    np.testing.assert_allclose(beta_hat, beta_ref, atol=1e-10, rtol=0)


def test_recovers_true_beta():
    X, y = make_data()
    beta_hat = estimate_beta(X, y)
    assert np.max(np.abs(beta_hat - BETA_TRUE)) < 0.05


def test_normal_equation_residual():
    X, y = make_data()
    beta_hat = estimate_beta(X, y)
    residual = np.linalg.norm(X.T @ (y - X @ beta_hat))
    assert residual < 1e-8
