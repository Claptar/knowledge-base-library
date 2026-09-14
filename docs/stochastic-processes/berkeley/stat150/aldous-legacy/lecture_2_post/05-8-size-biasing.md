---
title: 8. Size-biasing
source: https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_2_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8. Size-biasing

**Source:** [`lecture_2_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A topic maybe not discussed in STAT134. Suppose each child is in some family; we can then consider


_X_ = number of children in a uniform random family

- _X_ � =number of children in the family of a uniform randomly picked child.

**These are different!** To see why, write _N_ = number of families. Then Number of families with _i_ children = ??? Number of children in _i_ -child families = ???


Total number of children = ????

P( _X_<sup>�</sup> = _i_ ) =???

Say _X_<sup>�</sup> has the **size-biased** distribution of _X_ .

David Aldous

Lecture 2


_X_ = number of children in a uniform random family

_X_ � =number of children in the family of a uniform randomly picked child.


_N_ = number of families.

We calculate


Number of families with _i_ children = _N_ P( _X_ = _i_ ) Number of children in _i_ -child families = _i × N_ P( _X_ = _i_ ) Total number of children =<sup>�</sup> _i_<sup>_i× N_P(</sup><sup>_X_=</sup><sup>_i_) =</sup><sup>_N_E</sup><sup>_X_</sup>


Say _X_<sup>�</sup> has the **size-biased** distribution of _X_ .

It’s a good exercise to express the distribution of _X_ in terms of the distribution of _X_<sup>�</sup> , and to give formulas for the expectations in terms of the other distribution.

David Aldous Lecture 2


_X_ = number of children in a uniform random family _X_ � =number of children in the family of a uniform randomly picked child.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

To calculate E _X_ from the distribution of _X_<sup>�</sup> , observe

---

[← 7. Inventing extra structure in a problem.](04-7-inventing-extra-structure-in-a-problem.md) · [Up: contents](index.md) · [and so →](06-and-so.md)
