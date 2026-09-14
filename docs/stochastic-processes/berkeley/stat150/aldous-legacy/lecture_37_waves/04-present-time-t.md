---
title: present time T
source: https://www.stat.berkeley.edu/~aldous/150/lecture_37_waves.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_37_waves.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# present time T

**Source:** [`lecture_37_waves.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_37_waves.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


**Step -3.** (First step). Want to prove **upper** bound P( _W > w_ ) = _O_ ( _w_<sup>_−_1</sup><sup>_/_2</sup> ) _._

Given the current configuration with inter-customer distances ( _ξi , i ≥_ 1), the event that next-step wave has length _> w_ is essentially the event


for IID( _µ_ ) ( _ξi_<sup>_∗_).So</sup><sup>**if**thecurrent(</sup><sup>_ξi, i≥_1)werethemselvesIID(</sup><sup>_µ_)then</sup> by standard RW excursion theory the probability would be _≍ w_<sup>_−_1</sup><sup>_/_2</sup> . We now exploit the fact that, immediately after a long wave, the inter-customer distances are stochastically smaller than IID; this means that the time until the next long wave will be stochastically larger than if they were IID.

[end outline proof]

David Aldous Waves in a Spatial Queue: Stop-and-Go at Airport Security


A more sophisticated approach might be to consider **CBM as a space-indexed Markov process.**

The standard CBM process ( _By_ ( _s_ ) _,_ 0 _≤ s < ∞, y ∈_ R) with _By_ (0) = _y_ , with “time _s_ ” and “space” _y_ , can in fact be viewed in the opposite way. Define

_Xy_ = ( _By_ ( _s_ ) _− y ,_ 0 _≤ s < ∞_ )

so that _Xy_ takes values in the space _C_ 0(R<sup>+</sup> ) of continuous functions _f_ with _f_ (0) = 0. Now the process ( _Xy , −∞ < y < ∞_ ) with “time” _y_ is a continuous-time _C_ 0(R<sup>+</sup> )-valued Markov process. Apparently CBM has not been studied explicitly in this way. In principle one could determine its generator and seek to apply general techniques for weak convergence of discrete-time Markov chains to continuous-time limits.

Not yet tried . . . . . .

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous

---

[← Step -2.](03-step--2.md) · [Up: contents](index.md)
