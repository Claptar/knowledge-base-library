---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEight153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureEight153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureEight153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEight153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Uses of the Periodogram
---

The periodogram has the following uses:

1. If we want to use the single sinusoidal model: $y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t$, the periodogram gives a computationally efficient method to calculate $RSS(f)$ at Fourier frequencies $f$. This is very useful when the sample size $n$ is large.
2. The periodogram is an exploratory tool that can suggest useful models to fit to the data.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import librosa
```

An example for the first application is the following (we already saw this application in Lecture 6). Here the dataset represents the sound waveform for an audio file.

---

[Up: contents](index.md) · [Audio Data →](02-audio-data.md)
