---
title: Introduction
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/03-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 1.3 Forward Kolmogorov equation

Let us again start with the Master equation, for a system where the states can be ordered along a line, such as the previous examples with population size n = 0, 1, 2 · · · , N. We start again with a general Master equation


In many relevant circumstances, the number of states is large and the probability varies smoothly from one site to the next. In such cases, it is reasonable to replace the discrete index n with a continuous variable x, the probabilities pn(t) with a probability density p(x, t), and the rates Rmn with a rate function R(x<sup>′</sup> , x). The rate function R depends on two variables denoting the start and end positions along the line. We are free to redefine the two arguments of this function, and it is useful to reparametrize it as R(x<sup>′</sup> − x, x) indicating the rate at which, starting from the position x, a transition is made to a position ∆= x<sup>′</sup> − x away. As in the case of mutations, there is usually a preference for changes that are local, i.e. the rates decay rapidly when the separation x<sup>′</sup> − x becomes large.

These transformations and relabelings,


enable us to transform Eq. (1.28) to the continuous integral equation


Note, however, that the sum in Eq. (1.28) excluded the term m = n. To treat this properly in the continuum limit, we can focus on an interval y around any point x, and the change in probability due to incoming flux from x − y and the outgoing flux to x + y, leading to


We now make a Taylor expansion the first term in the square bracket, but only with respect to the location of the incoming flux, treating the argument pertaining to the separation of the two points as fixed, i.e.


While formally correct, the above expansion is useful only in cases where typical values of y are small (only almost local transitions occur). If we keep terms up to the second order, Eq. (1.31) can be rewritten as


9

The integrals over y can be taken inside the derivatives with respect to x,


after which we obtain


We have introduced


and


Equation (1.35) is a prototypical description of drift and diffusion which appears in many contexts. The drift term v(x) expresses the rate (velocity) with which the position changes from x due to the transition rates. Given the probabilistic nature of the process, there are variations in the rate of change of position captured by the position dependent diffusion coefficient D(x). The drift–diffusion equation is known as the forward Kolmogorov equation in the context of populations. As a description of random walks it appeared earlier in physics literature as the Fokker–Planck equation.

In the context of population genetics, it is convenient to introduce the variable x = n/N, such that in the continuum limit x ∈ [0, 1]. The rates in Eq. (1.22) change n by ±1, and hence


while

---

[Up: contents](index.md) · [1.3.1 Binomial selection →](02-1-3-1-binomial-selection.md)
