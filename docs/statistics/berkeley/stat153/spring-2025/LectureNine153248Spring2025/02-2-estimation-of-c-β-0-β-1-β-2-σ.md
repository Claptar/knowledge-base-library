---
title: 2 Estimation of c, β 0 , β 1 , β 2 , σ
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Estimation of c, β 0 , β 1 , β 2 , σ

**Source:** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Parameter estimation can be done via Maximum Likelihood Estimation. Just as in the case of the sinusoidal model, a crucial role is played by the residual sum of squares in the linear regression model (2):


The MLE of _c_ is given by the minimizer of _RSS_ ( _c_ ) over _c_ . On the computer, we calculate this by enumerating all the possible values of _c_ (these are just 1 _,_ 2 _, . . . , n_ ) and then using a function such as `np.argmin` .

After the MLE ˆ _c_ of _c_ is obtained, _β_ 0 _, β_ 1 _, β_ 2 are estimated as in linear regression (e.g., using `sm.OLS` ). Specifically,


Then _σ_ is estimated as in linear regression:

---

[← 1 Change of Slope Model](01-1-change-of-slope-model.md) · [Up: contents](index.md) · [3 Uncertainty Quantification for c, β 0 , β 1 , β 2 , σ →](03-3-uncertainty-quantification-for-c-β-0-β-1-β-2-σ.md)
