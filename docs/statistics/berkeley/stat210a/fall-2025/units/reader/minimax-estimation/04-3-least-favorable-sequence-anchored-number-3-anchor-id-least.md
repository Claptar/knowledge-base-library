---
title: 3 Least Favorable Sequence {.anchored number="3" anchor-id="least-favorable-sequence"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Least Favorable Sequence {.anchored number="3" anchor-id="least-favorable-sequence"}

**Source:** [`units/reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Sometimes there is no least favorable prior, e.g., if parameter space isn’t compact.

<span class="math inline">\$X \\sim N(\\theta, 1)\$</span>: LF prior should spread mass everywhere, but that is not a proper prior.

Definition: A sequence <span class="math inline">\$\\{\\pi\_n\\}\$</span> is LF if <span class="math inline">\$r(\\pi\_n) \\to \\sup\_\\pi r(\\pi)\$</span>

### <span class="header-section-number">3.1</span> Theorem {.anchored number="3.1" anchor-id="theorem-1"}

Suppose <span class="math inline">\$\\{\\pi\_n\\}\$</span> is a prior sequence and <span class="math inline">\$\\delta\$</span> satisfies <span class="math inline">\$\\sup\_\\theta R(\\theta, \\delta) = \\lim\_n r(\\pi\_n)\$</span>. Then:

1.  <span class="math inline">\$\\delta\$</span> is minimax
2.  <span class="math inline">\$\\{\\pi\_n\\}\$</span> is LF

Proof:

1.  Other est. <span class="math inline">\$\\delta'\$</span>. Then <span class="math inline">\$\\forall n\$</span>: <span class="math display">\\$$\\sup\_\\theta R(\\theta, \\delta') \\geq \\int R(\\theta, \\delta') d\\pi\_n(\\theta) \\geq r(\\pi\_n)\\$$</span> <span class="math display">\\$$\\geq \\lim\_n r(\\pi\_n) = \\sup\_\\theta R(\\theta, \\delta)\\$$</span>

2.  Prior <span class="math inline">\$\\pi\$</span>: <span class="math display">\\$$r(\\pi) = \\inf\_\\delta \\int R(\\theta, \\delta) d\\pi(\\theta) \\leq \\int R(\\theta, \\delta) d\\pi(\\theta)\\$$</span> <span class="math display">\\$$\\leq \\sup\_\\theta R(\\theta, \\delta) = \\lim\_n r(\\pi\_n)\\$$</span>

### <span class="header-section-number">3.2</span> Basic Picture {.anchored number="3.2" anchor-id="basic-picture"}

- <span class="math inline">\$\\sup\_\\theta R(\\theta, \\delta)\$</span> (generic <span class="math inline">\$\\delta\$</span>)
- <span class="math inline">\$\\inf\_\\delta \\sup\_\\theta R(\\theta, \\delta)\$</span> (minimax risk)
- <span class="math inline">\$\\sup\_\\pi r(\\pi)\$</span> (if LF prior exists)
- <span class="math inline">\$r(\\pi)\$</span> (generic <span class="math inline">\$\\pi\$</span>)

If minimax est. exists: <span class="math inline">\$\\inf\_\\delta \\sup\_\\theta R(\\theta, \\delta) = \\sup\_\\theta R(\\theta, \\delta^\*)\$</span>

If LF prior exists: <span class="math inline">\$\\sup\_\\pi r(\\pi) = r(\\pi^\*)\$</span>

---

[← 2 Least Favorable Priors {.anchored number="2" anchor-id="least-favorable-priors"}](03-2-least-favorable-priors-anchored-number-2-anchor-id-least-f.md) · [Up: contents](index.md) · [4 Practical Applications {.anchored number="4" anchor-id="practical-applications"} →](05-4-practical-applications-anchored-number-4-anchor-id-practic.md)
