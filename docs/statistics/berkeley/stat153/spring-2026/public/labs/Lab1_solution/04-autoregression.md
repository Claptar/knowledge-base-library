---
title: Autoregression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Autoregression

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

## Data as signal plus white noise

Many datasets can be modeled as $v_t = s_t + w_t$, where $s_t$ is some signal of interest and $w_t$ is white noise. We will talk later about how we might find $s_t$ or other components of the signal. But for now, let's look at a few examples generating these types of data.

---

[← Moving average and filtering](03-moving-average-and-filtering.md) · [Up: contents](index.md) · [Random walk →](05-random-walk.md)
