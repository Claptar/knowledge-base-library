---
title: "8. RNA-seq, Isoforms, and Expression Statistics"
course: "MIT 7.091J"
chapter: 8
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. RNA-seq, Isoforms, and Expression Statistics

## What this covers

How do you go from a pile of short sequencing reads to a quantitative statement about which gene
isoform is expressed, and whether a gene changes expression between two conditions? This chapter
follows RNA-seq from the bench protocol through to the statistics used to analyse it: a generative
model for reads that lets you estimate isoform abundance, the likelihood-ratio machinery used to
decide whether an apparent difference is real, the specific negative-binomial test (DESeq) used
for differential expression, the hypergeometric test used to ask whether a gene list is enriched
for some annotation, and principal component analysis, built up from multivariate Gaussians, used
to find structure in expression data. It closes with single-cell RNA-seq, which is where all of
the above gets used in practice. It assumes familiarity with genome assembly and mapping (reads,
coverage, the idea of mapping to a reference), with Poisson/negative binomial counting models and
library complexity from the ChIP-seq material, and with basic linear algebra (eigenvectors,
diagonalisation).

## RNA-seq: from RNA to reads

RNA-seq characterises the RNA molecules present in a cell or population of cells by sequencing
them. The basic protocol: isolate RNA from the sample, reverse-transcribe it to cDNA, fragment and
sequence the fragments, and map the resulting reads back to the genome.

What you isolate matters. Without any selection you get everything — unspliced pre-mRNA, introns,
and the many non-coding RNA species (long non-coding RNAs, of which over 3,300 had been
characterised at the time of the lecture, are one class). That is a great deal of noise if what
you want is gene expression. The usual fix is to purify for the poly-A tail, which selects mature,
spliced messenger RNA and excludes most intronic and non-coding reads. Mapped read data from such
an experiment looks like a pileup along the genome — the lecture showed the SOX2 locus, with reads
on the plus strand in one colour and the minus strand in another — concentrated over exons, with a
real, informative class of reads that cross an exon–exon boundary: a contiguous stretch of a
single RNA molecule that, in genomic coordinates, jumps over an intron. A mapper used for RNA-seq
has to be able to find these split alignments, which is one reason reads around 100 bases long are
preferred: long enough that a useful fraction of them cross a junction.

Two standard normalised units appear in the literature for a mapped library: RPKM (reads per
kilobase of transcript per million mapped reads) and FPKM (fragments per kilobase per million),
the latter used for paired-end data where a single sequenced *fragment* is represented by a read at
each end. Both divide out transcript length and library depth, so that a long gene and a short
gene with the same per-base expression are not reported as different.

## Isoforms, and the problem of assigning reads to them

An **isoform** is a particular splice variant of a gene: a specific choice, for each exon, of
whether it is retained or skipped. A gene with three exons could produce a transcript with all
three, or one that omits the middle exon, and so on — in principle a gene with $n$ exons has up to
$2^n$ possible isoforms, though in practice far fewer are ever actually produced; which ones appear
depends on the regulation of the splicing machinery (some splicing is constitutive, some
conditional on which splicing factors are expressed).

The analysis problem: given the read pileup for a gene, which isoforms are present, and in what
relative amounts? Reads carry two distinct kinds of evidence. A read landing within a single exon
tells you that exon is used by *some* transcript in the mixture, but not which one. A read that
spans a junction is sharper: it tells you two exons were spliced together in one contiguous
molecule. In particular, a junction-spanning read can be an **inclusion** read, supporting a middle
exon being retained, or an **exclusion** read, supporting it being skipped.

<figure>
<svg viewBox="0 0 400 210" role="img" aria-label="Junction-spanning reads supporting inclusion or exclusion of a middle exon">
  <rect x="40" y="95" width="60" height="30" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="70" y="115" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <rect x="170" y="95" width="60" height="30" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="200" y="115" text-anchor="middle" font-size="12" fill="currentColor">C</text>
  <rect x="300" y="95" width="60" height="30" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="330" y="115" text-anchor="middle" font-size="12" fill="currentColor">E</text>

  <path d="M 80 95 Q 125 55 170 95" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 210 95 Q 255 55 300 95" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="40" text-anchor="middle" font-size="12" fill="currentColor">inclusion reads: A–C and C–E junctions</text>

  <path d="M 80 125 Q 200 180 300 125" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="200" text-anchor="middle" font-size="12" fill="currentColor">exclusion read: A–E junction, C skipped</text>
</svg>
<figcaption>Reads spanning an A–C or C–E junction support inclusion of exon C; a read spanning
directly from A to E supports its exclusion.</figcaption>
</figure>

There are two general strategies for reconstructing transcripts from reads. One is *de novo*
assembly of the reads into transcripts, using the same assembly ideas as genome assembly; it has
the advantage of needing no reference genome, which matters for organisms without one, but
inherits assembly's correctness problems. The more common approach, and the one developed below,
is to map reads to a reference genome and use the pattern of junction and exon coverage, together
with a probabilistic model, to infer which isoforms are present and in what proportion.

## A generative model for a read, given an isoform

The strategy is to treat each read as a piece of evidence and build $P(\text{read}_i \mid
\text{isoform}_j)$ — the probability of observing a particular read if a particular isoform had
produced it — and then combine reads like a detective combining clues. There are three cases.

**Incompatible.** If a read's alignment (for instance a junction it crosses) is simply not
consistent with isoform $j$'s exon structure, $P(\text{read}_i \mid \text{isoform}_j) = 0$. This
holds whether the read is single- or paired-end.

**Single-end, compatible.** If isoform $j$ has (spliced, mature) length $l_j$, and the read is
assumed equally likely to start at any base of the transcript, then
$$P(\text{read}_i \mid \text{isoform}_j) = \frac{1}{l_j}.$$
This is simply "where along the transcript does the read align" — a uniform choice over $l_j$
positions. The uniformity assumption is a simplification: because libraries are typically purified
by pulling on the poly-A tail, and partially degraded molecules lose length from the 5′ end while
still having the tail, real libraries often show a bias toward the 3′ end. The model above ignores
that bias.

**Paired-end, compatible.** A paired-end read sequences both ends of a fragment without observing
the middle (the *insert*): if each read is 100 bases and the whole fragment is 300 bases, the
unobserved insert is 100 bases in the middle. Here the probability has two factors,
$$P(\text{read}_i \mid \text{isoform}_j) = \frac{1}{l_j}\, F\big(l_j(R_i)\big),$$
where the first factor is again the uniform choice of alignment position, and the second scores
the *implied fragment length* $l_j(R_i)$ — the distance between the two mapped ends, measured along
the spliced transcript, not along the genome — against $F$, a distribution over fragment lengths
fit from the library preparation (for instance centred around 200 bases). A pair of ends that,
mapped onto isoform $j$, implies a 200-base insert is scored as likely; one implying 400 bases is
scored as unlikely, because that is a much rarer fragment length in the library. This is how
paired-end data discounts an alignment to an isoform that would require an implausibly long or
short insert.

### From single-read probabilities to isoform proportions

Given a mixture of isoforms with unknown relative proportions $\psi_j$ (the fraction of transcripts
in the pool that are isoform $j$), the probability of a single observed read, marginalising over
which isoform produced it, is
$$P(\text{read}_i) = \sum_j \psi_j\, P(\text{read}_i \mid \text{isoform}_j),$$
and the likelihood of the whole basket of reads observed for a gene is the product over reads,
$$P(\text{all reads}) = \prod_i \sum_j \psi_j\, P(\text{read}_i \mid \text{isoform}_j).$$
Isoform quantitation is then choosing $\psi$ (the vector of isoform fractions) to maximise this
likelihood — the same kind of mixture-proportion estimation used earlier in the course for ChIP-seq.
In practice this is solved with EM or similar iterative methods. Two programs implementing this
(enumerating candidate isoforms from junction evidence, then fitting $\psi$) are **Cufflinks** and
**MISO**. Applied to an RNA-seq time series of myogenesis, Cufflinks placed 70% of reads in
previously annotated transcripts but also identified 643 new isoforms in that single series; genes
expressed at low copy number necessarily have sparse coverage and are harder to resolve. A caveat
raised in discussion: with reads much shorter than a full transcript, you can establish that two
*adjacent* exons are spliced together, but not necessarily that two exons far apart in the same
transcript are — unless a paired-end fragment, or a long enough single read, spans the distance.
Long-read sequencing (tens of kilobases) was noted as the technology that removes this limitation.

## An interlude on hypothesis testing: the likelihood-ratio test

Differential expression needs a principled way to ask "is this difference real, or could it have
arisen by chance under a single, shared model?" The general tool is the **likelihood-ratio test**.

Suppose a null model $H_0$ and an alternative $H_1$ are both fit to the same data, where $H_1$ has
more free parameters than $H_0$ (so $H_0$ is a restriction of $H_1$). Because $H_1$ has strictly
more freedom, it will always fit the observed data at least as well — the question is never "which
fits better" but "is it enough better to reject $H_0$". The test statistic is
$$\Lambda = 2 \log \frac{P(\text{data} \mid H_1)}{P(\text{data} \mid H_0)},$$
which is always $\ge 0$. Under $H_0$, $\Lambda$ follows (asymptotically) a chi-squared distribution
whose degrees of freedom equal the difference in the number of free parameters between $H_1$ and
$H_0$. Given an observed value $T_{\text{obs}}$, the p-value is the upper tail,
$$p = P(\Lambda \ge T_{\text{obs}} \mid H_0),$$
read off the chi-squared distribution with that many degrees of freedom.

The lecture's worked example: two genes' expression values, plotted against each other, were fit
either as two independent univariate Gaussians ($H_0$) or as a single correlated bivariate Gaussian
($H_1$). By the class's count in this example, $H_0$ had four free parameters (two means, two
variances) and $H_1$ had six (two means plus the parameters of the joint covariance structure), a
difference of two degrees of freedom, and the data in the example favoured $H_1$: the correlated
model was enough better to reject independence. The same apparatus — fit a restricted and an
unrestricted model, compare twice the log-likelihood ratio against a chi-squared distribution with
the parameter-count difference — is what the DESeq test below uses to decide whether a gene's mean
expression differs between two conditions.

## Differential expression: DESeq

Write $i$ for a gene or isoform, $j$ for a replicate (an individual sequencing experiment — several
replicates may share the same biological condition), and $K_{ij}$ for the observed read count of
gene $i$ in replicate $j$.

**Normalisation.** Replicates differ in total sequencing depth, so raw counts are not directly
comparable across them. DESeq computes a size factor $s_j$ per replicate: for each gene, take the
ratio of its count in replicate $j$ to the geometric mean of its count across all replicates, and
let $s_j$ be the median of these ratios over all genes. The geometric mean in the denominator is
used (rather than an arithmetic mean) so that no single highly-expressed gene dominates the
average — every gene contributes on an equal footing. If every replicate had identical depth, every
$s_j$ would equal 1; a replicate with exactly twice the depth of the others would get $s_j = 2$.

**Condition-level expression.** For a condition $p$ (which may pool several replicates), the
normalised expression of gene $i$ is the average, over the replicates belonging to that condition,
of $K_{ij}/s_j$:
$$q_{ip} = \text{average over replicates } j \text{ in condition } p \text{ of } K_{ij}/s_j.$$
Scaling a replicate's normalised mean back up by its own $s_j$ recovers the expected count for that
replicate — and the key modelling choice is what happens to the **variance**: DESeq takes it to be
the mean plus a further function of the mean,
$$\operatorname{Var} = \text{mean} + v_p(\text{mean}),$$
i.e. a **negative binomial** model rather than a Poisson one. A Poisson model has variance equal to
the mean, with a single free parameter $\lambda$; as already seen when discussing library
complexity, real count data is over-dispersed relative to Poisson, so DESeq instead fits the
function $v_p$ describing how variance grows with the mean directly from the data (the fitted curve
sits above the Poisson line on a mean-variance plot). EdgeR, an alternative tool, does not fit this
relationship from the data and instead uses a fixed estimate, which the lecture characterised as
less accurate.

**The test.** $H_0$: the gene is expressed identically (same mean and the fitted variance) in both
conditions, pooled. $H_1$: the two conditions have separate means (and correspondingly separate
variances, via $v_p$). Compute the likelihood-ratio statistic between the negative-binomial fits
under $H_0$ and $H_1$ and read a p-value off the chi-squared distribution at the appropriate
degrees-of-freedom difference, exactly as above. Because many genes are tested at once, the
resulting p-values are corrected for multiple testing with the Benjamini–Hochberg procedure (used
earlier in the course). On a plot of log2 fold-change versus mean expression, the genes called
significant after this correction need a *smaller* fold-change to reach significance as the mean
increases — more observations per gene give more statistical power, so a smaller true difference is
enough to be distinguishable from noise.

## The hypergeometric test: is an overlap more than chance?

A different, common question: given a universe of $N$ genes, a set $A$ of $n_1$ genes (say, genes
called differentially expressed) and a set $B$ of $n_2$ genes with some independently known
annotation (say, stress-response genes), is the observed overlap between $A$ and $B$ larger than
would be expected if the two sets were unrelated?

<figure>
<svg viewBox="0 0 320 190" role="img" aria-label="Two overlapping gene sets inside a universe of genes">
  <rect x="20" y="20" width="280" height="150" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="30" y="35" font-size="12" fill="currentColor">N = 1000 genes</text>
  <ellipse cx="130" cy="105" rx="80" ry="55" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <ellipse cx="190" cy="105" rx="80" ry="55" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="90" y="105" text-anchor="middle" font-size="12" fill="currentColor">A (20)</text>
  <text x="230" y="105" text-anchor="middle" font-size="12" fill="currentColor">B (30)</text>
  <text x="160" y="105" text-anchor="middle" font-size="12" fill="currentColor">k = 3</text>
</svg>
<figcaption>Overlap of size $k$ between a set $A$ of 20 genes and a set $B$ of 30 genes, inside a
universe of 1,000 genes.</figcaption>
</figure>

The number of ways to choose $B$ with no constraint is $\binom{N}{n_2}$. The number of ways to
choose $B$ such that it overlaps $A$ in exactly $k$ elements is the number of ways to choose those
$k$ elements from $A$, $\binom{n_1}{k}$, times the number of ways to choose the remaining $n_2 - k$
elements of $B$ from the genes outside $A$, $\binom{N - n_1}{n_2 - k}$. So
$$P(\text{overlap} = k) = \frac{\binom{n_1}{k}\binom{N-n_1}{n_2-k}}{\binom{N}{n_2}}.$$
As usual the relevant question is not the probability of exactly the observed overlap but of an
overlap at least that large, $P(\text{overlap} \ge k)$, summed over all $k' \ge k$, since a still
larger overlap would be even more surprising under the null. In the worked numbers above
($N = 1000$, $n_1 = 20$, $n_2 = 30$, $k = 3$), $P(\text{overlap} = 3) = 0.017$ and
$P(\text{overlap} \ge 3) = 0.02$ — a two-in-a-hundred chance of that much overlap arising at random,
read as a significant enrichment.

## Multivariate Gaussians, and principal component analysis

PCA is used to reveal hidden structure in expression data and to reduce its dimensionality, and the
cleanest route to it is through a particular way of building a multivariate Gaussian, rather than
writing down its density directly.

Start from a vector $z$ of independent, standard univariate Gaussians (mean 0, variance 1), of
whatever length $n$ you like. Build a multivariate Gaussian $x$ by an affine transformation,
$$x = Az + \mu,$$
where $A$ is an $n \times n$ matrix and $\mu$ an $n$-vector. The matrix $A$ mixes the independent
univariate Gaussians together, and the resulting covariance matrix of $x$ is
$$\Sigma = AA^{T}.$$
So if $A$ were known, $\Sigma$ would follow immediately; in practice $\Sigma$ is instead estimated
from the data as a sample average, $\Sigma = E\big[(x-\mu)(x-\mu)^{T}\big]$.

For any unit vector $v$ (direction), the variance of $x$ projected onto that direction is
$$\operatorname{Var}(v^{T}x) = v^{T}\Sigma v$$
(the short derivation was on the board and not transcribed, but the identity itself is standard and
is what the rest of the argument rests on). PCA asks: in which direction(s) is this variance
largest? That is, find unit vectors $v_i$ maximising $v_i^{T}\Sigma v_i$ subject to
$v_i^{T}v_i = 1$. The vectors solving this are exactly the **eigenvectors** of $\Sigma$,
$$\Sigma v_i = \lambda_i v_i,$$
and left-multiplying by $v_i^{T}$ and using $v_i^{T}v_i = 1$ gives $v_i^{T}\Sigma v_i = \lambda_i$:
the eigenvalue $\lambda_i$ **is** the variance of the data in the direction of its eigenvector
$v_i$. These eigenvectors are the **principal components**.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="An elliptical Gaussian density with its two principal axes">
  <g transform="translate(160,110) rotate(-25)">
    <ellipse cx="0" cy="0" rx="110" ry="50" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
    <line x1="-110" y1="0" x2="110" y2="0" stroke="currentColor" stroke-width="1.5"/>
    <line x1="0" y1="-50" x2="0" y2="50" stroke="currentColor" stroke-width="1.5"/>
    <text x="100" y="-8" font-size="12" fill="currentColor">$v_1$</text>
    <text x="8" y="-55" font-size="12" fill="currentColor">$v_2$</text>
  </g>
</svg>
<figcaption>A bivariate Gaussian's density contour is an ellipse whose axes are the eigenvectors of
$\Sigma$; the axis lengths are set by the eigenvalues, the variances in those directions.</figcaption>
</figure>

To actually find the eigenvectors and eigenvalues, compute $\Sigma$ from the data and take its
singular value decomposition $\Sigma = USU^{T}$, where $S$ is diagonal with the eigenvalues on the
diagonal and the columns of $U$ are the corresponding eigenvectors. Since $\Sigma = AA^{T}$ as well,
this gives
$$x = US^{1/2}z + \mu:$$
building a multivariate Gaussian is nothing more than taking independent univariate Gaussians,
*scaling* them (by the square roots of the eigenvalues) and *rotating* them (by $U$), then shifting
by the mean. The eigenvectors are the directions of this rotation and the eigenvalues say how much
variance sits in each one. Having found them, data is organised, or its dimensionality reduced, by
projecting each observation onto the leading principal components.

## Single-cell RNA-seq

Everything above is normally applied to RNA pooled from thousands or millions of cells; the
lecture's closing topic is what happens when single cells are profiled individually, made possible
by microfluidic devices such as the Fluidigm C1 chip, which isolates 96 cells into independent
reaction wells and delivers reagents to each well to build an RNA-seq library from that one cell.

The motivating question, from an early single-cell study discussed in the lecture: take two
10,000-cell aliquots of the same culture, profile each independently as a bulk sample, and compare
gene expression between them — a very high correlation is expected and observed ($r = 0.98$), since
averaging over 10,000 cells washes out any cell-to-cell variation. Now take individual cells from
that same culture and compare two of them to each other: if cells were all alike, the comparison
should again look like the bulk-versus-bulk plot. It does not — the correlation drops to $r = 0.54$,
with some genes detected in one cell and not the other. Single cells disagree with each other far
more than bulk replicates do, which is direct evidence that the bulk average is hiding real,
substantial heterogeneity between individual cells.

That heterogeneity goes beyond which genes are on: the same study found that individual cells
could differ in *which isoform* of a gene was expressed, for some genes — a distinction invisible
in the bulk average — and this was cross-checked against fluorescence in-situ hybridisation
(counting individual RNA molecules by microscopy), which agreed with the sequencing-based isoform
calls.

Treating each cell's full expression profile as a vector, the study then ran PCA on the population
of single cells and projected them onto the first two principal components. This separated the
cells (derived from bone marrow and stimulated with lipopolysaccharide to provoke an immune
response) into distinct groups along the first principal component — cells expressing certain
surface proteins (read as more mature) separating from cells expressing certain cytokines (read as
less mature, still maturing). A single linear projection was enough to recover at least two
distinct cell states in a population that looked uniform in bulk.

Finally, correlating gene pairs across individual cells was used to propose a regulatory circuit:
genes that are reliably co-expressed cell by cell are hypothesised to belong to one circuit. In the
example discussed, an interferon-regulatory gene (transcribed in the lecture captions as "LRF7")
together with IFIT1 and STAT2 were hypothesised to form part of an anti-viral response circuit,
downstream of the interferon receptor. Knocking out the regulatory gene partially reduced
expression of the other circuit members; knocking out the upstream interferon receptor largely
abolished expression of the whole cluster — consistent with the hypothesised circuit structure.

The lecture closed on a practical point connecting back to library complexity (covered earlier in
the course): data quality matters per cell. As a cell's library complexity increases, the
coefficient of variation of its expression estimates (standard deviation over mean) falls and mean
expression rises; cells independently flagged as poor quality by microscopy during the Fluidigm
processing step were the ones with low library complexity.

## Sources

All material in this chapter is from the transcript of MIT 7.91J Spring 2014, Lecture 8
(`recordings/lectures/08.md`), David Gifford lecturing; no slide deck was available for this
lecture, so figures described from the board or screen (the SOX2 and SMUG1 read pileups, the
exon-inclusion/exclusion diagram, the mean–variance DESeq plot, the Benjamini–Hochberg significance
plot, the single-cell scatter and PCA panels) are described from what the transcript says about
them, not reproduced, except for the junction-reads, overlap, and Gaussian-ellipse diagrams above,
which are redrawn here from the verbal description because the picture is part of the argument.

- RNA-seq principles, poly-A selection, splicing and isoforms, RPKM/FPKM — 00:00–09:05.
- The generative read model (incompatible / single-end / paired-end cases) and mixture likelihood
  for isoform quantitation, with audience Q&A on 3′ bias and paired-end intuition — 09:05–22:45.
  Cufflinks myogenesis result — 23:04–25:10.
- Likelihood-ratio hypothesis testing digression — 29:25–38:30.
- DESeq normalisation, the negative-binomial mean–variance model, and the differential-expression
  test — 38:30–49:34.
- Hypergeometric test for set overlap — 50:34–55:57.
- Multivariate Gaussians and PCA, including audience questions on computing $\Sigma$ — 55:57–1:09:42.
- Single-cell RNA-seq, the Fluidigm C1 chip, the bulk-vs-single-cell correlation comparison,
  isoform heterogeneity, PCA on single cells, the antiviral co-expression circuit, and quality
  metrics via library complexity — 1:09:42–1:20:30 (end).
- The lecture refers to, but the transcript does not contain: a paper on isoform-prevalence
  estimation posted to the course's Stellar site (likely the Cufflinks paper, Trapnell et al.); the
  DESeq paper, posted on Stellar, which derives the fitted mean–variance function $v_p$; and the
  single-cell RNA-seq paper underlying the final section, named in neither the transcript nor
  recoverable from it. The board derivation of $\operatorname{Var}(v^Tx) = v^T\Sigma v$ and the
  algebra reducing the eigenvector condition to $v_i^T\Sigma v_i = \lambda_i$ were worked on the
  board and are not captured in the transcript; the clean final identities are given here in place
  of the (partly garbled in transcription) intermediate steps.

---

[← 7. ChIP-seq Peak Calling and IDR](07-chip-seq-peak-calling-and-idr.md) · [Contents](index.md) · [9. Sequence Motifs and the Gibbs Sampler →](09-sequence-motifs-and-the-gibbs-sampler.md)
