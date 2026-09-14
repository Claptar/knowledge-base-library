---
title: 2 Ancillarity
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/completeness.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/completeness.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Ancillarity

**Source:** [`units/reader/completeness.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/completeness.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We’ve spent a lot of time discussing sufficient statistics, which are statistics that carry *all* of the information about <span class="math inline">\$\\theta\$</span>. Our next definition describes a type of statistic that carry *no* information about the parameter.

**Definition:** We say <span class="math inline">\$V(X)\$</span> is ancillary for the model <span class="math inline">\$\\cP = \\{P\_\\theta: \\theta \\in \\Theta\\}\$</span> if its distribution does not depend on <span class="math inline">\$\\theta\$</span>.

Just as the sufficiency principle tells us that our inference procedures should depend only on information from sufficient statistics, an analogous principle suggests in effect that procedures should depend as little as possible on ancillary statistics. Specifically, it recommends treating <span class="math inline">\$V(X)\$</span> as a fixed value and evaluating the rest of the data set according to its distribution *conditional on* <span class="math inline">\$V(X)\$</span>:

**Conditionality Principle:** If <span class="math inline">\$V(X)\$</span> is ancillary, then all inference should be conditional on <span class="math inline">\$V(X)\$</span>.

It may not be immediately clear why conditioning on <span class="math inline">\$V(X)\$</span> “removes” it from the problem, but we will return to the idea of conditional inference during our unit on hypothesis testing and interval estimation, where it will play an important role.

---

[← 1 Completeness](02-1-completeness.md) · [Up: contents](index.md) · [3 Basu’s Theorem →](04-3-basu-s-theorem.md)
