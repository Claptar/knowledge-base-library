---
title: '----- Left subplot: Eyes Open -----'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFourteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ----- Left subplot: Eyes Open -----

**Source:** [`CodeLectureFourteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

axes[0].plot(freqs, np.log(pgram_o), color='lightblue', label='Periodogram')
axes[0].plot(freqs, np.log(pgram_mean_ridge_o), color='red', label='Ridge')
axes[0].plot(freqs, np.log(pgram_mean_lasso_o), color='black', label='LASSO')
axes[0].set_title('Log Periodogram (Eyes Open)')
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Log of 2 \gamma_j^2/n')
axes[0].legend()

---

[← Download S&P 500 data](02-download-s-p-500-data.md) · [Up: contents](index.md) · [----- Right subplot: Eyes Closed ----- →](04-------right-subplot-eyes-closed.md)
