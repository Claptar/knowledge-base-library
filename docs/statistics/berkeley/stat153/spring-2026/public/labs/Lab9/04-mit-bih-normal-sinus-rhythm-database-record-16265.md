---
title: MIT-BIH Normal Sinus Rhythm Database, record 16265
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# MIT-BIH Normal Sinus Rhythm Database, record 16265

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

record = wfdb.rdrecord('16265', pn_dir='nsrdb/', channels=[0],
                       sampfrom=0, sampto=128*600)  # ~10 min at 128 Hz
ecg = record.p_signal[:, 0]

---

[← Heart Rate Variability - RR intervals](03-heart-rate-variability---rr-intervals.md) · [Up: contents](index.md) · [First we will plot the original ECG waveform. We will use this to measure →](05-first-we-will-plot-the-original-ecg-waveform-we-will-use-thi.md)
