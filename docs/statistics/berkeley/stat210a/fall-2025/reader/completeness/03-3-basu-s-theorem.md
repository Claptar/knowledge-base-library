---
title: 3 Basu’s Theorem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html
source_file: sources/berkeley-stat210a/fall-2025/reader/completeness.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/completeness.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Basu’s Theorem

Basu’s Theorem gives us a simple way to prove that statistics are independent of one another using the definitions introduced above.

**Theorem (Basu):** If $T(X)$ is complete sufficient and $V(X)$ ancillary for the model $\cP$, then $V(X) \indep T(X)$ for all $\theta \in \Theta$.

Again, for this proof our strategy will be to show that two quantities are almost surely equal to each other, by showing that they have the same expectation for all $\theta$.

*Proof:* Define the following two quantities representing the marginal and conditional probabilities that $V$ falls into a generic set $A$.

$$
\begin{aligned}
p_A &= \PP(V \in A)[5pt]
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

## 3.1 Using Basu’s Theorem {.anchored number="3.1" anchor-id="using-basus-theorem"}

Basu’s Theorem can be helpful in proving independence. To use it, remember that the hypotheses of the theorem (sufficiency, completeness, and ancillarity) are all defined with respect to a *family* $\cP$. The conclusion, however, is defined with respect to individual *distributions*. As a result, when we apply the theorem we can often benefit from being a little clever about how to define $\cP$. The following example should make this clear:

**Example (Independence of sample mean and sample variance for Gaussian):** Assume $X_1,\ldots,X_n \simiid \cN(\mu, \sigma^2)$ for $\mu \in \RR$ and $\sigma^2 > 0$. Define the *sample mean* and *sample variance* as

$$
\begin{aligned}
\overline{X} &= \frac{1}{n}\sum_{i=1}^n X_i[5pt]
S^2 &= \frac{1}{n-1}\sum_{i=1}^n (X_i - \overline{X})^2
\end{aligned}
$$

 We would like to show $\overline{X} \indep S^2$.

Initially the approach of applying Basu’s Theorem appears hopeless because, in the model with $\mu$ and $\sigma^2$ unknown, neither of these two statistics is ancillary *or* sufficient. However, we can nevertheless apply Basu’s Theorem if we are just a bit more clever:

Expand for answer

Consider the model $\cP$ with *known* $\sigma^2 > 0$ and unknown $\mu\in \RR$. This $\cP$ is a one-parameter full-rank exponential family with complete sufficient statistic $\overline{X}$. Moreover, $S^2$ is ancillary, since we can write

$$
S^2 = \sum_{i=1}^n (Z_i - \overline{Z})^2, \quad \text{ for } Z_i = X_i - \mu.
$$

 Because the distribution of $Z_1,\ldots,Z_n \simiid N(0,\sigma^2)$ is known, it follows that the distribution of $S^2$ is known as well (specifically, $S^2/\sigma^2$ is a $\chi^2$ random variable with $n-1$ degrees of freedom). Since $\mu$ is the only unknown parameter, $S^2$ is therefore ancillary in $\cP$. Applying Basu’s theorem, we have $\overline{X} \indep S^2$ for any $\mu \in \RR$. But $\sigma^2$ was arbitrary, so we have the result for all $\mu$ and $\sigma^2$.

---

[← 2 Ancillarity](02-2-ancillarity.md) · [Up: contents](index.md)
