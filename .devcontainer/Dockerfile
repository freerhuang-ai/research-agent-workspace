FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

USER root

# --------------------------------------------------
# System dependencies + R
# --------------------------------------------------
# The base image may contain an obsolete Yarn apt source.
# We do not need it for this research environment.
RUN rm -f /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        build-essential \
        git \
        git-lfs \
        curl \
        openssh-client \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libzmq3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Python scientific stack
# --------------------------------------------------
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir \
        numpy \
        scipy \
        pandas \
        matplotlib \
        sympy \
        pytest \
        jupyterlab \
        jupytext \
        nbformat \
        papermill \
        ipykernel

# --------------------------------------------------
# R kernel for Jupyter
# --------------------------------------------------
RUN Rscript -e 'install.packages("IRkernel", repos="https://cloud.r-project.org")' && \
    Rscript -e 'IRkernel::installspec(user = FALSE)'

USER vscode
