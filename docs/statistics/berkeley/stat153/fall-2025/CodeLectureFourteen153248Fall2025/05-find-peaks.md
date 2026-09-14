---
title: Find peaks
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFourteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureFourteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks, _ = find_peaks(np.log(pgram_mean_lasso_c))
print(peaks/n)
```

```
[0.06270492 0.1079918  0.24518443]
```

The peak corresponds to the frequency $0.06270492$. To convert the frequency to Hertz, we multiply it by the sampling rate.

```python
(peaks[0]/n) * sampling_rate
```

```
10.032786885245901
```

So the differences between the two smoothed periodogram estimates is mainly at frequency 10.0328 Hz. This is very close to the 10Hz Alpha rhythm which apparently exists when eyes are closed as opposed to eyes being open (see, for example, the first sentence in this paper "Occipital alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes" by Hohaia et al 2022). The wiki page on the alpha wave (see https://en.wikipedia.org/wiki/Alpha_wave) says that alpha waves are neural oscillations in the frequency range 8-12 Hz. We can see from the plot above that at 8 - 12 Hz, the estimated spectrum for the closed eyes data is higher than the spectrm for open eyes data.

```python
#Estimated power spectra
plt.plot(freqs, np.log(pgram_mean_lasso_o), color = 'black', label = 'Open')
plt.plot(freqs, np.log(pgram_mean_lasso_c), color = 'red', label = 'Closed')
plt.axvline(x = 10/sampling_rate)
plt.axvline(x = 8/sampling_rate)
plt.axvline(x = 12/sampling_rate)
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← ----- Right subplot: Eyes Closed -----](04-------right-subplot-eyes-closed.md) · [Up: contents](index.md)
