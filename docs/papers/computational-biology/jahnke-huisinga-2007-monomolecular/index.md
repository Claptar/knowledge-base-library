---
title: "Jahnke & Huisinga 2007 — Solving the chemical master equation for monomolecular reaction systems analytically"
paper: "summary"
source: "https://doi.org/10.1007/s00285-006-0034-x"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Jahnke, T., & Huisinga, W. (2007). Solving the chemical master equation for monomolecular reaction systems analytically. Journal of Mathematical Biology, 54(1), 1-26. ([original](https://doi.org/10.1007/s00285-006-0034-x)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Solving the chemical master equation for monomolecular reaction systems analytically

## What this covers

How to write down the *exact* probability distribution solving the chemical master equation (CME)
for a well-stirred mixture of molecular species, in the case where every reaction is monomolecular
(conversion, inflow/production, or outflow/degradation). It speaks to stochastic chemical kinetics
and to the numerical analysis of Markov jump processes used to model gene expression and similar
biochemical networks.

## The question

The CME tracks the full probability distribution over molecule-count states of a reacting mixture,
and in principle captures everything the stochastic simulation algorithm (Gillespie's SSA) samples
from indirectly. But the CME is a linear ODE system with one equation per *state*, and the number
of states grows exponentially with the number of species and molecule counts — even a system of
three species with counts up to 99 already has on the order of $10^6$ coupled equations. Because of
this, almost all practical work solves the CME only indirectly, by simulating many trajectories of
the jump process rather than solving the distribution itself. Exact solutions were known only in
narrow special cases: closed linear systems started from a multinomial distribution, or open linear
systems started from a product Poisson distribution. Nothing was known for the practically
important case of a deterministic initial condition (a fixed starting molecule count), which is
neither multinomial nor Poisson. The authors set out to close that gap for the broad class of
monomolecular reaction networks, and to do so for arbitrary initial distributions.

## The approach

The key structural fact about purely monomolecular reactions is that the fate of each individual
molecule present at time zero, and each molecule later injected by an inflow reaction, evolves
independently of all the others — a molecule's type can change over time, but it never interacts
with or depends on any other molecule. This lets the authors split the full population into
disjoint subsets by origin: one subset per species present at $t=0$, plus one subset for all
molecules created later by inflow reactions. Because monomolecular dynamics keep these subsets
statistically independent, the joint distribution of the whole system is the convolution of the
distributions of the subsets.

Each of the initial-condition subsets starts as a point mass concentrated on one molecule of one
species, and the paper first shows (extending an existing result for multinomial initial data) that
such a subset's distribution stays multinomial for all time, with the multinomial parameter vector
evolving according to the ordinary differential equation used in traditional, deterministic
reaction-rate kinetics. The inflow subset starts empty and is shown to stay Poisson-distributed,
again with its parameter vector evolving by a reaction-rate-type ODE. Combining these two pieces
(their main result, Theorem 1) gives the exact CME solution for any deterministic initial condition
as a convolution of one product-Poisson distribution and $n$ multinomial distributions, all built
from time-dependent parameter vectors that solve ordinary differential equations of exactly the
same form as the classical, low-dimensional reaction-rate equations. An arbitrary initial
probability distribution is then handled by superposition, since the CME is linear.

## What it found

The main theorem gives, for the first time, a closed-form solution of the monomolecular CME valid
for arbitrary (including deterministic) initial conditions, reducing an exponentially large linear
system to a handful of low-dimensional ODEs — one $n$-dimensional linear ODE for the Poisson
parameter and $n$ more for the multinomial parameters, each the size of the number of species. The
structured, convolution form lets many properties of the full solution be read off directly:
marginal distributions over subsets of species have the same convolution form in lower dimension;
the mean and covariance of the molecule-number vector follow explicit formulas built from the same
parameter vectors, and the mean is shown to coincide with the classical reaction-rate-equation
solution; and the long-time behaviour is characterized exactly — a closed system (no inflow)
converges to a multinomial steady state (generically non-unique, depending on the initial
distribution, though it can also be Poisson for special initial data), while an open system (with
inflow) always converges to a unique product Poisson steady state, matching and generalizing known
results about first-order reaction networks. Two worked examples — a single-species
production/degradation system and a two-species isomerization — show the formulas reproducing known
binomial and Poisson transient and stationary distributions from the literature. A further
proposition extends the approach to the single-species autocatalytic reaction $S \to S+S$ in
isolation, giving a solution that is a shifted negative binomial distribution.

## Limits and context

The result is restricted to monomolecular reaction networks (conversion, production from a source,
and degradation); it explicitly does not cover bimolecular or higher-order reactions, nor
autocatalytic or splitting reactions combined with monomolecular ones in the same network — the
paper shows the isolated autocatalytic case can be solved but states plainly that a system mixing
autocatalysis with production, conversion or degradation reactions is "beyond the scope" of their
results, offering only the expectation that the true solution must interpolate between Poisson,
binomial and negative binomial forms. The steady-state analysis additionally assumes constant
reaction rates and an irreducible rate matrix, so it does not characterize long-time behaviour for
time-dependent rates or decomposable networks. The authors frame the result's significance mainly
as a benchmark and a stepping stone: a known, nontrivial exact solution for testing new numerical
CME solvers, and a potential source of basis functions (Galerkin-type ansatz functions) for
numerical methods aimed at the harder bimolecular case, rather than as a method intended to replace
stochastic simulation for general reaction networks.

## Citation

Jahnke, T., & Huisinga, W. (2007). Solving the chemical master equation for monomolecular reaction
systems analytically. *Journal of Mathematical Biology*, 54(1), 1–26.
https://doi.org/10.1007/s00285-006-0034-x. Available via Springer (J. Math. Biol.) and through the
knowledge-base library's paper cache.
