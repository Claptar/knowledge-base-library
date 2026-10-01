---
title: "23. Peptide-Level Models for Summarization"
course: "StatOmics Sga21"
chapter: 23
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Peptide-Level Models for Summarization

## What this covers

Once a mass-spec search has produced peptide intensities, a protein-level differential-abundance
test needs one value per protein per sample — so the many peptide measurements for a protein have
to be collapsed into one. This chapter asks whether the way you do that collapsing matters, using
the same CPTAC UPS1 spike-in benchmark used elsewhere in the course (a known true log2 fold change
for the spiked human proteins and a known true fold change of zero for the yeast background) to
compare summarization strategies against each other rather than against a single pipeline. It then
opens up *why* one of them wins, by fitting an explicit linear model to the peptides of a single
protein. It assumes the `QFeatures` import/log/filter/normalize workflow and the `msqrob2`
model-and-contrast pattern (`~condition`, `makeContrast`, `hypothesisTest`) used throughout this
course, and the CPTAC A-vs-B spike-in design (0.25 vs 0.74 fmol UPS1 protein/µL, true log2 fold
change $\log_2(0.74/0.25)\approx1.57$) as background.

Two different data sets appear below. The three-way method comparison uses a small subset built
for exactly this purpose — a single lab, two spike-in conditions (A and B) — so the same known
truth used elsewhere is available to grade each method against. The worked example that follows it
switches to the full study: three labs and five spike-in concentrations (A–E, at 0.25, 0.74, 2.22,
6.67 and 20 fmol UPS1 protein/µL), restricted afterwards to one protein in one lab, so that more
than two concentration levels are visible at once.

## Three ways to turn peptides into a protein value

For one lab, two-condition subset of the CPTAC data, the same protein set can be quantified three
different ways, and each is carried through the identical downstream pipeline — `msqrob(~condition)`
fit per protein, then a `conditionB = 0` contrast tested for every protein — so that only the
summarization step differs between them:

1. **maxLFQ.** The protein intensities are read directly from MaxQuant's `proteinGroups.txt`,
   already summarized peptide-to-protein by MaxQuant's own maxLFQ algorithm before the data ever
   reach R.
2. **Median summarization.** The peptide-level table (`peptides.txt`) is imported, log-transformed,
   filtered (resolving overlapping protein groups, removing decoys and contaminants, and requiring
   at least two observations per peptide) and median-centered per sample exactly as in the
   protein-level workflow, then rolled up to one value per protein per sample by taking the
   **median** of its peptides' log2 intensities: `aggregateFeatures(..., fun =
   matrixStats::colMedians)`.
3. **Robust summarization.** The same cleaned, normalized peptide table is instead rolled up with
   `aggregateFeatures`'s default aggregation function, which fits a **robust** (outlier-resistant)
   model per protein rather than taking a simple central tendency — the mechanism behind this is
   unpacked in the next section.

## The result: robust wins on both power and false-discovery control

Running the identical protein-level model and contrast on all three summaries and comparing the
resulting volcano plots and estimated fold changes gives a clear ranking, read directly off the
data:

- **Robust summarization** has the highest power of the three (finds the most true positives) while
  still controlling the false discovery rate well: of the proteins it calls significant, the
  observed false discovery proportion is $\text{FDP} = 1/20 = 0.05$, in line with the target level.
- **Median summarization** gives **biased** log fold-change estimates for the spiked-in proteins —
  its estimates systematically miss the known true value, $\log_2(0.74/0.25)\approx1.57$.
- **maxLFQ** gives **more variable** log fold-change estimates for the spiked-in proteins than
  either of the peptide-level approaches — its estimates scatter more widely around the truth.

The comparison is made visually with a boxplot: the estimated log fold change for every protein is
split by method (maxLFQ / median / robust) and by whether the protein is a UPS1 spike-in or a yeast
background protein, with two reference lines drawn in — $0$, the true value for background
proteins, and $\log_2(0.74/0.25)$, the true value for the spiked proteins. Robust summarization is
the one whose spiked-protein estimates sit tightest around the upper reference line; median's sit
off it (biased); maxLFQ's are the most spread out around it (variable). This is the empirical case
for reaching for a peptide-level, outlier-resistant summary rather than a plain median or an
already-summarized maxLFQ value — the next section works out mechanically why.

## Why the naive summaries are biased: one protein under the microscope

To see *why* a median or a mean can go wrong, the lecture zooms in on a single protein — the
spiked-in complement C5 standard, `P01031ups|CO5_HUMAN_UPS` — restricted to the samples from one
lab (lab 3) of the full, five-concentration study, and plots every peptide's log2 intensity in
every sample.

<figure>
<svg viewBox="0 0 400 250" role="img" aria-label="Peptide intensity profiles for two samples of one protein, showing a peptide missing only from the low-abundance sample">
  <line x1="50" y1="200" x2="360" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <text x="70" y="216" font-size="11" text-anchor="middle" fill="currentColor">pep 1</text>
  <text x="160" y="216" font-size="11" text-anchor="middle" fill="currentColor">pep 2</text>
  <text x="250" y="216" font-size="11" text-anchor="middle" fill="currentColor">pep 3</text>
  <text x="340" y="216" font-size="11" text-anchor="middle" fill="currentColor">pep 4</text>
  <text x="14" y="125" font-size="11" fill="currentColor" transform="rotate(-90 14 125)">log2 intensity</text>

  <polyline points="70,60 160,95" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.85"/>
  <polyline points="160,95 340,80" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="2 4" opacity="0.35"/>
  <circle cx="70" cy="60" r="4" fill="currentColor"/>
  <circle cx="160" cy="95" r="4" fill="currentColor"/>
  <circle cx="340" cy="80" r="4" fill="currentColor"/>
  <text x="345" y="76" font-size="12" fill="currentColor">A (low spike)</text>

  <polyline points="70,35 160,68 250,150 340,52" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.85"/>
  <circle cx="70" cy="35" r="4" fill="currentColor"/>
  <circle cx="160" cy="68" r="4" fill="currentColor"/>
  <circle cx="250" cy="150" r="4" fill="currentColor"/>
  <circle cx="340" cy="52" r="4" fill="currentColor"/>
  <text x="345" y="48" font-size="12" fill="currentColor">B (high spike)</text>

  <circle cx="250" cy="182" r="5" fill="none" stroke="#d2691e" stroke-width="1.8" stroke-dasharray="2 2"/>
  <text x="250" y="234" font-size="11" text-anchor="middle" fill="#d2691e">peptide 3: NA in A</text>
</svg>
<figcaption>Schematic of the mechanism: each peptide of one protein ionizes with its own
characteristic efficiency (the zig-zag shared by both sample traces — the "peptide effect").
Peptide 3 ionizes poorly, so in the low-abundance sample (A) its true signal falls below the
detection limit and is recorded as missing, while the higher overall abundance in sample B lifts it
just into range. A median or mean taken over whichever peptides happen to be observed then averages
a different mixture of peptides in A than in B, pulling B's summary down and biasing the estimated
difference between the two samples.</figcaption>
</figure>

**Median summarization**, drawn as a horizontal line per sample against this peptide-by-sample
scatter, is visibly a poor estimate of the true protein expression value. It does not account for
differences in *peptide effects*: different peptides ionize with different efficiency, giving each
one a characteristic intensity offset that has nothing to do with the protein's true abundance.
Because peptides that ionize poorly are picked up in samples with high spike-in concentration but
not in samples with low spike-in concentration, the set of peptides actually averaged differs from
sample to sample — and this introduces a bias.

**Mean summarization** is really the same idea stated as a linear model, and it inherits the same
problem. Fitting

$$
y_{ip} = \beta_i^\text{sample} + \epsilon_{ip}
$$

— a sample effect only, no term for which peptide $p$ produced the measurement — is equivalent to
averaging whatever peptides were observed for sample $i$. With no peptide term in the model, an
unbalanced mix of observed peptides across samples still biases $\hat\beta_i^\text{sample}$ exactly
as the median does.

## Correcting for the peptide effect with a linear model

The fix is to give the peptide effect its own term, so that it can be estimated and subtracted out
rather than left to contaminate the sample effect:

$$
y_{ip} = \beta_i^\text{sample}+\beta^\text{peptide}_{p} + \epsilon_{ip}
$$

Fitting this model (ordinary least squares) to the same peptide data produces per-sample effects
$\hat\beta_i^\text{sample}$ that are corrected for exactly which peptides happen to be present in
each sample — and, plotted alongside the median and mean summaries, they show a much better
separation of the samples by spike-in concentration. Median and mean summarization, which ignore
the peptide effect, are shown to systematically **overestimate** protein expression in the small
spike-in conditions and **underestimate** it in the large spike-in conditions — exactly the
direction the mechanism above predicts, since it is the high-concentration samples that pick up
extra, low-ionizing peptides that the low-concentration samples do not.

Still, this ordinary-least-squares fit is not perfect. A residual plot — each peptide's leftover
$\hat\epsilon_{ip}$ after fitting sample and peptide effects — shows some large outliers for one
particular peptide, `KIEEIAAK`. Its intensities do not line up well with the spike-in
concentration, and this induces a visible bias in the summarized values for some of the samples
(the higher-concentration conditions D and E).

## Down-weighting outliers: robust summarization by M-estimation

Ordinary least squares chooses $\beta$ to minimize the sum of *squared* residuals,

$$
\text{OLS}: \sum_{i,p} \epsilon_{ip}^2 = \sum_{i,p}\left(y_{ip}-\beta_i^\text{sample}-\beta_p^\text{peptide}\right)^2,
$$

which means a single badly-behaved peptide like `KIEEIAAK` can pull the fitted sample effects
around, because a large residual contributes to the objective in proportion to its *square*. Robust
summarization replaces this with **M-estimation**: minimize a weighted sum of squared residuals,

$$
\sum_{i,p} w_{ip}\,\epsilon_{ip}^2 = \sum_{i,p} w_{ip}\left(y_{ip}-\beta_i^\text{sample}-\beta_p^\text{peptide}\right)^2,
$$

where the weight $w_{ip}$ for each observation is calculated from its own *standardized* residual —
observations that look like outliers relative to the bulk of the data get a smaller weight; weights
close to that of a well-behaved residual get a weight close to $1$. Because the weights depend on
the residuals, and the residuals depend on the fit, the model is fit **iteratively**: fit, compute
weights from the resulting residuals, refit with those weights, and repeat until the fit stops
changing (`MASS::rlm`, using Huber's weight function). Plotting the weight against the standardized
residual shows the shape directly: flat at $1$ near zero, then falling off for large residuals in
either direction — exactly what is needed to automatically down-weight `KIEEIAAK`'s contribution
without having to identify and remove it by hand. Refitting with these weights produces a clearly
better separation between samples by spike-in concentration than the plain (unweighted) peptide-
level model did.

This is the mechanism behind the black-box "robust summarization" step used, without derivation,
elsewhere in the course (`MsCoreUtils::robustSummary()`): a peptide-level linear model with a
peptide effect, fit by iteratively reweighted least squares so that a handful of anomalous peptide
measurements cannot dominate the estimated sample effect.

## Other summarization strategies, named but not detailed

The lecture points at, without working through, three further ways this same peptide-to-protein
step is handled elsewhere:

- **maxLFQ** — MaxQuant's own built-in summarization algorithm, referred to via a figure
  (`maxLFQ_principle.png`) that is not reproduced here.
- **MS-stats** — also fits a robust peptide-level model of the same kind described above, but
  typically imputes missing values first, rather than fitting directly to the observed peptides
  with gaps.
- **Proteus's "high-flyer" method** — summarizes a protein by the mean of just its three
  highest-intensity peptides, discarding the rest, via a second figure
  (`msqrobsum_sum_novel.png`) also not reproduced here.

The robust, peptide-level-model approach used above is credited to Sticker et al. (2020),
`https://doi.org/10.1074/mcp.RA119.001624` — the paper behind `msqrob2`'s default summarization and
modelling.

## An alternative to summarizing at all: peptide-level mixed models

Summarization exists because a protein-level test needs one number per protein per sample. But an
entirely different strategy is available: skip summarization and model the peptide-level data
directly, testing for differential abundance at the peptide level rather than the protein level.

Doing this honestly requires dealing with **pseudo-replication**: many peptide measurements come
from the same sample (run), and they are not independent replicates of that sample's condition —
they share whatever made that particular run's overall signal higher or lower than another run of
the same condition. Treating every peptide observation as an independent data point would overstate
the effective sample size and understate the true uncertainty in the condition effect.

The fix is a mixed model with a random effect at the sample level:

$$
y_{iclp}= \beta_0 + \beta_c^\text{condition} + \beta_l^\text{lab} + \beta_p^\text{peptide} + u_s^\text{sample} + \epsilon_{iclp}
$$

- $\beta_c^\text{condition}$ — the spike-in condition effect, $c = b,\ldots,e$ (fixed, relative to
  baseline condition A) — the parameter the differential-abundance question is about;
- $\beta_l^\text{lab}$ — a fixed lab effect, $l = \text{lab}_2,\text{lab}_3$ (relative to lab 1);
- $\beta_p^\text{peptide}$ — the fixed peptide effect, exactly as in the summarization models above;
- $u_s^\text{sample}\sim N(0,\sigma^2_\text{run})$ — a **random** effect, one value per sample (run),
  which is precisely what addresses pseudo-replication: it absorbs the part of every peptide
  measurement from that sample that is shared across peptides, rather than letting the model treat
  it as independent noise;
- $\epsilon_{iclp}\sim N(0,\sigma^2_\epsilon)$ — the leftover, genuinely peptide-level noise within
  a sample.

Differential-abundance estimates are read off as contrasts between the condition coefficients, just
as in the protein-level models elsewhere in the course:

$$
\log_2FC_{B-A}=\beta^\text{condition}_B, \qquad
\log_2FC_{C-B}=\beta^\text{condition}_C - \beta^\text{condition}_B .
$$

Mixed peptide-level models of this form are implemented in `msqrob2`. Weighed against the
summarize-then-test approach used elsewhere in this course, they have real advantages:

1. they correctly address the different levels of variability in the data (within-sample,
   between-sample, between-peptide) instead of collapsing them all into one summarized number;
2. they avoid summarization altogether, and so automatically account for proteins having different
   numbers of observed peptides in different samples, rather than that variation disappearing once
   everything is reduced to one value per sample;
3. they are, as a consequence, a more powerful analysis.

But they also have real disadvantages, which is why this course does not use them for testing:

1. protein summaries are no longer available for plotting or communicating a result;
2. it is difficult to correctly specify the degrees of freedom for the resulting test statistic,
   which leads to inference that is too liberal (anti-conservative) in experiments with a small
   number of samples;
3. the sample-level random-effect variance $\sigma^2_\text{run}$ is sometimes estimated to be
   exactly zero for a given protein, in which case pseudo-replication is *not* actually addressed
   for that protein, and inference for it is too liberal;
4. they are considerably harder to explain to, and use correctly by, someone without a strong
   statistics background.

The course's own choice, stated directly, is to use peptide-level models *for summarization* — the
robust, peptide-effect-corrected model worked through above — while still testing for differential
expression at the protein level with the simpler, more easily communicated `msqrob` model and
contrast, rather than testing directly on a peptide-level mixed model.

## Sources

- `docs/omics-statistics/statomics/sga21/pda_robustSummarisation_peptideModels/01-subset-of-cptac-study-a-vs-b-comparison-in-lab-3.md`
  — the maxLFQ / median / robust three-way summarization comparison on the single-lab, two-condition
  subset: import and preprocessing of both the protein-level (`proteinGroups.txt`) and peptide-level
  (`peptides.txt`) data, the `aggregateFeatures` calls for median and robust summarization, the
  `msqrob`/contrast fit repeated for all three, and the volcano-plot and boxplot comparison with the
  FDP and bias/variability findings.
- `docs/omics-statistics/statomics/sga21/pda_robustSummarisation_peptideModels/02-full-cptac-study.md`
  — import, experimental design (three labs, five spike-in concentrations A–E) and preprocessing of
  the full CPTAC study, which supplies the data object used in the worked example that follows.
- `docs/omics-statistics/statomics/sga21/pda_robustSummarisation_peptideModels/03-peptide-level-models.md`
  — the single-protein (`P01031ups|CO5_HUMAN_UPS`, lab 3) worked example: median and mean
  summarization, the peptide-effect-corrected linear model, the `KIEEIAAK` outlier and residual
  analysis, robust summarization by M-estimation with Huber weights, the named-but-not-detailed
  alternative methods (maxLFQ, MS-stats, Proteus), the citation to Sticker et al. (2020), and the
  peptide-level mixed model with its stated advantages and disadvantages.

All three files are converted, lossless sections of a single source document,
`pda_robustSummarisation_peptideModels.Rmd`, from the `statOmics/SGA21` GitHub repository
(statomics-sga21, CC BY-NC-SA 4.0), itself drawn from the online course *Proteomics Data Analysis
2021* (PDA21). The source's own reference list (`## References`) is present as a heading only, with
no entries rendered in the converted text, so citations other than the one DOI given inline
(Sticker et al., 2020) cannot be resolved further here. Two figures the lecture displays but that
are not included in the converted material are named above (`maxLFQ_principle.png`,
`msqrobsum_sum_novel.png`); the `tidyverse`, `limma`, `QFeatures`, `msqrob2`, `plotly`, `gridExtra`
and `MASS` R/Bioconductor packages used to run the analysis are referred to by name only.

---

[← 22. Label-Free Proteomics Data Preprocessing](22-label-free-proteomics-data-preprocessing.md) · [Contents](index.md) · [24. Experimental Design and Blocking →](24-experimental-design-and-blocking.md)
