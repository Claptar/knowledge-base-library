---
title: note that the true value of f is 0.2035, b0 is 0, b1 is 3, b2 is 5 and sigma
  is 10
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# note that the true value of f is 0.2035, b0 is 0, b1 is 3, b2 is 5 and sigma is 10

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
0            1            2            3            4
count  2000.000000  2000.000000  2000.000000  2000.000000  2000.000000
mean      0.203554    -0.048116     2.926668     5.487344     9.567343
std       0.000154     0.479084     1.240482     0.894120     0.337935
min       0.203045    -2.282401    -1.430247     1.670873     8.564508
25%       0.203435    -0.359168     2.134556     4.928442     9.343711
50%       0.203555    -0.061192     3.009265     5.519098     9.567323
75%       0.203645     0.268955     3.769393     6.097100     9.787657
max       0.204095     1.614744     6.128241     8.477974    10.710101
```

## Change-point Model

The same method can be used for inference in other nonlinear models. For example, consider the following model:
\begin{equation*}
   y_t = \beta_0 + \beta_1 I\{t > c\} + \epsilon_t.
\end{equation*}
This is known as a change-point model. The parameter $c$ is called the change-point. $I\{t > c\}$ is the **indicator** function which takes the value 1 if $t > c$ and 0 otherwise. The function $\beta_0 + \beta_1 I\{t > c\}$ equals $\beta_0$ for times $t \leq c$ and equals $\beta_0 + \beta_1$ for times $t > c$. Therefore this model states that the level of the time series equals $\beta_0$ until a time $c$ at which point it switches to $\beta_0 + \beta_1$. The value of $c$ is therefore called the changepoint. From the given data $y_1, \dots, y_n$, we need to infer the parameter $c$ as well as $\beta_0, \beta_1, \sigma$. The unknown parameter $c$ makes it a nonlinear model. If $c$ were known, this will become a linear regression model with $X$-matrix given by
\begin{equation*}
    X_c = \begin{pmatrix} 1 & I\{1 > c\} \\ 1 & I\{2 > c\} \\ 1 & I\{3 > c\} \\ \cdot & \cdot \\ \cdot & \cdot \\ \cdot & \cdot \\ 1 & I\{n > c\} \end{pmatrix}
\end{equation*}

Inference for the parameter $c$ proceeds just like before. We first compute RSS($c$):
\begin{equation*}
    RSS(c) := \min_{\beta_0, \beta_1} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 I\{t > c\})^2
\end{equation*}
and then minimize over $c$ to obtain the MLE of $\hat{c}$. After finding $\hat{c}$, we can find the MLEs of the other parameters as in linear regression with known $c$.

```python

---

[← sig is the true value of sigma which generated the data](06-sig-is-the-true-value-of-sigma-which-generated-the-data.md) · [Up: contents](index.md) · [Here is a simulated dataset having a change point →](08-here-is-a-simulated-dataset-having-a-change-point.md)
