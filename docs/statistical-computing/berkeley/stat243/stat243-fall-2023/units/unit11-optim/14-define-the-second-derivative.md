---
title: Define the second derivative
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Define the second derivative

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

def fpp(x):
    return -np.cos(x)

xstar = np.pi  # known minimum

## Newton-Raphson (N-R) method
x0 = 2
n_it = 10
xvals = np.zeros(n_it)
xvals[0] = x0
for t in range(1, n_it):
    xvals[t] = xvals[t - 1] - fp(xvals[t - 1]) / fpp(xvals[t - 1])

print(xvals)
```

Next, here is bisection:

```python
## Bisection method
def bisec_step(interval, fp):
    interval = interval.copy()
    xt = np.mean(interval)
    if fp(interval[0]) * fp(xt) <= 0:
        interval[1] = xt
    else:
        interval[0] = xt
    return interval

n_it = 30
a0 = 2
b0 = (3 * np.pi / 2) - (xstar - a0)
interval = np.zeros((n_it, 2))
interval[0,:] = [a0, b0]

for t in range(1, n_it):
    interval[t,:] = bisec_step(interval[t-1,:], fp)

print(np.mean(interval, axis=1))
```

---

[← Define the gradient](13-define-the-gradient.md) · [Up: contents](index.md) · [5. Multivariate optimization →](15-5-multivariate-optimization.md)
