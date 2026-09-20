---
title: "4. A Proteomics Spike-In Case Study"
course: "StatOmics Sga21"
chapter: 4
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. A Proteomics Spike-In Case Study

## What this covers

This chapter answers a practical question in quantitative proteomics: given a MaxQuant search
output — a table of peptide intensities per sample — how do you turn it into a statistically
defensible list of proteins that differ between two conditions, and how do you know whether the
pipeline you used actually works? It walks through one complete case study, from raw peptide-level
intensities to a tested list of differentially abundant proteins, using a spike-in experiment where
the right answer is known in advance. It assumes some familiarity with linear regression and the
log-fold-change idea, and with the peptide/protein hierarchy of mass-spectrometry-based proteomics
(a protein is inferred from several peptides, each measured with its own noise).

## The case study: an experiment with a known answer

The data come from the sixth study of the Clinical Proteomic Technology Assessment for Cancer
(CPTAC). The authors spiked the Sigma Universal Protein Standard mixture 1 (UPS1) — 48 human
proteins — into a constant background of yeast (*Saccharomyces cerevisiae* strain BY4741) protein,
at two different concentrations:

- condition **A**: 0.25 fmol UPS1 protein/$\mu$L
- condition **B**: 0.74 fmol UPS1 protein/$\mu$L

with three replicate runs per condition, restricted here to one instrument (LTQ-Orbitrap W, site
56), searched with MaxQuant.

The point of spiking in a known quantity is that it gives the analysis a ground truth to check
itself against. Every UPS protein should show the same true fold change between B and A, namely
the ratio of the spiked concentrations:

$$\log_2\!\left(\frac{0.74}{0.25}\right) \approx 1.57$$

Every yeast (background) protein should show **no** true fold change — its concentration was not
touched. A pipeline that reports very different numbers, or that calls large numbers of yeast
proteins "significant", is telling you something is wrong with the pipeline, not with biology. That
is the thread that runs through the whole case study: at each stage the question is not just "does
this look reasonable" but "does it recover the numbers we know must be there".

The data used here are a teaching subset of the full CPTAC study, distributed as the `msdata`
package; the search settings are described in Goeminne et al. (2016), referenced in the source
material but not reproduced here.

## From MaxQuant output to a feature matrix

A MaxQuant search produces a `peptides.txt` file (found by default in
`path_to_raw_files/combined/txt/`) with one row per peptide and one intensity column per sample.
The `QFeatures` package reads this directly:

```r
ecols <- grep("Intensity\\.", names(read.delim(peptidesFile)))
pe <- readQFeatures(table = peptidesFile, fnames = 1, ecol = ecols,
                     name = "peptideRaw", sep = "\t")
```

`grepEcols`-style matching on the column names picks out the intensity columns; the spike-in
condition (A or B) is then read straight out of the sample names.

Two things need attention before any statistics happens:

- **Zero is not a measurement.** MaxQuant writes `0` for a peptide it did not detect in a sample.
  Treating that as a real intensity of zero would be wrong — it is a missing value, not a small
  value — so the first step converts every `0` to `NA` (`zeroIsNA`). This distinction matters
  because peptide intensities are typically **missing not at random**: a peptide is more likely to
  be undetected precisely when its true abundance is low, so the missingness itself carries
  information and cannot simply be dropped or imputed with zero.
- **A non-trivial fraction of the table is missing**, and some peptides have no signal in *any*
  sample. This is normal for shotgun proteomics — unlike, say, RNA-seq counts, which are complete
  by construction — and is the reason the preprocessing below exists.

## Preprocessing: log, filter, normalize

### Log transform

Peptide intensities are log$_2$-transformed before anything else. As with most intensity-type
measurements, variability scales with the signal (multiplicative noise); working on the log scale
turns that into additive noise, which is what the linear models used later assume.

### Filtering

Three filters are applied, each removing a different kind of unreliable evidence rather than
arbitrarily trimming the table:

1. **Ambiguous peptide-to-protein mapping.** A peptide sequence can belong to more than one protein
   (shared regions, isoforms, paralogs). A peptide is kept only if it maps to the *smallest* group
   of proteins consistent with the data (`smallestUniqueGroups`) — the usual "razor peptide"
   principle — so that its evidence is not silently double-counted across proteins or wrongly
   assigned to one when it could equally support another.
2. **Decoys and contaminants.** MaxQuant's reversed ("decoy") sequences exist only to estimate the
   search engine's false discovery rate; they are not real identifications and are removed, along
   with known laboratory contaminants (e.g. keratin) that are not part of the sample.
3. **Peptides seen in fewer than two samples.** With a single observation you cannot estimate
   variability at all, let alone test anything, so peptides observed in only one sample are
   dropped.

### Normalize by median centering

Even after filtering, samples differ by a roughly constant offset that has nothing to do with
biology — different total amounts loaded on the instrument, small drifts in sensitivity between
runs. The correction assumes that *most* peptides do not change between samples, so the sample's
own median intensity is a good estimate of that purely technical shift, and it is subtracted off:

$$y_{ip}^{\text{norm}} = y_{ip} - \hat\mu_i$$

where $\hat\mu_i$ is the median log$_2$ intensity over all observed peptides in sample $i$. After
this correction the per-sample intensity distributions line up closely with each other — the point
of the correction is exactly that alignment.

Median centering only removes a *global* per-sample shift, though. Looking at the peptide-level
data with a multidimensional scaling (MDS) plot — where the first axis shows the direction of the
largest log-fold-change between samples — the leading source of variation is still technical, not
the spike-in condition: samples do not separate cleanly into the A/B groups yet. Removing the
overall shift was necessary but not sufficient; the biological signal is still buried at the
peptide level.

## Summarization: from peptides to proteins

A protein's expression is not measured directly — it has to be assembled from however many
peptides mapped to it. The case study compares two ways of doing that assembly on the same,
normalized peptide data:

- **Median summarization**: for each protein and sample, just take the median of its peptides'
  log-intensities. Simple, but — as the source material stresses explicitly — suboptimal, and used
  here only for teaching contrast.
- **Robust summarization** (the actual default, `MsCoreUtils::robustSummary()`): an M-estimation
  procedure that fits an intensity per protein per sample while automatically downweighting peptides
  that behave like outliers, rather than treating every peptide equally.

```r
pe <- aggregateFeatures(pe, i = "peptideNorm", fcol = "Proteins",
                         na.rm = TRUE, name = "protein",
                         fun = matrixStats::colMedians)      # naive median
# vs. the default fun = MsCoreUtils::robustSummary()          # robust
```

The difference is not cosmetic. Re-running the MDS plot at the protein level:

<figure>
<svg viewBox="0 0 640 260" role="img" aria-label="MDS plots comparing median and robust protein summarization: median summarization leaves the two spike-in conditions mixed together, robust summarization separates them along the second axis">
  <text x="150" y="20" text-anchor="middle" font-size="13" fill="currentColor">median summarization</text>
  <line x1="40" y1="220" x2="280" y2="220" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="220" x2="40" y2="40" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="240" text-anchor="middle" font-size="12" fill="currentColor">MDS 1</text>
  <text x="18" y="130" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 130)">MDS 2</text>
  <g font-size="12" fill="currentColor">
    <text x="95" y="150">A</text><text x="115" y="165">B</text><text x="150" y="140">A</text>
    <text x="170" y="160">B</text><text x="200" y="155">A</text><text x="220" y="145">B</text>
  </g>
  <text x="150" y="255" text-anchor="middle" font-size="11" fill="currentColor">A and B mixed together — no separation</text>

  <text x="480" y="20" text-anchor="middle" font-size="13" fill="currentColor">robust summarization</text>
  <line x1="360" y1="220" x2="600" y2="220" stroke="currentColor" stroke-width="1.2"/>
  <line x1="360" y1="220" x2="360" y2="40" stroke="currentColor" stroke-width="1.2"/>
  <text x="480" y="240" text-anchor="middle" font-size="12" fill="currentColor">MDS 1</text>
  <text x="338" y="130" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 338 130)">MDS 2</text>
  <g font-size="12" fill="currentColor">
    <text x="410" y="90">A</text><text x="435" y="80">A</text><text x="460" y="95">A</text>
  </g>
  <g font-size="12" fill="currentColor" stroke="currentColor">
    <text x="420" y="190" fill="currentColor" stroke="none" font-weight="bold">B</text>
    <text x="450" y="200" fill="currentColor" stroke="none" font-weight="bold">B</text>
    <text x="475" y="185" fill="currentColor" stroke="none" font-weight="bold">B</text>
  </g>
  <text x="480" y="255" text-anchor="middle" font-size="11" fill="currentColor">A and B separate along MDS 2</text>
</svg>
<figcaption>Same normalized peptide data, two summarization rules. Naive per-protein medians leave
the spike-in groups indistinguishable; robust summarization, which downweights outlying peptides,
recovers a clean separation between conditions A and B on the second MDS axis.</figcaption>
</figure>

The lesson is not "robust methods are generically better" in the abstract — it is that *this
specific* choice, made silently at one line of code, decides whether the biological signal the
whole experiment was designed to detect is even visible before a single hypothesis test is run.

## Modeling protein expression and testing for a difference

With one robustly summarized log$_2$ intensity per protein per sample, a linear model is fit per
protein, again using robust regression rather than ordinary least squares — consistent with the
summarization step, since peptide-level outliers propagate into the model residuals too:

```r
pe <- msqrob(object = pe, i = "protein", formula = ~condition)
```

`condition` is a factor with two levels, A and B; with A as the reference level, the model's
intercept is the mean log$_2$ expression under A, and the coefficient `conditionB` is the average
log$_2$ fold change of B relative to A. Testing whether B differs from A is therefore testing the
single contrast

$$\texttt{conditionB} = 0$$

```r
L <- makeContrast("conditionB=0", parameterNames = c("conditionB"))
pe <- hypothesisTest(object = pe, i = "protein", contrast = L)
```

which yields, for every protein, an estimated log-fold-change, a p-value, and a multiplicity-adjusted
p-value.

## Reading the results against the known truth

This is where the spike-in design pays off: the results can be checked, not just reported.

**Volcano plot.** Plotting log-fold-change against $-\log_{10}(p)$, colored by
`adjPval < 0.05`, shows only a small number of proteins declared differentially abundant — most
proteins, correctly, are not.

**Heatmap of the significant proteins.** Restricting to the proteins called significant, the large
majority are UPS proteins — the ones that were actually spiked, so this is the pipeline working as
intended. But one yeast protein also passes the significance threshold. Since yeast was the
constant background, this one call is necessarily a false positive, and the case study does not
paper over it — it is used as the next question.

**Boxplot against the true fold changes.** Splitting the estimated log-fold-changes into "UPS" and
"not UPS" and overlaying the two true values makes the calibration visible directly:

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Boxplot of estimated log fold change for yeast versus UPS proteins, each compared against its known true value">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="170" y="208" text-anchor="middle" font-size="12" fill="currentColor">protein group</text>
  <text x="18" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 105)">estimated log2 FC</text>

  <line x1="40" y1="150" x2="130" y2="150" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="135" y="147" font-size="11" fill="currentColor">true FC = 0 (yeast)</text>
  <rect x="75" y="140" width="30" height="20" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <line x1="90" y1="120" x2="90" y2="140" stroke="currentColor" stroke-width="1.2"/>
  <line x1="90" y1="160" x2="90" y2="180" stroke="currentColor" stroke-width="1.2"/>
  <text x="90" y="200" text-anchor="middle" font-size="11" fill="currentColor">yeast</text>

  <line x1="170" y1="55" x2="260" y2="55" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="203" y="45" font-size="11" fill="currentColor">true FC ≈ 1.57 (UPS)</text>
  <rect x="195" y="45" width="30" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.3"/>
  <line x1="210" y1="30" x2="210" y2="45" stroke="currentColor" stroke-width="1.2"/>
  <line x1="210" y1="65" x2="210" y2="80" stroke="currentColor" stroke-width="1.2"/>
  <text x="210" y="200" text-anchor="middle" font-size="11" fill="currentColor">UPS</text>
</svg>
<figcaption>Estimated log fold changes for background (yeast) and spiked (UPS) proteins, each
against the fold change the spike-in concentrations dictate it must have.</figcaption>
</figure>

The true UPS fold change follows directly from the spiked concentrations, $\log_2(0.74/0.25)
\approx 1.57$, and the true yeast fold change is $0$. A pipeline that recovers estimates clustering
around these two lines, group by group, is doing what it is supposed to; systematic offsets or
wide scatter around the wrong line would flag a problem upstream (normalization, summarization, or
the model itself) rather than a biological effect.

**Detail plots for the flagged yeast protein.** The case study does not stop at "one false
positive" — it goes back to the peptide-level data underlying that one protein. It turns out to be
supported by only **three peptides total**, and one of those is observed just once in condition A
and once in condition B. A "significant" result built on essentially one data point per group is
not a discovery so much as a symptom of too little evidence being asked to support a confident
answer. This is exactly the failure mode the earlier "at least two observations" filter was meant
to guard against, and the fact that it slips through here is a reason to consider a stricter
peptide-count requirement, not a reason to distrust the statistical test itself.

## Reproducibility

The case study closes by recording the analysis session's software environment
(`sessionInfo()`). The point made is a general one: a reader of any analysis output should be able
to see exactly which R and package versions produced it, since preprocessing choices like the
summarization method above can change the answer.

## Sources

- `docs/omics-statistics/statomics/sga21/cptac_median/01-data.md` — the CPTAC spike-in experiment,
  reading the MaxQuant peptide table with `QFeatures`, converting zeros to `NA`, and the missingness
  observation.
- `docs/omics-statistics/statomics/sga21/cptac_median/02-preprocessing.md` — log transform, the
  three filters, median-centering normalization and its formula, the peptide-level MDS plot, and
  the median-vs-robust summarization comparison.
- `docs/omics-statistics/statomics/sga21/cptac_median/03-data-analysis.md` — the `msqrob` model,
  the `conditionB = 0` contrast and `hypothesisTest`, the volcano plot, heatmap, boxplot against the
  known truth, the peptide-level detail plots for the flagged yeast protein, and the reproducibility
  note.

All three are converted from `cptac_median.Rmd` in the statOmics SGA21 course repository (CC
BY-NC-SA 4.0), part of the online course *Proteomics Data Analysis 2021 (PDA21)*. The source
material cites Goeminne et al. (2016) for the MaxQuant search settings and references entries [1],
[5] and [6] of its own bibliography (the CPTAC study design, the spike-in concentrations, and the
MaxQuant search) — that reference list itself was not part of the supplied material and is not
reproduced here.

---

[← 3. CPTAC Spike-In Case Study](03-cptac-spike-in-case-study.md) · [Contents](index.md) · [5. Robust Summarization in Proteomics →](05-robust-summarization-in-proteomics.md)
