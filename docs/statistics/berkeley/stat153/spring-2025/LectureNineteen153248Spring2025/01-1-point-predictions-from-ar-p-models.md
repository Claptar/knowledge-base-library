---
title: 1 Point Predictions from AR ( p ) models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNineteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNineteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Point Predictions from AR ( p ) models

**Source:** [`LectureNineteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNineteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If the parameters _φ_ 0 _, . . . , φp_ and _σ_ (collectively denoted by _θ_ ) of the AR(p) model are fixed, then the prediction for a future value _yn_ + _i_ is given by


These values are calculated recursively for _i_ = 1 _,_ 2 _, . . ._ using the following recursion:


which is initialized by


Since _θ_ is unknown, we can replace it by the conditional MLE _θ_<sup>ˆ</sup> . Alternatively, one can try to compute:


numerically using posterior samples of _θ_ . This method is complicated and the common procedure is simply to replace _θ_ by the conditional MLE _θ_<sup>ˆ</sup> .

---

[Up: contents](index.md) · [2 Prediction Standard Errors →](02-2-prediction-standard-errors.md)
