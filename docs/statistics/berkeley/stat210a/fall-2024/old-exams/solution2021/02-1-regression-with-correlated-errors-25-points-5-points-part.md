---
title: 1. Regression with correlated errors (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2021.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2021.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Regression with correlated errors (25 points, 5 points / part).

Some useful facts for this problem:
• For $\mu \in \mathbb{R}^n$ and positive definite $\Sigma \in \mathbb{R}^{n \times n}$, the density for $Z \sim N_n(\mu, \Sigma)$ is
$$p_{\mu,\Sigma}(z) = |2\pi\Sigma|^{-1/2} \exp\left\{ -\frac{1}{2}(z - \mu)'\Sigma^{-1}(z - \mu) \right\},$$
where $|\cdot|$ is the determinant (note the exponent of $1/2$ is correct; it should not be $n/2$). The mean is $\mu$ and the variance is $\Sigma$.

• If $Z \sim N_n(\mu, \Sigma)$, and $A \in \mathbb{R}^{k \times n}$ and $b \in \mathbb{R}^k$ are fixed, then
$$AZ + b \sim N_k(A\mu + b, A\Sigma A').$$

Suppose that for $i = 1, \ldots, n$ we observe fixed covariates $x_i \in \mathbb{R}^d$ and random response $Y_i = x_i'\beta + \varepsilon_i$, for coefficient vector $\beta \in \mathbb{R}^d$ and $\varepsilon_i \in \mathbb{R}$. The errors are multivariate Gaussian with mean zero and positive definite covariance matrix $\Sigma \in \mathbb{R}^{n \times n}$. In terms of the full response vector $Y \in \mathbb{R}^n$ and design matrix $X \in \mathbb{R}^{n \times d}$ with $i$th row $x_i'$, we have
$$Y = X\beta + \varepsilon, \quad \text{with } \varepsilon \sim N_n(0, \Sigma).$$
Assume $n \geq d \geq 1$ and $X$ has full column rank. For parts (a) and (b), we will assume $\Sigma$ is known and we want to estimate $\beta$. For (c)-(e) we will assume $\Sigma$ is unknown.

(a) Show that $Y$ follows a full-rank exponential family model and identify its complete sufficient statistic.

**Solution:**
We can write the density for $Y$ as
$$\begin{aligned}
p_\beta(y) &= |2\pi\Sigma|^{-1/2} \exp\left\{ -\frac{1}{2}(y - X\beta)'\Sigma^{-1}(y - X\beta) \right\} \\
&= \exp\left\{ \beta' X' \Sigma^{-1} y - \frac{1}{2}\beta' X' \Sigma^{-1} X\beta \right\} \cdot |2\pi\Sigma|^{-1/2} \exp\{-y'\Sigma^{-1}y/2\} \\
&= e^{\beta' T(y) - A(\beta)} h(y),
\end{aligned}$$
for $T(y) = X'\Sigma^{-1}y$, $h(y) = |2\pi\Sigma|^{-1/2} \exp\{-y'\Sigma^{-1}y/2\}$, and $A(\beta) = \beta' X' \Sigma^{-1} X\beta / 2$. Because the natural parameter $\beta$ can range over all of $\mathbb{R}^d$, the exponential family is full-rank and $T(Y)$ is complete.

---

(b) Find the maximum likelihood estimator of $\beta$ and give its distribution.

**Solution:**
The MLE for an exponential family sets
$$T(Y) = X'\Sigma^{-1}Y = \mathbb{E}_{\hat{\beta}} T(Y) = X'\Sigma^{-1}X\hat{\beta} \iff \hat{\beta} = (X'\Sigma^{-1}X)^{-1}X'\Sigma^{-1}Y.$$
Its distribution, using the formula given in the preamble, is
$$\hat{\beta} \sim N\left(\beta, (X'\Sigma^{-1}X)^{-1}\right).$$

(c) Now, for the remainder of the problem, suppose that $\Sigma$ is unknown so we have to estimate it. To facilitate this, we observe i.i.d. replicates $Y^{(k)}$ for $k = 1, \ldots, m$, with distribution
$$Y^{(k)} = X\beta + \varepsilon^{(k)}, \quad \text{with } \varepsilon^{(k)} \overset{\text{i.i.d.}}{\sim} N_n(0, \Sigma).$$
Note that $X$ and $\beta$ are the same for $k = 1, \ldots, m$ (they do not depend on $k$); only the errors change (and the responses change as a result). Define
$$\overline{Y} = \frac{1}{m} \sum_{k=1}^m Y^{(k)}, \quad \text{and} \quad \widehat{\Sigma} = \frac{1}{m - 1} \sum_{k=1}^m (Y^{(k)} - \overline{Y})(Y^{(k)} - \overline{Y})'.$$
Show that $\overline{Y}$ and $\widehat{\Sigma}$ are independent of each other.

**Solution:**
Consider the model with $Y^{(1)}, \ldots, Y^{(m)} \overset{\text{i.i.d.}}{\sim} N_n(\mu, \Sigma)$, with arbitrary $\mu \in \mathbb{R}^n$ and positive definite $\Sigma$. In the submodel where $\Sigma$ is known, $\Sigma^{-1}\overline{Y}$ is complete sufficient (applying part (a) with $X = I_n$) and $\widehat{\Sigma}$ is ancillary, so by Basu's theorem $\Sigma^{-1}\overline{Y}$, and therefore also $\overline{Y}$, is independent of $\widehat{\Sigma}$. The two statistics are therefore independent for any $\mu$ and $\Sigma$, so in particular they are independent if $\mu = X\beta$ for any $\Sigma$.

**Common mistake:** $\overline{Y}$ is not complete sufficient in the model with $\mu = X\beta$, for $d < n$.

(d) Show that $\widehat{\Sigma}$ is an unbiased estimator of $\Sigma$.

**Solution:**

---

Note that $Y^{(k)} - \overline{Y} = \varepsilon^{(k)} - \bar{\varepsilon}$. For every $i, j \in \{1, \ldots, d\}$ we have
$$\begin{aligned}
\mathbb{E} \widehat{\Sigma}_{ij} &= \frac{1}{m - 1} \mathbb{E}\left[ \sum_{k=1}^m (\varepsilon_i^{(k)} - \bar{\varepsilon}_i)(\varepsilon_j^{(k)} - \bar{\varepsilon}_j) \right] \\
&= \frac{m}{m - 1} \mathbb{E}\left[ \left( \frac{m-1}{m}\varepsilon_i^{(1)} - \frac{1}{m}\sum_{k>1} \varepsilon_i^{(k)} \right)\left( \frac{m-1}{m}\varepsilon_j^{(1)} - \frac{1}{m}\sum_{k>1} \varepsilon_j^{(k)} \right) \right] \\
&= \frac{m}{m - 1} \cdot \left[ \left(\frac{m-1}{m}\right)^2 \mathbb{E}\left[\varepsilon_i^{(1)}\varepsilon_j^{(1)}\right] + \sum_{k>1} \frac{1}{m^2}\mathbb{E}\left[\varepsilon_i^{(k)}\varepsilon_j^{(k)}\right] \right] \\
&= \mathbb{E}[\varepsilon_i^{(1)}\varepsilon_j^{(1)}] = \Sigma_{ij}.
\end{aligned}$$
An alternative way to do it is to observe that
\$\$\sum_{k=1}^m (\varepsilon^{(k)} - \bar{\varepsilon})(\varepsilon^{(k)} - \bar{\varepsilon})' = \left(\sum_{k=1}^

---

[← Final Examination: QUESTION BOOKLET](01-final-examination-question-booklet.md) · [Up: contents](index.md)
