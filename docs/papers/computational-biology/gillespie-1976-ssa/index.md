---
title: "Gillespie 1976 — A General Method for Numerically Simulating the Stochastic Time Evolution of Coupled Chemical Reactions"
paper: "summary"
source: "https://doi.org/10.1016/0021-9991(76)90041-3"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Daniel T. Gillespie, "A General Method for Numerically Simulating the Stochastic Time Evolution of Coupled Chemical Reactions," Journal of Computational Physics, Vol. 22, Issue 4, pp. 403-434 (1976). ([original](https://doi.org/10.1016/0021-9991(76)90041-3)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# A General Method for Numerically Simulating the Stochastic Time Evolution of Coupled Chemical Reactions

## What this covers
This paper introduces the Stochastic Simulation Algorithm (SSA, the "Gillespie algorithm") -- an
exact Monte Carlo procedure for simulating the time evolution of a well-mixed system of chemical
species undergoing coupled reactions, within the stochastic rather than deterministic formulation
of chemical kinetics. It speaks to computational chemistry, and later computational systems
biology, wherever small molecule counts or a chemical instability make deterministic rate
equations unreliable.

## The question
Deterministic chemical kinetics describes a reacting system with coupled ordinary differential
equations for species concentrations, treating reaction constants as rates. This works when
molecule numbers are large, but was known to break down for systems with few molecules of some
species, or near chemical instabilities with multiple steady states, where fluctuations and
correlations between species change the qualitative behaviour. The rigorous alternative treats the
system as a continuous-time Markov process on molecule counts, governed by a master equation for
the joint probability of all species populations -- essentially always analytically intractable,
and impractical to solve numerically, since its state space is a combinatorially large lattice.
Gillespie's problem was to find an exact way to generate correct trajectories of the process
without ever writing down the master equation, and without the finite time-step approximation that
introduces error and can destabilise numerical solution of stiff rate equations.
He also wanted to settle a dispute over whether the stochastic formulation has
independent physical legitimacy or is merely an ad hoc rewriting of the deterministic one.

## The approach
The paper starts from one "fundamental hypothesis": each reaction channel has a parameter $c_\mu$
such that $c_\mu\,dt$ is the probability that a particular combination of its reactant molecules
reacts in the next infinitesimal interval $dt$. Gillespie justifies this physically for a
hard-sphere bimolecular reaction from molecular collision theory, and argues it holds whenever
non-reactive molecular collisions occur much more often than reactive ones, keeping the system
well mixed.

From that hypothesis he derives, without invoking the master equation, a "reaction probability
density function": the joint probability that the next reaction anywhere in the volume occurs
after a given waiting time and is of a given type. This has an exact exponential form, proved fully
equivalent to the master equation. The algorithm repeatedly draws a random waiting time and
reaction type from this density, advances the clock, updates the molecule counts by that
reaction's stoichiometry, and recomputes the rates before repeating -- one exact realisation of
the process with no time discretisation anywhere. Two equivalent ways of making the draw are
given: a "direct method" (an exponential waiting time set by the total rate, then a weighted choice
of reaction type) and a "first-reaction method" (tentatively schedule every channel, keep whichever
fires first); the direct method uses only two random numbers per step against one per channel for
the other, so is more efficient once there are more than a few channels. A worked four-species,
six-reaction example with a short Fortran routine demonstrates the method concretely.

## What it found
The algorithm is exact: it reproduces the master-equation process with no approximation beyond the
quality of the random number generator, stores only of order $N + 2M$ numbers, and uses no
integration time step. Computation scales with the number of reaction events that actually occur
rather than with an imposed step size, so there is no counterpart to the instability that
finite-difference solution of stiff rate equations can suffer.

On the dispute over the stochastic formulation's physical status, Gillespie argues his parameter
$c_\mu$ rests on firmer physical ground than the conventional rate constant $k_\mu$: for ordinary
systems with large molecule numbers the two agree, with $k_\mu$ proportional to $c_\mu$ (worked out
for the hard-sphere bimolecular case), so either can be used. It is specifically near chemical
instabilities, or with small molecule counts, that the correlations and fluctuations the stochastic
approach captures become important and the deterministic equations cannot be trusted. He also
shows an existing heuristic "hybrid" scheme by Bunker and co-workers is effectively an
approximation to his own method, replacing the random waiting time by its mean, now placed on a
rigorous footing.

## Limits and context
Gillespie is explicit that the paper establishes the algorithm's validity only in principle: no
numerical case study of a specific system is carried through, left to subsequent publications. He
identifies random-number-generator quality as the main source of inaccuracy, and notes
cost scales with the number of reaction events simulated, so system size and duration are tied to
computer speed. He sketches a possible, admittedly premature, extension to spatially inhomogeneous
systems by dividing the volume into well-mixed subvolumes linked by diffusive-transfer reactions.
He reiterates that for most macroscopic systems, ignoring fluctuations and correlations is
legitimate, resting on prior thermodynamic-limit results by Oppenheim et al. and by Kurtz showing
the two formulations coincide as molecule numbers and volume grow together; the stochastic
algorithm is offered as most valuable where that limit does not apply, not as a universal
replacement for deterministic kinetics.

## Citation
Daniel T. Gillespie, "A General Method for Numerically Simulating the Stochastic Time Evolution of
Coupled Chemical Reactions," *Journal of Computational Physics*, Vol. 22, Issue 4, pp. 403-434
(1976). DOI: https://doi.org/10.1016/0021-9991(76)90041-3. Available via the publisher
(ScienceDirect) or the library catalogue entry for this source.
