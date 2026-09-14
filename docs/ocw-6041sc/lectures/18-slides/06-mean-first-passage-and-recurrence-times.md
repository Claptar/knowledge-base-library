---
title: Mean first passage and recurrence times
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Mean first passage and recurrence times

**Source:** `lectures/18-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Chain with one recurrent class; fix _s_ recurrent

- Mean first passage time from _i_ to _s_ :

   - _ti_ = E[min _{n ≥_ 0 such that _Xn_ = _s} | X_ 0 = _i_ ]

- _t_ 1 _, t_ 2 _, . . . , tm_ are the unique solution to

      - _ts_ = 0 _, ti_ = 1 + � _pij tj,_ for all _i_ = _s j_

- Mean recurrence time of _s_ :

   - _t_<sup>_∗_</sup> _s_ = E[min _{n ≥_ 1 such that _Xn_ = _s} | X_ 0 = _s_ ]

- _t_<sup>_∗_</sup> _s_ = 1 +<sup>�</sup> _j_<sup>_p_</sup> _sj_<sup>_t_</sup> _j_

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

3

---

[← Expected time to absorption](05-expected-time-to-absorption.md) · [Up: contents](index.md)
