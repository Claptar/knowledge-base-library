---
title: 2 Predictions from AR ( p ) models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Predictions from AR ( p ) models

**Source:** [`LectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If the parameters _ϕ_ 0 _, . . . , ϕp_ and _σ_ (collectively denoted by _θ_ ) of the AR(p) model are fixed, then the prediction for a future value _yn_ + _i_ is given by


These values are calculated recursively for _i_ = 1 _,_ 2 _, . . ._ using the following recursion:


which is initialized by


Since _θ_ is unknown, we can replace it by the conditional MLE _θ_<sup>ˆ</sup> .

3

---

[← 1 AR models: estimation, inference and prediction](01-1-ar-models-estimation-inference-and-prediction.md) · [Up: contents](index.md) · [3 Prediction Standard Errors →](03-3-prediction-standard-errors.md)
