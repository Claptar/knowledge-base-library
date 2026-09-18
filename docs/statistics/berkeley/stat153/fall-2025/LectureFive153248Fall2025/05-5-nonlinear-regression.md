---
title: 5 Nonlinear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 Nonlinear Regression

We shall next start our discussion on models in which certain parameters appear in a non-linear fashion. A simple example is:

$$
y_t = \beta_0 + \beta_1 t + \beta_2 \text{ReLU}(t - c) + \epsilon_t \tag{8}
$$

with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. Here $\text{ReLU}(t - c) = (t - c)_+$ equals $0$ if $t \le c$ and equals $t - c$ if $t \ge c$. We can also write

$$
\text{ReLU}(t - c) = (t - c)_+ = (t - c)I\{t > c\} = \max(t - c, 0).
$$

$(\cdot)_+$ is also called the positive part function, or, the ramp function.

The model (8) says that for times $t \le c$, the slope of the regression line is $\beta_1$, while for $t > c$, the slope changes to $(\beta_1 + \beta_2)$. We shall refer to (8) as the 'Change of Slope' model. An alternative name for this model is "Broken-stick regression". This is because the function

$$
t \mapsto \beta_0 + \beta_1 t + \beta_2 \text{ReLU}(t - c)
$$

resembles a broken stick.

The unknown parameters for this model are $c, \beta_0, \beta_1, \beta_2$ as well as $\sigma$. The unknown parameter $c$ makes (8) a nonlinear regression model. If $c$ were known, then (8) would be a linear regression model:

$$
y = X_c \beta + \epsilon \tag{9}
$$

with

$$
X_c = \begin{pmatrix}
1 & 1 & \text{ReLU}(1 - c) \\
1 & 2 & \text{ReLU}(2 - c) \\
1 & 3 & \text{ReLU}(3 - c) \\
\cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot \\
1 & n & \text{ReLU}(n - c)
\end{pmatrix} \quad \text{and } \beta := \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{pmatrix} \text{ and } \epsilon = \begin{pmatrix} \epsilon_1 \\ \epsilon_2 \\ \cdot \\ \cdot \\ \cdot \\ \epsilon_n \end{pmatrix}.
$$

## 5.1 Estimation of $c, \beta_0, \beta_1, \beta_2, \sigma$

Least squares again is the most basic estimation procedure. The sum of squares is given by:

$$
S(\beta_0, \beta_1, \beta_2, c) := \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2 \text{ReLU}(t - c))^2.
$$

We need to minimize this over all the four variables $\beta_0, \beta_1, \beta_2, c$. Using matrix notation, we can write

$$
S(\beta, c) = \|y - X_c \beta\|^2.
$$

If we fix $c$, then it is easy to minimize $S(\beta, c)$ over $\beta$. This is the same as linear regression and the minimizing $\beta$ is given by:

\$\$
\hat{\beta}_c := (X_c^T X_c)^{-1} X_c

---

[← 4 Proof of (4)](04-4-proof-of-4.md) · [Up: contents](index.md)
