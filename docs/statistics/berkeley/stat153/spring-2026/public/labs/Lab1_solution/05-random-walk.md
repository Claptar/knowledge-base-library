---
title: Random walk
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Random walk

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
# Let's plot the random walk for `nt=250` time points
nt = 250
x0 = 0
x = random_walk(nt, x0=x0)
plt.plot(x)

# What do you notice about the data? Try running this cell a few times..
```

```
[<matplotlib.lines.Line2D at 0x12edc9210>]
```

*(1 figure omitted — see the original notebook.)*

```python
# Let's now look at what happens if we simulate 100 random walks for
# 1500 time points and plot them on top of one another.
# What do you see about how the mean and variance
# of the signals change over time? How does this differ from white noise?

nwalks = 100
nt=5000
all_r = np.zeros((nt, nwalks))
for n in np.arange(nwalks):
    all_r[:,n]=random_walk(nt)
    plt.plot(all_r[:,n])
    plt.xlabel('Time')

plt.figure()
plt.plot(all_r.mean(1))
plt.ylabel('Mean')
plt.figure()
plt.plot(all_r.var(1))
plt.ylabel('Variance')
```

```
Text(0, 0.5, 'Variance')
```

*(3 figures omitted — see the original notebook.)*

---

[← Autoregression](04-autoregression.md) · [Up: contents](index.md) · [Random Walk with Drift →](06-random-walk-with-drift.md)
