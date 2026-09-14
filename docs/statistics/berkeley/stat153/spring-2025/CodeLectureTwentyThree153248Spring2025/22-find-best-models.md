---
title: Find best models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find best models

**Source:** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

best_aic_idx = results_df['AIC'].idxmin()
best_bic_idx = results_df['BIC'].idxmin()

best_aic_model = results_df.loc[best_aic_idx]
best_bic_model = results_df.loc[best_bic_idx]

---

[← Convert results to DataFrame](21-convert-results-to-dataframe.md) · [Up: contents](index.md) · [Display results →](23-display-results.md)
