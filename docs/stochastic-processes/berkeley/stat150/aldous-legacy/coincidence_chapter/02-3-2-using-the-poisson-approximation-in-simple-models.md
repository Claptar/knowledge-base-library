---
title: 3.2 Using the Poisson approximation in simple models
source: https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf
source_file: sources/berkeley-stat150/aldous-legacy/coincidence_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.2 Using the Poisson approximation in simple models

**Source:** [`coincidence_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this section I want to make the point

mathematicians know how to do calculations in “small universe” settings, where one can specify in advance all the possible coincidences and their probabilities.

In fact while mathematicians have put great ingenuity into finding exact formulas, it is simpler and more informative to use approximate ones, based on the informal Poisson approximation<sup>3</sup> .

If events _A_ 1 _, A_ 2 _, . . ._ are roughly independent, and each has small probability, then the random number that occur has mean (exactly) _µ_ =<sup>P</sup> _i_<sup>P(</sup><sup>_Ai_)</sup> and distribution (approximately) Poisson( _µ_ ), so


Consider the birthday problem with _k_ people and non-uniform distribution

_pi_ = P(born of day _i_ of the year) _._

For each _pair_ of people, the chance they have the same birthday is<sup>P</sup> _i_<sup>_p_</sup> _i_<sup>2,</sup> and there are � _k_ 2� pairs, so from (3.1)


Write median- _k_ for the value of _k_ that makes this probability close to 1 _/_ 2 (and therefore makes the chance there _is_ a coincidence close to 1 _/_ 2). We calculate


> 3My 1989 book _Probability Approximations via the Poisson Clumping Heuristic_ consists of 100 examples of such calculations, within somewhat more complicated models.

38 _CHAPTER 3. COINCIDENCES, NEAR MISSES AND ONE-IN-A-MILLION CHANCES_

For the uniform distribution over _N_ categories this becomes


which for _N_ = 365 gives the familiar answer 23.

To illustrate robustness to non-uniformity, imagine hypothetically that half the categories were twice as likely as the other half, so _pI_ = 34 _N_<sup>or</sup> 32 _N_<sup>.Theapproximationbecomes</sup> 2<sup><u>1</u>+ 1</sup><sup>_._12</sup> _pN_ which for _N_ = 365 becomes 22. The smallness of the change might be considered another “paradox”, and is in fact atypical of combinatorial problems in general. In the coupon collector’s problem, for instance, the change would be much more noticable.

Let me quickly mention two variants. If we ask for the coincidence of _three_ people having the same birthday, then we can repeat the argument above to get


and then in the uniform case,


which for _N_ = 365 gives the less familiar answer 83.

If instead of calendar days we have _k_ events at independent uniform times during a year, and regard a coincidence as seeing two of these events within 24 hours (not necessarily the same calendar day), then the chance that a particular two events are within 24 hours is 2 _/N_ for _N_ = 365, and we can repeat the calculation for the birthday problem to get


Finding real-world instances where such theoretical predictions are applicable seems quite hard, in that the first instances one might think of – major fires in a big city, say – have noticeably non-uniform distribution.

---

[← 3.1 The birthday problem and its relatives](01-3-1-the-birthday-problem-and-its-relatives.md) · [Up: contents](index.md) · [3.3 Coincidences in everyday life →](03-3-3-coincidences-in-everyday-life.md)
