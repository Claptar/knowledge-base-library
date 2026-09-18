---
title: 3 Stationary and Causality for AR(p), $p \geq 2$
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyOne153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Stationary and Causality for AR(p), $p \geq 2$

Similar to $\text{AR}(1)$, it is possible to characterize parameter regimes which ensure existence of stationary (and also causal/non-causal) solutions of $\text{AR}(p)$ for $p \geq 1$. Recall that the $\text{AR}(p)$ model is given by the equation:
$$
y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t. \tag{5}
$$
In terms of the Backshift Notation, we can write the model as:
$$
\phi(B)y_t = \phi_0 + \epsilon_t
$$
where $\phi(B)$ is the result of the following polynomial applied to the Backshift operator:
$$
\phi(z) := 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p. \tag{6}
$$
This polynomial is called the $\text{AR}(p)$ polynomial or the $\text{AR}(p)$ characteristic polynomial. This polynomial will have $p$ roots $z_1, \dots, z_p$. Some of these roots may be complex.

1. Suppose all the roots $z_i$ have modulus distinct from one: $|z_i| \neq 1$ for every $i$. Then there exists a unique stationary solution to (5). Backshift calculus can be used to write the stationary solution $y_t$ explicitly in terms of $\{\epsilon_t\}$. We shall see how to do this in the next lecture.

2. Suppose all the roots $z_i$ have modulus strictly larger than one: $|z_i| > 1$ for every $i$. Then the unique stationary solution is of the form $y_t = \mu + \psi_0 \epsilon_t + \psi_1 \epsilon_{t-1} + \psi_2 \epsilon_{t-2} + \dots = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$, for some $\mu$ and $\{\psi_j, j \geq 0\}$. In other words, only the current and past $\epsilon_t$ values ($\epsilon_t, \epsilon_{t-1}, \dots$) determine $y_t$. Therefore, this stationary solution is causal.

3. Suppose at least one of the roots $z_i$ has modulus strictly smaller than 1 while all other roots have moduli strictly larger than 1. In this case, the unique stationary solution will involve $\epsilon_t$-terms from both in the past and future: $y_t = \mu + \sum_{j=-\infty}^\infty \psi_j \epsilon_{t-j}$ (note that the sum is now going from $-\infty$ to $\infty$). This stationary solution is non-causal.

4. Suppose at least one root $z_i$ has modulus exactly equal to 1. Then there is no stationary solution to (5).

When $p = 1$, the $\text{AR}(1)$ polynomial is $\phi(z) = 1 - \phi_1 z$ with root $1/\phi_1$. So the root having magnitude more than 1 is equivalent to $|\phi_1| < 1$. Then the above assertions are equivalent to the assertions made in the previous two sections for $\text{AR}(1)$.

We will see more details and examples in the next lecture.

## 4 Additional Optional Reading

1. Sections 3.1, 3.2, 3.3 of Shumway-Stoffer 4th edition.

---

[← 2 On the formulae for stationary AR(1)](02-2-on-the-formulae-for-stationary-ar-1.md) · [Up: contents](index.md)
