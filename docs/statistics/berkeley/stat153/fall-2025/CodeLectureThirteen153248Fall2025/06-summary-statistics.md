---
title: Summary statistics
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Summary statistics

**Source:** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(df_gamma_sigma.describe())
```

## Variance Models

Next we shall study variance models (mainly in the context of spectral analysis). To illustrate the main ideas, we first consider the following simple model:
\begin{equation*}
   y_t \overset{\text{independent}}{\sim} N(0, \tau_t^2)
\end{equation*}
We discuss estimation of $\tau_1, \dots, \tau_n$  under the assumption that they are smooth in some sense. We shall discuss estimation next week. For now, let us simulate some data from this model to see how they look like.

Below are two simulation settings for this variance model.

### Simulation 1

```python
#Simulate data from this variance model:
n = 400
tvals = np.arange(1, n+1)
th = -0.8
tau_t = np.sqrt((1 + (th ** 2) + 2*th*np.cos(2 * np.pi * (tvals)/n))) #this is a smooth function of t
y = rng.normal(loc = 0, scale = tau_t)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Simulation 2

Here is the second simulation setting for this model. We take the following smooth function $\alpha_t$ and then generate $\tau_t$ as $\exp(\alpha_t)$.

```python
def smoothfun(x):
    ans = np.sin(15*x) + np.exp(-(x ** 2)/2) + 0.5*((x - 0.5) ** 2) + 2*np.log(x + 0.1)
    return ans

n = 2000
xx = np.linspace(0, 1, n)
alpha_true = np.array([smoothfun(x) for x in xx])
plt.figure(figsize = (12, 6))
plt.plot(alpha_true)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
tau_t = np.exp(alpha_true)
y = rng.normal(loc = 0, scale = tau_t)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here are two common features about these simulated datasets:
1. The data $y_1, \dots, y_n$ would oscillate around zero, with clusters of small values when $\tau_t$ is small and bursts of large values when $\tau_t$ is large.
2. Because $\log \tau_t = \alpha_t$ is smooth, the standard deviation $\tau_t$ changes gradually, not abruptly -- so the data would exhibit smooth heteroscedasticity: periods of calm and periods of volatility, but with slow transitions.

There exist real datasets (particularly from finance) which also display these characteristics. Below is one example.

### A real dataset from finance for which this variance model is applicable

Next, we examine a real dataset where this variance model may be applicable. The dataset consists of stock price data for the S&P 500 mutual fund, downloaded from Yahoo Finance using the yfinance library.

```python
import yfinance as yf
```

```python

---

[← Summary statistics](05-summary-statistics.md) · [Up: contents](index.md) · [Download S&P 500 data →](07-download-s-p-500-data.md)
