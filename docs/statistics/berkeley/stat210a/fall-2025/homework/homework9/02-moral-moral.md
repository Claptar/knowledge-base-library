---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework9.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework9.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework9.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework9.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Fisher’s exact test is almost certainly the most important non-Gaussian example of a UMPU test with nuisance parameters, and has been used in countless clinical trials and observational studies. For example, we might give $n_1$ cardiac disease patients a new drug and give $n_0$ a placebo, then observe how many patients in each group suffer a heart attack within the next 5 years. It can be derived directly from the simple tools we are learning in class.

**Problem 2** (One-sample $t$-interval). If $Z\sim N(0,1)$ and $V \sim \chi_d^2$ with $Z,V$ independent, we say that $T=Z/\sqrt{V/d}$ follows a *Student’s $t$ distribution* with $d$ degrees of freedom, denoted by $T\sim t_d$. Note that $T^2 \sim F_{1,d}$ but $T$ preserves sign information in case we want to do one-sided tests.

Now suppose $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}N(\mu,\sigma^2)$ with $\sigma^2>0$ unknown and consider testing $H_0:\; \mu = \mu_0$ vs. $H_1:\; \mu \neq \mu_0$.

We showed in class that the one-sided UMPU test for $H_0:\;\mu \leq 0$ vs. $H_1:\; \mu > 0$ rejects for large values of $T_X = \frac{\overline X \sqrt{n}}{\sqrt{S_X^2}}$, where $S_X^2$ is defined as in Problem 2.

1.  Show that $T_X\sim t_{n-1}$ if $\mu = 0$ (see hint for previous problem).

2.  To test $H_0:\;\mu=0$ vs. $H_1:\; \mu \neq 0$, show that the UMPU test rejects for large values of $|T_X|$ (Hint: the simplest way is to use symmetry).

3.  Find a UMPU test of $H_0:\; \mu = \mu_0$ for a generic $\mu_0\in\mathbb{R}$, and invert to find a confidence interval for $\mu$ in terms of $\overline X$, $S_X^2$, quantiles of the $t_{n-1}$ distribution, and the desired level $\alpha$ (Hint: consider the distribution of $X_i-\mu_0$).

---

[← Homework9 Part 01 —](01-homework9-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
