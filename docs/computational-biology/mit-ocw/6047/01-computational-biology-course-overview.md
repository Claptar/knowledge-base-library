---
title: "1. Computational Biology: Course Overview"
course: "MIT 6047"
chapter: 1
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Computational Biology: Course Overview

## What this covers

This is the opening lecture of MIT's Computational Biology course (6.047 / 6.878 / HST.507, Fall
2015, taught by Manolis Kellis). It does not introduce a method — it lays out what the field is,
how the term ahead is organized, and why the course is built the way it is. It assumes nothing
beyond ordinary scientific literacy; the algorithms this map points to (alignment, hidden Markov
models, motif discovery, network inference, phylogenetics, GWAS, and so on) are the subject of the
chapters that follow. Read this one as an orientation to the rest of the book, not as content to
be learned for its own sake.

## What computational biology is

The course places every lecture along two independent axes.

<figure>
<svg viewBox="0 0 340 300" role="img" aria-label="The two axes that place every lecture in the course: biology versus computation, and foundations versus frontiers">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="170" y1="150" x2="170" y2="35" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="170" y1="150" x2="170" y2="265" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="170" y1="150" x2="35" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="170" y1="150" x2="305" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <circle cx="170" cy="150" r="2.5" fill="currentColor"/>
  <text x="170" y="22" text-anchor="middle" font-size="13" fill="currentColor">Frontiers</text>
  <text x="170" y="285" text-anchor="middle" font-size="13" fill="currentColor">Foundations</text>
  <text x="22" y="145" text-anchor="end" font-size="13" fill="currentColor">Biology</text>
  <text x="318" y="145" text-anchor="start" font-size="13" fill="currentColor">Computation</text>
</svg>
<figcaption>Duality #1 (horizontal): a lecture leans toward a real, current biological problem, or
toward a general computational/statistical technique. Duality #2 (vertical): it leans toward a
well-posed, classical problem with settled general methodology ("the classics"), or toward an
open, complex current problem that combines several such methods and is where a final-project idea
usually comes from. Every module below works through both halves of the vertical axis in turn.</figcaption>
</figure>

## The six modules

The course is organized into six modules, each corresponding to an active area of research:

| Module | Subject |
|---|---|
| I | Comparative genomics: aligning and modelling genomes |
| II | Genes and transcripts: RNA-seq, clustering, structure |
| III | Regulation: epigenomics, transcription factors, motifs, network inference |
| IV | Variation: population genetics, human history, heritability, eQTLs |
| V | Evolution: phylogeny, evolutionary signatures, whole-genome duplication, assembly |
| VI | Frontiers: personal and disease genomics, 3D genomes, pharmacogenomics, synthetic biology |

Within every module, the **foundations** half draws on one common toolbox, used again and again
across the course: dynamic programming, string matching, hashing, hidden Markov models,
expectation-maximization, Gibbs sampling, clustering, classification, feature selection, support
vector machines, conditional random fields, context-free grammars, phylogenetics, gene/species
trees, evolutionary models, and disease mapping (GWAS). The **frontiers** half of each module then
turns to open problems built on that toolbox: evolutionary signatures, transcript analysis, long
non-coding RNAs, network inference and analysis, epigenomics, recent human selection and ancestry,
chromatin regulation, missing heritability, and three-dimensional genome structure.

Stripped of dates and problem-set logistics, the lecture-by-lecture roadmap for the rest of this
book is:

**Module I — Comparative genomics**
Alignment I: dynamic programming, global and local alignment · Alignment II: database search,
rapid string matching, BLAST, BLOSUM · Hidden Markov Models I: evaluation/parsing, Viterbi, forward
algorithm · Hidden Markov Models II: posterior decoding, learning, Baum–Welch.

**Module II — Genes and transcripts**
Transcript structure: GenScan, RNA-seq, mapping, de novo assembly, differential expression ·
Expression analysis: clustering/classification, k-means, hierarchical and Bayesian methods ·
Networks I: Bayesian inference, deep learning, network dynamics · Networks II: network learning,
structure, spectral methods.

**Module III — Regulation and epigenomics**
Regulatory motifs: discovery, representation, protein-binding microarrays, Gibbs sampling, EM ·
Epigenomics: ChIP-seq, read mapping, peak calling, IDR, chromatin states · RNA modifications: RNA
editing, translation regulation, splicing regulation.

**Module IV — Variation**
Resolving human ancestry and history from genetic data · Disease association mapping, GWAS,
organismal phenotypes · Quantitative trait mapping, molecular traits, eQTLs · Missing heritability,
complex traits, interpreting GWAS, rank-based enrichment.

**Module V — Evolution**
Comparative genomics and evolutionary signatures · Phylogenetics: molecular evolution, tree
building, phylogenetic inference · Phylogenomics: gene/species trees, reconciliation, recombination
graphs.

**Module VI — Current research directions**
Personal genomics and disease epigenomics: systems approaches to disease · Three-dimensional
chromatin interactions: 3C, 5C, Hi-C, ChIA-PET · Genome engineering with CRISPR/Cas9 and related
technologies.

## Why computational biology

The lecture motivated the field with a list of reasons collected from past students, presented
without further elaboration:

- There is an enormous and growing amount of biological data — "lots of data times lots of data."
- Biological systems have rules: structure that computation can uncover and exploit.
- The data reward pattern-finding — correlations and higher-order relationships hidden in the
  numbers.
- Biology is, on this framing, fundamentally a data problem.
- Computation gives the ability to visualize what could otherwise not be seen.
- It supports simulation and reasoning about temporal relationships — how a system moves, not just
  a snapshot of its state.
- It supports a guess-and-verify cycle: generate a hypothesis computationally, then test it.
- It lets you propose and evaluate a mechanism or theory to explain what is observed.
- Biological systems are networks — combinations of variables acting together, not variables in
  isolation.
- Computation improves efficiency by narrowing the experimental space that actually has to be
  tested at the bench.
- It provides the informatics infrastructure needed to combine datasets collected separately.
- Life itself is digital, in the sense that a genome is a sequence of discrete symbols — so
  understanding a cell means understanding its instruction set.

## Sequence as data

The lecture made the "life is digital" point concrete by putting a real stretch of genomic
sequence on the slide — several dozen lines of nothing but the letters A, C, G and T:

```
TATTGAATTTTCAAAAATTCTTACTTTTTTTTTGGATGGACGCAAAGAAGTTTAATAATCATATTACATGGCATTACCACCATAT
ATCCATATCTAATCTTACTTATATGTTGTGGAAATGTAAAGAGCCCCATTATCTTAGCCTAAAAAAACCTTCTCTTTGGAACTTT
AATACGCTTAACTGCTCATTGCTATATTGAAGTACGGATTAGAAGCCGCCGAGCGGGCGACAGCCCTCCGACGGAAGACTCTCCT
...
```

followed immediately by a slide titled "From DNA to RNA: Transcription" (its image is not preserved
in the source material). The juxtaposition states the problem the rest of the course answers: an
organism's entire program is a string over a four-letter alphabet, and essentially everything in
the six modules above — alignment, motif-finding, gene structure, regulation, evolution — is a way
of pulling structure and meaning out of a string like this one.

## Exercises

These are drawn from Problem Set 1, "Aligning and Modeling Genomes," released alongside this
lecture. They draw on alignment and hidden-Markov-model material that Module I's lectures (covered
in the chapters that follow) introduce — nothing here needs anything beyond ordinary programming
and the definitions given in each problem.

**1. Evolutionary distances of orthologs and paralogs.** Implement Needleman–Wunsch global
alignment and use it to date a gene duplication.

(a) Complete a Needleman–Wunsch implementation (a skeleton and a traceback routine are supplied,
with a fixed substitution matrix and gap penalty). Give: the scoring/traceback code you wrote, the
optimal alignment of `CTAAGTACT` and `CATTA` together with the completed score matrix $F$ and the
optimal path through it, and the alignment score of the human and mouse *HoxA13* genes.

(b) The Hox genes control body-plan formation during development; the fruit fly has a single Hox
cluster, while most vertebrates have four, thought (on a hypothesis that remains controversial) to
have arisen from two rounds of whole-genome duplication. Modify your program so its score is a true
distance metric: zero for a sequence aligned to itself, never negative, and larger for more
dissimilar sequences. Describe the change; no code is required.

(c) Use the distance version of your program to compute the distance between the human and mouse
*HoxA13* genes.

(d) Human and mouse *HoxD13* arose from the same ancestral gene as *HoxA13*, by a whole-genome
duplication that predates the human–mouse split. Given a fossil-record estimate of about 70 million
years for the human–mouse divergence, and using your *HoxA13* distance from (c) together with the
human/mouse *HoxD13* distance, estimate the date of the whole-genome duplication that produced
*HoxA13* and *HoxD13*. State the assumptions the estimate rests on.

**2. Sequence hashing and dotplot visualization.** Full Needleman–Wunsch alignment is quadratic, so
genome-scale regions are instead aligned using hashing heuristics, visualized as a dotplot: a point
at $(x, y)$ marks a matching $k$-mer starting at position $x$ in one sequence and position $y$ in
the other. Work with a supplied 1 Mb region around the HoxA cluster in human and mouse.

(a) Run the supplied script unmodified; it finds all matching 30-mers. How many matches are there,
what fraction lie near the diagonal, and what structure appears in the off-diagonal matches? What
kind of genomic element could produce that structure? Why should a near-diagonal match be more
likely than an off-diagonal one to represent a true orthologous alignment?

(b) Modify the script to instead find: (i) exact matching 100-mers; (ii) 60-mers matching every
other base; (iii) 90-mers matching every third base; (iv) 120-mers matching every fourth base;
(v) 100-mers allowing up to two mismatches per contiguous 6-base block (describe how you would
implement this last case; no plot is required). For each, report how the plot and the hit counts
change, and how you implemented the change.

(c) Parts (a) and (b.ii–iv) all require the same number of matching bases
($30 = 60/2 = 90/3 = 120/4$), yet they differ in how specific they are to the diagonal. Explain why.

(d) Describe the trade-off between the number of near-diagonal hits (sensitivity) and the fraction
of all hits that are near-diagonal (specificity), and how the hashing parameters control it.

(e) Extend the script to detect an inversion — a stretch of DNA excised and reinserted in reverse
orientation, e.g. $CGT[GATT]AGA \to CGT[AATC]AGA$. Use it to locate an artificial inversion planted
in a modified copy of the human sequence.

**3. HMMs for GC-rich regions: state durations and limitations.** Model a genome with a two-state
HMM distinguishing high-GC regions (about 60% G/C) from low-GC regions (about 60% A/T) — regions
known to differ in melting temperature, replication timing and gene density, and hypothesized
(controversially) to differ in evolutionary origin ("isochores").

(a) In an HMM whose self-transition probabilities $a_{kk}$ dominate, the *state duration* $D_k$ is
the number of consecutive steps spent in state $k$ before leaving it. Derive the expected state
duration as a function of $a_{kk}$, and the full distribution $P(D_k = d)$.

(b) Complete a Viterbi decoder for the two-state model. What state duration does the hard-coded
model expect for each state? Confirm the decoder reaches about 83% accuracy on a sequence
(`hmmgen`) generated from that same model.

(c) Apply the decoder to three "mystery" sequences. How do their true state-duration distributions
differ from each other and from the model's assumed distribution, what accuracy does the decoder
reach on each, and how does the Viterbi-predicted duration distribution compare with the true one?
(Extra credit: try to improve the decoder by hand-tuning its parameters, and explain any gain.)

(d) Would re-estimating the HMM's parameters from the correct annotations (in the style of
Baum–Welch) improve accuracy on the mystery sequences? Justify the answer either way.

(e) Real genomic elements rarely follow the geometric duration distribution derived in (a). Read
Burge & Karlin's GENSCAN paper (*J Mol Biol* 268(1):78–94, 1997) and explain how GENSCAN works
around this: algorithmically, how can an HMM-like model be made to use a state-duration
distribution other than the geometric one?

## Sources

- Slides: `01-6-047-u---6-878-g-tqe---hst-507-fall-2015.md` (title slide, course goals, the
  computation/biology and foundations/frontiers duality) and
  `02-course-organized-around-bio-comp-modules.md` (six-module structure, foundations/frontiers
  toolbox, full lecture schedule) and `05-why-computational-biology-last-year-s-answers.md`
  (motivation bullets, the genomic-sequence slide) — MIT OCW 6.047/6.878/HST.507, Fall 2015
  (Manolis Kellis), lecture 1 slide deck, reconstructed by a model from a PDF with no text layer;
  treat the wording as paraphrase rather than verbatim.
- Slides `03-sign-up-here-if-you-haven-t-already.md` and `04-final-project-at-a-glance.md` (scribe
  sign-up sheet, lecture feedback form, problem-set and quiz mechanics, final-project timeline and
  grading weights) are course administration and are not reproduced here.
- Exercises: `psets/01-questions.md`, Problem Set 1 ("Aligning and Modeling Genomes"), questions
  1–3. Question 4, a reflective writing prompt on the student's own background and interests for
  final-project team formation, is administrative rather than technical and is not reproduced.
- No transcript or written notes were supplied for this lecture, so nothing beyond what the slides
  state is included here. The image on the closing slide ("From DNA to RNA: Transcription") was
  removed from the source material for copyright and could not be reconstructed.
- The paper in Exercise 3(e) — Burge C, Karlin S., "Prediction of complete gene structures in human
  genomic DNA," *J Mol Biol* 268(1):78–94, 1997 — is named by the problem set itself; it was not
  supplied as course material.

---

[Contents](index.md) · [2. Sequence Alignment and Dynamic Programming →](02-sequence-alignment-and-dynamic-programming.md)
