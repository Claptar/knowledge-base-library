---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFive153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureFive153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Linear Regression and Uncertainty Quantification
---

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

### Squares Function Plotting

Given some data $y_1, \dots, y_n$ that are not all equal, consider the squares function:
\begin{align*}
   S(\theta) := \sum_{i=1}^n (y_i - \theta)^2.
\end{align*}
This function will be minimized at $\hat{\theta} = (y_1 + \dots + y_n)/n$. The code below plots this function for some data $y_1, \dots, y_n$.

```python
y = np.array([1, 0, 2, -2, 5])
theta_hat = np.mean(y)
#Below is the squares function S(theta) := sum_i (y_i - theta)^2
def S(theta):
    return np.sum((y - theta)**2)
```

```python

---

[Up: contents](index.md) · [Plot S(theta) →](02-plot-s-theta.md)
