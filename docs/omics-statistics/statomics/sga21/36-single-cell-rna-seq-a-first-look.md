---
title: "36. Single-Cell RNA-Seq: A First Look"
course: "StatOmics Sga21"
chapter: 36
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 36. Single-Cell RNA-Seq: A First Look

## What this covers

This chapter is the first hands-on encounter with single-cell RNA-sequencing (scRNA-seq) data in
the course: loading a real scRNA-seq dataset in R/Bioconductor, inspecting how it is stored, and
turning the same visualisation tools already used for bulk RNA-seq — PCA and multidimensional
scaling (MDS) — on it to see how well they recover known biological structure. It assumes the
reader already knows how to build and read a PCA or MDS plot from a bulk RNA-seq count matrix, and
is comfortable with the standard Bioconductor container classes for expression data.

## The dataset: a mouse retina, one cell at a time

The practical works with `MacoskoRetinaData()`, a dataset shipped in the Bioconductor package
`scRNAseq`. Where a bulk RNA-seq experiment gives one expression profile per sample — a pool of
many cells averaged together — this dataset gives one expression profile per individual mouse
retina cell.

```r
if(!"BiocManager" %in% installed.packages()[,1]){
  install.packages("BiocManager")
}
if(!"scRNAseq" %in% installed.packages()[,1]){
  BiocManager::install("scRNAseq")
}
```

```r
suppressPackageStartupMessages(library(scRNAseq))
sce <- MacoskoRetinaData()
sce
class(sce)
counts(sce)[1:5,1:5]
head(colData(sce))

# filter cells
sce <- sce[,!is.na(colData(sce)$cluster)]
sce
```

`sce` is returned as a `SingleCellExperiment`, the standard Bioconductor container for single-cell
data. It behaves the way a `SummarizedExperiment` does for bulk data, with one change that matters
for everything that follows:

- `counts(sce)` is the expression matrix, but its columns are now individual cells rather than bulk
  samples — printing `counts(sce)[1:5,1:5]` shows the first five genes against the first five
  cells.
- `colData(sce)` is the per-column (per-cell) metadata. Here it carries a `cluster` column: a label
  of which cell type or cluster each cell belongs to.
- Not every cell has a cluster label. The line `sce <- sce[,!is.na(colData(sce)$cluster)]` drops
  the cells whose `cluster` entry is `NA`, keeping only the labelled ones — which is what makes it
  possible, later, to colour a plot by cluster and check whether the plot's structure matches the
  label.

That `cluster` column is the ground truth the rest of the exercise checks itself against: if a
visualisation method is doing its job, cells that share a label should end up close together, and
cells with different labels should end up apart.

## Exercises

- Explore the `sce` object directly — its class, its dimensions, the count matrix, and the cell
  metadata. Compared with a bulk RNA-seq count matrix, what is structurally different about this
  dataset?
- Build a PCA plot and an MDS plot of the cells, using the same tools used earlier in the course
  for bulk RNA-seq. Colour the points by the `cluster` label found in `colData(sce)`.
- Try visualising the structure of the dataset with any other tool you want.
- Having tried the above: do your plots recapitulate the known structure — do the cell-type
  clusters separate out? Where do you run into trouble, and why do you think that happens?

## Sources

- `docs/omics-statistics/statomics/sga21/singleCell_intro1.md` — converted from
  `singleCell_intro1.Rmd` (statOmics SGA21 course, CC BY-NC-SA 4.0). This is the only material
  supplied for this chapter: no slides, transcript, or separate problem set were given, and the
  chapter's code and exercises reproduce the practical in full.

---

[← 35. Filtering, Aliasing, and limma-voom](35-filtering-aliasing-and-limma-voom.md) · [Contents](index.md) · [38. Single-Cell QC and Dimensionality Reduction →](38-single-cell-qc-and-dimensionality-reduction.md)
