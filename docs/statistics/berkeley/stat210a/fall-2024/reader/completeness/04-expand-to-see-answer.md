---
title: Expand to see answer
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand to see answer

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

**Yes, $T(X)$ is complete.**

As we showed previously, the density of $T(X)$ for $t > 0$ is
$$
p_\theta(t) =  \frac{nt^{n-1}}{\theta^n}\,\cdot \;1\{t \leq \theta\}.
$$

Suppose we could find $f(t)$ such that
$$
0 = \EE_\theta f(T) = \frac{n}{\theta^n}\int_0^\theta f(t) t^{n-1} \,dt, \quad \text{ for all } \theta > 0.
$$
Dividing the last expression by $n/\theta^n$ and then differentiating with respect to $\theta$, we obtain
$$
0 = f(\theta) \theta^{n-1}, \quad \text{ for all } \theta > 0,
$$
hence $f \equiv 0$.

:::


### Full-rank exponential families

In the general case where $T(X)$ can take on infinitely many values, it is hard to show completeness because the space of possible counterexample functions $f$ is infinite-dimensional. But there is an important class of examples where we can quickly verify complete sufficiency, as we see next.

**Definition:** Let $\cP = \{P_\eta:\; \eta \in \Xi\}$ be an $s$-parameter exponential family with densities
$$
p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x),
$$
with respect to some carrier measure $\mu$. Assume further that the sufficient statistic $T(X)$ satisfies no affine constraint: that is, there is no $\alpha \in \RR$ and nonzero $\beta \in \RR^s$ with $\beta'T(x) \eqPas \alpha$.

If $\Xi$ contains an open set we say $\cP$ is *full-rank*; otherwise we say it is *curved*.

::: callout-note

If $T(X)$ does satisfy a linear constraint, that means $\cP$ can be defined equivalently as an $r$-parameter exponential family for some $r < s$. It may be full-rank or curved depending on the parameter space in a lower-dimensional parameterization.

:::

**Theorem (Complete sufficiency in full-rank exponential families):** If $\cP$ is a full-rank $s$-parameter exponential family, then $T(X)$ is complete sufficient.

The proof is somewhat technical and uses the uniqueness of moment-generating functions.

!!! important "Important"

---

[← Expand to see answer](03-expand-to-see-answer.md) · [Up: contents](index.md) · [Expand for proof →](05-expand-for-proof.md)
