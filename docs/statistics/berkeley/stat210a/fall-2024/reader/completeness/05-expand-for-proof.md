---
title: Expand for proof
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand for proof

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

$T(X)$ is sufficient by the factorization theorem, so it remains only to prove completeness.

Assume without loss of generality that $0$ is in the interior of $\Xi$; otherwise we can reparameterize. Assume also that $\cP$ is in canonical form, i.e. $T(X) = X$ and $p_\eta(x) = e^{\eta'x - A(\eta)}$; in general we can always reduce to this case by making a sufficiency reduction and taking $P_0^T$ as the carrier measure.

Any measurable function $f$ can be decomposed as $f(x) = f^+(x) - f^-(x)$ where $f^+$ and $f^-$ are non-negative measurable functions. If $\EE_\eta f(X) = \int (f^+-f^-)p_\eta \,d\mu = 0$ for all $\eta\in\Xi$, then we have
$$
\int e^{\eta'x} f^+(x) \,d\mu(x) = \int e^{\eta'x} f^-(x) \,d\mu(x), \quad \text{ for all } \eta \in \Xi.
$${#eq-mgf-equality}
By assumption, $\Xi$ contains an open neighborhood that includes $0$ on which both integrals are finite. Let $c = \int f^+(x)\,d\mu(x) \geq 0$.

If $c>0$ then we can define the random variables $Y^+$ and $Y^-$ with probability densities $f^+(x)/c$ and $f^-(x)/c$ respectively; then @eq-mgf-equality implies that $Y^+$ and $Y^-$ have equal MGFs in a neighborhood of $0$; hence they have the same distribution and their densities must be a.s. equal to each other. But $f^+(x)=f^-(x)$ only when both are zero, so we have $f^+, f^- \eqmuas 0$.
:::

The next figure shows three cases for exponential families with the same sufficient statistic. The set $\Xi_1$ indicates the full natural parameter space for a generic 2-parameter exponential family, and (A), (B), and (C) denote parameter spaces for three different subfamilies. The subfamily described by the shaded circle (A) is a full-rank exponential family, because it contains an open set. The subfamily described by the curve (B) is a typical example of a curved family, because it does not contain an open set. The subfamily described by the line segment (C) is technically curved according to the definition above, but we could view it as a full-rank $1$-parameter exponential family after reparameterizing it.

![This figure shows three cases: ](https://raw.githubusercontent.com/berkeley-stat210a/fall-2024/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.png)

### Complete sufficient statistics are minimal

A second convenient property of completeness is that complete sufficient statistics are always minimal sufficient.

**Theorem:** If $T(X)$ is complete sufficient for the family $\mathcal{P}$, then $T(X)$ is minimal sufficient for $\cP$.

The way that we usually use completeness in proofs is to show that two quantities are almost surely equal by showing that they have the same expectation. The next proof is an example.

*Proof:* Let $S(X)$ represent any minimal sufficient statistic, and define the conditional expectation of $T$ given $S$:
$$
\overline{T}(S(X)) = \EE[T(X) \mid S(X)].
$$
Note that this conditional expectation does not depend on the parameter $\theta$, because $S(X)$ is sufficient, so $\overline{T}$ is a valid statistic. If we can show that $\overline{T} \eqas T(X)$, that means we can calculate $T(X)$ from $S(X)$, so $T(X)$ is also minimal sufficient.

Because $S(X)$ is minimal sufficient, we can write it as $f(T(X))$ for some function $f$, and use $f$ to define a function $g$ giving the difference between $T$ and $\overline{T}$:
$$
g(t) = t - \overline{T}(f(t)).
$$
The expectation of $g(T)$ is always zero, because
$$
\begin{aligned}
\EE_\theta\; g(T(X)) &= \EE_\theta\; T(X) - \EE_\theta\; \overline{T}(S(X)) \\[5pt]
&= \EE_\theta\; T(X) - \EE_\theta\left[\EE[T(X) \mid S(X)]\right]\\
&= 0.
\end{aligned}
$$
As a result, $g(T) \eqas 0$ and hence $T \eqas \overline{T}$, as desired.

---

[← Expand to see answer](04-expand-to-see-answer.md) · [Up: contents](index.md) · [Ancillarity →](06-ancillarity.md)
