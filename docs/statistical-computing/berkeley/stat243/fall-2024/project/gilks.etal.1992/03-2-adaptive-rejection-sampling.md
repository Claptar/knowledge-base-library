---
title: 2. Adaptive Rejection Sampling
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf
source_file: sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/gilks.etal.1992.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. Adaptive Rejection Sampling

To set the scene we begin by describing standard (non-adaptive) rejection sampling.

## 2.1. Non-adaptive Rejection Sampling

Rejection sampling is a general method for sampling points independently from a density $f(x)$. The density need be specified only up to a constant of integration, i.e. rejection sampling may be performed by using $g(x)$ instead of $f(x)$, where $g(x) = cf(x)$ for some possibly unknown value of $c$. This is particularly useful when $c = \int_D g(x) \, dx$ is not available in closed form (where $D$ denotes the domain of $f(x)$, i.e. the set of $x$ for which $f(x) > 0$).

To sample $n$ points independently from $f(x)$ by rejection sampling, define an envelope function $g_u(x)$ such that $g_u(x) \geqslant g(x)$ for all $x$ in $D$, and optionally define also a squeezing function $g_l(x)$ such that $g_l(x) \leqslant g(x)$ for all $x$ in $D$. Then perform the following sampling step until $n$ points have been accepted.

Sample a value $x^*$ from $g_u(x)$, and sample a value $w$ independently from the $\text{uniform}(0, 1)$ distribution. If you have defined a $g_l(x)$-function, perform the following squeezing test: if
$$w \leqslant g_l(x^*)/g_u(x^*)$$
then accept $x^*$. Otherwise evaluate $g(x^*)$ and perform the following rejection test: if
$$w \leqslant g(x^*)/g_u(x^*)$$
then accept $x^*$; otherwise reject $x^*$. Repeat until $n$ points have been accepted.

Rejection sampling is only useful if it is more efficient or convenient to sample from the envelope $g_u(x)$ than from the density $f(x)$ itself. In practice, finding a suitable $g_u(x)$ can be difficult and often involves locating the supremum of $g(x)$ in $D$ by using a standard optimization technique.

## 2.2. Adaptive Rejection Sampling

For Gibbs sampling, usually only one sample is required from each density, although sampling from many thousands of different densities may be required. Moreover, when estimating a model involving non-conjugacy, evaluations of $g(x)$ may be computationally expensive. These points are elaborated in Section 3. In these circumstances rejection sampling may be very inefficient, since it may involve many thousands of optimizations, each involving several evaluations of a $g(x)$ function.

Adaptive rejection sampling reduces the number of evaluations of $g(x)$ in two ways. Firstly, through the assumption of log-concavity of $f(x)$, we avoid the need to locate the supremum of $g(x)$ in $D$. Secondly, after each rejection, the probability of needing to evaluate $g(x)$ further is reduced by updating the envelope and squeezing functions to incorporate the most recently acquired information about $g(x)$.

We now describe our method in more detail. We assume that $D$ is connected, that $g(x)$ is continuous and differentiable everywhere in $D$ and that $h(x) = \ln g(x)$ is concave everywhere in $D$ (i.e. $h'(x) = dh(x)/dx$ decreases monotonically with increasing $x$ in $D$). This definition of log-concavity admits both straight line segments in $h(x)$ and discontinuities in $h'(x)$. The continuous curve in Fig. 1 exemplifies a concave $h(x)$ in a domain $D$.

Suppose that $h(x)$ and $h'(x)$ have been evaluated at $k$ abscissae in $D$: $x_1 \leqslant x_2 \leqslant \dots \leqslant x_k$. Let $T_k = \{x_i; \, i = 1, \dots, k\}$. We define the rejection envelope on $T_k$ as $\exp u_k(x)$ where $u_k(x)$ is a piecewise linear upper hull formed from the tangents to $h(x)$ at the abscissae in $T_k$, in the manner of the upper broken curve of Fig. 1. For $j = 1, \dots, k - 1$ the tangents at $x_j$ and $x_{j+1}$ intersect at
$$z_j = \frac{h(x_{j+1}) - h(x_j) - x_{j+1} h'(x_{j+1}) + x_j h'(x_j)}{h'(x_j) - h'(x_{j+1})}. \tag{1}$$

Thus for $x \in [z_{j-1}, z_j]$ and $j = 1, \dots, k$, we define
$$u_k(x) = h(x_j) + (x - x_j) h'(x_j) \tag{2}$$
where $z_0$ is the lower bound of $D$ (or $-\infty$ if $D$ is not bounded below) and $z_k$ is the upper bound of $D$ (or $+\infty$ if $D$ is not bounded above). We also define
$$s_k(x) = \exp u_k(x) \Big/ \int_D \exp u_k(x') \, dx'. \tag{3}$$

Finally, we define the squeezing function on $T_k$ as $\exp l_k(x)$, where $l_k(x)$ is a piecewise linear lower hull formed from the chords between adjacent abscissae in $T_k$, in the manner of the lower broken curve of Fig. 1. Thus for $x \in [x_j, x_{j+1}]$
$$l_k(x) = \frac{(x_{j+1} - x) h(x_j) + (x - x_j) h(x_{j+1})}{x_{j+1} - x_j} \tag{4}$$
for $j = 1, \dots, k - 1$. For $x < x_1$ or $x > x_k$ we define $l_k(x) = -\infty$.

Thus the rejection envelope and the squeezing function are piecewise exponential functions. The concavity of $h(x)$ ensures that $l_k(x) \leqslant h(x) \leqslant u_k(x)$ for all $x$ in $D$.

To sample $n$ points independently from $f(x)$ by adaptive rejection sampling, perform the following initialization step, and then perform the following sampling and updating steps alternately until $n$ points have been accepted.

### 2.2.1. Initialization step
Initialize the abscissae in $T_k$. If $D$ is unbounded on the left then choose $x_1$ such that $h'(x_1) > 0$. If $D$ is unbounded on the right then choose $x_k$ such that $h'(x_k) < 0$. Having defined $k$ starting abscissae, calculate the functions $u_k(x)$, $s_k(x)$ and $l_k(x)$ from equations (2), (3) and (4) respectively.

### 2.2.2. Sampling step
Sample a value $x^*$ from $s_k(x)$ and sample a value $w$ independently from the $\text{uniform}(0, 1)$ distribution. Perform the following squeezing test: if
$$w \leqslant \exp\{l_k(x^*) - u_k(x^*)\}$$
then accept $x^*$. Otherwise evaluate $h(x^*)$ and $h'(x^*)$ and perform the following rejection test: if
$$w \leqslant \exp\{h(x^*) - u_k(x^*)\}$$
then accept $x^*$; otherwise reject $x^*$.

### 2.2.3. Updating step
If $h(x^*)$ and $h'(x^*)$ were evaluated at the sampling step, include $x^*$ in $T_k$ to form $T_{k+1}$; relabel the elements of $T_{k+1}$ in ascending order; construct the functions $u_{k+1}(x)$, $s_{k+1}(x)$ and $l_{k+1}(x)$ from equations (2), (3) and (4) respectively on the basis of $T_{k+1}$; increment $k$. Return to the sampling step if $n$ points have not yet been accepted.

Fig. 1. A concave log-density $h(x)$, bounded on the left, showing upper and lower hulls based on three abscissae $(x_1, x_2, x_3)$: ——, $h(x)$; - - -, upper hull; $\cdots\cdots$, lower hull

Fig. 1. A concave log-density $h(x)$, bounded on the left, showing upper and lower hulls based on three abscissae $(x_1, x_2, x_3)$: ——, $h(x)$; - - -, upper hull; $\cdots\cdots$, lower hull

## 2.3. Proof of Adaptive Rejection Sampling

The proof that adaptive rejection sampling leads to independent samples from $f(x)$ is straightforward. Let $x_r^*$ denote the $r\text{th}$ sampled value of $x$, whether or not it was accepted or included in $T_k$. Let
$$\delta_r = \begin{cases}
0 & \text{if } x_r^* \text{ was accepted at the squeezing test,} \\
1 & \text{if } x_r^* \text{ was accepted at the rejection test,} \\
2 & \text{if } x_r^* \text{ was rejected.}
\end{cases}$$
Let $H_r$ denote the history of the process, up to and including the processing of $x_r^*$: so $H_r = \{(x_i^*, \delta_i); \, i = 1, \dots, r\}$. Thus $H_r$ defines the current upper and lower hulls.

Let $[\ ]$ generically denote a conditional probability density function. Then
$$[(x_{r+1}^* = x) \cap (\delta_{r+1} \ne 2) \mid H_r] = \exp h(x) \Big/ \int_D \exp u_k(x') \, dx'$$
and so
$$[x_{r+1}^* = x \mid H_r \cap (\delta_{r+1} \ne 2)] = \exp h(x) \Big/ \int_D \exp h(x') \, dx' = f(x)$$
which does not depend on $H_r$. Thus accepted values of $x$ are drawn independently from $f(x)$.

## 2.4. Efficiency

Suppose that $k$ evaluations of $h(x)$ and $h'(x)$ have been performed. Suppose also that the current $x^*$ has not been accepted at the squeezing step. Then the probability that $x^* = x$ is proportional to $\exp u_k(x) - \exp l_k(x)$. Thus new evaluations of $h(x)$ and $h'(x)$ are most likely to occur at values of $x$ where the rejection envelope and squeezing function are most discrepant. Therefore the method tends to space evaluations of $h(x)$ and $h'(x)$ optimally.

The number of evaluations of $h(x)$ and $h'(x)$ needed to sample a value from $f(x)$ could be sensitive to the initial choice of $T_k$. We examine this empirically in Table 1, for the standard normal density and with two starting abscissae. Widely separated starting abscissae are only modestly detrimental, and the optimum starting abscissae are around $-1$ and $+1$. Asymmetry in the starting abscissae has little impact on the number of evaluations of $h(x)$ and $h'(x)$. In general we have found two starting abscissae ($k = 2$) to be necessary and sufficient for computational efficiency.

Empirically, the number of evaluations of $h(x)$ and $h'(x)$ required to sample $n$ points from $f(x)$ increases approximately in proportion to $\sqrt[3]{n}$, even for quite non-normal densities. To sample 100 points from the standard normal distribution about 15 evaluations of $h(x)$ and $h'(x)$ are required; to sample 1000 points about 30 evaluations of $h(x)$ and $h'(x)$ are required.

---

[← 1. Introduction](02-1-introduction.md) · [Up: contents](index.md) · [3. Adaptive Rejection Sampling and Gibbs Sampling →](04-3-adaptive-rejection-sampling-and-gibbs-sampling.md)
