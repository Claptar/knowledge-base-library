---
title: Initial parameter values
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Initial parameter values

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

y_exc = y[y > thresh]
in2 = np.sqrt(6 * np.var(y_exc)) / np.pi
in1 = np.mean(y_exc) - 0.57722 * in2
init0 = [in1, in2, 0.1]

---

[← Define objective (negative log-likelihood) function](29-define-objective-negative-log-likelihood-function.md) · [Up: contents](index.md) · [Optimization using Nelder-Mead →](31-optimization-using-nelder-mead.md)
