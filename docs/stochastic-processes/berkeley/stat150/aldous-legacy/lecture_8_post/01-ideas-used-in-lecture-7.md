---
title: Ideas used in Lecture 7.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_8_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ideas used in Lecture 7.

**Source:** [`lecture_8_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

First-step analysis of simple asymmetric random walk. Analysis of “success runs” chain using special structure. Analysis of “death and immigration” chain using special structure.

Recall that the transition matrix **P** of a Markov chain can be represented as a weighted directed graph. In this lecture we first look at some “structure theory”. This will show us that some qualitative aspects of the chain’s behavior do not depend on actual numerical transition probabilities but only on the graph of possible transitions. This material can be found in Chapter 4 of [KP].

David Aldous Lecture 8


Here are some definitions that depend only on the graph of possible transitions.


- _j_ is **accessible** from _i_ if there is a (directed) path from _i_ to _j_ (or _i_ = _j_ ).


- _i_ and _j_ **communicate** if each is accessible from the other.


- Because “communicate” is an equivalence relation, the state space **States** can be partitioned into **communicating classes** (CCs), say _C_ 1 _, C_ 2 _, . . ._ , such that _i_ and _j_ **communicate** if and only if they are in the same CC.


- A class _C_ is **open** if it is possible to leave; that is if _pij >_ 0 for some _i ∈ C_ and _j ∈/ C_ . Otherwise it is **closed** .


   - The graph is **strongly connected** if there is only one CC, that is if all states communicate. In the Markov chain context this property is called **irreducible** .

- I will give some theory results but just outline proofs.

David Aldous

Lecture 8


**Lemma.** If the state space is finite then there exists at least one closed CC.

If the hitting time _TC_ = min _{t_ : _Xt ∈ C }_ on a **closed** class _C_ is finite, then the chain must remain in _C_ for all times _t ≥ TC_ . **Lemma.** If the state space is finite then, for any initial _i_ ,

P _i_ ( _TC < ∞_ for some closed _C_ ) = 1 _._

The probabilities _pi,C_ = P _i_ ( _TC < ∞_ ) can be calculated using first-step analysis.

David Aldous Lecture 8

---

[Up: contents](index.md) · [Stationary distributions →](02-stationary-distributions.md)
