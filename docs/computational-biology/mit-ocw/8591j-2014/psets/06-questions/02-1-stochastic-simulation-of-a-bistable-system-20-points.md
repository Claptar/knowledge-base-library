---
title: 1 Stochastic simulation of a bistable system (20 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/06-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Stochastic simulation of a bistable system (20 points)

**Source:** `psets/06-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In class and in the previous problem set we have begun exploring the consequences of stochasticity. We showed that because of stochasticity, identical systems can evolve dierently in time despite having the same initial conditions. (This behavior is in stark contrast to the dierential equations models we explored earlier in the course.)

The master equation oers an exact description of the time evolution of the probability distribution of the system. However, solving the master equation for all but the simplest systems is fairly dicult (even if we are just talking about the steady state). We showed that it is possible (and reasonable) to approximate the master equation at intermediate particle numbers by neglecting particle discreteness. This approximation is called the Fokker-Planck equation. By the end of this exercise you will learn to apply the Fokker-Planck equation to explore and gain intuition for more complicated systems.

Our playground will be the bistable system considered in problem 3 of Problem Set 2. We showed that the dynamics of the protein _X_ were governed by the following dierential equation:


Set _γ_ = 1 _, K_ 1 _K_ 2 = 10<sup>_−_4</sup> _, v_ 0 = 12 _._ 5 _, v_ 1 = 200 _._ (These parameter values lead to a bistable system.)

- a. Sketch by hand the shape of the production and the degradation terms on the same plot. Indicate the location of the stable xed points on the plot. (No need to be fancy here.)

- b. Calculate the values of X that correspond to the stable xed points.

- c. Write explicitly the expression for the potential of the system as derived from the FokkerPlanck equation. Specically, what are _f_ ( _n_ ) and _g_ ( _n_ ) ? Don't forget to indicate the limits on the integral. (Page 61-62 of the supplementary notes Stochastic Chemical Kinetics by Alexander van Oudenaarden, which is listed under Lecture 10 reading, may prove useful).

- d. The potential can be thought of as the potential energy of the system. Systems attempt to minimize their potential energy (i.e., basketballs roll downhill not vice-versa), seeking the state corresponding to the local minimum of potential energy. Noise can excite a system (make the basketball temporarily roll uphill) and as a result the system may end jumping between local minima.

   1. Plot the potential for the parameter values introduced above.

   2. Is the plot consistent with the idea that the system is bistable?

   3. Compare your results to the values of X calculated in part b.

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 6

- e. Temporarily, set _K_ 1 _K_ 2 = 1 , and re-plot the potential of the system. Based on the plot of the potential would you say that the system is monostable or bistable?

Now, set _K_ 1 _K_ 2 back to its original value: 10<sup>_−_4</sup> .

- f. **COMPUTATION** Perform a stochastic simulation of this system to show that the expression level intermittently switches between the two stable states.

- g. Use the simulation data to estimate the fraction of time that the system spends in each stable state.

- h. In the notes the following expression is given for _p_ ( _n_ ) :


1. On a log-log scale plot _f_ + _g_ vs. _n_ and also _e_<sup>_−ϕ_</sup> vs. _n_ . Which of the two aects the probability distribution more? Is it fair to say that _p_ ( _n_ ) _∝ e_<sup>_−ϕ_</sup> ?

2. Approximate the value of the constant A. (Useful functions: quad on matlab or NIntegrate on Mathematica.)

3. Calculate the fraction of time you expect to see the system in each stable state and compare it to the result you got from your simulation.

---

[← Problem Set 6](01-problem-set-6.md) · [Up: contents](index.md) · [2 Life at low Reynolds number (10 points) →](03-2-life-at-low-reynolds-number-10-points.md)
