---
title: Optimization using Nelder-Mead
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Optimization using Nelder-Mead

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

start_time = time.time()
fit1 = minimize(nll, inits, args=(data), method='Nelder-Mead', options={'disp': True})
end_time = time.time()
print("Nelder-Mead Optimization:")
print(fit1)
print("Execution Time:", end_time - start_time, "seconds")

---

[← 6. Basic optimization in Python](22-6-basic-optimization-in-python.md) · [Up: contents](index.md) · [Optimization using BFGS →](24-optimization-using-bfgs.md)
