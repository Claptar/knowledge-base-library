---
title: This is scipy.signal.spectrogram — periodogram on a sliding window.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# This is scipy.signal.spectrogram — periodogram on a sliding window.

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, ax = plt.subplots(figsize=(14, 4))
nperseg = 2048
f_spec, t_spec, Sxx = spectrogram(y_solo, fs=sr, nperseg=nperseg,
                                    noverlap=nperseg*3//4)
ax.pcolormesh(t_spec, f_spec, 10*np.log10(Sxx + 1e-10),
              cmap='magma', shading='gouraud')
ax.set_ylim(0, 2000)
ax.set_title(f'spectrogram(y, fs=sr, nperseg={nperseg})')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### How do we get the spectrogram?

The periodogram is essentially:
```python
dft_y = np.fft.rfft(y)               # FFT of the whole signal, rfft gives only the positive frequencies
Pxx = (1/(fs*N)) * np.abs(dft_y)**2  # squared magnitude, normalized
freqs = np.fft.rfftfreq(N, d=1/fs)
```

The spectrogram is just this applied to overlapping windows. The steps are as follows:
1. Chop the signal into short chunks (each of length `nperseg`)
2. Compute the periodogram of each chunk
3. Stack them side by side to create a frequency x time matrix

So we have:
- The waveform shows **when** (loud vs quiet), but doesn't show **what** frequencies.
- The periodogram shows **what frequencies** are present across the whole sound, but loses time information
- The spectrogram shows **both**, but how well can it show both? We'll check out the difference between frequency and time resolution next.

---
## 2. Time-Frequency Tradeoff via Window Length

So why can't we have perfect resolution in both time AND frequency? Recall from the periodogram: the frequency resolution is $\Delta f = f_s / N$ where $N$ is the number of samples. In a spectrogram, each window has $N = $ `nperseg`
samples, and the time resolution is $\Delta t = $ `nperseg` $/ f_s$.

So: $\Delta t \times \Delta f = 1$

Remember we saw this when using the welch method for the periodogram to calculate our periodogram with different segment lengths and average. Smaller segments in the periodogram led to more segments to average over and thus lower variance, but worse frequency resolution. Larger segments in the periodogram let to better frequency resolution but a noisier estimate. Here this is similar, but we have both time and frequency to worry about.

Next we will compute the spectrogram three times with different `nperseg` samples, leaving everything else the same.

```python
window_configs = [
    (256,  f'Short window\nnperseg=256 (~{256/sr*1000:.0f}ms)\nΔf={sr/256:.0f} Hz'),
    (2048, f'Medium window\nnperseg=2048 (~{2048/sr*1000:.0f}ms)\nΔf={sr/2048:.1f} Hz'),
    (8192, f'Long window\nnperseg=8192 (~{8192/sr*1000:.0f}ms)\nΔf={sr/8192:.1f} Hz'),
]

fig, axes = plt.subplots(3,1, figsize=(14,10), sharey=True)

for ax, (nps, label) in zip(axes, window_configs):
    f_s, t_s, Sxx = spectrogram(y_rep, fs=sr, nperseg=nps, noverlap=nps*3//4)
    ax.pcolormesh(t_s, f_s, 10*np.log10(Sxx + 1e-10),
                  cmap='magma', shading='gouraud')
    ax.set_ylim(0, 5000)
    ax.set_title(label, fontsize=10, fontweight='bold')
    ax.set_xlabel('Time (s)')
    if ax == axes[0]:
        ax.set_ylabel('Frequency (Hz)')

plt.tight_layout()
plt.show()

print('Repetitive track:')
display(Audio(y_rep, rate=sr))
```

```
Repetitive track:
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Step 3: Spectrogram](08-step-3-spectrogram.md) · [Up: contents](index.md) · [Let's look at how nperseg affects both ∆t and ∆f →](10-let-s-look-at-how-nperseg-affects-both-t-and-f.md)
