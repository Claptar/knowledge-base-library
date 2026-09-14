---
title: 3. Social network model (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2024.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Social network model (20 points, 5 points / part).

**Source:** [`old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts you may assume are true for this problem:

- An _undirected graph_ is a set of vertices _V_ and a set of edges _E_ connecting pairs of vertices. Assume (without loss of generality) that the edges are labeled 1 to _m_ (so _V_ = _{_ 1 _, . . . , m}_ ) and each edge is represented by a pair of vertices ( _i, j_ ) with 1 _≤ i < j ≤ m_ ; that is, vertices _i_ and _j_ are connected to each other if ( _i, j_ ) _∈ E_ , in which case we say the edge ( _i, j_ ) is present.

- The binomial distribution Binom( _n, θ_ ) with parameter _θ ∈_ (0 _,_ 1) has probability mass function


Its mean and variance are


The binomial distribution arises when a coin lands heads with probability _θ_ , and we flip it _n_ times. Then, the number of heads we see is a Binom( _n, θ_ ) random variable.

We will consider a model where the set _V_ of vertices is fixed but the set _E_ of edges is random, governed by parameters that we are interested in. Define _Xi,j ∈ {_ 0 _,_ 1 _}_ as a binary indicator that ( _i, j_ ) is present. Assume that for each pair ( _i, j_ ), _Xi,j ∼_ Bern( _πi,j_ ), for _πi,j ∈_ (0 _,_ 1), and the _Xi,j_ values are independent.

Assume this model represents a social network, where each vertex represents an individual student in a school and an edge represents a friendship relation between two students; students _i_ and _j_ are friends if ( _i, j_ ) _∈ E_ .

In addition, assume each student belongs to a group _g_ ( _i_ ) _∈{_ 1 _, . . . , K}_ . Students in the same group may have a higher chance of forming friendships than students in different groups. We assume that it is known which group each student belongs to.

- (a) Suppose that _πi,j_ = _α_ + _β_ 1 _{g_ ( _i_ ) = _g_ ( _j_ ) _}_ , for unknown parameters _α ∈_ [0 _,_ 1] and _β ∈_ [0 _,_ 1 _− α_ ] (note _β_ is non-negative). Let


10

the total number of friendships between pairs of students within the same group, and let


the total number of friendships between pairs of students in different groups. Show that ( _Tw, Tb_ ) is a complete sufficient statistic for this model.

- (b) Find the maximum likelihood estimator _α,_ ˆ _β_<sup>ˆ</sup> .

- (c) (*) Now (for this part only) assume _α ∈_ (0 _,_ 1) is known. Does there exist an admissible unbiased estimator for _β_ , for the squared error loss?

- (d) (*) Now assume that the _β_ parameter possibly varies by group. That is, _πi,j_ = _α_ +<sup>�</sup><sup>_K_</sup> _k_ =1<sup>_βk_1</sup><sup>_{g_(</sup><sup>_i_) =</sup><sup>_g_(</sup><sup>_j_) =</sup><sup>_k}_, where</sup><sup>_α ∈_[0</sup><sup>_,_1] and</sup><sup>_β_1</sup><sup>_, . . . , βK∈_[0</sup><sup>_,_1</sup><sup>_−α_]</sup> are all unknown.

Assume we want to test the hypothesis _H_ 0 : _β_ 1 = _. . ._ = _βK_ = 0 against the alternative _H_ 1 : max _k βk >_ 0. Assume we have an estimator _β_<sup>ˆ</sup><sup>_∗_</sup> ( _X_ ) for the parameter _β_<sup>_∗_</sup> = max _k βk_ , and we want to will use a test that rejects for large values of _β_<sup>ˆ</sup><sup>_∗_</sup> ( _X_ ). How could we carry out an exact (finite-sample) test using _β_<sup>ˆ</sup><sup>_∗_</sup> as the test statistic? You do not need to give an explicit formula for the threshold, but explain how you would calculate it either in words or pseudocode.

11

---

[← Problem 2 answers continued (3)](09-problem-2-answers-continued-3.md) · [Up: contents](index.md) · [Problem 3 answers continued (1) →](11-problem-3-answers-continued-1.md)
