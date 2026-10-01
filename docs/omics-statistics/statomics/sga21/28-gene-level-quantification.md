---
title: "28. Gene-level quantification"
course: "StatOmics Sga21"
chapter: 28
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 28. Gene-level quantification

## What this covers

Once RNA-seq reads have been aligned to a genome, what number do you actually write down as "the
expression of this gene," and why should anyone trust it? This chapter follows that question in
two steps: first, why counting reads exon-by-exon and counting them gene-by-gene are genuinely
different operations that need not agree; second, a worked case — the study that first put RNA-seq
gene counts on the same footing as microarrays — showing how those counts are defined in practice
and how their reproducibility was checked statistically. It assumes the reader already knows what
a read, an exon, a transcript and a gene are, and has seen reads aligned against a reference.

## Why a gene's exons don't just add up

A gene is not one fixed sequence read out every time. The same locus can be spliced into several
different messenger RNAs, each keeping some of the gene's exons and dropping others, and each
translated into a different protein:

<figure>
<svg viewBox="0 0 340 210" role="img" aria-label="A gene with five exons spliced into three different mRNA isoforms, each missing a different subset of exons">
  <text x="4" y="14" font-size="11" fill="currentColor">gene</text>
  <rect x="30" y="8" width="28" height="24" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="44" y="24" font-size="11" text-anchor="middle" fill="currentColor">1</text>
  <rect x="70" y="8" width="28" height="24" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="84" y="24" font-size="11" text-anchor="middle" fill="currentColor">2</text>
  <rect x="110" y="8" width="28" height="24" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="124" y="24" font-size="11" text-anchor="middle" fill="currentColor">3</text>
  <rect x="150" y="8" width="28" height="24" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="164" y="24" font-size="11" text-anchor="middle" fill="currentColor">4</text>
  <rect x="190" y="8" width="28" height="24" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="204" y="24" font-size="11" text-anchor="middle" fill="currentColor">5</text>
  <line x1="124" y1="40" x2="124" y2="58" stroke="currentColor" stroke-width="1.2"/>
  <polygon points="124,62 120,54 128,54" fill="currentColor"/>
  <text x="230" y="55" font-size="11" fill="currentColor">alternative splicing</text>

  <text x="4" y="94" font-size="11" fill="currentColor">mRNA A</text>
  <rect x="30" y="80" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="70" y="80" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="110" y="80" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="150" y="80" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="190" y="80" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <text x="4" y="134" font-size="11" fill="currentColor">mRNA B</text>
  <rect x="30" y="120" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="70" y="120" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="150" y="120" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="190" y="120" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="124" y="136" font-size="10" text-anchor="middle" fill="currentColor">(exon 3 skipped)</text>

  <text x="4" y="174" font-size="11" fill="currentColor">mRNA C</text>
  <rect x="30" y="160" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="70" y="160" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="110" y="160" width="28" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="200" y="176" font-size="10" text-anchor="middle" fill="currentColor">(exons 4, 5 skipped)</text>
</svg>
<figcaption>The same gene body, spliced into three isoforms that each keep a different subset of
its exons and are translated into different proteins. Exons 1 and 2 are shared by every isoform;
exon 3 and the pair 4–5 are not.</figcaption>
</figure>

That picture is the reason two different ways of counting the same aligned reads give different
answers.

**Gene-level quantification** assigns a read to a gene as soon as the read falls anywhere within
that gene's exons — its "gene body," taken as the union of all exons across all of its annotated
transcripts — and adds up all such reads into one number per gene.

**Exon-level quantification** instead keeps one running total per exon: a read is tallied against
whichever specific exon(s) it overlaps, so a single gene ends up with as many counts as it has
exons.

A worked example makes the two disagree in a way that is easy to reproduce: for one gene, summing
reads over the whole gene body gives a total of $30$, while the five exons of that gene, counted
separately, give totals of $11, 7, 10, 6, 6$ — which add up to $40$, not $30$. That is exactly what
the splicing picture predicts: a read that lands where two exons or two isoforms overlap (for
instance, one spanning an exon–exon junction) can be legitimately tallied into more than one
exon's count, while the gene-level total only ever adds that read in once, wherever in the gene
body it happens to fall. The two schemes are not two ways of writing the same number — gene-level
counting discards exactly the isoform information the exon-level counts still carry.

## Turning a pile of reads into "the" gene count

The rest of this chapter follows one worked case in detail: a study built to check whether
gene-level counts, defined and computed at scale, behave the way a measurement of expression
should. Its counts were built as follows. For each lane of sequencing, a gene's count is the sum of
all reads mapping to exons within that gene; for a gene with more than one annotated transcript,
the count used is the median across its transcripts. Under idealized assumptions — no alignment
errors, no sequence-context bias in which fragments get sequenced — a gene's count is, in
expectation, proportional to its transcript length times its mRNA expression level.

In that study, $22{,}925$ of the genes in the Ensembl database (72%) were hit by at least one read.
The distribution of read counts across genes was heavily skewed: most genes had relatively few
reads, with a median of 46 reads per gene in the liver sample and 101 in the kidney sample. As a
first, rough check of reproducibility, the gene counts for a given sample were highly correlated
across lanes — an average Spearman correlation of 0.96.

## A case study: comparing sequencing counts against a mature technology

The design behind these numbers set up a direct comparison between gene-level RNA-seq counts and
the technology they were being asked to replace. Total RNA was extracted from liver and kidney
samples of a single human male, the poly(A) mRNA purified and sheared, and the resulting cDNA
sequenced on an Illumina Genome Analyzer. To test reproducibility at more than one level, each
sample was sequenced seven times, split across two runs of the machine, and at two different cDNA
concentrations (3 pM, five lanes per sample; 1.5 pM, two lanes per sample). The same RNA samples
were also hybridized, in three technical replicates, to Affymetrix U133 Plus 2 microarrays. To make
the two platforms comparable gene-for-gene, array probe sets were mapped onto Ensembl v.48 genes;
17,708 probe sets mapped uniquely to 17,708 genes, and these were used for the comparison.

Reads were aligned genome-wide with ELAND, allowing at most two mismatches and keeping only reads
that mapped to a single genomic location. Of all reads, 40% mapped uniquely; of those, 65% mapped
to autosomal or sex chromosomes (almost all the rest to mitochondrial DNA). Of the mapped reads,
83% fell in annotated genic regions, and 68% of those fell specifically in annotated exons — which
is the population of reads that feeds the gene-level count defined above. A sizeable minority
(10.6%) of the reads that fell outside annotated genes mapped more than 100 kb from any known gene,
consistent with there being transcriptionally active regions not yet in the annotation.

## Testing the count for a "lane effect"

The question the design was built to answer is whether a gene's count depends on more than just
how much of its mRNA was in the sample — specifically, whether it depends systematically on which
lane, run, or concentration happened to be used, over and above the variation you'd expect from
sampling reads at random. Call any such systematic, non-sampling difference between technical
replicates a **lane effect**. Two statistical tests were used to look for one.

**Pairwise test.** For two lanes sequencing the same sample, fix the total number of reads landing
in each lane. If there is no lane effect, then for any one gene, how those total reads split
between the two lanes should look like a random draw governed by the hypergeometric distribution —
the split shouldn't depend on which gene the reads came from. That gives one $p$-value per gene.
Under the null hypothesis of no lane effect, these $p$-values should be uniform on $[0,1]$, so a
quantile-quantile plot of the observed $p$-values against a uniform reference should sit on the
diagonal; genes with a real lane effect show up as points that peel away from it.

**Joint, multi-lane test.** Let $x_{ijk}$ be the number of reads mapping to gene $j$ in the $k$-th
lane of sample $i$. Model these as independent Poisson variables with mean $\mu_{ijk} =
c_{ik}\lambda_{ijk}$, where $c_{ik}$ is the total rate at which lane $k$ of sample $i$ produces
reads, and $\lambda_{ijk}$ is the share of reads gene $j$ should get relative to every other gene in
that lane, constrained so that $\sum_j \lambda_{ijk} = 1$. No lane effect means $\lambda_{ijk}$ is
the same for every lane $k$ of a given sample — the same gene claims the same relative share of
reads no matter which lane it was sequenced in. For each gene, a goodness-of-fit statistic computed
across all $L$ lanes tests exactly this; under the null it should follow a $\chi^2$ distribution on
$L-1$ degrees of freedom.

<figure>
<svg viewBox="0 0 300 220" role="img" aria-label="A quantile-quantile plot: most genes fall on the diagonal expected under no lane effect, a small tail departs from it">
  <line x1="40" y1="180" x2="280" y2="180" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="20" x2="40" y2="180" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="180" x2="200" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <path d="M40,180 C90,140 130,95 160,70 S190,45 205,35 S225,25 240,20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="203" text-anchor="middle" font-size="12" fill="currentColor">expected under no lane effect</text>
  <text x="16" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 100)">observed statistic</text>
  <text x="95" y="160" font-size="11" fill="currentColor">bulk of genes: on the line</text>
  <text x="205" y="55" font-size="11" fill="currentColor">tail: lane effect</text>
</svg>
<figcaption>The diagnostic behind both tests: plot the observed statistic (a p-value or a
goodness-of-fit statistic, one per gene) against what is expected if there is no systematic lane
effect. Points on the diagonal are consistent with pure sampling noise; a small tail pulling above
it flags genes with a real, systematic difference between replicates.</figcaption>
</figure>

The pairwise test was run on 22 comparisons between lanes sequencing the same sample at the same
concentration: consistently fewer than 0.5% of genes showed the very small $p$-values that would
indicate a lane effect, though comparisons across the two runs showed slightly more of this than
comparisons within a single run. The same test applied to two lanes sequencing the same sample at
*different* concentrations showed much larger departures from the diagonal — concentration, unlike
lane or run, does appear to introduce a systematic effect. The joint, multi-lane $\chi^2$ test told
the same story: only around 0.5% of genes showed strong evidence of extra-Poisson variation, for
both the liver and the kidney sample sequenced at either concentration.

## What a carefully defined count buys you

Taken together, this is the case for trusting a gene-level RNA-seq count as a measurement: gene
counts correlate strongly (Spearman $\approx 0.96$) across technical replicates, and the way they
vary across lanes is well described by simple Poisson sampling for well over 99% of genes. Because
that Poisson model captures the technical noise, it can also be used directly to test for
differential expression between conditions — and doing so on this data identified 30% more
differentially expressed genes than a standard analysis of the array data found at the same false
discovery rate. The comparison also illustrates the earlier point about gene- versus exon-level
counting from the other direction: because sequencing counts reads rather than fluorescence
intensity, the same data can be used to flag alternative splicing directly — something a single
gene-level number, by construction, cannot show.

## Sources

- `01-gene-level-quantification.md` (a model's page-by-page reconstruction of
  `images_sequencing/seqKeynote.pdf`, statOmics SGA21, licensed CC BY-NC-SA 4.0) — the gene-level vs.
  exon-level worked example and its numbers ($\sum=30$ against $11,7,10,6,6$), and the alternative
  splicing figure on page 1 of the deck (`figures/p001-6.png`), redrawn here as the isoform diagram.
- `02-results.md` (same deck, same conversion) — the definition of a gene count, the experimental
  design, the alignment statistics, the hypergeometric and Poisson lane-effect tests, and the
  closing comparison with the array data. The study-design figure (`figures/p002-2.jpeg` /
  `p003-2.jpeg`) and the four-panel quantile-quantile plot (`figures/p002-1.jpeg` / `p003-1.jpeg`)
  were consulted for this chapter's redrawn QQ-plot diagram.
- Both source files are flagged by the conversion itself as **reconstructed**: the original PDF
  had no extractable text layer, a model read the pages, and every equation in it is marked
  unverified. The numbers and formulas above are reproduced as given in that reconstruction and
  should be checked against the original deck (linked in both files) before being relied on.
- The prose making up most of `02-results.md`, and the closing paragraph of `01-gene-level-
  quantification.md`, is recognizable — from the specific design (liver and kidney RNA from one
  human male, Illumina Genome Analyzer, ELAND alignment, Affymetrix U133 Plus 2 arrays, Ensembl
  v.48, 17,708 mapped probe sets) — as the results and abstract of Marioni, Mason, Mane, Stephens
  & Gilad, "RNA-seq: an assessment of technical reproducibility and comparison with gene expression
  arrays," *Genome Research* (2008). The slide deck carries no citation for it, and the full paper
  — its Methods section, and the Supplemental Tables and Figures referenced throughout ("Supplemental
  Table 1," "Supplemental Fig. 1–6") — was not supplied and is not part of this chapter.
- No slides, transcript, written notes beyond the two files above, or exercises were supplied for
  this chapter.

---

[← 27. Recap: The General Linear Model](27-recap-the-general-linear-model.md) · [Contents](index.md) · [29. Poisson GLMs for Count Data →](29-poisson-glms-for-count-data.md)
