---
title: 'Special setting: detailed balance.'
source: https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_8_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Special setting: detailed balance.

**Source:** [`lecture_8_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose we can find numbers _wi >_ 0 such that

_wi pij_ = _wj pji ∀i, j._ (2)

Then


is a stationary distribution.

[board] The condition (2) is called **detailed balance** . It is stronger than the **balance** condition


David Aldous Lecture 8


**Example: random walk on a weighted undirected graph.**

Suppose we are given an undirected graph, and suppose there is a “weight” _aij_ = _aji >_ 0 on each edge ( _i, j_ ). Define _ai_ =<sup>�</sup> _j_<sup>_aij_.Then</sup> _pij_ = _aij /ai_

defines a transition matrix.

Easy to check [board] that the detailed balance condition (2) always holds for _wi_ = _ai_ . So


is a stationary distribution.

David Aldous Lecture 8

---

[← Special setting: Doubly stochastic chains](03-special-setting-doubly-stochastic-chains.md) · [Up: contents](index.md)
