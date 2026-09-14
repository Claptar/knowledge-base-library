---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework11.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework11.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework11.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework11.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

If $P^n$ is the distribution of $(X_1,\ldots,X_n)$ then it is easy to check that the set of all square-integrable random variables of the form $f(X_1,\ldots,X_n)$ (where $f:\; \mathcal{X}^n \to \mathbb{R}$ is measurable) forms a vector space over $\mathbb{R}$, which we call $L^2(P^n)$, where we can define an inner product as $$\langle f(X), g(X) \rangle_{L^2} = \mathbb{E}[ f(X)g(X)] \leq \sqrt{\mathbb{E}[f(X)^2] \mathbb{E}[g(X)^2]} < \infty.$$

Moreover, the subset of those random variables that can be written as $\sum_i f_i(X_i)$, where each $f_i$ is measurable, forms a subspace. Part (b) establishes that the simpler random variable $\widehat{U}_n$ is the *projection* of $U_n$ onto this subspace, and part (c) establishes that $U_n$ is asymptotically very close to its projection.

**Problem 4** (Super-Efficient Estimator).

Let $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}N(\theta,1)$ and consider estimating $\theta$ via: $$\delta_n(X) = \overline{X}_n 1\{|\overline{X}_n| > a_n\},$$ where $a_n \to 0$ but $a_n\sqrt{n} \to \infty$ as $n \to \infty$ (for example, $a_n = n^{-1/4}$).

1.  Show that $\delta_n$ has the same asymptotic distribution as $\overline X_n$ when $\theta \neq 0$, but that $\sqrt{n}(\delta_n-0)\overset{p}{\to}0$ if $\theta = 0$.

2.  Show that, pointwise in $\theta$, as $n\to\infty$, $$n\,\text{MSE}(\delta_n;\theta) \to 1\{\theta\neq 0\},$$ but that the convergence is not uniform in $\theta$; in fact, $$\sup_{\theta\in\mathbb{R}}\;\; n\,\text{MSE}(\delta_n;\theta) \rightarrow \infty.$$ (**Note**: this is an example of a situation where it is incorrect to exchange a limit with a supremum.)

---

[← Moral](03-moral.md) · [Up: contents](index.md) · [Moral →](05-moral.md)
