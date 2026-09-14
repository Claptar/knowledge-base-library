---
title: 2 Noise induced oscillations in predator-prey dynamics (24 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/10-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Noise induced oscillations in predator-prey dynamics (24 points)

**Source:** `psets/10-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As we saw in class, the Lotka-Volterra predator-prey dynamics leads to neutral cycles. In this problem, we will see how, in a predator-prey system that has a stable fxed point, demographic fuctuations alone can cause sustained oscillations<sup>1</sup> .

Consider a system of _n_ predator and _m_ prey individuals, with a total carrying capacity (prey + predator) _N_ . \e will denote the state of the system as _S_ ( _n, m_ ) . The following processes occur

> 1Predator-Prey Cycles from Resonant Amplifcation of Demographic Stochasticity, Phys. Rev. Lett. 94, 218102

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 10

in this population:


The expressions on top of the arrows are the rates at which these processes occur. \e will call this the individual based model, as opposed to the deterministic model that you will derive below.

a. [3 points] \hat do each of the processes, and the parameters _d_ 1 , _d_ 2 _, p_ 1 , _p_ 2 , _b_ represent?

- b. [7 points] Master equation formulation:

   1. \rite down the master equation for this system.

   2. Show that the normalized means, _f_ 1 =<sup>_<u><n></u>_</sup> _N , f_ 2 =<sup>_<u><m></u>_</sup> _N_ , satisfy the equations shown below. You can do this by multipling<sup>_dP_</sup><sup><u>(</u></sup> _dt_<sup>_n,m_</sup><sup><u>)</u></sup> by _n_ , _m_ respectively, and then summing over all _n_ , _m_ for each case. Assume higher order correlations are negligible, i.e. _(nm)_ = _(n) (m)_ . \hat are _r, K, p_ in terms of the parameters defned above?


Notice that this equation is like the Lotka-Volterra equations incorporating an efective carrying capacity _K_ for the prey. \e will call this the deterministic model.

- c. [6 points] Stability analysis:

   1. \hat are the fxed points in the deterministic model? \hat is their stability?

   2. Does the system oscillate (limit cycle or neutral) about any of the fxed points?

   - =

   - 3. If the interior fxed point ( _f_ 1 _, f_ 2 0 ) is neutrally stable, what is the oscillation frequency? If not, what is the frequency of transient oscillations around the fxed point?

- d. [10 points] **COMPUTATION** <mark>S</mark> tochastic simulations of the individual based model:

   1. Set _d_ 1 = 0 _._ 1 _, d_ 2 = 0 _._ 05 _, b_ = 0 _._ 1 _, p_ 1 = 0 _._ 25 _, p_ 2 = 0 _._ 05 _, N_ = 3000 . \ill the corresponding deterministic model show transient oscillations with these parameter values? If yes, what is their frequency?

   2. The resonant frequencies from the deterministic model amplify demographic noise, so that the frequency of oscillations in the individual based model is close to the frequency of transients you see in the deterministic model. To see this, perform a Gillispie simulation of the individual based model. Plot the timeseries of the prey and predator number as a function of time. Do you see oscillations?

2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 10

3. Plot the Fourier transform of either the predator or the prey population timeseries, and mark the resonant frequency. Does it agree with part (a) of this subquestion?

4. Now choose the parameters appropriately so that the interior fxed point has purely real eigenvalues and repeat the simulation. Plot the Fourier transform and comment on the result.

5. To see how the amplitude of oscillations scales with the population size, run the above simulations with parameters from part 1 for _N_ = 300 _,_ 3000 _,_ 30000 . Plot the amplitude against _N_ on a log-log scale. The slope gives the powerlaw co-efcient _β_ of the scaling relation _A ∝ N_<sup>_β_</sup> . \hat is _β_ ?

---

[← Problem Set 10 (70 points)](01-problem-set-10-70-points.md) · [Up: contents](index.md) · [3 Critical Transitions: Allee efect and bifurcation diagram (15 points) →](03-3-critical-transitions-allee-efect-and-bifurcation-diagram-1.md)
