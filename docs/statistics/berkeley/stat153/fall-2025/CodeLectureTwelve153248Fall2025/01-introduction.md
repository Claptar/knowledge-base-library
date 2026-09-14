---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Bayesian Regularization
---

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import cvxpy as cp
```

Let us consider the temperature anomalies dataset that we already used in the last lecture.

```python
temp_jan = pd.read_csv('TempAnomalies_January.csv', skiprows=4)
print(temp_jan.head())
y = temp_jan['Anomaly']
plt.plot(y)
plt.xlabel('year')
plt.ylabel('Celsius')
plt.title('Temperature anomalies (from 1901-2000 average) for January')
plt.show()
```

```
Year  Anomaly
0  1850    -0.46
1  1851    -0.17
2  1852    -0.02
3  1853    -0.12
4  1854    -0.28
```

*(1 figure omitted — see the original notebook.)*

The $X$ matrix for our high-dimensional regression model is calculated as follows.

```python
n = len(y)
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n), x-1])
for i in range(n-2):
    c = i+2
    xc = ((x > c).astype(float))*(x-c)
    X = np.column_stack([X, xc])
print(X)
```

```
[[  1.   0.  -0. ...  -0.  -0.  -0.]
 [  1.   1.   0. ...  -0.  -0.  -0.]
 [  1.   2.   1. ...  -0.  -0.  -0.]
 ...
 [  1. 173. 172. ...   1.   0.  -0.]
 [  1. 174. 173. ...   2.   1.   0.]
 [  1. 175. 174. ...   3.   2.   1.]]
```

### Posterior corresponding to Normal Prior

Consider the prior $\beta \sim N(0, Q)$ along with likelihood given by $N(X \beta, \sigma^2 I)$. The posterior of $\beta$ (given the data and $\sigma$) is then:
\begin{align*}
   \beta \mid \text{data}, \sigma \sim N \left(\left(\frac{X^T
                          X}{\sigma^2} + Q^{-1}  \right)^{-1} \frac{X^T y}{\sigma^2},  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}\right).
\end{align*}
Given $\tau$ (and a large positive $C$), we take $Q$ to be the diagonal matrix with diagonals $C, C, \tau^2, \dots, \tau^2$. The code below computes the posterior mean:
\begin{equation*}
   \left(\frac{X^T
                          X}{\sigma^2} + Q^{-1}  \right)^{-1} \frac{X^T y}{\sigma^2}.
\end{equation*}
for fixed $C$, $\tau$ and $\sigma$.

```python

---

[Up: contents](index.md) · [Posterior mean of beta with fixed tau and sig →](02-posterior-mean-of-beta-with-fixed-tau-and-sig.md)
