---
title: Basu's Theorem
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Basu's Theorem

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Basu's Theorem gives us a simple way to prove that statistics are independent of one another using the definitions introduced above.

**Theorem (Basu):** If $T(X)$ is complete sufficient and $V(X)$ ancillary for the model $\cP$, then $V(X) \indep T(X)$ for all $\theta \in \Theta$.

Again, for this proof our strategy will be to show that two quantities are almost surely equal to each other, by showing that they have the same expectation for all $\theta$.

*Proof:* Define the following two quantities representing the marginal and conditional probabilities that $V$ falls into a generic set $A$.
$$
\begin{aligned}
p_A &= \PP(V \in A)\\[5pt]
q_A(T(X)) &= \PP(V \in A \mid T(X))
\end{aligned}
$$
Note that $p_A$ does not depend on $\theta$ by ancillarity of $V$, while $q_A$ does not depend on $\theta$ by sufficiency of $T$.

The expectation of their difference is
$$
\EE_\theta\left[q_A(T) - p_A\right] = p_A - p_A = 0, \quad \text{ for all } \theta.
$$
By completeness of $T$, this implies that $q_A(T) \eqas p_A$: the conditional probability equals the marginal probability. Hence, for any $B$, we have
$$
\begin{aligned}
\PP_\theta(V \in A, T \in B) &= \int q_A(t) 1\{t \in B\}\,dP_\theta^T(t)\\
&= \int p_A 1\{t \in B\}\,dP_\theta^T(t)\\
&= \PP_\theta(V \in A) \PP_\theta(T \in B).
\end{aligned}
$$

### Using Basu's Theorem

Basu's Theorem can be helpful in proving independence. To use it, remember that the hypotheses of the theorem (sufficiency, completeness, and ancillarity) are all defined with respect to a *family* $\cP$. The conclusion, however, is defined with respect to individual *distributions*. As a result, when we apply the theorem we can often benefit from being a little clever about how to define $\cP$. The following example should make this clear:

**Example (Independence of sample mean and sample variance for Gaussian):** Assume $X_1,\ldots,X_n \simiid \cN(\mu, \sigma^2)$ for $\mu \in \RR$ and $\sigma^2 > 0$. Define the *sample mean* and *sample variance* as
$$
\begin{aligned}
\overline{X} &= \frac{1}{n}\sum_{i=1}^n X_i\\[5pt]
S^2 &= \frac{1}{n-1}\sum_{i=1}^n (X_i - \overline{X})^2
\end{aligned}
$$
We would like to show $\overline{X} \indep S^2$.

Initially the approach of applying Basu's Theorem appears hopeless because, in the model with $\mu$ and $\sigma^2$ unknown, neither of these two statistics is ancillary *or* sufficient. However, we can nevertheless apply Basu's Theorem if we are just a bit more clever:

!!! important "Important"

---

[← Ancillarity](05-ancillarity.md) · [Up: contents](index.md) · [Expand for answer →](07-expand-for-answer.md)
