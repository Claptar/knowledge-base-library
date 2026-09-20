---
title: "5. Robust Summarization in Proteomics"
course: "StatOmics Sga21"
chapter: 5
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Robust Summarization in Proteomics

## What this covers

This chapter works through one complete case study in quantitative, label-free proteomics: turning
raw peptide-level mass-spectrometry intensities into a list of differentially abundant proteins —
and, because the experiment was built so that the right answer is known in advance, checking
whether the analysis pipeline actually recovers it. It assumes the vocabulary of MS-based
proteomics (peptides, proteins, protein groups, MaxQuant search output) and enough linear-model
background to read a model with a factor covariate and to interpret a contrast and a p-value.

## The experiment: a spike-in design with a known answer

The data are a subset of the sixth study of the Clinical Proteomic Technology Assessment for
Cancer (CPTAC). The authors took a constant background of *Saccharomyces cerevisiae* proteins (60
ng/µL) and spiked in the Sigma Universal Protein Standard mixture 1 (UPS1, 48 human proteins) at
two different concentrations:

- condition **A**: 0.25 fmol UPS1 protein/µL
- condition **B**: 0.74 fmol UPS1 protein/µL

with three replicate runs per condition, all on the same instrument (LTQ-Orbitrap W, site 56),
searched with MaxQuant.

This design is what makes the case study useful for *teaching* a pipeline rather than just running
one: for the spiked-in (UPS) proteins the true log2 fold change between B and A is known exactly,
$$
\log_2\!\left(\frac{0.74}{0.25}\right) \approx 1.57,
$$
while for the yeast background proteins — present at the same amount in both conditions — the true
log2 fold change is $0$. Any analysis pipeline can therefore be graded against ground truth: a good
pipeline should find the UPS proteins differentially abundant with an estimated fold change near
$1.57$, and should call very few yeast proteins differentially abundant at all.

## Getting the data in: peptides, and zero is not zero

The raw material is `peptides.txt`, the peptide-level intensity table MaxQuant writes to
`path_to_raw_files/combined/txt/`. It is read into a `QFeatures` object — a container built for
exactly this kind of experiment, where the same features (here, peptides) are assayed across many
samples and later need to be rolled up into a coarser feature (proteins). The intensity columns are
located by matching the column-name pattern `Intensity.`, and the spike-in condition (A or B) for
each sample is read straight out of the corresponding column name.

The first substantive modelling decision is about missing data. MaxQuant reports a $0$ for a
peptide it did not detect in a given run — but a $0$ intensity is not a measurement of zero
abundance, it is the *absence* of a measurement. Treating it as a real numerical value would be
biased twice over: it would enter later as an implausibly low intensity, and (once the data are put
on a log scale) $\log(0)$ is not even defined. So before anything else, every zero is recoded as a
missing value, `NA`:

```r
rowData(pe[["peptideRaw"]])$nNonZero <- rowSums(assay(pe[["peptideRaw"]]) > 0)
pe <- zeroIsNA(pe, "peptideRaw")   # convert 0 to NA
```

The count of non-missing observations per peptide (`nNonZero`), computed just before the
conversion, is kept for use in the filtering step below. On this data set, a large fraction of all
peptide intensities are missing, and some peptides carry no signal in any sample at all — a
reminder that missingness, not just noise, is a first-class feature of this kind of data.

## Preprocessing: log scale, filtering, normalisation

Three things happen before the peptide table is fit for summarisation.

**Log transform.** Intensities are put on the $\log_2$ scale, which is the scale on which MS
intensity noise is roughly symmetric and on which fold changes become differences.

**Filtering**, in three steps:

1. *Resolve overlapping protein groups.* A peptide sequence can be consistent with more than one
   protein. It is kept only if none of its candidate proteins is already covered by a *smaller*
   protein group elsewhere in the data — `smallestUniqueGroups` — so that ambiguous peptides are
   assigned to the most specific protein group they can support rather than being double-counted.
2. *Remove decoys and contaminants.* Peptides matched to reversed (decoy) sequences, and
   laboratory contaminant proteins, are dropped before any biological comparison is made.
3. *Require replication.* A peptide observed in only one sample (using the `nNonZero` count from
   the import step) is dropped — it cannot on its own provide evidence of a difference between
   conditions.

**Normalisation.** Even within one condition, samples differ in overall loading and instrument
response, which shifts every intensity in a sample up or down together. This is corrected by
median centering: for peptide $p$ in sample $i$,
$$
y_{ip}^{\text{norm}} = y_{ip} - \hat\mu_i,
$$
where $\hat\mu_i$ is the median log2 intensity over all observed peptides in sample $i$. Subtracting
a per-sample constant removes the *sample-level* shift while leaving peptide-to-peptide and
condition-to-condition differences untouched. After this step the per-sample intensity
distributions line up (their density curves register), which is the visual check that the
correction worked.

## Why summarize at all: peptides hide the signal, proteins reveal it

Once the peptide table is cleaned and normalised, it can already be visualised: an MDS
(multidimensional scaling) plot of the peptide-level data shows the *first* axis — the direction of
largest variability between samples — driven by something other than the spike-in condition. The
two conditions are not cleanly separated at the peptide level; technical variability between runs
dominates the biological signal at this resolution.

The remedy is to combine, for each protein, the (many) peptides that were measured for it into a
single per-protein value per sample — *summarisation*. Here this is done with a **robust**
summary (`MsCoreUtils::robustSummary()`), which combines the peptide measurements for a protein
using a robust-regression style estimator rather than a plain mean, so that one unusually
high or low peptide does not dominate the protein-level result. After summarisation the same kind
of MDS plot shows a clear separation between the two spike-in conditions, now on the *second* MDS
axis. Aggregating many partially-missing, partially-noisy peptide measurements into one
protein-level number, in a way that down-weights outliers, is what recovers the biological signal
that was there all along but swamped by peptide-level noise.

<figure>
<svg viewBox="0 0 340 480" role="img" aria-label="The analysis pipeline from raw peptide intensities to a tested contrast">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g font-size="12" fill="currentColor">
    <rect x="40" y="10" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="36" text-anchor="middle">Peptide intensities (MaxQuant)</text>

    <line x1="170" y1="52" x2="170" y2="78" stroke="currentColor" marker-end="url(#arrow)"/>
    <rect x="40" y="80" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="106" text-anchor="middle">Zero → NA, log2 transform</text>

    <line x1="170" y1="122" x2="170" y2="148" stroke="currentColor" marker-end="url(#arrow)"/>
    <rect x="40" y="150" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="176" text-anchor="middle">Filter: groups, decoys, coverage</text>

    <line x1="170" y1="192" x2="170" y2="218" stroke="currentColor" marker-end="url(#arrow)"/>
    <rect x="40" y="220" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="246" text-anchor="middle">Median-centre each sample</text>

    <line x1="170" y1="262" x2="170" y2="288" stroke="currentColor" marker-end="url(#arrow)"/>
    <rect x="40" y="290" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="316" text-anchor="middle">Robust summary: peptide → protein</text>

    <line x1="170" y1="332" x2="170" y2="358" stroke="currentColor" marker-end="url(#arrow)"/>
    <rect x="40" y="360" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="386" text-anchor="middle">msqrob: robust regression per protein</text>

    <line x1="170" y1="402" x2="170" y2="428" stroke="currentColor" marker-end="url(#arrow)"/>
    <rect x="40" y="430" width="260" height="42" rx="6" fill="none" stroke="currentColor"/>
    <text x="170" y="456" text-anchor="middle">Contrast test: conditionB = 0</text>
  </g>
</svg>
<figcaption>The pipeline, in order: cleaning and transforming the peptide table, aggregating it to
one robust value per protein per sample, then fitting and testing a per-protein model. Each stage
exists to remove a specific source of distortion before the next stage runs on cleaner input.</figcaption>
</figure>

## Modelling protein abundance: msqrob and robust regression

At the protein level, each protein gets its own model, with expression explained by the factor
`condition`:

```r
pe <- msqrob(object = pe, i = "protein", formula = ~condition)
```

`msqrob2` fits this by robust regression by default, which is the same idea as the robust
summarisation step one level up: the parameter estimates are not thrown off by a small number of
outlying observations the way ordinary least squares would be.

With `condition` coded so that **A is the reference level**, the model has two parameters:

- `(Intercept)` — the mean log2 expression for samples from condition A,
- `conditionB` — the average log2 fold change of condition B relative to A, so that the mean log2
  expression for condition B is `(Intercept) + conditionB`.

## Testing a hypothesis: the contrast

The scientific question — is there a difference between the two spike-in conditions? — is
expressed as a **contrast**: a linear combination of the model's parameters that is zero exactly
when the hypothesis of no difference holds. Because `conditionB` already *is* the B-versus-A log2
fold change, the contrast of interest is simply

```r
L <- makeContrast("conditionB=0", parameterNames = c("conditionB"))
pe <- hypothesisTest(object = pe, i = "protein", contrast = L)
```

which tests, for every protein independently, whether its estimated `conditionB` coefficient is
distinguishable from zero.

## Reading the results against the known truth

With a p-value (and multiple-testing-adjusted p-value) attached to every protein, the results can
be read off in the usual ways — a volcano plot of estimated log fold change against $-\log_{10}$ of
the p-value, coloured by significance at the 0.05 adjusted-p-value threshold, and a heatmap of the
proteins called significant.

What makes this case study distinctive is that the significant proteins can be checked against the
ground truth built into the experiment. The estimated log fold changes are compared, in a boxplot,
between the UPS (spiked) and non-UPS (background) proteins, against two reference lines: $0$ for
the background proteins and $\log_2(0.74/0.25)\approx 1.57$ for the spiked proteins. A working
pipeline should show the UPS proteins clustering near the upper line and the background proteins
clustering near zero — and in this data set, of the proteins declared significant, the large
majority are indeed UPS proteins, with one yeast (background) protein also called significant.

## A cautionary example: how much evidence backs a "significant" protein

That one significant background protein is worth looking at directly, rather than trusting the
p-value alone. Plotting its supporting peptide intensities and its summarized protein value across
all six samples shows that it is covered by only three peptides in total, and one of those peptides
is observed only *once* in condition A and only *once* in condition B. A result built on that little
replication carries a heavy burden of inference: a single low-information peptide can move a
protein's summarized value enough to look like a real difference, even after robust summarisation.
The lesson drawn directly from this example is that such a case would be avoided, or at least
flagged, by more stringent filtering than was applied here — for instance, requiring more than the
bare minimum of two observations, or requiring support from more than a couple of peptides, before
a protein is even tested.

## Reproducibility: session info

The walkthrough ends by calling `sessionInfo()`. Recording the exact versions of R and every
package used is presented as routine good practice: it is what lets a reader of the analysis
reproduce it, or diagnose a discrepancy caused by a package update, later.

## Sources

- `docs/omics-statistics/statomics/sga21/cptac_robust/01-data.md` — the experiment background, the
  spike-in design, and importing/`zeroIsNA` handling of the raw peptide table.
- `docs/omics-statistics/statomics/sga21/cptac_robust/02-preprocessing.md` — log transform,
  the three filtering steps, median-centering normalisation, and the peptide- vs protein-level MDS
  comparison.
- `docs/omics-statistics/statomics/sga21/cptac_robust/03-data-analysis.md` — the `msqrob` model,
  the `conditionB=0` contrast and hypothesis test, the volcano plot, heatmap, the ground-truth
  boxplot, the peptide-level detail plots, and the closing note on `sessionInfo()`.

All three are converted, split sections of a single source document, `cptac_robust.Rmd` from the
statOmics SGA21 course (itself drawn from the online course *Proteomics Data Analysis 2021*,
PDA21), licensed CC BY-NC-SA 4.0. The lecture names but does not itself detail the internal
algorithm of `MsCoreUtils::robustSummary()` or of `msqrob2`'s default robust regression estimator —
those are referred to by name only, and are not reconstructed here beyond what the notes state.

---

[← 4. A Proteomics Spike-In Case Study](04-a-proteomics-spike-in-case-study.md) · [Contents](index.md) · [6. The msqrob2gui Analysis Workflow →](06-the-msqrob2gui-analysis-workflow.md)
