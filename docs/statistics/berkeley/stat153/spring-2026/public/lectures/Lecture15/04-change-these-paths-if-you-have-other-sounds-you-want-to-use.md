---
title: Change these paths if you have other sounds you want to use
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Change these paths if you have other sounds you want to use

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← Load audio here](03-load-audio-here.md) · [Up: contents](index.md) · [Step 1: Waveform only - what do we get from this? →](05-step-1-waveform-only---what-do-we-get-from-this.md)
