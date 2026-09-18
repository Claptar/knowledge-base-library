---
title: Quick poll - Guess the category
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Quick poll - Guess the category

1. Mostly one instrument
2. A cappella (singing only, no instruments)
3. Strong beat / danceable
4. Very repetitive
5. Very slow

```python
# Load audio here

SR = 22050  # target sample rate (librosa default)

def load_clip(path, duration=60, offset=0):
    """Load an audio file. Returns (waveform, sample_rate)."""
    import librosa
    y, sr = librosa.load(path, sr=SR, duration=duration, offset=offset)
    print(f'Loaded: {path}  ({len(y)/sr:.1f}s, {len(y):,} samples, fs={sr} Hz)')
    return y, sr

# Change these paths if you have other sounds you want to use
y_solo, sr = load_clip('sounds/acappella/lec15_ariana.wav')       # Demo 1
y_rep,  sr = load_clip('sounds/repetitive/lec15_60scardin.wav')    # Demo 2
#y_rep,  sr = load_clip('sounds/dance/lec15_makemefeel.wav')   # Demo 2
y_dance, sr = load_clip('sounds/dance/lec15_gasolina.wav')    # Demo 3 & 4
y_slow,  sr = load_clip('sounds/one_inst/lec15_flowerdance.wav') # Demo 4 & 5
```

```
Loaded: sounds/acappella/lec15_ariana.wav  (24.3s, 536,111 samples, fs=22050 Hz)
Loaded: sounds/repetitive/lec15_60scardin.wav  (31.1s, 685,134 samples, fs=22050 Hz)
Loaded: sounds/dance/lec15_gasolina.wav  (41.3s, 909,809 samples, fs=22050 Hz)
Loaded: sounds/one_inst/lec15_flowerdance.wav  (49.6s, 1,093,779 samples, fs=22050 Hz)
```

## 1. Plotting sound time series
### Waveform → Periodogram → Spectrogram

**Song:** Solo instrument or A cappella

Here we will show three views of the same signal, using tools we already know as well as the spectrogram, which is something new:
1. **Waveform** — amplitude vs. time
2. **Periodogram** via `scipy.signal.periodogram` — power vs. frequency
3. **Spectrogram** via `scipy.signal.spectrogram` — power vs. frequency vs. time

```python
# Step 1: Waveform only - what do we get from this?

fig, ax = plt.subplots(figsize=(14, 3))
time_axis = np.arange(len(y_solo)) / sr
ax.plot(time_axis, y_solo, color='#0f3460', linewidth=0.3)
ax.set_title('Waveform', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_xlim(0,time_axis[-1])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
# Step 2: Periodogram - can we tell which notes are in the song?

fig, ax = plt.subplots(figsize=(14, 3))
f_psd, Pxx = periodogram(y_solo, fs=sr)
ax.plot(f_psd, Pxx, color='#e94560', linewidth=0.6)
ax.set_title('periodogram(y, fs=sr) — Which frequencies are present?', fontsize=14, fontweight='bold')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('PSD (V²/Hz)')
ax.set_xlim(0, 2000)
plt.tight_layout()
plt.show()

# Could you sing the song from this or identify the melody?
```

*(1 figure omitted — see the original notebook.)*

```python
# Step 3: Spectrogram
# This is scipy.signal.spectrogram — periodogram on a sliding window.

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
# Let's look at how nperseg affects both ∆t and ∆f
# This is the same Δf = fs/N relationship from when we discussed
# periodogram frequency resolution.

print('Time-Frequency Resolution Tradeoff')
print('=' * 55)
print(f'{"nperseg":>10} | {"Δt (s)":>10} | {"Δf (Hz)":>10} | {"Δt × Δf":>10}')
print('-' * 55)
for nps in [128, 2048, 8192]:
    dt = nps / sr     # time resolution in ms
    df = sr / nps            # freq resolution in Hz
    print(f'{nps:>10} | {dt:>10.3f} | {df:>10.1f} | {dt*df:>10.2f}')

print()
print('Δt × Δf = 1 for all segment lengths.')
print('The periodogram is the extreme: N = len(signal) → best Δf, but Δt = entire signal.')
```

```
Time-Frequency Resolution Tradeoff
=======================================================
   nperseg |     Δt (s) |    Δf (Hz) |    Δt × Δf
-------------------------------------------------------
       128 |      0.006 |      172.3 |       1.00
      2048 |      0.093 |       10.8 |       1.00
      8192 |      0.372 |        2.7 |       1.00

Δt × Δf = 1 for all segment lengths.
The periodogram is the extreme: N = len(signal) → best Δf, but Δt = entire signal.
```

### Connection to prior datasets

Remember when we discussed `periodogram(sunspots, fs=2.0)` — the frequency resolution was $\Delta f = 2/N$ cycles per year. The whole signal gave us fine frequency resolution. But we lost all information about *when* the 11-year cycle was strong or weak.

The spectrogram is just a periodogram computed on a **sliding window**. A shorter window means we have better time resolution but coarser frequency resolution. The periodogram is the limit case: window = entire signal.

## Welch vs. Raw Periodogram

Now we will show the same `periodogram` vs. `welch` comparison we've done in class, but now on music instead of simulated data.

```python
# We will use the following functions:
#   scipy.signal.periodogram  — single FFT of entire signal
#   scipy.signal.welch        — average periodograms over overlapping segments

fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

# 3a. Raw periodogram
f_raw, Pxx_raw = periodogram(y_dance, fs=sr)
axes[0].plot(f_raw, Pxx_raw, color='#e94560', linewidth=0.4, alpha=0.8)
axes[0].set_title('periodogram(y, fs=sr)')
axes[0].set_ylabel('Power')
axes[0].set_xlim(0, 4000)

# 3b. Welch with different segment lengths
for nperseg in [4096, 2048, 1024]:
    f_w, Pxx_w = welch(y_dance, fs=sr, nperseg=nperseg, noverlap=nperseg//2)
    n_segs = (len(y_dance) - nperseg) // (nperseg//2) + 1
    axes[1].plot(f_w, Pxx_w, linewidth=1.2, label=f'welch(nperseg={nperseg}, ~{n_segs} segments)')

axes[1].set_title('welch(y, fs=sr, nperseg=...)')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Power')
axes[1].legend(fontsize=9, loc='upper right')

plt.tight_layout()
plt.show()

print('Dance track:')
display(Audio(y_dance, rate=sr))
```

```
Dance track:
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

Now let's overlay some raw periodograms from different chunks of the music data. Do you think the individual periodograms will look the same or different?

```python
# --- Overlay raw periodograms from different chunks ---
# This is the key visualization: each chunk gives a DIFFERENT periodogram,
# even though the signal is approximately stationary.
# Welch averages over these to reduce variance.

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

chunk_len = sr * 1  # 1-second chunks
n_chunks = min(30, len(y_dance) // chunk_len)

for i in range(n_chunks):
    chunk = y_dance[i*chunk_len:(i+1)*chunk_len]
    f_c, Pxx_c = periodogram(chunk, fs=sr)
    axes[0].plot(f_c, Pxx_c, linewidth=0.5, alpha=0.5)

axes[0].set_title(f'{n_chunks} raw periodograms from 1s chunks')
axes[0].set_xlabel('Frequency (Hz)')
axes[0].set_ylabel('Power')
axes[0].set_xlim(0, 3000)

# Welch does this averaging for us
f_w, Pxx_w = welch(y_dance, fs=sr, nperseg=chunk_len, noverlap=chunk_len//2)
axes[1].plot(f_w, Pxx_w, color='#e94560', linewidth=1.5)
axes[1].set_title('welch average (overlapping segments)')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Power')
axes[1].set_xlim(0, 3000)

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Low-Pass and High-Pass Filters

Next let's show what low-pass and high-pass filters do to a signal both in frequency and in time. Here we will use Butterworth filters, which are designed to have frequencies as flat as possible in the pass band (the frequencies you want to keep or "pass"). We will:

1. Listen to the filtered audio
2. See the spectrogram before and after
3. Examine the filter's frequency response

We'll use the slow and dance songs here, but you can try any of them you'd like.

```python
# Filter design and application
# First run this cell to get the functions we need to create and apply filters to the data
#
# scipy.signal.butter  — design a Butterworth filter
# scipy.signal.sosfiltfilt — apply it (zero-phase, so no time shift)
# scipy.signal.sosfreqz — compute the filter's frequency response

def apply_filter(y, sr, cutoff, btype, order=5):
    """Design and apply a Butterworth filter.

    btype: 'low' or 'high'
    Returns: filtered signal, filter coefficients (sos)
    """
    sos = butter(order, cutoff, btype=btype, fs=sr, output='sos')
    y_filt = sosfiltfilt(sos, y)
    return y_filt, sos


def plot_filter_result(y_orig, y_lp, y_hp, sos_lp, sos_hp, sr,
                       cutoff_lp, cutoff_hp, title=''):
    """Comprehensive filter demo figure."""
    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(3, 3, hspace=0.45, wspace=0.3)

    # --- Row 1: Filter frequency response (using sosfreqz) ---
    ax_resp = fig.add_subplot(gs[0, :])
    for sos, label, color in [
        (sos_lp, f'Low-pass (cutoff={cutoff_lp} Hz)', '#0f3460'),
        (sos_hp, f'High-pass (cutoff={cutoff_hp} Hz)', '#e94560'),
    ]:
        w, h = sosfreqz(sos, worN=2048, fs=sr)
        ax_resp.plot(w, 20*np.log10(np.abs(h) + 1e-10), color=color,
                     linewidth=2, label=label)
    ax_resp.axhline(-3, color='#aaa', linestyle='--', linewidth=0.8, label='-3 dB')
    ax_resp.set_title('Filter frequency responses (sosfreqz)', fontsize=12, fontweight='bold')
    ax_resp.set_xlabel('Frequency (Hz)')
    ax_resp.set_ylabel('Gain (dB)')
    ax_resp.set_xlim(0, 5000)
    ax_resp.set_ylim(-60, 5)
    ax_resp.legend(fontsize=10)

    # --- Row 2: Spectrograms (original, LP, HP) ---
    for i, (y, lab) in enumerate([
        (y_orig, 'Original'),
        (y_lp, f'Low-pass (< {cutoff_lp} Hz)'),
        (y_hp, f'High-pass (> {cutoff_hp} Hz)'),
    ]):
        ax = fig.add_subplot(gs[1, i])
        nps = 2048
        f_s, t_s, Sxx = spectrogram(y, fs=sr, nperseg=nps, noverlap=nps*3//4)
        ax.pcolormesh(t_s, f_s, 10*np.log10(Sxx + 1e-10),
                      cmap='magma', shading='gouraud')
        ax.set_ylim(0, 5000)
        ax.set_title(lab, fontsize=10, fontweight='bold')
        ax.set_xlabel('Time (s)')
        if i == 0:
            ax.set_ylabel('Frequency (Hz)')

    # --- Row 3: Periodograms overlay ---
    ax_psd = fig.add_subplot(gs[2, :])
    for y, lab, color, lw in [
        (y_orig, 'Original', '#aaa', 0.5),
        (y_lp, f'Low-pass (< {cutoff_lp} Hz)', '#0f3460', 1.2),
        (y_hp, f'High-pass (> {cutoff_hp} Hz)', '#e94560', 1.2),
    ]:
        f_w, Pxx_w = welch(y, fs=sr, nperseg=4096)
        ax_psd.semilogy(f_w, Pxx_w, color=color, linewidth=lw, label=lab)
    ax_psd.set_title('PSD before and after filtering (welch)', fontsize=12, fontweight='bold')
    ax_psd.set_xlabel('Frequency (Hz)')
    ax_psd.set_ylabel('PSD')
    ax_psd.set_xlim(0, 5000)
    ax_psd.legend(fontsize=9)

    if title:
        plt.suptitle(title, fontsize=14, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.show()
```

```python
# Apply to the dance track

CUTOFF_LP = 500   # Hz - this means we keep anything below this frequency for our lowpass filter (LP)
CUTOFF_HP = 3000  # Hz - this means we keep anything above this frequency for our highpass filter (HP)

y = y_dance
y_lp, sos_lp = apply_filter(y, sr, CUTOFF_LP, 'low')
y_hp, sos_hp = apply_filter(y, sr, CUTOFF_HP, 'high')

plot_filter_result(y_dance, y_lp, y_hp, sos_lp, sos_hp, sr,
                   CUTOFF_LP, CUTOFF_HP,
                   title='Filtered Dance Track')

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

```python
# Apply to the slow track

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
# statsmodels.tsa.stattools.acf computes the sample autocorrelation function.

max_lag_samples = sr  # 1 second of lags
lag_axis_ms = np.arange(max_lag_samples + 1) / sr * 1000  # in ms

fig, axes = plt.subplots(2, 2, figsize=(14, 8))

signals_all = [
    (y_solo,  'Solo / A cappella', '#e94560'),
    (y_rep,   'Repetitive',        '#533483'),
    (y_dance, 'Danceable',         '#0f3460'),
    (y_slow,  'Slow',              '#16c79a'),
]

for ax, (y, name, color) in zip(axes.flat, signals_all):
    acf_vals = acf(y, nlags=max_lag_samples, fft=True)
    ax.plot(lag_axis_ms, acf_vals, color=color, linewidth=0.6)
    ax.axhline(0, color='#aaa', linewidth=0.5)
    ax.set_title(name, fontsize=12, fontweight='bold')
    ax.set_xlabel('Lag (ms)')
    ax.set_ylabel('ACF')
    ax.set_ylim(-0.5, 1.05)

plt.suptitle('Demo 5a: Sample ACF (statsmodels.tsa.stattools.acf) — What patterns repeat?',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### What do we see in the ACF for these different songs?

What if we try other dance songs, slow songs, a cappella songs?

### Relationship between periodogram and autocovariance

Here we will show that the periodogram is the same as the FFT of the autocovariance function directly by plotting the power spectrum in two ways:
1. Using welch estimation `scipy.signal.welch`
2. Using `np.fft.rfft` on the sample autocovariance

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

for ax, (y, name, color) in zip(axes.flat, signals_all):
    # Method 1: Welch PSD
    f_w, Pxx_w = welch(y, fs=sr, nperseg=4096)

    # Method 2: FFT of the ACF
    acf_vals = acf(y, nlags = len(y)-1, fft=True)
    psd_from_acov = np.abs(np.fft.rfft(acf_vals))
    f_acov = np.fft.rfftfreq(len(acf_vals), d=1/sr)

    # Plot both (scale the FFT version to match Welch for visual comparison)
    ax.semilogy(f_w, Pxx_w, color=color, linewidth=1.2, label='welch')
    scale = np.max(Pxx_w) / np.max(psd_from_acov)
    ax.semilogy(f_acov, psd_from_acov * scale,
                color='#aaa', linewidth=0.7, alpha=0.7, label='FFT of acf')
    ax.set_title(name, fontsize=12, fontweight='bold')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_xlim(0, 4000)
    if ax in [axes[0,0], axes[1,0]]:
        ax.set_ylabel('PSD')
    ax.legend(fontsize=8)

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Stationarity check

If the signal is stationary, the PSD should look similar no matter which chunk of the signal we compute it from. This is the same logic behind why Welch works — it assumes each segment is a sample from the same stationary process.

```python
def plot_stationarity_check(y, sr, name, color, n_segments=6):
    """Overlay Welch PSD from time segments to visually check stationarity."""
    seg_len = len(y) // n_segments

    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(n_segments):
        chunk = y[i*seg_len:(i+1)*seg_len]
        f, Pxx = welch(chunk, fs=sr, nperseg=min(2048, seg_len//2))
        alpha = 0.3 + 0.7 * i / n_segments
        ax.semilogy(f, Pxx, color=color, alpha=alpha, linewidth=1,
                     label=f'Segment {i+1}')

    ax.set_title(f'{name} — Do all segments have the same PSD?',
                  fontsize=12, fontweight='bold')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('PSD')
    ax.set_xlim(0, 4000)
    ax.legend(fontsize=8, ncol=3)
    plt.tight_layout()
    plt.show()


print('Stationarity check: if PSD is stable across time segments,')
print('the signal is approximately stationary and our spectral estimates are valid.\n')

for y, name, color in signals_all:
    plot_stationarity_check(y, sr, name, color)
```

```
Stationarity check: if PSD is stable across time segments,
the signal is approximately stationary and our spectral estimates are valid.
```

*(4 figures omitted — see the original notebook.)*

## Bonus: Build Your Own Spectrogram from `np.fft`

Since the spectrogram is really just the periodogram on a sliding window, let's build one from scratch.

```python
# Build a spectrogram from scratch

def my_spectrogram(y, fs, nperseg=2048, noverlap=None):
    """Spectrogram from np.fft.rfft — no scipy needed."""
    if noverlap is None:
        noverlap = nperseg // 2

    hop = nperseg - noverlap
    n_windows = (len(y) - nperseg) // hop + 1

    freqs = np.fft.rfftfreq(nperseg, d=1/fs)
    times = (np.arange(n_windows) * hop + nperseg // 2) / fs
    window = np.hanning(nperseg)

    Sxx = np.zeros((len(freqs), n_windows))
    for i in range(n_windows):
        start = i * hop
        segment = y[start:start+nperseg] * window
        Y = np.fft.rfft(segment)
        Sxx[:, i] = np.abs(Y)**2 / (fs * np.sum(window**2))

    return freqs, times, Sxx


# Compare to scipy
fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
nps = 2048

f1, t1, S1 = spectrogram(y_rep, fs=sr, nperseg=nps, noverlap=nps//2)
axes[0].pcolormesh(t1, f1, 10*np.log10(S1+1e-10), cmap='magma', shading='gouraud')
axes[0].set_title('scipy.signal.spectrogram', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Frequency (Hz)')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylim(0, 1500)

f2, t2, S2 = my_spectrogram(y_rep, fs=sr, nperseg=nps, noverlap=nps//2)
axes[1].pcolormesh(t2, f2, 10*np.log10(S2+1e-10), cmap='magma', shading='gouraud')
axes[1].set_title('my_spectrogram (np.fft by hand)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylim(0, 1500)

plt.suptitle('No magic — spectrogram = sliding periodogram',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Lecture 15: Time-Frequency Analysis with Music](01-lecture-15-time-frequency-analysis-with-music.md) · [Up: contents](index.md)
