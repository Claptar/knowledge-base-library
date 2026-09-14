---
title: 1 Multiple Testing {.anchored number="1" anchor-id="multiple-testing"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Multiple Testing {.anchored number="1" anchor-id="multiple-testing"}

**Source:** [`units/reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

In many testing problems, we want to test many hypotheses at a time, e.g.:

- Test <span class="math inline">\$H\_0: \\beta\_j = 0\$</span> for <span class="math inline">\$j = 1,\\ldots,d\$</span> in linear regression
- Test whether each of 20K single nucleotide polymorphisms (SNPs) is associated with a given phenotype (e.g., diabetes, schizophrenia)
- Test whether each of 2000 website tweaks affect user engagement

### <span class="header-section-number">1.1</span> Setup {.anchored number="1.1" anchor-id="setup"}

<span class="math inline">\$X \\sim P\_\\theta \\in \\cP\$</span>, <span class="math inline">\$H\_{0i}: \\theta \\in \\Theta\_i\$</span>, <span class="math inline">\$i = 1,\\ldots,m\$</span>

Commonly, <span class="math inline">\$H\_{0i}: \\theta\_i = 0\$</span>

Goal: Return accept/reject decision for each <span class="math inline">\$i\$</span>

Let <span class="math inline">\$R = \\{i: H\_{0i} \\text{ rejected}\\}\$</span>, <span class="math inline">\$\|R\| \\leq m\$</span>

<span class="math inline">\$H\_{0c} = \\{i: H\_{0i} \\text{ true}\\}\$</span>, <span class="math inline">\$\|H\_{0c}\| = m\_0 \\leq m\$</span>

<span class="math inline">\$R \\cap H\_{0c}\$</span> = false rejections

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Multiple testing Part 03 — →](03-multiple-testing-part-03.md)
