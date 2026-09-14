---
title: other values of n
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# other values of n

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(w)
plt.plot(moving_average(w))
plt.plot(moving_average(w, n=10)) # FILL IN, try several...
```

```
[<matplotlib.lines.Line2D at 0x12ec48b50>]
```

*(1 figure omitted — see the original notebook.)*

Below let's create the moving average function assuming negative lags (a __causal__ filter) $v_t = \frac{1}{3} (w_{t-2}+w_{t-1}+w_t)$

```python
def moving_average_causal(w, n=3):
    '''
    Create a causal moving average of the time series `w` using an `n`-point moving average (default 3)
    Inputs:
        w (np.array) : original time series
        n (int) : number of points incorporated in the moving average
    Output:
        v (np.array) : smoothed time series
    '''
    v = np.zeros((len(w),)) * np.nan
    for t in np.arange(n, len(w) - n):
        v[t] = np.mean(w[t-n : t])
    return v
```

Now let's look at how this causal filtering compares to the original centered n-point moving average. What do you notice?

```python
n = 3
plt.figure(figsize=(12,3))
#plt.plot(w, label='original')
plt.plot(moving_average(w, n), label='centered n-point MA')
plt.plot(moving_average_causal(w, n), label='causal n-point MA')
plt.legend()
```

```
<matplotlib.legend.Legend at 0x12ec9c820>
```

*(1 figure omitted — see the original notebook.)*

---

[← Lab1 solution Part 10 —](10-lab1-solution-part-10.md) · [Up: contents](index.md) · [Autoregression →](12-autoregression.md)
