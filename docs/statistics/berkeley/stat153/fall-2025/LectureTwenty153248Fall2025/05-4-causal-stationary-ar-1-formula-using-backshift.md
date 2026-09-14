---
title: 4 Causal Stationary AR (1) formula using Backshift
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Causal Stationary AR (1) formula using Backshift

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We derived the formula (3) by recursing the AR(1) equation _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _ϵt_ successively into the past (as in (2)) and taking the limit _M →∞_ . This method is difficult to carry out for AR( _p_ ) when _p ≥_ 2. Instead there is an alternative method (using Backshift) of directly arriving at (3) from _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _ϵt_ . This alternative method is very easy to generalize to higher _p_ .

Here is the description of the backshift method for AR(1). We will tackle higher _p_ in the next section. First note that AR(1) difference equation in backshift notation is


Thus we can formally write


Using

we obtain


6

which gives (3). This formal method is sometimes called Backshift Calculus and it works for higher order AR models as well.

---

[← 3 Backshift Notation](04-3-backshift-notation.md) · [Up: contents](index.md) · [5 AR( p ) for p ≥ 1 →](06-5-ar-p-for-p-1.md)
