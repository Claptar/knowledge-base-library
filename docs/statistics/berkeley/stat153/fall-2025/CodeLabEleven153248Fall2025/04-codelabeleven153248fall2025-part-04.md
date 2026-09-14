---
title: CodeLabEleven153248Fall2025 Part 04 —
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLabEleven153248Fall2025 Part 04 —

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
MLE estimates from custom optimization:
[[1.5434168  1.5415492  1.54154255]
 [0.24870755 0.24797155 0.24797565]
 [1.55971966 1.55508381 1.55511122]]
-513.2625963846933 -513.2616222294719 -513.2616221995303
```

Another difference between AutoReg and ARIMA is that ARIMA only searches for parameters in the causal stationary region but AutoReg does not place any such restrictions.

```python

---

[← note that the bound on phi1 ensures stationarity](03-note-that-the-bound-on-phi1-ensures-stationarity.md) · [Up: contents](index.md) · [Below we fit these models to the original data without any differencing or logging. →](05-below-we-fit-these-models-to-the-original-data-without-any-d.md)
