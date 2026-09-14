---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps4.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/ps4.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps4.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps4.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. If I want to compute the trace of a matrix, _A_ = _XY_ , where both _X_ and _Y_ are _n × n_ and where the trace is<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Aii_, a naive implementation is sum(diag(X%</sup> *<sup>%Y)).</sup>

   - (a) What is the computational complexity of that naive implementation: _O_ ( _n_ ) _, O_ ( _n_<sup>2</sup> ) or _O_ ( _n_<sup>3</sup> )?

   - (b) Why is that naive implementation inefficient?

   - (c) How could you (much) more efficiently compute the trace in R using vectorized operations on the matrices (please provide R code and do not use _apply()_ )? What computational complexity is your solution?

2. First, some background on random number generation, which we’ll discuss in great detail in the simulation unit. Random numbers on a computer are actually pseudo-random and are generated from deterministic algorithms that produce a fixed sequence of numbers that behave as if they are random. _set.seed()_ initializes the object _.Random.seed_ , and that object determines where in the deterministic sequence we start generating random numbers. If we set the seed to be a given number, we can repeatedly generate the same “random” numbers, as seen by running the code here.

**set.seed** (1) **save** (.Random.seed, file = 'tmp.Rda') **runif** (1) ## [1] 0.2655087 **set.seed** (1) **runif** (1) _## same random number!_

1

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Ps 04 — Part 03 — →](03-ps-04-part-03.md)
