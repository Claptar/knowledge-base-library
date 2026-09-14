---
title: 4. Change point problem (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/final2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Change point problem (25 points, 5 points / part).

**Source:** [`units/old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

_•_ The Beta distribution Beta( _α, β_ ) with parameters _α, β >_ 0 has density


with respect to the Lebesgue measure on (0 _,_ 1). Its mean and variance are


- The negative binomial distribution NB( _m, θ_ ) with parameters _m ∈{_ 1 _,_ 2 _, . . .}, θ ∈_ (0 _,_ 1) has probability mass function


Its mean and variance are


Assume we observe independent random variables _Xi ∼_ NB( _m, θi_ ) for _i_ = 1 _, . . . , n_ . Assume also that the _θi_ values are constant except at some integer _k ∈ {_ 1 _, . . . , n −_ 1 _}_ where they change. That is,


for _γ_ 0 _, γ_ 1 _∈_ (0 _,_ 1).

Until otherwise specified, assume _k_ is known. Throughout the problem, we will assume _m_ is known.

- (a) Calculate the maximum likelihood estimator for _γ_ 0 and find its asymptotic distribution if _k, n →∞_ . You do not need to check regularity conditions.

- i.i.d.

- (b) Next assume we introduce a prior distribution that _γ_ 0 _, γ_ 1 _∼_ Beta( _α, β_ ). Give the posterior distribution for ( _γ_ 0 _, γ_ 1) given _X_ 1 _, . . . , Xn_ , and give the Bayes estimator for squared error loss.

16

- (c) (*) Find the asymptotic distribution of the Bayes estimator for _γ_ 0, holding _γ_ 0 and _γ_ 1 fixed and sending _k, n →∞_ .

- (d) Next, we relax the assumption that _k_ is known. Instead assume _n_ = 10 and all we know is that _k ∈{_ 4 _,_ 5 _,_ 6 _}_ . Find a minimal sufficient statistic for the three-parameter model with _γ_ 0 _, γ_ 1 _∈_ (0 _,_ 1) and _k ∈{_ 4 _,_ 5 _,_ 6 _}_ . You do not need to prove it is minimal, as long as you give the right answer.

- (e) Continuing with the three-parameter model above, consider a Bayesian api.i.d. _∼_

- proach where we assign priors _k ∼_ Unif( _{_ 4 _,_ 5 _,_ 6 _}_ ) independently of _γ_ 0 _, γ_ 1 Beta( _α, β_ ). Give a Gibbs sampler algorithm to sample from the posterior distribution of ( _k, γ_ 0 _, γ_ 1).

17

---

[← Problem 3 answers continued (3)](14-problem-3-answers-continued-3.md) · [Up: contents](index.md) · [Problem 4 answers continued (1) →](16-problem-4-answers-continued-1.md)
