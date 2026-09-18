---
title: 2 AutoRegression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 AutoRegression

We also studied autoregression models where the covariates are simply lagged values of $y_t$. The simplest of these models is AR(1) where $x_t = y_{t-1}$. This is simply (1) with $t$ replaced by $x_t = y_{t-1}$:
$$y_t = \beta_0 + \beta_1 x_t + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2).$$
One can create a nonlinear version of AR(1) by simply using (3) with $x_t = y_{t-1}$. We shall refer to this as Nonlinear AutoRegression of order 1: NAR(1) (there are many nonlinear autoregression models and this one is only one of them):
$$\begin{aligned}
x_t &= y_{t-1} \\
s_t &= (x_t - c_1, \dots, x_t - c_k)^T \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{4}$$
Now let us consider the case of AR($p$) for $p \ge 1$. The usual AR($p$) model is simply:
$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
\mu_t &= \beta_0 + \beta^T x_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{5}$$
Observe that (5) can be written in compressed form as simply $y_t = \beta_0 + \beta_1 y_{t-1} + \dots + \beta_p y_{t-p} + \epsilon_t$ which is the usual form of AR($p$).

What is a natural nonlinear version of (5)? Put another way, what is a good extension of (4) for $p \ge 1$? There are multiple ways of obtaining these versions. Looking at the structure of (4), clearly $x_t = y_{t-1}$ will be replaced by $x_t = (y_{t-1}, \dots, y_{t-p})^T$. The next line gives the formula for $s_t$. This would need to be changed because $x_t$ is no longer a scalar. One way to do this would be to write one version of the formula for $s_t$ in (4) for each component of $x_t$. This would result in:
$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
s_t &= (x_{t1} - c_1^{(1)}, \dots, x_{t1} - c_k^{(1)}, x_{t2} - c_1^{(2)}, \dots, x_{t2} - c_k^{(2)}, \dots, x_{tp} - c_1^{(p)}, \dots, x_{tp} - c_k^{(p)})^T \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{6}$$

Here $x_{t1} = y_{t-1}, \dots, x_{tp} = y_{t-p}$ denote the components of $x_t$. With this choice of $s_t$, note that $\mu_t$ becomes
$$\mu_t = \beta_0 + \beta^T r_t = \beta_0 + \beta^T \sigma(s_t) = \beta_0 + \sum_{j=1}^p g_j(x_{tj}) \quad \text{where } g_j(x) := \sum_{i=1}^k \beta_{i,j} \sigma(x_{tj} - c_j^{(i)}).$$
In other words, we are fitting an **additive model** for $y_t$ in terms of the covariates $x_{t1} = y_{t-1}, \dots, x_{tp} = y_{t-p}$. Additive models are popular in regression but they do not incorporate any interactions between the covariates. For example, if the true model generating the data is $y_t = 0.5 y_{t-1} y_{t-2} + \epsilon_t$, the additive model is unlikely to work well (because $(x_1, x_2) \mapsto 0.5 x_1 x_2$ is not an additive function of $x_1$ and $x_2$).

Instead of using the additive model in (6), we shall use the following model as NAR($p$) (Nonlinear AutoRegression of order $p$). This is obtained by changing the second line of (6) to be an arbitrary linear function of $x_t$:
$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
s_t &= W x_t + b \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{7}$$
Here $W$ is a $k \times p$ matrix and $b$ is a $k \times 1$ vector. The parameters in this model are the entries of the matrix $W$, the vector $b$, the coefficients $\beta_0$ and the components of $\beta$ and finally the noise standard deviation $\sigma$.

In neural network terminology, the model (7) is called a **single-hidden layer neural network** because it first applies a linear transformation to the input $x_t$ (via $s_t = W x_t + b$), then passes the result through the nonlinear activation function $\sigma$ to get $r_t$, which forms the hidden layer. The output $\mu_t$ is then computed as a linear function of $r_t$ (via $\mu_t = \beta_0 + \beta^T r_t$) and noise $\epsilon_t$ is added to explain the discrepancy between $y_t$ and $\mu_t$. The presence of one nonlinear transformation between the input $x_t$ and the output $\mu_t$, combined with otherwise linear operations, is exactly the structure of a single-hidden layer neural network.

To sum up, we take the single-hidden layer neural network model (7) to be our nonlinear generalization of AR($p$).

Note that (7) can also be treated as a linear regression model but the linearity is in terms of the feature vector $r_t$ (not in terms of the original covariate $x_t$). We shall refer to $r_t$ as the feature vector at time $t$, it is also common to refer to it as the hidden layer output at time $t$.

---

[← 1 Regression with $t$ as covariate](01-1-regression-with-as-covariate.md) · [Up: contents](index.md) · [3 Recurrent Neural Networks (RNNs) →](03-3-recurrent-neural-networks-rnns.md)
