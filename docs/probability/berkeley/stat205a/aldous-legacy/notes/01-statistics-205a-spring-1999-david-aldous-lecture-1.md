---
title: STATISTICS 205A Spring 1999. David Aldous. Lecture 1.
source: https://www.stat.berkeley.edu/~aldous/205A/notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STATISTICS 205A Spring 1999. David Aldous. Lecture 1.

**Source:** [`notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (i) Constructing random variables.

- (ii) Radon-Nikodym densities.

A r.v. X with values in a measurable space (S, S) has a <u>distribution</u> ν:


Question: given a p.m. ν, does there exist a r.v. X whose distribution is ν? Uninteresting answer: Yes, because we can take Ω= S and X = identity.

To get something more interesting, recall undergraduate result.

**Lemma 1** Let µ be a probability measure on R, let F (x) = µ(−∞, x] be its distribution function, let


be the inverse distribution function. Then


where U has U (0, 1) distribution.

Now consider S-valued r.v.’s of the form h(U ), where h : [0, 1] → S is measurable.

**Lemma 2** Let ν be a p.m. on a <u>nice</u> (= <u>Standard Borel:</u> p. 33) space. Then there exists measurable h : [0, 1] → S such that h(U ) has distribution ν.

Proof. Easy: use Lemma 1 and definition of nice: there exists 1 − 1 map φ : S → R with φ and φ<sup>−1</sup> measurable.

To apply we need (Theorem 1.4.12): any complete separable metric space is nice.

**Corollary 3** (Counter-intuitive?). Let X1, X2, . . . be R-valued. Then there exist measurable h1, h2, . . . such that (h1(U ), h2(U ), . . .) has the same (joint) distribution as (X1, X2, . . .).

1

Proof. Use idea: consider **X** = (X1, X2, . . .) as a single R<sup>∞</sup> -valued r.v. Here’s a more constructive approach. Consider the binary representation of reals in (0, 1)


The B’s are independent Bernoulli (1/2). For each k ≥ 1 let I<sup>(k)</sup> = (ik1, ik2, . . .) be an infinite sequence of integers, the sequences disjoint in k. Use the B’s from I<sup>(k)</sup> to define Uk:


Then the U ’s are independent U (0, 1). Apply Lemma 1:

**Corollary 4** Let θ1, θ2, . . . be p.m.’s on R. Then there exist independent r.v.’s X1, X2, . . . such that Xi has distribution θi for each i.

Note this does not use Kolmogorov extension – later we will give a “constructive” proof of the Kolmogorov extension theorem.

---

[Up: contents](index.md) · [Radon-Nikodym densities. →](02-radon-nikodym-densities.md)
