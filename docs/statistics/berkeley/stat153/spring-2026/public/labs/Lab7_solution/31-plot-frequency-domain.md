---
title: Plot frequency domain
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot frequency domain

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

freqs_x, power_x = periodogram(x, fs=1)
freqs_y, power_y = periodogram(y, fs=1)

plt.subplot(2,2,3)
plt.plot(freqs_x, power_x)
plt.title('Spectrum of original')
plt.xlabel('Frequency')
plt.ylabel('Power')

plt.subplot(2,2,4)
plt.plot(freqs_y, power_y)
plt.title('Spectrum of filtered')
plt.xlabel('Frequency')
plt.ylabel('Power')

plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

What do you notice about how both the time series and the frequency spectrum change after the filtering?

The frequency spectrum after filtering has a flatter high frequency response, meaning these frequencies have been suppressed. This also shows up as a smoother looking (less jagged) time series in the time domain.

### First-difference filter as a high-pass filter

Taking first differences ($y_t = x_t - x_{t-1}$) is a common operation for removing trends. This is a linear filter with $a_0 = 1, a_1 = -1$.

```python
def frequency_response_diff(omega):
    '''
    Compute |A(omega)|^2 for the first-difference filter.

    A(omega) = 1 - exp(-2*pi*i*omega)
    '''
    # TODO: Compute |A(omega)|^2
    # Hint: You can show analytically that |A(omega)|^2 = 2 - 2*cos(2*pi*omega)
    return 2-2*np.cos(2*math.pi*omega)  # FILL IN
```

```python
omega = np.linspace(0, 0.5, 1000)

plt.figure(figsize=(7, 3))
plt.plot(omega, frequency_response_diff(omega), label='First difference')
plt.plot(omega, frequency_response_ma(omega, 5), label='MA(5)')
plt.xlabel('Frequency')
plt.ylabel('$|A(\omega)|^2$')
plt.title('Low-pass vs. High-pass Filters')
plt.legend()
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

Why does differencing remove trends? Think about what a trend looks like in the frequency domain.

Differencing removes low frequencies, which could look like a very slow oscillation (or even linear trend) in the time domain.

---
## Part 4: Periodogram as a Noisy Estimator

An important property of the periodogram: it is an **inconsistent** estimator of the spectral density. Even as $n \to \infty$, the periodogram does not converge to $f(\omega)$ — its variance doesn't shrink! Let's see this.

```python

---

[← Plot time domain](30-plot-time-domain.md) · [Up: contents](index.md) · [Simulate many periodograms from white noise and overlay them →](32-simulate-many-periodograms-from-white-noise-and-overlay-them.md)
