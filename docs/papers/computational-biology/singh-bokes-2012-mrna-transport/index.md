---
title: "Singh & Bokes, 2012 — Consequences of mRNA Transport on Stochastic Variability in Protein Levels"
paper: "summary"
source: "https://doi.org/10.1016/j.bpj.2012.07.015"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Singh, A., and P. Bokes. 2012. Consequences of mRNA Transport on Stochastic Variability in Protein Levels. Biophysical Journal 103(5):1087-1096. ([original](https://doi.org/10.1016/j.bpj.2012.07.015)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Consequences of mRNA Transport on Stochastic Variability in Protein Levels

## What this covers

A stochastic-modelling paper asking how the nuclear export of pre-mRNA shapes cell-to-cell
variability in mRNA and protein levels, within the systems-biology study of gene-expression noise.

## The question

Transcriptional bursting -- cells making several mRNA copies per promoter-firing event -- is a
major source of expression noise. In eukaryotes, newly made pre-mRNA has to be processed and
exported from the nucleus before it becomes functional cytoplasmic mRNA, and measured export times
(minutes to about an hour) can be comparable to mRNA turnover rates. The authors ask whether this
export step is itself a buffer that protects protein levels from transcriptional bursts, and set
out to get an exact description of the underlying stochastic process -- rather than a
variance-only or simulation-based account -- covering nuclear pre-mRNA, cytoplasmic mRNA and
protein together.

## The approach

They build a chemical master equation for a minimal model: a promoter fires in bursts of random
size to produce nuclear pre-mRNA, pre-mRNA leaves the nucleus as a first-order reaction at rate
$\gamma_e$ (modelling the unknown nuclear residence time as exponentially distributed, the
opposite limit from a fixed delay), cytoplasmic mRNA degrades at rate $\gamma_c$, and mRNA is
translated into protein which degrades at rate $\gamma_p$. Rather than simulating the system, they
convert the master equation into a probability-generating function, then into a
factorial-cumulant-generating function, and solve the resulting first-order PDE by the method of
characteristics. This yields an exact integral representation for the steady-state joint
distribution of nuclear and cytoplasmic mRNA counts, specialised to the case of geometrically
distributed burst sizes. A Fourier-transform numerical recipe is used to turn the generating
function into actual probability distributions for plotting. Separately, they derive the linear
ODEs for the first and second moments (mean, variance, covariance, and cytoplasmic mRNA
autocorrelation), and extend the moment analysis to include translation and protein degradation to
get a closed-form expression for steady-state protein noise (variance over mean squared).

## What it found

The exact distribution recovers two known limits: a negative binomial for cytoplasmic mRNA when
export is fast, and a Poisson distribution when export is very slow (pre-mRNA pools up in the
nucleus and trickles out). For intermediate export rates the distribution interpolates between
these, and slowing export visibly narrows and thins the tail of the cytoplasmic mRNA distribution
-- a direct noise reduction at the mRNA level. However, slowing export also lengthens the
mRNA autocorrelation time substantially; in one illustrated case (1-hour mRNA half-life),
lengthening the export half-life from about a minute to an hour roughly doubles how long
fluctuations persist. These two effects pull in opposite directions at the protein level and
largely cancel: in a representative high-bursting regime (mean burst size 100 transcripts, mean
mRNA count 500, mean protein count 10,000), the same change in export half-life that cuts mRNA
variability by about 50% reduces protein noise by only about 2%. A closed-form approximation for
protein noise in the regime where export is fast relative to protein turnover ($\gamma_e \gg
\gamma_p$) shows it is essentially insensitive to the export rate. The transient response of the
model to a single transcriptional burst shows the same pattern: fast versus slow export changes
the height and shape of the cytoplasmic mRNA peak but leaves the protein peak almost unchanged.
The authors conclude that nuclear pre-mRNA export can substantially reduce stochastic variability
in mRNA counts arising from transcriptional bursting, but, under physiologically plausible
parameters, it does not reduce -- and is largely unable to reduce -- the resulting noise in
protein levels.

## Limits and context

The result rests on modelling nuclear residence as an exponentially distributed (memoryless)
delay; the authors note explicitly that a deterministic, fixed-duration delay is the opposite
limiting case and would not affect steady-state protein noise at all, so the finding is tied to
this choice of delay distribution. The model also assumes pre-mRNA is stable in the nucleus (no
nuclear degradation) and deliberately excludes any feedback onto the export process itself, such as
saturation of nuclear pore complexes -- a mechanism the authors note (citing prior work) can
suppress transcriptional noise at the protein level when it operates, but which available
experimental imaging of pore-RNA interactions shows no sign of under normal conditions, so they
argue it is unlikely to be the active mechanism in practice. The paper states the conclusion that
protein noise is invariant to export rate holds specifically when export is fast relative to
protein turnover -- a condition the authors judge very likely to hold given measured protein and
export timescales, but they flag as unresolved, for further theoretical or experimental work,
exactly how robust this protein-noise invariance is more generally and what other regulatory
mechanisms might filter transcriptional noise at the export step.

## Citation

Singh, A., and P. Bokes. 2012. Consequences of mRNA Transport on Stochastic Variability in Protein
Levels. *Biophysical Journal* 103(5):1087-1096. https://doi.org/10.1016/j.bpj.2012.07.015. Paper on
file in the library repository's sources cache.
