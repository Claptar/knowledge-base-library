---
title: BFGS with specific relative tolerance on 'x', given precision loss message.
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# BFGS with specific relative tolerance on 'x', given precision loss message.

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## See `https://docs.scipy.org/doc/scipy/reference/optimize.minimize-bfgs.html`.

fit2_alt = minimize(nll, inits, args=(data), method='BFGS',
    options={'disp': True, 'xrtol': 1e-6})

---

[← Optimization using BFGS](24-optimization-using-bfgs.md) · [Up: contents](index.md) · [Different starting value (recall non-positive definite Hessian) →](26-different-starting-value-recall-non-positive-definite-hessia.md)
