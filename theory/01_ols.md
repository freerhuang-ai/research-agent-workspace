\
# 01 OLS / Gaussian linear model

Model:

\[
y = X\beta + \varepsilon,\qquad
\varepsilon \sim N(0,\sigma^2 I_n)
\]

Dimensions:

- \(y \in \mathbb{R}^{n}\)
- \(X \in \mathbb{R}^{n\times p}\)
- \(\beta \in \mathbb{R}^{p}\)

If \(X\) has full column rank, the normal equations are

\[
X^\top X\hat\beta = X^\top y
\]

and therefore

\[
\hat\beta = (X^\top X)^{-1}X^\top y.
\]

Numerically, do not explicitly compute the inverse unless there is a reason to do so.
Use a linear solver.
