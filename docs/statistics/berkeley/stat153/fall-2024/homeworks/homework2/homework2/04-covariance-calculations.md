---
title: Covariance calculations
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Covariance calculations

**Source:** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

7. (3 pts)
Let $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^m$ be random vectors, and let
$A \in \mathbb{R}^{k \times n}$ and $B \in \mathbb{R}^{\ell \times m}$ be fixed
matrices. Prove that
$$
\mathrm{Cov}(Ax, By) = A \mathrm{Cov}(x, y) B^T.
$$
Prove as a consequence that $\mathrm{Cov}(Ax) = A \mathrm{Cov}(x) A^T$. Hint:
you may use the rule for covariances of linear combinations (as reviewed in the
lecture from week 2, "Measures of dependence and stationarity").

8. (2 pts)
Suppose that $y = X \beta + \epsilon$, with $X$ and $\beta$ fixed, and where
$\epsilon$ is a vector with white noise entries, with variance $\sigma^2$. Use
the rule in Q7 to prove that for the sample least squares coefficients, namely,
$\hat\beta = (X^T X)^{-1} X^T y$, it holds that
$$
\mathrm{Cov}(\hat\beta) = \sigma^2 (X^T X)^{-1}.
$$

9. (4 pts)
An equivalent way to state the Gauss-Markov theorem is as follows. Under the
model from Q8, if $\tilde\beta$ is any other unbiased linear estimator of
$\beta$ (where linearity means that $\tilde\beta = My$ for a fixed matrix $M$)
then
$$
\mathrm{Cov}(\hat\beta) \lesssim \mathrm{Cov}(\tilde\beta)
$$
where $\lesssim$ means less than or equal to in the *PSD (positive semidefinite)
ordering*. Precisely, $A \lesssim B$ if and only if $B-A$ is a PSD matrix, which
recall, means $z^T (B-A) z \geq 0$ for all vectors $z$. Prove that this is
indeed equivalent to the statement of the Gauss-Markov theorem given in lecture.

---

[← Multiple regression](03-multiple-regression.md) · [Up: contents](index.md) · [Metrics matter →](05-metrics-matter.md)
