---
title: A.1. Proof of theorem 1
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A.1. Proof of theorem 1

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The key idea is to establish the relationship


where A. _β_ 0/ is given in theorem 1 and


where F _β_ .s, y/ = E[X.s/ _g{_ X.s + y/<sup>T</sup> _β}_ ]. To obtain result (13), first, using _P_ n and _P_ to denote the empirical measure and true probability measure respectively, we obtain


For the second term on the right-hand side of equation (14), we have


770 _H. Cao, D. Zeng and J. P. Fine_


Recall that F _β_ 0 .s, hz/ = E[X.s/ _g{_ X.s + hz/<sup>T</sup> _β_ 0 _}_ ]. Using condition 3 and after the Taylor series expansion of F _β_ 0 .s, hz/, since � zK.z/ dz = 0 and � K.z/ dz = 1, we obtain


We then extract the main terms


Moreover, if _γ_<sup>T</sup> A. _β_ 0/ _γ_ = 0, then _γ_<sup>T</sup> X.s/ = 0 almost surely for s ∈ _G_ , so _γ_ = 0 from condition 2. Thus, A. _β_ 0/ is a positive definite matrix, and thus non-singular. For the first term on the right-hand side of equation (14), we consider the class of functions


for a given constant ". Note that the functions in this class are Lipschitz continuous in _β_ and the Lipschitz constant is uniformly bounded by


Since, by condition 3,


we have


for some constant M2. Conditionally on N. _τ_ , _τ_ /, E _{_ �� hKh.t − s/<sup>2</sup> dN.t, s/| N. _τ_ , _τ_ / _}_ can be easily verified to be finite. Therefore, E.M1<sup>2/isfinite.Therefore,thisclassisa</sup><sup>_P_-DonskerclassbytheJain–Marcus</sup> theorem (van der Vaart and Wellner, 1996). As the result, we obtain that the first term on the right-hand side of equation (14) for | _β_ − _β_ 0| <M.nh/<sup>−1=2</sup> is equal to


Combining equations (15) and (17) and by condition 4, we obtain result (13).

Consequently,

.nh/<sup>1=2</sup> A. _β_ 0/. _β_<sup>ˆ</sup> − _β_ 0/ + Cn<sup>1=2</sup> h<sup>5=2</sup> + op.n<sup>1=2</sup> h<sup>5=2</sup> / + op _{_ 1 + .nh/<sup>1=2</sup> | _β_<sup>ˆ</sup> − _β_ 0| _}_ = .nh/<sup>1=2</sup> [Un. _β_ 0/ − E _{_ Un. _β_ 0/ _}_ ]: .18/

_Analysis of Asynchronous Data_ 771

In contrast, following a similar argument to that before, we can calculate


as follows:

Using conditioning arguments, we obtain


After a change of variables and incorporating conditions 3 and 4, the first three terms in term I are all of order O.h/ and the last term equals


So we have


Similarly, it can be shown that


772 _H. Cao, D. Zeng and J. P. Fine_

and I3 − I4 = O.h<sup>2</sup> /. Therefore, we have


Similarly to the calculation of Σ,


Therefore,


Combining with equation (18), we finish the proof of theorem 1.

---

[← Appendix A](14-appendix-a.md) · [Up: contents](index.md) · [A.2. Proof of corollary 2 →](16-a-2-proof-of-corollary-2.md)
