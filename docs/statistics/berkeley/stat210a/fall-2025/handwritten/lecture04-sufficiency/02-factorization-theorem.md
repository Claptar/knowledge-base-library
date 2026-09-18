---
title: Factorization Theorem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture04-sufficiency.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture04-sufficiency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-sufficiency.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture04-sufficiency.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Factorization Theorem

Usually, we can recognize sufficient stats by inspecting the density

## Theorem (Factorization Theorem)

Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ be a model with densities $p_\theta(x)$ wrt common measure $\mu$.

$T(X)$ is sufficient iff there exist $g_\theta(t)$, $h(x) \ge 0$ with

$$p_\theta(x) = g_\theta(T(x)) \, h(x) \quad (\text{for } \mu\text{-a.e. } x)$$

**Note** we could absorb $h$ into $\mu$ as density
(define new base measure $\nu$, $\nu(A) = \int_A h(x) \, d\mu(x)$)
$\Rightarrow \mathcal{P}$ has densities $p_\theta(x) = g_\theta(T(x))$ wrt $\nu$

**Interp**: after changing base measure, density depends on $x$ only through $T(x)$

(Can't absorb $g_\theta(T(x))$ into $\mu$: depends on $\theta$)

---

## **Proof (discrete $\mathcal{X}$):** Assume wlog $\mu = #$ on $\mathcal{X}$

($\Leftarrow$)
$$P_\theta(X = x \mid T = t) = \frac{P_\theta(X = x, \, T(x) = t)}{P_\theta(T(x) = t)}$$

$$= \frac{g_\theta(t) \, h(x) \, \mathbf{1}\{T(x) = t\}}{\sum_{T(z) = t} g_\theta(t) \, h(z)}$$

($\Rightarrow$) Assume $T(X)$ sufficient, let
$$g_\theta(t) = P_\theta(T(X) = t)$$
$$h(x) = P(X = x \mid T(X) = T(x)) \quad (\text{no dep. on } \theta)$$

$$\Rightarrow g_\theta(T(x)) \, h(x) = P_\theta(T(X) = T(x) \text{ and } X = x)$$
$$= P_\theta(X = x) = p_\theta(x) \quad \blacksquare$$

**Proof** similar for general densities
- careful about conditioning in cts spaces

---

---

[← Sufficiency](01-sufficiency.md) · [Up: contents](index.md) · [Examples →](03-examples.md)
