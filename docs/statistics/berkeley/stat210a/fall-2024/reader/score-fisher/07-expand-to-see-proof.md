---
title: Expand to see proof
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand to see proof

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

For any $a \in \RR^d$, we can write
$$\begin{aligned}
\Var_\theta(\delta(X)) \cdot a'J(\theta)a &= \Var_\theta(\delta)\Var_\theta(a'\nabla\ell(\theta;X))\\
&\geq \Cov_\theta(\delta(X), a'\nabla\ell(\theta;X))^2\\
&= \left(a'\nabla \Cov_\theta(\delta, \nabla\ell(\theta))\right)^2\\
&= (a'\nabla g(\theta))^2.
\end{aligned}$$

Thus we obtain for all nonzero $a \in \RR^d$,

$$\Var_\theta(\delta(X)) \geq \frac{(a'\nabla g(\theta))^2}{a'J(\theta)a}.$$

We obtain the result by optimizing the bound, with $a = J(\theta)^{-1}\nabla g(\theta)$ (show this as an exercise).

:::

<!-- For multivariate $\theta \in \RR^d$, $g(\theta) \in \RR^k$: -->

<!-- $$\Var_\theta(\delta) \succeq g'(\theta)I(\theta)^{-1}g'(\theta)'$$ -->

<!-- Meaning: $a'\Var_\theta(\delta)a \geq a'g'(\theta)I(\theta)^{-1}g'(\theta)'a$ for all $a \in \RR^k$. -->

---

[← Cramér-Rao Lower Bound](06-cramér-rao-lower-bound.md) · [Up: contents](index.md) · [Examples →](08-examples.md)
