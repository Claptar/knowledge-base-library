---
title: 'Part 1: The Discrete Fourier Transform (DFT)'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Part 1: The Discrete Fourier Transform (DFT)

**Source:** [`public/labs/Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Recall from last lecture that the periodogram used coefficients:

$$a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi t j/n), \quad b_j = \frac{2}{n}\sum_{t=1}^n x_t \sin(2\pi t j/n)$$

The DFT wraps these together using Euler's formula $e^{-i\theta}=\cos\theta - i\sin\theta$:

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i 2\pi t j/n}$$

And the scaled periodogram is $P(j/n) = \frac{4}{n}|d(j/n)|^2$.

Let's implement the DFT by hand and compare it to `numpy.fft.fft`.

### Implement the DFT manually

Write a function that computes $d(j/n)$ for all $j = 0, 1, \dots, n-1$.

```python
def dft(x):
    '''Compute the Discrete Fourier Transform of signal x.

    Parameters
    ----------
    x : array of length n

    Returns
    -------
    d : complex array of length n, where d[j] = d(j/n)
    '''
    n = len(x)
    t = np.arange(1, n + 1)  # t = 1, ..., n
    d = np.zeros(n, dtype=complex)

    for j in range(n):
        # TODO: Compute d[j] using the DFT formula
        d[j] = # FILL IN

    return d
```

### Compare your DFT to numpy's FFT

Note: `numpy.fft.fft` uses the convention $X[j] = \sum_{t=0}^{n-1} x_t e^{-i 2\pi t j/n}$ (no $1/\sqrt{n}$ scaling, and $t$ starts at 0). So to compare, we need to account for the different normalization and indexing.

```python
# Create a test signal: sum of two sinusoids + noise
np.random.seed(42)
n = 100
t = np.arange(1, n+1)

# You can also try changing the cycles here (j/n) and the amplitudes of the
# sin and cos
x = 3*np.cos(2*math.pi*t*5/n) + 2*np.sin(2*math.pi*t*12/n) + np.random.normal(0, 0.5, n)

# Compute using your function
d_manual = dft(x)

# Compute using numpy (adjust for our convention)
# numpy uses t=0,...,n-1 and no 1/sqrt(n) normalization
# Our convention uses t=1,...,n and 1/sqrt(n)
# To match: multiply numpy result by exp(-i*2pi*j/n)/sqrt(n) to shift from 0-indexing to 1-indexing
fft_numpy = np.fft.fft(x)
j_vals = np.arange(n)
d_numpy = 1/np.sqrt(n) * fft_numpy * np.exp(-1j*2*math.pi*j_vals/n)

# Check they match by plotting both
plt.figure()
plt.plot(d_manual)
plt.plot(d_numpy)

plt.figure()
plt.plot(fft_numpy)
print("Max difference between manual and numpy DFT:", np.max(np.abs(d_manual - d_numpy)))
```

### From DFT to periodogram

The scaled periodogram is $P(j/n) = \frac{4}{n}|d(j/n)|^2$. Let's compute it from the DFT and compare to `scipy.signal.periodogram`.

```python
# Compute the scaled periodogram from our DFT
P_manual = # FILL IN using the equation above

# Only plot up to the Nyquist frequency (j = 0, ..., n/2)
freqs_manual = np.arange(n // 2 + 1) / n  # frequencies j/n

# Compare with scipy periodogram (fs=1 so frequencies are in cycles/sample)
freqs_scipy, power_scipy = periodogram(x, fs=1)

plt.figure(figsize=(10, 3))
plt.subplot(1,2,1)
plt.stem(freqs_manual, P_manual[:n // 2 + 1])
plt.title('Our periodogram (from DFT)')
plt.xlabel('Frequency (cycles/sample)')
plt.ylabel('Power')

plt.subplot(1,2,2)
plt.stem(freqs_scipy, power_scipy)
plt.set_title('scipy.signal.periodogram')
plt.xlabel('Frequency (cycles/sample)')
plt.ylabel('Power')
plt.tight_layout()

# Note: scipy uses a slightly different normalization. The shapes should match
# even if the scale differs. What normalization does scipy use?
```

### The symmetry property

We noted that $P(j/n) = P(1 - j/n)$, which is why we only need to look at frequencies up to 1/2. Let's verify this.

```python
# TODO: Verify that |d(j/n)|^2 = |d(1-j/n)|^2 for our test signal
# Hint: d(1 - j/n) corresponds to index (n - j) in the array

for j in range(1, 6):
    power_j = np.abs(d_manual[j])**2
    power_mirror = # FILL IN: |d[n-j]|^2
    print(f"j={j}: |d(j/n)|^2 = {power_j:.4f}, |d(1-j/n)|^2 = {power_mirror:.4f}")
```

Why does this symmetry hold? What does it tell us about the information content of the DFT?

---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Part 2: Spectral Density of Common Processes →](03-part-2-spectral-density-of-common-processes.md)
