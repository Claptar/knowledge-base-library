---
title: Proof
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture17-nuisanceparams.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-nuisanceparams.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Proof

Assume $\phi$ any unbiased test

**Step 1:** $\mathbb{E}_{\theta, \lambda} |\phi(X)| \leq 1 < \infty \qquad \forall (\theta, \lambda) \in \Omega$

(Keener Thm 2.4) $\Rightarrow \mathbb{E}_{\theta, \lambda} \phi(X)$ infinitely diff. on $\Omega$, can diff. under $\int$

$\phi$ unbiased $\Rightarrow \mathbb{E}_{\theta_0, \lambda} [\phi(X)] = \alpha \qquad \forall (\theta_0, \lambda) \in \Omega$

**Step 2: Boundary submodel:** $\mathcal{P}_{\theta_0} = \{ P_{\theta_0, \lambda} : (\theta_0, \lambda) \in \Omega \}$

$$p_{\theta_0, \lambda}(x) = e^{\lambda' U(x) - A(\theta_0, \lambda)} \cdot \frac{e^{\theta_0 T(x)}}{h(x)}$$

$\mathcal{P}_{\theta_0}$ is full-rank, $s$-param exp. fam, $U(X)$ comp. suff.

Let $f(u) = \mathbb{E}_{\theta_0} [\phi(X) \mid U(X) = u] - \alpha$

$$\mathbb{E}_{\theta_0, \lambda} [f(U(X))] = \mathbb{E}_{\theta_0, \lambda} [\phi(X)] - \alpha = 0 \quad \forall \lambda$$

$$\Rightarrow f(u) \overset{\text{a.s.}}{=} 0$$

$$\Rightarrow \mathbb{E}_{\theta_0} [\phi(X) \mid U(X) = u] = \alpha \quad \forall u$$

**Two-sided case:**

$$\begin{aligned}
g(u) &= \frac{d}{d\theta} \mathbb{E}_{\theta_0} [\phi \mid U = u] \\
&= \mathbb{E}_{\theta_0} \left[ (T - \mathbb{E}_{\theta_0}[T \mid u]) \phi \mid U \right] \\
&= \mathbb{E}_{\theta_0} [T(\phi - \alpha) \mid U]
\end{aligned}$$

$$\mathbb{E}_{\theta_0, \lambda} g(U) = \mathbb{E}_{\theta_0, \lambda} [T(\phi - \alpha)] = \frac{\partial}{\partial \theta} \beta_\phi(\theta_0) = 0 \ \forall \lambda$$

$$\Rightarrow \frac{d}{d\theta} \mathbb{E}_{\theta_0} [\phi \mid U] \overset{\text{a.s.}}{=} 0 \qquad (\text{cond'l power has derivative } 0 \text{ at } \theta_0)$$

---

---

[← Multiparameter Exp. Families](02-multiparameter-exp-families.md) · [Up: contents](index.md) · [Step 3 →](04-step-3.md)
