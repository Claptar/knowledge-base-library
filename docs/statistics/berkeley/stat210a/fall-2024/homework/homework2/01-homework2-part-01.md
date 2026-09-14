---
title: Homework2 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/homework/homework2.tex
source_file: sources/berkeley-stat210a/fall-2024/homework/homework2.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework2 Part 01 —

**Source:** [`homework/homework2.tex`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/homework/homework2.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

**Problem 1** (Bayesian interpretation of sufficiency). Assume we have a family $\mathcal{P}$ defined by densities $p_{\theta}(x)$ with respect to a common measure $\mu$ on $\mathcal{X}$, for $\theta\in \Theta \subseteq \mathbb{R}^n$. Additionally, assume the parameter $\theta$ is itself random, following *prior density* $q(\theta)$ with respect to the Lebesgue measure on $\Theta$.

Then, we can write the *posterior density* (distribution of $\theta$ given $X=x$) as $$q_{\text{post}}(\theta \mid x) = \frac{p_\theta(x)q(\theta)}{\int_{\Theta} p_\zeta(x)q(\zeta) \,d \zeta}.$$ **Note:** this manipulation of the densities generally works even though we might worry about conditioning on a measure zero set. Feel free to make similar manipulations yourself in the problem.

1.  Suppose a statistic $T(X)$ has the property that, for any prior distribution $q(\theta)$, the posterior distribution $q_{\text{post}}(\theta \mid x)$ depends on $x$ only through $T(x)$. Show that $T(X)$ is sufficient for $\mathcal{P}$.

2.  Conversely, show that, if $T(X)$ is sufficient for $\mathcal{P}$ then, for any prior $q$, the posterior depends on $x$ only through $T(x)$.

---

[Up: contents](index.md) · [Moral: {#moral} →](02-moral-moral.md)
