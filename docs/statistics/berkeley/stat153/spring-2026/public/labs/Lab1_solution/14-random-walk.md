---
title: Random walk
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Random walk

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

A _random walk_ is the term for a time series in which the value of the time series at time $t$ is the value of the series at time $t-1$ plus a random movement determined by $w_t$ (white noise). This is a classic example of a _nonstationary_ process (which we'll get into later). Let's first generate a function for this:

```python
def random_walk(nt, x0=0):
    '''
    Generate a random walk `x` for `nt` time points using initial value `x0=0`
    Inputs:
        nt (int) : number of time points
        x0 (float) :
    '''
    x = np.zeros((nt,))
    x[0] = x0
    for n in np.arange(1,nt):
        x[n] = x[n-1] + white_noise(1)[0]
    return x
```

```python

---

[← Data as signal plus white noise](13-data-as-signal-plus-white-noise.md) · [Up: contents](index.md) · [Let's plot the random walk for nt=250 time points →](15-let-s-plot-the-random-walk-for-nt-250-time-points.md)
