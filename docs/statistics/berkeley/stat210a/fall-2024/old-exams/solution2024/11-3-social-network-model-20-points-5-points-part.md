---
title: 3. Social network model (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2024.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Social network model (20 points, 5 points / part).

**Source:** [`old-exams/solution2024.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

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


8

the total number of friendships between pairs of students within the same group, and let


the total number of friendships between pairs of students in different groups. Show that ( _Tw, Tb_ ) is a complete sufficient statistic for this model.

---

[← Solution](10-solution.md) · [Up: contents](index.md) · [Solution →](12-solution.md)
