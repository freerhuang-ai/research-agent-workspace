#!/usr/bin/env bash
set -euo pipefail

echo "=== Installing system dependencies ==="
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    r-base \
    r-base-dev \
    build-essential \
    git \
    curl \
    openssh-client

echo "=== Installing Python research stack ==="
python -m pip install --upgrade pip
python -m pip install \
    numpy \
    scipy \
    pandas \
    matplotlib \
    sympy \
    pytest \
    jupyterlab \
    jupytext \
    nbformat \
    papermill

echo "=== Installing R Jupyter kernel ==="
Rscript -e '
if (!requireNamespace("IRkernel", quietly = TRUE)) {
    install.packages("IRkernel", repos="https://cloud.r-project.org")
}
IRkernel::installspec(user = TRUE)
'

echo "=== Installing uv ==="
if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

echo
echo "Base research environment ready."
echo "Trae Agent will be installed separately after verification."
