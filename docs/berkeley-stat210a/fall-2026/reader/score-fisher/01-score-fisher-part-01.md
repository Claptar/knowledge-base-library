---
title: Score fisher Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Score fisher Part 01 —

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In this section we introduce the score function and Fisher information, two concepts that are central in asymptotic statistics. We

Assume a family $\cP$ has densities $p_\theta$ with respect to a measure $\mu$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that these densities have common support: that $\{x: p_\theta(x) > 0\}$ is the same for all $\theta$ (since we can truncate the sample space to this common support, we could just as well assume $p_\theta(x) > 0$ for all $x$ and $\theta$).

**Definition:** The *Score function* is defined as $S_{\theta}(X) = \nabla \ell(\theta;X)$, a random vector of dimension $d$.

We can think of the score function $S_{\theta_0}(X)$ at a given value $\theta_0$ as a kind of "local" sufficient statistic that we could use to distinguish between $\theta$ values in a small neighorhood of $\theta_0$.

To see why, recall that the log-likelihood $\ell(\theta;X) = \log p_\theta(X)$, thought of as a random function with argument $\theta$, is a minimal sufficient statistic for $X$, up to a vertical shift.

!!! important "Important"

---

[Up: contents](index.md) · [Wait! Didn't we say a statistic can't be a function of $\theta$? →](02-wait-didn-t-we-say-a-statistic-can-t-be-a-function-of.md)
