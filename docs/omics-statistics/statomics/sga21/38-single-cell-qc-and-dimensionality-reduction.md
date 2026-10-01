---
title: "38. Single-Cell QC and Dimensionality Reduction"
course: "StatOmics Sga21"
chapter: 38
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 38. Single-Cell QC and Dimensionality Reduction

## What this covers

This chapter follows one worked pipeline for taking a droplet-based single-cell RNA-seq dataset
from raw, unfiltered counts to a clustered, visualised dataset. It picks up once the counts are
already sitting in a `SingleCellExperiment` (`sce`) — the import step itself is not part of this
material — and answers four questions in order: which cells are worth keeping, how to put the
surviving cells on a comparable scale, which genes are worth looking at, and how to see and label
whatever structure is left. It assumes familiarity with UMI counts and the `SingleCellExperiment`
container, and uses the retina drop-seq dataset of Macosko et al. as its running example throughout.

## Per-cell quality metrics

A droplet-based experiment does not hand you a clean matrix of cells by genes: some "cells" are
really empty droplets that picked up stray RNA, some are two cells stuck together, and some are
real cells that were damaged during preparation. Before anything else can be trusted, each cell
needs to be scored on a few simple summaries, computed per cell across all genes:

- **library size** — the total UMI count for that cell, $\mathrm{sum}$;
- **number of genes detected** — how many distinct genes have at least one read, $\mathrm{detected}$;
- **percentage of mitochondrial reads** — the fraction of a cell's counts coming from a chosen set
  of mitochondrial genes (here, 28 genes matched by the pattern `^MT-`), `subsets_Mito_percent`.

`scater::perCellQCMetrics()` computes all three at once and the result is attached back onto the
`sce` object's `colData`.

The logic behind the third metric is worth stating explicitly, because it is the least obvious of
the three: a cell whose membrane has been perforated loses its free cytoplasmic RNA first, while
the RNA sealed inside mitochondria survives. So a damaged cell looks, in these summaries, like a
cell with **few genes detected and an unusually high mitochondrial percentage** — not low counts
across the board, but a specific, lopsided signature. A high-quality cell, by contrast, should show
many expressed genes and a low mitochondrial contribution.

## Removing damaged cells: adaptive thresholds

Rather than picking a fixed cutoff on each metric in advance, the pipeline flags cells that are
**outliers relative to the rest of the dataset** — `scater::isOutlier()` applied to each metric
separately:

- unusually **low** library size (on the log scale, since library size is strictly positive and
  right-skewed);
- unusually **low** number of detected genes (also log scale);
- unusually **high** mitochondrial percentage.

A cell is discarded if it trips *any* of the three flags:

```r
lowLib      <- isOutlier(df$sum, type = "lower", log = TRUE)
lowFeatures <- isOutlier(df$detected, type = "lower", log = TRUE)
highMito    <- isOutlier(df$subsets_Mito_percent, type = "higher")

discardCells <- (lowLib | lowFeatures | highMito)
```

In this dataset the combined rule removes 3,423 cells, and the majority of those are flagged for
the mitochondrial-percentage criterion rather than for low counts. Plotting detected genes against
mitochondrial percentage, and colouring by `discardCells`, is the check that this isn't an arbitrary
statistical artefact: the discarded cells really do sit apart from the rest, in the low-genes,
high-mito corner the biology predicts.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Scatter of detected genes against mitochondrial read percentage, with the low-gene, high-mito corner flagged for removal">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="210" text-anchor="middle" font-size="12" fill="currentColor">genes detected per cell</text>
  <text x="14" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 14 105)">% UMIs from mitochondrial genes</text>

  <rect x="40" y="20" width="70" height="70" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-dasharray="3 3" stroke-width="1"/>
  <text x="75" y="34" text-anchor="middle" font-size="11" fill="currentColor">discarded</text>

  <g fill="currentColor">
    <circle cx="160" cy="165" r="2.5"/><circle cx="180" cy="172" r="2.5"/>
    <circle cx="200" cy="160" r="2.5"/><circle cx="220" cy="175" r="2.5"/>
    <circle cx="240" cy="168" r="2.5"/><circle cx="260" cy="172" r="2.5"/>
    <circle cx="150" cy="178" r="2.5"/><circle cx="270" cy="160" r="2.5"/>
    <circle cx="190" cy="180" r="2.5"/><circle cx="230" cy="182" r="2.5"/>
    <circle cx="210" cy="170" r="2.5"/><circle cx="285" cy="176" r="2.5"/>
    <circle cx="170" cy="158" r="2.5"/><circle cx="250" cy="180" r="2.5"/>
  </g>
  <g fill="currentColor">
    <circle cx="55" cy="40" r="2.5"/><circle cx="65" cy="55" r="2.5"/>
    <circle cx="80" cy="30" r="2.5"/><circle cx="50" cy="65" r="2.5"/>
    <circle cx="90" cy="45" r="2.5"/><circle cx="70" cy="60" r="2.5"/>
  </g>
</svg>
<figcaption>Damaged cells occupy a specific corner of this plane — few genes detected and a high
mitochondrial fraction — rather than being spread evenly across low counts. The adaptive threshold
is set from the spread of each metric in this particular dataset, not a fixed number chosen up front.</figcaption>
</figure>

## Empty droplets

Most droplets generated in a droplet-based protocol do not contain a cell at all — they pick up a
small amount of "ambient" RNA floating free in the suspension and still get sequenced, producing a
low but non-zero count. Removing cells with a low library size, via the adaptive threshold above,
already discards most of these empty droplets, since real cells generally have far higher UMI
counts than ambient droplets do.

A more direct alternative is a statistical test, `DropletUtils::emptyDrops()`, which checks whether
a barcode's expression profile is distinguishable from the ambient RNA pool rather than just
thresholding on total counts. It needs a lower bound: barcodes below it are treated as definitely
empty and used to characterise what the ambient RNA profile looks like (`test.ambient = TRUE`).

Where does that bound come from? `DropletUtils::barcodeRanks()` ranks all barcodes by total UMI
count and plots count against rank on log-log axes. This curve typically has a **knee**: a steep
drop (real cells, thinning out) followed by a flat low plateau (ambient droplets). `barcodeRanks`
reports an inflection point and a knee point as two candidate automatic cutoffs; here a third value,
350, was chosen by eye and used as the `lower` argument to `emptyDrops`.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Barcode-rank plot: total UMI count falling with rank, with a knee separating real cells from an ambient plateau of empty droplets">
  <line x1="40" y1="195" x2="300" y2="195" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="195" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="212" text-anchor="middle" font-size="12" fill="currentColor">barcode rank (log)</text>
  <text x="14" y="107" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 14 107)">total UMI count (log)</text>

  <rect x="40" y="150" width="260" height="45" fill="currentColor" fill-opacity="0.15"/>
  <text x="220" y="185" text-anchor="middle" font-size="11" fill="currentColor">empty droplets</text>

  <path d="M 48 30 C 100 35, 140 55, 158 90 C 172 118, 182 140, 200 152 C 230 160, 270 163, 292 165"
        fill="none" stroke="currentColor" stroke-width="2"/>

  <line x1="40" y1="95" x2="300" y2="95" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3"/>
  <text x="296" y="91" text-anchor="end" font-size="10" fill="currentColor">inflection</text>

  <line x1="40" y1="128" x2="300" y2="128" stroke="currentColor" stroke-width="1" stroke-dasharray="5 3"/>
  <text x="296" y="124" text-anchor="end" font-size="10" fill="currentColor">knee</text>

  <line x1="40" y1="150" x2="300" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="1 4"/>
  <text x="296" y="146" text-anchor="end" font-size="10" fill="currentColor">chosen by eye (350)</text>
</svg>
<figcaption>Real cells sit on the steep drop of the barcode-rank curve, empty droplets on the flat
low plateau. `barcodeRanks` proposes an inflection point and a knee point as candidate lower
bounds; here a cutoff of 350 UMIs was chosen by eye instead and fed to `emptyDrops`.</figcaption>
</figure>

Running `emptyDrops` with that bound and checking the p-values it assigns to barcodes just under
350 UMIs is one sanity check on the ambient model. But the practical verdict in this dataset was
that thresholding on the resulting FDR (at 0.001) would discard a very large number of cells — more
aggressive than wanted. So the pipeline sticks with the simpler adaptive-threshold filter from the
previous section, and only that filter (`discardCells`) is actually applied to remove cells:
`emptyDrops` is run and inspected, but not used as the final filter here.

## Doublets

A **doublet** is a droplet that captured two (or more) cells rather than one, producing a hybrid
transcriptome that can look, superficially, like a novel cell type. `scDblFinder` estimates a
per-cell doublet score and a `doublet`/`singlet` classification. Because the expected doublet rate
and cell-type mix can differ between samples, the detector is run **per sample**
(`samples = factor(sampleID)`), not pooled across the whole dataset.

The diagnostic step is to see whether flagged doublets concentrate in particular clusters — plotting
`log1p(scDblFinder.score)` against the existing cluster labels, and the fraction of doublets per
cluster as a bar chart — since a cluster that is disproportionately doublets is a candidate false
population rather than a genuine cell type. Cells classified as doublets are then removed.

## Normalisation: size factors

Even after filtering, cells differ in total sequencing depth for reasons that have nothing to do
with biology — that variation has to be scaled out before expression levels are compared across
cells. The normalisation used here is the simplest version of this idea: a **size factor** per cell
that is just its scaled library size. Writing $Y_{gi}$ for the count of gene $g$ in cell $i$,

$$
N_i = \sum_g Y_{gi}, \qquad s_i = \frac{N_i}{\bar N},
$$

where $\bar N$ is the mean library size over all cells — so that the size factors themselves
average to 1 across the dataset. `scater::logNormCounts()` divides each cell's counts by its size
factor and log-transforms the result, storing it as a new `logcounts` assay alongside the raw
`counts`. The size factors can be pulled out directly with `librarySizeFactors()`; since they are,
by construction, exactly proportional to each cell's raw total count, plotting one against the
other is just a check that the scaling did what it says.

## Feature selection: highly variable genes

Not every gene is worth carrying into a dimensionality reduction: most of a gene's variance across
cells, especially at low expression, is just Poisson counting noise rather than biology.
`scran::modelGeneVar()` fits a trend of variance against mean log-expression across all genes — the
expected, largely technical relationship — and genes that sit well above that trend are the ones
whose variance is more than counting noise can explain: the **highly variable genes** (HVGs).

```r
dec <- modelGeneVar(sce)
hvg <- getTopHVGs(dec, prop = 0.1)   # top 10% by biological variance
```

`getTopHVGs()` here keeps the top 10% of genes by this criterion. Plotting mean against variance for
every gene, with the fitted trend overlaid and the selected genes coloured separately, is the check
that the selection is really picking out genes that depart from the trend rather than an arbitrary
top-10%-by-mean list.

## From genes to a picture: dimensionality reduction

A dataset with thousands of genes cannot be looked at directly, so the next question is how to
project it down to something visualisable while keeping as much real structure as possible. Every
plot in this section colours cells by their **true**, previously known cell-type label — this is
only possible because the label happens to be available for evaluation; in a real unsupervised
analysis at this stage, it would not be.

**The crudest possible reduction** is just to plot the two most informative genes (from feature
selection) against each other. Even this already separates cell types partially — evidence that the
structure really is there in the expression data, before any reduction method is applied at all.

### Linear reduction: PCA

Running PCA on the HVG-restricted expression matrix, keeping 30 components, recovers substantially
more structure than the two-gene plot, but plotting the first two components still leaves many cell
populations overlapping and the display overcrowded — 30 components is more than two dimensions can
show. The pipeline also reruns PCA using *all* genes rather than just the HVGs, as a direct
comparison of what feature selection buys before reduction.

Ordinary PCA finds a low-rank approximation that minimises squared error on the (log-transformed)
data — implicitly treating it as roughly continuous. `glmpca` generalises this to let the
reconstruction error come from a distribution matched to the data instead, fitting a low-rank
representation directly against the **raw counts** under a chosen exponential-family likelihood.
Here it is fit with a Poisson likelihood and two latent factors, optimised approximately via
stochastic minibatches for scalability:

```r
poipca <- glmpca(assays(sce)$counts[hvg,], L = 2, fam = "poi", minibatch = "stochastic")
```

### Non-linear reduction: UMAP

UMAP is run not on the raw expression matrix but on top of the 30-dimensional PCA embedding
(`dimred = 'PCA'`), reducing that space further down to two dimensions for plotting. Because it
preserves local neighbourhood structure rather than global linear variance, it typically pulls cell
populations apart more cleanly in two dimensions than a straight PCA projection does.

## Clustering: graphs and communities

Dimensionality reduction to two dimensions is for looking at the data, not for assigning labels.
The clustering itself is done back in the higher-dimensional PCA space, not the 2-D UMAP coordinates
used for plotting:

1. **Build a graph.** `buildSNNGraph(sce, use.dimred = 'PCA')` constructs a shared nearest-neighbour
   (SNN) graph: cells become nodes, and cells with substantially overlapping neighbourhoods in PCA
   space are connected.
2. **Detect communities.** Louvain clustering (`igraph::cluster_louvain()`) partitions this graph
   into groups that are more densely connected internally than to the rest of the graph — no
   distance threshold or fixed number of clusters is specified in advance.

The resulting cluster labels are then overlaid on the UMAP plot purely for visualisation; the
clustering itself never used the UMAP coordinates.

## Sources

- Per-cell QC metrics, adaptive-threshold filtering, empty-droplet detection via `barcodeRanks` and
  `emptyDrops`, doublet detection via `scDblFinder`, library-size-factor normalisation, and feature
  selection via `modelGeneVar`/`getTopHVGs` — `singleCell_MacoskoWorkflow/02-quality-control.md`
  (statOmics SGA21, `singleCell_MacoskoWorkflow.Rmd`, CC BY-NC-SA 4.0).
- The basic two-gene plot, linear PCA (with and without feature selection), Poisson GLM-PCA via
  `glmpca`, UMAP, and SNN/Louvain clustering — `singleCell_MacoskoWorkflow/03-dimensionality-reduction.md`
  (same source).
- The overall framing — that this is the Macosko et al. workflow, split into a quality-control
  section and a dimensionality-reduction section — comes from the section index,
  `singleCell_MacoskoWorkflow/index.md` (same source).
- Not included in the supplied material: the import step itself (linked from the quality-control
  page as "Import data" but not converted here), and the earlier exercise that first loads this
  dataset via `scRNAseq::MacoskoRetinaData()` and introduces the `sce` object and its `cluster`
  ground-truth labels (`singleCell_intro1.md`, same course).

---

[← 36. Single-Cell RNA-Seq: A First Look](36-single-cell-rna-seq-a-first-look.md) · [Contents](index.md) · [39. Variance-Stabilizing Transformation for Poisson Counts →](39-variance-stabilizing-transformation-for-poisson-counts.md)
