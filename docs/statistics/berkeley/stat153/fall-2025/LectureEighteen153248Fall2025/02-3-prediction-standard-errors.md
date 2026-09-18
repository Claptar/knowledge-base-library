---
title: 3 Prediction Standard Errors
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Prediction Standard Errors

To compute prediction standard errors, we can again fix the parameter values $\theta$, and then attempt to calculate:
$$V_i(\theta) := \text{var}(y_{n+i} \mid y_1, \dots, y_n, \theta) \quad \text{for } i = 1, 2, \dots$$
The prediction standard error corresponding to the predicted value for $y_{n+i}$ can then be taken to be $\sqrt{V_i(\hat{\theta})}$ (note that $\theta$ is replaced by the conditional MLE $\hat{\theta}$).

It turns out that it is not really possible to setup a recursion for $V_i(\theta)$. To see this, note that:
$$\begin{aligned}
V_1(\theta) &= \text{var}(y_{n+1} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_0 + \phi_1 y_n + \phi_2 y_{n-1} + \dots + \phi_p y_{n+1-p} + \epsilon_{n+1} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\epsilon_{n+1} \mid y_1, \dots, y_n, \theta) = \sigma^2.
Next
$$\begin{aligned}
V_2(\theta) &= \text{var}(y_{n+2} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_0 + \phi_1 y_{n+1} + \phi_2 y_n + \dots + \phi_p y_{n+2-p} + \epsilon_{n+2} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_1 y_{n+1} + \epsilon_{n+2} \mid y_1, \dots, y_n, \theta) \\
&= \phi_1^2 \text{var}(y_{n+1} \mid y_1, \dots, y_n, \theta) + \text{var}(\epsilon_{n+2} \mid y_1, \dots, y_n, \theta) \\
&= \phi_1^2 V_1(\theta) + \sigma^2 = \sigma^2(1 + \phi_1^2).
The next term is
$$\begin{aligned}
V_3(\theta) &= \text{var}(y_{n+3} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_0 + \phi_1 y_{n+2} + \phi_2 y_{n+1} + \dots + \phi_p y_{n+3-p} + \epsilon_{n+3} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_1 y_{n+2} + \phi_2 y_{n+1} + \epsilon_{n+3} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_1 y_{n+2} + \phi_2 y_{n+1} \mid y_1, \dots, y_n, \theta) + \text{var}(\epsilon_{n+3} \mid y_1, \dots, y_n, \theta).
The first term in the right hand side above cannot be written down in terms of $V_1(\theta)$ and $V_2(\theta)$ alone. It also involves the covariance between $y_{n+1}$ and $y_{n+2}$ (given $y_1, \dots, y_n, \theta$).

Instead of working with the variances alone, we will get the recursion by working with the conditional covariance matrices of $y_{n+1}, \dots, y_{n+k}$ (given $\theta$ and the data) for $k = 1, 2, \dots$.

Below we review some basic facts about covariance matrices.

## 3.1 Covariance Matrices

A finite number of random variables can be viewed together as a random vector. More precisely, a random vector is a vector whose entries are random variables. Let $Y = (Y_1, \dots, Y_n)^T$ be an $n \times 1$ random vector. Its Expectation $\mathbb{E}Y$ is defined as a vector whose $i$th entry is the expectation of $Y_i$ i.e., $\mathbb{E}Y = (\mathbb{E}Y_1, \mathbb{E}Y_2, \dots, \mathbb{E}Y_n)^T$. The covariance matrix of $Y$, denoted by $\text{Cov}(Y)$, is an $n \times n$ matrix whose $(i, j)$th entry is the covariance between $Y_i$ and $Y_j$. Two important but easy facts about $\text{Cov}(Y)$ are:

1. The diagonal entries of $\text{Cov}(Y)$ are the variances of $Y_1, \dots, Y_n$. More specifically the $(i, i)$th entry of the matrix $\text{Cov}(Y)$ equals $\text{var}(Y_i)$.
2. $\text{Cov}(Y)$ is a symmetric matrix i.e., the $(i, j)$th entry of $\text{Cov}(Y)$ equals the $(j, i)$ entry. This follows because $\text{Cov}(Y_i, Y_j) = \text{Cov}(Y_j, Y_i)$.

The following formulae are very important:

1. $\mathbb{E}(AY + c) = A\mathbb{E}(Y) + c$ for every deterministic matrix $A$ and every deterministic vector $c$.
2. $\text{Cov}(AY + c) = A\text{Cov}(Y)A^T$ for every deterministic matrix $A$ and every deterministic vector $c$.

As a consequence of the second formula above, we get
$$\text{var}(a^T Y) = a^T \text{Cov}(Y)a = \sum_{i,j} a_i a_j \text{Cov}(Y_i, Y_j) \quad \text{for every } p \times 1 \text{ vector } a.$$

Given two random vectors $Y$ ($p \times 1$) and $W$ ($q \times 1$), we use $\text{Cov}(Y, W)$ to denote the $p \times q$ matrix whose $(i, j)$th entry equals the covariance $\text{Cov}(Y_i, W_j)$ between $Y_i$ and $W_j$. With this definition, the previous notion of $\text{Cov}(Y)$ equals simply $\text{Cov}(Y, Y)$. It can be checked that
$$\text{Cov}(AY + c, BW + d) = A\text{Cov}(Y, W)B^T.$$

## 3.2 Covariance Recursion in AR($p$)

We shall set up a recursion for the covariance matrices:
$$\Gamma_k(\theta) := \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k} \end{pmatrix} \;\middle|\; \theta, y_1, \dots, y_n\right)$$
The $(i, j)$th entry of $\Gamma_k(\theta)$ is
$$\text{Cov}(y_{n+i}, y_{n+j} \mid y_1, \dots, y_n, \theta).$$
The diagonal entries of $\Gamma_k(\theta)$ equal $V_1(\theta), \dots, V_k(\theta)$.

To initialize the recursion for $\Gamma_k(\theta)$, note that
$$\begin{aligned}
\Gamma_1(\theta) &= \text{var}(y_{n+1} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\phi_0 + \phi_1 y_n + \dots \phi_p y_{n+1-p} + \epsilon_{n+1} \mid y_1, \dots, y_n, \theta) \\
&= \text{var}(\epsilon_{n+1} \mid y_1, \dots, y_n, \theta) = \sigma^2
We now relate $\Gamma_{k+1}(\theta)$ to $\Gamma_k(\theta)$ to establish the recursion. We can write
$$\Gamma_k(\theta) = \begin{pmatrix} \Gamma_{k-1}(\theta) & \gamma_{k1}(\theta) \\ \gamma_{k1}^T(\theta) & V_k(\theta) \end{pmatrix}$$
where
$$\gamma_{k1}(\theta) := \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix}, y_{n+k} \;\middle|\; \theta, y_1, \dots, y_n\right)$$
and, as before,
$$V_k(\theta) = \text{var}(y_{n+k} \mid \theta, y_1, \dots, y_n).$$
We compute $\hat{\gamma}_{k1}$ as
$$\begin{aligned}
\gamma_{k1}(\theta) &:= \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix}, y_{n+k} \;\middle|\; \theta, y_1, \dots, y_n\right) \\
&= \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix}, \phi_0 + \phi_1 y_{n+k-1} + \phi_2 y_{n+k-2} + \dots + \phi_p y_{n+k-p} + \epsilon_{n+k} \;\middle|\; \theta, \text{data}\right) \\
&= \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix}, \phi_1 y_{n+k-1} + \phi_2 y_{n+k-2} + \dots + \phi_p y_{n+k-p} \;\middle|\; \theta, \text{data}\right) \\
&= \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix}, \sum_{i=1}^{k-1} a_i y_{n+i} \;\middle|\; \theta, \text{data}\right)
where, for $i = 1, \dots, k - 1$,
$$a_i = \begin{cases} \phi_{k-i} & \text{provided } k - p \le i \le k - 1 \\ 0 & \text{otherwise} \end{cases}$$
Thus if $a$ is the $(k - 1) \times 1$ vector with entries $a_1, \dots, a_{k-1}$, we have
$$\gamma_{k1}(\theta) = \text{Cov}\left(\begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix}, a^T \begin{pmatrix} y_{n+1} \\ \cdot \\ \cdot \\ \cdot \\ y_{n+k-1} \end{pmatrix} \;\middle|\; \theta, \text{data}\right) = \Gamma_{k-1}(\theta)a.$$
Further
$$\begin{aligned}
V_k(\theta) &= \text{var}(y_{n+k} \mid \theta, \text{data}) \\
&= \text{var}(\phi_0 + \phi_1 y_{n+k-1} + \phi_2 y_{n+k-2} + \dots + \phi_p y_{n+k-p} + \epsilon_{n+k} \mid \theta, \text{data}) \\
&= \text{var}(\phi_0 + \phi_1 y_{n+k-1} + \phi_2 y_{n+k-2} + \dots + \phi_p y_{n+k-p} \mid \theta, \text{data}) + \sigma^2 \\
&= \text{var}\left(\sum_{i=1}^{k-1} a_i y_{n+i} \;\middle|\; \theta, \text{data}\right) + \sigma^2 = a^T \Gamma_{k-1}(\theta)a + \sigma^2.
The equation for obtaining $\Gamma_k(\theta)$ from $\Gamma_{k-1}(\theta)$ is therefore
$$\Gamma_k(\theta) = \begin{pmatrix} \Gamma_{k-1}(\theta) & \gamma_{k1}(\theta) \\ \gamma_{k1}^T(\theta) & V_k(\theta) \end{pmatrix} = \begin{pmatrix} \Gamma_{k-1}(\theta) & \Gamma_{k-1}(\theta)a \\ a^T \Gamma_{k-1}(\theta) & a^T \Gamma_{k-1}(\theta)a + \sigma^2 \end{pmatrix}$$
The algorithm for calculating the variances $V_i(\theta)$ for $i = 1, 2, \dots, K$ is thus given by

1. Initialize with $\Gamma_1(\theta) = V_1(\theta) = \sigma^2$.
2. For $k = 2, 3, \dots, K$, repeat the following
   a) Form the $(k - 1) \times 1$ vector $a$ whose $i^{\text{th}}$ entry is $\phi_{k-i}$ if $k - p \le i \le k - 1$ and $0$ otherwise.
   b) Calculate $\Gamma_k(\theta)$ using $\Gamma_{k-1}(\theta)$ and $a$ by the formula given above.
3. The variances $V_i(\theta), i = 1, 2, \dots, K$ are given by the diagonal entries of the matrix $\Gamma_K(\theta)$.

Because $\theta$ is unknown, in practice, we run this recursion with $\theta$ replaced by its conditional MLE $\hat{\theta}$. The prediction standard errors are then the square roots of $V_i(\hat{\theta})$. These prediction errors coincide with those given by the `get_prediction` function in statsmodels.

---

[← 1 AR models: estimation, inference and prediction](01-1-ar-models-estimation-inference-and-prediction.md) · [Up: contents](index.md)
