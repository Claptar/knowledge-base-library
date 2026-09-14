---
title: 4 Practical Applications {.anchored number="4" anchor-id="practical-applications"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Practical Applications {.anchored number="4" anchor-id="practical-applications"}

**Source:** [`units/reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Minimax estimators are very hard to find, but minimax bounds are often used in statistical theory to characterize hardness, especially lower bounds.

### <span class="header-section-number">4.1</span> Approach 1: Near-optimal Estimators {.anchored number="4.1" anchor-id="approach-1-near-optimal-estimators"}

1.  Propose practical estimator <span class="math inline">\$\\delta\$</span>
2.  Find <span class="math inline">\$\\pi\$</span> for which <span class="math inline">\$r(\\pi)\$</span> close to <span class="math inline">\$\\sup\_\\theta R(\\theta, \\delta)\$</span> (or same rate, or asymptotically)
3.  Conclude <span class="math inline">\$\\delta\$</span> can’t be improved much

### <span class="header-section-number">4.2</span> Approach 2: Problem Hardness {.anchored number="4.2" anchor-id="approach-2-problem-hardness"}

Quantify hardness of a problem by its minimax rate in some asymptotic regime.

Caveat: A problem might be easy throughout most of parameter space but very hard in some bizarre corner we never encounter in practice.

---

[← 3 Least Favorable Sequence {.anchored number="3" anchor-id="least-favorable-sequence"}](04-3-least-favorable-sequence-anchored-number-3-anchor-id-least.md) · [Up: contents](index.md)
