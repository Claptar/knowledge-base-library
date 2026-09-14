---
title: Group Sequential Designs
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Group Sequential Designs

**Source:** [`27-sequential-analysis/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Group Sequential Designs

- Instead of checking after every shell is fired
- Let’s check at time 10, 20, 30, 40, 50
- This is an example of a Group Sequential Design: the analyst picks some set of points <span class="math inline">\$H = \\{t\_0, t\_1, \\ldots, t\_k\\}\$</span> and we ask for some <span class="math inline">\$\\bar C\_n(X)\$</span> so that <span class="math display">\\$$ \\mathsf{P}\\!\\left(\\forall\\, n \\in H : \\mu \\in \\bar C\_n(X)\\right) \\geq 1 - \\alpha \\$$</span>

## Group Sequential Designs are Popular

- [FDA Guidance](https://www.fda.gov/media/78495/download)
- Most popular method for A/B testers (Big tech)
- They can be visualized as a confidence sequence too.

## Group Sequential Designs in Action

Show simulation code

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(gsDesign)

---

[← --- Parameters ---](08-----parameters.md) · [Up: contents](index.md) · [5 equally-spaced interim analyses with O'Brien-Fleming spending →](10-5-equally-spaced-interim-analyses-with-o-brien-fleming-spend.md)
