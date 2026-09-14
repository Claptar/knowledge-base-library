---
title: extend data by k placeholder values
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# extend data by k placeholder values

**Source:** [`CodeLabNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

phi_vals = armod_sm.params
for i in range(1, k+1):
    ans = phi_vals.iloc[0]
    for j in range(1, p+1):
        ans += phi_vals.iloc[j] * yhat[n_train+i-j-1]
    yhat[n_train+i-1] = ans
predvalues = yhat[n_train:]

---

[← the default choice is trend = 'c' so we can just drop it if we want](07-the-default-choice-is-trend-c-so-we-can-just-drop-it-if-we-w.md) · [Up: contents](index.md) · [Check that both predictions are identical →](09-check-that-both-predictions-are-identical.md)
