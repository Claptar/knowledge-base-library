---
title: Random Walk with Drift
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Random Walk with Drift

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
# Now let's plot a single example of the random walk. Try running a few times
# with different parameters. How does the `drift` parameter influence what
# you get? What about the properties of the white noise itself (if you go
# back...?)
nt = 250
drift = 0.1
plt.figure()
plt.plot(random_walk_drift(nt, drift))
```

```
/var/folders/3f/h3pnh73d18ldksmkrp_fvtk00000gn/T/ipykernel_79118/2370165387.py:13: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  x[n] = x[n-1] + white_noise(1) + drift
[<matplotlib.lines.Line2D at 0x12e99c370>]
```

*(1 figure omitted — see the original notebook.)*

```python
# Let's compare the mean and variance of the random
# walk with drift to our example above. Let's create
# a matrix of random walks with drift - `nwalks` samples
# and `nt` time points for drift `drift`.
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
# Now plot the mean and variance over time. How do these change compare
# to the other graphs you created?

plt.figure()
plt.plot(all_r_drift.mean(1))

plt.figure()
plt.plot(all_r_drift.var(1))
```

```
[<matplotlib.lines.Line2D at 0x148bbdc30>]
```

*(2 figures omitted — see the original notebook.)*

---

[← Random walk](05-random-walk.md) · [Up: contents](index.md) · Load some data from Shumway and Stoffer examples →
