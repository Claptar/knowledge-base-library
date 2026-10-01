---
title: "Gardiner & Chaturvedi 1977 — The Poisson Representation. I. A New Technique for Chemical Master Equations"
paper: "summary"
source: "https://doi.org/10.1007/BF01014349"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Gardiner, C. W., & Chaturvedi, S. (1977). The Poisson Representation. I. A New Technique for Chemical Master Equations. Journal of Statistical Physics, 17(6), 429–468. ([original](https://doi.org/10.1007/BF01014349)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# The Poisson Representation. I. A New Technique for Chemical Master Equations

## What this covers

This paper introduces a technique for solving chemical master equations — the exact stochastic
description of molecule-number fluctuations in reacting systems — by expanding the probability
distribution as a (possibly complex-valued) superposition of Poisson distributions. It speaks to
nonequilibrium statistical mechanics and stochastic chemical kinetics.

## The question

By the mid-1970s, fluctuations in chemical reactions were handled either heuristically, via
Langevin equations whose noise strength was assumed Gaussian and fixed by equilibrium
fluctuation-dissipation arguments, or exactly but awkwardly, via the master equation itself,
attacked by van Kampen's system-size expansion or cumulant methods. None of the exact routes were
easy to use in practice, especially with several reacting and diffusing species, and the Langevin
route was not obviously valid away from equilibrium. The authors wanted a method converting a
master equation into a Fokker–Planck or stochastic differential equation *exactly*, not as an
approximate by-product of a large-volume limit, and tractable for multivariable, spatially
extended systems.

## The approach

They represent the probability distribution over molecule numbers as an integral of multivariate
Poisson distributions weighted by a function $f$ of continuous auxiliary variables — the "Poisson
representation." Substituting this ansatz into the master equation and integrating by parts turns
it into a Fokker–Planck equation for $f$ with no approximation: reactions of at most bimolecular
order give drift and diffusion terms only, and general reactions give derivatives of some higher
but finite order. The device that makes this work is that $f$ is a *quasiprobability*: it can be
negative or complex, and its natural integration domain can be a contour in the complex plane
rather than the real line, yet its moments equal exactly the factorial moments of the true
molecule-number distribution. The authors first show, from statistical mechanics alone, that ideal
reacting systems in thermodynamic equilibrium (grand canonical ensemble) always have exactly
Poissonian steady states, which motivates the Poisson basis generally. Where the Fokker–Planck
equation is second order, it is converted, via the Itô formalism, into an equivalent stochastic
differential equation solvable iteratively as a power series in the inverse square root of system
volume, giving a systematic asymptotic expansion of moments. For reactions with trimolecular steps,
which produce higher-order Fokker–Planck equations, they extend this with a new "higher-order
noise" source — apparently not attempted before, and tolerable only because quasiprobabilities need
not stay positive.

## What it found

Ideal reacting systems at thermodynamic equilibrium have exactly Poissonian steady-state
distributions, recovering the law of mass action along the way. Any reversible reaction with a
single pathway, and any reaction obeying detailed balance, also reaches a Poissonian steady state,
and the authors give an example where this holds even without detailed balance, with a net
probability flux still present. For purely bimolecular reactions, the exact Fokker–Planck noise
term vanishes whenever the deterministic rate equations reach steady state, again forcing a
Poissonian limit. Worked examples — a linear reversible reaction, a bimolecular second-order phase transition
model, a reaction with a negative diffusion coefficient, and a trimolecular model — reproduce
results obtained previously by other methods (agreeing with McNeil and Walls, and with Mori and
McNeil's critical dimension of $4$ for a reaction-diffusion phase transition) and extend them with
exact moment formulas in confluent hypergeometric and Bessel functions. Diffusion between spatial cells, being linear, contributes no noise of its own: all
stochasticity comes from the chemical step, unlike conventional Langevin treatments where diffusion
also adds noise. The Gaussian (linearized)
approximation holds almost everywhere except near critical points; for the spatial
phase-transition model it stays valid for dimension $d>4$ even arbitrarily close to the critical
point, but breaks down for $d<4$, where corrections to the concentration variance diverge as cell
size shrinks. Higher-order noise, worked out for the trimolecular example, affects the skewness but
contributes negligibly to the mean and variance at leading orders in the volume expansion.

## Limits and context

The authors flag the higher-order noise construction as heuristic, introduced because no prior
theory existed for it, and say giving it a rigorous footing is work for mathematicians, not done
here. The continuum limit of their cell-based treatment of spatial diffusion gives a
second-order correction to the mean concentration that diverges as cell size shrinks for spatial
dimension below four (logarithmically at exactly four); they call this "disturbing," trace it to
the artificial locality built into the cell model, and state that fixing it needs a more
microscopic, nonlocal account of diffusive reaction that they do not supply. They also note the integration contour defining the quasiprobability is not always unique,
that the wrong choice gives a finite but inadmissible solution, and that picking the right one
needs a separate analyticity argument, carried out case by case in an appendix rather than as a
general rule. The method is restricted to master equations with finitely separated states and polynomial
transition rates. The paper argues against treating Langevin-style Gaussian noise and the
system-size expansion as the general or sufficient tools for nonequilibrium reaction fluctuations,
positioning its exact Fokker–Planck derivation as a replacement rather than a supplement. A
companion paper, Part II, is said to treat two-time correlation functions, outside this paper's
scope.

## Citation

Gardiner, C. W., & Chaturvedi, S. (1977). The Poisson Representation. I. A New Technique for
Chemical Master Equations. *Journal of Statistical Physics*, 17(6), 429–468.
https://doi.org/10.1007/BF01014349
