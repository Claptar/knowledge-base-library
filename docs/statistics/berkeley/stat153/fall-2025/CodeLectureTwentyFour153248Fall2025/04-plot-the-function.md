---
title: Plot the function
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the function

**Source:** [`CodeLectureTwentyFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(x_vals, y_vals, label = 'True function g')
plt.plot(x_vals, ghat_nar, color = 'red', label = 'Fitted function by the Nonlinear AR model')
plt.title(r'$g(x) = \frac{2x}{1 + 0.8x^2}$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can also superimpose the fitted linear function by the usual AR(1) model.

```python
#Function fitted by AR(1)
from statsmodels.tsa.ar_model import AutoReg
ar = AutoReg(y_sim, lags = 1).fit()
print(ar.params)
ar_vals = ar.params[0] + ar.params[1] * x_vals

---

[← Plot the function](03-plot-the-function.md) · [Up: contents](index.md) · [Plot the function →](05-plot-the-function.md)
