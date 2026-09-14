---
title: 1 Waiting times for chemical reactions (8 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Waiting times for chemical reactions (8 points)

**Source:** `psets/05-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the previous assignment, we saw that for a chemical reaction occurring at rate r, the distribution of waiting times τ between reaction events is given by:


- a. By integrating over time, verify that the distribution is normalized

- b. Here we will see a method for obtaining a random variable from a given distribution, starting from a uniformly distributed random variable:

Suppose _u_ is a random variable with some distribution _p_ ( _u_ ) , and _θ_ ( _u_ ) is a function of _u_ . Then the probability that _θ_<sup>_∗_</sup> lies between _θ_ ( _u_ ) and _θ_ ( _u_ + _du_ ) is the same as the probability that _u_<sup>_∗_</sup> lies between _u_ and _u_ + _du_ . This gives us a recipe for calculating the distribution _p_ ( _θ_ ) :


Assuming u is uniformly distributed between 0 and 1, show that the number


is distributed precisely as required for the waiting times above.

---

[← Problem Set 5](01-problem-set-5.md) · [Up: contents](index.md) · [2 Stochastic simulation of an auto-regulatory system (22 points) →](03-2-stochastic-simulation-of-an-auto-regulatory-system-22-poin.md)
