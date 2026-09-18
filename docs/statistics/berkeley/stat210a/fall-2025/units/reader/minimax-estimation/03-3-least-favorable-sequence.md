---
title: 3 Least Favorable Sequence
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Least Favorable Sequence

Sometimes there is no least favorable prior, e.g., if parameter space isn’t compact.

$X \sim N(\theta, 1)$: LF prior should spread mass everywhere, but that is not a proper prior.

Definition: A sequence $\{\pi_n\}$ is LF if $r(\pi_n) \to \sup_\pi r(\pi)$

### 3.1 Theorem {.anchored number="3.1" anchor-id="theorem-1"}

Suppose $\{\pi_n\}$ is a prior sequence and $\delta$ satisfies $\sup_\theta R(\theta, \delta) = \lim_n r(\pi_n)$. Then:

1.  $\delta$ is minimax
2.  $\{\pi_n\}$ is LF

Proof:

1.  Other est. $\delta'$. Then $\forall n$:

$$
\sup_\theta R(\theta, \delta') \geq \int R(\theta, \delta') d\pi_n(\theta) \geq r(\pi_n)
$$

$$
\geq \lim_n r(\pi_n) = \sup_\theta R(\theta, \delta)
$$

2.  Prior $\pi$:

$$
r(\pi) = \inf_\delta \int R(\theta, \delta) d\pi(\theta) \leq \int R(\theta, \delta) d\pi(\theta)
$$

$$
\leq \sup_\theta R(\theta, \delta) = \lim_n r(\pi_n)
$$

### 3.2 Basic Picture {.anchored number="3.2" anchor-id="basic-picture"}

- $\sup_\theta R(\theta, \delta)$ (generic $\delta$)
- $\inf_\delta \sup_\theta R(\theta, \delta)$ (minimax risk)
- $\sup_\pi r(\pi)$ (if LF prior exists)
- $r(\pi)$ (generic $\pi$)

If minimax est. exists: $\inf_\delta \sup_\theta R(\theta, \delta) = \sup_\theta R(\theta, \delta^*)$

If LF prior exists: $\sup_\pi r(\pi) = r(\pi^*)$

## 4 Practical Applications {.anchored number="4" anchor-id="practical-applications"}

Minimax estimators are very hard to find, but minimax bounds are often used in statistical theory to characterize hardness, especially lower bounds.

### 4.1 Approach 1: Near-optimal Estimators {.anchored number="4.1" anchor-id="approach-1-near-optimal-estimators"}

1.  Propose practical estimator $\delta$
2.  Find $\pi$ for which $r(\pi)$ close to $\sup_\theta R(\theta, \delta)$ (or same rate, or asymptotically)
3.  Conclude $\delta$ can’t be improved much

### 4.2 Approach 2: Problem Hardness {.anchored number="4.2" anchor-id="approach-2-problem-hardness"}

Quantify hardness of a problem by its minimax rate in some asymptotic regime.

Caveat: A problem might be easy throughout most of parameter space but very hard in some bizarre corner we never encounter in practice.

---

[← 2 Least Favorable Priors](02-2-least-favorable-priors.md) · [Up: contents](index.md)
