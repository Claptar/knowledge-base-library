---
title: "Luebbert 2024 — Complexity of Transcriptomic Data Analysis and Implications for Biological Discovery"
paper: "summary"
source: "https://doi.org/10.7907/xnw5-v914"
licence: "all rights reserved — not reproduced"
written: "2026-10-02"
---

> **Summary of a thesis.** Luebbert, L. (2024). Complexity of Transcriptomic Data Analysis and Implications for Biological Discovery. PhD thesis, California Institute of Technology, Pasadena, California. https://doi.org/10.7907/xnw5-v914 ([original](https://doi.org/10.7907/xnw5-v914)). Rights: all rights reserved — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Complexity of Transcriptomic Data Analysis and Implications for Biological Discovery

## What this covers

A computational biology PhD thesis arguing that methods for analyzing transcriptomic data have not
kept pace with the data itself, developed across five case studies: software adoption, two
bioinformatics tools, detecting viral RNA without a matching reference genome, transcriptomics in a
species with a poor reference genome, and a CAR T-cell clinical trial dataset.

## The question

Sequencing technologies generate data at a scale and complexity that computational methods for
interpreting it have not matched, and the author — a wet-lab geneticist who moved into computational
biology during her PhD — asks why so many published analysis tools go unused, and what
computational obstacles keep real information locked inside transcriptomic data already being
collected. Each chapter takes one version of that question: finding a virus with no matching viral
genome; analyzing a species with a poorly annotated reference genome; and interpreting single-cell
data collected across many patients and sequencing batches in a clinical trial.

## The approach

The thesis mixes software engineering with analysis of real datasets. It surveys the scRNA-tools
database to quantify what separates widely-used software from ignored tools, then builds two tools
following the resulting guidelines: `gget`, for querying genomic databases in one line of code, and
`gget elm`, for locally matching short linear interaction motifs. Its central methodological
contribution extends the aligner kallisto to perform "translated search": nucleotide reads and an
amino-acid reference are both translated into a shared comma-free code so reads can be pseudoaligned
against a protein reference while retaining each read's cell barcode. Applied to PalmDB, a database
of the viral RNA-dependent RNA polymerase (RdRP) domain conserved across RNA viruses, this detects
viral RNA at single-cell resolution without a matching viral genome. The same idea is applied to a
species with sparse annotation (zebra finch), then to a heterogeneous clinical dataset — 32
multiplexed datasets from 12 prostate cancer patients treated with CAR T cells — where the problem
shifts from detection to combining data collected under inconsistent conditions.

## What it found

**Chapter I** quantifies why most published scRNA-seq tools go unused: only about 3% released
between 2016 and 2022 reached over 1,000 citations, nearly half received fewer than 20, and
highly-cited tools were far more likely to install in one line and still be updated six months after
release (91.4% vs. 47.4%), yielding a checklist for user-friendly omics software.

**Chapter II** describes `gget` (nine modules spanning Ensembl, NCBI, UniProt, BLAST/BLAT, Enrichr,
ARCHS4; 97,000 downloads by writing) and `gget elm`, which matches proteins against the Eukaryotic
Linear Motif database locally rather than through ELM's rate-limited web API — returning identical
results 3.5-8x faster, and correctly flagging the loss of a PALB2-binding motif in a known
carcinogenic BRCA2 mutation.

**Chapter III** validates kallisto translated search against PalmDB on data with known SARS-CoV-2 or
Zaire ebolavirus infection, finding viral counts tracking RT-qPCR/RNA-ISH measurements and 96.76%
correct species-level assignment in a self-consistency test; it tolerated simulated mutation better
than existing translated-search and standard nucleotide alignment methods. Applied to rhesus macaque
PBMC data, it recovered virus-like sequences beyond the known Ebola infection, some confined to
specific cell types (one, provisionally an *Alphacoronavirus*, concentrated in neutrophils) and
predictable from host gene expression at over 70% accuracy — read as a real viral signal, unlike
other candidates that also appeared in blank control libraries.

**Chapter IV** documents concrete obstacles in a non-model organism: genome assembly quality varies
enormously across species, versions are inconsistently labeled between databases, and about 24% of
zebra finch gene IDs carried no annotation, motivating several `gget` modules. A collaborative
single-cell study then found that chronically silencing inhibitory neurons elevated microglia and
MHC class I expression, implicating these pathways in the brain's later recovery of a learned
behavior despite the perturbation persisting.

**Chapter V** reports a phase 1 trial (NCT03873805) of PSCA-targeted CAR T cells in 14 men with
metastatic castration-resistant prostate cancer. Cystitis was the dose-limiting toxicity; reducing
lymphodepletion lowered high-grade cystitis while roughly preserving CAR T expansion. Four of 14
patients had PSA declines over 30%, including one sustained decline over 90% with radiographic
tumor regression; persistence was generally short-lived, linked to the lack of durable remissions.
Re-analyzing the trial's 32 single-cell datasets showed a batch-correction tool spuriously spread the
CAR transgene's expression into cell types that could never have expressed it, whereas clustering
without batch correction separated cleanly by timepoint and cell type.

**Chapter VI** closes by arguing that methods for modeling noise and basic steps like visualization
are still catching up to the pace of data generation, and that results such as how a minor
host-genome masking choice changed which viruses were detected in Chapter III show why rigorous
omics analysis increasingly requires collaboration between biologists and computer scientists.

## Limits and context

Several viral sequences in Chapter III cannot be distinguished from reagent or environmental
contamination without further wet-lab confirmation; specific candidates are flagged as likely
contaminants because they also appeared in blank libraries. Detection is restricted to the conserved
RdRP domain, missing viruses without recognizable RdRP homology, and RdRP reads made up only about
1% of total viral RNA analyzed, leaving the virus count matrix sparse and prone to false negatives.
A k-mer-length ceiling in kallisto's current implementation is expected to lift in future versions.
The CAR T trial is a small, single-center phase 1 study with modest, non-durable responses
attributed to limited CAR T persistence, motivating future trials with multiple smaller doses rather
than single-dose escalation. The thesis argues against routine, unexamined batch correction on
heterogeneous clinical data, having shown a case where it destroyed a known biological signal rather
than removing a technical artifact.

## Citation

Luebbert, L. (2024). *Complexity of Transcriptomic Data Analysis and Implications for Biological
Discovery*. PhD thesis, California Institute of Technology, Pasadena, California. Defended March 14,
2024. https://doi.org/10.7907/xnw5-v914
