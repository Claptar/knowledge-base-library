---
title: Causal Stationary AR(2) Example
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Causal Stationary AR(2) Example

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
```

Consider the AR(2) equation:
\begin{equation*}
  y_t - 0.5 y_{t-1} + 0.25 y_{t-2} = \epsilon_t
\end{equation*}
Show that it has a causal stationary solution. Write the solution explicitly in terms of $\epsilon_t$.

The characteristic polynomial corresponding to this equation is: $\phi(z) = 1 - 0.5 z + 0.25 z^2$. Its roots are easily seen to be $2 \exp(\pm i\pi/3)$ whose modulus equals 2. Since the modulus is strictly larger than 1, this AR(2) equation admits a causal stationary solution. To express the solution explicitly in terms of $\{\epsilon_t\}$, we first write:
\begin{equation*}
   \phi(z) = \left(1 - 0.5 \exp(i \pi/3) z \right)\left(1 - 0.5 \exp(-i \pi/3) z \right)
\end{equation*}
so that
\begin{align*}
  y_t &= \frac{1}{\phi(B)} \epsilon_t \\ &= \left(I - 0.5 \exp(i \pi/3) B \right)^{-1}\left(I - 0.5 \exp(-i \pi/3) B \right)^{-1} \epsilon_t \\ &= \left(\sum_{j=0}^{\infty} 0.5^j \exp(i j \pi/3) B^j \right)\left(\sum_{k=0}^{\infty} 0.5^k \exp(-i k \pi/3) B^k \right) \epsilon_t \\
  &= \sum_{j=0}^{\infty} \sum_{k=0}^{\infty} 0.5^{j+k} \exp \left(\frac{i(j-k)\pi}{3} \right) \epsilon_{t - j - k}.
\end{align*}
A simpler expression for $y_t$ can be obtained using the following.  Let $a_1 = 0.5 \exp(i \pi/3)$ and $a_2 = 0.5 \exp(-i\pi/3)$. Check that
\begin{align*}
    \frac{1}{(1 - a_1 z)(1 - a_2 z)} = \frac{a_1}{(a_1 - a_2)(1 - a_1 z)} + \frac{a_2}{(a_2 - a_1) (1 - a_2 z)} = \frac{a_1}{a_1 - a_2} \sum_{j=0}^{\infty} (a_1 z)^j + \frac{a_2}{a_2 - a_1} \sum_{j=0}^{\infty} (a_2 z)^j = \sum_{j=0}^{\infty} \psi_j z^j
\end{align*}
where
\begin{align*}
   \psi_j = \frac{a_1^{j+1} - a_2^{j+1}}{a_1 - a_2} = (0.5)^{j+1}\frac{\exp((j+1)i\pi/3) - \exp(-(j+1)i\pi/3)}{0.5\exp(i\pi/3) - 0.5\exp(-i\pi/3)} = (0.5)^{j} \frac{\sin((j+1)\pi/3)}{\sin(\pi/3)} = \frac{2}{\sqrt{3}} (0.5)^{j} \sin \left( \frac{(j+1)\pi}{3} \right).
\end{align*}
We thus  have
\begin{align*}
   y_t = \sum_{j=0}^{\infty} \psi_j \epsilon_{t-j} = \frac{2}{\sqrt{3}} \sum_{j=0}^{\infty} (0.5)^{j} \sin\left( \frac{(j+1)\pi}{3} \right) \epsilon_{t-j} .
\end{align*}
The above expression represents the given causal stationary AR(2) process as an infinite order MA (MA($\infty$)) process. Recall that the MA($q$) process is defined by $y_t = \mu + \sum_{j = 0}^q \theta_j \epsilon_{t-j}$ for some $q$. The above expression for $y_t$ is reminiscent of MA($q$) but with $q = \infty$.

These $\psi_j$ coefficients decay rapidly with $j$ (because of the presence of $(0.5)^j$). Otherwise the process will not be causal-stationary. In the plot below, we plot the $\psi_j$ coefficients as a function of $j$.

```python
nlags = 40
psi_j = np.array([
    (2 / np.sqrt(3)) * (0.5) ** j * np.sin((j + 1) * np.pi / 3)
    for j in range(nlags)
])

plt.figure(figsize=(8, 5))
plt.plot(
    np.arange(nlags), psi_j,
    marker='o', linestyle='-', linewidth=2, markersize=6,
    color='royalblue', label=r'$\psi_j$ coefficients'
)
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.title(r"Decay of $\psi_j$ Coefficients Toward Zero", fontsize=14)
plt.xlabel("Lag $j$", fontsize=12)
plt.ylabel(r"$\psi_j$", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There is an inbuilt statsmodels function (shown  below) which gives the MA($\infty$) representation of every causal stationary AR($p$) (in fact for every causal stationary ARMA model; we will learn about ARMA models next week). Specifically, given coefficients $\phi_1, \dots \phi_p$ it outputs $\psi_0 = 1, \psi_1, \psi_2, \dots $ such that $y_t = \sum_{j=0}^{\infty} \psi_j \epsilon_{t-j}$ solves the AR($p$) equation: $y_t = \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t$.

```python
from statsmodels.tsa.arima_process import ArmaProcess

ar = [1, -0.5, 0.25] # these are the phi-coefficients of the given AR process
ma = [1]
# these are the theta-coefficients of the ARMA process
# (since we are dealing with a pure AR process, there is no theta coefficient)

AR2_process = ArmaProcess(ar, ma)
nlags = 40

ma_infinity = AR2_process.arma2ma(lags = nlags)
# this gives \psi_j, j = 0, \dots, lags-1

print(np.column_stack([psi_j, ma_infinity]))
```

```
[[ 1.00000000e+00  1.00000000e+00]
 [ 5.00000000e-01  5.00000000e-01]
 [ 3.53525080e-17  0.00000000e+00]
 [-1.25000000e-01 -1.25000000e-01]
 [-6.25000000e-02 -6.25000000e-02]
 [-8.83812699e-18  0.00000000e+00]
 [ 1.56250000e-02  1.56250000e-02]
 [ 7.81250000e-03  7.81250000e-03]
 [ 1.65714881e-18  0.00000000e+00]
 [-1.95312500e-03 -1.95312500e-03]
 [-9.76562500e-04 -9.76562500e-04]
 [-2.76191468e-19  0.00000000e+00]
 [ 2.44140625e-04  2.44140625e-04]
 [ 1.22070313e-04  1.22070312e-04]
 [ 1.68347800e-19  0.00000000e+00]
 [-3.05175781e-05 -3.05175781e-05]
 [-1.52587891e-05 -1.52587891e-05]
 [-6.47323754e-21  0.00000000e+00]
 [ 3.81469727e-06  3.81469727e-06]
 [ 1.90734863e-06  1.90734863e-06]
 [ 9.44013808e-22  0.00000000e+00]
 [-4.76837158e-07 -4.76837158e-07]
 [-2.38418579e-07 -2.38418579e-07]
 [-1.34859115e-22  0.00000000e+00]
 [ 5.96046448e-08  5.96046448e-08]
 [ 2.98023224e-08  2.98023224e-08]
 [ 1.89645631e-23  0.00000000e+00]
 [-7.45058060e-09 -7.45058060e-09]
 [-3.72529030e-09 -3.72529030e-09]
 [-1.02751343e-23  0.00000000e+00]
 [ 9.31322575e-10  9.31322575e-10]
 [ 4.65661287e-10  4.65661287e-10]
 [-5.92975423e-25  0.00000000e+00]
 [-1.16415322e-10 -1.16415322e-10]
 [-5.82076609e-11 -5.82076609e-11]
 [-4.93868831e-26  0.00000000e+00]
 [ 1.45519152e-11  1.45519152e-11]
 [ 7.27595761e-12  7.27595761e-12]
 [ 2.16119618e-26  0.00000000e+00]
 [-1.81898940e-12 -1.81898940e-12]]
```

We can check from the above that the $\psi_j$ calculated by our formula (which we obtained by  using the Backshift method) coincide with the values output by the statsmodels function.

---

[Up: contents](index.md) · [AR order selection through PACF →](02-ar-order-selection-through-pacf.md)
