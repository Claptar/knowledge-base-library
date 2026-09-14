---
title: 4 Seasonal ARMA Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Seasonal ARMA Models

**Source:** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Seasonal ARMA models are often useful while modeling datasets having seasonal features (e.g., monthly datasets). We say that _{yt}_ is a seasonal ARMA( _P_ , _Q_ ) process with period _s_ if it satisfies the difference equation Φ( _B_<sup>_s_</sup> )( _yt − µ_ ) = Θ( _B_<sup>_s_</sup> ) _ϵt_ where _ϵt_ i.i.d _∼ N_ (0 _, σ_<sup>2</sup> ) and


and Θ( _B_<sup>_s_</sup> ) = 1 + Θ1 _B_<sup>2</sup> + Θ2 _B_<sup>2</sup><sup>_s_</sup> + _· · ·_ + Θ _QB_<sup>_Qs_</sup> _._

The seasonal ARMA( _P_ , _Q_ ) model with period _s_ is a special case of an ARMA( _Ps_ , _Qs_ ) model. However the seasonal model has _P_ + _Q_ + 1 (the 1 is for _σ_<sup>2</sup> ) parameters while a general ARMA( _Ps_ , _Qs_ ) model will have _Ps_ + _Qs_ + 1 parameters. So the seasonal models are much sparser.

Causal stationary solution exists when every root of Φ( _z_<sup>_s_</sup> ) (equivalently, Φ( _z_ )) has modulus strictly larger than one.

The ACF and PACF of seasonal ARMA models are **non-zero** only at the seasonal lags _h_ = 0 _, s,_ 2 _s,_ 3 _s, . . ._ . At these seasonal lags, the ACF and PACF of these models behave just as the case of the unseasonal ARMA model: Φ( _B_ ) _Xt_ = Θ( _B_ ) _ϵt_ .

---

[← 3 ARIMA models](03-3-arima-models.md) · [Up: contents](index.md) · [5 Multiplicative Seasonal ARMA Models →](05-5-multiplicative-seasonal-arma-models.md)
