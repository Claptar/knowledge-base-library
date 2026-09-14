---
title: Autoregression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Autoregression

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The smoothed moving average data we generated here still doesn't have a lot of the quasiperiodic characteristics of time series like the speech series and fMRI series examples from lecture (Fig. 1.3 and 1.7 in SS). Instead, we can generate time series with oscillatory behavior in a few ways, one of which is to use the concept of autoregression, where we predict the current value $x_t$ of a time series as a function of past values, e.g.

$x_t = 1.5x_{t-1} + 0.75x_{t-2} + w_t $

We will start with some initial values for the first two values of $x$ so that $x_0=x_1=0$

```python
def generate_autoreg(w):
    '''
    Generate some autocorrelated data starting with white noise
    time series `w`, for `nt` time points.
    Inputs:
        w [np.array] : white noise time series
        nt [int] : number of time points to generate
    Output:
        x [np.array] : autocorrelated time series
    '''
    nt = len(w)
    x = np.zeros((nt,))

    x[0] = w[0]
    #x[1] = w[1]
    for t in np.arange(1,nt):
        x[t] = 1.5*x[t-1] - 0.75*x[t-2] + w[t]
    return x
```

```python
nt = 250
x = generate_autoreg(white_noise(nt))
plt.plot(x)
```

```
[<matplotlib.lines.Line2D at 0x12ed58430>]
```

*(1 figure omitted — see the original notebook.)*

---

[← other values of n](11-other-values-of-n.md) · [Up: contents](index.md) · [Data as signal plus white noise →](13-data-as-signal-plus-white-noise.md)
