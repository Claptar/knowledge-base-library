---
title: 5 AR( p ) for p ≥ 1
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 AR( p ) for p ≥ 1

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now consider the AR(p) difference equationl In backshift notation, this is


We shall call _φ_ ( _z_ ) := 1 _− φ_ 1 _z − φ_ 2 _z_<sup>2</sup> _−· · · − φpz_<sup>_p_</sup> the AR polynomial.

We “solve” the AR( _p_ ) by writing:


The next step is to make sense of 1 _/_ (1 _− φ_ 1 _B −· · · − φpB_<sup>_p_</sup> ). It is natural here to factorize the polynomial 1 _− φ_ 1 _B −· · · − φpB_<sup>_p_</sup> into monomials, and then use (9). So we write


so that


The numbers _a_ 1 _, . . . , ap_ appearing in (10) are simply the reciprocals of the roots of _φ_ ( _z_ ) i.e., the roots of _φ_ ( _z_ ) are given by 1 _/a_ 1 _, . . . ,_ 1 _/ap_ . Note here that some of the _aj_ ’s can be complex because the polynomial 1 _− φ_ 1 _z −· · · − φpz_<sup>_p_</sup> can have complex roots (even though all its coefficients are real).

We then get


For each 1 _/_ (1 _− ajB_ ), we use the formula (9) to get:

Multiplying out the product<sup>�</sup><sup>_p_</sup> _k_ =1 �� _j∞_ =0<sup>_aj_</sup> _k_<sup>_Bj_�</sup> , we get

7

The above expression involves powers of _a_ 1 _, . . . , ap_ . For these powers to not explode, we need


Note that _ai_ can be complex so _|ai|_ represents the modulus of _aj_ . When _|ai| <_ 1, the powers _|ai|_<sup>_j_</sup> decay rapidly in _j_ which makes the infinite sums above well-defined.

The formula above writes _yt_ in terms of _ϵt, ϵt−_ 1 _, . . ._ . By collecting terms where _j_ 1+ _· · ·_ + _jp_ = _j_ for each _j_ = 0 _,_ 1 _, . . ._ , we can write this solution as


for some _µ, ψ_ 1 _, ψ_ 2 _, . . ._ . It can be checked that this is a stationary time series (note it is also causal as _yt_ only depends on _ϵt, ϵt−_ 1 _, . . ._ ).

The key condition here is (13). This is the analogue of the AR(1) condition _|φ_ 1 _| <_ 1 for AR( _p_ ) when _p ≥_ 1. Because the roots of the AR polynomial _φ_ ( _z_ ) = 1 _− φ_ 1 _z −· · · − φpz_<sup>_p_</sup> are 1 _/a_ 1 _, . . . ,_ 1 _/ap_ , the condition (13) is equivalent to assuming that all roots of the AR polynomial are strictly larger than 1 in modulus.

This analysis can be made rigorous to show the following:

1. When all roots of the AR polynomial are strictly larger than 1 in modulus, then there exists a unique causal stationary process _{yt}_ which satisfies the AR( _p_ ) equation: _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _· · ·_ + _φpyt−p_ + _ϵt_ . This causal stationary solution is of the form (14) where the coefficients _ψ_ 1 _, ψ_ 2 _, . . ._ are derived from (12).

2. When even one root of the AR polynomial has modulus _≤_ 1, then there cannot exist a causal stationary solution to the AR equation.

3. `AutoReg` fits the model

_y_ 1 = fixed at observed value and _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _· · ·_ + _φpyt−p_ + _ϵt_

i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). When the condition (13) is true, this model has similar behavior to (14) in the same way as the similarity between (3) and (7) for _p_ = 1.

For assessing causal-stationarity of the fitted model, the output summary of `AutoReg` gives the values of the moduli of the roots of the fitted AR polynomial.

---

[← 4 Causal Stationary AR (1) formula using Backshift](05-4-causal-stationary-ar-1-formula-using-backshift.md) · [Up: contents](index.md) · [6 Determination of the order p of AR( p ) →](07-6-determination-of-the-order-p-of-ar-p.md)
