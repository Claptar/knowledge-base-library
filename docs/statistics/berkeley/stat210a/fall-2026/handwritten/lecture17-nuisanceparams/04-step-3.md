---
title: Step 3
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture17-nuisanceparams.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-nuisanceparams.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Step 3

For any value $u$, the conditional model is

$$q_\theta(t \mid u) = e^{\theta t - B_u(\theta)} g(t, u), \quad \text{1-param. exp. fam}$$

In one- / two-sided case, we have shown $\psi(t; u)$ is UMP / UMPU in $\mathcal{Q}_u$

Let $\bar{\phi}(t; u) = \mathbb{E}[\phi(X) \mid T(X) = t, U(X) = u]$

$$\mathbb{E}_\theta [\bar{\phi}(T; u) \mid U = u] = \mathbb{E}_\theta [\phi(X) \mid U(X) = u] = \alpha \quad \text{if } \theta = \theta_0$$

$\Rightarrow \bar{\phi}(\cdot; u)$ is a (cond.'l) test of $H_0$ vs. $H_1$ in $\mathcal{Q}_u$ with $\text{power} = \alpha$ at boundary (or $\theta \leq \theta_0$)

**One-sided case:**

$\psi(t; u)$ is the UMP test of $\theta = \theta_0$ vs $\theta > \theta_0$ in $\mathcal{Q}_u$, which is a 1-param. exp. fam.

**Two-sided case:**

$\psi(t; u)$ is the UMP test of $\theta = \theta_0$ vs. $\theta \neq \theta_0$ among tests with $\text{power} = \alpha$, $\frac{d}{d\theta}\text{power} = 0$ @ $\theta_0$.

In either case $\psi$ has higher cond. power than $\bar{\phi}$, a.s.

---

For $(\theta, \lambda) \in \Omega_1$:

$$\begin{aligned}
\mathbb{E}_{\theta, \lambda}[\phi(X)] &= \mathbb{E}_{\theta, \lambda} \left[ \mathbb{E}_\theta \left[ \bar{\phi}(T; U) \mid U \right] \right] \\
&\leq \mathbb{E}_{\theta, \lambda} \left[ \mathbb{E}_\theta \left[ \psi(T; U) \mid U \right] \right] \\
&= \mathbb{E}_{\theta, \lambda} [\phi^*(X)]
\end{aligned}$$

---

---

[← Proof](03-proof.md) · [Up: contents](index.md) · [Permutation Tests →](05-permutation-tests.md)
