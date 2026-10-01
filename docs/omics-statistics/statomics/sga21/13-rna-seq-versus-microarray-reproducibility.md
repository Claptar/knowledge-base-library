---
title: "13. RNA-seq versus Microarray Reproducibility"
course: "StatOmics Sga21"
chapter: 13
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. RNA-seq versus Microarray Reproducibility

## What this covers

This chapter works from a single figure and a fragment of surrounding text — Figure 1 and part of
the abstract of Marioni et al.'s study comparing RNA sequencing to microarrays, kept in the course
materials as a standalone image. It answers one question: how do you build an experiment so that a
claim like "sequencing finds more differentially expressed genes than microarrays" is a fair
comparison rather than an artefact of the samples being different, and what did that comparison
find? It assumes only that the reader knows what a microarray and RNA sequencing are as
expression-profiling technologies, and what a technical replicate is.

## Why the comparison needed a paper

By the time high-throughput sequencing became cheap enough to use for expression profiling,
microarrays were the established, well-characterised technology. Before switching, two things need
checking: is the new measurement reproducible across repeated runs of the same sample, and does it
actually do better at the task it would replace the array for — finding genes whose expression
differs between conditions? Marioni et al. built one experiment to answer both questions together,
by using the same extracted RNA to feed both platforms, so that any difference in the outcome could
not be blamed on the two platforms having measured different biological material.

## The experimental design

<figure>
<svg viewBox="0 0 640 320" role="img" aria-label="Workflow splitting liver and kidney RNA samples between a microarray arm and a sequencing arm, converging on a comparison of differentially expressed genes">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <rect x="70" y="8" width="140" height="34" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="140" y="29" text-anchor="middle" font-size="12" fill="currentColor">Liver, total RNA</text>

  <rect x="430" y="8" width="140" height="34" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="500" y="29" text-anchor="middle" font-size="12" fill="currentColor">Kidney, total RNA</text>

  <rect x="60" y="83" width="160" height="34" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="140" y="104" text-anchor="middle" font-size="12" fill="currentColor">mRNA purification</text>

  <rect x="420" y="83" width="160" height="34" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="500" y="104" text-anchor="middle" font-size="12" fill="currentColor">mRNA purification</text>

  <line x1="140" y1="42" x2="140" y2="83" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="500" y1="42" x2="500" y2="83" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="140" y1="42" x2="497" y2="83" stroke="currentColor" stroke-width="1" marker-end="url(#arrow)" opacity="0.6"/>
  <line x1="500" y1="42" x2="143" y2="83" stroke="currentColor" stroke-width="1" marker-end="url(#arrow)" opacity="0.6"/>

  <rect x="30" y="163" width="220" height="40" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="140" y="180" text-anchor="middle" font-size="12" fill="currentColor">Affymetrix array,</text>
  <text x="140" y="196" text-anchor="middle" font-size="12" fill="currentColor">3 technical replicates</text>

  <rect x="380" y="163" width="230" height="40" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="495" y="180" text-anchor="middle" font-size="12" fill="currentColor">Illumina sequencing,</text>
  <text x="495" y="196" text-anchor="middle" font-size="12" fill="currentColor">7 lanes across 2 runs</text>

  <line x1="140" y1="117" x2="140" y2="163" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="500" y1="117" x2="495" y2="163" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>

  <rect x="170" y="255" width="300" height="40" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="320" y="272" text-anchor="middle" font-size="12" fill="currentColor">Compare differentially expressed</text>
  <text x="320" y="288" text-anchor="middle" font-size="12" fill="currentColor">genes between technologies</text>

  <line x1="140" y1="203" x2="260" y2="255" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="495" y1="203" x2="390" y2="255" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
</svg>
<figcaption>Figure 1A of Marioni et al.: the same liver and kidney RNA is purified and then split
between the array and sequencing platforms, so that both technologies measure the same biological
starting material before their results are compared.</figcaption>
</figure>

Two tissue samples — liver and kidney — were each carried through total RNA extraction and mRNA
purification, and then each split between two arms:

- an **array arm**: each mRNA sample hybridized to Affymetrix microarrays, in three technical
  replicates;
- a **sequencing arm**: each mRNA sample sequenced on the Illumina platform across seven lanes,
  spread over two sequencing runs.

Both arms feed the same downstream step: finding differentially expressed genes, and comparing the
two technologies' results directly, on the same underlying RNA.

The layout of the sequencing runs (Figure 1B) does not put all of one tissue's lanes together.
Each run's eight lanes alternate kidney and liver samples, with the fifth lane of each run shown in
a third colour, and most of Run 2's lanes — marked with an asterisk — were sequenced at a lower
loading concentration (1.5 pM) than the rest. Spreading each tissue across lanes and across both
runs keeps a difference between the tissues from being confounded with a difference between lanes
or between runs.

## What the comparison found

Three findings, reported from the same dataset:

- **Reproducibility.** The sequencing data were highly reproducible, with few systematic
  differences among the technical replicates.
- **A Poisson model fits the technical noise.** For a gene measured by counting reads, the natural
  model for pure counting noise is the Poisson distribution, in which the variance of a count
  equals its mean. The variation seen across technical replicates was well captured by exactly this
  model: only about 0.5% of genes showed counts more variable across replicates than a Poisson
  model would predict. That gives a statistical basis for treating a departure from Poisson
  variation as a signal of real, biological differential expression, rather than of measurement
  noise.
- **More power to detect differential expression.** Using a Poisson-based test built on that
  model, the sequence data identified 30% more differentially expressed genes than a standard
  analysis of the array data did, at the same false discovery rate. The source also notes the
  sequencing data's potential to detect alternative splicing — something a fixed microarray probe
  design cannot do, since a microarray can only measure what its probes were manufactured to look
  for.

## Sources

- Text and figure: `docs/omics-statistics/statomics/sga21/images_sequencing/marioni_fig1.md` and
  its associated image `marioni_fig1/figures/p001-1.jpeg`, in the `knowledge-base-library`
  repository. This is a model-reconstructed conversion (`fidelity: reconstructed`) of
  `images_sequencing/marioni_fig1.pdf` from the statOmics/SGA21 course repository (commit
  `0ad787d4cc2bb2f4636440840a8a923cf6c09839`), licensed CC BY-NC-SA 4.0, converted 2026-09-18. The
  source PDF has no text layer; the extracted prose follows the note's paraphrase of what appears
  to be the abstract of Marioni, Mason, Mane, Stephens & Gilad, "RNA-seq: an assessment of
  technical reproducibility and comparison with gene expression arrays" — the paper the figure is
  drawn from. The description of the two-panel figure (study workflow and lane layout) is this
  writer's reading of the image itself; the original PDF carried no machine-readable caption.
- No slides, transcript, or exercises were supplied for this item — the note above is the entirety
  of the source material for this chapter. The full paper is referred to by the figure but was not
  itself part of the supplied material, and neither was whatever lecture originally showed this
  slide alongside it.

---

[← 12. Genomics: A Molecular Biology Primer](12-genomics-a-molecular-biology-primer.md) · [Contents](index.md) · [14. Detecting Lane Effects in RNA-seq →](14-detecting-lane-effects-in-rna-seq.md)
