---
title: "11. Genome Alignment and Evolution"
course: "MIT 6047"
chapter: 11
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Genome Alignment and Evolution

## What this covers

Two genomes are almost never one long collinear match: insertion, deletion, duplication,
inversion and translocation break up the correspondence between them. This chapter asks how you
align whole genomes anyway, and what falls out of doing so — which parts of a genome change fast
and which stay frozen, what mechanisms drive rearrangement, and how a single ancient duplication
event leaves a recognisable fingerprint millions of years later. It assumes you already have
pairwise sequence alignment by dynamic programming: global (Needleman–Wunsch, end-to-end) and
local (BLAST-style, best-matching subregions) alignment are both used here as building blocks
rather than derived again.

## From pairwise alignment to whole-genome alignment

Running a single global dynamic-programming alignment across two whole genomes is both too slow —
the table is quadratic in genome length — and the wrong model, since it assumes the two sequences
stay collinear from start to end, which real genomes do not.

The fix used by the tools in this lecture is to separate finding matches from connecting them.
First run an efficient local aligner such as BLAST to find all of the local alignments between the
two genomes — this is fast because it does not have to explain every position, only the ones that
match well. Then chain the local alignments that fall along a consistent diagonal into a single
path, and only fall back on the expensive dynamic program to fill in the small rectangles left
between consecutive anchors. Local alignment finds the easy 90%; restricted dynamic programming
mops up the hard, ambiguous 10% between anchors.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Local alignments chained along the diagonal, with dynamic programming restricted to the small gaps between them">
  <line x1="40" y1="190" x2="320" y2="190" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1"/>
  <text x="180" y="208" text-anchor="middle" font-size="12" fill="currentColor">genome A position</text>
  <text x="14" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 14 105)">genome B position</text>
  <line x1="45" y1="185" x2="315" y2="25" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 3" opacity="0.4"/>
  <line x1="55" y1="172" x2="90" y2="150" stroke="currentColor" stroke-width="3"/>
  <line x1="130" y1="118" x2="160" y2="98" stroke="currentColor" stroke-width="3"/>
  <line x1="205" y1="72" x2="235" y2="52" stroke="currentColor" stroke-width="3"/>
  <line x1="270" y1="38" x2="295" y2="28" stroke="currentColor" stroke-width="3"/>
  <rect x="90" y="98" width="40" height="52" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <text x="42" y="145" font-size="11" fill="currentColor">local alignment</text>
  <text x="96" y="93" font-size="11" fill="currentColor">restricted DP</text>
</svg>
<figcaption>BLAST-style local alignments (thick segments) are chained along the diagonal; dynamic
programming is only run in the rectangles between them, not across the whole genome.</figcaption>
</figure>

Extending this idea further gives **glocal alignment**: instead of requiring the chain of local
alignments to run along a single diagonal, allow it to also include inversions, duplications and
translocations, and connect the pieces by their least-cost transformation into one another. The
name is deliberate — it combines the coverage of global alignment with the flexibility of local
alignment, aiming for the most accurate picture of how genomes actually evolve, rather than the
most collinear one.

**LAGAN** is the toolkit built around these ideas, in three variants:

- **Regular LAGAN** does exactly the three-step recipe above: find local alignments, chain them
  along the diagonal, then run restricted dynamic programming between them.
- **Multi-LAGAN** generalises this to several species at once. Given a set of genomes and a
  phylogenetic tree, it aligns pairwise guided by the tree — comparing the most closely related
  species first, then bringing in progressively more distant ones.
- **Shuffle-LAGAN (S-LAGAN)** is the glocal version. It (A) finds all local alignments, (B) builds
  a rough homology map by choosing the maximum-scoring subset of local alignments, under gap and
  transformation penalties, that forms a non-decreasing chain in at least one of the two sequences
  — and unlike regular LAGAN, every ordering of local alignments is allowed as a step, since it
  might represent a translocation, an inversion or an inverted translocation rather than an
  untransformed match — and (C) breaks the resulting homology map into chunks that follow roughly
  one continuous path, finishing each chunk with ordinary LAGAN-style restricted dynamic
  programming.

Running Shuffle-LAGAN, or another glocal aligner, over a genome pair surfaces its inversions,
translocations and other rearrangements directly. Mapping out those rearrangements is itself a
window onto how each species diverged from a common ancestor.

## Aligning genomes gene by gene

A different strategy skips nucleotide-level alignment as the anchor and uses genes instead:
identify which gene in one genome corresponds to which gene in the other, use that correspondence
to pin down which regions of the two genomes are homologous, and only then run a nucleotide-level
alignment within each multiply-conserved region.

The hard part is that gene correspondence is not always one-to-one. Genes diverge, duplicate and
get lost, and whole genomes rearrange around them, so resolving correspondence needs two kinds of
evidence: amino-acid similarity between candidate gene pairs, and where each gene sits within its
own genome.

The natural structure for this is a weighted **bipartite graph**: a graph whose vertices split into
two disjoint sets $U$ and $V$ such that every edge joins a vertex in $U$ to a vertex in $V$. Here
$U$ and $V$ are the gene sets of the two genomes, each node carries the gene's genomic coordinates,
and each edge is weighted by sequence similarity. An **orthologous** relationship is a one-to-one
match in this graph; a **paralogous** relationship is one-to-many or many-to-many, reflecting
within-genome duplication. The graph is first simplified by removing spurious edges, and the
remaining edges are chosen using conserved gene order and protein sequence similarity.

The **Best Unambiguous Subgroups (BUS)** algorithm then resolves the correspondence of genes and
regions from this graph. It extends the standard heuristic of best-bidirectional hits with
iterative refinement at an increasing relative threshold, using the full bipartite connectivity
together with amino-acid similarity and gene-order information. Applied to *S. cerevisiae* against
three related species, this correctly resolved more than 90% of genes to a one-to-one
correspondence, and located the remaining regions and protein families as exactly the ones
undergoing rapid change.

## Rates and mechanisms of genome evolution

Once genomes are aligned, comparing the alignments reveals their evolutionary history — and the
first thing it shows is that the rate of change is very unevenly distributed.

**Across the genome:** in *S. cerevisiae*, 80% of alignment ambiguities are concentrated in just 5%
of the genome, and that 5% corresponds almost entirely to telomeric regions — 31 of the genome's 32
telomeres. **Telomeres** are the repetitive DNA sequences capping the ends of chromosomes that
protect them from degradation; they are also inherently structurally unstable. Gene families
located there — HXT, FLO, COS, PAU and YRF — show substantial evolution in copy number, order and
orientation, and several novel protein-coding sequences arise specifically in these regions. Because
genomic rearrangement is otherwise rare in *S. cerevisiae*, regions of rapid change can effectively
be spotted just by looking for protein family expansions at the chromosome ends.

**Across individual genes:** rates vary just as sharply gene by gene. YBR184W in yeast shows
unusually low sequence conservation and numerous insertions and deletions across species, while at
the opposite extreme MatA2 shows perfect amino acid and nucleotide conservation. Mutation rate also
tracks functional class — mitochondrial ribosomal proteins, for instance, are less conserved than
(cytoplasmic) ribosomal proteins. Some of the difference between species may simply reflect factors
such as longer life cycles giving fewer generations per unit time; but the near-total absence of
change in a specific gene like MatA2 suggests an additional biological function is constraining it
beyond whatever is already known. Yeast switch mating type by exchanging their entire complement of
A and $\alpha$ genes, and MatA2 is one of the four mating-type genes (MatA2, Mat$\alpha$2, MatA1,
Mat$\alpha$1); its perfect conservation hints that nucleotide-level conservation analysis could
reveal a role for it beyond the one currently known.

Fast evolution is not just noise, either — several mechanisms make rapid protein change functional:

- **Protein domain creation** via stretches of glutamine (Q) and asparagine (N), which support new
  protein–protein interactions.
- **Compensatory frameshifts**, which let a lineage explore new reading frames and read or create
  RNA-editing signals.
- **Stop-codon variation and regulated read-through** — gaining a stop enables rapid change, while
  losing one can generate new diversity by extending the protein.
- **Inteins** — protein segments that excise themselves post-translationally and rejoin the
  remaining protein, which can spread between lineages via horizontal transfer.

**Across species:** comparing gene content among *S. cerevisiae*, *S. paradoxus*, *S. mikatae* and
*S. bayanus* — by tracking the genomic position and rate of change of paralogs — reveals patterns of
gene loss and gene conversion. Each genome carries roughly 8–10 genes unique to it, mostly involved
in metabolism, regulation and silencing, and stress response. Gene dosage also changes through
tandem and segmental duplication, and protein family expansion leaves 211 genes with ambiguous
correspondence across the four species. Even so, truly novel genes are rare — most of the
difference between these genomes is rearrangement, loss or duplication of existing genes rather
than new gene birth.

### Chromosomal rearrangements

Translocations between otherwise dissimilar genes are frequently mediated by transposable genetic
elements — Ty elements, in yeast. Transposon locations themselves are conserved: recent insertions
turn up at old, previously-used locations, and remnants of long terminal repeats from earlier
insertions are found in other genomes. Yet the transposons are also evolutionarily active — yeast Ty
elements, for example, are recent insertions — and typically appear in only one genome at a time.
Keeping transposon locations conserved may be advantageous precisely because it allows reversible
rearrangements at those sites. Separately, inversions are often flanked by tRNA genes in opposite
transcriptional orientation, suggesting that the inversions themselves arise from recombination
between the flanking tRNA genes.

## Whole-genome duplication

Moving further back in evolutionary time changes which questions become askable. The lecture's
example is *K. waltii*, placed at roughly 95 million years before the divergence of *S. cerevisiae*
and 80 million years before that of *S. bayanus*.

A dotplot of *S. cerevisiae* chromosomes against *K. waltii* scaffolds is mostly a single clean
diagonal — the signature of ordinary one-to-one conserved synteny — except in the middle of the
plot, where the diagonal visibly splits rather than running straight. Zooming in on that split shows
why: two separate *S. cerevisiae* "sister fragments" both map onto the *same* corresponding region
of the *K. waltii* scaffold, a 2-to-1 correspondence rather than 1-to-1.

Looking at gene order within these sister regions (the same trick used to recognise sister regions
around duplicated centromeres) shows **gene interleaving**: each of the two *S. cerevisiae* copies
retains only part of the ancestral gene order, and the two retained subsets are complementary, so
that laid side by side they reconstruct the full ancestral order gene by gene.

<figure>
<svg viewBox="0 0 360 190" role="img" aria-label="Two duplicated chromosome regions each keep a complementary half of an ancestral gene order, interleaving to reconstruct it">
  <text x="8" y="34" font-size="12" fill="currentColor">K. waltii region (ancestral)</text>
  <text x="8" y="94" font-size="12" fill="currentColor">S. cerevisiae copy A</text>
  <text x="8" y="154" font-size="12" fill="currentColor">S. cerevisiae copy B</text>
  <g stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 3" opacity="0.35">
    <line x1="140" y1="40" x2="140" y2="160"/>
    <line x1="168" y1="40" x2="168" y2="160"/>
    <line x1="196" y1="40" x2="196" y2="160"/>
    <line x1="224" y1="40" x2="224" y2="160"/>
    <line x1="252" y1="40" x2="252" y2="160"/>
    <line x1="280" y1="40" x2="280" y2="160"/>
    <line x1="308" y1="40" x2="308" y2="160"/>
    <line x1="336" y1="40" x2="336" y2="160"/>
  </g>
  <g fill="currentColor">
    <circle cx="140" cy="40" r="6"/><circle cx="168" cy="40" r="6"/><circle cx="196" cy="40" r="6"/>
    <circle cx="224" cy="40" r="6"/><circle cx="252" cy="40" r="6"/><circle cx="280" cy="40" r="6"/>
    <circle cx="308" cy="40" r="6"/><circle cx="336" cy="40" r="6"/>
  </g>
  <g fill="currentColor">
    <circle cx="140" cy="100" r="6"/><circle cx="196" cy="100" r="6"/>
    <circle cx="252" cy="100" r="6"/><circle cx="308" cy="100" r="6"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="1" opacity="0.4">
    <circle cx="168" cy="100" r="6"/><circle cx="224" cy="100" r="6"/>
    <circle cx="280" cy="100" r="6"/><circle cx="336" cy="100" r="6"/>
  </g>
  <g fill="currentColor">
    <circle cx="168" cy="160" r="6"/><circle cx="224" cy="160" r="6"/>
    <circle cx="280" cy="160" r="6"/><circle cx="336" cy="160" r="6"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="1" opacity="0.4">
    <circle cx="140" cy="160" r="6"/><circle cx="196" cy="160" r="6"/>
    <circle cx="252" cy="160" r="6"/><circle cx="308" cy="160" r="6"/>
  </g>
</svg>
<figcaption>Filled circles mark genes retained after duplication, open circles mark genes lost from
that copy. Copy A and copy B retain complementary genes, and together interleave to reconstruct the
single ancestral order.</figcaption>
</figure>

This complementary, interleaved retention pattern is the evidence itself: it is what you would
expect from a single ancestral genome duplicating and then each copy independently losing roughly
half of the redundant genes, and it is not the pattern two unrelated, independent duplications would
be expected to leave behind.

## Sources

- Notes: `computational-biology/mit-ocw/6047`, compiled document
  `docs/computational-biology/mit-ocw/6047/compiled/compiled-compiled/01-introduction.md`, sections
  5.4.2–5.8 (Lagan chaining of local alignments; gene-based region alignment and the BUS algorithm;
  mechanisms of genome evolution; chromosomal rearrangements; whole-genome duplication in *K.
  waltii*). No slides, transcript or exercises were supplied for this chapter — the compiled notes
  document is the only input.
- The source file itself carries a fidelity warning worth repeating here: it is a model's
  reconstruction of a PDF with no usable text layer, the prose is paraphrased in places, and any
  equations in it are unverified. It should be treated as a pointer into the original MIT OCW 6.047
  (Computational Biology, Fall 2015) materials, not as a citable source in its own right.
- The excerpt begins mid-chapter (headed "Chapter Two: Sequence Alignment and Dynamic Programming"
  but numbered as section 5.4 onward, suggesting a multi-year compiled course document) and ends
  mid-heading at "Chapter Six." Earlier material it refers to but that is not included in this
  excerpt: Figure 2.1 (a sequence alignment of Gal10-Gal1 across four yeast strains) and Figure 5.15
  (the Needleman-Wunsch algorithm for two- and three-genome alignment), both of which this chapter
  assumes as background rather than covers.
- The source's own bibliography names further material not included here: Kellis, *Lecture slides
  04/05.1/05.2: Comparative genomics I-III* (2010); Batzoglou et al., *Arachne: a whole-genome
  shotgun assembler*, Genome Research (2002); Chen and Rajewsky, *The evolution of gene regulation
  by transcription factors and microRNAs*, Nature Reviews Genetics (2007); Robinson and Cooley,
  *Examination of the function of two kelch proteins generated by stop codon suppression*,
  Development (1997); Stark et al., *Discovery of functional elements in 12 Drosophila genomes using
  evolutionary signatures*, Nature (2007); Tan, *Lecture 15 notes: Comparative genomics I: genome
  annotation* (2009).

---

[← 10. Disease Epigenomics and Genetic Epidemiology](10-disease-epigenomics-and-genetic-epidemiology.md) · [Contents](index.md) · [12. Genomics of Microbial Ecosystems →](12-genomics-of-microbial-ecosystems.md)
