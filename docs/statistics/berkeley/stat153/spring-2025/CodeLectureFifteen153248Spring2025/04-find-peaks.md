---
title: Find peaks
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFifteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureFifteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureFifteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFifteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks, _ = find_peaks(np.log(pgram_mean_lasso_c))
print(peaks/n)
```

```
[0.06270492 0.1079918  0.24518443]
```

The peak corresponds to the frequency $0.06270492$. To conver the frequency to Hertz, we multiply it by the sampling rate.

```python
(peaks[0]/n) * sampling_rate
```

```
10.032786885245901
```

So the differences between the two power spectra is mainly at frequency 10.0328 Hz. This is very close to the 10Hz Alpha rhythm which apparently exists when eyes are closed as opposed to eyes being open (see, for example, the first sentence in this paper "Occipital alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes" by Hohaia et al 2022)

---

[← Find peaks](03-find-peaks.md) · [Up: contents](index.md)
