---
title: 6. The 3rd formula for variance.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_2_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6. The 3rd formula for variance.

**Source:** [`lecture_2_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Writing _µ_ = E _X_ , the definition of variance is


and a line of algebra gives an equivalent formula


Recall s _._ d _._ ( _X_ ) = _√_ var _X_ is the “interpretable” measure of spread of the RV _X_ , which scales in the natural way:

s _._ d _._ ( _cX_ ) = _|c| ×_ s _._ d _._ ( _X_ ); var ( _cX_ ) = _c_<sup>2</sup> var ( _X_ ) _._

David Aldous Lecture 2


Variance is mathematically convenient because of the property:

if _X , Y_ independent then var ( _X_ + _Y_ ) = var ( _X_ ) + var ( _Y_ ) _._

But note this implies

if _X , Y_ independent then var ( _X − Y_ ) = var ( _X_ ) + var ( _Y_ )

with a “plus” not a “minus”. This leads to the “ 3rd formula for variance”:


where _X_ 1 and _X_ 2 are independent r.v.’s distributed as _X_ . This formula has an intuitive “variability of realizations” interpretation.

David Aldous Lecture 2

---

[← 5. Decreasing dice rolls.](02-5-decreasing-dice-rolls.md) · [Up: contents](index.md) · [7. Inventing extra structure in a problem. →](04-7-inventing-extra-structure-in-a-problem.md)
