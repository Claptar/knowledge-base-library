---
title: Data on a different scale
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data on a different scale

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

y_exc2 = y[y > thresh] * 1000
y2 = y * 1000
thresh2 = thresh * 1000

init3 = [np.mean(y_exc2), np.std(y_exc2), 0.1]
fit3 = minimize(pp_negloglik, init3, args=(y2, thresh2, npy), method='Nelder-Mead', options={'disp': True})
fit4 = minimize(pp_negloglik, init3, args=(y2, thresh2, npy), method='BFGS', options={'disp': True})

---

[← Bad starting value for BFGS](35-bad-starting-value-for-bfgs.md) · [Up: contents](index.md) · [Plot the objective function →](37-plot-the-objective-function.md)
