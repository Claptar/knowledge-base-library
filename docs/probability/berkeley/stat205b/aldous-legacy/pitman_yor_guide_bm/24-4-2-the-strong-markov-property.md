---
title: 4.2. The strong Markov property
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.2. The strong Markov property

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If _B_ is an ( _Ft_ ) Brownian motion then for each fixed time _T_ the process


is a Brownian motion independent of _FT_ . According to the _strong Markov property_ of Brownian motion, this is true also for all ( _Ft_ ) _stopping times T_ , that is random times _T_ : Ω _→_ R+ _∪{∞}_ such that ( _T ≤ t_ ) _∈Ft_ for all _t ≥_ 0. The sigma-field _FT_ of events determined by time _T_ is defined as:


and the process (27) is considered only conditionally on the event _T < ∞_ . See [106], [43] for the proof and numerous applications. More generally, a Markov process _X_ with filtration ( _Ft_ ) is said to have the strong Markov property if for

_J. Pitman and M. Yor/Guide to Brownian motion_

15

all ( _Ft_ ) stopping times _T_ , conditionally given _FT_ on ( _T < ∞_ ) with _XT_ = _x_ the process ( _XT_ + _s, s ≥_ 0) is distributed like ( _Xs, s ≥_ 0) given _X_ 0 = _x_ . It is known [372, Th. III (9.4)] that the strong Markov property holds for L´evy processes, and more generally for the class of _Feller-Dynkin processes X_ defined by the following regularity conditions: the state space _E_ is locally compact with countable base, _E_ is the Borel sigma field on _E_ , and the transition probability operators _Pt_ act in a strongly continuous way on the Banach space _C_ 0( _E_ ) of bounded continuous functions on _E_ which vanish at infinity [201, Ch. 19], [370, III.2], [372, Def. (6.5)].

---

[← 4.1. Markov processes and their semigroups](23-4-1-markov-processes-and-their-semigroups.md) · [Up: contents](index.md) · [4.3. Generators →](25-4-3-generators.md)
