# %% [markdown]
# # Notebook 01 — OLS：从公式到数值验证
#
# 本 Notebook 的目标不是“让 AI 给出答案”，而是把一个统计结论拆成：
#
# 1. 模型与维度
# 2. 手推公式
# 3. 可执行实现
# 4. 基准实现对照
# 5. 数值验收

# %%
from pathlib import Path
import sys
import numpy as np

PROJECT = Path.cwd()
if PROJECT.name == "notebooks":
    PROJECT = PROJECT.parent
sys.path.insert(0, str(PROJECT))

from src.ols import estimate_beta

# %% [markdown]
# ## 1. 固定数据生成机制
#
# 规格来自 `specs/01_ols_spec.md`。
# 不要为了“得到漂亮结果”改 seed、真实参数或噪声水平。

# %%
SEED = 20260928
N = 2000
P = 3
BETA_TRUE = np.array([1.0, -2.0, 0.5])
SIGMA = 0.5

rng = np.random.default_rng(SEED)
X = rng.normal(size=(N, P))
eps = rng.normal(scale=SIGMA, size=N)
y = X @ BETA_TRUE + eps

X.shape, y.shape

# %% [markdown]
# ## 2. 我们要验证的公式
#
# \[
# \hat\beta = (X^T X)^{-1} X^T y
# \]
#
# 代码中不用显式求逆，而解线性方程：
#
# \[
# (X^T X)\hat\beta = X^T y.
# \]

# %%
beta_hat = estimate_beta(X, y)
beta_ref = np.linalg.lstsq(X, y, rcond=None)[0]

print("beta_true:", BETA_TRUE)
print("beta_hat :", beta_hat)
print("lstsq ref:", beta_ref)
print("max |hat-true|:", np.max(np.abs(beta_hat - BETA_TRUE)))
print("max |hat-ref| :", np.max(np.abs(beta_hat - beta_ref)))

# %% [markdown]
# ## 3. 验证一阶条件

# %%
gradient_like_residual = X.T @ (y - X @ beta_hat)
print("||X.T @ residual||_2 =", np.linalg.norm(gradient_like_residual))

# %% [markdown]
# ## 4. 人的结论区
#
# 请自己回答：
#
# - 维度是否全部一致？
# - 为什么这里可以解 `(X.T @ X) beta = X.T @ y`？
# - 如果 `X` 不满列秩会发生什么？
# - “代码能跑”与“模型正确”有什么区别？
