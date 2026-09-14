---
title: Species
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2018.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Species

**Source:** [`old-exams/solution2018.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will assume throughout that the rows _N_<sup>(1)</sup> _, . . . , N_<sup>(</sup><sup>_m_)</sup> are i.i.d. random vectors in R<sup>_s_</sup> (but the coordinates _N_ 1<sup>(</sup><sup>_i_)</sup><sup>_, . . . , N_</sup> _s_<sup>(</sup><sup>_i_)</sup> within a single site are _not_ i.i.d.).

- (a) First assume _Nj_<sup>(</sup><sup>_i_)</sup> ind. _∼_ Pois( _λj_ ) for _j_ = 1 _, . . . , s_ , and that at each site the species counts are independent, i.e.


5

Find a complete sufficient statistic for the entire data table and give a UMVU estimator for _λj_ , the average abundance of species _j_ , explaining why it is UMVU.

- (b) Next, assume we use outside data to compute a dissimilarity measure _d_ ( _j, k_ ) _∈_ [0 _, ∞_ ) for each pair of species 1 _≤ j < k ≤ s_ ; for example _d_ ( _j, k_ ) could denote how long ago the species diverged in their evolution. Take the _d_ ( _j, k_ ) as fixed and known.

We might expect that some latent characteristics of the habitat at site _i_ cause similar species to be more or less common together, and we can test this hypothesis by modifying our model:


Show that this model is an exponential family with _s_ + 1 sufficient statistics, and find the natural parameter corresponding to each (as always, there are multiple ways to write these). You do _not_ need to find the normalizing constant.

- (c) Find a UMPU test of _H_ 0 : _β_ = 0 (independence) vs. _H_ 1 : _β >_ 0 (positive correlation between similar species) and explain how to find its critical value.

- (d) (*) Now suppose we want to make our test more robust by dropping the Poisson assumption: under the null hypothesis the species counts are still independent, but now with unknown distributions (still supported on the non-negative integers):


and under the alternative the counts of similar species are still more correlated. Modify your test from part (b) so that it controls finitesample Type I error, in this nonparametric model.

6

---

[← Problem 1 Solutions](03-problem-1-solutions.md) · [Up: contents](index.md) · [Problem 2 solutions →](05-problem-2-solutions.md)
