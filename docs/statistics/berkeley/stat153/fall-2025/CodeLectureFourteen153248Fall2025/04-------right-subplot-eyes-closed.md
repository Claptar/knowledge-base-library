---
title: '----- Right subplot: Eyes Closed -----'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFourteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ----- Right subplot: Eyes Closed -----

**Source:** [`CodeLectureFourteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

axes[1].plot(freqs, np.log(pgram_c), color='lightblue', label='Periodogram')
axes[1].plot(freqs, np.log(pgram_mean_ridge_c), color='red', label='Ridge')
axes[1].plot(freqs, np.log(pgram_mean_lasso_c), color='black', label='LASSO')
axes[1].set_title('Log Periodogram (Eyes Closed)')
axes[1].set_xlabel('Frequency')
axes[1].legend()

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we plot the estimated $2 \gamma_j^2/n$ (on the log-scale). These should be viewed as smoothed versions of the respective periodograms.

```python
plt.plot(freqs, np.log(pgram_mean_ridge_o), color = 'black', label = 'Open')
plt.plot(freqs, np.log(pgram_mean_ridge_c), color = 'red', label = 'Closed')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

plt.plot(freqs, np.log(pgram_mean_lasso_o), color = 'black', label = 'Open')
plt.plot(freqs, np.log(pgram_mean_lasso_c), color = 'red', label = 'Closed')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The peak in the 'eyes closed' curve above can be computed as follows.

```python
from scipy.signal import find_peaks

---

[← ----- Left subplot: Eyes Open -----](03-------left-subplot-eyes-open.md) · [Up: contents](index.md) · [Find peaks →](05-find-peaks.md)
