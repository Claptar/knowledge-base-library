---
title: 3 Recurrent Neural Networks (RNNs)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Recurrent Neural Networks (RNNs)

We are now ready to define an RNN. RNN will involve one modification of the second equation in (7). Specifically, we will take $s_t$ to be a linear function not only of $x_t$ but also of the feature vector $r_{t-1}$ at the previous time. This leads to (the difference relative to (7) is highlighted in blue below)
$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
s_t &= W_r r_{t-1} + W x_t + b \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{8}$$

In Model (7), the hidden layer output $r_t$ is computed purely from the current input $x_t$ through a linear transformation ($s_t$) and the nonlinearity $\sigma(\cdot)$, so $r_t$ depends only on $x_t$. In the RNN (8) however, the computation of $r_t$ involves not just the current $x_t$ but also the previous hidden layer output $r_{t-1}$ through an additional linear term $W_r r_{t-1}$. This means that in the second model, the feature vector $r_t$ is influenced both by the current input and by the feature vector from the previous step, whereas in the first model, it is influenced only by the current input.

Model (7) is a standard single-hidden layer feedforward neural network where the hidden layer $r_t$ depends only on the current input. In contrast, the second model RNN (8) introduces a **recurrent connection** by adding a term $W_r r_{t-1}$ to the hidden layer input, meaning that $r_t$ now depends not only on the current input $x_t$ but also on the previous hidden state $r_{t-1}$. This recurrence creates a form of memory across time steps, making the second model a recurrent neural network (RNN), while the first model has no memory and treats each input independently.

The matrix $W_r$ is $k \times k$ so it is a square matrix. The parameters now include $W_r, W, b, \beta_0, \beta$ (along with the noise standard deviation $\sigma$). Typically $k$ will be larger than $p$. Model (8) also requires an initialization of $r_t$ usually done by $r_0 = 0$.

In the model (7), the feature vector $r_t$ depends only on $x_t$. On the other hand, in (8), $r_t$ depends on all the inputs: $x_t, x_{t-1}, \dots, x_1$ (or $x_t, x_{t-1}, \dots, x_{p+1}$ in case $x_t = (y_{t-1}, \dots, y_{t-p})^T$ is not defined for $t \le p$; below we assume that the inputs $x_t$ are defined for all $t = 1, 2, \dots$ without loss of generality; in a time series setting, this can be arranged by rearranging the time index). To see how $r_t$ depends on $x_t, x_{t-1}, \dots$, note that
$$\begin{aligned}
r_1 &= \sigma(W x_1 + b) \quad \text{because } r_0 = 0 \\
r_2 &= \sigma(W_r \sigma(W x_1 + b) + W x_2 + b), \\
r_3 &= \sigma(W_r \sigma(W_r \sigma(W x_1 + b) + W x_2 + b) + W x_3 + b), \\
r_4 &= \sigma(W_r \sigma(W_r \sigma(W_r \sigma(W x_1 + b) + W x_2 + b) + W x_3 + b) + W x_4 + b).
\end{aligned} \tag{9}$$
From the above, $r_t$ clearly depends on all of $x_1, \dots, x_t$. But the strength of the dependence of $r_t$ on $x_s$ varies with $s$.

RNNs can have stability issues because the formula for $r_t$ involves the product of a possibly large number of terms where the matrix $W_r$ appears multiple times (e.g., see the formula (9) for $r_4$ above). Imagining $W_r$ to be a scalar (just for the sake of making this argument), then two things can happen: it can be strictly larger than 1 in magnitude or strictly smaller than 1 in magnitude (it cannot be exactly equal to 1 in magnitude because these parameters are learning by a training algorithm and it is unlikely that this algorithm will output an estimate of $W_r$ that is exactly equal to 1 in magnitude). If $W_r$ is strictly larger than 1 in magnitude, then multiple appearances of $W_r$ in products will blow them up, causing $r_t$ to explode for moderate and large $t$. On the other hand, if $W_r$ is strictly smaller than 1 in magnitude, then the products will be very small, and this leads to $r_t$ depending mainly on $x_s$ for which $s$ is close to $t$ (the implication is that RNNs cannot capture long-range dependence). When $W_r$ is a matrix (instead of a scalar), this argument will still hold but, instead of magnitude, we need to use the spectral radius of $W_r$ (spectral radius of a square matrix is defined as the largest magnitude of any eigenvalue).

The nonlinear activation function $\sigma(\cdot)$ also appears multiple times in the formula for $r_t$, (see again the formula (9) for $r_4$). To solve stability problems, it is customary in RNNs to take $\sigma$ to be the hyperbolic tangent function (instead of ReLU). The hyperbolic tangent function is given by
$$\sigma(u) := \frac{e^u - e^{-u}}{e^u + e^{-u}}.$$
Unlike the ReLU function (which can take arbitrarily large positive values), the hyperbolic tangent activation function always takes values between $-1$ and 1. This helps the RNN be more stable.

We will discuss the RNNs more next week (along with related models such as GRU and LSTM).

## 4 Parameter Estimation via PyTorch

Given a time series dataset $y_1, \dots, y_n$, we estimate the parameters of these models simply by least squares. Specifically the parameters are estimated by minimizing:
$$\sum_{t=1}^n (y_t - \mu_t)^2. \tag{10}$$
Note that $\mu_t$ depends on the parameters $W, W_r \dots$ so that these parameters need to be chosen so that the sum of squares above is as small as possible. Minimization of (10) is done in an iterative fashion using a simple algorithm such as gradient descent. This requires calculation of gradients which is done efficiently in PyTorch. This also requires an initial value of the parameters.

## 5 Additional Optional Reading

1. Read the wikipedia article for Recurrent Neural Networks: https://en.wikipedia.org/wiki/Recurrent_neural_network. Our RNN model (8) is referred to as the Elman network in this wiki article.
2. For more on RNNs, I recommend the paper https://arxiv.org/abs/1808.03314.

---

[← 2 AutoRegression](02-2-autoregression.md) · [Up: contents](index.md)
