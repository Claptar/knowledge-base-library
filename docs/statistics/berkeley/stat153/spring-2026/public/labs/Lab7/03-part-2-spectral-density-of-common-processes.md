---
title: 'Part 2: Spectral Density of Common Processes'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Part 2: Spectral Density of Common Processes

**Source:** [`public/labs/Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The spectral density is the theoretical quantity that the periodogram estimates:

$$f(\omega) = \sum_{h=-\infty}^{\infty} \gamma(h) e^{-2\pi i \omega h}$$

Let's compute and visualize the theoretical spectra and compare them to periodograms from simulated data.

### White noise spectrum

For white noise, $\gamma(h) = \sigma_w^2$ when $h=0$ and $0$ otherwise. So the spectral density is simply $f(\omega) = \sigma_w^2$. That is, it is flat across all frequencies.

```python
np.random.seed(42)
sigma_w = 2.0
n = 500

# Generate white noise with variance sigma_w for n points
wn = # FILL IN

# Compute the periodogram
freqs_wn, power_wn = periodogram(wn, fs=1)

# Plot periodogram vs. theoretical spectrum
plt.figure(figsize=(7, 3))
plt.plot(freqs_wn, power_wn, alpha=0.6, label='Periodogram')

# TODO: Plot the theoretical spectral density as a horizontal line
# Hint: For white noise, f(omega) = sigma_w^2
# The total area under the periodogram should equal the variance.
# Note that scipy.signal.periodogram returns a one-sided spectrum by default (only [0,1/2]),
# which folds the negative-frequency power onto the positive side,
# effectively doubling the values, so you will have to scale this value accordingly
plt.axhline(..., color='r', linewidth=2, label='Theoretical $f(\omega)$')  # FILL IN

plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title('White Noise Spectrum')
plt.legend()
plt.tight_layout()
```

**Question:** The periodogram looks very noisy even though the *theoretical* spectrum is flat. Why? Does increasing $n$ help?

---

---

[← Part 1: The Discrete Fourier Transform (DFT)](02-part-1-the-discrete-fourier-transform-dft.md) · [Up: contents](index.md) · [Part 3: Linear Filtering in the Frequency Domain →](04-part-3-linear-filtering-in-the-frequency-domain.md)
