---
title: Ideas used in Lecture 8.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_9_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_9_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ideas used in Lecture 8.

**Source:** [`lecture_9_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_9_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Communicating classes, defined in terms of possible transitions. Definition of stationary distribution.


Special structures making it easy to calculate the stationary distribution: doubly stochastic, detailed balance, RW on weighted undirected graph, success runs.

To repeat the first item, recall that the transition matrix **P** of a Markov chain can be represented as a weighted directed graph. In the previous lecture we first looked at some “structure theory” – some qualitative aspects of the chain’s behavior do not depend on actual numerical transition probabilities but only on the graph of possible transitions.

David Aldous Lecture 9


_j_ is **accessible** from _i_ if there is a (directed) path from _i_ to _j_ (or _i_ = _j_ ).


_i_ and _j_ **communicate** if each is accessible from the other.


Because “communicate” is an equivalence relation, the state space **States** can be partitioned into **communicating classes** (CCs), say _C_ 1 _, C_ 2 _, . . ._ , such that _i_ and _j_ **communicate** if and only if they are in the same CC.


A class _C_ is **open** if it is possible to leave; that is if _pij >_ 0 for some _i ∈ C_ and _j ∈/ C_ . Otherwise it is **closed** .


The graph is **strongly connected** if there is only one CC, that is if all states communicate. In the Markov chain context this property is called **irreducible** .

David Aldous

Lecture 9


Here is another definition that depends only on the graph of possible transitions. Suppose we can partition the states into _k ≥_ 2 subsets _D_ 0 _, D_ 1 _, . . . , Dk−_ 1 such that every transition _i → j_ takes the particle from its current subset to the next subset. That is


where _u_ + 1 is taken modulo _k_ .

If (1) holds for some _k_ the chain is said to have **period** _k_ . (More precisely, the period is the largest _k_ for which (1) holds). If not, the chain is called **aperiodic** .

Some later theory will involve the assumption that a chain is irreducible and aperiodic. Given irreducible, to check the chain is aperiodic it is sufficient to know that _pii >_ 0 for some _i_ . The general necessary-and-sufficient condition – see [PK] section 4.3.2 – is that for some state _i_

greatest common divisor of _{t_ : _pii_<sup>(</sup><sup>_t_)</sup> _>_ 0 _}_ is 1.

David Aldous Lecture 9

---

[Up: contents](index.md) · [Stationary distributions →](02-stationary-distributions.md)
