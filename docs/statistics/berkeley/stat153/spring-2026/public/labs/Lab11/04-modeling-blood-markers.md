---
title: Modeling blood markers
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Modeling blood markers

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We model three blood markers — log(WBC), log(PLT), and HCT — as a VAR(1) state-space model with missing observations. This matches the Shumway & Stoffer formulation:

**State equation:**
$$x_t = \Phi x_{t-1} + w_t, \quad w_t \sim \mathcal{N}(0, Q)$$

**Observation equation:**
$$y_t = A_t x_t + v_t, \quad v_t \sim \mathcal{N}(0, R)$$

where $A_t = I_3$ when a blood sample is taken on day $t$ and $A_t = 0$ when no sample is available. The state $x_t = [\text{WBC}_t, \text{PLT}_t, \text{HCT}_t]^\top$ represents the underlying (unobserved) true marker levels.

**What we estimate via MLE:**
* $\Phi$: $(3 \times 3)$ transition matrix (9 parameters). This represents how markers evolve and interact from one day to the next.
* $Q$: $(3 \times 3)$ symmetric state noise covariance (6 parameters). This represents unmodeled biological variability
* $R$: $(3 \times 3)$ symmetric observation noise covariance (6 parameters). This represents measurement error

**What the Kalman filter/smoother computes:**
* Filtered estimates $x_t^t = E[x_t \mid y_{1:t}]$ for real-time tracking
* Smoothed estimates $x_t^n = E[x_t \mid y_{1:n}]$ for the best estimate using all data, including future observations
* Forecasts $x_{n+h}^n$ for prediction beyond the observation window [e.g., platelet count at day 100]

```python
from statsmodels.tsa.statespace.mlemodel import MLEModel
```

```python

---

[← Load the data](03-load-the-data.md) · [Up: contents](index.md) · [Look at the raw data and see what is missing →](05-look-at-the-raw-data-and-see-what-is-missing.md)
