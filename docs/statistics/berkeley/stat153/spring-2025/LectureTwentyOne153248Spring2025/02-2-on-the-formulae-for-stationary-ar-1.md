---
title: 2 On the formulae for stationary AR(1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 On the formulae for stationary AR(1)

**Source:** [`LectureTwentyOne153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Above, we first wrote down the formulae (3) and (4) for stationary AR(1) and then verified that they indeed satisfy the AR(1) equation. It turns that these formulae can be derived by “solving” the AR(1) equation (1) for _yt_ in terms of _{ϵt}_ . We shall present this solution method here. We will not present a rigorous justification for this method (which can be found, for example, in the book “Time Series: theory and methods” by Brockwell and Davis).

Before describing this solution method, we need to introduce the backshift notation.

### **2.1 Backshift Notation**

A convenient piece of notation used while working with AR and MA models is the Backshift notation. Let _B_ denote the _backshift operator_ defined by

_Byt_ = _yt−_ 1 _, B_<sup>2</sup> _yt_ = _yt−_ 2 _, B_<sup>3</sup> _yt_ = _yt−_ 3 _, . . ._

3

and similarly

_Bϵt_ = _ϵt−_ 1 _, B_<sup>2</sup> _ϵt_ = _ϵt−_ 2 _, B_<sup>3</sup> _ϵt_ = _ϵt−_ 3 _, . . . ._

Also let _I_ denote the identity operator: _Iyt_ = _yt_ . More generally, we can define polynomial functions of the Backshift operator by, for example,

( _I_ + _B_ + 3 _B_<sup>2</sup> ) _yt_ = _Iyt_ + _Byt_ + 3 _B_<sup>2</sup> _yt_ = _yt_ + _yt−_ 1 + 3 _yt−_ 2 _._

In general, for every polynomial _f_ ( _z_ ), we can define _f_ ( _B_ ). One can even extend this notation to negative powers of _B_ which correspond to forward shifts. For example, _B_<sup>_−_1</sup> _yt_ = _yt_ +1 _, B_<sup>_−_5</sup> _yt_ = _yt_ +5 and ( _B_<sup>3</sup> + 9 _B_<sup>_−_2</sup> ) _yt_ = _yt−_ 3 + 9 _yt_ +2 etc.

In this notation, the defining equation _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _φ_ 2 _yt−_ 2 + _· · ·_ + _φpyt−p_ + _ϵt_ for the _AR_ ( _p_ ) model can be written as _φ_ ( _B_ ) _yt_ = _φ_ 0 + _ϵt_ for the polynomial _φ_ ( _z_ ) = 1 _− φ_ 1 _z − φ_ 2 _z_<sup>2</sup> _−· · · − φpz_<sup>_p_</sup> .

The defining equation _yt_ = _ϵt_ + _θϵt−_ 1 for the MA(1) model can be written as _yt_ = _θ_ ( _B_ ) _ϵt_ for the polynomial _θ_ ( _z_ ) = 1 + _θ_ 1 _z_ .

The defining equation _yt_ = _ϵt_ + _θ_ 1 _ϵt−_ 1 + _· · ·_ + _θqϵt−q_ for the MA( _q_ ) model becomes _yt_ = _θ_ ( _B_ ) _ϵt_ for the polynomial _θ_ ( _z_ ) = 1 + _θ_ 1 _z_ + _. . . θqz_<sup>_q_</sup> .

### **2.2** _AR_ (1) **solutions using Backshift Calculus**

The two stationary solutions (3) and (4) to the AR(1) difference equation (1) for the two cases _|φ_ 1 _| <_ 1 and _|φ_ 1 _| >_ 1 can also be derived using formal operations that are sometimes known as Backshift Calculus. This is described in this section. First note that (1) can be written as


Thus we can formally write


Using

we obtain


which gives (3).

When _|φ_ 1 _| >_ 1, the process (3) does not make sense. So we expand 1 _/φ_ ( _z_ ) in the following alternative way:


4

We thus get


which gives (4). This formal method is called Backshift Calculus and it works for higher order AR models as well.

---

[← 1 Stationarity of AR(1)](01-1-stationarity-of-ar-1.md) · [Up: contents](index.md) · [3 Stationary and Causality for AR( p ), p ≥ 2 →](03-3-stationary-and-causality-for-ar-p-p-2.md)
