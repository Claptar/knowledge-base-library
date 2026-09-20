---
title: "3. CPTAC Spike-In Case Study"
course: "StatOmics Sga21"
chapter: 3
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. CPTAC Spike-In Case Study

## What this covers

How do you tell whether a differential-abundance pipeline for quantitative proteomics is finding
real changes and not noise? This chapter works through a single case study that answers that
question by construction: a spike-in experiment where the true fold changes are known in advance,
so every step of the pipeline — import, transform, normalize, model, test — can be checked against
a ground truth rather than taken on faith. It assumes you know roughly what a label-free
quantification (LFQ) intensity is, and are comfortable with linear models, hypothesis tests and the
idea of correcting for multiple testing; it does not assume familiarity with the specific R/
Bioconductor tools (`QFeatures`, `msqrob2`) used to carry it out, which are introduced as they
appear.

## The CPTAC spike-in benchmark

The case study uses a subset of data from the 6th study of the Clinical Proteomic Technology
Assessment for Cancer (CPTAC). The design is a spike-in experiment: the Sigma Universal Protein
Standard mixture 1 (UPS1), containing 48 human proteins, was spiked into a constant background of
60 ng/$\mu$L *Saccharomyces cerevisiae* (yeast) protein, at two different concentrations —

- condition **6A**: 0.25 fmol UPS1 protein/$\mu$L
- condition **6B**: 0.74 fmol UPS1 protein/$\mu$L

with three replicates of each. The data used here come from a single instrument (LTQ-Orbitrap W,
site 56), searched with MaxQuant, with search settings described in Goeminne et al. (2016).

The point of a design like this is that it manufactures a known answer. Every UPS1 protein has a
*true* log2 fold change between condition B and condition A of $\log_2(0.74/0.25)$ — the ratio of
the two spiked-in concentrations — because that is the only thing that changed for those proteins.
Every yeast (background) protein has a true log2 fold change of $0$, because its true
concentration was held constant across both conditions. So instead of only asking "which proteins
does the pipeline call significant?", you can ask the sharper question "does it call the *right*
proteins significant, and does it recover the *right size* of change?" That is what the later
volcano plot, heatmap and boxplot in this chapter are for.

One caveat carried directly from the source material: the protein-level intensities used here come
from MaxQuant's own **maxLFQ** peptide-to-protein summarization, which the case study flags
explicitly as a suboptimal choice — it is used only because it lets the rest of the workflow
(filtering, normalization, modelling, testing) be demonstrated on protein-level data without first
building peptide-to-protein summarization from scratch. It should not be read as an endorsement of
maxLFQ as the best way to get from peptides to proteins.

## From a MaxQuant search to an R object

A MaxQuant search produces, among other files, a `proteinGroups.txt` table in the search output's
`combined/txt/` folder. This file holds one row per identified protein group and, for each sample,
a maxLFQ-summarized intensity column, plus per-protein metadata columns (including quality flags
used below).

The case study reads this table with the Bioconductor package `QFeatures`, which is built around
one object (here called `pe`) that can hold several *parallel* representations of the same
features — the raw intensities, the log-transformed intensities, the normalized intensities — each
stored as a named **assay**, alongside a shared **row data** table of per-protein metadata and a
shared **column data** table of per-sample metadata. Concretely:

- `grep("LFQ\\.intensity\\.", ...)` picks out just the sample intensity columns among all the
  columns MaxQuant writes to `proteinGroups.txt`.
- `readQFeatures(...)` builds the object, naming this first assay `"proteinRaw"`.
- The spike-in condition (`A` or `B`) is read straight out of each sample's column name and stored
  in the object's column data as `condition` — this is the factor the whole downstream analysis is
  built around.
- The count of non-zero intensities per protein (`nNonZero`) is computed and stored in the row data,
  to have on hand for later completeness-based filtering.

One detail matters enough to call out on its own: MaxQuant reports an intensity of exactly `0` when
a protein was not observed in a sample, but a `0` is not a measured value of zero abundance — it is
the *absence* of a measurement. Treating it as a real zero would corrupt any statistic computed on
the log scale (there is no $\log(0)$) and would bias comparisons toward proteins that happen to be
easy to detect. So the first thing the pipeline does with the raw assay is convert every `0` to
`NA`, recording it honestly as missing rather than as an observed low value.

## Preprocessing: scale, filter, normalize

Three preprocessing steps turn the raw, missing-value-laden protein intensities into something a
linear model can be fit to.

**Log transform.** The intensities are put on the $\log_2$ scale, producing a new assay
(`"proteinLog"`) alongside the raw one — the object keeps both, rather than overwriting.

**Filtering.** Two quality flags that MaxQuant attaches to every protein group are used to remove
rows that should never be treated as real biological signal:

- `Reverse == "+"` marks a protein group that only matches the *decoy* (reversed) database used to
  estimate the false discovery rate of the search itself — not a real protein.
- `Potential.contaminant == "+"` marks common laboratory contaminants (keratins, trypsin, and
  similar) that are artefacts of sample handling, not of the biology under study.

Both are filtered out before anything else is computed.

**Normalization.** Even after log transformation, the overall intensity level can differ from
sample to sample for reasons that have nothing to do with biology — how much material was loaded,
day-to-day instrument variation, and so on. The case study corrects for this with **median
centering**: for every peptide (protein) $p$ measured in sample $i$,

$$y_{ip}^{\text{norm}} = y_{ip} - \hat\mu_i$$

where $\hat\mu_i$ is the median of the observed log2 intensities in sample $i$. Subtracting a
per-sample constant shifts each sample's whole distribution so that its median lines up with every
other sample's — it removes a systematic, sample-wide offset without touching the *relative*
differences between proteins within a sample, which is exactly the signal the analysis is trying to
preserve.

## Checking the normalization worked

Two exploratory plots are used to sanity-check the steps above before trusting them.

The first is a density plot of the (now normalized) intensities, one curve per sample, colored by
condition. After median centering the case study reports that the curves are "nicely registered" —
i.e. they sit on top of one another — which is the visual signature that the per-sample offset has
in fact been removed. If the curves were still offset from each other, that would be a sign the
normalization step had not done its job, or that something more than a simple shift is needed.

The second is a **multi-dimensional scaling (MDS)** plot (via `limma::plotMDS`), which represents
each *sample* as a point in a low-dimensional space chosen so that samples with more similar overall
expression profiles sit closer together. It is a standard first check for whether the variable you
actually care about — here, spike-in condition — is visible in the data at all, and whether it is
the dominant source of variation or a smaller one competing with technical noise. In this data set,
the samples separate clearly by condition, but only in the *second* dimension of the plot, not the
first: the biological signal from the spike-in is real and detectable, but it is not the largest
source of variability between samples.

## Fitting a per-protein model with msqrob2

With a cleaned, normalized assay in hand, the case study fits one linear model *per protein* using
`msqrob2`, via `msqrob(object = pe, i = "protein", formula = ~condition)`. By default `msqrob2` uses
**robust regression** to estimate each model's parameters — a fitting method that down-weights
observations that look like outliers relative to the rest, rather than letting a handful of
mis-quantified peptides pull a protein's estimated fold change around.

The formula `~condition` is a one-factor model: log2 protein expression explained by which spike-in
condition the sample belongs to. With the two-level factor `condition` coded the default way (`A`
as the reference level, since it comes first alphabetically), the fitted model has two parameters
per protein:

- the **intercept**, equal to the mean log2 expression in condition A;
- the coefficient **`conditionB`**, equal to the average log2 fold change of condition B relative to
  condition A.

So the mean log2 expression in condition B is `(Intercept) + conditionB`, and the parameter of
interest — the one the differential-abundance question is really about — is `conditionB` itself.
(`getCoef()` on the first protein's fitted model, and the `ExploreModelMatrix` package's
`VisualizeDesign`, are used in the case study purely to check that the model was built the way it
was intended to be, before trusting any of its output.)

## Testing for differential abundance

Because the quantity of interest is a single coefficient, testing for differential abundance comes
down to testing whether `conditionB` is zero. The case study expresses this as an explicit
**contrast** — `makeContrast("conditionB = 0", parameterNames = c("conditionB"))` — and passes it to
`hypothesisTest()`, which, for every protein, returns:

- `logFC`: the estimated log2 fold change (the fitted value of `conditionB`),
- `pval`: the p-value for the test that this fold change is zero,
- `adjPval`: that p-value after correction for testing thousands of proteins at once.

These per-protein results are attached to the object's row data under the name of the contrast
(`conditionB`), sitting alongside the raw and normalized intensities in the same object.

## Reading the results against the known truth

This is where the spike-in design earns its keep: the results are not just inspected for
statistical significance, but checked against the true fold changes the experiment was built to
have.

**Volcano plot.** Plotting `logFC` against $-\log_{10}(\text{pval})$, colored by whether
`adjPval < 0.05`, is the standard way to see effect size and significance at once — a real,
strong, differentially-abundant protein should sit far from zero on the x-axis *and* high up on the
y-axis, not just one or the other. In this data set only a small fraction of proteins clear the
significance threshold.

**Heatmap.** Restricting to just the proteins declared significant and looking at their (normalized)
intensities directly, the case study reports that the great majority of the significant proteins
are indeed UPS1 proteins — the ones that were actually spiked at different levels — which is what a
correctly-working pipeline should recover. One yeast (background) protein is also returned as
significant. Rather than dismissing this automatically as a false positive because it "shouldn't"
be there, the case study flags that this particular yeast protein does show real evidence of a
genuine abundance difference between the two sample groups — a reminder that a spike-in benchmark's
"expected" answer (all yeast proteins unchanged) is a design target, not a guarantee, and that a hit
outside the expected set is worth looking at rather than automatically discounting.

**Boxplot against the true fold change.** The most direct check plots the estimated `logFC` for
every protein, split into two groups by whether the protein name contains "UPS" (spiked) or not
(background), and overlays each group with a horizontal reference line at its *true* value: $0$ for
the background group, and $\log_2(0.74/0.25) \approx 1.57$ for the UPS1 group. This turns the whole
analysis into a single picture: do the estimated fold changes for each group actually cluster around
the value they are supposed to have?

## Exercises

From the case study's own closing prompt, on the boxplot of estimated log2 fold change split by
spiked (UPS1) versus background protein, with reference lines at the true values $0$ and
$\log_2(0.74/0.25)$:

1. What do you observe? In particular, does each group's distribution of estimated fold changes sit
   close to its reference line, or is there a systematic offset — and if so, in which direction?
2. Are there any proteins in either group whose estimated fold change is far from what the group's
   reference line would predict? What would you want to check about those specific proteins before
   concluding the pipeline had made an error on them?

## Sources

- `docs/omics-statistics/statomics/sga21/cptac_maxLFQ/01-data.md` — background on the CPTAC study 6
  spike-in design, and the data-import section of `cptac_maxLFQ.Rmd` (reading `proteinGroups.txt`
  with `QFeatures`, extracting the condition factor, converting zero intensities to `NA`).
- `docs/omics-statistics/statomics/sga21/cptac_maxLFQ/02-preprocessing.md` — the log-transform,
  decoy/contaminant filtering, and median-centering normalization sections, including the density
  and MDS exploratory plots.
- `docs/omics-statistics/statomics/sga21/cptac_maxLFQ/03-data-analysis.md` — the `msqrob2` model
  fit, the `conditionB` contrast and hypothesis test, and the volcano plot, heatmap and boxplot used
  to read the results against the known spike-in fold changes.

All three files are converted, lossless, from `cptac_maxLFQ.Rmd` in the `statOmics/SGA21` GitHub
repository (statomics-sga21, CC BY-NC-SA 4.0), itself part of the online course *Proteomics Data
Analysis 2021* (PDA21). The source cites Goeminne et al. (2016) for the MaxQuant search settings
used, and separately cites the original CPTAC study 6 paper and the MaxQuant paper by reference
number, but does not include the reference list itself, so those citations cannot be resolved more
precisely here. The source also refers to, without including, the `tidyverse`, `limma`, `QFeatures`,
`msqrob2`, `plotly`, `gridExtra` and `ExploreModelMatrix` R/Bioconductor packages used to run the
analysis.

---

[← 2. From Peptides to Differential Expression](02-from-peptides-to-differential-expression.md) · [Contents](index.md) · [4. A Proteomics Spike-In Case Study →](04-a-proteomics-spike-in-case-study.md)
