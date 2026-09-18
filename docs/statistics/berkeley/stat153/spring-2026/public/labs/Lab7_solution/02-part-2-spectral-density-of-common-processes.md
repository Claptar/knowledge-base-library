---
title: 'Part 2: Spectral Density of Common Processes'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Part 2: Spectral Density of Common Processes

The spectral density is the theoretical quantity that the periodogram estimates:

$$f(\omega) = \sum_{h=-\infty}^{\infty} \gamma(h) e^{-2\pi i \omega h}$$

Let's compute and visualize the theoretical spectra and compare them to periodograms from simulated data.

## White noise spectrum

For white noise, $\gamma(h) = \sigma_w^2$ when $h=0$ and $0$ otherwise. So the spectral density is simply $f(\omega) = \sigma_w^2$. That is, it is flat across all frequencies.

```python
np.random.seed(42)
sigma_w = 2.0
n = 500

# Generate white noise
wn = np.random.normal(0, sigma_w, n)

# Compute the periodogram
freqs_wn, power_wn = periodogram(wn, fs=1)

# Plot periodogram vs. theoretical spectrum
plt.figure(figsize=(7, 3))
plt.plot(freqs_wn, power_wn, alpha=0.6, label='Periodogram')

# TODO: Plot the theoretical spectral density as a horizontal line
# Hint: For white noise, f(omega) = sigma_w^2
# But note scipy's periodogram normalization, so you may need to adjust by a factor.
# The total area under the periodogram should equal the variance.
# Note that scipy.signal.periodogram returns a one-sided spectrum by default (only [0,1/2]),
# which folds the negative-frequency power onto the positive side,
# effectively doubling the values.
plt.axhline(2*sigma_w**2, color='r', linewidth=2, label='Theoretical $f(\omega)$')  # FILL IN

plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title('White Noise Spectrum')
plt.legend()
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

The periodogram looks very noisy even though the *theoretical* spectrum is flat. Why? Does increasing $n$ help?

In this case, increasing $n$ actually doesn't help! You can estimate power at more and more frequencies, but the noise per bin stays the same.

---

---

[← Part 1: The Discrete Fourier Transform (DFT)](01-part-1-the-discrete-fourier-transform-dft.md) · [Up: contents](index.md) · [Part 3: Linear Filtering in the Frequency Domain →](03-part-3-linear-filtering-in-the-frequency-domain.md)
