---
title: Random Walk with Drift
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Random Walk with Drift

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

A _random walk with drift_ is a specific modification of the _random walk_ model in which we add a constant $\delta>0$ to our _random walk_:

$x_t = \delta + x_{t-1} + w_t$

which can also be written:

$x_t = \delta t + \displaystyle\sum_{j=1}^t w_j$

Let's now write a function for this:

```python
def random_walk_drift(nt, drift, x0=0):
    '''
    Create a random walk with drift for `nt` time points, `drift` drift, and
    with initial value `x0`.
    Inputs:
        nt (int) : number of time points
        drift (float) : constant drift
        x0 (float) : initial value
    '''
    x = np.zeros((nt,))
    x[0] = x0
    for n in np.arange(1,nt):
        x[n] = x[n-1] + white_noise(1) + drift
    return x
```

```python

---

[← of the signals change over time? How does this differ from white noise?](20-of-the-signals-change-over-time-how-does-this-differ-from-wh.md) · [Up: contents](index.md) · [Now let's plot a single example of the random walk. Try running a few times →](22-now-let-s-plot-a-single-example-of-the-random-walk-try-runni.md)
