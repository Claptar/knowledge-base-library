---
title: Ancillarity
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Ancillarity

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We've spent a lot of time discussing sufficient statistics, which are statistics that carry *all* of the information about $\theta$. Our next definition describes a type of statistic that carry *no* information about the parameter.

**Definition:** We say $V(X)$ is ancillary for the model $\cP = \{P_\theta: \theta \in \Theta\}$ if its distribution does not depend on $\theta$.

Just as the sufficiency principle tells us that our inference procedures should depend only on information from sufficient statistics, an analogous principle suggests in effect that procedures should depend as little as possible on ancillary statistics. Specifically, it recommends treating $V(X)$ as a fixed value and evaluating the rest of the data set according to its distribution *conditional on* $V(X)$:

**Conditionality Principle:** If $V(X)$ is ancillary, then all inference should be conditional on $V(X)$.

It may not be immediately clear why conditioning on $V(X)$ "removes" it from the problem, but we will return to the idea of conditional inference during our unit on hypothesis testing and interval estimation, where it will play an important role.

---

[← Expand for proof](05-expand-for-proof.md) · [Up: contents](index.md) · [Basu's Theorem →](07-basu-s-theorem.md)
