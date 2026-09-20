---
title: "2. From Peptides to Differential Expression"
course: "StatOmics Sga21"
chapter: 2
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. From Peptides to Differential Expression

## What this covers

This chapter works through a complete differential-expression analysis of a proteomics dataset,
from the raw output of a peptide search engine to a short list of proteins whose abundance differs
between two patient groups. It follows one dataset end to end — eighteen breast-cancer proteomes
assessed by mass spectrometry — through import, preprocessing, statistical modelling, and the plots
used to report and sanity-check the result. It assumes some familiarity with linear regression and
hypothesis testing, and with the basic vocabulary of shotgun proteomics (peptide, protein group,
intensity).

## The dataset

Eighteen estrogen-receptor-positive breast cancer tissues, from patients treated with tamoxifen
upon recurrence, were assessed in a proteomics study. Nine patients had a good outcome ("or") and
nine had a poor outcome ("pd"). The proteomes were measured on an LTQ-Orbitrap mass spectrometer,
and the resulting raw files were searched with MaxQuant (version 1.4.1.2) against the human
canonical proteome (FASTA version 2012-09).

The question the rest of the chapter answers is the standard one in this kind of study: **which
proteins are differentially abundant between the good-outcome and poor-outcome groups?**

A MaxQuant search produces a `peptides.txt` file of peptide-level intensities (by default found in
`path_to_raw_files/combined/txt/`), one row per peptide and one column per sample. This is where
the analysis starts — not from protein-level intensities directly, because a protein's abundance
has to be reconstructed from the peptides that were actually detected for it, and that
reconstruction is itself part of the pipeline (see *Summarizing peptides to proteins*, below).

## Getting the data into R

The `QFeatures` package represents the experiment as a single object that can hold several linked
versions of the same features — raw, log-transformed, normalized, aggregated to protein — side by
side, together with sample-level metadata. `readQFeatures` builds this object directly from
`peptides.txt`; `grep` on the column names is used first to identify which columns hold intensities
(they are all named `Intensity.<something>`):

```r
ecols <- grep("Intensity\\.", names(read.delim(peptidesFile)))

pe <- readQFeatures(
  table = peptidesFile,
  fnames = 1,
  ecol = ecols,
  name = "peptideRaw", sep = "\t")
```

The sample outcome (`or`/`pd`) is not a separate column of `peptides.txt`; it is encoded inside the
sample names themselves, so it has to be pulled out with a string operation and attached as a
factor in the object's sample metadata:

```r
colData(pe)$outcome <- substr(colnames(pe[["peptideRaw"]]), 11, 12) %>% unlist %>% as.factor
```

Two more quantities are computed before any transformation of the intensities happens, because
both are needed later, for filtering:

- `nNonZero`, the number of samples in which a given peptide has a non-zero intensity —
  `rowSums(assay(pe[["peptideRaw"]]) > 0)`.
- the zero intensities themselves are converted to `NA`. A recorded intensity of exactly zero is
  not a peptide that truly has zero abundance; it is a peptide the search engine failed to detect
  in that sample. Treating it as a genuine measurement of zero would be wrong, so it is recoded as
  missing: `pe <- zeroIsNA(pe, "peptideRaw")`.

Once this is done, a first look at the data matters as much as any later step: a substantial
fraction of all peptide intensities are missing, and for some peptides there is no signal at all,
in any sample. A preprocessing pipeline for this kind of data has to deal with that missingness
rather than pretend it isn't there — which the filtering step, below, is partly for.

## Preprocessing

### Putting intensities on the log scale

The first step is a base-2 log transformation of the raw, peptide-level intensities:

```r
pe <- logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")
```

This creates a new, parallel assay (`peptideLog`) inside the same object rather than overwriting
the raw one — the `QFeatures` object keeps every stage of the pipeline addressable by name, which
is what later lets the detail plots go back and compare a peptide's raw and processed values side
by side.

### Filtering

Filtering removes rows of the data that should not be trusted, or should not be counted twice, in
three separate passes.

**Overlapping protein groups.** A peptide can map to more than one protein — its sequence occurs in
several proteins at once — and it is only kept if none of those proteins is already covered by some
other, smaller group of proteins that the peptide is also consistent with. Practically, each
peptide is assigned to the *smallest* unique group of proteins it is compatible with, via
`smallestUniqueGroups`, and ambiguous assignments that cannot be resolved this way are dropped:

```r
pe <- filterFeatures(pe, ~ Proteins %in% smallestUniqueGroups(rowData(pe[["peptideLog"]])$Proteins))
```

**Decoys and contaminants.** Peptides matching reverse (decoy) sequences, and known contaminant
proteins, are removed:

```r
pe <- filterFeatures(pe, ~ Reverse != "+")
pe <- filterFeatures(pe, ~ Contaminant != "+")
```

A further filter — dropping proteins that were only identified via peptides carrying a chemical
modification — is skipped in this run, because it needs the larger protein-groups file, which was
not used here. This is left as a genuine gap in the pipeline as run, not a step judged unnecessary.

**Peptides seen in only one sample.** A peptide's intensity is only informative about
between-sample differences if it was actually detected more than once. Peptides observed in fewer
than two samples are dropped:

```r
pe <- filterFeatures(pe, ~ nNonZero >= 2)
```

### Normalizing by median centering

Even after filtering, samples can differ in overall intensity for reasons that have nothing to do
with the biology — how much material was loaded, day-to-day differences in the instrument. Median
centering removes this per-sample shift by subtracting, from every peptide intensity in a sample,
that sample's own median intensity over all of its observed peptides:

$$y_{ip}^{\text{norm}} = y_{ip} - \hat\mu_i$$

where $\hat\mu_i$ is the median intensity across peptides in sample $i$. After this step the
per-sample density curves of intensity line up with one another — a rough check that the procedure
did what it was meant to — and a multidimensional scaling (MDS) plot can be used to look at the
overall structure of the samples, with its first axis showing the leading log fold changes between
them.

### Summarizing peptides to proteins

The last step of preprocessing collapses the (now normalized) peptide-level intensities into one
value per protein per sample, by robust aggregation of the peptides belonging to each protein
group:

```r
pe <- aggregateFeatures(pe, i = "peptideNorm", fcol = "Proteins", na.rm = TRUE, name = "proteinRobust")
```

"Robust" here is the default behaviour of `aggregateFeatures`: the summary for a protein is not
simply an average of its peptides' intensities — a peptide whose intensity is out of line with the
others mapping to the same protein contributes less to the protein-level summary than the rest do.
The same MDS diagnostic used on the peptide-level data is repeated here, on the protein-level
assay.

## Modelling and testing for differential abundance

### Fitting the model

`msqrob2` fits, for every protein, a regression of log2 protein intensity on the experimental
factor of interest — here, outcome:

```r
pe <- msqrob(object = pe, i = "proteinRobust", formula = ~ outcome)
```

By default this regression is also robust: a protein's fit is not thrown off by one peptide-poor
sample, or one badly-behaved observation, in the way an ordinary least-squares fit would be.

### The contrast that answers the question

Before writing down a contrast it is worth checking what the model's parameters actually are.
`getCoef(rowData(pe[["proteinRobust"]])$msqrobModels[[1]])` lists them for one protein's fit, and
`ExploreModelMatrix::VisualizeDesign(colData(pe), ~outcome)` draws the design matrix they belong to.

`outcome` has two levels, `or` and `pd`; the default treatment coding takes the alphabetically
first level, `or` (the good-outcome group), as the reference. The fitted model therefore has two
parameters: an intercept, which is the mean log2 protein expression in the good-outcome group, and
a parameter `outcomePD`, added to the intercept to get the mean log2 expression in the poor-outcome
group. `outcomePD` is exactly the log2 fold change between the poor-outcome and good-outcome
groups — so the biological question "does this protein differ between the two outcomes?" becomes
the statistical question "is `outcomePD` different from zero?", tested as the contrast
`outcomePD = 0`:

```r
L <- makeContrast("outcomePD = 0", parameterNames = c("outcomePD"))
pe <- hypothesisTest(object = pe, i = "proteinRobust", contrast = L)
```

This attaches, to every protein's row of data, an estimated log fold change (`logFC`), a
$p$-value, and a multiple-testing-adjusted $p$-value (`adjPval`).

## Reading and checking the result

### Volcano plot

A volcano plot puts the estimated fold change on one axis against statistical significance on the
other, so that proteins that are both large in effect and confidently detected stand out from
proteins that are merely noisy:

```r
volcano <- ggplot(rowData(pe[["proteinRobust"]])$outcomePD,
                   aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
  geom_point(cex = 2.5) +
  scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
```

Proteins declared significant at the 5% false discovery rate (`adjPval < 0.05`) are highlighted in
the plot.

### Heatmap

The significant proteins' names are extracted, and a heatmap of their protein-level intensities
across all eighteen samples gives a second view of the same result — whether the significant
proteins actually separate the two outcome groups, rather than merely happening to pass the
threshold:

```r
sigNames <- rowData(pe[["proteinRobust"]])$outcomePD %>%
  rownames_to_column("proteinRobust") %>%
  filter(adjPval < 0.05) %>%
  pull(proteinRobust)
heatmap(assay(pe[["proteinRobust"]])[sigNames, ])
```

### Detail plots

The most useful check is going back down a level, from the protein-level summary to the individual
peptides that produced it. For each of the first few significant proteins, the peptide-level
(`peptideNorm`) and protein-level (`proteinRobust`) values for that protein are pulled out together
and plotted twice: once as a line plot of each peptide's intensity across all eighteen samples,
faceted by level, to see whether the underlying peptides move together or the "significant" call is
driven by a handful of outliers; and once as a boxplot of intensities grouped by outcome, which is
the most direct picture of whether the two outcome groups actually separate for that protein.

<figure>
<svg viewBox="0 0 860 190" role="img" aria-label="Pipeline from raw peptide intensities to a tested list of differentially abundant proteins">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g font-size="12" fill="currentColor">
    <rect x="15" y="60" width="115" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="72" y="86" text-anchor="middle">Raw peptide</text>
    <text x="72" y="102" text-anchor="middle">intensities</text>

    <rect x="160" y="60" width="115" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="217" y="86" text-anchor="middle">0 &#8594; NA,</text>
    <text x="217" y="102" text-anchor="middle">log2</text>

    <rect x="305" y="60" width="115" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="362" y="80" text-anchor="middle">Filter groups,</text>
    <text x="362" y="96" text-anchor="middle">decoys,</text>
    <text x="362" y="112" text-anchor="middle">coverage</text>

    <rect x="450" y="60" width="115" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="507" y="86" text-anchor="middle">Median-center</text>
    <text x="507" y="102" text-anchor="middle">normalize</text>

    <rect x="595" y="60" width="115" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="652" y="86" text-anchor="middle">Aggregate to</text>
    <text x="652" y="102" text-anchor="middle">protein (robust)</text>

    <rect x="740" y="60" width="105" height="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
    <text x="792" y="86" text-anchor="middle">msqrob fit +</text>
    <text x="792" y="102" text-anchor="middle">contrast test</text>

    <line x1="130" y1="90" x2="158" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
    <line x1="275" y1="90" x2="303" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
    <line x1="420" y1="90" x2="448" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
    <line x1="565" y1="90" x2="593" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
    <line x1="710" y1="90" x2="738" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  </g>
</svg>
<figcaption>The pipeline this chapter follows: every arrow is a step that changes what a "peptide" or
"protein" value means, from a raw MaxQuant intensity to a tested log fold change.</figcaption>
</figure>

## Sources

- `docs/omics-statistics/statomics/sga21/cancer2_6x6/01-data.md` — dataset description, import via
  `QFeatures`/`readQFeatures`, the `outcome` factor, `nNonZero`, and `zeroIsNA`.
- `docs/omics-statistics/statomics/sga21/cancer2_6x6/02-preprocessing.md` — log transformation, the
  three filtering steps, median-centering normalization, MDS diagnostics, and `aggregateFeatures`.
- `docs/omics-statistics/statomics/sga21/cancer2_6x6/03-data-analysis.md` — `msqrob` model fitting,
  the design and contrast, `hypothesisTest`, the volcano plot, heatmap, and detail plots.

All three files convert the same source, `cancer2_6x6.Rmd` from the statOmics SGA21 course
(licensed CC BY-NC-SA 4.0). Two things the source points to but does not itself contain: reference
`[6]`, cited in `01-data.md` for the MaxQuant search, without a full citation; and the
`peptides6vs6.txt` data file, and the larger protein-groups file needed for the modified-peptide
filtering step, both hosted externally on the `statOmics/SGA2020` GitHub data branch rather than
supplied here.

---

[← 1. The MSqRob Statistical Model](01-the-msqrob-statistical-model.md) · [Contents](index.md) · [3. CPTAC Spike-In Case Study →](03-cptac-spike-in-case-study.md)
