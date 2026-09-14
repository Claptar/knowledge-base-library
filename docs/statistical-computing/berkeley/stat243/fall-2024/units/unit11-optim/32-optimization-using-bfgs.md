---
title: Optimization using BFGS
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Optimization using BFGS

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

start_time = time.time()
fit2 = minimize(pp_negloglik, init0, args=(y, thresh, npy), method='BFGS', options={'disp': True})
end_time = time.time()
print("\nBFGS Optimization:")
print(fit2)
print("Execution Time:", end_time - start_time, "seconds")

mle = fit2.x

---

[← Optimization using Nelder-Mead](31-optimization-using-nelder-mead.md) · [Up: contents](index.md) · [Need code to get Hessian at optimum; hessinv is NOT that. →](33-need-code-to-get-hessian-at-optimum-hessinv-is-not-that.md)
