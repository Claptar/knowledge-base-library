---
title: "Shahrezaei & Swain 2008 — Analytical distributions for stochastic gene expression"
paper: "summary"
source: "https://doi.org/10.1073/pnas.0803850105"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Vahid Shahrezaei and Peter S. Swain, "Analytical distributions for stochastic gene expression," Proceedings of the National Academy of Sciences 105(45):17256-17261 (2008), correction in PNAS 106(1):346 (2009). ([original](https://doi.org/10.1073/pnas.0803850105)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Analytical distributions for stochastic gene expression

## What this covers

A method for computing the full probability distribution of protein copy numbers under stochastic
gene expression, not just its mean and variance, for the standard two-stage (transcription,
translation) and three-stage (promoter switching, transcription, translation) reaction models used
across systems biology.

## The question

Master equations for gene expression are easy to write down but, beyond the mean and variance,
almost never solvable in closed form, so most predictions compared to single-cell data were limited
to first and second moments. The authors wanted an analytical handle on the whole distribution,
because the shape of a protein-number distribution (symmetric or skewed, unimodal or bimodal) carries
information that summary statistics discard, and because moments are hard to estimate reliably from
real, often asymmetric, experimental samples.

## The approach

The key observation is a separation of timescales: in most cells protein molecules live much longer
than the mRNAs that encode them. Writing $\gamma$ for the ratio of protein to mRNA degradation rates,
the authors take the limit $\gamma \gg 1$ and treat the mRNA population as equilibrating fast
compared to protein turnover. Working with the generating function of the joint mRNA/protein master
equation, they solve the resulting first-order PDE by the method of characteristics in this limit,
which eliminates mRNA as an explicit variable. The result has a direct biological reading: each mRNA,
before it decays, spawns a geometrically distributed "burst" of proteins, because translation and
degradation compete as first-order processes on the ribosome-bound transcript. Replacing the fast
mRNA dynamics with this burst-size distribution yields a one-variable effective master equation for
protein number alone. Solving it gives a negative binomial steady-state distribution for the simpler
two-stage model, and a distribution built from a Gauss hypergeometric function for the three-stage
model with promoter switching; a time-dependent solution is derived as well. Predictions are checked
against Gillespie stochastic simulations, with the Kullback-Leibler divergence between analytical and
simulated distributions used to quantify where the large-$\gamma$ approximation holds.

## What it found

The two-stage model's protein number distribution is exactly negative binomial at steady state, and
this reduces to a known gamma-distribution limit for large copy numbers, recovering earlier mean/
variance results as a special case. The three-stage model's distribution can be unimodal, monotonically
decreasing, or bimodal with peaks at both zero and a nonzero protein number — the authors stress this
bimodality is a signature of slow, discrete promoter switching rather than necessarily reflecting an
underlying bistable biochemical network. Comparison against simulation shows the approximation already
works well for $\gamma$ of order 10 and degrades for $\gamma$ near 1, with accuracy quantified via
Kullback-Leibler divergence. A noise (coefficient-of-variation squared) decomposition separates a
Poisson-like term, a term scaling as $1/\gamma$ from residual mRNA fluctuations, and a term set by the
promoter's on/off switching noise. Using genome-wide mRNA and protein half-life data from budding
yeast, the authors show that roughly 80% of about 1,962 yeast genes have $\gamma > 1$ (median
$\gamma \approx 3$), supporting the approximation's relevance in practice; grouping genes by Gene
Ontology class, they find proteins involved in complex assembly (e.g., structural and nucleotidyl-
transferase activities) tend to have high median $\gamma$, while transcription factors have low
median $\gamma$ (around 1), and across all yeast genes there is a small but statistically significant
negative correlation between total expression noise and $\gamma$ (rank correlation about $-0.2$,
$P \approx 10^{-6}$).

## Limits and context

The derivation explicitly requires $\gamma \gg 1$ and, for the time-dependent solution, times
$\tau \gg 1/\gamma$ for mRNA to have reached quasi-steady-state; the paper shows numerically where
this breaks down rather than claiming universal validity. The authors caution against reading a
bimodal protein distribution in the three-stage model as evidence of bistability in the underlying
chemistry, since slow promoter switching alone reproduces it. They argue, without fully resolving it,
that fitting full distributions (ideally through a Bayesian or maximum-likelihood framework) is more
informative and more robust than fitting only means and standard deviations, since real distributions
are often asymmetric and not locally Gaussian. They also note that mean and variance alone, or even the
full distribution, may not be sufficient to uniquely determine which biochemical mechanism (two-stage
versus three-stage) generated the data, and that non-steady-state dynamics or extrinsic noise sources
can further complicate the comparison — time-series data, not just snapshot distributions, may be
needed to discriminate between mechanisms. The approach is presented as one instance of a more general
strategy for simplifying stochastic systems by eliminating a fast variable in favor of a time-dependent
effective parameter on the slow variable.

## Citation

Vahid Shahrezaei and Peter S. Swain, "Analytical distributions for stochastic gene expression,"
*Proceedings of the National Academy of Sciences* 105(45):17256-17261 (2008), with a correction to
Eq. 13 published in *PNAS* 106(1):346 (2009). https://doi.org/10.1073/pnas.0803850105. Available via
PNAS (open access) and PubMed Central.
