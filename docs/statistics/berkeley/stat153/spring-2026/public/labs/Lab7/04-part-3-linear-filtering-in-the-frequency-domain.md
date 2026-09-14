---
title: 'Part 3: Linear Filtering in the Frequency Domain'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Part 3: Linear Filtering in the Frequency Domain

**Source:** [`public/labs/Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

A linear filter transforms $x_t$ into $y_t = \sum_j a_j x_{t-j}$.

In the frequency domain, the output spectrum is:
$$f_y(\omega) = |A(\omega)|^2 f_x(\omega)$$

where $A(\omega) = \sum_j a_j e^{-2\pi i \omega j}$ is the *frequency response function*.

This is powerful because **convolution in time becomes multiplication in frequency**.

### Simple moving average as a low-pass filter

A simple moving average of order $m$ uses weights $a_j = 1/m$ for $j = 0, 1, \dots, m-1$. Let's see how this reshapes the spectrum.

```python
def frequency_response_ma(omega, m):
    '''Compute |A(omega)|^2 for a simple moving average filter of order m.

    A(omega) = (1/m) * sum_{j=0}^{m-1} exp(-2*pi*i*omega*j)
    '''
    # TODO: Compute A(omega) and return |A(omega)|^2
    A = np.zeros_like(omega, dtype=complex)
    for j in range(m):
        A += # FILL IN
    return np.abs(A)**2
```

```python
omega = np.linspace(0, 0.5, 1000)

plt.figure(figsize=(7, 3))
for m in [3, 5, 11, 21]:
    plt.plot(omega, frequency_response_ma(omega, m), label=f'm={m}')

plt.xlabel('Frequency')
plt.ylabel('$|A(\omega)|^2$')
plt.title('Frequency Response of Moving Average Filters')
plt.legend()
plt.tight_layout()
```

The simple moving average is called a "low-pass" filter. From looking at the plot above, what do you think this means? What happens to the frequencies as $m$ increases?

### Filtering a noisy signal

Now let's create a signal with a clear low-frequency component plus high-frequency noise, then apply a moving average filter and see how the spectrum changes.

```python
np.random.seed(10)
n = 500
t = np.arange(n)

# Signal: slow sinusoid + noise
signal = 4*np.cos(2*math.pi*t*5/n)  # 5 cycles over n points
noise = np.random.normal(0, 6, n)
x = signal + noise

# Apply a moving average filter of order m
m = 11

# Compute the filtered signal using np.convolve with weights 1/m
weights = np.ones(m) / m
y = np.convolve(x, weights, mode='valid')

# Plot time domain
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.plot(t, x, alpha=0.6)
plt.plot(t, signal, 'r', linewidth=2)
plt.title('Original signal + noise')
plt.xlabel('Time')

plt.subplot(2,2,2)
plt.plot(y)
plt.plot(t, signal, 'r', linewidth=2)
plt.title(f'After MA filter (m={m})')
plt.xlabel('Time')

# Plot frequency domain
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

What do you notice about how both the time series and the frequency spectrum change after the filtering?

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
    return # FILL IN
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

Why does differencing remove trends? Think about what a trend looks like in the frequency domain.

---

---

[← Part 2: Spectral Density of Common Processes](03-part-2-spectral-density-of-common-processes.md) · [Up: contents](index.md) · [Part 4: Periodogram as a Noisy Estimator →](05-part-4-periodogram-as-a-noisy-estimator.md)
