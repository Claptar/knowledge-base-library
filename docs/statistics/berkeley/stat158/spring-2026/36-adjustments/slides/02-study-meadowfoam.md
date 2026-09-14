---
title: 'Study: Meadowfoam'
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/36-adjustments/slides.html
source_file: sources/berkeley-stat158/spring-2026/36-adjustments/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Study: Meadowfoam

**Source:** [`36-adjustments/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/36-adjustments/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Study: Meadowfoam

Meadowfoam is a flowering California native plant.

Can we effect the *number of flowers* produced by plants by providing extra light treatment, which varies in its *intensity* as well as it’s *timing*?

##

How would you describe the effect of intensity and timing? Would you fit an ANOVA or a regression model? Why?

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

##

A model for a categorical and continuous effect (ANCOVA):

<span class="math display">\\$$ y\_{ij} = \\mu + \\alpha\_i + \\beta\_1 x\_{ij} + \\epsilon\_{ij} \\$$</span>

Each group has a linear model with the same effect on <span class="math inline">\$x\$</span> and different effect on the categorical effect (two intercepts).

<span class="math display">\\$$\\begin{align} y\_{i1} &= \\mu + \\alpha\_1 + \\beta\_1 x\_{i1} + \\epsilon\_{i1} = \\mu\_1 + \\beta\_1 x\_{i1} + \\epsilon\_{i1} \\\\ y\_{i2} &= \\mu + \\alpha\_2 + \\beta\_1 x\_{i2} + \\epsilon\_{i2} = \\mu\_2 + \\beta\_1 x\_{i2} + \\epsilon\_{i2} \\end{align}\\$$</span>

---

[← Regression Adjustments](01-regression-adjustments.md) · [Up: contents](index.md) · [Regression Adjustments →](03-regression-adjustments.md)
