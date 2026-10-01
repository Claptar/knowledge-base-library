---
title: "Peccoud & Ycart 1995 — Markovian Modelling of Gene Product Synthesis"
paper: "summary"
source: "https://doi.org/10.1006/tpbi.1995.1027"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Peccoud, J., & Ycart, B. (1995). Markovian Modelling of Gene Product Synthesis. Theoretical Population Biology, 48(3), 222–234. ([original](https://doi.org/10.1006/tpbi.1995.1027)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Markovian Modelling of Gene Product Synthesis

## What this covers

A fully worked-out stochastic model of a single inducible gene switching between "on" and "off"
states and producing protein while it is on — the model now generally called the telegraph model
of gene expression. It speaks to the mathematical biology of gene-expression noise: the paper
derives the exact probability distribution of protein copy number, both as it evolves in time and
at equilibrium, for this process.

## The question

The authors were responding to single-cell experiments (Ko and co-workers, 1990) in which a
reporter gene under an inducible promoter showed large, heterogeneous fluctuations in activity
across genetically identical cells kept in the same, constant concentration of inducer — fluctuations
invisible to bulk in vitro assays, which only report population averages. Ko had modelled this
behaviour by simulating a discrete-time two-state Markov chain for gene activity on a computer.
Peccoud and Ycart ask whether the resulting distribution of protein numbers can instead be obtained
in closed form — for the process as it evolves from a given starting condition, and in its
long-run equilibrium — and whether that closed form lets the model's parameters be estimated from
an observed sample of protein counts, rather than only reproduced in simulation.

## The approach

The gene is represented as a continuous-time two-state Markov chain: inactive to active at rate
$\lambda$, active to inactive at rate $\mu$. While active, protein is synthesised at constant rate
$\nu$ (a birth event); each existing protein copy degrades independently after an exponentially
distributed lifetime, so the total degradation rate when $n$ copies are present is $n\delta$ (a
death event whose rate scales with the population). The combined state is a pair (gene status,
copy number), and its evolution is a birth-and-death process set in a two-state random
environment — the authors call it the IAP process (inactive-active-protein). They write down the
Kolmogorov forward equations for this process and convert them, via probability generating
functions for the two gene states, into a system of partial differential equations. The
no-degradation case ($\delta=0$, where protein count is simply a Poisson process) is solved first
and separately from the general case ($\delta>0$), where the system is singular at the point
needed for the stationary solution and is instead solved by a power-series expansion. That series
is recognised as a case of the (confluent, or degenerate) hypergeometric function.

## What it found

For the no-degradation case, the generating function of protein number at any time $t$ is given
explicitly, along with closed-form expressions for its mean and variance, each decomposing into a
Poisson-type component (as if the gene were permanently active) scaled by the fraction of time the
gene spends active, plus an extra variance term attributable to the gene's own switching noise.
For the general case with degradation, the same quantities are obtained as explicit functions of
time, showing that the distribution converges to a stationary regime with exponential speed, at a
rate set jointly by the gene's switching rate $\lambda+\mu$ and the degradation rate $\delta$. The
stationary distribution's generating function is shown to be a degenerate hypergeometric function,
with stationary mean $\mathbb{E} = \frac{\lambda}{\lambda+\mu}\cdot\frac{\nu}{\delta}$ and a variance with
the same two-part structure as in the transient case. From this closed form, the paper shows that
only three of the model's four parameters ($\lambda$, $\mu$, $\nu$, $\delta$) can be identified from a
sample of the stationary distribution, because rescaling time rescales all four rates together; fixing
$\delta=1$ as the time unit removes the redundancy. Estimators for the remaining three parameters are
then given explicitly, as functions of the ratios of the first three sample factorial moments of
observed protein counts, and shown by the law of large numbers to converge to the true parameter
values as sample size grows.

## Limits and context

The paper states plainly that it does not supply full proofs of ergodicity and the exponential
rate of convergence to the stationary regime, relying instead on general existing theory for
birth-and-death processes in Markovian random environments (work the paper cites by Cogburn and
Torrez) to establish that a stationary regime exists at all; "details of proofs are not given here
for sake of brevity." The authors are explicit that this kind of exact solution is unusual: they
note that explicit solutions to this class of Kolmogorov systems are generally out of reach even in
the stationary case, so the contribution is specific to the tractability of this particular model.
The parameter-estimation scheme assumes the available sample is already drawn from the stationary
regime, since that is the only distribution experimentally accessible in practice, and it cannot
recover the overall time scale (the fourth parameter) without further information. The paper
proposes this estimation method as a route to experimentally validating the model against real
data, but does not itself apply it to an experimental data set.

## Citation

Peccoud, J., & Ycart, B. (1995). Markovian Modelling of Gene Product Synthesis. *Theoretical
Population Biology*, 48(3), 222–234. https://doi.org/10.1006/tpbi.1995.1027

Available via the publisher (Academic Press / Elsevier) at the DOI above; cached copy catalogued in
the knowledge-base-library.
