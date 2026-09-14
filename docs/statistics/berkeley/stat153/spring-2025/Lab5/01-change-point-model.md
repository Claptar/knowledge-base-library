---
title: Change-point model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Change-point model

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Consider the following model:
\begin{equation*}
   y_t = \beta_0 + \beta_1 I\{t > c\} + \epsilon_t.
\end{equation*}
This is known as a change-point model. The parameter $c$ is called the change-point. $I\{t > c\}$ is the **indicator** function which takes the value 1 if $t > c$ and 0 otherwise. The function $\beta_0 + \beta_1 I\{t > c\}$ equals $\beta_0$ for times $t \leq c$ and equals $\beta_0 + \beta_1$ for times $t > c$. Therefore this model states that the level of the time series equals $\beta_0$ until a time $c$ at which point it switches to $\beta_0 + \beta_1$. The value of $c$ is therefore called the changepoint. From the given data $y_1, \dots, y_n$, we need to infer the parameter $c$ as well as $\beta_0, \beta_1, \sigma$. The unknown parameter $c$ makes it a nonlinear model. If $c$ were known, this will become a linear regression model with $X$-matrix given by
\begin{equation*}
    X_c = \begin{pmatrix} 1 & I\{1 > c\} \\ 1 & I\{2 > c\} \\ 1 & I\{3 > c\} \\ \cdot & \cdot \\ \cdot & \cdot \\ \cdot & \cdot \\ 1 & I\{n > c\} \end{pmatrix}
\end{equation*}

For parameter estimation and inference, we first compute RSS($c$):
\begin{equation*}
    RSS(c) := \min_{\beta_0, \beta_1} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 I\{t > c\})^2
\end{equation*}
and then minimize over $c$ to obtain the MLE of $\hat{c}$. After finding $\hat{c}$, we can find the MLEs of the other parameters as in linear regression with known $c$.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python

---

[Up: contents](index.md) · [Here is a simulated dataset having a change point →](02-here-is-a-simulated-dataset-having-a-change-point.md)
