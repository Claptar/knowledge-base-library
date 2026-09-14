---
title: 3 Bonferroni Correction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Bonferroni Correction

**Source:** [`units/reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assume <span class="math inline">\$p\_1,\\ldots,p\_m\$</span> are p-values for <span class="math inline">\$H\_{01},\\ldots,H\_{0m}\$</span> with <span class="math inline">\$p\_i \\sim U(0,1)\$</span> under <span class="math inline">\$H\_{0i}\$</span>

For general dependence, can guarantee control by rejecting <span class="math inline">\$H\_{0i}\$</span> iff <span class="math inline">\$p\_i \\leq \\alpha/m\$</span>:

<span class="math inline">\$\\mathbb{P}\_\\theta(\\text{any false rejections}) \\leq \\mathbb{P}\_\\theta(\\text{any } H\_{0i} \\text{ rejected}) \\leq \\sum\_{i \\in H\_{0c}} \\mathbb{P}\_\\theta(H\_{0i} \\text{ rejected}) \\leq m\_0\\alpha/m \\leq \\alpha\$</span>

If p-values independent, can improve to <span class="math inline">\$1-(1-\\alpha)^{1/m}\$</span> (Šidák correction)

Then <span class="math inline">\$\\mathbb{P}\_\\theta(\\text{no false rejections}) = \\prod\_{i \\in H\_{0c}} \\mathbb{P}\_\\theta(p\_i &gt; (1-(1-\\alpha)^{1/m})) \\geq (1-\\alpha)^{m\_0/m} \\geq 1-\\alpha\$</span>

For small <span class="math inline">\$\\alpha\$</span>: <span class="math inline">\$1-(1-\\alpha)^{1/m} \\approx \\alpha/m\$</span>

Šidák doesn’t improve much on Bonferroni

---

[← 2 Family-wise Error Rate (FWER)](03-2-family-wise-error-rate-fwer.md) · [Up: contents](index.md) · [4 Testing with Dependence →](05-4-testing-with-dependence.md)
