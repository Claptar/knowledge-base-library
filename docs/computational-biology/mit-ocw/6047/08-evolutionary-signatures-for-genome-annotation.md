---
title: "8. Evolutionary Signatures for Genome Annotation"
course: "MIT 6047"
chapter: 8
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Evolutionary Signatures for Genome Annotation

## What this covers

This is the opening lecture of Module V, "Comparative genomics and evolution." It answers a single
question: why does comparing the genomes of related species tell you which stretches of DNA are
functional, and how much comparative data do you actually need before that signal is trustworthy?
It is a roadmap lecture — it lays out the underlying logic and previews the specific evolutionary
signatures (nucleotide conservation, protein-coding signatures, microRNA signatures) that later
lectures develop in detail. It assumes the reader is comfortable with a multiple sequence alignment
and with the idea of a phylogenetic tree and branch length, both used here without being re-derived.

## Two directions between evolution and genomics

The module frames comparative genomics as a two-way relationship between evolution and genomics.
Lecture 17 goes in one direction — using evolution to study genomes, i.e. turning patterns of
change across species into an annotation of what a genome's sequence does. Lectures 18 and 19 go
the other way — using genomics to study evolution, building the phylogenetic and phylogenomic
machinery (distance-based and model-based phylogenetics, gene trees versus species trees,
reconciliation, coalescence) that this lecture's genome-annotation arguments quietly rely on.

## The logic: selection filters mutations differently in functional and non-functional DNA

The whole method rests on one fact about evolution: random mutation supplies changes everywhere in
a genome, but natural selection does not treat all of them alike.

- In a **non-functional region**, most mutations have no effect on fitness. They accumulate and are
  kept in the lineage, so over time the sequence simply drifts.
- In a **functional region**, a mutation more often reduces fitness. An organism carrying it is, on
  average, less fit, and over evolutionary time less-fit organisms — and the mutant copies of the
  gene they carry — thin out of the population. This is purifying selection.

A functional element is not exempt from mutation; it accumulates mutations at the same underlying
rate as anything else, but a larger share of those mutations get rejected by selection before they
become permanent differences between species. What is left, when the region is compared across
species, is a residue of change smaller than the neutral expectation. That gap between how much a
region actually diverged and how much it would have diverged with no selection at all is the
conservation signal genome annotation is built on.

## A worked example: reading factor footprints out of a yeast promoter

The lecture's example is the region upstream of the yeast GAL10/GAL4/GAL1 genes, aligned across
four related yeasts (*S. cerevisiae*, *S. paradoxus*, *S. mikatae*, *S. bayanus*). Most of the
intergenic sequence is only loosely conserved — plenty of substitutions and a scattering of gaps
between the four species — but the slides mark specific short blocks where the match line runs
almost solid, and those blocks line up with known transcription-factor binding sites: three tandem
GAL4 sites in the block below, and separate TBP and MIG1 sites elsewhere in the same region.

```
                           GAL4                    GAL4                    GAL4
Scer  CTTAACTGCTCATTGC-----TATATTGAAGTACGGATTAGAAGCCGCCGAGCGGGCGACAGCCCTCCGACGGAAGACTCTCCTCCGTGCGTCCTCGTCT
Spar  CTAAACTGCTCATTGC-----AATATTGAAGTACGGATCAGAAGCCGCCGAGCGGACGACAGCCCTCCGACGGAATATTCCCCTCCGTGCGTCGCCGTCT
Smik  TTTAGCTGTTCAAG--------ATATTGAAATACGGATGAGAAGCCGCCGAACGGACGACAATTCCCCGACGGAACATTCTCCTCCGCGCGGCGTCCTCT
Sbay  TCTTATTGTCCATTACTTCGCAATGTTGAAATACGGATCAGAAGCTGCCGACCGGATGACAGTACTCCGGCGGAAAACTGTCCTCCGTGCGAAGTCGTCT
       **  ** **   ***** ******* ****** ***** ***  **** * *** ***** * * ****** *** * ***
```

The slides call blocks like this one **factor footprints**, and the run of near-total matches
around them a **conservation island**. Nothing marks a footprint as special except that it changes
far more slowly than the sequence around it — exactly the signature purifying selection predicts
for a real binding site. This way of reading alignments across yeast, mammal and fly genomes to
expose functional elements is credited to Kellis et al. (*Nature*, 2003) for yeast, Xie (*Nature*,
2005) for mammals, and Stark et al. (*Nature*, 2007) for fly.

## Why many closely related genomes beat a few distant ones

Turning "less change than expected" into a usable statistic needs enough evolutionary distance to
work with, but the right amount matters:

- **Too close**: the species have barely diverged, so neither functional nor non-functional regions
  show any mutations yet — there is nothing to compare.
- **Sufficient distance**: non-functional regions have accumulated enough substitutions to look
  random, while functional regions still show the constraint signal — this is the regime where the
  two are distinguishable.
- **Too far**: even functional regions have taken so many hits, including repeated substitutions at
  the same site, that the original conservation signal saturates and disappears too.

Given a fixed budget of total branch length — a fixed amount of evolutionary time to spend across
all the species compared — the lecture's claim is that many closely related species are worth more
than a few distantly related ones for the same total budget. The reason is independence, not
distance: a functional region stays recognizable along each branch, close or far, as long as no
single branch falls in the "too far" regime. But a non-functional region only looks conserved
across species by chance, and that chance coincidence has to survive every independent branch of
the comparison at once. Spreading a fixed total branch length over many short, independent branches
multiplies the number of independent chances for a spurious pattern to be exposed — something a few
long branches cannot do, even though the total amount of accumulated mutation is the same either
way.

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Two trees with the same total branch length: five short branches to five close relatives versus two long branches to two distant relatives">
  <line x1="40" y1="110" x2="170" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="110" x2="170" y2="60" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="110" x2="170" y2="100" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="110" x2="170" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="110" x2="170" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="40" cy="110" r="3" fill="currentColor"/>
  <circle cx="170" cy="20" r="3" fill="currentColor"/>
  <circle cx="170" cy="60" r="3" fill="currentColor"/>
  <circle cx="170" cy="100" r="3" fill="currentColor"/>
  <circle cx="170" cy="140" r="3" fill="currentColor"/>
  <circle cx="170" cy="180" r="3" fill="currentColor"/>
  <text x="105" y="205" text-anchor="middle" font-size="12" fill="currentColor">5 short, independent branches</text>
  <line x1="250" y1="110" x2="380" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <line x1="250" y1="110" x2="380" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="250" cy="110" r="3" fill="currentColor"/>
  <circle cx="380" cy="30" r="3" fill="currentColor"/>
  <circle cx="380" cy="190" r="3" fill="currentColor"/>
  <text x="315" y="205" text-anchor="middle" font-size="12" fill="currentColor">2 long branches</text>
  <text x="210" y="14" text-anchor="middle" font-size="12" fill="currentColor">same total branch length</text>
</svg>
<figcaption>Same total branch length spent two ways. A functional region stays recognizable along
every branch in both trees. A non-functional region only looks conserved by chance, and the more
independent branches that chance has to survive at once, the less likely it is — so five short
branches give more discovery power than two long ones for the same total amount of evolutionary
change.</figcaption>
</figure>

The lecture's own analogy: this is like recording a concert with several microphones rather than
one. Each microphone picks up the same music (the signal shared by every lineage: the functional
constraint) plus its own independent hiss (the neutral drift specific to that lineage). Average
across many microphones and the independent noise cancels while the shared signal remains; turning
up the gain on a single microphone only amplifies its own hiss along with the music, with nothing
independent to average it against.

## The genomes behind this argument

The comparisons in this lecture and the ones that follow are drawn from three panels: 29 mammals,
12 flies, and 17 fungi — the fungal panel splitting further into 9 yeasts (separated into
post-duplication and pre-duplication lineages) and 8 Candida species (diploid and haploid).
Genome-wide alignments built from these panels span entire genomes rather than single loci — the
slides illustrate this with roughly 100 genes aligned across the Drosophila phylogeny — which is
what lets the same comparative-identification argument be applied systematically across a whole
genome rather than gene by gene. The finding cited for comparisons at this scale is that
protein-coding exons are deeply conserved all the way out to mouse, chicken and fish, and that many
other elements are conserved just as strongly, without yet being labelled exon or regulatory.

## The evolutionary-signatures roadmap

Having established that conservation is visible, and that many genomes give more power to detect
it, the module's plan for turning that into systematic genome annotation runs as follows.

- **Nucleotide conservation as evolutionary constraint.** Formalize purifying selection and
  "neutral branch length" into a measure of discovery power; detect constrained elements at the
  level of single nucleotides, sliding windows, and hidden Markov model states; and estimate what
  fraction of a genome is constrained at all, by separating a real conservation signal from
  background.
- **Evolutionary signatures beyond simple conservation.** Different kinds of functional element do
  not just change more slowly than average — they change in characteristic *patterns*. The rest of
  the module is organized around reading off which pattern is present, not only how much change
  there is.
- **Signatures of protein-coding genes.** Reading-frame conservation and codon-substitution
  frequency, formalized in a likelihood-ratio framework that estimates separate substitution-rate
  parameters for a coding model ($Q_C$) and a neutral, non-coding model ($Q_N$), and scores a
  region by comparing the two. This is later used to revise gene annotations — catching genes that
  read through a stop codon, or regions of excess constraint that a gene model missed.
- **Signatures of microRNA genes.** Structural and evolutionary features specific to microRNA
  hairpins, combined with decision trees and random forests; using consistency between sense and
  antisense strands, and cooperation between a microRNA's mature and star arms, as further
  evidence.
- **Measuring selection within the human lineage**, listed as a further topic but not developed on
  these slides.

## Estimating the level of constraint

The closing slide sets out, in order, the technical steps needed to turn an alignment into a
constraint estimate: count the edit operations between aligned sequences (substitutions and gaps);
estimate the actual number of mutations from that count, including a correction for back-mutations
that a raw edit count cannot see; use information from neighboring columns via conservation
"windows" rather than judging one column at a time; estimate the probability that a position sits
in a constrained hidden state using a hidden Markov model (the following week's topic); use the
phylogenetic tree itself to estimate the neutral mutation rate, so observed substitutions can be
compared against it to count "rejected substitutions" — the ones selection prevented; and finally
allow different parts of the tree to carry different rates, which is where the phylogenetics of the
next lectures comes in.

## Sources

- Slide deck: `computational-biology/mit-ocw/6047`, lecture 17 slides, "Key goal: Evolution
  preserves functional elements" — all sections above are drawn from this deck. It is a model
  reconstruction of a PDF with no text layer; the deck itself flags that "every equation is
  unverified," so $Q_C$ and $Q_N$ are reproduced exactly as named on the slide, with no derivation
  available to check them against.
- No transcript, notes, or exercise set was supplied for this lecture; nothing here is drawn from
  spoken commentary, and no `## Exercises` section is included for that reason.
- The deck's citations for "reading evolution to reveal functional elements": Kellis et al.,
  *Nature* 2003 (yeast); Xie, *Nature* 2005 (mammals); Stark et al., *Nature* 2007 (fly, given as
  "Nature 07" on the slide).
- The deck's own footer points forward to "Detecting rates and patterns of selection ($\omega/\pi$)"
  and to lectures 18-19 on phylogenetics and phylogenomics — neither is contained in this file.
- The converted deck lists roughly ninety additional page images (`figures/p006-1.jpeg` through
  `figures/p071-1.jpeg`) that the conversion could not place in the text or describe; they are not
  reproduced here because their content is not recoverable from this source.

---

[← 7. Challenges in Regulatory Genomics](07-challenges-in-regulatory-genomics.md) · [Contents](index.md) · [9. Molecular Evolution and Phylogenetics →](09-molecular-evolution-and-phylogenetics.md)
