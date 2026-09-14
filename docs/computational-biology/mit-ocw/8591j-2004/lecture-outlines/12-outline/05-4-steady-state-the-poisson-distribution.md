---
title: '4. Steady state: the Poisson distribution'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Steady state: the Poisson distribution

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Assume now that we are in steady state, so _dpn_ / _dt_ = 0. Then,


or, setting _<u>n</u>_ = _k_ /γ ,


Since this is true for all _n_ , both sides must be equal to a constant; and because _pn_ must be normalizable, it can be shown that the constant is simply zero. Therefore,


Setting Σ _pn_ = 1 gives _p_ 0 = _e_ − _<u>n</u>_ . The final steady state result is known as the Poisson distribution:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

---

[← 3. Emergence of the deterministic law](04-3-emergence-of-the-deterministic-law.md) · [Up: contents](index.md) · [5. The limit of large numbers →](06-5-the-limit-of-large-numbers.md)
