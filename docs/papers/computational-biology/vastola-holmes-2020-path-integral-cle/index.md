---
title: "Vastola & Holmes 2020 — The chemical Langevin equation: a path integral view of Gillespie's derivation"
paper: "summary"
source: "https://doi.org/10.1103/PhysRevE.101.032417"
licence: "arXiv non-exclusive distribution licence — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Vastola, J. J., & Holmes, W. R. (2020). The chemical Langevin equation: a path integral view of Gillespie's derivation. Physical Review E, 101(3), 032417. ([original](https://doi.org/10.1103/PhysRevE.101.032417)). Rights: arXiv non-exclusive distribution licence — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# The chemical Langevin equation: a path integral view of Gillespie's derivation

## What this covers

A physics paper that reframes Gillespie's 2000 derivation of the chemical Langevin equation (CLE)
from the chemical master equation (CME) in the language of path integrals, for readers in
stochastic chemical kinetics and computational biology who want a precise account of when and why
the CLE approximation holds.

## The question

Gillespie's 2000 paper justified the CLE — a Langevin-equation approximation to the CME — not by
naively truncating the Kramers-Moyal expansion, and not by the usual large-system-volume argument
(as in van Kampen's expansion), but by positing a time scale $\tau$ over which two conditions hold:
propensity functions don't change appreciably (the first leap condition), and each reaction fires
many times (the second leap condition). Path integrals offer a way of thinking about stochastic
processes that is somewhat independent of the differential-equations viewpoint, and are known to be
useful for reasoning about coarse-graining elsewhere (the renormalization group, effective field
theory). The authors ask whether Gillespie's two conditions have a natural path-integral
counterpart, and whether phrasing the CLE derivation this way sheds light on coarse-graining
biochemical systems more generally.

## The approach

Building on their own earlier construction of path integrals for Langevin/Fokker-Planck dynamics,
the authors first build an original path integral representation of the CME itself. They treat the
probability distribution over molecule-count states as a vector in an infinite-dimensional Hilbert
space spanned by basis states for each discrete state, define propensity-function operators, and
assemble a "Hamiltonian" from them whose action reproduces the CME. Slicing the resulting
time-evolution operator into many short time steps, inserting resolutions of the identity between
them, and using an integral representation of the Kronecker delta turns each short-time matrix
element into an integral over a conjugate momentum variable. The result is a path integral over
discrete trajectories through the state space, weighted by an action built from the propensity
functions — distinct from the more familiar Doi-Peliti coherent-state path integral for the same
dynamics.

They then reinterpret Gillespie's two conditions inside this path integral, using the Euler-Maclaurin
formula (which approximates a sum by an integral plus correction terms controlled by derivatives of
the summand) as the central tool. The first leap condition lets them restrict the sum over
trajectories to "dominant paths" — a neighbourhood of each state where propensities and their
derivatives vary negligibly — argue the Euler-Maclaurin correction terms are negligible there, and
so replace sums over discrete states with integrals over continuous ones. The second leap condition
then licenses a second-order Taylor expansion, in the momentum variable, of the exponential term that
appears in the action, turning it into exactly the quadratic (Gaussian) form of an MSRJD
(Martin-Siggia-Rose-De Dominicis) path integral. An MSRJD path integral of that form is already known
to be equivalent to a Langevin/Fokker-Planck description, and matching terms shows the one obtained
here is equivalent to the CLE and its associated chemical Fokker-Planck equation.

For comparison, the authors redo the same conversion by the more traditional route — rewriting the
CME in concentration variables and taking the system volume to infinity — and show that this
corresponds to approximating sums by Riemann sums rather than by the Euler-Maclaurin formula, arriving
at the same quadratic action (with explicit volume factors) and hence the same CLE.

## What it found

- An original, explicit path integral formulation of general CME dynamics, built from
  propensity-operator matrix elements and a momentum-integral representation of the Kronecker delta.
- Gillespie's first leap condition corresponds, in path-integral language, to restricting the sum over
  trajectories to a neighbourhood of dominant paths on which the Euler-Maclaurin correction terms for
  converting sums into integrals are negligible.
- Gillespie's second leap condition corresponds to truncating the action's exponential at second
  order in the conjugate-momentum variable, which is exactly what turns the path integral into the
  Gaussian MSRJD integral equivalent to the CLE / chemical Fokker-Planck equation.
- The large-system-volume derivation of the CLE is, in this language, the same two-step procedure but
  with Riemann sums standing in for the Euler-Maclaurin formula; the two approaches yield the same
  quadratic action term by term (up to volume factors) and so the same CLE.
- The Euler-Maclaurin route is argued to be more broadly applicable than the volume route: it does
  not require the thermodynamic limit (which may fail for crowded, finite-volume biochemical
  systems), does not depend on a well-stirred dilute-gas microphysical picture, and makes explicit the
  integration bounds on the resulting path integral — generally not all of $[0,\infty)^N$ — which the
  volume argument obscures.

## Limits and context

The authors describe their derivation as proceeding "with little mathematical rigor (as is typical in
physics)," though with enough clarity that it could in principle be made precise. They note an
internal tension: the exact CME path integral is derived by taking the elementary time step to zero,
but the final CLE path integral only holds at the coarser, fixed macroscopic time scale $\tau$, so the
CLE path integral is not a strict zero-time-step limit — a further sense in which the CLE remains an
approximation. They flag as open whether Gillespie's conditions could instead be applied directly to
the Doi-Peliti coherent-state path integral, noting that its coherent-state integration variables are
not obviously easy to relate to the state-space integration bounds used here. They also note, without
carrying it out, that the approach should generalize to "hybrid" path integrals in which some
reactions are treated CLE-style and others CME-style, echoing existing partitioned-leaping methods,
and suggest this as a route toward large-deviation results for biochemical systems.

## Citation

Vastola, J. J., & Holmes, W. R. (2020). The chemical Langevin equation: a path integral view of
Gillespie's derivation. *Physical Review E*, 101(3), 032417.
https://doi.org/10.1103/PhysRevE.101.032417
