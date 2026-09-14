---
title: Factorization theorem
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/sufficiency.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Factorization theorem

**Source:** [`reader/sufficiency.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We didn't really need to go to the trouble of calculating the conditional distribution in the previous examples. The easiest way to verify that a statistic is sufficient is to show that the density $p_\theta$ factorizes into a part that involves only $\theta$ and $T(x)$, and a part that involves only $x$.

**Factorization Theorem:** Let $\cP$ be a model having densities $p_\theta(x)$ with respect to a common dominating measure $\mu$. Then $T(X)$ is sufficient for $\cP$ if and only if there exist non-negative functions $g_\theta$ and $h$ for which

$$
p_\theta(x) = g_\theta(T(x)) h(x),
$$

for almost every $x$ under $\mu$.

The "almost every $x$" qualification means that

$$
\mu\left(\{x:\; p_\theta(x) \neq g_\theta(T(x))h(x)\}\right) = 0.
$$

It is needed to avoid counterexamples where we mess with the densities on a set of points that the base measure doesn't assign any mass, which would let us destroy the factorization structure without changing any of the distributions.

**Proof (discrete** $\cX$): The proof is easiest in the discrete case, so that we don't have to deal with conditioning on measure-zero events and worry about things like Jacobians for change of variables.

We'll assume without loss of generality that $\mu$ is the counting measure: if $\mu$ were some other measure, it would have to have a density $m$ with respect to the counting measure and we would just have to carry around $m(x)$ in all of our expressions.

First, assume that there exists a factorization $p_\theta(x) = g_\theta(T(x)) h(x)$. Then we have

$$
\begin{aligned}
\PP_\theta(X = x \mid T(X) = t)
&= \frac{\PP_\theta(X = x, T(X) = t)}{\PP_\theta(T(X) = t)}\\[7pt]
&= \frac{g_\theta(t) h(x) 1\{T(x) = t\}}{g_\theta(t)\displaystyle\sum_{z:\;T(z) = t} h(z)}\\[7pt]
&= \frac{h(x) 1\{T(x) = t\}}{\displaystyle\sum_{z:\;T(z) = t} h(z)},
\end{aligned}
$$

which we see does not depend on $\theta$.

Next consider the opposite direction. If $T(X)$ is sufficient, then we can construct a factorization by writing

$$
\begin{aligned}
g_\theta(t) &= \PP_\theta(T(X)=t)\\
h(x) &= \PP(X = x \mid T(X) = T(x)),
\end{aligned}
$$ noting that the conditional probability in the definition of $h(x)$ does not depend on $\theta$ by sufficiency. Then we have

$$
\PP_\theta(X = x) = \PP_\theta(T(X) = T(x)) \;\cdot\;\PP_\theta(X = x \mid T(X) = T(x)) = g_\theta(T(x)) h(x),
$$ so $g_\theta(T(x))h(x)$ is indeed the pmf $p_\theta(x)$.

---

[← Visualization of sufficiency](02-visualization-of-sufficiency.md) · [Up: contents](index.md) · [Statement for general $\mathcal{X}$ →](04-statement-for-general.md)
