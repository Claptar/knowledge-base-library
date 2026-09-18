---
title: Least Favorable Sequence
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Least Favorable Sequence

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

## Practical Applications

Minimax estimators are very hard to find, but minimax bounds are often used in statistical theory to characterize hardness, especially lower bounds.

### Approach 1: Near-optimal Estimators

1. Propose practical estimator $\delta$
2. Find $\pi$ for which $r(\pi)$ close to $\sup_\theta R(\theta, \delta)$ (or same rate, or asymptotically)
3. Conclude $\delta$ can't be improved much

### Approach 2: Problem Hardness

Quantify hardness of a problem by its minimax rate in some asymptotic regime.

Caveat: A problem might be easy throughout most of parameter space but very hard in some bizarre corner we never encounter in practice.

---

[← Least Favorable Priors](01-least-favorable-priors.md) · [Up: contents](index.md)
