---
title: '$convergence ## [1] 0 ## ## $message ## NULL'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit11-optim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $convergence ## [1] 0 ## ## $message ## NULL

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here’s an online graphical illustration of Nelder-Mead.

This is the default in _optim()_ in R, however it is relatively slow, so you may want to try one of the alternatives, such as BFGS.

### **5.8 Simulated annealing (SA) (optional)**

Simulated annealing is a _stochastic_ descent algorithm, unlike the deterministic algorithms we’ve already discussed. It has a couple critical features that set it aside from other approaches. First, uphill moves are allowed; second, whether a move is accepted is stochastic, and finally, as the iterations proceed the algorithm becomes less likely to accept uphill moves.

Assume we are minimizing a negative log likelihood as a function of _θ_ , _f_ ( _θ_ ).

The basic idea of simulated annealing is that one modifies the objective function, _f_ in this case, to make it less peaked at the beginning, using a “temperature” variable that changes over time. This helps to allow moves away from local minima, when combined with the ability to move uphill. The name comes from an analogy to heating up a solid to its melting temperature and cooling it slowly - as it cools the atoms go through rearrangements and slowly freeze into the crystal configuration that is at the lowest energy level.

Here’s the algorithm. We divide up iterations into stages, _j_ = 1 _,_ 2 _, . . ._ in which the temperature variable, _τj_ , is constant. Like MCMC, we require a proposal distribution to propose new values of _θ_ .

1. Propose to move from _θt_ to _θ_<sup>˜</sup> from a proposal density, _gt_ ( _·|θt_ ), such as a normal distribution centered at _θt_ .

2. Accept _θ_<sup>˜</sup> as _θt_ +1 according to the probability min(1 _,_ exp(( _f_ ( _θt_ ) _− f_ ( _θ_<sup>˜</sup> )) _/τj_ ) - i.e., accept if a uniform random deviate is less than that probability. Otherwise set _θt_ +1 = _θt_ . Notice that for larger values of _τj_ the differences between the function values at the two locations are reduced (just like a large standard deviation spreads out a distribution). So the exponentiation smooths out the objective function when _τj_ is large.

3. Repeat steps 1 and 2 _mj_ times.

29

4. Increment the temperature and cooling schedule: _τj_ = _α_ ( _τj−_ 1) and _mj_ = _β_ ( _mj−_ 1). Back to step 1.

The temperature should slowly decrease to 0 while the number of iterations, _mj_ , should be large. Choosing these ’schedules’ is at the core of implementing SA. Note that we always accept downhill moves in step 2 but we sometimes accept uphill moves as well.

For each temperature, SA produces an MCMC based on the Metropolis algorithm. So if _mj_ is long enough, we should sample from the stationary distribution of the Markov chain, exp( _−f_ ( _θ_ ) _/τj_ )). Provided we can move between local minima, the chain should gravitate toward the global minima because these are increasingly deep (low values) relative to the local minima as the temperature drops. Then as the temperature cools, _θt_ should get trapped in an increasingly deep well centered on the global minimum. There is a danger that we will get trapped in a local minimum and not be able to get out as the temperature drops, so the temperature schedule is quite important in trying to avoid this.

A wide variety of schedules have been tried. One approach is to set _mj_ = 1 _∀j_ and _α_ ( _τj−_ 1) = 1+ _τaτj−j_ 1 _−_ 1<sup>for a small</sup><sup>_a_.For a given problem it can take a lot of experimentation to choose</sup><sup>_τ_0 and</sup><sup>_m_0</sup> and the values for the scheduling functions. For the initial temperature, it’s a good idea to choose it large enough that exp(( _f_ ( _θi_ ) _− f_ ( _θj_ )) _/τ_ 0) _≈_ 1 for any pair _{θi, θj}_ in the domain, so that the algorithm can visit the entire space initially.

Simulated annealing can converge slowly. Multiple random starting points or stratified starting points can be helpful for finding a global minimum. However, given the slow convergence, these can also be computationally burdensome.

---

[← $par ## [1] 0 0 ## ## $value ## [1] 0 ## ## $counts ## function gradient ## 77 NA](09-value-1-0-counts-function-gradient-77-na.md) · [Up: contents](index.md) · [6 Basic optimization in R →](11-6-basic-optimization-in-r.md)
