---
title: Homework6 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/homework/homework6.tex
source_file: sources/berkeley-stat210a/fall-2024/homework/homework6.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework6 Part 01 —

**Source:** [`homework/homework6.tex`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/homework/homework6.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Effective degrees of freedom). We can write a standard Gaussian sequence model in the form $$Y_i = \mu_i + \varepsilon_i, \quad \varepsilon_i \overset{\text{i.i.d.}}{\sim}N(0,\sigma^2), \quad i = 1,\ldots,n$$ with $\mu\in\mathbb{R}^n$ and $\sigma^2 > 0$ possibly unknown. If we estimate $\mu$ by some estimator $\hat\mu(Y)$, we can compute the residual sum of squares (RSS): $$\text{RSS}(\hat\mu,Y) = \|\hat\mu(Y)-Y\|^2 = \sum_{i=1}^n (\hat\mu_i(Y) - Y_i)^2.$$ If we were to observe the same signal with independent noise $Y^* = \mu + \varepsilon^*$, the expected prediction error (EPE) is defined as $$\text{EPE}(\mu,\hat\mu) = \mathbb{E}_\mu\left[\| \hat\mu(Y) - Y^*\|^2\right] = \mathbb{E}_\mu\left[\|\hat\mu(Y)-\mu\|^2\right] + n\sigma^2.$$

Because $\hat\mu$ is typically chosen to make RSS small for the observed data $Y$ (i.e., to fit $Y$ well), the RSS is usually an optimistic estimator of the EPE, especially if $\hat\mu$ tends to overfit. To quantify how much $\hat\mu$ overfits, we can define the *effective degrees of freedom* (or simply the *degrees of freedom*) of $\hat\mu$ as $$\text{DF}(\mu,\hat\mu) = \frac{1}{2\sigma^2}\mathbb{E}\left[\text{EPE} - \text{RSS}\right],$$ which uses optimism as a proxy for overfitting.

For the following questions assume we also have a predictor matrix $X\in \mathbb{R}^{n\times d}$, which is simply a matrix of fixed real numbers. Suppose that $d\leq n$ and $X$ has full column rank.

1.  Show that if $\hat\mu$ is differentiable with $\mathbb{E}_\mu\|D\hat\mu(Y)\|_F < \infty$ then $$\sum_{i=1}^n \frac{\partial \hat\mu_i(Y)}{\partial Y_i}$$ is an unbiased estimator of the DF. (Recall $D\hat\mu(Y)$ is the Jacobian matrix from class).

2.  Suppose $\hat\mu = X\hat\beta$, where $\hat\beta$ is the ordinary least squares estimator (i.e., chosen to minimize the RSS). Show that the DF is $d$. (This confirms that DF generalizes the intuitive notion of degrees of freedom as “the number of free variables”).

3.  Suppose $\hat\mu = X\hat\beta$, where $\hat\beta$ minimizes the penalized least squares criterion: $$\hat\beta = \arg\min_\beta \|Y - X\beta\|_2^2 + \rho \|\beta\|_2^2,$$ for some $\rho \geq 0$. Show that the DF is $\sum_{j=1}^d \frac{\lambda_j}{\rho+\lambda_j}$, where $\lambda_1 \geq \cdots \geq \lambda_d > 0$ are the eigenvalues of $X'X$ (counted with multiplicity) (**Hint:** use the singular value decomposition of $X$).

---

[Up: contents](index.md) · [Moral →](02-moral.md)
