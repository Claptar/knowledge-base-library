---
title: 1 Stationarity of AR(1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyOne153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Stationarity of AR(1)

## Lecture Twenty One
### Spring 2025, UC Berkeley
### Aditya Guntuboyina
### April 10, 2025

In this lecture, we shall discuss stationarity of AR models. The answer is a bit complicated. Let us start with $\text{AR}(1)$ and then consider $\text{AR}(p)$ for $p \geq 2$.

The $\text{AR}(1)$ equation is
$$
y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t \tag{1}
$$
One issue is that this equation does not fully specify $y_t$ and there can be multiple processes $\{y_t\}$ that satisfy (1):

1. Suppose $y_0 = 10$. Define $y_1, y_2, y_3, \dots$ recursively via (1). Also define $y_{-1}, y_{-2}, y_{-3}, \dots$ recursively via the following equation for $t = 0, -1, -2, \dots$:
$$
y_{t-1} = -\frac{\phi_0}{\phi_1} + \frac{y_t}{\phi_1} - \frac{\epsilon_t}{\phi_1} \tag{2}
$$
Note that (2) is just a restatement of (1) obtained by rearranging (1) with $y_{t-1}$ on the left hand side. The resulting time series model will then clearly satisfy (1). However it will not be stationary because:
$$
\text{var}(y_0) = 0 \quad \text{and} \quad \text{var}(y_1) = \text{var}(\phi_0 + \phi_1 y_0 + \epsilon_1) = \text{var}(\phi_0 + \epsilon_1) = \text{var}(\epsilon_1) = \sigma^2.
$$

2. Suppose $|\phi_1| < 1$ and define
$$
y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^{\infty} \phi_1^j \epsilon_{t-j}. \tag{3}
$$
The summation in the right hand side above is an infinite summation, and hence we need to address convergence issues. Because $|\phi_1| < 1$, the terms $\phi_1^j$ rapidly decay to $0$ as $j$ increases. This ensures that $\sum_{j=0}^{\infty} \phi_1^j \epsilon_{t-j}$ is well-defined.

It is easy to check that (3) satisfies (1) because:
$$
\begin{aligned}
y_t &= \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j} \\
&= \frac{\phi_0}{1 - \phi_1} + \epsilon_t + \phi_1 \epsilon_{t-1} + \phi_1^2 \epsilon_{t-2} + \phi_1^3 \epsilon_{t-3} + \dots \\
&= \frac{\phi_0}{1 - \phi_1} + \epsilon_t + \phi_1 (\epsilon_{t-1} + \phi_1 \epsilon_{t-2} + \phi_1^2 \epsilon_{t-3} + \dots) \\
&= \frac{\phi_0}{1 - \phi_1} + \epsilon_t + \phi_1 \left( y_{t-1} - \frac{\phi_0}{1 - \phi_1} \right) = \phi_0 + \phi_1 y_{t-1} + \epsilon_t.
\end{aligned}
$$
It is also true that (3) is a stationary model. This is because
$$
\mathbb{E} y_t = \frac{\phi_0}{1 - \phi_1} \quad \text{for all } t
$$
and, for $h \geq 0$,
$$
\begin{aligned}
\text{cov}(y_t, y_{t+h}) &= \text{cov}\left(\frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}, \frac{\phi_0}{1 - \phi_1} + \sum_{k=0}^\infty \phi_1^k \epsilon_{t+h-k}\right) \\
&= \text{cov}\left(\sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}, \sum_{k=0}^\infty \phi_1^k \epsilon_{t+h-k}\right) = \sum_{j=0}^\infty \sum_{k=0}^\infty \phi_1^{j+k} \text{cov}(\epsilon_{t-j}, \epsilon_{t+h-k})
\end{aligned}
$$
Because $\text{cov}(\epsilon_{t-j}, \epsilon_{t+h-k})$ is non-zero (equal to $\sigma^2$) only when $t - j = t + h - k$ i.e., $k = j + h$, we get
$$
\text{cov}(y_t, y_{t+h}) = \sigma^2 \sum_{j=0}^\infty \phi_1^{2j+h} = \sigma^2 \frac{\phi_1^h}{1 - \phi_1^2}.
$$
This clearly shows that $\{y_t\}$ is stationary with ACVF and ACF given by:
$$
\gamma(h) = \sigma^2 \frac{\phi_1^{|h|}}{1 - \phi_1^2} \quad \text{and} \quad \rho(h) = \frac{\gamma(h)}{\gamma(0)} = \phi_1^{|h|}.
$$
We have thus proved that (3) is a stationary time series model that satisfies the $\text{AR}(1)$ equation (1) when $|\phi_1| < 1$. In fact, it turns out that (3) is the only stationary solution of (1) when $|\phi_1| < 1$ (I am skipping proof of this). Thus (3) is the unique stationary $\text{AR}(1)$ model when $|\phi_1| < 1$. The model (3) when $|\phi_1| < 1$ is known as the **causal stationary $\text{AR}(1)$ model**. Causal refers to the fact that $y_t$ is fully determined by present and past values of $\{\epsilon_t\}$.

3. Suppose $|\phi_1| > 1$ and define
$$
y_t = \frac{\phi_0}{1 - \phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}. \tag{4}
$$
Note that $y_t$ is well-defined because the infinite sum above has the coefficients $\phi_1^{-j}$ which decay rapidly as $|\phi_1| > 1$. It is easy to check that (4) also satisfies the $\text{AR}(1)$ equation (1) and is stationary. In fact, it is the unique stationary $\text{AR}(1)$ for $|\phi_1| > 1$. The model (4) is called the **non-causal, stationary $\text{AR}(1)$**. It is non-causal because $y_t$ depends on the future values of $\epsilon_{t+1}, \epsilon_{t+2}, \dots$.

For the model (4), it is certainly not true that $\epsilon_t$ is independent of $y_{t-1}, y_{t-2}, y_{t-3}, \dots$. Recall that we used this estimation while writing the likelihood for $\text{AR}(1)$ for parameter estimation. Thus, if we attempt to estimate the parameters $\phi_0, \phi_1, \sigma$ of (4) using our AR-parameter estimation technique, we will get incorrect an estimate of $\phi_1$ (for more details, see Example 3.3 and 3.4 in the Shumway-Stoffer book 4th edition).

To summarize the above discussion, there exist many non-stationary $\text{AR}(1)$ time series models. When $|\phi_1| < 1$, there exists a unique stationary $\text{AR}(1)$ model that is given by the formula (3), this is called the causal, stationary $\text{AR}(1)$ model. When $|\phi_1| > 1$, there also exists a unique stationary $\text{AR}(1)$ model that is given by the formula (4), this is called the non-causal, stationary $\text{AR}(1)$ model.

When $|\phi_1| = 1$ (i.e., $\phi_1 = 1$ or $\phi_1 = -1$), neither of the two formulae (3) and (4) are meaningful (i.e., the infinite series do not converge). Here it turns out that there is no stationary $\text{AR}(1)$ model. To see this, consider the case $\phi_1 = 1$ (the case $\phi_1 = -1$ is similar) where
$$
y_t = \phi_0 + y_{t-1} + \epsilon_t
$$
This implies that for every $t \geq 1$
$$
y_t - y_0 = t\phi_0 + \epsilon_1 + \dots + \epsilon_t
$$
When $\phi_0 \neq 0$, clearly $y_t$ and $y_0$ have different means (because $\mathbb{E}y_t = \mathbb{E}y_0 + t\phi_0$) so there is no stationarity. But even if $\phi_0 = 0$, we have
$$
\text{var}(y_t - y_0) = \text{var}(\epsilon_1 + \dots + \epsilon_t) = t\sigma^2
$$
which approaches $\infty$ as $t \uparrow \infty$. But if $\{y_t\}$ were stationary, we would have
$$
\text{var}(y_t - y_0) \leq 2\text{var}(y_t) + 2\text{var}(y_0) \leq \text{constant}.
$$

Thus there are two kinds of $\text{AR}(1)$: stationary and non-stationary. Stationarity is only possible when $|\phi_1| \neq 1$. There are also two kinds of stationary $\text{AR}(1)$ models. When $|\phi_1| < 1$, the stationary $\text{AR}(1)$ model has the formula (3); this is the causal kind of stationarity. When $|\phi_1| > 1$, the stationary $\text{AR}(1)$ model has the formula (4); this is the non-causal kind of stationarity.

---

[Up: contents](index.md) · [2 On the formulae for stationary AR(1) →](02-2-on-the-formulae-for-stationary-ar-1.md)
