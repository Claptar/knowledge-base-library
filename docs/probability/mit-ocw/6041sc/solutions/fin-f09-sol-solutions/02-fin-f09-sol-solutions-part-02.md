---
title: Fin f09 sol solutions Part 02 —
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/fin-f09-sol-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fin f09 sol solutions Part 02 —

**Source:** `solutions/fin-f09-sol-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

�C���� 9��� {�������� � C��� �����

_·_ a normal random variable with mean _np_ = 72 2 _/_ 3 = 48 and variance _np_ (1 _− p_ ) = 16 and approximate the desired probability as


## (d) (5 points)

The event that Al is the first to finish a lap is the same as the event that the first arrival in the merged process came from Al’s process. This probability is


## (e) (5 points)

This is an instance of the random incidence paradox, so the duration of Al’s current lap consists of the sum of the duration from the time of your arrival until Al’s next lap completion and the duration from the time of your arrival back to the time of Al’s previous lap completion. This is the sum of 2 independent exponential random variables with parameter _λA_ = 21 (i.e. a second- order Erlang random variable):


## (f) (5 points)

As in the previous part, the duration of Al’s second lap consists of the time remaining from _t_ = 1 _/_ 4 until he completes his second lap and the time elapsed since he began his second lap until _t_ = 1 _/_ 4. Let _X_ be the time elapsed and _Y_ be the time remaining. We can still model the time remaining _Y_ as an exponential random variable. However, we can no longer do the same for the time elapsed _X_ because we know _X_ can be no larger than 1/4, whereas the exponential random variable can be arbitrarily large.

To find the PDF of _X_ , let’s first consider its CDF.


Thus, we find that the X is uniform over the interval [0 _,_ 1 _/_ 4], with PDF


3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

�C���� 9��� {�������� � C��� �����

The total time that Al spends on his second lap is _T_ = _X_ + _Y_ . Since _X_ and _Y_ correspond to disjoint time intervals in the Poisson process, they are independent, and therefore we can use convolution to find the PDF of _T_ :


**Problem 5.** (25 points)


Using the law of iterated expectations and the law of total variance,


where var( _N | X_ ) = **E** [ _N | X_ ] = _X._

(b) (5 points)


(c) (5 points)

The equation for _X_<sup>ˆ</sup> lin( _N_ ), the linear least-squares estimator of _X_ based on an observation of _N_ , is


4

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Fin f09 sol solutions Part 03 — →](03-fin-f09-sol-solutions-part-03.md)
