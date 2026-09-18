---
title: ARMA $(p, q)$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# ARMA $(p, q)$

$y_t$ is $\text{ARMA}(p, q)$

$$
(y_t - \mu) - \phi_1(y_{t-1} - \mu) - \dots - \phi_p(y_{t-p} - \mu) \\
= \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}
$$

$$
y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p} = \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}
$$

$\phi_0 = \mu(1 - \phi_1 - \dots - \phi_p)$

$\mu = \frac{\phi_0}{1 - \phi_1 - \dots - \phi_p}$

$\text{ARMA}(p, q)$

$y_t = \mu + \eta_t$ where $\eta_t$ is $\text{ARMA}(p, q)$ with no $\mu$ or $\phi_0$

$\text{ARMA}(p, q) = \text{AR}(p)$ with $\text{MA}(q)$ errors.

1. $q = 0 \to \text{ARMA}(p, 0) = \text{AR}(p)$
2. $p = 0 \to \text{ARMA}(0, q) = \text{MA}(q)$

Backshift Notation:
$$
\to \phi(B)(y_t - \mu) = \theta(B)\varepsilon_t \quad \text{--- (ARMA)}
$$
$$
\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p
$$

---

$$
\theta(z) = 1 + \theta_1 z + \theta_2 z^2 + \dots + \theta_q z^q
$$
(Sometimes people use $L$ instead of $B$, Lag Operator)

$$
y_t - \mu = \frac{\theta(B)}{\phi(B)} \varepsilon_t
$$

$$
\phi(z) = (1 - a_1 z) \dots (1 - a_p z)
$$
where roots of $\phi$ are $\frac{1}{a_1}, \dots, \frac{1}{a_p}$

$$
&= \frac{\theta(B)}{(1 - a_1 B) \dots (1 - a_p B)} \varepsilon_t \\
&= \theta(B)[1 + a_1 B + (a_1 B)^2 + \dots][1 + a_2 B + (a_2 B)^2 + \dots] \dots [1 + a_p B + (a_p B)^2 + \dots] \varepsilon_t
$$

If all $|a_j| < 1$, then the above is well-defined

$$
= \psi_0 \varepsilon_t + \psi_1 \varepsilon_{t-1} + \psi_2 \varepsilon_{t-2} + \dots,
$$
$$
\sum |\psi_j| < \infty
$$

$$
\frac{1}{1 - x} = 1 + x + x^2 + \dots
$$

$$
\frac{\theta(z)}{\phi(z)} = \psi(z) = \psi_0 + \psi_1 z + \psi_2 z^2 + \dots
$$

---

$$
\theta(z) = (\psi_0 + \psi_1 z + \psi_2 z^2 + \dots)(1 - \phi_1 z - \dots - \phi_p z^p)
$$
$$
1 + \theta_1 z + \dots + \theta_q z^q
$$

$$
\left.
1 &= \psi_0 \\
\theta_1 &= \psi_1 - \phi_1 \psi_0 \\
\theta_2 &= \psi_2 - \psi_1 \phi_1 - \phi_2 \psi_0
\right\} \text{ARMA} \to \text{MA}
$$

$\text{ARMA}(p, q)$: Causal-Stationary Regime (All roots of $\phi$ have modulus $> 1$)

$$
y_t = \mu + \sum_{j=0}^\infty \psi_j \varepsilon_{t-j}
$$

## ACF & PACF

$\{y_t\}$ **STATIONARY** time series model. ($h \ge 0$)

$\text{ACF}(h) = \text{correlation between } y_t \ & \ y_{t+h}$

$\text{PACF}(h) = \text{partial correlation between } y_t \ & \ y_{t+h} \text{ after removing the effects of } y_{t+1}, \dots, y_{t+h-1}$

**Facts**
1. $\text{MA}(q) \to \text{ACF}(h) = 0 \text{ for } |h| > q$
2. $\text{AR}(p) \to \text{PACF}(h) = 0 \text{ for } |h| > p$
3. Given data $y_1, \dots, y_n$, get Sample $\text{ACF}(h)$ & Sample $\text{PACF}(h)$

---

4. $\text{ARMA}(p, q)$: neither $\text{ACF}(h)$ nor $\text{PACF}(h)$ cut off after a finite lag.

$$
\left.
p &\le p_{\max} \\
q &\le q_{\max}
\right\} \text{ARMA}(p, q) \text{ for all } & \text{ use model selection e.g. AIC or BIC.}
$$
Automatic

## Parameter Estimation in $\text{ARMA}(p, q)$

$\text{ARIMA}(\text{data}, \text{order} = (p, d, q))$
$\downarrow$
Statsmodels function

estimates $\mu, \begin{matrix} \theta_1, \dots, \theta_q \\ \phi_1, \dots, \phi_p \end{matrix}, \sigma^2$

$p + q + 2$

Writing likelihood
Maximize log-likelihood

$\text{MA}(1)$ $\text{ARIMA}$ uses Kalman filter to write the log likelihood

## AIC & BIC

$$
(-2) \times \textbf{Maximized log-likelihood} + 2 \text{ (# parameters)}
$$
$\text{AIC}$
$\uparrow$
Akaike Akaike Information Criterion

---

$$
(-2) \times \textbf{Maximized log-likelihood} + (\log n) \text{ (# parameters)}
$$
$\downarrow$
Bayesian Information Criterion (BIC)

Fit $\text{AR}(2)$ to $\log y_t - \log y_{t-1}, t = 2 \dots n$

$$
\left[
\log y_{n+1} - \log y_n \\
\log y_{n+2} - \log y_{n+1} \\
\log y_{n+3} - \log y_{n+2} \\
\vdots \\
\log y_{n+100} - \log y_{n+99}
\right\}
\log y_{n+1} - \log y_n \\
\log y_{n+2} - \log y_n \\
\log y_{n+3} - \log y_n \\
\vdots \\
\log y_{n+100} - \log y_n
\right]
$$

---

[Up: contents](index.md) · [ARIMA models →](02-arima-models.md)
