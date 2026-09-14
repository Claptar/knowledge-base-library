---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework4.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework4.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework4.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework4.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

This is a nice estimator that transitions adaptively between the data splitting estimator (when $X_1$ is subject to extreme selection bias) and the unadjusted sample mean (when $X_1$ is nearly unaffected by selection bias). It manages to do this even though we don’t know how bad the selection bias is, since that depends on $\mu$. It would be difficult to come up with an estimator like this without the theory of exponential families and UMVU estimators, specifically the idea of Rao-Blackwellization. You can read more about problems like this in \citet{hung2020statistical}.

**Problem 3** (Bayesian law of large numbers).

Let $p(x)$ and $q(x)$ denote two strictly positive probability densities with respect to a common dominating measure $\mu$. The *Kullback–Leibler divergence* between $p$ and $q$ is defined as $$D(p \| q) = \int_{\mathcal{X}} p(x) \log \frac{p(x)}{q(x)} \,d\mu(x).$$

1.  Show that $D(p \| q) \geq 0$, with equality only in the case that $p(X) = q(X)$ almost surely

    **Hint:** recall that $\log(1+x) \leq x$ for all $x>-1$.

2.  Consider a dominated likelihood model $\mathcal{P}= \{p_{\theta}(x):\; \theta\in \Theta\}$, where the parameter space $\Theta$ is a finite set, and the densities are strictly positive on $\mathcal{X}$. Let $\lambda$ denote a prior density w.r.t. the counting measure on $\Theta$, and consider the Bayes posterior after observing a sample $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}p_{\theta_0}(x)$ for some *fixed* value $\theta_0$ (that is, we are examining the *frequency* properties of the *Bayesian* posterior distribution). Assume that all the densities are distinct; that is, $p_{\theta_1}(X) = p_{\theta_2}(X)$ almost surely if and only if $\theta_1=\theta_2$.

    If the prior $\lambda$ puts positive mass on all values in $\Theta$, show that as $n\to\infty$, the posterior density eventually concentrates nearly all its mass on the true value $\theta_0$. That is, $$\mathbb{P}_{\theta_0}\left[\lambda(\theta_0 \mid X_1,\ldots,X_n) \geq 1-\varepsilon\right] \to 1, \quad \text{for all } \varepsilon> 0.$$ **Hint:** apply the law of large numbers and see if you can find a way to use part (a).

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
