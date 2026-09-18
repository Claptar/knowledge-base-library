---
title: 2 Ancillarity
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html
source_file: sources/berkeley-stat210a/fall-2025/reader/completeness.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/completeness.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Ancillarity

We’ve spent a lot of time discussing sufficient statistics, which are statistics that carry *all* of the information about $\theta$. Our next definition describes a type of statistic that carries *no* information about the parameter.

**Definition:** We say $V(X)$ is ancillary for the model $\cP = \{P_\theta: \theta \in \Theta\}$ if its distribution does not depend on $\theta$.

Just as the sufficiency principle tells us that our inference procedures should depend only on information from sufficient statistics, an analogous principle suggests in effect that procedures should depend as little as possible on ancillary statistics. Specifically, it recommends treating $V(X)$ as a fixed value and evaluating the rest of the data set according to its distribution *conditional on* $V(X)$:

**Conditionality Principle:** If $V(X)$ is ancillary, then all inference should be conditional on $V(X)$.

It may not be immediately clear why conditioning on $V(X)$ “removes” it from the problem, but we will return to the idea of conditional inference during our unit on hypothesis testing and interval estimation, where it will play an important role.

---

[← 1 Completeness](01-1-completeness.md) · [Up: contents](index.md) · [3 Basu’s Theorem →](03-3-basu-s-theorem.md)
