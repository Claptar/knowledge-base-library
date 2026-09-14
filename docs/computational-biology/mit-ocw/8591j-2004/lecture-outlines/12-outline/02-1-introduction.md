---
title: 1. Introduction
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Introduction

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider a simple chemical system in which a molecule _X_ is created at some constant rate _k_ and destroyed in a first-order reaction with rate γ. If the total number _n_ of molecules is large, as is the case in standard chemical systems (Avogadro’s number is about 10<sup>24</sup> ), we can ignore the fact that _n_ is an integer, but treat it instead as a continuous variable (Fig. 1a, dashed line), writing


However, this is certainly not applicable in living cells, where there are typically thousands of molecules of a given protein, hundreds of free ribosomes and RNA polymerases, tens of mRNA molecules of each kind, and one or two copies of most genes. Moving, then, to a discrete description, we might guess that the actual time evolution of _n_ would be somewhat coarse, but still completely predictable. For example, we could imagine a situation in which creation events occurred at time intervals ∆ _t_ = ∆ _n_ /( _k_ -γ _n_ ), with ∆ _n_ = 1 (Fig. 1a, solid line). However, this is physically impossible: it would require the system to somehow


<!-- Start of picture text -->
35  35<br>30  a  30  b  c<br>25  25<br>20  20<br>15  15<br>10  10<br>5  Internal clock  5  Markov process<br>0  0<br>0.0  2.5  5.0  7.5  0.0  2.5  5.0  7.5<br>time  time<br>n(t)  n(t)<br><!-- End of picture text -->

Figure 1: The implications of discreteness

keep track of the time that elapsed between event occurrences, as a clock does between successive ticks. But there is no internal clock in our simple system – there are only molecules which collide into one another. The system has no memory of the past, so its response can only depend on present conditions. (This is the defining property of a Markov process.) What therefore happens is that creation and destruction reactions occur with some _probability_ per unit time, proportional to the reaction rates. This means that each time the reaction is run with fixed initial conditions, it will proceed somewhat differently:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

the system will be stochastic (Fig. 1b). If we ran several experiments of this kind, recording the number of molecules present after some fixed time had elapsed, we would find a distribution of possible values (Fig. 1c).

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Probabilistic formulation of reaction kinetics: the Master Equation →](03-2-probabilistic-formulation-of-reaction-kinetics-the-master.md)
