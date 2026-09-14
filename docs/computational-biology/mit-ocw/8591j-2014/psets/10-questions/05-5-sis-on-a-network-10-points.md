---
title: 5 SIS on a Network (10 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/10-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 SIS on a Network (10 points)

**Source:** `psets/10-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

SIS (Susceptible-Infectious-Susceptible) is an epidemic model in which there are two species: Susceptible (S) and Infectious (I). Let's study this model on a network, where each node of the network is occupied by some individuals.

- a. Let's defne _St_ and _It_ as the population densities of susceptible and infectious individuals on the nodes of a random network, at time _t_ . _pI_ is the probability for a susceptible individual to be infected by a neighboring infectious individual. Show that, on average, the probability _Pt_ for a susceptible individual (randomly picked from the network) to be infected at time _t_ is:

_Pt_ = 1 _− exp_ ( _−pIIt (d)_ ) _,_

where _(d)_ is the average degree of a node, and we assume that the degree follows a Poisson distribution. (Hint: the probability of being infected is one minus the probability of not being infected.)

- b. Assume that _It_ + _St_ = _ρ_ at any time _t_ (in unit of generations). If _pR_ is the probability for an infectious individual to recover and become susceptible again in a generation, write down the expression for _It_ +1 as a function of _It_ .

- c. In the infnite-time limit, we can assume that _It_ = _It_ +1 = _I∞_ . Under what condition is _I∞_ = 0 no longer stable? In this case, a nonzero fraction of the population are infected and the system is in the endemic state. \hat is the threshold value of _ρ_ that leads to the transition? Comment on how the threshold depends on _(d)_ .

4

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4 Time is Discrete: logistic map and chaos (9 points)](04-4-time-is-discrete-logistic-map-and-chaos-9-points.md) · [Up: contents](index.md)
