# Experiment Spec 01: OLS recovery

This file defines the acceptance criteria. Agent must not change it without explicit permission.

## Data generation

- seed = 20260928
- n = 2000
- p = 3
- beta_true = [1.0, -2.0, 0.5]
- sigma = 0.5
- X_ij ~ iid Normal(0,1)
- epsilon_i ~ iid Normal(0, sigma^2)
- y = X beta_true + epsilon

## Acceptance criteria

1. `estimate_beta(X, y)` returns shape `(3,)`.
2. Its output matches `numpy.linalg.lstsq(X, y, rcond=None)[0]` within `1e-10`.
3. On the specified simulated data, max absolute estimation error from `beta_true` is below `0.05`.
4. The normal-equation residual
   `||X.T @ (y - X @ beta_hat)||_2`
   is below `1e-8`.
5. Tests may not be weakened to make an implementation pass.
