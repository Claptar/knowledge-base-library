---
title: Problem 2 answers continued (3)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2019.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/final2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 2 answers continued (3)

**Source:** [`old-exams/final2019.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

10

**3. “And if you ever saw it...” (24 points, 6 points / part).**

Some useful facts for this problem:

- For _n ∈{_ 0 _,_ 1 _, . . .}_ and _p ∈_ [0 _,_ 1]<sup>_d_</sup> with<sup>�</sup> _pi_ = 1, the multinomial density for _X ∼_ Multinom( _n, p_ ) is


An ecologist is interested in estimating the total population of reindeer in a wildlife preserve near the North Pole. She makes two visits to the preserve on two consecutive days and looks for reindeer. Each time she finds a reindeer she marks it with a unique identifying tag, so she can tell if she sees the same reindeer twice (in ecology this type of study is called a _capture-recapture_ or _mark-recapture_ study).

Assume that the same population of _n_ of reindeer is present in the preserve on both days, and each reindeer on each day has the same probability _π ∈_ (0 _,_ 1) of being seen by her, independently across the reindeer and the days (so the detections / non-detections are like 2 _n_ i.i.d. “coin flips” each with success probability _π_ ). Note that _n_ is the unknown parameter of interest and _π_ is an unknown nuisance parameter.

Let _N_ 11 denote the number of reindeer she sees both days, _N_ 10 the number she sees the first day not the second, and _N_ 01 the number she sees the second day but not the first. (Note that _N_ 00, the number of reindeer she sees on neither day, is not observed.)

- (a) Write down the likelihood for the model as a function of _N_ 01 _, N_ 10 _,_ and _N_ 11 and show that _T_ = ( _N_ 01 + _N_ 10 _, N_ 11) is a sufficient statistic for the model.

You do **NOT** need to show a sufficiency reduction from the Bernoulli model of detected/non-detected “coin flips” for each reindeer-day; after all we do not really get to observe the data for that model because we don’t know how many reindeer went undetected on both days. Just start with _N_ 01 _, N_ 10 _, N_ 11 as the data and _n_ and _π_ as the parameters.

- (b) (*) Show that _T_ is minimal sufficient (for this part you may assume we already know it is sufficient).

- (c) Define the estimator


11

Show that _n_ ˆ is consistent in the sense that _n/n_ ˆ _→p_ 1 as _n →∞_ with _π_ fixed.

- (d) Find the asymptotic distribution of _n_ ˆ from part (c) as _n →∞_ with _π_ fixed. You should center and scale appropriately so that it has a nondegenerate limiting distribution (that is, after centering and scaling it shouldn’t converge in probability to a constant).

12

---

[← Problem 2 answers continued (2)](09-problem-2-answers-continued-2.md) · [Up: contents](index.md) · [Problem 3 answers continued (1) →](11-problem-3-answers-continued-1.md)
