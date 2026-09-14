---
title: Least Favorable Sequence
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Least Favorable Sequence

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Sometimes there is no least favorable prior, e.g., if parameter space isn't compact.

$X \sim N(\theta, 1)$: LF prior should spread mass everywhere, but that is not a proper prior.

Definition: A sequence $\{\pi_n\}$ is LF if $r(\pi_n) \to \sup_\pi r(\pi)$

### Theorem

Suppose $\{\pi_n\}$ is a prior sequence and $\delta$ satisfies $\sup_\theta R(\theta, \delta) = \lim_n r(\pi_n)$. Then:

a) $\delta$ is minimax
b) $\{\pi_n\}$ is LF

Proof:

a) Other est. $\delta'$. Then $\forall n$:
   $$\sup_\theta R(\theta, \delta') \geq \int R(\theta, \delta') d\pi_n(\theta) \geq r(\pi_n)$$
   $$\geq \lim_n r(\pi_n) = \sup_\theta R(\theta, \delta)$$

b) Prior $\pi$:
   $$r(\pi) = \inf_\delta \int R(\theta, \delta) d\pi(\theta) \leq \int R(\theta, \delta) d\pi(\theta)$$
   $$\leq \sup_\theta R(\theta, \delta) = \lim_n r(\pi_n)$$

### Basic Picture

- $\sup_\theta R(\theta, \delta)$ (generic $\delta$)
- $\inf_\delta \sup_\theta R(\theta, \delta)$ (minimax risk)
- $\sup_\pi r(\pi)$ (if LF prior exists)
- $r(\pi)$ (generic $\pi$)

If minimax est. exists: $\inf_\delta \sup_\theta R(\theta, \delta) = \sup_\theta R(\theta, \delta^*)$

If LF prior exists: $\sup_\pi r(\pi) = r(\pi^*)$

---

[← Least Favorable Priors](02-least-favorable-priors.md) · [Up: contents](index.md) · [Practical Applications →](04-practical-applications.md)
