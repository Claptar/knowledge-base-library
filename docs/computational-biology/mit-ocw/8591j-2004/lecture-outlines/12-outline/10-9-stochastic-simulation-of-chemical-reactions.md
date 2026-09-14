---
title: 9. Stochastic simulation of chemical reactions
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9. Stochastic simulation of chemical reactions

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If _u_ is a random number drawn from a uniform distribution between zero and one, then the following function of _u_ is distributed precisely as τ is in Eq. 20:


This gives us a very simple prescription for numerically simulating the behavior of a stochastic system. Start with some initial condition for each molecule type. If there are _m_ possible types of reactions ( _m_ = 2 for Eq. 2, as there are only creation and destruction events) occuring with rates _ri_ ( _i_ = 1, ..., _m_ ), then we can generate _m_ random variables θ _i_ which are the putative waiting times to the next occurrence of each reaction type. The smallest of these gives the time interval after which the first reaction which will actually occur. At this stage, simply update the variables (for Eq. 2, we would increment _n_ if a creation event occurred, or decrement it if a destruction event occurred), recalculate the rates, and repeat the generation of putative times. Continue this until some convenient time limit is reached. This is how the timecourses in Fig. 1b were generated. To obtain Fig. 1c, simply repeat this procedure several times (2,500 times for Fig. 1b), recording the final state of the system, then calculate the histogram of final states. This procedure is a slight simplification of the Gillespie algorithm.

---

[← 8. Waiting times between reaction events](09-8-waiting-times-between-reaction-events.md) · [Up: contents](index.md) · [10. Spontaneous switching rates in a bistable system →](11-10-spontaneous-switching-rates-in-a-bistable-system.md)
