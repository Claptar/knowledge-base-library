---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyTwo153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyTwo153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

## Lecture Twenty Two
### Spring 2025, UC Berkeley

Aditya Guntuboyina

April 15, 2025

In the past few lectures, we studied the $\text{MA}(q)$ and $\text{AR}(p)$ models which are reviewed below.

## 1 $\text{MA}(q)$

The $\text{MA}(q)$ model is given by:
$$y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q}$$
where, as always, $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. This process is always stationary. Its ACF $\rho(h)$ equals 0 when $|h| > q$. The ACF is therefore considered a signature for the $\text{MA}(q)$ model. Given an observed time series dataset $y_1, \dots, y_n$, one can decide whether to fit an MA model to the data by looking at the sample acf of the data. If the sample acf seems to become negligible after a certain lag $q$, then the $\text{MA}(q)$ would be a good model for the dataset.

## 2 $\text{AR}(p)$

The $\text{AR}(p)$ model is defined by the equation:
$$y_t - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p} = \phi_0 + \epsilon_t \tag{1}$$
This is an implicit definition in the sense that $y_t$ is defined as any set of random variables that satisfy (1). There are, in fact, multiple solutions to (1).

Whether $\text{AR}(p)$ is stationary or not depends on the exact values of the parameters $\phi_1, \dots, \phi_p$, and also on which solution to (1) is being considered.

### 2.1 $p = 1$

Consider $p = 1$ when the equation is given by:
$$y_t - \phi_1 y_{t-1} = \phi_0 + \epsilon_t. \tag{2}$$
Here it is quite easy to answer questions of stationarity by separately considering the following three regimes:

1. $|\phi_1| < 1$: Here (2) admits a unique stationary solution that is given by the formula:
$$y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}. \tag{3}$$
Note that the infinite series above is well-defined because $|\phi_1| < 1$ which means that the powers $\phi_1^j$ decay rapidly. The process (3) has the property that $\epsilon_t$ is independent of $y_{t-1}, y_{t-2}, \dots$. The process (3) is referred to as **causal stationary $\text{AR}(1)$**.

2. $|\phi_1| > 1$: Here (2) admits a unique stationary solution that is given by the formula:
$$y_t = \frac{\phi_0}{1 - \phi_1} - \sum_{j=0}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}. \tag{4}$$
This infinite series is also well-defined because the powers $\phi_1^{-j}$ decay rapidly as $|\phi_1| > 1$. For (4), it is no longer true that $\epsilon_t$ is independent of $y_{t-1}, y_{t-2}, \dots$. Instead it is true that $\epsilon_t$ is independent of $y_{t+1}, y_{t+2}, \dots$. The process (4) is referred to as the **non-causal stationary $\text{AR}(1)$**.

3. $|\phi_1| = 1$: Here (2) does not have a stationary solution. $|\phi_1| = 1$ refers to either $\phi_1 = 1$ or $\phi_1 = -1$. Of these two, the case $\phi_1 = 1$ is more commonly used. When $\phi_1$, the equation (2) becomes
$$y_t - y_{t-1} = \phi_0 + \epsilon_t. \tag{5}$$
This means that the **differenced series** $y_t - y_{t-1}$ is Gaussian white noise (plus a constant $\phi_0$). When $\phi_0 = 0$, (5) is called the Random Walk model.

The $\text{AR}(1)$ stationary solutions (3) (causal) and (4) (non-causal) can be derived directly from the defining equation (2) using Backshift calculus as follows. $B$ denotes the Backshift operator satisfying $B^k y_t = y_{t-k}$, $k$ here can be any integer positive or negative or zero (when $k = 0$, we denote $B^0$ by simply 1). The $\text{AR}(1)$ equation, in backshift notation, becomes $\phi(B)y_t = \phi_0 + \epsilon_t$ where $\phi(z) = 1 - \phi_1 z$ and $\phi(B) = 1 - \phi_1 B$ (here $I = B^0$ is the identity operator). This means that
$$y_t = \frac{1}{\phi(B)} (\phi_0 + \epsilon_t).$$
We now make sense of $1/\phi(B)$. For this, we use the following:
$$\frac{1}{1 - r} = 1 + r + r^2 + r^3 + \dots$$
which gives
$$\frac{1}{\phi(B)} = \frac{1}{1 - \phi_1 B} = 1 + \phi_1 B + \phi_1^2 B^2 + \dots = \sum_{j=0}^\infty \phi_1^j B^j$$
so that
$$y_t = \frac{1}{\phi(B)} (\phi_0 + \epsilon_t) = \sum_{j=0}^\infty \phi_1^j B^j (\phi_0 + \epsilon_t) = \sum_{j=0}^\infty \phi_1^j B^j (\phi_0) + \sum_{j=0}^\infty \phi_1^j B^j (\epsilon_t) = \sum_{j=0}^\infty \phi_1^j + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}.$$
The above infinite sums only make sense when $|\phi_1| < 1$, and we get
$$y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}$$
which gives us the causal stationary solution (3).

When $|\phi_1| > 1$, this definition of $1/\phi(B)$ does not lead to anything meaningful. Here, there is a different formula that can be used for $1/\phi(B)$. This comes from:
$$\frac{1}{1 - r} = -\frac{1}{r} \frac{1}{1 - (1/r)} = -\frac{1}{r} \left( 1 + \frac{1}{r} + \frac{1}{r^2} + \dots \right) = -\sum_{j=1}^\infty r^{-j}.$$
This gives
$$\frac{1}{\phi(B)} = -\sum_{j=1}^\infty \frac{B^{-j}}{\phi_1^j}$$
and so
$$\frac{1}{\phi(B)} (\phi_0 + \epsilon_t) = -\phi_0 \sum_{j=1}^\infty \frac{1}{\phi_1^j} - \sum_{j=1}^\infty \frac{B^{-j} \epsilon_t}{\phi_1^j} = \frac{\phi_0}{1 - \phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}$$
which is the non-causal stationary $\text{AR}(1)$ in (4).

To recap, we have the following two formulae:
$$\frac{1}{1 - \phi_1 B} = \sum_{j=0}^\infty \phi_1^j B^j \quad \text{and} \quad \frac{1}{1 - \phi_1 B} = -\sum_{j=1}^\infty \frac{B^{-j}}{\phi_1^j}. \tag{6}$$
When $|\phi_1| < 1$, we use the first formula because it results in the powers $\phi_1^j$ which decay rapidly with $j$. When $|\phi_1| > 1$, we use the second formula because it results in powers $\phi_1^{-j}$ which again decay rapidly with $j$.

When $|\phi_1| = 1$, then neither of the two formulae in (6) lead to rapidly decaying coefficients (in other words, neither (3) nor (4) make sense). This is reasonable because, as was mentioned last class, (2) does not have a stationary solution when $|\phi_1| = 1$.

### 2.2 $p \ge 1$

The backshift method actually works for every $p \ge 1$ and gives us correct answers for causal, non-causal stationary regimes of $\text{AR}(p)$. In backshift notation, the $\text{AR}(p)$ difference equation becomes
$$\phi(B) y_t = \phi_0 + \epsilon_t \quad \text{where } \phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p.$$
We can therefore 'solve' it by writing
$$y_t = \frac{1}{\phi(B)} \epsilon_t = \frac{1}{1 - \phi_1 B - \dots - \phi_p B^p} \epsilon_t$$
The next step is to make sense of $1/(1 - \phi_1 B - \dots - \phi_p B^p)$. It is natural here to factorize the polynomial $1 - \phi_1 B - \dots - \phi_p B^p$ into monomials, and then use (6). So we write
$$\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p = (1 - a_1 z) \dots (1 - a_p z). \tag{7}$$
so that
$$\phi(B) = (1 - a_1 B) \dots (1 - a_p B).$$
The numbers $a_1, \dots, a_p$ appearing in (7) are simply the reciprocals of the roots of $\phi(z)$ i.e., the roots of $\phi(z)$ are given by $1/a_1, \dots, 1/a_p$. Note here that some of the $a_j$'s can be complex because the polynomial $1 - \phi_1 z - \dots - \phi_p z^p$ can have complex roots (even though all its coefficients are real).

We then get
$$y_t = \frac{1}{(1 - a_1 B) \dots (1 - a_p B)} (\phi_0 + \epsilon_t) = \prod_{k=1}^p \frac{1}{1 - a_k B} (\phi_0 + \epsilon_t).$$
For $1/(1 - a_j B)$, we use (6). Specifically, if $|a_j| < 1$, we use the first formula in (6) and when $|a_j| > 1$, we use the second formula in (6) (when $a_j$ is complex, $|a_j|$ denotes its modulus). Thus we get
$$y_t = \prod_{k:|a_k|<1} \left( \sum_{j=0}^\infty a_k^j B^j \right) \prod_{k:|a_k|>1} \left( \sum_{j=1}^\infty \frac{B^{-j}}{a_k^j} \right) (\phi_0 + \epsilon_t). \tag{8}$$
Suppose now that every $|a_k|$ is strictly smaller than 1. Then
$$\begin{aligned}
y_t &= \prod_k \left( \sum_{j=0}^\infty a_k^j B^j \right) (\phi_0 + \epsilon_t) \\
&= \left( \sum_{j_1=0}^\infty a_1^{j_1} B^{j_1} \right) \dots \left( \sum_{j_p=0}^\infty a_p^{j_p} B^{j_p} \right) (\phi_0 + \epsilon_t) \\
&= \left( \sum_{j_1=0}^\infty \dots \sum_{j_p=0}^\infty a_1^{j_1} \dots a_p^{j_p} B^{j_1 + \dots + j_p} \right) (\phi_0 + \epsilon_t) \\
&= \phi_0 \sum_{j_1=0}^\infty \dots \sum_{j_p=0}^\infty a_1^{j_1} \dots a_p^{j_p} + \sum_{j_1=0}^\infty \dots \sum_{j_p=0}^\infty a_1^{j_1} \dots a_p^{j_p} \epsilon_{t - j_1 - \dots - j_p}.
\end{aligned}$$
Because each $a_k$ above was assumed to have modulus strictly smaller than 1, the series above involves rapidly decaying powers of $a_k$ so it makes sense. The formula above writes $y_t$ in terms of $\epsilon_t, \epsilon_{t-1}, \dots$. It can be checked that this is a causal, stationary solution. By collecting terms where $j_1 + \dots + j_p = j$ for each $j = 0, 1, \dots$, we can write this solution as
$$y_t = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$$
for some $\mu, \psi_1, \psi_2, \dots$.

If $|a_k| > 1$ for even one $k$, then it is easy to see that (8) would give
$$y_t = \mu + \sum_{j=-\infty}^\infty \psi_j \epsilon_{t-j}$$
for some $\psi_j, j = \dots, -3, -2, -1, 0, 1, 2, 3, \dots$. In this case, the formula for $y_t$ involves future values of $\epsilon_t$ so this is a non-causal stationary solution.

Finally if $|a_k| = 1$ even for one $k$, then we cannot make sense of $1/(1 - a_k B)$ (both the formulae in (6) fail to work). This hints that a stationary solution might not exist in this regime. This indeed turns out to be true.

Here is a summary of the discussion above: To determine the nature of the solutions of the $\text{AR}(p)$ equation (1), first compute the roots $z_1, \dots, z_p$ of $\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p$ and set $a_j = 1/z_j$ for $j = 1, \dots, p$.

1. If $|a_k| \neq 1$ for every $k$ (i.e., no root of $\phi(z)$ has modulus equal to 1), then there exists a unique stationary solution to (1).

---

[Up: contents](index.md)
