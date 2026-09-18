---
title: 2 $t$-density
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 $t$-density

The formula for the density corresponding to the $t$-distribution $t_p(\mu, \Sigma, \nu)$ is (see (https://en.wikipedia.org/wiki/Multivariate_t-distribution):

$$
\begin{aligned}
f(x) &:= \frac{\Gamma((\nu + p)/2)}{\Gamma(\nu/2)\nu^{p/2}\pi^{p/2}\sqrt{\det \Sigma}} \left[ 1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1}(x - \mu) \right]^{-(\nu+p)/2} \\
&\propto \left[ 1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1}(x - \mu) \right]^{-(\nu+p)/2}.
\end{aligned} \tag{3}
$$

Here:

1. $p$ denotes dimension of the vector $x$ (this is a $p$-variate joint density)
2. $\mu$ is a $p \times 1$ vector called the location
3. $\Sigma$ is a $p \times p$ matrix called the scale matrix
4. $\nu > 0$ denotes the degrees of freedom.

Here is some more information about the $t$-density (3):

1. **Connection to the Multivariate Normal Density:** The most important term in the formula (3) is $(x - \mu)^T \Sigma^{-1}(x - \mu)$. This exact term also appears in the multivariate normal density. If $X \sim N(\mu, \Sigma)$, then the density of $X$ is given by:

$$
\frac{1}{(2\pi)^{p/2}\sqrt{\det \Sigma}} \exp \left( -\frac{1}{2}(x - \mu)^T \Sigma^{-1}(x - \mu) \right).
$$

This suggests that the $t$-density is closely related to the multivariate normal density. Here is the connection. Suppose $X \sim N_p(\mu, \Sigma)$ and $V \sim \chi_\nu^2$ (this is the chi-squared distribution with $\nu$ degrees of freedom) are independent. Then

$$
T := \mu + \frac{X - \mu}{\sqrt{V/\nu}} \sim t_p(\mu, \Sigma, \nu). \tag{4}
$$

Thus, in the notation $t_p(\mu, \Sigma, \nu)$, $\nu$ denotes degrees of freedom, $p$ denotes dimension, $\mu$ and $\Sigma$ denote the mean vector and covariance matrix of the corresponding normal random vector $X$. For completeness, we include a proof of (4) in Section 4.

2. **Individual Components as well as Linear Combinations of Components of $T$ are also $t$-distributed:** Suppose $T \sim t_p(\mu, \Sigma, \nu)$ and the components of $T$ are $T_1, \dots, T_p$. Then each individual component $T_j$ is also $t$-distributed. Also every linear combination $a_0 + a_1 T_1 + a_2 T_2 + \dots + a_p T_p$ is also $t$-distributed. To see this, first write

$$
a_0 + a_1 T_1 + \dots + a_p T_p = a_0 + a^T T
$$

where $a$ is the $p \times 1$ vector with components $a_1, \dots, a_p$. Using the formula (4), we can write

$$
a_0 + a^T T = (a_0 + a^T \mu) + \frac{(a_0 + a^T X) - (a_0 + a^T \mu)}{\sqrt{V/\nu}}
$$

Because $a_0 + a^T X \sim N(a_0 + a^T \mu, a^T \Sigma a)$, the same fact (4) applied to this case gives:

$$
a_0 + a^T T \sim t_1(a_0 + a^T \mu, a^T \Sigma a, \nu).
$$

In particular, this implies that for each $j = 1, \dots, p$,

$$
T_j \sim t_1(\mu_j, \Sigma(j, j), \nu)
$$

where $\mu_j$ is the $j$th component of $\mu$ and $\Sigma(j, j)$ is the $(j, j)$th entry of $\Sigma$.

3. **When $\nu$ is large, $t$ is very close to normal:** This can intuitively be seen by noting that when $\nu$ is large, the term $(x - \mu)^T \Sigma^{-1}(x - \mu)/\nu$ is small so that

$$
1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1}(x - \mu) \approx \exp \left( \frac{1}{\nu}(x - \mu)^T \Sigma^{-1}(x - \mu) \right),
$$

where we used the observation that $1 + z \approx e^z$ when $z$ is small. Thus the $t$-density (3) for large $\nu$ becomes approximately:

$$
\exp \left( -\frac{\nu + p}{2\nu}(x - \mu)^T \Sigma^{-1}(x - \mu) \right) \approx \exp \left( -\frac{1}{2}(x - \mu)^T \Sigma^{-1}(x - \mu) \right)
$$

because $\frac{\nu+p}{\nu} \approx 1$ when $\nu$ is large. This gets us the normal density:

$$
t_p(\mu, \Sigma, \nu) \approx N_p(\mu, \Sigma) \quad \text{if } \nu \text{ is large.}
$$

In our regression case, the degrees of freedom is $n - m - 1$ where $n$ is the number of observations, and $m$ is the number of covariates. Thus if $n - m - 1$ is large, then the posterior distribution (which is actually $t$) is approximately normal:

$$
t_{m+1} \left( \hat{\beta}, \frac{S(\hat{\beta})}{n - m - 1}(X^T X)^{-1}, n - m - 1 \right) \approx N_{m+1} \left( \hat{\beta}, \frac{S(\hat{\beta})}{n - m - 1}(X^T X)^{-1} \right).
$$

---

[← 1 Posterior $t$-density in Multiple Linear Regression](01-1-posterior--density-in-multiple-linear-regression.md) · [Up: contents](index.md) · [3 Back to Regression →](03-3-back-to-regression.md)
