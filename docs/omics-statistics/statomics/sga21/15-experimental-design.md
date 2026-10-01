---
title: "15. Experimental design"
course: "StatOmics Sga21"
chapter: 15
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Experimental design

## What this covers

This chapter works through a real case study in designing a sequencing-based gene-expression
experiment, and in checking, from the data itself, whether the design delivered what it promised.
It follows the study that first put Illumina RNA sequencing (RNA-seq) head to head against
microarrays: the same RNA sequenced many times over, so that the amount of purely technical
variation between "replicate" measurements could be pinned down statistically before any claim
about biological differences was made. It assumes you know what a read count is and are
comfortable with the Poisson distribution, with $p$-values, and with a goodness-of-fit test; it
does not assume you have seen a sequencing lane, a sequencing run, or a hypergeometric test used
this way before.

## Why build technical replication into the design at all

Before trusting that two RNA samples differ in expression, you first need to know how much two
measurements of the *same* sample differ purely because of the machinery — a molecule ending up on
one part of the sequencer rather than another, with no biology involved at all. The study behind
this chapter sequenced the same RNA sample repeatedly while deliberately varying things that
should not matter biologically — which lane, which run of the machine, how much cDNA was loaded —
and then asked whether the resulting gene counts behaved exactly as pure sampling noise would
predict. Only once that question is answered can a difference between genuinely different samples
(here, liver versus kidney) be trusted as biology rather than as one sample happening to land in a
noisier lane. The same design also made it possible to compare sequencing directly against the
incumbent technology, microarrays, on identical starting material.

## The design: one individual, two tissues, two platforms, two knobs

Total RNA was extracted from liver and kidney of a single human male, the poly(A) mRNA purified
and sheared, and a cDNA library built from it for sequencing on an Illumina Genome Analyzer. Each
of the two tissue samples was sequenced seven times, and those seven lanes were split across two
separate runs of the machine — which is what lets the analysis later separate lane-to-lane
variation within a run from run-to-run variation. On top of that, each sample was sequenced at two
different cDNA concentrations, 3 pM (five lanes) and 1.5 pM (two lanes), which is what lets the
analysis ask whether concentration itself behaves like a real experimental factor or like more
noise.

<figure>
<svg viewBox="0 0 420 170" role="img" aria-label="Diagram of the two sequencing runs, each split into eight lanes, showing the control lane in each run and which lanes were sequenced at the lower cDNA concentration">
  <text x="210" y="16" text-anchor="middle" font-size="12" fill="currentColor">Run 1</text>
  <rect x="20" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="40" y="50" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <rect x="64" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="84" y="50" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <rect x="108" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="128" y="50" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <rect x="152" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="172" y="50" text-anchor="middle" font-size="12" fill="currentColor">4</text>
  <rect x="196" y="26" width="40" height="40" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="216" y="50" text-anchor="middle" font-size="12" fill="currentColor">5</text>
  <rect x="240" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="260" y="50" text-anchor="middle" font-size="12" fill="currentColor">6</text>
  <rect x="284" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="304" y="50" text-anchor="middle" font-size="12" fill="currentColor">7</text>
  <rect x="328" y="26" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="348" y="50" text-anchor="middle" font-size="12" fill="currentColor">8</text>

  <text x="210" y="96" text-anchor="middle" font-size="12" fill="currentColor">Run 2</text>
  <rect x="20" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="40" y="130" text-anchor="middle" font-size="12" fill="currentColor">1*</text>
  <rect x="64" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="84" y="130" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <rect x="108" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="128" y="130" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <rect x="152" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="172" y="130" text-anchor="middle" font-size="12" fill="currentColor">4*</text>
  <rect x="196" y="106" width="40" height="40" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="216" y="130" text-anchor="middle" font-size="12" fill="currentColor">5</text>
  <rect x="240" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="260" y="130" text-anchor="middle" font-size="12" fill="currentColor">6</text>
  <rect x="284" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="304" y="130" text-anchor="middle" font-size="12" fill="currentColor">7*</text>
  <rect x="328" y="106" width="40" height="40" fill="none" stroke="currentColor"/>
  <text x="348" y="130" text-anchor="middle" font-size="12" fill="currentColor">8*</text>

  <text x="210" y="163" text-anchor="middle" font-size="11" fill="currentColor">shaded lane = control sample; * = sequenced at 1.5 pM (unmarked lanes: 3 pM)</text>
</svg>
<figcaption>Each of the two runs had eight lanes; lane 5 (shaded) carried a control sample in both
runs, leaving seven lanes per run for the liver and kidney samples. All seven sample lanes of Run 1
and three of Run 2 were sequenced at 3 pM; the remaining four lanes of Run 2 (marked *) were
sequenced at 1.5 pM, giving two lanes per tissue at each concentration overall. Which lane held
liver and which held kidney is colour-coded in the original figure (linked below) and not
reproduced here.</figcaption>
</figure>

The same two RNA samples were also hybridised to Affymetrix U133 Plus 2 microarrays, three
technical replicate arrays per sample, with the array sample preparation and analysis kept as
close as possible to the sequencing side. To make the two platforms comparable gene-for-gene, the
array probe sets were mapped onto Ensembl (v.48) gene annotation: 70% of probe sets mapped to a
gene, and after removing probe sets mapping to more than one gene, or not mapping uniquely, 17,708
probe sets were left, mapping one-to-one onto 17,708 genes — the common yardstick both platforms
were measured against.

## Turning reads into a gene count

Each lane produced many millions of short (32 bp) reads — 12.9–14.7 million per lane at 3 pM,
8.4–9.3 million per lane at 1.5 pM. Reads were aligned to the whole genome with ELAND, allowing up
to two mismatches, and any read that aligned equally well to more than one genomic location was
discarded rather than guessed at. Of all reads, 40% mapped uniquely; of those, 65% mapped to
autosomal or sex chromosomes (nearly all the rest were mitochondrial). Non-unique mapping can come
from sequencing errors or polymorphisms, from repetitive sequence, or from reads that straddle an
exon–exon junction and so match no single genomic stretch.

Among uniquely mapped reads, 83% fell in annotated genic regions, and of those, 68% fell inside an
annotated exon. Reads landing outside any annotated gene tended to cluster near one — except for a
sizeable minority (10.6%) that mapped more than 100 kb from any known gene, hinting that the
annotation itself is missing some transcriptionally active regions. That is a data-quality
observation rather than a design one, but it matters for the same reason as everything else here:
before treating a gene's count as a measurement of that gene, you have to know what fraction of the
raw material behind it is actually attributable to that gene.

The gene count itself is built by summing, within each lane, all the reads that fall in a gene's
exons (taking the median across annotated transcripts when a gene has more than one). Under an
idealised, error-free and bias-free reading of the process, this count is, in expectation,
proportional to transcript length times expression level. Of the genes in the Ensembl annotation,
22,925 (72%) received at least one read, and the count distribution across genes was highly skewed,
with typical (median) values of 46 reads for liver and 101 for kidney. A first, rough check that
the numbers behave consistently is that gene counts correlated strongly across lanes of the same
sample (average Spearman correlation 0.96).

## Is there a "lane effect"? Two ways to test it

Correlation across lanes is reassuring but coarse. The sharper question is whether there is a
*lane effect* — a systematic difference between counts for the same sample sequenced at the same
concentration in different lanes, over and above what sampling error alone would produce. Two
complementary tests were used: comparing lanes two at a time, which is good at spotting one
outlying lane, and comparing several lanes of the same sample simultaneously, which has more power
to detect an effect that consistently nudges the same genes.

### Pairwise: a hypergeometric test

Take two lanes that sequenced the same sample at the same concentration, and pool their reads for a
given gene. If there truly is no lane effect, then which of the two lanes any individual read of
that gene landed in is, after accounting for the two lanes' different total depths, no more than a
random split of that pooled total between them — exactly what a hypergeometric distribution
describes: drawing without replacement from a finite pool made up of "lane 1 reads" and "lane 2
reads". Testing that hypothesis for each gene produces a $p$-value, and under the null those
$p$-values should be uniformly distributed across genes. A qq-plot of the observed $p$-values
against the uniform distribution — the standard way to see whether too many values are surprisingly
small — reveals a lane effect as a bulge of points above the line $y=x$.

Across the 22 pairwise comparisons between lanes carrying the same sample at the same
concentration, consistently fewer than 0.5% of genes showed a $p$-value small enough to signal a
real lane effect, both within a single run and across the two runs — though cross-run comparisons
showed a slightly larger proportion of small $p$-values, a hint (not conclusive from a single
experiment) of a small run-to-run component. By sharp contrast, comparing the same sample sequenced
at *different* concentrations gave $p$-values that deviated from uniformity far more strongly.

![Figure 2. qq-plots testing for a lane effect: (A) two lanes at the same concentration; (B) two lanes at different concentrations; (C, D) the multi-lane goodness-of-fit statistic against a chi-squared distribution on 4 degrees of freedom, on two different scales.](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/images_sequencing/figure2.png)

### Simultaneously: a Poisson model across several lanes

The multi-lane version of the same idea starts from an explicit model. Let $x_{ijk}$ be the number
of reads mapping to gene $j$, in lane $k$ of sample $i$. Model each $x_{ijk}$ as an independent
Poisson random variable,

$$x_{ijk} \sim \mathrm{Poisson}(\mu_{ijk}), \qquad \mu_{ijk} = c_{ik}\,\lambda_{ijk}, \qquad \sum_j \lambda_{ijk} = 1 \ \text{(for fixed } i,k\text{)}.$$

*(The notes this chapter is drawn from are a model's reconstruction of a scanned page with no text
layer, so treat this equation as a guide to the argument, not as a citable formula.)*

Here $c_{ik}$ is the overall rate at which lane $k$ of sample $i$ produces reads — its sequencing
depth — and $\lambda_{ijk}$ is the share of that lane's reads attributable to gene $j$, i.e., gene
$j$'s relative expression on that particular lane. "No lane effect" means exactly that this relative
share does not depend on which lane $k$ you look at: $\lambda_{ijk}$ is the same for every lane of a
given sample. For each gene, a goodness-of-fit statistic is computed across the $L$ lanes of a
sample, testing that constancy; under the null it should follow a $\chi^2$ distribution on $L-1$
degrees of freedom (one degree of freedom is spent estimating the common relative-expression level,
leaving $L-1$ free to disagree with it if something real is going on). In the actual figure, this
statistic is plotted against a $\chi^2$ distribution on 4 degrees of freedom — that is, $L=5$, the
five lanes of one sample sequenced at 3 pM. A qq-plot of the statistics against that theoretical
distribution again showed only about 0.5% of genes with strong evidence of "extra-Poisson"
variation, for both the liver and kidney samples.

## Why the pattern of results is the point

The two tests — one comparing pairs of lanes with a hypergeometric argument, one comparing several
lanes at once with a Poisson model — agree closely: only a small fraction of genes (around 0.5%)
show any sign of a real lane effect. That is what makes the design a success: lanes carrying the
same sample at the same concentration behave, for the overwhelming majority of genes, exactly as if
counts were nothing but Poisson sampling noise around a fixed relative-expression profile. That
licenses pooling same-concentration lanes as if they were interchangeable Poisson replicates, and,
more importantly, reusing the same Poisson model as the *null* against which a real biological
difference — liver versus kidney, rather than lane versus lane — is then judged. Using that
approach, the sequencing data identified 30% more differentially expressed genes than a standard
analysis of the array data found at the same false discovery rate, and the same reasoning was
reported to extend to detecting alternatively spliced forms from the sequence data — though neither
the differential-expression analysis nor the splicing analysis is worked through in the material
this chapter draws on.

Concentration is the counter-example that sharpens the point: it is "technical" in exactly the same
sense that a lane or a run is, yet it produced far larger, systematic differences than either. The
design was built specifically to be able to tell the two apart — and having told them apart, the
lesson generalises beyond this one study: not every knob you can turn between "replicates" is safe
to ignore. Some behave like noise and can be pooled over; others behave like a real experimental
factor and have to be measured, controlled for, or modelled explicitly — and the only way to know
which is which is to build both possibilities into the design and check.

## Sources

- Built from the two reconstructed notes pages converted from
  `images_sequencing/marioniFigs_cropped.pdf` in the `statomics-sga21` course materials:
  - `docs/omics-statistics/statomics/sga21/images_sequencing/marioniFigs_cropped/01-experimental-design.md`
  - `docs/omics-statistics/statomics/sga21/images_sequencing/marioniFigs_cropped/02-illumina-sequencing-data-processing.md`
- No slide deck, lecture transcript, or problem set accompanied this material for this session —
  the chapter follows these two notes pages directly, including the figures embedded in them
  (Figure 1, the study design; Figure 2, the lane-effect qq-plots).
- The design diagram above, and the "$L=5$, $\chi^2$ on 4 degrees of freedom" detail, were checked
  directly against the extracted page images alongside the notes:
  `docs/omics-statistics/statomics/sga21/images_sequencing/marioniFigs_cropped/figures/p001-2.jpeg`
  (Figure 1) and `.../figures/p001-1.jpeg` (Figure 2), including the caption already present in
  the notes ("the control sample was sequenced in lane 5 ... 1.5 pM indicated by an asterisk").
- Those notes are themselves a model's reconstruction of a PDF with no text layer ("fidelity:
  reconstructed"), licensed CC BY-NC-SA 4.0; the notes' own header flags the prose as paraphrased
  in places and every equation as unverified, a caveat carried through to the Poisson model above.
- The source filename, `marioniFigs_cropped.pdf`, indicates the figures come from a paper by an
  author named Marioni; neither the paper's full citation nor its "Methods" section (referred to
  repeatedly for sample-preparation and analysis detail) was supplied.
- Referred to but not supplied: Supplemental Tables 1–2 and Supplemental Figures 1–6 of the
  underlying paper, the full probe-to-gene mapping procedure, and the differential-expression and
  alternative-splicing analyses mentioned only in summary.

---

[← 14. Detecting Lane Effects in RNA-seq](14-detecting-lane-effects-in-rna-seq.md) · [Contents](index.md) · [16. Mass Spectrometry Basics for Proteomics →](16-mass-spectrometry-basics-for-proteomics.md)
