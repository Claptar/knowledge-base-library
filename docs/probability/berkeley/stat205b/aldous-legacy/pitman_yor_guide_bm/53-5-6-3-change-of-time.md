---
title: 5.6.3. Change of time
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.6.3. Change of time

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If the time parameter _t ≥_ 0 is replaced by some increasing and right continuous family of stopping times ( _τu, u ≥_ 0), then according to the general theory of semimartingales we obtain from Brownian motion _B_ a process ( _Bτu, u ≥_ 0) which is a semimartingale relative to the filtration ( _Fτu , u ≥_ 0). In particular, it is follows from the Burkholder-Davis-Gundy inequalities [370, _§_ IV.4] that if E(<sup>_√_</sup> _<u>τu</u>_ <u>)</u> _< ∞_ then ( _Bτu , u ≥_ 0) is a martingale. Monroe [312] showed that every semimartingale can be obtained, in distribution, as ( _Bτu , u ≥_ 0) for a suitable time change process ( _τu_ ).

A beautiful application of L´evy’s characterization of BM is the representation of continuous martingales as time-changed Brownian motions. Here is the precise statement. Let ( _Mt, t ≥_ 0) be a _d_ -dimensional continuous local martingale relative to some filtration ( _Ft_ ), such that

- (i) _⟨M_<sup>(</sup><sup>_i_)</sup> _⟩t_ = _At_ for some increasing process ( _At_ ) with _A∞_ = _∞_ , and all _i_ .

- (ii) _⟨M_<sup>(</sup><sup>_i_)</sup> _, M_<sup>(</sup><sup>_j_)</sup> _⟩t ≡_ 0, which is to say that the product _Mt_<sup>(</sup><sup>_i_)</sup><sup>_M_(</sup> _t_<sup>_j_)</sup> is an ( _Ft_ ) local martingale, for all _i̸_ = _j_ .

Let


Then the process ( _Bt_ ) is an ( _Fτ_ ( _t_ )) Brownian motion, and


Doeblin in 1940 discovered the instance of this result for _d_ = 1 and _Mt_ = _f_ ( _Xt_ ) _−_ �0 _t_<sup>(</sup><sup>_Lf_)(</sup><sup>_Xs_)</sup><sup>_ds_for</sup><sup>_X_aone-dimensionaldiffusionand</sup><sup>_f_afunctionin</sup> the domain of the infinitesimal generator _L_ of _X_ . See [62, p. 20]. Dambis [89] and Dubins-Schwarz [101] gave the general result for _d_ = 1, while Getoor and Sharpe [151] formulated it for _d_ = 2, as discussed in the next subsection.

As a simple application of (69), we mention the following: if ( _Mu, u ≥_ 0) is a non-negative local martingale, such that


then


To prove (70), it suffices thanks to (69) to check it for _M_ a Brownian motion started at _a_ and stopped at its first hitting time of 0. The conclusion (70) can also be deduced quite easily by optional sampling. See [328] for further results in this vein.

---

[← 5.6.2. Change of filtration](52-5-6-2-change-of-filtration.md) · [Up: contents](index.md) · [5.6.4. Knight’s theorem →](54-5-6-4-knight-s-theorem.md)
