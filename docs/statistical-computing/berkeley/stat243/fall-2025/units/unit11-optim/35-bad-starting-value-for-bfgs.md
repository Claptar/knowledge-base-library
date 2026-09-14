---
title: Bad starting value for BFGS
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Bad starting value for BFGS

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

init2 = [thresh, 0.01, .5]
fit1b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='BFGS', options={'disp': True})

---

[← Different starting values](34-different-starting-values.md) · [Up: contents](index.md) · [Data on a different scale →](36-data-on-a-different-scale.md)
