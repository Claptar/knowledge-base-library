---
title: Simulation 2
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Simulation 2

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

---

[← Bayesian Regularization (with a slightly different prior)](04-bayesian-regularization-with-a-slightly-different-prior.md) · [Up: contents](index.md) · [A real dataset from finance for which this variance model is applicable →](06-a-real-dataset-from-finance-for-which-this-variance-model-is.md)
