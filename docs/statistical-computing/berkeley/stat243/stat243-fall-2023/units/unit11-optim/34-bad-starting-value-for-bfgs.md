---
title: Bad starting value for BFGS
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Bad starting value for BFGS

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

init2 = [thresh, 0.01, .5]
fit1b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='BFGS', options={'disp': True})

---

[← Different starting values](33-different-starting-values.md) · [Up: contents](index.md) · [Data on a different scale →](35-data-on-a-different-scale.md)
