---
title: Different starting values
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Different starting values

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

init1 = [np.mean(y[y > thresh]), np.std(y[y > thresh]), -0.1]
fit1a = minimize(pp_negloglik, init1, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2a = minimize(pp_negloglik, init1, args=(y, thresh, npy), method='BFGS', options={'disp': True})

---

[← Need code to get Hessian at optimum; hessinv is NOT that.](32-need-code-to-get-hessian-at-optimum-hessinv-is-not-that.md) · [Up: contents](index.md) · [Bad starting value for BFGS →](34-bad-starting-value-for-bfgs.md)
