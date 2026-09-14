---
title: 1 Parameter Estimation in AutoRegressive Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Parameter Estimation in AutoRegressive Models

**Source:** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall discuss parameter estimation in _AR_ ( _p_ ) models. Recall that the _AR_ ( _p_ ) is given by:


for _t_ = _p_ + 1 _, . . . , n_ . In matrix notation,


where


The _AR_ ( _p_ ) can be seen as a spcial of the usual linear regression model where the covariate matrix _X_ as well as the response vector _y_ are both formed from a single data set _y_ 1 _, . . . , yn_ .

We shall discuss estimation of the parameters _ϕ_ 0 _, . . . , ϕp_ and _σ_ in _AR_ ( _p_ ). For simplicity, let us first assume _p_ = 1 (we shall revert to the more general case later). The AR(1) model is given by:


Because of the close relation between _AR_ ( _p_ ) models and linear regression, let us first revisit parameter estimation in usual linear regression.

---

[Up: contents](index.md) · [2 Detour: usual linear regression →](02-2-detour-usual-linear-regression.md)
