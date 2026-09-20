---
title: "22. Label-Free Proteomics Data Preprocessing"
course: "StatOmics Sga21"
chapter: 22
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Label-Free Proteomics Data Preprocessing

## What this covers

Mass-spectrometry proteomics measures peptide *intensities*, but the biological question is
usually about protein abundance, and a protein is not measured directly — it is inferred from a
patchwork of peptides that are themselves incompletely and unevenly detected. This chapter asks
what makes that inference hard (missingness, peptide-to-peptide variability, ambiguous
peptide-protein mapping), how the raw MaxQuant output is organised in R once it is imported, and
what the four standard preprocessing steps — log-transformation, filtering, normalisation,
summarisation — are for and why each is done the way it is. It assumes only familiarity with basic
regression ($y = \beta + \epsilon$) and log arithmetic; no prior proteomics is assumed.

## Why label-free quantification is hard

In a label-free MS run, a sample's proteins are digested into peptides (commonly with trypsin),
the peptides are ionised and separated, and a mass spectrometer records precursor ion intensities
(MS1) and fragments a subset of them for identification (MS2). Several features of this process
work against clean quantification:

- **Modifications.** A peptide can carry post-translational modifications, so the "same" peptide
  sequence can appear at several measured masses.
- **Ionisation efficiency varies hugely from peptide to peptide.** Two peptides present at the same
  molar amount need not give the same measured intensity, so intensities are not comparable
  *across* peptides — only a peptide's own intensity across samples is informative about its
  relative change.
- **Identification is imperfect.** Misidentified spectra become outliers in the data, and because
  MS2 fragmentation (needed for identification) is only attempted on a subset of ions, which
  peptides get identified in a given run depends on peptide abundance. Missingness is therefore
  not random — it is context-dependent and abundance-related, not a coin flip.

The combined effect is unbalanced peptide identification across samples and, correspondingly,
messy data: some peptides are seen everywhere, most are seen in only some samples, and the pattern
of "seen/not seen" is itself informative rather than nuisance noise.

### From peptides to proteins

MS-based proteomics returns peptides — fragments of proteins — but the quantity of interest is
almost always at the protein level. Getting from one to the other requires aggregating many
peptide measurements, produced from many spectra, into one number per protein per sample. That
aggregation is not always unambiguous: a peptide sequence can be shared between several proteins,
and a decision has to be made about which protein group it is credited to.

<figure>
<svg viewBox="0 0 420 260" role="img" aria-label="Spectra aggregate into peptides, and peptides aggregate into proteins, with a shared peptide assigned by the razor rule">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="55" y="8" text-anchor="middle" font-size="12" fill="currentColor">spectra</text>
  <text x="235" y="8" text-anchor="middle" font-size="12" fill="currentColor">peptides</text>
  <text x="375" y="8" text-anchor="middle" font-size="12" fill="currentColor">protein groups</text>

  <rect x="20" y="10" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="20" y="35" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="20" y="60" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="20" y="100" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="20" y="125" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="20" y="175" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="20" y="200" width="70" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <rect x="190" y="25" width="90" height="26" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="235" y="42" text-anchor="middle" font-size="11" fill="currentColor">peptide 1</text>
  <rect x="190" y="100" width="90" height="26" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="235" y="117" text-anchor="middle" font-size="11" fill="currentColor">peptide 2</text>
  <rect x="190" y="175" width="90" height="26" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="235" y="192" text-anchor="middle" font-size="11" fill="currentColor">peptide 3 (shared)</text>

  <rect x="340" y="50" width="70" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="375" y="70" text-anchor="middle" font-size="11" fill="currentColor">protein A</text>
  <rect x="340" y="175" width="70" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="375" y="195" text-anchor="middle" font-size="11" fill="currentColor">protein B</text>

  <line x1="90" y1="20" x2="190" y2="38" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="90" y1="45" x2="190" y2="38" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="90" y1="70" x2="190" y2="38" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="90" y1="110" x2="190" y2="113" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="90" y1="135" x2="190" y2="113" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="90" y1="185" x2="190" y2="188" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="90" y1="210" x2="190" y2="188" stroke="currentColor" marker-end="url(#arrow)"/>

  <line x1="280" y1="38" x2="340" y2="67" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="280" y1="113" x2="340" y2="67" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="280" y1="188" x2="340" y2="67" stroke="currentColor" marker-end="url(#arrow)"/>
  <line x1="280" y1="188" x2="340" y2="192" stroke="currentColor" stroke-dasharray="4 3"/>
</svg>
<figcaption>Spectra are summarised into peptides, and peptides into proteins. Peptide 3 could be
credited to protein A or protein B; the razor rule assigns it to the larger group (protein A,
solid line) and drops the alternative (dashed).</figcaption>
</figure>

This hierarchy — spectra below peptides below proteins — is exactly what the R data structure
introduced below (`QFeatures`) is built to track: every assay is linked to the one below it, and
the relations survive filtering and aggregation.

## The CPTAC spike-in benchmark

The workflow is illustrated throughout on a CPTAC spike-in study, whose design is worth stating
because it explains both why the dataset is trusted and why missingness is still severe even in
close-to-ideal conditions:

- Every sample shares the same trypsin-digested **yeast** proteome background.
- A trypsin-digested **Sigma UPS1 standard** — 48 distinct human proteins — is spiked into that
  background at five concentrations, labelled conditions A–E ($0.25, 0.74, 2.22, 6.67, 20$
  fmol/l). Since only these 48 proteins are supposed to differ between conditions, any other
  protein that appears to change is evidence of a technical artefact rather than biology.
- Samples were run repeatedly, on different instruments in different labs.

Even in this controlled setting, after a MaxQuant search with the "match between runs" option,
only 41% of all proteins and 6.6% of all peptides were quantified in *every* sample. Missingness
is therefore not an edge case to be patched over — it is the dominant feature of the data that
every downstream step has to be designed around.

## Getting the data into R: the `QFeatures` object

MaxQuant's search output is a set of tables, one of which — `peptides.txt` — holds MS1
intensities summarised at the peptide level, with one column per sample. In R, this is loaded into
a `QFeatures` object (built on the `SummarizedExperiment` / `MultiAssayExperiment` classes), which
stores several *assays* — here, initially just the raw peptide intensities (`"peptideRaw"`) — and
keeps the hierarchical relations between them (proteins built from peptides, peptides from
spectra) so that later aggregation steps can track back down to the original measurements.

Within the object, `rowData` carries per-feature information (peptide sequence, which protein(s) it
maps to, ...) and `colData` carries per-sample information. Neither the peptide table nor the
default import knows anything about the experimental design, so it has to be added by hand. In the
CPTAC data, sample names encode both the spike-in condition (a fixed character position in the
column name) and, by convention, which lab ran the sample — samples 1–3 came from lab 1, 4–6 from
lab 2, 7–9 from lab 3, and this pattern repeats for each of the five conditions. That information
is written into `colData` before anything else is done, since every later plot and every model
compares samples by exactly these labels (lab, condition, spike concentration).

## Preprocessing: four steps, in order

Four things are routinely done to peptide intensities before they are fit to a statistical model:
log-transformation, filtering, normalisation, and summarisation to the protein level. Each solves
a specific, demonstrable problem in the raw data; none of them is cosmetic.

### Log-transformation: taming a multiplicative error

Plotting the raw intensity of a single peptide (AALEELVK, from a spiked UPS protein) against its
known spike-in concentration, restricted to one lab, shows the spread of the intensities growing
as the concentration — and hence the mean intensity — grows. This is a *multiplicative* error
structure: the noise scales with the signal, rather than sitting on top of it at constant size.
Re-plotting both axes on a $\log_2$ scale removes this pattern: the vertical spread becomes roughly
constant across concentrations, i.e. the data are **homoscedastic on the log scale**. That is the
whole justification for working with $\log_2$ intensities throughout quantitative proteomics
rather than raw ones — it converts a variance that depends on the mean into one that (roughly)
does not, which is the condition ordinary linear models and their standard errors assume.

Working on the $\log_2$ scale has a second, very convenient consequence: differences of
log-intensities are $\log_2$ fold changes,
$$
\log_2 B - \log_2 A = \log_2 \frac{B}{A} = \log FC_{B-A},
$$
so that
$$
\log_2 FC = 1 \iff FC = 2^1 = 2, \qquad \log_2 FC = 2 \iff FC = 2^2 = 4 .
$$
A model fit on the log scale therefore reports fold changes directly, as differences of estimated
effects, rather than ratios.

Before transforming, it is worth recording, for every peptide, how many samples it was observed
in at all (its number of non-zero intensities) — this count is reused for filtering below. A raw
intensity of exactly zero does not mean "zero abundance"; it means the peptide was not detected,
i.e. it is *missing*, and must be recoded as `NA` (rather than a numeric 0) before the log
transform — $\log_2(0)$ is not defined, and treating a non-detection as a real small value would
misrepresent it as data.

### Filtering: removing entries that should not count

Several categories of peptide/protein entries are removed before any modelling, because they are
not trustworthy measurements of a real peptide's abundance: reverse (decoy) sequences used
internally for quality control, peptides identified only by a modification site, contaminants,
peptides with very few identifications across samples, and proteins backed by only one or a
handful of peptides.

The guiding principle behind all of this is: **filtering does not bias the downstream analysis, as
long as the filtering criterion is independent of what is being compared downstream.** Removing
peptides because they are decoys, or because a sample simply failed to detect them at all, does
not favour one condition over another; removing them because of how they behaved in the very
comparison being tested would.

Three concrete filtering steps are applied here:

1. **Overlapping protein groups.** A peptide sequence is allowed to map to several proteins, but
   only as long as none of those candidate proteins is *already* covered, on its own, by a
   smaller, more specific protein group elsewhere in the data — the shared "razor" peptide (see
   the figure above) is credited to the protein group with the most other supporting peptides, and
   the smaller/redundant groups are dropped.
2. **Decoys and contaminants.** Reverse sequences (search decoys) and peptides flagged as
   potential contaminants are removed outright — they are search-engine bookkeeping, not
   biological signal.
3. **Singleton peptides.** Peptides observed as non-zero in fewer than two samples are dropped,
   using the non-zero count recorded before the log transform. A peptide seen only once gives no
   way to judge whether the measurement is reproducible.

### Normalisation: putting samples on a common scale

Plotting the distribution of log-intensities across samples — either all samples that share a
spike-in condition, or all samples that share a lab — shows that even in this very clean,
essentially two-component dataset (one shared background, 48 proteins that are allowed to differ),
the *marginal* distribution of peptide intensities is noticeably different from sample to sample:
there are consistent shifts between labs and between replicates within a lab, and between samples
run at different spike-in concentrations. None of this is meant to be biology — it is loading
differences, instrument drift, and similar technical effects — so it has to be removed before
samples are compared.

The natural summary statistic to remove is a location shift per sample, and the choice of *which*
location statistic matters. A mean is very sensitive to outliers: in a well-known survey result
(Miller and Fishkin, 1997) on the number of partners people would like to have over a 30-year
period, the reported *means* were wildly different between sexes (64.3 vs 2.8), yet the *median*
for both was 1 — a small number of extreme responses can drag a mean far from what is typical of
the bulk of the data. The same risk applies to a sample of peptide intensities: a handful of very
high-abundance peptides could dominate a mean-based correction. Normalisation is therefore done by
**median centering**: for every sample $i$, subtract that sample's median log-intensity
$\hat\mu_i$ (taken over all peptides observed in that sample) from every peptide intensity in the
sample,
$$
y_{ip}^{\text{norm}} = y_{ip} - \hat\mu_i .
$$

After this correction the marginal distributions of the samples line up much more closely,
although not perfectly — some residual technical variability remains. Two further points are worth
holding on to. First, **quantile normalisation**, standard in microarray analysis, goes further
and forces every quantile (not just the median) to match across samples; in proteomics this
routinely introduces artefacts, because samples differ in *which* peptides are missing, so forcing
every quantile to agree treats structurally different sets of observed features as if they were
the same set. Second, if it is not just the *centre* but also the *spread* of the distribution that
differs between samples, both can be corrected at once with a robust location-and-scale
standardisation,
$$
y_{ip}^{\text{norm}} = \frac{y_{ip} - \mu_i}{s_i} .
$$

### Summarisation: from peptide to protein

Plotting several peptides that all belong to one spiked protein (P12081), within one lab and two
conditions, shows two things at once. First, the peptides sit at very different absolute
intensities from each other — a **peptide effect**: some peptides are simply detected more
efficiently than others, a property of the peptide, not of the sample. Second, and more subtly,
the peptide intensities belonging to *the same protein in the same sample* move together — they
are correlated, because they share one underlying protein abundance and one preparation history —
while intensities of that protein *between* samples are comparatively less alike. This is
**pseudo-replication**: several peptide measurements of one protein in one sample are not
independent replicate measurements of that protein's abundance, and treating them as if they were
would understate the true uncertainty of the resulting protein-level number.

The fix is to summarise every protein's peptide intensities, sample by sample, into a single
protein expression value. Several summarisation methods are in use:

- **Mean summarisation** — average the peptide log-intensities for a protein in a sample. This
  amounts to fitting the one-way model $y_{ip} = \beta_i^{\text{samp}} + \epsilon_{ip}$ and
  reading off $\beta_i^{\text{samp}}$ as the protein summary; it gives every peptide equal weight
  and makes no correction for a peptide's own baseline level.
- **Median summarisation** — the same idea, robust to a single outlying peptide.
- **MaxQuant's maxLFQ** — computed by MaxQuant itself and reported in its protein groups file,
  using a different, intensity-ratio-based algorithm.
- **Model-based summarisation** — explicitly account for the peptide effect by fitting the
  two-way model
  $$
  y_{ip} = \beta_i^{\text{samp}} + \beta_p^{\text{pep}} + \epsilon_{ip},
  $$
  so that each peptide's own systematic offset ($\beta_p^{\text{pep}}$) is estimated and removed
  before the sample effect ($\beta_i^{\text{samp}}$, the protein summary) is read off. Fitting this
  robustly — with Tukey's median polish, or with a robust regression such as `MASS::rlm` — keeps a
  handful of outlying peptide/sample combinations from distorting the estimate; a robust version of
  this model is the default summarisation method used by `aggregateFeatures` in this workflow.

## Exercises

From the course material (tutorial session, following this lecture):

1. Evaluate the different protein summarisation methods discussed above — MaxQuant's maxLFQ,
   median summarisation, and robust model-based summarisation — on the CPTAC dataset, and compare
   their advantages and disadvantages.
2. Before running that comparison: what problems would you anticipate arising from summarising
   several peptide intensities into one protein value?

## Sources

- All material in this chapter comes from the lecture "Intro: Challenges in Label-Free Quantitative
  Proteomics" in the statOmics SGA21 course (Statistical Genomics Analysis), converted from
  `pda_quantification_preprocessing_noframes.Rmd`:
  - Challenges, the peptide/protein hierarchy, and the CPTAC spike-in design —
    `01-intro-challenges-in-label-free-quantitative-proteomics.md`.
  - The `QFeatures` data structure, reading `peptides.txt`, and building the sample design
    (`colData`) — `02-import-the-data-in-r.md`.
  - Log-transformation, filtering, normalisation, and summarisation, including the worked
    peptide/protein examples and the two exercises above — `03-preprocessing.md`.
- The lecture's slides referenced several figures generated by `knitr::include_graphics()`
  (e.g. `ProteomicsWorkflow.png`, `challenges_peptides.png`, `SE.png`, `partners.png`) and R plots
  built from the CPTAC dataset; the images themselves were not part of the converted material used
  here, so the diagram above and the descriptions of the plots are reconstructed from the
  surrounding bullet text and code comments only, not from having seen the images.
- The Miller and Fishkin (1997) survey figures are quoted in the slides as-is; no further citation
  for that study was given in the source material.
- No transcript or separate slide PDF was supplied for this lecture — only the converted markdown
  notes listed above.

---

[← 21. Preprocessing Quantitative Proteomics Data](21-preprocessing-quantitative-proteomics-data.md) · [Contents](index.md) · [23. Peptide-Level Models for Summarization →](23-peptide-level-models-for-summarization.md)
