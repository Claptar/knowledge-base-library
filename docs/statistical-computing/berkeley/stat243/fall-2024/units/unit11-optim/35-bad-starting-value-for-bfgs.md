---
title: Bad starting value for BFGS
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Bad starting value for BFGS

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

init2 = [thresh, 0.01, .5]
fit1b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='BFGS', options={'disp': True})

---

[← Different starting values](34-different-starting-values.md) · [Up: contents](index.md) · [Data on a different scale →](36-data-on-a-different-scale.md)
