---
title: "7. Challenges in Regulatory Genomics"
course: "MIT 6047"
chapter: 7
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Challenges in Regulatory Genomics

## What this covers

This chapter is built from a single slide deck — MIT's 6.047/6.878 Computational Biology, lecture
10, "Challenges in regulatory genomics" — with no transcript to go alongside it. Most of the deck's
own text extraction stopped after its outline slides, so the substance below was read directly off
the embedded slide images: protocol diagrams, a phylogeny-based conservation score, and validation
plots. It answers two questions the lecture poses back to back: what is the standing menu of
methods for identifying a regulator, its motif and its targets — and, once a comparative-genomics
search has proposed a candidate motif, how do you decide whether one particular occurrence of it in
a genome is a real functional site rather than a chance match? It assumes you already have position
weight matrices (PWMs), and the EM and Gibbs-sampling algorithms for finding a motif shared by a
set of co-regulated genes, from an earlier point in the course — those two algorithms are named
here as waypoints on the lecture's own roadmap, not re-derived.

## The pipeline: regulator, motif, targets

The lecture organises the whole subject of regulatory genomics around three objects:

- **Regulator** — the transcription factor (TF) or microRNA (miRNA) doing the regulating.
- **Motif** — the sequence specificity: what the regulator actually recognises.
- **Targets** — the functional instances of that motif genome-wide: the genes or transcripts
  actually regulated.

A fourth step, relating regulators to their targets as a **network**, is explicitly deferred —
"network analysis" is next lecture's topic, not this one. Three items on the lecture's own list of
methods are marked as *today's* material: **de novo comparative discovery** of a motif, **enrichment**
of a motif in co-regulated genes or already-bound regions, and **evolutionary signatures**. Everything
else below is either recap of methods established earlier in the course or a preview of the next
day's recitation.

## Finding regulators: homology, biochemistry, and comparative discovery

The oldest route to a candidate regulator is homology. A transcription factor is recognisable from
its sequence alone if it carries one of a small number of DNA-binding folds — the helix-turn-helix,
the zinc finger, the leucine zipper — each a different way of presenting an $\alpha$-helix or a loop
to sit in the DNA major groove and read off contacts to the bases and the backbone. One slide shows
this directly: a dimeric bHLH/zipper-type factor, with specific contact residues on its recognition
helix numbered, inserted into the DNA at the palindromic sequence it reads (a logo elsewhere in the
same slide gives that sequence as CACGTG). The point of showing the structure is that the fold, not
a binding assay, is what lets you recognise a new candidate TF from sequence homology alone. For
miRNAs the equivalent recognition-by-structure argument runs through evolutionary conservation
signatures in the hairpin, backed up by direct experimental cloning of the mature small RNA.

Biochemistry supplies a second, in vitro route: SELEX, DIP-chip, and protein-binding microarrays
(PBMs) for TFs; evolutionary/structural signatures plus cloning of the mature 5$'$ end for miRNAs.
One slide sketches a generic version of this kind of genome-scale in vitro assay: naked, sheared
genomic DNA is mixed with purified DNA-binding protein; the bound and unbound fractions are
separated, each independently amplified and fluorescently labelled, and both are hybridised to a
whole-genome tiling microarray. Comparing the two channels locates the bound loci, and computing
across all of them yields a consensus — the slide's own toy example comes out as the palindrome
CCGGTACCGG. Mass spectrometry can in principle read a TF-DNA complex directly, but the slide's own
verdict on it is one word: "difficult."

Last on the list, and the one flagged as today's actual subject, is *de novo* comparative discovery
— finding a motif, for either TFs or miRNAs, with no prior candidate at all, purely from patterns of
sequence conservation across related genomes. The rest of the chapter is about that route, and about
the harder problem it opens up once a motif has been proposed: telling a real occurrence of it from
noise.

## Preview: tomorrow's recitation on SELEX and PBMs

The deck previews the next day's recitation rather than covering it: **SELEX** (Systematic
Evolution of Ligands by Exponential Enrichment; Klug & Famulok, 1994) and **PBMs** (protein-binding
microarrays, using double-stranded DNA arrays; Mukherjee, 2004). Two protocol diagrams accompany
the announcement. The SELEX cycle — credited in the deck to a review on aptamers (Ray & White,
"Aptamers for targeted drug delivery," *Pharmaceuticals*, 2010) — runs: start from a library of
RNA molecules, incubate with the protein target of interest, partition the RNAs that bound the
protein from those that did not, amplify the selected RNAs by RT-PCR, and repeat, enriching the
pool for binders each round. The PBM diagram shows the reverse logic — protein applied to a fixed
array of DNA probes — read out either by tagging the protein with an epitope and detecting it with
a fluorescent antibody, or by fusing it directly to a fluorescent tag.

The recitation's own list of what it will cover is worth recording as a pointer, even though none
of it is developed on these slides: designing PBM probes with de Bruijn graphs, going from raw
$k$-mer counts to a motif, handling gapped and degenerate motifs, using DNA shape to capture what a
simple base-identity motif misses, and relaxing the independence assumption a PWM makes between
positions.

## Finding targets: ChIP and enrichment

For TFs, the standard way to find where a regulator is actually bound in vivo is chromatin
immunoprecipitation, and the deck walks through the protocol as a single diagram, built up in four
stages:

1. Start from cells in which proteins are cross-linked to the DNA they are bound to.
2. Isolate the DNA and fragment it, leaving the cross-linked protein attached.
3. Use an antibody against the regulator of interest to pull down only the DNA fragments carrying
   it — keeping a whole-cell-extract sample aside, without the antibody step, to measure background.
4. Reverse the cross-links and purify the DNA.

From that last, purified pool, the protocol forks in two directions: hybridise it to a tiling
microarray against the whole genome (**ChIP-chip**), or sequence it directly and map the reads back
to the genome (**ChIP-seq**).

For TFs and miRNAs alike, a second and independent line of evidence comes from perturbing the
regulator — knocking it down or removing it — and reading off which genes' expression responds.

Two further methods are marked as today's material and both recur in detail below: enrichment of a
motif among a set of co-regulated genes or among regions already known to be bound, and evolutionary
signatures. For miRNA targets specifically, base-pairing to a hairpin means the composition and
predicted folding stability of a candidate site are themselves used as evidence, on top of sequence
match alone.

## The roadmap for motif discovery

The lecture's own overview slide lays out five steps, and steps 4 and 5 are what the rest of this
chapter works through:

1. Two settings for motif discovery: a set of **co-regulated genes** assumed to share a motif
   (searched with EM or Gibbs sampling), versus ***de novo*** genome-wide discovery with no gene set
   to start from.
2. **Expectation maximisation**, for the co-regulated-gene setting: the motif matrix $M$ and the
   position indicators $Z_{ij}$ are estimated in alternation, $M \Leftrightarrow Z_{ij}$. The E-step
   estimates, from the current motif matrix, where the motif most likely starts in each sequence
   (the values $Z_{ij}$); the M-step then re-estimates the maximum-likelihood motif matrix from all
   of those position estimates.
3. **Gibbs sampling**, as an alternative to EM in the same setting: rather than alternating two
   point estimates, it samples from the joint distribution over $(M, Z_{ij})$, resampling motif
   positions according to the current $Z$ vector. Because it is a stochastic search rather than a
   deterministic hill-climb, the lecture's own verdict is that it is more likely to find the global
   maximum, and it is easy to implement.
4. **Evolutionary signatures for de novo discovery**: score candidate motifs genome-wide by
   cross-species conservation, extend a seed motif using that signal, and validate whatever is
   discovered against independent functional datasets.
5. **Evolutionary signatures for instance identification**: given a motif (from any source), use a
   phylogeny and a branch length score to attach a confidence to each individual occurrence, and
   validate that confidence by comparing real instances against a foreground/background or
   real-versus-control set.

Step 4 is the *de novo* comparative discovery item from the earlier method list; step 5 is where the
enrichment-in-bound-regions item comes back, now as a way of checking a score rather than finding a
motif in the first place.

## The branch length score: scoring a single instance

A discovered motif can match a sequence anywhere in a genome, and most matches will be there by
chance rather than because they do anything. Comparative genomics gives a way to tell the two apart
that does not depend on any functional assay: if an occurrence of the motif is doing something, it
should be under selective constraint, and so it should be conserved — present at the *same aligned
position* — across a wider stretch of the phylogeny than a chance match would be. The **branch
length score (BLS)** of an instance is built directly on that idea: it is the total branch length of
the smallest subtree of the phylogeny connecting the species that share the instance at that aligned
position, normalised by the depth of the whole tree.

<figure>
<svg viewBox="0 0 460 240" role="img" aria-label="A phylogenetic tree illustrating how the branch length score sums the branches spanned by species that share a motif instance at the same aligned position">
  <line x1="20" y1="139" x2="90" y2="139" stroke="currentColor" stroke-width="1.5"/>
  <text x="15" y="130" font-size="11" fill="currentColor" text-anchor="end">ancestor</text>
  <line x1="90" y1="78" x2="90" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="200" x2="330" y2="200" stroke="#2f9e6e" stroke-width="3"/>
  <line x1="90" y1="78" x2="170" y2="78" stroke="#2f9e6e" stroke-width="3"/>
  <line x1="170" y1="40" x2="170" y2="115" stroke="currentColor" stroke-width="1.5"/>
  <line x1="170" y1="40" x2="330" y2="40" stroke="#2f9e6e" stroke-width="3"/>
  <line x1="170" y1="115" x2="250" y2="115" stroke="#2f9e6e" stroke-width="3"/>
  <line x1="250" y1="90" x2="250" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <line x1="250" y1="90" x2="330" y2="90" stroke="#2f9e6e" stroke-width="3"/>
  <line x1="250" y1="140" x2="330" y2="140" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="333" cy="40" r="4" fill="#2f9e6e"/>
  <circle cx="333" cy="90" r="4" fill="#2f9e6e"/>
  <circle cx="333" cy="140" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="333" cy="200" r="4" fill="#2f9e6e"/>
  <text x="342" y="44" font-size="12" fill="currentColor">Human</text>
  <text x="342" y="94" font-size="12" fill="currentColor">Mouse</text>
  <text x="342" y="144" font-size="12" fill="currentColor">Rat</text>
  <text x="342" y="204" font-size="12" fill="currentColor">Dog</text>
</svg>
<figcaption>Human, mouse and dog retain a candidate instance at the same aligned position; rat does
not. The branch length score sums the highlighted branches — the shared ancestry with mouse still
counts, so losing the site in rat alone only removes rat's own terminal branch from the total.</figcaption>
</figure>

The deck makes the "aligned position" condition concrete with a worked comparison: a candidate motif
instance sitting upstream of a gene's transcription start site, checked across human, mouse, rat and
dog. In the case the slides treat as a real hit, the instance sits at the same place relative to the
same gene in all four species. In a contrasting case, the same short sequence is present in rat and
dog, but not at the orthologous position — a coincidence of local sequence, not a conserved
regulatory element — and it is shown alongside a genuine multi-species alignment (seventeen mammals,
from human and chimp down to armadillo and tenrec) in which the real instance's columns are visibly
conserved while its flanks are not.

## Reading the score: signal, noise, and independent validation

Plotted across every candidate instance genome-wide, the branch length score distribution has a
characteristic shape: a very large number of instances cluster at or near zero, and a smaller number
extend out to much higher scores. The lecture's own reading of this shape is to decompose it into
two components it labels "noise" — the near-zero pile, consistent with chance matches under no
constraint — and "signal" — the longer tail, attributed to instances actually under selection. From
that decomposition, a **confidence** can be assigned to any branch length score threshold: roughly,
the fraction of instances at or above that threshold that belong to the "signal" component rather
than the "noise" one. Read off the deck's own curve, confidence starts near zero for the smallest
scores, is already above 0.4 once an instance spans even a modest piece of the tree, and climbs
toward nearly 1 for instances conserved across almost the whole phylogeny.

That confidence score is then checked against evidence the comparative-genomics argument never used:

- **Independent binding data.** Instances above a given confidence cutoff are more enriched among
  regions independently shown to be ChIP-bound, and that enrichment grows as the cutoff is raised —
  shown for at least one specific factor's binding data in the deck, though as two curves rising at
  different rates that the slide does not caption further.
- **A cross-factor comparison.** For three Drosophila mesoderm regulators — Snail, Twist and Mef-2 —
  the deck compares enrichment in muscle-gene promoters under four definitions of a target region:
  sequence motif matches, motif matches that fall outside ChIP-bound regions, ChIP-bound regions
  themselves, and ChIP-bound regions that lack the motif. Twist and Mef-2 come out enriched under
  every one of the four definitions; Snail, in contrast, comes out *depleted* under all four — the
  same validation logic applied to three factors does not tell the same story about all of them.
- **A strand-asymmetry sanity check.** Plotting the fraction of conserved instances that fall on the
  forward strand against confidence separates TF motifs from miRNA motifs cleanly: TF motifs hover
  noisily around 50%, exactly as expected for a double-stranded DNA element with no reason to prefer
  either strand, while miRNA motifs climb toward 100% as confidence rises, consistent with a
  base-pairing interaction with a strand-specific mRNA target that a DNA motif-finder would not
  respect unless the underlying signal really is strand-specific.

Together, these checks are the point of the whole exercise: a branch length score is cheap to
compute from sequence alignments alone, but its calibration — what confidence to attach to a given
score — is only trustworthy once it has been shown to agree with functional evidence gathered by
completely different means.

## Sources

All material is drawn from a single input: the slide deck for MIT OpenCourseWare 6.047/6.878/HST.507
Computational Biology (Fall 2015), lecture 10, "Challenges in regulatory genomics"
(`docs/computational-biology/mit-ocw/6047/lectures/10-slides.md` in the library). No transcript,
notes, or problem set were supplied for this lecture.

The deck's own machine transcription captured only its first three slides as text (the method-list
title slide, the recitation announcement, and the "Motif discovery overview" roadmap); those are the
source for "The pipeline," "Finding regulators," "Preview: tomorrow's recitation," "Finding
targets," and "The roadmap for motif discovery" above, including the $Z_{ij}$/EM/Gibbs-sampling
wording, which is quoted close to the original phrasing. Everything from "The branch length score"
onward was reconstructed by reading the deck's embedded page images directly, since the automatic
transcription treated the rest of the ~80-slide deck as untranscribed figures: the TF/DNA structure
and DNA-binding-fold cartoons and the CACGTG logo (slide images from PDF pages 6 and 8), the PWM/logo
table (page 9), the SELEX and PBM protocol diagrams (pages 10 and 82, with the SELEX diagram's own
attribution to Ray & White, "Aptamers for targeted drug delivery," *Pharmaceuticals* 3(6), 2010),
the generic in vitro genome-scale binding assay (page 10), the ChIP-chip/ChIP-seq protocol (page
62), the cross-species motif-conservation examples and alignment (pages 64–65), the branch length
score histogram and confidence curve (page 67), the strand-asymmetry chart (page 72), and the
confidence/enrichment and Snail/Twist/Mef-2 charts (pages 74, 76 and 77).

A handful of embedded figures could not be responsibly captioned from the material supplied and are
flagged rather than described: a repeated decorative 3-D surface plot (pages 33, 34, 45); several
unlabelled scatter plots (pages 51–53); a network diagram clustering motif-site trees for named
yeast regulators (STRE, GCN4, RAP1, REB1, UME6, CTCGAG, PHO4, MCB, SFF, ESR1, ESR2, page 55); two
stacked-area charts of conserved instances against confidence with no caption (page 70); and a
single-factor (HNF6) bar chart with an unlabelled axis (page 79). A citation visible on one slide but
not obviously tied to the figure around it — Kraut & Levine, "Spatial regulation of the gap gene
giant during Drosophila development," *Development* 111:601–609 (1991) — is recorded here rather
than interpreted. The opening slides also include a specific human-disease regulatory circuit
— thermogenic signalling through ARID5B, an "AATATT" motif, and IRX3/IRX5, affecting
UCP1/PGC1$\alpha$/PRDM16-driven adipocyte browning versus lipid storage (page 7) — which is not
folded into the discussion above: the deck gives it no caption or citation, so what it is doing at
the start of this lecture is left unstated by the material supplied.

---

[← 6. Gene Expression Clustering and Classification](06-gene-expression-clustering-and-classification.md) · [Contents](index.md) · [8. Evolutionary Signatures for Genome Annotation →](08-evolutionary-signatures-for-genome-annotation.md)
