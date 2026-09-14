---
title: How do the ideas from the course interact?
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# How do the ideas from the course interact?

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

So far we have covered several different topics.

I: Empirical Process Theory

II: Derivatives in Function Space

III: The Functional Delta Method

IV: Estimating Equations

V: Efficiency Theory

The topics relate to each other as follows.

I _−→_ III,IV: Empirical process theory is a tool used for showing that the functional delta method gives asymptotically linear estimates (along with Hadamard differentiability of the function), and a tool for showing solutions to estimating equations are asymptotically linear.

II _−→_ III,V: Hadamard differentiability is needed to show the functional delta method gives asymptotically linear estimates. The smoothness condition needed to define _regular_ parametric models (which form the foundation of efficiency theory) is Frechet differentiability of the mapping from a Euclidean parameter to the square-root density in _L_ 2( _P_ ).

30

III _−→_ IV: The functional delta method can be used to show that estimating equations give asymptotically linear estimators, as discussed in class, although this is not a standard approach.

V _−→_ III,IV: Efficiency theory lets us examine estimators (coming from either the functional delta method or estimating equations) to check whether they are efficient (the asymptotically best regular estimator). Efficiency theory also provides the class of all estimating functions of interest, through the orthogonal complement of the nuisance tangent space.

---

[← 1 Estimating Functions](27-1-estimating-functions.md) · [Up: contents](index.md) · [The general methodology of van der Laan and Robins →](29-the-general-methodology-of-van-der-laan-and-robins.md)
