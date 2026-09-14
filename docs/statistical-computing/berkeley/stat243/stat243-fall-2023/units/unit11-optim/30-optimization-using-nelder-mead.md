---
title: Optimization using Nelder-Mead
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Optimization using Nelder-Mead

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

start_time = time.time()
fit1 = minimize(pp_negloglik, init0, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
end_time = time.time()
print("Nelder-Mead Optimization:")
print(fit1)
print("Execution Time:", end_time - start_time, "seconds")

---

[← Initial parameter values](29-initial-parameter-values.md) · [Up: contents](index.md) · [Optimization using BFGS →](31-optimization-using-bfgs.md)
