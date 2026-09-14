---
title: 4. Estimation in the Geometric model (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Estimation in the Geometric model (25 points, 5 points / part).

**Source:** [`old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- The geometric distribution Geom( _θ_ ) with parameter _θ ∈_ (0 _,_ 1) has probability mass function


Its mean and variance are


The geometric distribution arises when a coin lands heads with probability _θ_ , and we flip it repeatedly until it lands heads. Then, the number of tails we see before the first heads is a Geom( _θ_ ) random variable.

Assume throughout this problem that we observe _X_ 1 _, . . . , Xn_


- (a) Find a minimal sufficient statistic for the distribution. Is it complete?

- (b) Let _θ_<sup>ˆ</sup> ( _X_ ) denote the maximum likelihood estimator for _θ_ , where _X_ = ( _X_ 1 _, . . . , Xn_ ). Give an explicit formula.

- (c) Show that _θ_<sup>ˆ</sup> ( _X_ ) is consistent and use it to construct a Wald confidence interval for _θ_ . Give an explicit formula.

- (d) Define the tail probability _τk_ ( _θ_ ) = (1 _− θ_ )<sup>_k_</sup> to be the probability that a single observation is at least _k_ . That is,


Give the asymptotic distribution for the maximum likelihood estimator ˆ _τk_ ( _X_ ) = _τk_ ( _θ_<sup>ˆ</sup> ( _X_ )) when _k_ is fixed and _n →∞_ (appropriately centered and scaled).

- (e) (*) Assume that _n_ = 4, and ( _X_ 1 _, X_ 2 _, X_ 3 _, X_ 4) = (0 _,_ 3 _,_ 4 _,_ 2). Evaluate the UMVU estimator for _τ_ 10( _θ_ ) on the given data set. Your answer should be a number, and you should justify how you calculated it.

15

---

[← Problem 3 answers continued (3)](13-problem-3-answers-continued-3.md) · [Up: contents](index.md) · [Problem 4 answers continued (1) →](15-problem-4-answers-continued-1.md)
