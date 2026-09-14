---
title: Lemma 5.1.
source: https://www.stat.berkeley.edu/~aldous/205B/511.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/511.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lemma 5.1.

**Source:** [`511.pdf`](https://www.stat.berkeley.edu/~aldous/205B/511.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(i) _X is a Borel subset of X ._

(ii) _f → Kf is a Borel function on X ._ (iii) ( _f, s_ ) _→ f_ ( _s_ ) _is a Borel map from X × S to S._

Proof: For _f ∈ X_ , let


Plainly, _f → Lf_ is a Borel function on _X_ . If _Lf < ∞_ then _f_ can be extended as a Lipschitz function to all of _S_ with _Kf_ = _Lf_ . Conversely, if _f_ is Lipschitz on _S_ , its retraction to _S_ 0 has _Lf_ = _Kf_ . Thus, the Lipschitz functions _f_ on _S_ can be identified as the functions _f_ on _S_ 0 with _Lf < ∞_ , and _Kf_ = _Lf_ . This proves (i) and (ii).

For (iii), enumerate _S_ 0 as _{s_ 1 _, s_ 2 _, . . . }_ . Fix a positive integer _n_ . Let _Bn,_ 1 be the set of points that are within 1 _/n_ of _s_ 1. Let _Bn,j_ +1 be the set of points that are within 1 _/n_ of _sj_ +1, but at a distance of 1 _/n_ or more from _s_ 1 _, . . . , sj_ . (In other words, take the balls of radius 1 _/n_ around the _sj_ and make them disjoint.) For each _n_ , the _Bn,j_ are pairwise disjoint and


Given a mapping _f_ of _S_ into itself, let _fn_ ( _s_ ) = _f_ ( _sj_ ) for _s ∈ Bn,j_ . That is, _fn_ approximates _f_ by _f_ ( _sj_ ) in the vicinity of _sj_ . The map ( _f, s_ ) _→ fn_ ( _s_ ) is Borel from _X × S_ to _S_ . And on the set of Lipschitz _f_ , this sequence of maps converges pointwise to the evaluation map. Q.E.D.

**Remark.** To make the connection with the setup of Section 1, if _{fθ}_ is a family of Lipschitz functions indexed by _θ ∈_ Θ, we require that the map _θ → fθ_ ( _x_ ) be

16 PERSI DIACONIS AND DAVID FREEDMAN

measurable for each _x ∈ S_ 0. Then _θ → fθ_ is a measurable map from Θ to _X_ , and a measure on Θ induces a measure on _X_ . This section works directly with measures on _X_ .

The metric _ρ_ induces a “Prokhorov metric” on probabilities, also denoted by _ρ_ , as follows.

**Definition 5.1.** If _P_ , _Q_ are probabilities on _S_ , then _ρ_ ( _P, Q_ ) is the infimum of the _δ >_ 0 such that

_P_ ( _C_ ) _< Q_ ( _Cδ_ ) + _δ_ and _Q_ ( _C_ ) _< P_ ( _Cδ_ ) + _δ_

for all compact _C ⊂ S_ , where _Cδ_ is the set of all points whose distance from _C_ is less than _δ_ .

---

[← ITERATED RANDOM FUNCTIONS](02-iterated-random-functions.md) · [Up: contents](index.md) · [Remarks. →](04-remarks.md)
