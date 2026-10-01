---
title: "Cargnelli et al. 2026 — Benchmarking computational decontamination of ambient RNA"
paper: "summary"
source: "https://doi.org/10.64898/2026.01.13.699237"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Cargnelli, C. B., Nielsen, J. V. & Madsen, J. G. S. (2026). Benchmarking computational decontamination of ambient RNA. bioRxiv preprint, posted April 1, 2026. https://doi.org/10.64898/2026.01.13.699237 ([original](https://doi.org/10.64898/2026.01.13.699237)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Benchmarking computational decontamination of ambient RNA

**[Read the full text](full-text/index.md)**

## What this covers

An independent benchmark of computational methods for removing "ambient RNA" contamination from
single-cell and single-nucleus RNA-sequencing data, speaking to the practice of sxRNA-seq
preprocessing in genomics.

## The question

Single-cell and single-nucleus RNA-seq data are contaminated by ambient RNA: molecules released
into solution, chiefly by cell lysis during harsh sample preparation, that get captured in droplets
alongside a cell's own transcripts and are misattributed to it. This distorts expression
measurements, confounds cell-type classification, and biases downstream conclusions. Several
computational decontamination tools exist, but no independent study had evaluated them side by side
on comparable data — leaving developers without a shared standard and users without a basis for
choosing a tool, or for judging whether one is warranted at all. The paper also asks a second
question: since decontamination tools are now run routinely inside standard pipelines (e.g.
nf-core), does applying "correction" to data that is not actually contaminated introduce its own
distortion?

## The approach

The authors benchmarked seven methods — CellBender, DecontX, FastCAR, scAR, scCDC, SoupX, and
CellClear — run with default parameters, across four dataset categories chosen to supply different
kinds of ground truth: three **species-mixing** experiments of increasing complexity (from a simple
human-mouse mixture to human islets xenografted into mouse kidney), where reads aligning to the
"wrong" species establish genuine contamination; a **strain-mixing** experiment using
genotype-specific SNPs between mouse strains; **synthetic datasets** built by sampling from
negative-binomial models fitted to real cell lines with a specified ambient fraction mixed in; and
**negative-control datasets** with no contamination (including a non-droplet Smart-seq2 dataset),
used to test for over-correction.

Each method-dataset pair was scored on an "ambient removal score" and an "endogenous retain score"
(0–1 scale). The authors then traced the downstream consequences of decontamination through
standard analysis tasks — unsupervised clustering, marker-gene scoring, batch integration
(Harmony), and reference-based label transfer (Azimuth) — to see whether cleaning the data actually
improved biological interpretation, not just the raw counts.

## What it found

Ambient RNA is pervasive: across 97,357 real cells and nuclei from 49 samples, 81.56% showed
detectable contamination, higher on average in single-nucleus (11.80%) than single-cell (7.79%)
preparations. Contamination is dominated by a small number of ubiquitous, highly expressed mRNAs —
the 10% most frequently expressed genes accounted for 82.30% of ambient signal on average — and its
per-cell level was only weakly predicted by standard quality metrics, so stringent filtering reduces
but cannot eliminate it.

No single method won across every dataset and metric. scAR and CellBender gave the strongest raw
ambient-removal scores, but scAR also stripped out a large share (44.5% on average) of genuine
endogenous signal, especially from lowly expressed genes, and could degrade batch integration and
label transfer even on uncontaminated data — a strong tendency to over-correct. scCDC and FastCAR
removed ambient RNA mainly from already highly expressed genes, limiting collateral damage but also
yielding little improvement in interpretation. CellClear showed the opposite skew, removing signal
mainly from lowly expressed genes, and stripped out nearly as much endogenous as ambient RNA.
DecontX and SoupX sat in the middle, preserving endogenous RNA well and consistently improving
downstream interpretation with comparatively low over-correction risk.

The authors recommend CellBender or DecontX (full mode, unfiltered matrix) when contamination is
expected and the full matrix is available, and SoupX in reduced mode when only a filtered matrix can
be obtained or there is no strong prior expectation of contamination, since it was least prone to
over-correcting clean data. CellBender had the best overall weighted performance but the heaviest
compute footprint (GPU, more memory). A general finding: applying any of these tools is not a safe
default — several methods altered expression and biological scores even with no contamination
present, so decontamination should be guided by prior evidence of ambient RNA, not applied
automatically.

## Limits and context

The authors note that each ground-truth strategy has a distinct limitation. Synthetic data, built
from fitted per-gene distributions, lacks higher-order structure such as gene-gene covariance
present in real data. Species-mixing gives a robust ground truth but places endogenous and ambient
RNA in non-overlapping feature spaces (different species' genes), unlike real contamination where
both compete for the same genes. Strain-mixing via SNPs is accurate but only measures contamination
at genetically variable genes, a limited subset. The paper argues that further progress is
constrained less by algorithms than by the lack of experimental designs where ambient and
endogenous RNA share the same feature space while contamination can still be measured without bias
— a gap not yet closed. Results and code are released as an open, extensible resource meant to be
rerun as new methods and datasets appear, rather than as a final verdict.

## Citation

Cargnelli, C. B., Nielsen, J. V. & Madsen, J. G. S. (2026). Benchmarking computational
decontamination of ambient RNA. *bioRxiv* preprint, posted April 1, 2026.
https://doi.org/10.64898/2026.01.13.699237 (preprint, CC BY 4.0 licence).
