---
title: 5.7. BM as a harness
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.7. BM as a harness

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Another characterization of BM is obtained by considering the conditional expectation of _Bu_ for some _u ∈_ [ _s, t_ ] conditionally given the path of _Bv_ for _v ∈/_ ( _s, t_ ). As a consequence of the Markov property of _B_ and exchangeability of increments, there is the basic formula


which just states that given the path of _B_ outside of ( _s, t_ ), the path of _B_ on ( _s, t_ ) is expected to follow the straight line from ( _s, Bs_ ) to ( _t, Bt_ ). Following Hammersley [161] a process _B_ with this property is called a _harness_ . D. Williams showed around 1980 that every harness with continuous paths parameterized by [0 _, ∞_ ) may be represented as ( _σBs_ + _µs, s ≥_ 0) for _σ_ and _µ_ two random variables which are measurable with respect to the germ _σ_ -field


See also Jacod-Protter [186] who showed that every integrable L´evy process is a harness. Further discussion and references can be found in [289].

---

[← ( Ft ), such that](55-ft-such-that.md) · [Up: contents](index.md) · [5.8. Gaussian semi-martingales →](57-5-8-gaussian-semi-martingales.md)
