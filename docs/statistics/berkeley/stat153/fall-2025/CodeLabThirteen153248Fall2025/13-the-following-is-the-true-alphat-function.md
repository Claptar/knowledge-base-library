---
title: the following is the true alphat function
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# the following is the true alphat function

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def smoothfun(x):
    ans = np.sin(15 * x) + np.exp(-(x ** 2)/2) + 0.5 * ((x - 0.5) ** 2) + 2 * np.log(x + 0.1)
    return ans

n = 2000
xx = np.linspace(0, 1, n)
alpha_true = np.array([smoothfun(x) for x in xx])

plt.figure(figsize = (12, 6))
plt.plot(alpha_true)
plt.title('True Smooth Function (alpha)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We generate data from the above true function using the model: $y_t \overset{\text{ind}}{\sim} N(0, \tau_t^2)$ where $\tau_t = \exp(\alpha_t)$.

```python

---

[← First fix the number of knots](12-first-fix-the-number-of-knots.md) · [Up: contents](index.md) · [Generating Data using the above smooth function →](14-generating-data-using-the-above-smooth-function.md)
