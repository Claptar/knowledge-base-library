---
title: Apply to the slow track
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Apply to the slow track

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

CUTOFF_LP = 500   # Hz - this means we keep anything below this frequency for our lowpass filter (LP)
CUTOFF_HP = 3000  # Hz - this means we keep anything above this frequency for our highpass filter (HP)

y = y_solo
y_lp, sos_lp = apply_filter(y, sr, CUTOFF_LP, 'low')
y_hp, sos_hp = apply_filter(y, sr, CUTOFF_HP, 'high')

plot_filter_result(y_dance, y_lp, y_hp, sos_lp, sos_hp, sr,
                   CUTOFF_LP, CUTOFF_HP,
                   title='Filtered Slow Track')

print('Original:')
display(Audio(y, rate=sr))
print(f'Low-pass (< {CUTOFF_LP} Hz)')
display(Audio(y_lp, rate=sr))
print(f'High-pass (> {CUTOFF_HP} Hz)')
display(Audio(y_hp, rate=sr))
```

```
Original:
<IPython.lib.display.Audio object>
Low-pass (< 500 Hz)
<IPython.lib.display.Audio object>
High-pass (> 3000 Hz)
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

### Signals in the time domain

How does our low pass and high pass filter affect the signals in the time domain? Let's plot them.

```python
fig, ax = plt.subplots(figsize=(14, 3))
time_axis = np.arange(len(y)) / sr
ax.plot(time_axis, y/y.max(), linewidth=0.5, label='original')
ax.plot(time_axis, y_hp/y_hp.max(), linewidth=0.5, label='high pass')
ax.plot(time_axis, y_lp/y_lp.max(), linewidth=0.5, alpha=0.3, label='low pass')
ax.set_title('Waveform', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_xlim(0,time_axis[-1])
plt.legend(loc='right')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Filtering, convolution, and multiplication

The filter's **frequency response** $H(f)$ multiplies the signal's spectrum:
$$S_{\text{filtered}}(f) = |H(f)|^2 \cdot S_{\text{original}}(f)$$

In the time domain, this is **convolution** with the filter's impulse response. Multiplication in frequency = convolution in time.

Comparing the two tracks with the low-pass and high-pass filter, we can see that the low-pass filtered version is smoother and high-pass is spikier, but the specifics also depend on which track we're looking at and where the original signal frequencies lie in the space!

## Connection to Autocovariance, PSD, and Stationarity

- The autocovariance function and the power spectral density are a Fourier transform pair.
- **Stationarity**: `periodogram` and `welch` assume stationary statistics. When is that approximately true for music?

In this step, we'll use `statsmodels.tsa.stattools.acf` as in previous lectures.

```python

---

[← Apply to the dance track](28-apply-to-the-dance-track.md) · [Up: contents](index.md) · [statsmodels.tsa.stattools.acf computes the sample autocorrelation function. →](30-statsmodels-tsa-stattools-acf-computes-the-sample-autocorrel.md)
