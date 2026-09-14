---
title: BFGS with specific relative tolerance on 'x', given precision loss message.
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# BFGS with specific relative tolerance on 'x', given precision loss message.

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## See `https://docs.scipy.org/doc/scipy/reference/optimize.minimize-bfgs.html`.

fit2_alt = minimize(nll, inits, args=(data), method='BFGS',
    options={'disp': True, 'xrtol': 1e-6})

---

[← Optimization using BFGS](24-optimization-using-bfgs.md) · [Up: contents](index.md) · [Different starting value (recall non-positive definite Hessian) →](26-different-starting-value-recall-non-positive-definite-hessia.md)
