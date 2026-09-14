---
title: 3 Backshift Notation
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Backshift Notation

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A convenient piece of notation used while working with AR and MA models is the Backshift notation. Let _B_ denote the _backshift operator_ defined by


and similarly


Also let _I_ denote the identity operator: _Iyt_ = _yt_ . More generally, we can define polynomial functions of the Backshift operator by, for example,


In general, for every polynomial _f_ ( _z_ ), we can define _f_ ( _B_ ). One can even extend this notation to negative powers of _B_ which correspond to forward shifts. For example, _B_<sup>_−_1</sup> _yt_ = _yt_ +1 _, B_<sup>_−_5</sup> _yt_ = _yt_ +5 and ( _B_<sup>3</sup> + 9 _B_<sup>_−_2</sup> ) _yt_ = _yt−_ 3 + 9 _yt_ +2 etc.

In this notation, the defining equation _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _φ_ 2 _yt−_ 2 + _· · ·_ + _φpyt−p_ + _ϵt_ for the _AR_ ( _p_ ) model can be written as _φ_ ( _B_ ) _yt_ = _φ_ 0 + _ϵt_ for the polynomial _φ_ ( _z_ ) = 1 _− φ_ 1 _z − φ_ 2 _z_<sup>2</sup> _−· · · − φpz_<sup>_p_</sup> .

The defining equation _yt_ = _ϵt_ + _θϵt−_ 1 for the MA(1) model can be written as _yt_ = _θ_ ( _B_ ) _ϵt_ for the polynomial _θ_ ( _z_ ) = 1 + _θ_ 1 _z_ .

The defining equation _yt_ = _ϵt_ + _θ_ 1 _ϵt−_ 1 + _· · ·_ + _θqϵt−q_ for the MA( _q_ ) model becomes _yt_ = _θ_ ( _B_ ) _ϵt_ for the polynomial _θ_ ( _z_ ) = 1 + _θ_ 1 _z_ + _. . . θqz_<sup>_q_</sup> .

---

[← 2 Stationarity of AR(1)](03-2-stationarity-of-ar-1.md) · [Up: contents](index.md) · [4 Causal Stationary AR (1) formula using Backshift →](05-4-causal-stationary-ar-1-formula-using-backshift.md)
