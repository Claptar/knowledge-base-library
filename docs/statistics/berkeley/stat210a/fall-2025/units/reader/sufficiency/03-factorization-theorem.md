---
title: Factorization theorem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Factorization theorem

As we will see next, we didn’t really need to go to the trouble of calculating the conditional distribution in the first example. Once we noticed that the density depends on $x$ only through $T(x)$, we could have concluded that $T(X)$ was sufficient.

The easiest way to verify that a statistic is sufficient is to show that the density $p_\theta$ factorizes into a part that involves only $\theta$ and $T(x)$, and a part that involves only $h(x)$.

**Factorization Theorem:** Let $\cP$ be a model having densities $p_\theta(x)$ with respect to a common dominating measure $\mu$. Then $T(X)$ is sufficient for $\cP$ if and only if there exist non-negative functions $g_\theta$ and $h$ for which

$$
p_\theta(x) = g_\theta(T(x)) h(x),
$$

for almost every $x$ under $\mu$.

The “almost every $x$” qualification means that

$$
\mu\left(\{x:\; p_\theta(x) \neq g_\theta(T(x))h(x)\}\right) = 0.
$$

It is needed to avoid counterexamples where we mess with the densities on a set of points that the base measure doesn’t assign any mass, which would let us destroy the factorization structure without changing any of the distributions.

**Proof (discrete** $\cX$): The proof is easiest in the discrete case, so that we don’t have to deal with conditioning on measure-zero events and worry about things like Jacobians for change of variables.

We’ll assume without loss of generality that $\mu$ is the counting measure: if $\mu$ were some other measure, it would have to have a density $m$ with respect to the counting measure and we would just have to carry around $m(x)$ in all of our expressions.

First, assume that there exists a factorization $p_\theta(x) = g_\theta(T(x)) h(x)$. Then we have

$$
\begin{aligned}
\PP_\theta(X = x \mid T(X) = t)
&= \frac{\PP_\theta(X = x, T(X) = t)}{\PP_\theta(T(X) = t)}[7pt]
&= \frac{g_\theta(t) h(x) 1\{T(x) = t\}}{g_\theta(t)\displaystyle\sum_{z:\;T(z) = t} h(z)}[7pt]
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
$$

 noting that the conditional probability in the definition of $h(x)$ does not depend on $\theta$ by sufficiency. Then we have

$$
\PP_\theta(X = x) = \PP_\theta(T(X) = T(x)) \;\cdot\;\PP_\theta(X = x \mid T(X) = T(x)) = g_\theta(T(x)) h(x),
$$

 so $g_\theta(T(x))h(x)$ is indeed the pmf $p_\theta(x)$.

## Statement for general $\cX$ {#statement-for-general-math76 .anchored anchor-id="statement-for-general-cx"}

---

[← Visualization of sufficiency for two binomials](02-visualization-of-sufficiency-for-two-binomials.md) · [Up: contents](index.md) · [Examples →](04-examples.md)
