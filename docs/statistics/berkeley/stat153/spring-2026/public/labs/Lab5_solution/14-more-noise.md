---
title: More noise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# More noise

**Source:** [`public/labs/Lab5_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now try re-running the analysis above using a higher noise level (i.e. set `var_eps` to be much larger for the error variance). What do you notice? Fill in your edited code below, and first try doing a grid search over all frequencies from 0 to the Nyquist limit.

When do things break down?

```python
fs = 500 # sampling rate
duration = 2
t = np.arange(0,duration,step=1/fs)
B0 = 2
phi = 0
f = 3.2
R =  2.5
var_eps = 1000 # Variance of white noise

---

[← use t2 as our new time observations, then calculate our new estimate of y](13-use-t2-as-our-new-time-observations-then-calculate-our-new-e.md) · [Up: contents](index.md) · [Our true sinusoid →](15-our-true-sinusoid.md)
