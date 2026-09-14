---
title: 8 FDR Control
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 8 FDR Control

**Source:** [`units/reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Elegant but fragile proof due to Storey, Taylor, Siegmund (2002)

Assume <span class="math inline">\$\\#\\{i: H\_{0i} \\text{ true}\\} = m\_0\$</span> indep. <span class="math inline">\$p\_i \\sim U$$0,1$$\$</span> under <span class="math inline">\$H\_{0i}\$</span>

Let <span class="math inline">\$V(t) = \\#\\{i \\in H\_{0c}: p\_i \\leq t\\}\$</span>

<span class="math inline">\$\\text{FDR} = \\mathbb{E}$$\\text{FDP}$$ = \\mathbb{E}\\left$$\\frac{V(T)}{R(T)} \\cdot 1\\{R(T) &gt; 0\\}\\right$$\$</span>

Then FDR <span class="math inline">\$= \\mathbb{E}$$\\text{FDP}$$ = \\mathbb{E}$$\\mathbb{E}\[\\text{FDP} \| T$$\] \\leq \\mathbb{E}$$m\_0T/(mT)$$ = \\alpha m\_0/m \\leq \\alpha\$</span>

Note: <span class="math inline">\$Q(t) = V(t)/(mt)\$</span> is a martingale when <span class="math inline">\$t\$</span> runs backwards from <span class="math inline">\$t=1\$</span> to <span class="math inline">\$t=0\$</span>

<span class="math inline">\$\\mathbb{E}$$V(s) \| V(t)$$ = V(t) \\cdot s/t\$</span>

<span class="math inline">\$\\mathbb{E}$$1\\{p\_i \\leq s\\} \| 1\\{p\_i \\leq t\\}, V(t)$$ = s/t \\cdot 1\\{p\_i \\leq t\\}\$</span>

And <span class="math inline">\$T\$</span> is a stopping time w.r.t. the filtration <span class="math inline">\$\\mathcal{F}\_t\$</span> of <span class="math inline">\$\\{V(t), R(t)\\}\$</span> (again, filtration with <span class="math inline">\$t=1 \\to t=0\$</span>)

Why? For <span class="math inline">\$s&lt;t\$</span>, <span class="math inline">\$R(s) = \\#\\{i: p\_i \\leq s\\}\$</span>

<span class="math inline">\$\\mathbb{E}$$1\\{p\_i \\leq s\\} \| \\mathcal{F}\_t$$ = s/t \\cdot 1\\{p\_i \\leq t\\}\$</span>

<span class="math inline">\$\\hat{F}(s) = R(s)/m\$</span>

$$Insert graph showing <span class="math inline">\$\\hat{F}(t)\$</span> vs <span class="math inline">\$t/\\alpha\$</span> and <span class="math inline">\$Q(t)\$</span>$$

<span class="math inline">\$\\text{FDR} = \\alpha \\mathbb{E}$$V(T)/(mT)$$ = \\alpha \\mathbb{E}$$Q(T)$$ = \\alpha \\mathbb{E}$$Q(1)$$ = \\alpha m\_0/m\$</span>

### <span class="header-section-number">8.1</span> Remarks {.anchored number="8.1" anchor-id="remarks"}

- Proof only works if p-values indep., null ones exactly uniform
- More robust proof shows FDR controlled when null p-values conservative
- Can be extended to positive dependence
- FDR controlled under general dependence if we use corrected level <span class="math inline">\$\\alpha m / (m+1-i)\$</span>
- <span class="math inline">\$\\sum\_{i=1}^m 1/i \\approx \\log m + 0.577\$</span>

---

[← 7 Benjamini-Hochberg Procedure](08-7-benjamini-hochberg-procedure.md) · [Up: contents](index.md)
