---
title: Introduction
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/05-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 1.4 Backward Kolmogorov equation

When mutations are less likely, genetic drift dominates and the steady state distributions are peaked at x = 0 and 1. In the limit of µ1 = 0 (or µ2 = 0), Eq. (1.63) no longer corresponds to a well-defined probability distribution, as the 1/x (or 1/(1 − x)) divergence close to x = 0 (or x = 1) precludes normalization. This is the mathematical signal that our expression for the steady state is no longer valid in this limit. Indeed, in the absence of mutations a homogeneous population (all individuals A1 or A2) cannot change through random mating. In the parlance of dynamics these are absorbing states, where transitions are possible into the state but not away from it. In the presence of a single absorbing state, the steady state probability is one at this state, and zero for all other states. If there is more than one absorbing state, the steady state probability will be proportioned (split) among them.

In the absence of mutations, our models of reproducing populations have two absorbing states at x = 0 and x = 1. At long times, a population of fixed number either evolves to x = 0 with probability Π0, or to x = 1 with probability Π1 = 1 − Π0. The value of Π0 depends on the initial composition of the population that we shall denote by 0 < y < 1, i.e. p(x, t = 0) = δ(x − y). Starting from this initial condition, we can follow the probability distribution p(x, t) via the forward Kolmogorov equation (1.35). For purposes of finding the long-time behavior with absorbing states it is actually more convenient to express this as a conditional probability p(x, t|y) that starting from a state y at t = 0, we move to state x at time t. Note that in any realization the variable x(t) evolves from one time step to the next following the transition rates, but irrespective of its previous history. This type of process with no memory is called Markovian, after the Russian mathematician Andrey Andreyevich Markov (1856-1922). We can use this probability to construct evolution equations for the probability by focusing on the change of position for the last step (as we did before in deriving Eq. (1.35)), or the first step. From the latter perspective, we can write


where we employ the same parameterization of the reaction rates as in Eq. (1.30), with δy denoting the change in position. (The second term is the probability that the particle does not move in the initial dt.) The above equation merely states that the probability to arrive at x from y in time t + dt is the same as that of first moving away from y by δy in the initial interval of dt, and then proceeding from y + δy to x in the remaining time t (first term). The second term corresponds to staying in place in the initial interval dt. (Naturally we have to integrate over all allowed intermediate positions.) Expanding both sides of Eq. (1.65) gives


15

Using the normalization condition for R(δy, y) and the definitions of drift and diffusion coefficients from Eqs. (1.36) and (1.37), we obtain


which is known as the backward Kolmogorov equation. If the drift velocity and the diffusion coefficient are independent of position, the forward and backward equations are the samemore generally one is the adjoint of the other.

---

[Up: contents](index.md) · [1.4.1 Fixation probability →](02-1-4-1-fixation-probability.md)
