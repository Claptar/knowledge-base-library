---
title: 'Lecture 15: Time-Frequency Analysis with Music'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 15: Time-Frequency Analysis with Music

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

This notebook uses songs from the class playlist to build intuition for
spectral analysis concepts — using the same tools from our course:
`scipy.signal.periodogram`, `scipy.signal.welch`, `statsmodels.tsa.stattools.acf`,
and `np.fft`.

| Demo | Song Category | Concept |
|------|--------------|--------|
| 1 | Solo instrument / A cappella | Waveform → Periodogram → Spectrogram |
| 2 | Repetitive song | Time-frequency tradeoff (window length) |
| 3 | Danceable / strong beat | Welch vs. raw periodogram (bias-variance) |
| 4 | Slow + Danceable | Low-pass and high-pass filtering |
| 5 | All categories | Autocovariance, PSD, and stationarity |

---

## Setup & Audio Loading

We use:
- `scipy.signal` — `periodogram`, `welch`, `spectrogram`, `butter`, `sosfiltfilt`
- `statsmodels.tsa.stattools` — `acf`
- `numpy.fft` — for building things from scratch
- `librosa` — just for loading audio files (it handles mp3/wav/etc.)
- `IPython.display.Audio` — so we can listen to the sounds in the notebook

**To use your own songs:** You can record some audio using software like [Audacity](https://audio.com/download/audacity). Record and export a clip (30–60s) as `.wav` or `.mp3` and update the file paths below.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import signal
from scipy.signal import periodogram, welch, spectrogram, butter, sosfiltfilt, sosfreqz
from statsmodels.tsa.stattools import acf
from IPython.display import Audio, display
import warnings
warnings.filterwarnings('ignore')
```

---

[Up: contents](index.md) · [Quick poll - Guess the category →](02-quick-poll---guess-the-category.md)
