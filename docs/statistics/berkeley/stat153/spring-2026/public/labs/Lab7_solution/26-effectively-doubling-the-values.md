---
title: effectively doubling the values.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# effectively doubling the values.

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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
## Part 3: Linear Filtering in the Frequency Domain

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
    # Hint: you can compute the sum using a loop or the geometric series formula
    A = np.zeros_like(omega, dtype=complex)
    for j in range(m):
        A += (1/m) * np.exp(-2*math.pi*1j*omega*j)  # FILL IN: (1/m) * exp(-2*pi*i*omega*j)
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

*(1 figure omitted — see the original notebook.)*

The simple moving average is called a "low-pass" filter. From looking at the plot above, what do you think this means? What happens to the frequencies as $m$ increases?

### Filtering a noisy signal

Now let's create a signal with a clear low-frequency component plus high-frequency noise, then apply a moving average filter and see how the spectrum changes.

```python
np.random.seed(10)
n = 500
t = np.arange(n)

---

[← which folds the negative-frequency power onto the positive side,](25-which-folds-the-negative-frequency-power-onto-the-positive-s.md) · [Up: contents](index.md) · [Signal: slow sinusoid + noise →](27-signal-slow-sinusoid-noise.md)
