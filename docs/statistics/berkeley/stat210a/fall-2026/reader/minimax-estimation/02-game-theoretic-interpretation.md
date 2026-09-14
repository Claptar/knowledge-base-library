---
title: Game theoretic interpretation
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Game theoretic interpretation

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We can think of the minimax risk as the expected payoff in an adversarial zero-sum game between the analyst, who chooses the estimator to make the risk as small as possible, and "Nature," who waits to see what estimator the analyst chooses and then assigns the parameter to make the risk as large as possible. If the analyst plays first and selects the estimator $\delta$, then Nature will always select the value of $\theta$ that maximizes $R(\theta;\delta)$; then $r^*$ corresponds to the attained risk in this game, and $\delta^*$ to the analyst's optimal move.

What if Nature played first? If the analyst could know $\theta$ while choosing $\delta$, the problem would be too easy, but it becomes more interesting if we allow Nature to choose a *mixed strategy* of sampling $\theta \sim \Lambda$. Then, an analyst who could see the prior (but not the realized value of $\theta$) would play the Bayes estimator $\delta_\Lambda$ and attain the Bayes risk.

Intuitively, the analyst is in a better position when playing second than when playing first, and indeed the Bayes risk for any $\Lambda$ is a lower bound for the minimax risk:
$$
r_\Lambda \;=\; \inf_{\delta} \int_\Theta R(\theta;\delta)\;d\Lambda(\theta) \;\leq\; \inf_{\delta} \sup_\theta R(\theta; \delta) \;=\; r^*,
$$
since any estimator's average-case risk is no larger than its worst-case risk.

To optimize this lower bound on $r^*$, we can try to find Nature's Nash equilibrium strategy.

---

[← Definitions](01-definitions.md) · [Up: contents](index.md) · [Least Favorable Priors →](03-least-favorable-priors.md)
