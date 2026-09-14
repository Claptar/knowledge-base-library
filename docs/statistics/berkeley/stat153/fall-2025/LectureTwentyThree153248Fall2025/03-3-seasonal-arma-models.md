---
title: 3 Seasonal ARMA Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Seasonal ARMA Models

**Source:** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Seasonal ARMA models are often useful while modeling datasets having seasonal features (e.g., monthly datasets). We say that _{yt}_ is a seasonal ARMA( _P_ , _Q_ ) process with period _s_ if it satisfies the difference equation Φ( _B_<sup>_s_</sup> )( _yt − µ_ ) = Θ( _B_<sup>_s_</sup> ) _ϵt_ where _ϵt_ i.i.d _∼ N_ (0 _, σ_<sup>2</sup> ) and


The seasonal ARMA( _P_ , _Q_ ) model with period _s_ is a special case of an ARMA( _Ps_ , _Qs_ ) model. However the seasonal model has _P_ + _Q_ + 1 (the 1 is for _σ_<sup>2</sup> ) parameters while a general ARMA( _Ps_ , _Qs_ ) model will have _Ps_ + _Qs_ + 1 parameters. So the seasonal models are much sparser.

Causal stationary solution exists when every root of Φ( _z_<sup>_s_</sup> ) (equivalently, Φ( _z_ )) has modulus strictly larger than one.

The ACF and PACF of seasonal ARMA models are **non-zero** only at the seasonal lags _h_ = 0 _, s,_ 2 _s,_ 3 _s, . . ._ . At these seasonal lags, the ACF and PACF of these models behave just as the case of the unseasonal ARMA model: Φ( _B_ ) _Xt_ = Θ( _B_ ) _ϵt_ .

---

[← 2 ARIMA models](02-2-arima-models.md) · [Up: contents](index.md) · [4 Multiplicative Seasonal ARMA Models →](04-4-multiplicative-seasonal-arma-models.md)
