---
title: Spectrum Model applied to a FRED dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Spectrum Model applied to a FRED dataset

**Source:** [`Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The following basically follows the analysis given in Section 6.4 of the book "Time Series Analysis" by James D. Hamilton (this is widely recognized as a classic textbook on time series).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import cvxpy as cp
from scipy.signal import find_peaks
```

The following datset is FRED's "Industrial Production: Total Index" dataset. It is a monthly dataset that is **not** seasonally adjusted.

```python
prod_index = pd.read_csv("IPB50001N-06March2025FRED.csv")
print(prod_index.head(10))

pind = prod_index['IPB50001N']
plt.figure(figsize = (12, 6))
plt.plot(pind)
plt.show()
```

```
observation_date  IPB50001N
0       1919-01-01     4.7841
1       1919-02-01     4.5959
2       1919-03-01     4.4884
3       1919-04-01     4.5691
4       1919-05-01     4.7035
5       1919-06-01     4.9991
6       1919-07-01     5.1604
7       1919-08-01     5.2679
8       1919-09-01     5.2947
9       1919-10-01     5.2679
```

*(1 figure omitted — see the original notebook.)*

Instead of working with the index data directly, we want to work with the monthly growth rate of the index. This is defined by:
\begin{equation*}
   y_t = 100 \left(\log I_t - \log I_{t-1} \right)
\end{equation*}
where $I_t$ is the index value at time $t$. Why does this definition correspond to the growth rate?

```python
y = 100 * np.diff(np.log(pind))
n = len(y)
print(n)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

```
1272
```

*(1 figure omitted — see the original notebook.)*

We want to fit the spectrum model to this dataset. Since the data size is even ($n = 1272$), the spectrum model is given by:
\begin{equation*}
    y_t = \beta_0 + \sum_{j=1}^m \left( \beta_{1j} \cos(2 \pi (j/n) t) + \beta_{2j} \sin(2 \pi (j/n) t) \right) + \beta_{m+1} \cos(\pi t).
\end{equation*}
where $m = (n/2) - 1$ (the presence of the $\cos(\pi t)$ term at the end makes this slightly different from the model when $n$ is odd), along with
\begin{equation*}
   \beta_{1j}, \beta_{2j} \overset{\text{i.i.d}}{\sim} N(0, \tau_j^2) ~~~ \text{ and } ~~~ \beta_{m+1} \sim N(0, \tau_{m+1}^2).
\end{equation*}

Observe first that
\begin{equation*}
   \beta_0 = \bar{y}, ~~~ \beta_{1j} = \frac{2}{n} \sum_{t=1}^n y_t \cos(2 \pi (j/n) t), ~~~ \beta_{2j} = \frac{2}{n} \sum_{t=1}^n y_t \sin(2 \pi (j/n) t), ~~~ \beta_{m+1} = \frac{1}{n} \sum_{t=1}^n y_t \cos(\pi t).
\end{equation*}
Recall that $\sum_{t=1}^n y_t \cos(2 \pi (k/n) t)$ is the real part and $\sum_{t=1}^n y_t \sin(2 \pi (k/n) t)$ is the imaginary part of the DFT term $b_k$. Thus the model can be alternatively be written in terms of DFT as:
\begin{equation*}
  Re(b_j), Im(b_j) \overset{\text{i.i.d}}{\sim} N(0, n^2 \tau_j^2/4) ~~~ \text{ and }~~~  b_{m+1} = b_{n/2} \sim N(0, \tau_{m+1}^2 n^2).
\end{equation*}
We also have
\begin{equation*}
   |b_j|^2 \sim \frac{n^2 \tau_j^2}{4} \chi^2_2 ~~ \text{ for } j = 1, \dots, m ~~ \text{ and } ~~~ b_{m+1}^2 \sim n^2 \tau_{m+1}^2 \chi^2_1
\end{equation*}
In terms of the periodogram, we have
\begin{equation*}
   I(j/n) = \frac{|b_j|^2}{n} \sim \frac{n \tau_j^2}{4} \chi^2_2 ~~ \text{ for } j = 1, \dots, m ~~ \text{ and } ~~~ I(1/2) = \frac{b_{m+1}^2}{n} \sim n \tau_{m+1}^2 \chi^2_1
\end{equation*}
The likelihood of the periodogram is then given by (up to constant)
\begin{equation*}
   \left(\prod_{j=1}^m \frac{1}{\tau_j^2} \right) \frac{1}{\tau_{m+1}} \exp \left(-\frac{2}{n} \sum_{j=1}^m \frac{I(j/n)}{\tau_j^2} - \frac{I(1/2)}{2n\tau^2_{m+1}}\right)
\end{equation*}
which implies that the negative log-likelihood is
\begin{equation*}
   \frac{2}{n} \sum_{j=1}^m \frac{I(j/n)}{\tau_j^2} + \frac{I(1/2)}{2n \tau_{m+1}^2} + 2 \sum_{j=1}^m \log \tau_j + \log \tau_{m+1}
\end{equation*}
Writing $\tau_j = e^{\alpha_j}$ or equivalently $\alpha_j = \log \tau_j$, we can rewrite the log-likelihood as
\begin{equation*}
    \frac{2}{n} \sum_{j=1}^m I(j/n) e^{-2\alpha_j} + \frac{1}{2n} I(1/2) e^{-2\alpha_{m+1}} + 2 \sum_{j=1}^m \alpha_j + \alpha_{m+1}.
\end{equation*}

Minimizing the above without regularization leads to
\begin{equation*}
   \alpha_j = \log \sqrt{\frac{2I(j/n)}{n}} ~~ \text{ for } j = 1, \dots, m ~~ \text{ and }~~ \alpha_{m+1} = \log \sqrt{\frac{I(1/2)}{n}}.
\end{equation*}
We therefore minimize the following:
\begin{equation*}
    \frac{2}{n} \sum_{j=1}^m I(j/n) e^{-2\alpha_j} + \frac{1}{2n} I(1/2) e^{-2\alpha_{m+1}} + 2 \sum_{j=1}^m \alpha_j + \alpha_{m+1} + \lambda \sum_{j=2}^{m-1} \left((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right)^2
\end{equation*}
or
\begin{equation*}
    \frac{2}{n} \sum_{j=1}^m I(j/n) e^{-2\alpha_j} + \frac{1}{2n} I(1/2) e^{-2\alpha_{m+1}} + 2 \sum_{j=1}^m \alpha_j + \alpha_{m+1} + \lambda \sum_{j=2}^{m-1} \left|(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right|.
\end{equation*}
Note that we are not including $\alpha_{m+1}$ in the penalty.

```python
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)
    # we are now including 1/2 in the set of Fourier frequencies
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m + 1]) ** 2) / n

    return fourier_freqs, pgram_y
```

```python
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)

    if n % 2 == 0: # even n
        fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)  # Includes 1/2
    else:  # odd n
        fourier_freqs = np.arange(1/n, 1/2, 1/n)  # Excludes 1/2

    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m + 1]) ** 2) / n

    return fourier_freqs, pgram_y
```

```python
freq, pgram = periodogram(y)

plt.figure(figsize = (12, 6))
#plt.plot(freq, np.log(pgram))
plt.plot(freq, pgram)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram))
plt.show()
```

*(1 figure omitted — see the original notebook.)*

What can be interpreted from the periodogram? The big peaks probably correspond to seasonal effects (this is a monthly dataset). Is there any information in the initial part of the periodogram. In these kinds of datasets, one often looks for evidence of "business cycles". Is it obvious to find such evidence from the periodogram?

```python
def spectrum_n_even_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    n = len(y) # Length of original time series (assumed to be even here)
    m = (n // 2) - 1

    alpha = cp.Variable(n // 2)

    I_1_to_m = I[0:(m - 1)]
    I_m_plus_1 = I[m]

    neg_likelihood_term_1_to_m = cp.sum(cp.multiply((2 * I_1_to_m / n), cp.exp(-2 * alpha[0:(m - 1)])) + 2 * alpha[0:(m - 1)])
    neg_likelihood_term_m_plus_1 = cp.multiply((I_m_plus_1 / (2 * n)), cp.exp(-2 * alpha[m])) + alpha[m]
    neg_likelihood_term = neg_likelihood_term_1_to_m + neg_likelihood_term_m_plus_1

    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))

    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()

    return alpha.value, freq
```

```python
alpha_opt_ridge, freq = spectrum_n_even_estimator_ridge(y, 5000)

---

[Up: contents](index.md) · [I found lambda = 5000 is reasonable here →](02-i-found-lambda-5000-is-reasonable-here.md)
