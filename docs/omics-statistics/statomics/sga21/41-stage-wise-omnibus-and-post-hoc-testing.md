---
title: "41. Stage-wise Omnibus and Post-hoc Testing"
course: "StatOmics Sga21"
chapter: 41
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 41. Stage-wise Omnibus and Post-hoc Testing

## What this covers

Modern high-throughput experiments routinely put more than one hypothesis on the same gene or
protein: one hypothesis per transcript in a transcript-level RNA-seq analysis, one per timepoint
plus an interaction in a time-course design, one per cell type in a single-cell experiment. This
chapter answers what goes wrong if you test each of those hypotheses separately and control the
false discovery rate (FDR) on the pooled list of p-values, and what a **stage-wise testing**
procedure — screen each gene with one omnibus test, then confirm within the genes that pass — does
to fix it. It assumes the reader already knows what a p-value and an FDR are, and how the
Benjamini–Hochberg (BH) procedure turns a ranked list of p-values into a set of rejections at a
target FDR level $\alpha$.

## Why one gene now carries many hypotheses

Falling sequencing cost and rising throughput have pushed experiments toward increasingly complex
designs, and complex designs generate more than one question per feature. A proteomics example
from the lecture: is a protein differentially abundant between different regions of the heart, and
does that pattern of differential abundance change from left to right — two hypotheses, to be
assessed for thousands of proteins at once.

RNA-seq adds a second source of multiplicity: transcript-level analysis. State-of-the-art
quantification tools (the lecture cites the "near-optimal RNA-seq quantification" line of work and
Salmon, published in *Nature Methods*) can now assign reads to individual transcripts rather than
just genes, cheaply and at scale — in human, more than 38,000 genes and more than 173,000
transcripts. Because a single gene routinely produces several transcript isoforms through
alternative splicing, this immediately means several hypotheses per gene: is transcript $i$
differentially **expressed** (DTE, differential transcript expression — expression of one isoform
compared between conditions), and, at the gene level, is the isoform usage itself different between
conditions (DTU, differential transcript usage — the relative proportions of a gene's isoforms).
DTU and DTE have been linked to Parkinson's disease and to resistance to prostate-cancer treatment
in work the lecture cites but does not walk through.

Single-cell RNA-seq adds a third source. In the example from Kang et al. (2018), peripheral blood
mononuclear cells from 8 individuals, stimulated versus control, were profiled (more than 29,000
cells, across two channels of a 10x Genomics chip and two HiSeq lanes, with individuals
demultiplexed from SNPs) and annotated into six cell types (NK cells, FCGR3A+ monocytes, CD8 T
cells, CD4 T cells, CD14+ monocytes, B cells). Per gene, that gives two families of hypotheses at
once: is the gene differentially expressed between stimulated and control *within* each cell type
(six tests per gene), and does the *size* of the stimulus effect itself differ between cell types
(one test per pair of cell types, $\binom{6}{2}=15$ tests per gene).

In every one of these settings, the conventional strategy is: assess each hypothesis separately,
control FDR at level $\alpha$ on each contrast's list, and hand the biologist a top-gene list per
contrast. The rest of the chapter is about why that strategy is the wrong one once there is more
than one hypothesis per gene, and where the fix comes from.

## Where testing each hypothesis separately breaks down

### It is underpowered for the hardest hypothesis

In a factorial RNA-seq design — condition, timepoint, and their interaction — the interaction
effect's standard error is typically much larger than a main effect's, so the interaction test is
intrinsically the weakest of the three. The lecture's illustration, from the cross-sectional
time-course study of Hammer et al. (2010) analysed with limma-voom: testing for a treatment effect
within a single timepoint flags more than 6000 genes at 5% FDR, while testing the treatment-by-time
interaction on the same data returns **no** significant genes at the same FDR level. Higher
resolution — a separate hypothesis for the interaction — is bought at the price of essentially no
power to detect it.

### It does not control FDR at the level anyone actually uses

Downstream biological interpretation and validation happen at the gene level — a biologist follows
up a *gene*, not a contrast — so gene-level FDR is the quantity that matters, and controlling FDR
hypothesis-by-hypothesis does not control it. The mechanism, as the lecture's source spells out
with a small worked case: suppose three hypotheses are each tested and controlled at 5% FDR, so
each contrast's own top-list is 5% false positives. The false positives in different contrasts
tend to sit on *different* genes. So the number of *genes* that have a false positive in at least
one of their contrasts grows with the number of hypotheses tested per gene, even though each
contrast is individually well calibrated and the total number of genes stays fixed. Taking the
union of "significant in at least one contrast" as the gene-level shortlist — which is what a
biologist naturally does — therefore inflates the gene-level FDR above the nominal $\alpha$, and
the inflation gets worse the more hypotheses each gene carries.

### Naively aggregating fixes the FDR but throws away the resolution

A first fix suggests itself: instead of testing each of a gene's hypotheses separately, aggregate
the evidence across them into a single p-value per gene (an omnibus test), and run BH on that one
list. This does control FDR at the gene level, and — because aggregated tests pool more data and
test an easier-to-reject null than any one individual hypothesis — it is also more sensitive: this
is the effect behind the gap between the gene-level and transcript-level curves in simulation
studies of DTU analysis (Soneson et al., cited in the lecture), where aggregating all of a gene's
transcript-level evidence gives a materially higher true positive rate at a given false discovery
proportion than testing every transcript on its own. But the aggregated test answers only "is
*something* going on in this gene" — it cannot say *which* transcript, *which* timepoint, or *which*
cell-type comparison drove the significance. Higher sensitivity is bought at the cost of losing the
biological resolution the individual hypotheses were there to provide.

## The stage-wise testing procedure

The fix keeps both properties by splitting the analysis into two stages that talk to each other
through a single number, $R$: aggregate first to screen, then only re-open the individual
hypotheses for genes that passed screening, at a significance level corrected for having screened.
This is the two-stage procedure of Heller et al. (2009), applied here to high-throughput data.

<figure>
<svg viewBox="0 0 480 260" role="img" aria-label="Flow diagram of stage-wise testing: a gene's hypotheses are combined into one screening test, and only genes that pass are opened back up for individual confirmation tests">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <text x="110" y="24" text-anchor="middle" font-size="12" fill="currentColor">H_g1</text>
  <text x="240" y="24" text-anchor="middle" font-size="12" fill="currentColor">...</text>
  <text x="370" y="24" text-anchor="middle" font-size="12" fill="currentColor">H_gng</text>

  <line x1="110" y1="32" x2="220" y2="66" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <line x1="240" y1="32" x2="240" y2="66" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <line x1="370" y1="32" x2="260" y2="66" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>

  <rect x="130" y="68" width="220" height="42" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.3"/>
  <text x="240" y="94" text-anchor="middle" font-size="12" fill="currentColor">Screening: omnibus test per gene</text>

  <line x1="240" y1="110" x2="240" y2="146" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="255" y="130" text-anchor="start" font-size="11" fill="currentColor">BH at level &#945; over G genes &#8594; R rejected</text>

  <rect x="130" y="148" width="220" height="42" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.3"/>
  <text x="240" y="174" text-anchor="middle" font-size="12" fill="currentColor">Confirmation: only the R genes</text>

  <line x1="220" y1="190" x2="110" y2="224" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <line x1="240" y1="190" x2="240" y2="224" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <line x1="260" y1="190" x2="370" y2="224" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>

  <text x="110" y="238" text-anchor="middle" font-size="12" fill="currentColor">H_g1</text>
  <text x="240" y="238" text-anchor="middle" font-size="12" fill="currentColor">...</text>
  <text x="370" y="238" text-anchor="middle" font-size="12" fill="currentColor">H_gng</text>
  <text x="240" y="256" text-anchor="middle" font-size="11" fill="currentColor">each tested at level &#945;_II = R&#945;/G</text>
</svg>
<figcaption>A gene's individual hypotheses are aggregated into one screening test; only the genes
that clear the screening FDR threshold are opened back up, and their individual hypotheses are
tested at a level corrected for the screening stage.</figcaption>
</figure>

Concretely, for a set of genes $G$ where gene $g$ carries $n_g$ individual null hypotheses:

1. **Screening stage.** For every gene $g \in G$, assess a screening (global) null hypothesis
   $H_g^S$ — that none of gene $g$'s $n_g$ individual hypotheses is false — using an omnibus test
   such as a global $F$-test, a global likelihood-ratio test, or an aggregate of the $n_g$
   individual p-values. Apply BH at FDR level $\alpha$ to the resulting $|G|$ screening p-values.
   Let $R$ be the number of genes whose screening hypothesis is rejected.
2. **Confirmation stage.** For each of those $R$ genes, take
   $$\alpha_{II} = \frac{R\alpha}{|G|}$$
   as the FDR-adjusted significance level carried over from the screening stage, and use a multiple
   testing procedure that controls the within-gene error rate at level $\alpha_{II}$ while now
   assessing the gene's $n_g$ individual hypotheses separately.

The screening stage is exactly the aggregated test from the previous section, so it inherits its
sensitivity; it is what earns a gene the right to have its individual hypotheses looked at at all.
The confirmation stage is what restores the resolution, and doing it at $\alpha_{II}$ rather than at
$\alpha$ is what keeps the whole two-stage procedure's gene-level FDR controlled at (about) $\alpha$
overall, rather than inflating in the way the naive per-hypothesis approach does.

## What the two-stage procedure buys, in the two motivating cases

**Complex-design differential expression.** Applied to a design with main effects and an
interaction (the Hammer et al. setting above), the screening stage's omnibus test pools evidence
across all of a gene's hypotheses, so a gene with a genuine interaction effect is more likely to
clear screening than it would be judged on the interaction test alone. This enriches the
confirmation stage for genes with real interaction effects and so boosts power specifically for
that hard-to-detect hypothesis, while leaving power for the two main effects essentially unchanged
— and, unlike the naive per-hypothesis approach, the procedure correctly controls the FDR at the
gene level.

**Transcript-level (DTU) analysis.** Applied with the omnibus screening test aggregating
transcript-level evidence per gene, followed by confirmation of the individual transcripts within
genes that pass, the two-stage procedure was shown (in simulations based on the Drosophila and
human transcriptomes) to reach power at the transcript level that is equal to or better than testing
transcripts individually, together with better FDR control — it sits on top of, rather than between,
the gene-level and transcript-level curves, because it combines the sensitivity of the gene-level
aggregate test with the biological resolution of the transcript-level tests.

This is the method the lecture's source paper — Van den Berge, Soneson, Robinson and Clement,
*Genome Biology* (2017) 18:151 — names **stageR**: "a two-stage testing paradigm that leverages the
increased power of aggregated gene-level tests and allows post hoc assessment for significant
genes," providing gene-level FDR control, boosting power for interaction effects, and giving a
transcript-level analysis that keeps its biological resolution. The paper situates this within an
existing line of stage-wise testing work that the lecture names without developing: Lu et al.
proposed an earlier two-stage strategy for microarrays based on mixed models, which does not carry
over to sequencing data because of the different distributional assumptions; Jiang and Doerge
proposed a generic two-stage differential-expression procedure whose first stage tests whether *at
least one* hypothesis is false, with post hoc tests only for the genes that pass — the same
screen-then-confirm shape, of which the procedure above (with its explicit $\alpha_{II}=R\alpha/|G|$
correction) is a refinement. The single-cell example above (six within-cell-type tests and fifteen
across-cell-type tests per gene) is presented in the lecture only as a further illustration of how
many hypotheses one gene can carry in current experiments; the lecture does not carry a worked
stage-wise analysis of that dataset through to a result.

## Sources

- Slide deck *Omnibus testing and post-hoc tests for high throughput experiments* (statOmics
  SGA21, Lieven Clement), converted pages `01-omnibus-testing-and-post-hoc-tests-for-high-throughput-exper.md`,
  `02-power-issue-transcript-level-analysis.md` and `03-stagewisetesting-part-03.md`. The source
  PDF has no extractable text layer; the conversion is a model reconstruction, and its own header
  flags the prose as a paraphrase in places and every displayed equation as unverified — this
  applies in particular to $\alpha_{II} = R\alpha/|G|$ and to the numeric claims (gene/transcript
  counts, cell counts, TPR/FDR figures) reproduced above.
- The opening motivation (throughput and cost trends, the heart-proteomics example, RNA-seq
  quantification tools, single-cell 10x/Kang et al. example) is from file 1 and the first half of
  file 2.
- The core argument — power loss for interaction effects, gene-level FDR inflation under
  per-hypothesis control, the naive aggregation trade-off, the two-stage screening/confirmation
  procedure and its results — reproduces the Background section of Van den Berge, Soneson, Robinson
  and Clement, *Genome Biology* (2017) 18:151 ("stageR: a general stage-wise method for controlling
  the gene-level false discovery rate in differential expression and differential transcript usage"),
  embedded in files 2 and 3 of the slide conversion; the two-stage procedure itself is attributed by
  the slides to Heller et al. (2009, *Bioinformatics*).
- Named but not developed in the lecture material: the Soneson et al. (2016) Drosophila/human
  DTU simulation studies behind Fig. 1's performance curves; the DEXSeq method; the Hammer et al.
  (2010, *Genome Research*) dataset and its limma-voom analysis; Lu et al.'s microarray two-stage
  method; Jiang and Doerge's generic two-stage procedure; the Parkinson's-disease and
  prostate-cancer DTU/DTE studies; Kang et al. (2018, *Nat. Biotechnol.* 36(1):89–94) and Zheng et
  al. (2017, *Nat. Commun.*) single-cell studies. None of these is worked through in the supplied
  material beyond the citation.
- No transcript or problem set was supplied for this lecture.

---

[← 40. Proteomics Software Setup](40-proteomics-software-setup.md) · [Contents](index.md) · [42. Testing for Differential Protein Abundance →](42-testing-for-differential-protein-abundance.md)
