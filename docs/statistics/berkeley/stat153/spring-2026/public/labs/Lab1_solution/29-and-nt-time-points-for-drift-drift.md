---
title: and nt time points for drift drift.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# and nt time points for drift drift.

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

nwalks = 1000
nt = 1500
drift = 0.1
all_r_drift = np.zeros((nt, nwalks))
for n in np.arange(nwalks):
    all_r_drift[:,n]=random_walk_drift(nt, drift)
    plt.plot(all_r_drift[:,n])
    plt.xlabel('Time')
```

```
/var/folders/3f/h3pnh73d18ldksmkrp_fvtk00000gn/T/ipykernel_79118/2370165387.py:13: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  x[n] = x[n-1] + white_noise(1) + drift
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← a matrix of random walks with drift - nwalks samples](28-a-matrix-of-random-walks-with-drift---nwalks-samples.md) · [Up: contents](index.md) · [Now plot the mean and variance over time. How do these change compare →](30-now-plot-the-mean-and-variance-over-time-how-do-these-change.md)
