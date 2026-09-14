---
title: Predictions
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Predictions

**Source:** [`Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

yhat = np.concatenate([y_train.astype(float), np.full(k, -9999)]) # extend data by k placeholder values
phi_vals = armod_sm.params
for i in range(1, k + 1):
    ans = phi_vals.iloc[0]
    for j in range(1, p + 1):
        ans += phi_vals.iloc[j] * yhat[n_train + i - j - 1]
    yhat[n_train + i - 1] = ans
predvalues = yhat[n_train: ]

---

[← the default choice is trend = 'c' so we can just drop it if we want](05-the-default-choice-is-trend-c-so-we-can-just-drop-it-if-we-w.md) · [Up: contents](index.md) · [Check that both predictions are identical →](07-check-that-both-predictions-are-identical.md)
