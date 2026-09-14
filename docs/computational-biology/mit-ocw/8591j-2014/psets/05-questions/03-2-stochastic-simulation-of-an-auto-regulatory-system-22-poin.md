---
title: 2 Stochastic simulation of an auto-regulatory system (22 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Stochastic simulation of an auto-regulatory system (22 points)

**Source:** `psets/05-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem you will learn how to implement a stochastic simulation. You will also use the simulation to unveil the role of negative auto-regulation in reducing fuctuations.

a. Consider a simple diferential equation that describes the rate of change of some molecule _x_ :


\hat is the solution of the diferential equation? Let's assume _β_ = 6 , _α_ = 3 and the initial condition _x_ ( _t_ = 0) = _x_ 0 .

- b. Unfortunately, the solution of the diferential equation is deterministic and fails when fuctuations become important. Specifcally, when the system has reached the steady state, the deterministic solution says that _x_ will no longer change. But if _x_ were to describe a real mRNA, then _x_ should fuctuate about its mean value, since translation and degradation are stochastic processes. Consistency with reality requires a stochastic description that respects both the probabilistic nature of events and the discreteness of molecule numbers. From now

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 5

on, _x_ will represent the molecule numbers instead of molecule concentration, and the reaction rates ( _β_ and _αx_ ) will be regarded as probabilities per unit time of an reaction taking place. _β_ will be the probability per unit time of the creation of a molecule _x_ , and _αx_ will be the probability per unit time of the degradation of a molecule _x_ . So let's start by returning to the actual underlying reactions:


   1. Consider a system that has _x_ 0 = 3 at time _t_ = 0 . \hat is the probability that the system will transition to the state _x_ = 2 during the next transition? (i.e., what is the probability that degradation occurs before transcription?)

   2. \hich aspect of the stochastic process does the deterministic diferential equation describe successfully?

- c. Let's consider how to perform stochastic simulations of chemical reactions. A rather inefcient (and potentially inaccurate) method to perform the stochastic simulation is by determining what process takes place during infnitesimal time intervals _dt_ . Say the system starts at the state _x_ 0 = 3 . The simulation examines what happens during the frst "infnitesimal" time interval _dt_ = 10<sup>_−_10</sup> . The probability of degradation is _pdeg_ = _αx ×_ 10<sup>_−_10</sup> = 9 _×_ 10<sup>_−_10</sup> while the probability of transcription is _ptrans_ = _β ×_ 10<sup>_−_10</sup> = 6 _×_ 10<sup>_−_10</sup> . A random number _m_ is drawn from a uniform distribution between 0 and 1 . \hat happens next depends on the value of _m_ as follows:

(1) If _m < pdeg →_ one molecule of _x_ is degraded, reaction rates are updated and the simulation proceeds to the next time step.

(2) If _pdeg < m < pdeg_ + _ptrans →_ one molecule of _x_ is transcribed, reaction rates are updated and the simulation proceeds to the next time step.

(3) If _pdeg_ + _ptrans < m →_ nothing happens and the simulation proceeds to the next time step.

A better way to approach the simulation is using Gillespie's "frst-reaction" method. This method is much more efcient and is analytically exact. The main idea is to determine which of the two competing processes (degradation or transcription) takes place frst and at what time it occurs. Gillespie shows that you can do it in the following manner: for each process ( _i_ ) generate a waiting time ( _τi_ ) from the probability distribution ( _Pi_ ( _τi_ ) ): _Pi_ ( _τi_ ) = _ki_ exp[ _−kiτi_ ] . The process that occurs frst is the one with the shorter waiting time. The time at which it occurs is just the waiting time.

Sketch an algorithm for simulating stochastic reactions using Gillespie's method. In this case we are dealing with only one species, the output of a simulation run should be the number of molecule at diferent time points.

## d. **COMPUTATION** Now consider the following two systems:

System A: a system in which protein X is expressed constitutively. In a deterministic setting, the concentration of X would evolve according to


2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 5


System B: a system in which protein X represses its own synthesis. In a deterministic setting, it would evolve according to


Problem 2d Image and problem courtesy of Alexander van Oudenaarden. Used with permission.

1. Compute the fxed points of the deterministic systems and their stability.

2. In the following, we will interpret the reaction rates as probabilities per unit time of an reaction taking place, as we discussed in b). Based on the algorithm that you sketch in c), implement a discrete stochastic simulation for System A, for both _A_ = 10 and _A_ = 100 . \ithout loss of generality, we set _γ_ = 1 . \e can also measure volume in units of cell size, thus concentrations are equivalent to molecule numbers.

   - i. Plot a time series of your simulation results. Compare it to the numerical solution of the corresponding diferential equation.

   - ii. Run the system for a long enough time so that it has reached a steady state. Plot a histogram of _x_ . Verify that the variance and mean of the steady state distribution are consistent with Poisson statistics.

3. For System B, set _K_ = 100 and choose B such that _(x)_ = 100 is a steady state. Implement a discrete stochastic simulation to demonstrate that the variance of the auto-regulatory system is lower than that of the constitutive system given the same mean.

---

[← 1 Waiting times for chemical reactions (8 points)](02-1-waiting-times-for-chemical-reactions-8-points.md) · [Up: contents](index.md) · [05 questions Part 04 — →](04-05-questions-part-04.md)
