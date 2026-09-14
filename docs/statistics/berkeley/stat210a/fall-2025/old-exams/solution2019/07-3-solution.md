---
title: 3. Solution.
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/solution2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Solution.

**Source:** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) ( **Common mistake:** In applying the factorization theorem we need to treat _n_ as an unknown parameter: _n_ ! _/_ ( _n − N_ 11 _− N_ 10 _− N_ 01)! is not just a function of the data.)

There are four possible outcomes for each reindeer, labeled 00 (undetected twice), 01 (undetected then detected), 10 (detected then undetected), and 11 (detected twice), which occur respectively with probability _p_ 00 = (1 _− π_ )<sup>2</sup> , _p_ 01 = _p_ 10 = _π_ (1 _− π_ ), and _p_ 11 = _π_<sup>2</sup> . The counts _N_ 00 _, N_ 01 _, N_ 10 _, N_ 11 record how many times each outcome happens, so

( _N_ 00 _, N_ 01 _, N_ 10 _, N_ 11) _∼_ Multinom( _n,_ ((1 _− π_ )<sup>2</sup> _, π_ (1 _− π_ ) _, π_ (1 _− π_ ) _, π_<sup>2</sup> ))


where the first two factors are functions of _T_ = ( _N_ 11 _, N_ 01 + _N_ 10) and the parameters ( _n, π_ ) but the last factor is only a function of the data. By the factorization theorem, then, _T_ is sufficient.

- (b) If _T_ can be computed from the collection of all likelihood ratios (and if it is also sufficient, as we have just shown it is), then it is minimal sufficient. The likelihood ratio between ( _n, π_ ) and (˜ _n,_ ˜ _π_ ) is


By taking _n_ = _n_ ˜ = _N_ 11 _− N_ 10 _− N_ 01 and varying _π/π_ ˜, we can learn 2 _N_ 11 + _N_ 10 + _N_ 01; whereas by taking _π_ = _π_ ˜ = 0 _._ 5 and varying _n_ and _n_ ˜, we can learn _N_ 11 + _N_ 11 + _N_ 10 + _N_ 01; knowing both of these is equivalent to knowing _T_ .

- (c) Note that _Nij/n → pij_ by LLN, since it is an average of _n_ i.i.d. Bern( _pij_ ) random variables which have finite expectation. Dividing by _n_<sup>2</sup> in the numerator and _n_ in the denominator and applying the continuous map-

11

ping theorem, we get


- (d) By grouping together the outcomes 01 and 10 we can get a reduced multinomial


which is also a sum of _n_ i.i.d. Multinom(1 _,_ ( _p_ 00 _,_ 2 _p_ 01 _, p_ 11)) random variables which have finite variance. Restricting attention to the two entries we actually observe and then applying the CLT gives


where


We will apply delta method to the function _f_ ( _t_ 1 _, t_ 2) = ( _t_ 1 + 2 _t_ 2)<sup>2</sup> _/_ 4 _t_ 2:


Applying the delta method to _f_ � _<u>N</u>_ <u>10+</u> _nN_ <u>01</u> _,_<sup>_<u>N</u>_</sup> _n_<sup><u>11</u></sup> � gives


where _σ_<sup>2</sup> = _∇f_ (2 _p_ 10 _, p_ 11)<sup>_′_</sup> Σ _∇f_ (2 _p_ 10 _, p_ 11). After a lot of algebra we can simplify _σ_<sup>2</sup> = (1 _− π_ )<sup>2</sup> _/π_<sup>2</sup> , but we would award full credit for the unsimplified form as described above.

12

---

[← 2. Solution.](06-2-solution.md) · [Up: contents](index.md) · [4. Nonlinear regression (24 points, 6 points / part). →](08-4-nonlinear-regression-24-points-6-points-part.md)
