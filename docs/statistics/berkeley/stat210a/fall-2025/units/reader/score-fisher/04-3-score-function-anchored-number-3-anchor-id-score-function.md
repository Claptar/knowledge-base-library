---
title: 3 Score Function {.anchored number="3" anchor-id="score-function"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Score Function {.anchored number="3" anchor-id="score-function"}

**Source:** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assume a family <span class="math inline">\$\\cP\$</span> has densities <span class="math inline">\$p\_\\theta\$</span> with respect to a measure <span class="math inline">\$\\mu\$</span>, for <span class="math inline">\$\\theta \\in \\Theta \\subseteq \\RR^d\$</span>. Assume additionally that these densities have common support: that <span class="math inline">\$\\{x: p\_\\theta(x) &gt; 0\\}\$</span> is the same for all <span class="math inline">\$\\theta\$</span>.

Recall the log-likelihood is <span class="math inline">\$l(\\theta;X) = \\log p\_\\theta(X)\$</span> (thought of as a random function of <span class="math inline">\$\\theta\$</span>)

**Definition:** The *Score function* is <span class="math inline">\$\\nabla l\_\\theta(X)\$</span>.

It plays a key role in many areas of statistics, especially in asymptotics. We can think of it as a “local complete sufficient statistic.” For <span class="math inline">\$\\eta \\approx 0\$</span>, and <span class="math inline">\$\\theta\_0 \\in \\Theta^\\circ\$</span>, we have

<span class="math display">\\$$p\_{\\theta\_0+\\eta}(x) = e^{\\ell(\\theta\_0 + \\eta; x)} \\approx e^{\\eta'\\nabla \\ell(\\theta\_0;x)}p\_{\\theta\_0}(x).\\$$</span>

---

[← 2 Motivation: Tangent Family {.anchored number="2" anchor-id="motivation-tangent-family"}](03-2-motivation-tangent-family-anchored-number-2-anchor-id-moti.md) · [Up: contents](index.md) · [Score fisher Part 05 — →](05-score-fisher-part-05.md)
