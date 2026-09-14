---
title: Different starting values
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Different starting values

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

init1 = [np.mean(y[y > thresh]), np.std(y[y > thresh]), -0.1]
fit1a = minimize(pp_negloglik, init1, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2a = minimize(pp_negloglik, init1, args=(y, thresh, npy), method='BFGS', options={'disp': True})

---

[← Need code to get Hessian at optimum; hessinv is NOT that.](33-need-code-to-get-hessian-at-optimum-hessinv-is-not-that.md) · [Up: contents](index.md) · [Bad starting value for BFGS →](35-bad-starting-value-for-bfgs.md)
