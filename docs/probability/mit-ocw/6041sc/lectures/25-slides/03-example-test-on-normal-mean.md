---
title: Example (test on normal mean)
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/25-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example (test on normal mean)

**Source:** `lectures/25-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- _n_ data points, i.i.d. _H_ 0: _Xi ∼ N_ (0 _,_ 1) _H_ 1: _Xi ∼ N_ (1 _,_ 1)

- Likelihood ratio test; rejection region:

   - <u>(1</u> _<u>/</u>_ _~~<u>√</u>~~_ 2 _π_ <u>)</u> _n_ exp _<u>{−</u>_ <u>￿</u> _<u>i</u>_ <u>(</u><sup>_X_</sup> _i_<sup>_−_1)</sup> 2<sup>_<u>/</u>_2</sup><sup>_<u>}</u>_</sup> _−_ 2 _> ξ_

   - (1 _/_ _~~√~~_ 2 _π_ )<sup>_n_</sup> exp _{_ ~~￿~~ _i_<sup>_X_</sup> _i_<sup>_/_2</sup> _}_

**–** algebra: reject _H_ 0 if: ￿ _Xi > ξ_<sup>_￿_</sup> _i_

- Find _ξ_<sup>_￿_</sup> such that

   - _n_

   - **P** _Xi > ξ￿_ ; _H_ 0 = _α_ ￿￿ ￿ _i_ =1

- use normal tables

- Likelihood ratio test: reject _H_ 0 if _pX_ <u>(</u> _x_ ; _H_ 1) _<u>fX</u>_ <u>(</u> _x_ ; _H_ 1) _> ξ_ or _> ξ_

- _pX_ ( _x_ ; _H_ 0) _fX_ ( _x_ ; _H_ 0)

- fix false rejection probability _α_ (e.g., _α_ = 0 _._ 05)

- choose _ξ_ so that **P** (reject _H_ 0; _H_ 0) = _α_

---

[← Simple binary hypothesis testing](02-simple-binary-hypothesis-testing.md) · [Up: contents](index.md) · [Example (test on normal variance) →](04-example-test-on-normal-variance.md)
