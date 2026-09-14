---
title: Stationary solutions, Box-Jenkins Modeling, AIC and BIC
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stationary solutions, Box-Jenkins Modeling, AIC and BIC

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
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
The above expression represents the given causal stationary AR(2) process as an infinite order MA (MA($\infty$)) process.

There is an inbuilt statsmodels function (shown  below) which gives the MA($\infty$) representation of every casual stationary ARMA process.

```python
from statsmodels.tsa.arima_process import ArmaProcess

ar = [1, -0.5, 0.25] # these are the phi-coefficients of the given AR process
ma = [1]

---

[Up: contents](index.md) · [these are the theta-coefficients of the ARMA process →](02-these-are-the-theta-coefficients-of-the-arma-process.md)
