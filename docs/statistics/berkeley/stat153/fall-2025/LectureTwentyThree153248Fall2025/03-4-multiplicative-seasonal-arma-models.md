---
title: 4 Multiplicative Seasonal ARMA Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Multiplicative Seasonal ARMA Models

For the `co2` dataset (from the time series analysis textbook by Cryer and Chan), for the first and seasonal differenced data, we saw that the sample autocorrelations seem nonnegligible at lags 0, 1, 11, 12, 13 and those at all other lags seem negligible. This behaviour can be produced in a $\text{MA}(13)$ model but that model will have 14 parameters possibly leading to overfitting.

We can get a much more parsimonious model for this dataset by combining the $\text{MA}(1)$ model with a seasonal $\text{MA}(1)$ model of period 12. Specifically, consider the model
$$
y_t = (1 + \Theta B^{12})(1 + \theta B)\epsilon_t = (1 + \theta B + \Theta B^{12} + \theta\Theta B^{13})\epsilon_t = \epsilon_t + \theta\epsilon_{t-1} + \Theta\epsilon_{t-12} + \theta\Theta\epsilon_{t-13}.
$$
It is easy to check that model has the autocorrelation function:
$$
\rho(1) = \frac{\theta}{1 + \theta^2} \quad \text{and} \quad \rho(12) = \frac{\Theta}{1 + \Theta^2}
$$
and
$$
\rho(11) = \rho(13) = \frac{\theta\Theta}{(1 + \theta^2)(1 + \Theta^2)}.
$$
At every other lag $h > 0$, the autocorrelation $\rho_X(h)$ equals zero. Based on this ACF (and the sample ACF calculated from the data), this model can be suitable for the first and seasonal differenced data in the co2 dataset.

More generally, we can combine, by multiplication, ARMA and seasonal ARMA models to obtain models which have special autocorrelation properties with respect to seasonal lags. The **Multiplicative Seasonal Autoregressive Moving Average Model $\text{ARMA}(p, q) \times (P, Q)_s$** is defined via the difference equation:
$$
\Phi(B^s)\phi(B)(y_t - \mu) = \Theta(B^s)\theta(B)\epsilon_t.
$$
The model we looked at above for the co2 dataset is $\text{ARMA}(0, 1) \times (0, 1)_{12}$.

Another example of a multiplicative seasonal ARMA model is $\text{ARMA}(0, 1) \times (1, 0)_{12}$ (this is same as $\text{MA}(1) \times \text{AR}(1)_{12}$)
$$
(y_t - \mu) - \Phi(y_{t-12} - \mu) = \epsilon_t + \theta\epsilon_{t-1}.
$$
The autocorrelation function of this model can be checked to be $\rho(12h) = \Phi^h$ for $h \ge 0$ and
$$
\rho(12h - 1) = \rho(12h + 1) = \frac{\theta}{1 + \theta^2}\Phi^h \quad \text{for } h = 0, 1, 2, \dots
$$
and $\rho(h) = 0$ at all other lags.

When we have a dataset whose ACF and PACF show interesting patterns at seasonal lags, consider using a multiplicative seasonal ARMA model. You may use the Statsmodels functions `arma_acf` and `arma_pacf` to understand the autocorrelation and partial autocorrelation functions of these models.

## 5 SARIMA Models

These models are obtained by combining differencing with multiplicative seasonal ARMA models. These models are denoted by $\text{ARIMA}(p, d, q) \times (P, D, Q)_s$. This means that after differencing $d$ times and seasonal differencing $D$ times (with period $s$), we get a multiplicative seasonal ARMA model. In other words, $\{y_t\}$ is $\text{ARIMA}(p, d, q) \times (P, D, Q)_s$ if it satisfies the difference equation:
$$
\Phi(B^s)\phi(B)\nabla_s^D \nabla^d (y_t - \mu) = \delta + \Theta(B^s)\theta(B)\epsilon_t.
$$
Recall that $\nabla_s^d = (1 - B^s)^d$ and $\nabla^d = (1 - B)^d$ denote the differencing operators.

In the co2 example, we wanted to use the model $\text{ARMA}(0, 1) \times (0, 1)_{12}$ to the seasonal and first differenced data: $\nabla\nabla_{12}X_t$. In other words, we want to fit the SARIMA model with nonseasonal orders $0, 1, 1$ and seasonal orders $0, 1, 1$ with seasonal period 12 to the original co2 dataset. This model can be fit to the data using the function `ARIMA` with the `seasonal_order` argument.

---

[← 3 Seasonal ARMA Models](02-3-seasonal-arma-models.md) · [Up: contents](index.md)
