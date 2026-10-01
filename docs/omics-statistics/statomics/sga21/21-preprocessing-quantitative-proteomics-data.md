---
title: "21. Preprocessing Quantitative Proteomics Data"
course: "StatOmics Sga21"
chapter: 21
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. Preprocessing Quantitative Proteomics Data

## What this covers

This chapter opens a course on analysing label-free, mass-spectrometry-based quantitative
proteomics data. It answers two questions: why proteomics measurements are unusually noisy and
incomplete compared with other omics data, and what has to be done to a raw MaxQuant output table
— log-transformation, filtering, normalization, summarization — before any statistical model can
be fit to it. It assumes ordinary statistical vocabulary (mean, median, variance, robust
estimation) and some prior experience normalizing omics data (e.g. microarrays), but no proteomics
background.

## Why label-free quantification is hard

A shotgun MS-based proteomics workflow does not measure proteins directly. Proteins are digested
into peptides, the peptides are separated and ionised, and the mass spectrometer records spectra
from which peptide identities and intensities are inferred. Several things go wrong on the way:

- **Modifications.** A peptide can carry post-translational modifications, so the same stretch of
  protein sequence does not always produce the same measured species.
- **Ionisation efficiency** varies hugely from peptide to peptide, so raw intensity is not
  comparable across peptides.
- **Identification problems.** Misidentifying a peptide's sequence introduces outliers. More
  seriously, which peptide ions get selected for fragmentation (MS$^2$) in a data-dependent
  acquisition run depends on how abundant they are in the survey scan — so whether a peptide is
  identified in a given sample depends on its own abundance in that sample. Missingness is
  therefore **context-dependent and non-random**, not a peptide dropping out at random.

The consequence stated on the slide is blunt: unbalanced peptide identifications across samples,
and messy data. This is the standing problem the rest of the pipeline exists to manage.

A second, separate difficulty is the **level of quantification**. MS returns peptides — pieces of
proteins — but the scientific question is almost always about protein abundance. A protein is
represented by several peptides, and a peptide can be shared between more than one protein or
protein isoform, so getting from "peptide intensities" to "one expression value per protein per
sample" is itself a nontrivial step, taken up under Summarization below.

## From spectra to peptides to proteins

In R, the `QFeatures` package (built on the `SummarizedExperiment` and `MultiAssayExperiment`
classes used across Bioconductor) stores this multi-level structure and tracks, as the data are
processed, which features at one level were combined into which feature at the level above.

<figure>
<svg viewBox="0 0 360 165" role="img" aria-label="Spectra group into peptides, peptides group into proteins, and a shared peptide is consistent with more than one protein">
  <text x="50" y="12" text-anchor="middle" font-size="12" fill="currentColor">Spectra</text>
  <text x="185" y="12" text-anchor="middle" font-size="12" fill="currentColor">Peptides</text>
  <text x="315" y="12" text-anchor="middle" font-size="12" fill="currentColor">Proteins</text>

  <rect x="15" y="25" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="15" y="45" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="15" y="65" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="15" y="85" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="15" y="105" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="15" y="125" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <rect x="150" y="25" width="70" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="150" y="65" width="70" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="150" y="105" width="70" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <rect x="285" y="25" width="60" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="285" y="65" width="60" height="74" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <line x1="85" y1="32" x2="150" y2="42" stroke="currentColor"/>
  <line x1="85" y1="52" x2="150" y2="42" stroke="currentColor"/>
  <line x1="85" y1="72" x2="150" y2="82" stroke="currentColor"/>
  <line x1="85" y1="92" x2="150" y2="82" stroke="currentColor"/>
  <line x1="85" y1="112" x2="150" y2="122" stroke="currentColor"/>
  <line x1="85" y1="132" x2="150" y2="122" stroke="currentColor"/>

  <line x1="220" y1="42" x2="285" y2="42" stroke="currentColor"/>
  <line x1="220" y1="82" x2="285" y2="102" stroke="currentColor"/>
  <line x1="220" y1="122" x2="285" y2="102" stroke="currentColor"/>

  <line x1="220" y1="42" x2="285" y2="102" stroke="currentColor" stroke-dasharray="4 3"/>

  <text x="223" y="150" font-size="11" fill="currentColor">shared peptide</text>
</svg>
<figcaption>Several spectra summarize into one peptide, several peptides summarize into one
protein. A peptide that is not unique to a single protein group (dashed line) is consistent with
more than one protein and has to be resolved by a filtering convention rather than counted for
both.</figcaption>
</figure>

## A running example: the CPTAC spike-in study

The examples in this chapter come from a controlled spike-in dataset: the same trypsin-digested
yeast proteome background is present in every sample, and a Sigma UPS1 standard of 48 different
human proteins is spiked in at 5 concentrations, labelled conditions A–E (0.25, 0.74, 2.22, 6.67
and 20 fmol/l respectively). Samples were run repeatedly, on different instruments, in three
different labs — giving 5 conditions × 3 labs × 3 replicates = 45 samples in total. Because only
the 48 spiked proteins differ across conditions and everything else is constant background, this
is about as clean a design as label-free proteomics gets.

Even so, after a standard MaxQuant search with the "match between runs" option (which borrows
identifications across runs to reduce missingness), only 41% of all proteins and 6.6% of all
peptides are quantified in **every** sample. The vast amount of missingness described above is not
a symptom of a badly run experiment — it shows up even here.

## Getting the data into R

MaxQuant's `peptides.txt` output holds MS1 intensities summarized at the peptide level, with one
`Intensity.<sample>` column per sample plus metadata columns (`Sequence`, `Proteins`, `Reverse`,
`Potential.contaminant`, …). It is read into a `QFeatures` object by picking out the intensity
columns and pointing `readQFeatures()` at them:

```r
ecols <- grep("Intensity\\.", names(read.delim(peptidesFile)))
pe <- readQFeatures(table = peptidesFile, fnames = 1, ecol = ecols,
                     name = "peptideRaw", sep = "\t")
```

MaxQuant knows nothing about the experimental design, so it has to be reconstructed from the
sample names by hand: which three columns belong to which lab, and which spike-in condition (and
concentration) each sample belongs to. This design information is then attached to the object's
`colData` before anything else is done.

## Preprocessing, step by step

The outline for the rest of the chapter — and the order in which the steps are actually applied —
is: log-transformation, filtering, normalization, summarization.

### Log-transformation

Take peptide `AALEELVK`, from the spiked-in UPS protein P12081, and look only at lab 1. Plotted on
the raw scale, intensity against spike-in concentration, the variance of the replicate
measurements clearly grows with the mean: a **multiplicative error structure**. Plotted instead
with both axes on a $\log_2$ scale, the spread of the replicates looks roughly constant across
concentrations — homoscedastic. That is the justification for working in $\log_2$ intensity for
the rest of the analysis, and it is also why proteomics reports differences as $\log_2$ fold
changes:

$$
\log_2 FC_{B-A} = \log_2 B - \log_2 A = \log_2\frac{B}{A}
$$

so $\log_2 FC = 1$ corresponds to a fold change of $2^1 = 2$, and $\log_2 FC = 2$ to $2^2 = 4$.

Before taking logs, a zero intensity has to be recoded as missing (`NA`) rather than left as `0`
— a peptide with intensity 0 was not detected, it does not have zero abundance, and $\log_2(0)$
is undefined:

```r
pe <- zeroIsNA(pe, "peptideRaw")            # 0 -> NA
pe <- logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")
```

The number of non-missing intensities per peptide is also recorded at this point, since it feeds
into filtering next.

### Filtering

Several groups of peptides are removed before analysis: reverse (decoy) sequences, peptides
identified only by a modification site, razor peptides (non-unique peptides assigned by
convention to whichever protein group they could support with the most other peptides),
contaminants, and peptides or proteins with very few identifications.

The principle behind all of this: **filtering does not bias the downstream analysis, provided the
filtering criterion is independent of that analysis.** Dropping peptides on a criterion such as
"observed in at least two samples" is safe because it says nothing about whether the peptide's
abundance differs between conditions; filtering on a criterion correlated with the actual test
would not be.

Concretely, three filters are applied in order:

1. **Resolve shared peptides.** A peptide can map to several proteins; it is kept only under the
   smallest protein group consistent with the data (`smallestUniqueGroups`), rather than being
   counted toward every protein it could in principle belong to — this is exactly the ambiguity
   drawn as the dashed line above.
2. **Remove reverse sequences and contaminants** outright.
3. **Require at least two non-missing observations** per peptide across all samples.

### Normalization

Even in the clean CPTAC design, the marginal distribution of $\log_2$ peptide intensities differs
considerably from sample to sample — both between labs within the same spike-in condition, and
between spike-in conditions within the same lab. Before samples can be compared, they need to be
put on a common scale.

A short aside on why the course centers on the *median* rather than the mean: Miller and Fishkin
(1997) reported that, asked how many partners they would like to have over a 30-year period, men
answered on average 64.3 and women 2.8 — but the *median* answer was 1, for both. The mean is very
sensitive to outliers; the median is not.

The default normalization here is **median centering**:

$$
y_{ip}^{\text{norm}} = y_{ip} - \hat\mu_i
$$

with $\hat\mu_i$ the median $\log_2$ intensity over all observed peptides in sample $i$
(`normalize(..., method = "center.median")`). After centering, the marginal distributions line up
far better across samples, though some residual differences remain, attributed to technical
variability.

Two further points are worth holding on to. Microarray analysis typically uses **quantile
normalization**, which forces every quantile — not just the median — to match across samples; in
proteomics this often introduces artefacts, because samples differ in *which* peptides are missing,
and forcing whole distributions to coincide can distort real differences along with technical
ones. If samples also differ in the *width* of their distribution, not just its centre, a more
general robust standardization can be used instead:

$$
y_{ip}^{\text{norm}} = \frac{y_{ip} - \mu_i}{s_i}
$$

### Summarization

Restrict to lab 2, conditions A and E, and the spiked protein P12081 (UniProt entry SYHC_HUMAN).
Plotting each of its peptides' normalized $\log_2$ intensities across those samples shows, all at
once: several peptides contribute to one protein's signal; different peptides sit at very
different absolute intensity levels (a **peptide effect**); peptides are not identified in every
sample (**unbalanced peptide identification**); and a protein's peptides move together within a
sample — peptide intensities from the same protein in the same sample are more alike than the same
peptide's intensities across samples (**pseudo-replication**: they are not independent replicate
measurements of the protein's abundance).

So peptide intensities have to be summarized into a single protein expression value per sample,
and a summarization method that ignores the peptide effect is throwing away structure it should be
using. Several methods are in use:

- **Mean summarization**: $y_{ip} = \beta_i^{\text{samp}} + \epsilon_{ip}$ — a plain average
  across a protein's peptides.
- **Median summarization** — the plain median instead.
- **MaxQuant's maxLFQ** algorithm, computed separately and reported in the `proteinGroups` file.
- **Model-based summarization**: $y_{ip} = \beta_i^{\text{samp}} + \beta_p^{\text{pep}} +
  \epsilon_{ip}$, which explicitly fits and removes the peptide-specific effect $\beta_p^{\text{pep}}$
  before reading off the sample effect $\beta_i^{\text{samp}}$ as the protein's expression estimate.

The default in this course is a **robust, model-based summarization**, via `aggregateFeatures()`:

```r
pe <- aggregateFeatures(pe, i = "peptideNorm", fcol = "Proteins",
                         na.rm = TRUE, name = "protein")
```

Other choices are available through the `fun` argument: Tukey's median polish
(`MsCoreUtils::medianPolish`, an additive two-way decomposition), a robust regression fit with
`MASS::rlm()` (`MsCoreUtils::robustSummary`, the default), or plain `colMeans`, `colMedians` or
`colSums`.

## Software

The course's workflow is implemented in the Bioconductor package `msqrob2`, usable either from R
markdown scripts or through a graphical front end, `msqrob2gui`. The GUI is meant as an entry
point for users with no R experience; writing the analysis as an R markdown script is presented as
the way to keep the analysis — and its reporting — open and reproducible.

## Exercises

1. Compare the different summarization methods available for this dataset — MaxQuant's maxLFQ,
   plain median summarization, and robust model-based summarization — and their advantages and
   disadvantages relative to one another.
2. Before running that comparison, try to anticipate what could go wrong with each summarization
   method.

## Sources

All material is from the *Proteomics Data Analysis* course (statOmics, SGA21/PDA21), converted
from `pda_quantification_preprocessing.Rmd`, CC BY-NC-SA 4.0:

- Course context, outline and audience note —
  [`01-introduction.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd).
- MS-based workflow, level of quantification, the CPTAC spike-in design and MaxQuant output —
  [`02-intro-challenges-in-label-free-quantitative-proteomics.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd).
- `QFeatures` data infrastructure and reading `peptides.txt` into R —
  [`03-import-the-data-in-r.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd).
- Log-transformation, filtering, normalization, summarization, and the chapter's exercise —
  [`04-preprocessing.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd).
- Software (`msqrob2`, `msqrob2gui`) —
  [`05-software-code.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd).

No slide deck or lecture transcript was supplied for this chapter — only the converted course
notes above. The notes point to a video playlist ("Playlist PDA Preprocessing") and to three
papers (Goeminne et al. 2016, Goeminne et al. 2020, Sticker et al. 2020) behind the `msqrob2`
tools; neither the recordings nor the papers themselves were supplied, so their content is not
reproduced here.

---

[← 20. Proteomics Hypothesis Testing and Design](20-proteomics-hypothesis-testing-and-design.md) · [Contents](index.md) · [22. Label-Free Proteomics Data Preprocessing →](22-label-free-proteomics-data-preprocessing.md)
