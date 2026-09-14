---
title: Initial parameter values
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Initial parameter values

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

y_exc = y[y > thresh]
in2 = np.sqrt(6 * np.var(y_exc)) / np.pi
in1 = np.mean(y_exc) - 0.57722 * in2
init0 = [in1, in2, 0.1]

---

[← Define objective (negative log-likelihood) function](28-define-objective-negative-log-likelihood-function.md) · [Up: contents](index.md) · [Optimization using Nelder-Mead →](30-optimization-using-nelder-mead.md)
