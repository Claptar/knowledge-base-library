---
title: perform a weighted regression use lm with weights=w
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/robustRegression.nb.html
source_file: sources/statomics-sga2020-ghpages/pages/robustRegression.nb.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# perform a weighted regression use lm with weights=w

**Source:** [`pages/robustRegression.nb.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/robustRegression.nb.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

``` r
lmMod=lm(y~x,weights=w)
```

---

[← Implement it yourself](05-implement-it-yourself.md) · [Up: contents](index.md) · [plot results →](07-plot-results.md)
