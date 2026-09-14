---
title: Fin f09 sol solutions Part 03 —
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/fin-f09-sol-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fin f09 sol solutions Part 03 —

**Source:** `solutions/fin-f09-sol-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

�C���� 9��� {�������� � C��� �����

The only unknown quantity is cov( _X, N_ ) = **E** [ _XN_ ] _−_ **E** [ _X_ ] **E** [ _N_ ] = **E** [ _XN_ ] _−_ ( **E** [ _X_ ])<sup>2</sup> . Using the law of iterated expectations again,


Thus, cov( _X, N_ ) = 6 _/λ_<sup>2</sup> _−_ 4 _/λ_<sup>2</sup> = 2 _/λ_<sup>2</sup> _._ Combining this result with those from (a),


## (d) (5 points)

The expression for _X_<sup>ˆ</sup> MAP( _N_ ), the MAP estimator of _X_ based on an observation of _N_ is


where the third equality holds since _pN_ ( _n_ ) has no dependency on _x_ and the last equality holds by removing all quantities that have no dependency on _x_ . The max can be found by differentiation and the result is:


This is the only local extremum in the range _x ∈_ [0 _, ∞_ ). Moreover, _fX|N_ ( _x | n_ ) equals 0 at _x_ = 0 and goes to 0 as _x →∞_ and _fX|N_ ( _x | n_ ) _>_ 0 otherwise. We can therefore conclude that _X_<sup>ˆ</sup> MAP( _N_ ) is indeed a maximum.

## (e) (5 points)

To minimize the probability of error, we choose the hypothesis that has the larger posterior

5

---

[← Fin f09 sol solutions Part 02 —](02-fin-f09-sol-solutions-part-02.md) · [Up: contents](index.md) · [Fin f09 sol solutions Part 04 — →](04-fin-f09-sol-solutions-part-04.md)
