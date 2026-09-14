---
title: Simulate many periodograms from white noise and overlay them
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulate many periodograms from white noise and overlay them

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.random.seed(42)
sigma2 = 1.0
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for idx, n in enumerate([64, 256, 1024]):
    for rep in range(20):
        wn = np.random.normal(0, np.sqrt(sigma2), n)
        freqs, power = periodogram(wn, fs=1)
        axes[idx].plot(freqs, power, alpha=0.2, color='steelblue')

    axes[idx].axhline(2 * sigma2, color='r', linewidth=2, label='$2\sigma^2$')
    axes[idx].set_title(f'n = {n}')
    axes[idx].set_xlabel('Frequency')
    axes[idx].set_ylim([0, 15])
    if idx == 0:
        axes[idx].set_ylabel('Power')
    axes[idx].legend(fontsize=8)
plt.suptitle('Periodogram variability does NOT decrease with n', y=1.02)
plt.tight_layout()
```

Each blue line is one periodogram. The red line is the true spectral density.

Notice that as $n$ grows from 64 to 1024, the periodogram gets *denser*
(more Fourier frequencies), but the scatter around the red line doesn't shrink at all.
Every individual periodogram ordinate has roughly the same wild variability regardless of $n$.

## Averaging the periodogram

If we could observe many independent copies of the same process, we could average
their periodograms. Since the periodogram is unbiased ($E[P(\omega)] \approx f(\omega)$),
the average converges to $f(\omega)$ by the law of large numbers.

Of course, in practice we usually only have *one* time series — but this exercise
shows the principle.

```python
np.random.seed(153)
n = 256
num_reps = [1, 5, 20, 100]

fig, axes = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)

for ax, K in zip(axes, num_reps):
    # Average K periodograms
    avg_power = None
    for rep in range(K):
        # Create a white noise signal with mean 0 and variance sigma^2
        # for n time points
        wn = np.random.normal(0, np.sqrt(sigma2), n)

        # Calculate the periodogram
        freqs, power = periodogram(wn, fs=1)

        # increment avg_power (later we'll divide by K)
        if avg_power is None:
            avg_power = power.copy()
        else:
            avg_power += power
        # Also plot individuals faintly for small K
        if K <= 5:
            ax.plot(freqs, power, alpha=0.15, color='steelblue', lw=0.5)
    avg_power /= K

    ax.plot(freqs, avg_power, lw=1.5, label=f'Avg of {K}')
    ax.axhline(2 * sigma2, color='r', lw=2, label='$2\sigma^2$')
    ax.set_title(f'K = {K} realization{"s" if K > 1 else ""}', fontsize=11)
    ax.set_xlabel('Frequency')
    ax.set_ylim([0, 8])

axes[0].set_ylabel('Power')
fig.suptitle('Averaging periodograms across independent realizations (n = 256 each)',
             y=1.02, fontsize=13)
plt.tight_layout()
```

With $K = 1$ our estimates are very noisy. By $K = 100$, the average is nearly flat at $2\sigma^2$.
By law of large numbers, we see this convergence when averaging independent, unbiased estimates.

**But we usually only have one time series.** So how do we get this averaging effect?

## Averaging across neighboring frequencies (Daniell smoother)

Another way that we can smooth the periodogram is by averaging across neighboring frequencies, rather than realizations of a time series (which we often don't have). For a smooth spectral density, neighboring periodogram ordinates are approximately independent and have approximately the same expectation.
So averaging $2L+1$ neighbors is like averaging $2L+1$ independent estimates:

$$\hat{f}(\omega) = \frac{1}{2L+1}\sum_{k=-L}^{L} P\!\left(\omega + \frac{k}{n}\right)$$

This reduces variance by a factor of roughly $1/(2L+1)$, at the cost of some bias
(blurring in frequency).

```python
def daniell_smooth(power, L):
    """Smooth a periodogram by averaging 2L+1 neighbors."""
    kernel = np.ones(2 * L + 1) / (2 * L + 1)
    return np.convolve(power, kernel, mode='same')

np.random.seed(42)
n = 512
wn = np.random.normal(0, np.sqrt(sigma2), n)
freqs, power = periodogram(wn, fs=1)

L_values = [0, 3, 10, 30]

fig, axes = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)

for ax, L in zip(axes, L_values):
    if L == 0:
        smoothed = power
        label = 'Raw periodogram'
    else:
        smoothed = daniell_smooth(power, L)
        label = f'Smoothed (2L+1 = {2*L+1})'

    ax.plot(freqs, smoothed, color='steelblue', lw=0.8, label=label)
    ax.axhline(2 * sigma2, color='r', lw=2, label='$2\sigma^2$')
    ax.set_title(f'L = {L}  (window = {2*L+1})', fontsize=11)
    ax.set_xlabel('Frequency')
    ax.set_ylim([0, 8])
    ax.legend(fontsize=8)

axes[0].set_ylabel('Power')
fig.suptitle('Daniell smoother: averaging neighboring frequencies from ONE time series',
             y=1.02, fontsize=13)
plt.tight_layout()
```

This is the same idea as before, but now we're averaging across frequencies instead of across realizations or repetitions of our time series. With $L = 30$ (averaging 61 neighbors), the estimate is nearly flat.

For white noise, there's no bias from smoothing since the true spectrum is already constant. For a process with a peaked spectrum, smoothing would flatten the peak, so this can introduce bias in our estimates.

## Comparing averaging methods

Let's put them side by side with the same effective number of averages, so you can see that they give similar results.

```python
np.random.seed(99)
n = 512
K = 21  # number of realizations to average
L = int((K-1)/2)  # Daniell half-width, so 2L+1 = K neighbors

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

---

[← Lecture 14](01-lecture-14.md) · [Up: contents](index.md) · [(a) Single raw periodogram →](03-a-single-raw-periodogram.md)
