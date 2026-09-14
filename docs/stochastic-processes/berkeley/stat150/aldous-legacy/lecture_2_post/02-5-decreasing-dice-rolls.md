---
title: 5. Decreasing dice rolls.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_2_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5. Decreasing dice rolls.

**Source:** [`lecture_2_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Throw a die 3 times – what is the chance that the successive numbers are strictly decreasing, like_ 5 _,_ 3 _,_ 2 _?_

Can do by counting – there are 20 possibilities, so chance = 20 _/_ 6<sup>3</sup> . But how to do the general question:

_Throw a hypothetical m-sided (numbers_ 1 _,_ 2 _, . . . , m) die k times, for k ≤ m. What is the chance p_ ( _k, m_ ) _that the successive numbers are strictly decreasing?_

Now we need to get more organized . . . . . .

David Aldous Lecture 2


Throw a hypothetical _m_ -sided (numbers 1 _,_ 2 _, . . . , m_ ) die _k_ times. _p_ ( _k, m_ ) = P(successive numbers are strictly decreasing).

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Small trick: for this to happen, the numbers must be all different. If the _k_ numbers are all different, then each of the _k_ ! possible orders are equally likely (“argument by symmetry”), so the conditional probability of being strictly decreasing = 1 _/k_ ! So


But we know from the “birthday problem” that


and we find


which suggests another way to derive this answer.

David Aldous Lecture 2

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [6. The 3rd formula for variance. →](03-6-the-3rd-formula-for-variance.md)
