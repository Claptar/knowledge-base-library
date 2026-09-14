---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework8.tex
source_file: sources/berkeley-stat210a/fall-2025/units/homework/homework8.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`units/homework/homework8.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework8.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

We saw before that, while a one-parameter exponential family like the one in part (a) has a complete sufficient statistic that allows for optimal inference throughout the parameter space, a curved exponential family like the mixture family in parts (b-d) has no complete sufficient statistic. Instead, the score acts like a complete sufficient statistic in a local neighborhood of the parameter space, but the score is different in different parts of the parameter space. Hence, the structure of the family has important ramifications for how we should think about statistically efficient inference.

**Problem 3** (Confidence intervals for quantiles).

Assume we observe $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}F$, where the cdf $F$ is assumed to be strictly increasing and continuous. Consider inference on the quantile $q(F) = F^{-1}(p)$, for a fixed $p \in (0,1)$.

1.  Suggest a nonparametric level-$\alpha$ test for $H_0:\; q(F) = q_0$ vs $H_1:\; q(F) \neq q_0$. Since $\alpha$ and $p$ are unspecified, you don’t need to solve for any cutoff values, but describe how you might do so.

2.  For $n = 1000$ and $p = 0.9$, invert your test from part (a) to find an explicit confidence interval for $q(F)$, as a function of $X_1,\ldots,X_n$.

**Problem 4** (Testing with multidirectional alternatives).

Suppose $X\sim N_d(\mu,I_d)$ for unknown $\mu\in\mathbb{R}^d$. Consider testing $H_0:\; \mu=0$ vs. $H_1:\; \mu \neq 0$.

1.  If $d=1$, elaborate on the UMPU proof from class to show that the usual two-sided test $\phi^*(X) = 1\{|X| > z_{\alpha/2}\}$ is the only UMPU test up to almost sure equality.

2.  Show that for any $d>1$ and $\alpha\in(0,1)$, there exists no UMP or UMPU level-$\alpha$ test.

    **Hint:** what would we do if we knew $\mu = (\theta,0,0,\ldots,0)$ for an unknown $\theta\in\mathbb{R}$?

3.  Suppose we have a prior $\Lambda_1$ for the value that $\mu$ takes under the alternative; that is, $\mu \sim \Lambda_1$ if $H_1$ is true and $\mu = 0$ if $H_0$ is true. Define the average power as $$\int_{\mathbb{R}^d} \mathbb{E}_\mu [\phi(X)] \,d\Lambda_1(\mu).$$

    If $\Lambda_1 = N(\nu, \Sigma)$, with positive definite covariance matrix $\Sigma$, find the level-$\alpha$ test that maximizes the average power. Show that the acceptance region is an ellipse centered at $0$ if $\nu = 0$.

4.  **Optional:** (Not graded, no extra points) Suppose the prior $\Lambda_1$ (not necessarily multivariate Gaussian) is rotationally invariant, meaning $\Lambda_1(Q A) = \Lambda_1(A)$ where $A \subseteq \mathbb{R}^d$, $Q$ is any rotation matrix and $QA = \{Qa:\; a\in A\}$. Show that the $\chi^2$ test that rejects for large $\|X\|^2$ maximizes the average power.

**Moral:** Choosing a test in higher dimensions requires us to think harder about how to compromise across different alternative directions, and Bayesian thinking can give us some guidance.

**Problem 5** ($p$-value densities).

Suppose $\mathcal{P}$ is a family with monotone likelihood ratio in $T(X)$, and the distribution of $T(X)$ is continuous with common support for all $\theta$. Let $\phi_{\alpha}$ denote the UMP level-$\alpha$ test of $H_0:\theta\leq \theta_0$ vs. $H_0:\theta > \theta_0$ that rejects when $T(X)$ is large. Let $p(X)$ denote the resulting $p$-value. Show that $p(X)\sim \text{Unif}[0,1]$ if $\theta=\theta_0$, has non-increasing density on $[0,1]$ if $\theta>\theta_0$, and has non-decreasing density on $[0,1]$ if $\theta<\theta_0$.

**Note:** As always there is technically some ambiguity in how we could define the density, but the version we want is the derivative of the cdf. Feel free to work more informally and ignore such technical issues.

---

[← Homework8 Part 01 —](01-homework8-part-01.md) · [Up: contents](index.md)
