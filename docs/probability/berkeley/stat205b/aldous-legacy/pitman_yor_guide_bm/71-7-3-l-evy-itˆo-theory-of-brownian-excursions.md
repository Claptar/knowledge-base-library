---
title: 7.3. L´evy-Itˆo theory of Brownian excursions
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.3. L´evy-Itˆo theory of Brownian excursions

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The L´evy-Itˆo excursion theory allows the Brownian path to be reconstructed from its random zero set, an ensemble of independent standard Brownian excursions, and a collection of independent random signs, one for each excursion. The zero set can first be created as the closed range of a stable subordinator ( _Tℓ, ℓ ≥_ 0) which ends up being the inverse local time process of _B_ . Then for each _ℓ_ such that _Tℓ− < Tℓ_ the path of _B_ on [ _Tℓ−, Tℓ_ ] can be recreated by shifting and scaling a standard Brownian excursion to start at time _Tℓ−_ and end at time _Tℓ_ .

Due to (78), the process of excursions of _|B|_ away from 0 is equivalent in distribution to the process of excursions of _B_ above _<u>B</u>_ <u>.</u> According to the L´evyItˆo description of this process, if _Iℓ_ := [ _Tℓ−, Tℓ_ ] for _Tℓ_ := inf _{t_ : _B_ ( _t_ ) _< −ℓ}_ , the points


where _µ_ is Lebesgue measure, are the points of a Poisson point process on R _>_ 0 _×_ R _>_ 0 _× C_ [0 _, ∞_ ) with intensity


_J. Pitman and M. Yor/Guide to Brownian motion_

49

On the other hand, according to Williams [438], if _Mℓ_ := _B_ [ _Iℓ_ ] _−_ _<u>B</u>_ <u>[</u> _Iℓ_ ] is the maximum height of the excursion of _B_ over _<u>B</u>_ on the interval _Iℓ_ , the points


are the points of a Poisson point process on R _>_ 0 _×_ R _>_ 0 _× C_ [0 _, ∞_ ) with intensity


where _B_<sup>ex</sup><sup>_| m_</sup> is a _Brownian excursion conditioned to have maximum m_ . That is to say _B_<sup>ex</sup><sup>_| m_</sup> is a process _X_ with _X_ (0) = 0 such that for each _m >_ 0, and _Hx_ ( _X_ ) := inf _{t_ : _t >_ 0 _, X_ ( _t_ ) = _x}_ , the processes _X_ [0 _, Hm_ ( _X_ )] and _m − X_ [ _Hm_ ( _X_ ) _, H_ 0( _X_ )] are two independent copies of _R_ 3[0 _, Hm_ ( _R_ 3)], and _X_ is stopped at 0 at time _H_ 0( _X_ ). _Itˆo’s law of Brownian excursions_ is the _σ_ -finite measure _ν_ on _C_ [0 _, ∞_ ) which can be presented in two different ways according to (97) and (99) as


where the first expression is a disintegration according to the lifetime of the excursion, and the second according to its maximum. The identity (100) has a number of interesting applications and generalizations [36, 351, 356]. See [370, Ch. XII], [352] and [448] for more detailed accounts of Itˆo’s excursion theory and its applications.

**Notes and Comments** See [371, 252, 23, 370, 160] for different approaches to the basic path transformation (94) from _B_ to _R_ 3, its discrete analogs, and various extensions. In terms of _X_ := _−B_ and _M_ := _X_ = _−B_ <u>,</u> the transformation takes _X_ to 2 _M − X_ . For a generalization to exponential functionals, see Matsumoto and Yor [291]. This is also discussed in [333], where an alternative proof is given using reversibility and symmetry arguments, with an application to a certain directed polymer problem. A multidimensional extension is presented in [334], where a representation for Brownian motion conditioned never to exit a (type A) Weyl chamber is obtained using reversibility and symmetry properties of certain queueing networks. See also [333, 228] and the survey paper [332]. This representation theorem is closely connected to random matrices, Young tableaux, the Robinson-Schensted-Knuth correspondence, and symmetric functions theory [331, 335]. A similar representation theorem has been obtained in [58] in a more general symmetric spaces context, using quite different methods. These multidimensional versions of the transformation from _X_ to 2 _M − X_ are intimately connected with combinatorial representation theory and Littelmann’s path model [278].

_J. Pitman and M. Yor/Guide to Brownian motion_

50

---

[← 7.2. The Brownian zero set](70-7-2-the-brownian-zero-set.md) · [Up: contents](index.md) · [8. Planar Brownian motion →](72-8-planar-brownian-motion.md)
