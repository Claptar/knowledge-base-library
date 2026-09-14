---
title: '2 Motivation: Tangent Family {.anchored number="2" anchor-id="motivation-tangent-family"}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Motivation: Tangent Family {.anchored number="2" anchor-id="motivation-tangent-family"}

**Source:** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Consider a family of densities:

<span class="math display">\\$$p(x; \\theta) = e^{\\theta'T(x) - A(\\theta)}h(x)\\$$</span>

where <span class="math inline">\$\\theta \\in \\RR^d\$</span> and <span class="math inline">\$A(\\theta) = \\log \\int e^{\\theta'T(x)}h(x)dx\$</span>.

For this family:

- <span class="math inline">\$T(X)\$</span> is complete sufficient
- <span class="math inline">\$T(X)\$</span> is minimal
- <span class="math inline">\$\\PP\_\\theta(T(X) = t) = e^{\\theta't - A(\\theta)}\$</span>
- <span class="math inline">\$\\EE\_\\theta$$T(X)$$ = A'(\\theta)\$</span>

Let <span class="math inline">\$\\theta\_0 \\in \\RR^d\$</span> be fixed. Define the **tangent family**

<span class="math display">\\$$q(x; t) = e^{t'\\nabla l\_{\\theta\_0}(x) - k(t)}p\_{\\theta\_0}(x)\\$$</span>

where <span class="math inline">\$k(t) = \\log \\int e^{t'\\nabla l\_{\\theta\_0}(x)}p\_{\\theta\_0}(x)dx\$</span>.

Then <span class="math inline">\$\\nabla l\_{\\theta\_0}(X)\$</span> is complete sufficient for the tangent family at <span class="math inline">\$\\theta\_0\$</span>.

This is called the Score function.

---

[← 1 Outline {.anchored number="1" anchor-id="outline"}](02-1-outline-anchored-number-1-anchor-id-outline.md) · [Up: contents](index.md) · [3 Score Function {.anchored number="3" anchor-id="score-function"} →](04-3-score-function-anchored-number-3-anchor-id-score-function.md)
