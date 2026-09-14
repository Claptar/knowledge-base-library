---
title: Optimization using BFGS
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Optimization using BFGS

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

start_time = time.time()
fit2 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})
end_time = time.time()
print("\nBFGS Optimization:")
print(fit2)
print("Execution Time:", end_time - start_time, "seconds")

## IMPORTANT: `hess_inv` is just the final estimate from BFGS not
## a direct numerical estimate of the Hessian at the optimum.
## If you need the Hessian, calculate it directly, e.g, using `numdifftools`.

---

[← Optimization using Nelder-Mead](23-optimization-using-nelder-mead.md) · [Up: contents](index.md) · [Different starting value (recall non-positive definite Hessian) →](25-different-starting-value-recall-non-positive-definite-hessia.md)
