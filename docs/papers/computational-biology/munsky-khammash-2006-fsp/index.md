---
title: "Munsky & Khammash 2006 — The finite state projection algorithm for the solution of the chemical master equation"
paper: "summary"
source: "https://doi.org/10.1063/1.2145882"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Brian Munsky and Mustafa Khammash, "The finite state projection algorithm for the solution of the chemical master equation," The Journal of Chemical Physics 124, 044104 (2006). ([original](https://doi.org/10.1063/1.2145882)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# The finite state projection algorithm for the solution of the chemical master equation

## What this covers

A numerical method for solving the chemical master equation (CME) directly, rather than by sampling
trajectories — relevant to stochastic chemical kinetics and systems biology wherever molecule counts
are too small for deterministic rate equations to be trusted.

## The question

The CME gives the exact time evolution of the probability distribution over all possible molecular
population states of a well-mixed, constant-volume reaction system, but for all but the simplest
systems it cannot be solved in closed form. The standard workaround, Gillespie's stochastic
simulation algorithm (SSA), generates individual sample trajectories and estimates the distribution
by averaging many runs — but an accurate probability can require very large numbers of runs, and
this becomes prohibitive when the quantity of interest is a rare event. The motivating example is the
Pap epigenetic switch in *E. coli*, whose ON-switching rate is of order $10^{-4}$ per cell per
generation; resolving it to 1% relative accuracy by simulation alone was estimated to need more than
$10^6$ SSA runs. Faster time-leaping methods ($\tau$-leaping) advance many reactions at once but
degrade badly when propensities change quickly or populations are very small — exactly the regime of
interest. The authors set out to compute the probability density vector (pdv) itself, without
simulating any trajectories, while quantifying how much error any truncation of the problem
introduces.

## The approach

The CME can be written as a linear ODE $\dot{\mathbf{P}}(\mathbf{X};t) = \mathbf{A}\cdot
\mathbf{P}(\mathbf{X};t)$ over the (generally infinite) state space of population vectors, where
$\mathbf{A}$ is built from the reaction propensities and stoichiometries. When the reachable space is
finite it can be solved exactly via the matrix exponential. When it is infinite or too large, the
authors truncate to a finite subset $J$, lumping everything else into a single absorbing state. They
prove that enlarging $J$ can only increase the probability mass it captures (monotonic convergence),
and that if the mass captured by $J$ at the final time of interest is at least $1-\epsilon$, the
truncated solution bounds the true pdv both above and below, with the gap no more than $\epsilon$.
This gives a solution together with a guaranteed, computable certificate of its error, rather than
only an estimate whose own accuracy is uncertain, as with Monte Carlo sampling. These results are
assembled into the finite state projection (FSP) algorithm: start from an initial set of states,
compute the trapped probability mass over the time horizon, and if it falls short of $1-\epsilon$,
add more states — using reachability within $k$ reaction steps from the initial condition, in the
worked example — and repeat. For a system whose true reachable space is finite, or for which a
sufficiently accurate finite approximation exists, the authors show this loop terminates in a finite
number of steps.

## What it found

The method is demonstrated on two versions of a model of the Pap operon switch. In the first, a
four-state submodel with LRP and PapI held fixed, the state space is already finite, so FSP gives the
exact pdv directly from one matrix exponential; the SSA, run $10^4$ times, approximated the
probability of the "production" configuration with relative errors up to about 19%, and even at
$10^6$ runs retained errors as high as 0.6%, while FSP computed its answer in a fraction of a second.
In the second, more realistic version, PapI is produced and degraded stochastically so the state
space is genuinely infinite; FSP truncates it while guaranteeing the retained probability mass to
within $10^{-6}$ (124 states in the worked case). Applied to estimating the probability that the
switch has turned ON, FSP bounded that probability to $[1.376, 1.383]\times10^{-4}$ — a guaranteed
relative width below 0.5% — in under four seconds, whereas $10^5$–$10^6$ independent SSA runs gave
relative errors from about $-35\%$ to $+30\%$ and took tens of seconds to minutes; adaptive explicit
$\tau$-leaping performed comparably poorly, since the frequent binding/unbinding reactions and small
populations restrict leap sizes to barely more than single SSA steps, eliminating its usual speed
advantage. Across both examples, FSP outperformed both Monte Carlo methods in accuracy and
computational cost, with the gap widest for the rare, biologically important event (switching ON).

## Limits and context

The authors are explicit that FSP in this basic form is not yet feasible for every class of system:
when a species has a high probability of large excursions in a short time, the required finite state
set can become very large, forcing exponentiation of correspondingly large matrices — a genuine
computational challenge for which they point to future remedies (Krylov subspace methods, lower-order
approximations, state aggregation and multiscale partitioning) that are described as being developed
rather than demonstrated here. The paper deliberately does not compare FSP against partition-based
methods such as the slow-scale SSA, arguing the comparison is unnecessary since similar partitioning
ideas could, in principle, speed up FSP too. It also exercises FSP only on a simplified Pap submodel
(four operon configurations, rather than the full 64-configuration model mentioned as already
explored elsewhere), stating that the aim here is solely to illustrate the algorithm, not to give a
complete biological account of the switch.

## Citation

Brian Munsky and Mustafa Khammash, "The finite state projection algorithm for the solution of the
chemical master equation," *The Journal of Chemical Physics* 124, 044104 (2006).
DOI: [10.1063/1.2145882](https://doi.org/10.1063/1.2145882). Available via AIP Publishing /
J. Chem. Phys.
