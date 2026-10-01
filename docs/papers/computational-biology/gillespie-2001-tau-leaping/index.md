---
title: "Gillespie 2001 — Approximate accelerated stochastic simulation of chemically reacting systems"
paper: "summary"
source: "https://doi.org/10.1063/1.1378322"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Daniel T. Gillespie, "Approximate accelerated stochastic simulation of chemically reacting systems," Journal of Chemical Physics 115(4), 1716-1733 (2001). ([original](https://doi.org/10.1063/1.1378322)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Approximate accelerated stochastic simulation of chemically reacting systems

## What this covers

Introduces "tau-leaping," a way to speed up stochastic simulation of chemical reaction networks, for
readers in stochastic chemical kinetics and computational systems biology who need to simulate
well-stirred reacting systems faster than the exact Stochastic Simulation Algorithm (SSA) allows.

## The question

The author's own SSA is an exact procedure for generating trajectories of the chemical master
equation, and it is the right tool whenever small molecular populations make the deterministic
reaction rate equation (RRE) unreliable. Its drawback is speed: because it simulates one reaction
event at a time, it can require an enormous number of steps to cover a modest span of system time,
especially when some species are abundant even while others are not — a situation common inside
cells. The question is whether a deliberate, controlled sacrifice of simulation detail can buy a
large gain in speed without discarding the stochastic effects that motivated using SSA at all.

## The approach

The central device is the "Leap Condition": choose a time increment $\tau$ small enough that no
propensity function (the instantaneous reaction-firing rate) changes appreciably over $[t,t+\tau)$,
yet large enough that many reaction events occur in that interval. Under this condition, the number
of times each reaction channel fires during the leap is, to good approximation, an independent
Poisson random variable with mean given by the propensity times $\tau$, so the simulation can sample
those firing counts directly and jump the state forward, instead of generating every individual
event. The paper shows this "tau-leap" method sits at the centre of a hierarchy of approximations:
when each leap spans very many firings, it reduces to an existing diffusion approximation, the
chemical Langevin equation, which in turn reduces, as the system grows still larger, to the
conventional deterministic RRE — so SSA, the Langevin method, and the RRE appear as limiting cases
of one leaping procedure. A simple rule is proposed for selecting the largest tau consistent with
the Leap Condition, governed by one tolerance parameter, with a built-in fallback to exact SSA
stepping whenever the proposed leap would not actually be larger than an SSA step. A refinement,
the "estimated-midpoint" technique (modelled on the midpoint rule for numerical integration),
evaluates the propensities at an estimated midpoint state of the leap rather than at its start,
intended to reduce a systematic bias the plain method otherwise shows. A related alternative,
"k_alpha-leaping," leaps by a fixed number of firings of one chosen reaction channel instead of a
fixed time interval, using gamma- rather than Poisson-distributed random numbers.

## What it found

The methods are demonstrated on two small test systems rather than validated broadly. For a single
isomerization reaction starting from $10^5$ molecules, plain tau-leaping with a modest tolerance
matched the exact SSA trajectory using 305 leaps in place of 100,000 individual reaction events.
Pushing the tolerance higher for more speed (66 leaps) produced a visible systematic bias in the
plain method's leap-size distribution; the estimated-midpoint technique removed that bias while
needing only 70 leaps — roughly a fourfold increase in usable leap size for the same accuracy,
checked against the exact distribution available analytically for this simple reaction. For a
three-reaction, three-species decaying-dimerization system, exact SSA needed 526,692 steps; plain
tau-leaping reached comparable terminal populations in 459 leaps, and a hybrid strategy — applying
the estimated-midpoint correction only while one reaction channel dominated the total propensity —
cut this further to 289 leaps while also curing a spurious transient instability that the
estimated-midpoint method introduced when used throughout the run. The k_alpha-leap variant gave
comparable speed and accuracy on the same examples. Across these cases the ratio of leap count to
exact event count was under 1/1000, though the author stresses this is not a real wall-clock
speedup figure, since one leap costs more to execute than one SSA step and the code was not tuned
for efficiency.

## Limits and context

The author repeatedly frames the results as preliminary. The rule given for choosing $\tau$ is
described as only "a very modest first step toward a more robust optimal control strategy," not a
finished solution. Why the estimated-midpoint technique corrects bias in one test system but
destabilizes another is left unexplained. No general strategy yet exists for deciding when and how
aggressively to leap, and the paper states plainly that until one is developed, "the tau-leap
method cannot be considered ready for practical application." The single-trajectory comparisons
shown are not a substitute for the systematic statistical validation — comparing simulated state
histograms against the master equation's predictions over many repeated runs — that the author says
is still needed. Open implementation questions include whether faster Poisson generators or
alternative k-value sampling schemes would help, and how the method might extend to larger networks
such as genetic regulatory systems or chemical oscillators. It positions tau-leaping as filling a
gap between exact molecular simulation, the chemical Langevin equation, and the deterministic rate
equation, closing explicitly with "the present work is only a beginning."

## Citation

Daniel T. Gillespie, "Approximate accelerated stochastic simulation of chemically reacting systems,"
*Journal of Chemical Physics* 115(4), 1716–1733 (2001). https://doi.org/10.1063/1.1378322. Available
from the publisher (AIP Publishing) or via institutional/library access; cached copy at
`knowledge-base-library/sources/papers/gillespie-2001-tau-leaping/`.
