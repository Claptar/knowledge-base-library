---
title: Optimization using BFGS
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Optimization using BFGS

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← Optimization using Nelder-Mead](23-optimization-using-nelder-mead.md) · [Up: contents](index.md) · [BFGS with specific relative tolerance on 'x', given precision loss message. →](25-bfgs-with-specific-relative-tolerance-on-x-given-precision-l.md)
