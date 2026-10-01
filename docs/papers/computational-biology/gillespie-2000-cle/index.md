---
title: "Gillespie 2000 — The chemical Langevin equation"
paper: "summary"
source: "https://doi.org/10.1063/1.481811"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Daniel T. Gillespie, "The chemical Langevin equation," Journal of Chemical Physics, Vol. 113, No. 1, pp. 297–306 (1 July 2000). ([original](https://doi.org/10.1063/1.481811)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# The chemical Langevin equation

## What this covers

This paper, in stochastic chemical kinetics, derives an approximate Langevin-type (continuous,
noisy) equation for how molecular population numbers evolve in a well-stirred chemical reaction
system, starting from the same microphysical assumption that underlies the exact chemical master
equation.

## The question

The chemical master equation (CME) exactly describes a well-stirred reacting mixture, but it is
generally unsolvable, and the exact Monte Carlo method built on it (the stochastic simulation
algorithm) tracks every individual reaction event, which can be slow. Several groups — van Kampen,
Grossmann, Kubo/Matsuo/Kitahara — had proposed continuous diffusion-type (Langevin or
Fokker-Planck) approximations to the underlying jump process, reached by different routes
(a system-size expansion, a fluctuation-dissipation argument, a bare truncation of a series
expansion of the master equation), and Gillespie describes the resulting literature as a "confused
history" of attempts to find a limiting Fokker-Planck form. A numerical study by Baras, Malek
Mansour and Pearson had found that one such Langevin equation disagreed with master-equation and
molecular-dynamics results for a system with multiple stable states, which read as evidence against
Langevin approximations in chemical kinetics generally. Gillespie's question is when, and why, a
Langevin approximation to the CME is actually justified — derived from the same first principles as
the master equation itself, rather than a deterministic law with noise added afterward.

## The approach

Starting from the propensity function that also generates the CME, Gillespie asks how many times
each reaction channel fires during a time increment $\tau$. If $\tau$ is short enough that no
propensity function changes appreciably during it (condition i), the reaction counts in that
interval are independent Poisson random variables. If $\tau$ is also long enough that each
channel's expected number of firings is much greater than one (condition ii), each Poisson variable
is well approximated by a normal random variable with the same mean and variance. Applying both
approximations together, for any interval that satisfies both conditions at once, gives an update
formula for the population numbers that is linear in the interval and in independent Gaussian noise
terms scaled by its square root — the chemical Langevin equation. Letting that interval become
formally infinitesimal yields a white-noise stochastic differential equation, with the
corresponding Fokker-Planck equation for the probability density following as a direct consequence.
The central move is to make the validity of the approximation depend on these two dynamical
conditions holding over some interval, rather than on the value of a fixed system-size parameter
such as the container volume — and to note that whether they hold can change from moment to moment
within a single system.

## What it found

The resulting chemical Langevin equation is the same equation studied earlier by Kurtz, and
Gillespie shows it is distinct from the Langevin equation often attributed to Grossmann, which
builds its noise terms around the deterministic solution via a fluctuation-dissipation argument, and
from van Kampen's system-size expansion. The deterministic reaction rate equation of conventional
chemical kinetics is recovered from the chemical Langevin equation only in a further limit where the
random terms become negligible next to the deterministic drift, and the standard rule of thumb that
relative population fluctuations scale as the inverse square root of population size falls directly
out of the Poisson-variance step used in the derivation. Revisiting the Baras, Malek Mansour and
Pearson result, Gillespie argues that it demonstrates the failure of the Grossmann-type equation
specifically — whose noise terms are known to misbehave near multiple stable states — not of the
Langevin formalism derived here. He also notes that their system held a fixed total molecule count
of 2000 across three time-varying species, so it is plausible that at least one species' population
was at times too small for condition (ii) to hold, which would independently rule out any Langevin
approximation regardless of its form.

## Limits and context

Gillespie states that satisfying both conditions will "nearly always" require large molecular
populations, but argues the deciding factor is the existence of a macroscopically infinitesimal
timescale over which propensities stay effectively constant while every channel still fires many
times, not the size of any population or volume parameter as such. He acknowledges that for some
systems no such timescale may exist during certain periods, in which case the Langevin or
Fokker-Planck approximation must be abandoned in favour of the exact master equation or direct
stochastic simulation, and that continually verifying the two conditions is not straightforward in
practice. He sets aside the thermodynamic-limit question of whether the chemical Langevin equation's
concentration process converges to the deterministic rate-equation solution as Kurtz had already
addressed it, and as having little practical importance for the finite, finite-time systems — such
as reactions inside a living cell with populations sometimes below 100 — that motivate this work.
The paper's own stated motivation is a broader effort to find faster approximate alternatives to
exact stochastic simulation, with results from that effort left to future work.

## Citation

Daniel T. Gillespie, "The chemical Langevin equation," *Journal of Chemical Physics*, Vol. 113,
No. 1, pp. 297–306 (1 July 2000). DOI: [10.1063/1.481811](https://doi.org/10.1063/1.481811).
Available from the publisher (American Institute of Physics / AIP Publishing) and catalogued in the
knowledge-base-library.
