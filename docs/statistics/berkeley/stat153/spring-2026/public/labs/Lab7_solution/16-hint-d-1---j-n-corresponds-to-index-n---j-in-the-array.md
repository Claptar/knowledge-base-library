---
title: 'Hint: d(1 - j/n) corresponds to index (n - j) in the array'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Hint: d(1 - j/n) corresponds to index (n - j) in the array

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

for j in range(1, 6):
    power_j = np.abs(d_manual[j])**2
    power_mirror = np.abs(d_manual[n-j])**2  # FILL IN: |d[n-j]|^2
    print(f"j={j}: |d(j/n)|^2 = {power_j:.4f}, |d(1-j/n)|^2 = {power_mirror:.4f}")
```

```
j=1: |d(j/n)|^2 = 0.3022, |d(1-j/n)|^2 = 0.3022
j=2: |d(j/n)|^2 = 0.0796, |d(1-j/n)|^2 = 0.0796
j=3: |d(j/n)|^2 = 0.2221, |d(1-j/n)|^2 = 0.2221
j=4: |d(j/n)|^2 = 0.1463, |d(1-j/n)|^2 = 0.1463
j=5: |d(j/n)|^2 = 214.0105, |d(1-j/n)|^2 = 214.0105
```

Why does this symmetry hold? What does it tell us about the information content of the DFT?

---
## Part 2: Spectral Density of Common Processes

The spectral density is the theoretical quantity that the periodogram estimates:

$$f(\omega) = \sum_{h=-\infty}^{\infty} \gamma(h) e^{-2\pi i \omega h}$$

Let's compute and visualize the theoretical spectra and compare them to periodograms from simulated data.

### White noise spectrum

For white noise, $\gamma(h) = \sigma_w^2$ when $h=0$ and $0$ otherwise. So the spectral density is simply $f(\omega) = \sigma_w^2$. That is, it is flat across all frequencies.

```python
np.random.seed(42)
sigma_w = 2.0
n = 500

---

[← TODO: Verify that |d(j/n)|^2 = |d(1-j/n)|^2 for our test signal](15-todo-verify-that-d-j-n-2-d-1-j-n-2-for-our-test-signal.md) · [Up: contents](index.md) · [Generate white noise →](17-generate-white-noise.md)
