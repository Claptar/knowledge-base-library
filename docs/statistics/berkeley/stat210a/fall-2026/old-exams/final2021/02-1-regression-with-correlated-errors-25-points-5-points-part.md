---
title: 1. Regression with correlated errors (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2021.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2021.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Regression with correlated errors (25 points, 5 points / part).

Some useful facts for this problem:
- For $\mu \in \mathbb{R}^n$ and positive definite $\Sigma \in \mathbb{R}^{n \times n}$, the density for $Z \sim N_n(\mu, \Sigma)$ is
$$p_{\mu,\Sigma}(z) = |2\pi\Sigma|^{-1/2} \exp\left\{ -\frac{1}{2} (z - \mu)' \Sigma^{-1} (z - \mu) \right\},$$
where $|\cdot|$ is the determinant (note the exponent of $1/2$ is correct; it should not be $n/2$). The mean is $\mu$ and the variance is $\Sigma$.
- If $Z \sim N_n(\mu, \Sigma)$, and $A \in \mathbb{R}^{k \times n}$ and $b \in \mathbb{R}^k$ are fixed, then
$$AZ + b \sim N_k(A\mu + b, A\Sigma A').$$

Suppose that for $i = 1, \dots, n$ we observe fixed covariates $x_i \in \mathbb{R}^d$ and random response $Y_i = x_i'\beta + \varepsilon_i$, for coefficient vector $\beta \in \mathbb{R}^d$ and $\varepsilon_i \in \mathbb{R}$. The errors are multivariate Gaussian with mean zero and positive definite covariance matrix $\Sigma \in \mathbb{R}^{n \times n}$. In terms of the full response vector $Y \in \mathbb{R}^n$ and design matrix $X \in \mathbb{R}^{n \times d}$ with $i$th row $x_i'$, we have
$$Y = X\beta + \varepsilon, \quad \text{with } \varepsilon \sim N_n(0, \Sigma).$$
Assume $n \ge d \ge 1$ and $X$ has full column rank. For parts (a) and (b), we will assume $\Sigma$ is known and we want to estimate $\beta$. For (c)-(e) we will assume $\Sigma$ is unknown.

(a) Show that $Y$ follows a full-rank exponential family model and identify its complete sufficient statistic.

(b) Find the maximum likelihood estimator of $\beta$ and give its distribution.

(c) Now, for the remainder of the problem, suppose that $\Sigma$ is unknown so we have to estimate it. To facilitate this, we observe i.i.d. replicates $Y^{(k)}$ for $k = 1, \dots, m$, with distribution
$$Y^{(k)} = X\beta + \varepsilon^{(k)}, \quad \text{with } \varepsilon^{(k)} \overset{\text{i.i.d.}}{\sim} N_n(0, \Sigma).$$
Note that $X$ and $\beta$ are the same for $k = 1, \dots, m$ (they do not depend on $k$); only the errors change (and the responses change as a result). Define
$$\overline{Y} = \frac{1}{m} \sum_{k=1}^m Y^{(k)}, \quad \text{and } \widehat{\Sigma} = \frac{1}{m-1} \sum_{k=1}^m (Y^{(k)} - \overline{Y})(Y^{(k)} - \overline{Y})'.$$
Show that $\overline{Y}$ and $\widehat{\Sigma}$ are independent of each other.

(d) Show that $\widehat{\Sigma}$ is an unbiased estimator of $\Sigma$.

(e) Now assume $n = d$. Is $\widehat{\Sigma}$ UMVU? Why or why not?

---

Problem 1 answers continued (1):

---

Problem 1 answers continued (2):

---

Problem 1 answers continued (3):

---

---

[← Final Examination: QUESTION BOOKLET](01-final-examination-question-booklet.md) · [Up: contents](index.md) · [2. Contamination model (25 points, 5 points / part). →](03-2-contamination-model-25-points-5-points-part.md)
