---
title: '4 Time is Discrete: logistic map and chaos (9 points)'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/10-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Time is Discrete: logistic map and chaos (9 points)

**Source:** `psets/10-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**COMPUTATION** The logistic map is a great example of how complex, chaotic dynamics can arise from simple nonlinear equations. The logistical model in population dynamics is a description of population growth in the presence of overcrowding. The diferential equation for logistic growth

3

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 10

is<sup>_<u>dN</u>_</sup> _dt_ = _rN_ (1 _− K_<sup>_<u>N</u>_</sup> ) , where _N_ is the population size, _r_ is the rate of reproduction and _K_ is the carrying capacity. In this problem, we will explore its version in discrete time, i.e. a diference equation, the logistic map:

_xt_ +1 = _Rxt_ (1 _− xt_ )

- a. [2 points] Set _R_ = 2 , _x_ 0 = 0 _._ 2 . Plot _x_ vs. _t_ for 20 time steps. Then make a similar plot for _x_ 0 = 0 _._ 99 . \hat kind of behavior do you observe with diferent initial poplation size ( _x_ 0 between 0 and 1)?

- b. [1 point] Set _R_ = 3 _._ 1 , _x_ 0 = 0 _._ 2 . Plot _x_ vs. _t_ for 20 time steps. How is the trajectory diferent from the previous simulation?

- c. [1 point] Set _R_ = 3 _._ 5 , _x_ 0 = 0 _._ 2 . Plot _x_ vs. _t_ for 20 time steps. \hat is the oscillation period now?

- d. [2 points] Find a value of _R_ which gives an oscillation period equal to 8.

- e. [3 points] In dynamical systems theory, each of these transitions is called a period-doubling bifurcation. However, as we continue increasing _R_ , deterministic chaos occurs. Set _R_ = 4 . Plot _x_ vs. _t_ for 80 time steps, with _x_ 0 = 0 _._ 2 and _x_ 0 = 0 _._ 2000000001 . Plot the two trajectories on the same graph and compare them. Do you observe "sensitive dependence on initial conditions"?

---

[← 3 Critical Transitions: Allee efect and bifurcation diagram (15 points)](03-3-critical-transitions-allee-efect-and-bifurcation-diagram-1.md) · [Up: contents](index.md) · [5 SIS on a Network (10 points) →](05-5-sis-on-a-network-10-points.md)
