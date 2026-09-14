---
title: Some models of coincidences.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_19_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_19_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Some models of coincidences.

**Source:** [`lecture_19_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_19_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Almost every textbook and popular science account of probability discusses the _birthday problem_ , and the conclusion

_with 23 people in a room, there is roughly a 50% chance that some two will have the same birthday._

And it’s easy to check this prediction with real data, for instance from MLB active rosters, which conveniently have 25 players and their birth dates.

[show ]

The predicted chance of a birthday coincidence is about 57%. With 30 MLB teams one expects around 17 teams to have the coincidence – can check in freshman seminar course.

David Aldous

Lecture 19


Mathematicians have put great ingenuity into finding exact formulas, but it’s simpler and more broadly useful to use approximate ones, based on the informal Poisson approximation. If events _A_ 1 _, A_ 2 _, . . ._ are roughly independent, and each has small probability, then the random number that occur has mean (exactly) _µ_ =<sup>�</sup> _i_<sup>P(</sup><sup>_Ai_)anddistribution</sup> (approximately) Poisson( _µ_ ), so


So if we list all possible coincidences in our model as _A_ 1 _, A_ 2 _, . . ._ then


David Aldous

Lecture 19


For the usual birthday problem, people often ask whether the fact that birthdays are not distributed exactly uniformly over the year makes any difference. So let’s consider _k_ people and non-uniform distribution _pi_ = P(born of day _i_ of the year) _._

For each _pair_ of people, the chance they have the same birthday is � _i_<sup>_p_</sup> _i_<sup>2,andthereare</sup> � _k_ 2� pairs, so from (1)


Write _median-k_ for the value of _k_ that makes this probability close to 1 _/_ 2 (and therefore makes the chance there _is_ a coincidence close to 1 _/_ 2). We calculate [board]


For the uniform distribution over _N_ categories this becomes


which for _N_ = 365 gives the familiar answer 23.

David Aldous Lecture 19


- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

To illustrate the non-uniform case, imagine hypothetically that there were twice as many births per day in one half of the year as in the other half, so _pi_ = 34 _N_<sup>or</sup> 32 _N_<sup>.Theapproximationbecomes</sup> 2<sup><u>1</u>+ 1</sup><sup>_._12</sup> _√N_ which for _N_ = 365 becomes 22.

The smallness of the change (“robustness to non-uniformity”) is in fact **not** typical of combinatorial problems in general. In the coupon collector’s problem, for instance, the change would be much more noticeable.

David Aldous Lecture 19


and then in the uniform case,

median- _k ≈_ 1 + 1 _._ 61 _N_<sup>2</sup><sup>_/_3</sup>

which for _N_ = 365 gives the less familiar answer 83.

( **2.** ) If instead of calendar days we have _k_ events at independent uniform times during a year, and regard a coincidence as seeing two of these events within 24 hours (not necessarily the same calendar day), then the chance that a particular two events are within 24 hours is 2 _/N_ for _N_ = 365, and we can repeat the calculation for the birthday problem to get


David Aldous Lecture 19

---

[← [From last class]](02-from-last-class.md) · [Up: contents](index.md)
