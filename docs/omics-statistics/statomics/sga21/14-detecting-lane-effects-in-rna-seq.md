---
title: "14. Detecting Lane Effects in RNA-seq"
course: "StatOmics Sga21"
chapter: 14
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Detecting Lane Effects in RNA-seq

## What this covers

This chapter works through a single worked example, taken from Marioni et al.'s study of the
technical reproducibility of RNA-seq: how do you tell, from read counts alone, whether two
sequencing lanes running the same sample disagree by more than pure sampling noise would explain?
That disagreement is called a **lane effect**, and the chapter covers the two ways the study tested
for it — a per-gene test comparing one pair of lanes, and a per-gene test comparing several lanes
at once — and how a qq-plot is used to read the result. It assumes the Poisson distribution, the
idea of a $p$-value and its null distribution, and a qq-plot as a way of comparing an empirical
distribution to a theoretical one; the chi-squared goodness-of-fit test is used but its degrees of
freedom are argued for rather than assumed.

## The gene counts being tested

For each sequencing lane, the study obtained an "overall" expression measure for every gene by
summing the reads mapping to that gene's exons (medianed across transcripts, for genes with more
than one). Under idealized assumptions — no alignment errors, no sequence-context bias — a gene's
count should, in expectation, be proportional to its transcript length times its mRNA expression
level. Of the genes in the Ensembl database, 22,925 (72%) were hit by at least one read, and the
distribution of read counts across genes was highly skewed: the median gene had only 46 reads in
liver and 101 in kidney. As a first, informal check that the data were reproducible at all, the
gene counts for a sample turned out to be highly correlated across lanes (average Spearman
correlation 0.96).

The question the rest of the chapter answers is more exacting than "highly correlated": is there
a *systematic* difference between lanes running the same sample at the same concentration, over
and above what sampling error on its own would produce? Two strategies are used. Comparing lanes
two at a time lets an unusually bad lane stand out on its own. Comparing several lanes at once
gains power to detect an effect that consistently hits the same genes, even if no single pair of
lanes looks obviously wrong.

## Testing one pair of lanes: a hypergeometric test

Take two lanes sequencing the same sample. For a given gene $j$, let $n_j$ be the total number of
reads mapping to gene $j$ pooled across both lanes, and let $N_1$ and $N_2$ be the lanes' overall
read totals (across all genes). If there is no lane effect, a read landing on gene $j$ is no more
or less likely to have come from lane 1 than any other read is — so the $n_j$ reads for gene $j$
behave like a random subset of the pooled $N_1 + N_2$ reads, split $N_1$ against $N_2$. The number
of them, $x_j$, that fall in lane 1 therefore follows a hypergeometric distribution: exactly the
logic behind Fisher's exact test on the $2\times2$ table of (gene $j$ vs. all other genes) by
(lane 1 vs. lane 2). That gives a $p$-value for each gene, testing the null hypothesis that the
gene's counts in the two lanes are consistent with this random split.

If there really is no lane effect, these $p$-values should be uniform on $[0,1]$ across genes.
A lane effect shows up as a departure from uniformity — specifically, more small $p$-values than
uniformity predicts, because some genes are systematically imbalanced between the two lanes.

## Reading a qq-plot of the $p$-values

The uniformity of the $p$-values is checked with a qq-plot, plotting $-\log$ of the observed
$p$-values against $-\log$ of what they would be under a uniform distribution. Points that fall on
the line $y=x$ are consistent with no lane effect; points that rise above the line — particularly
in the tail of very small $p$-values, which sits at the top right of the plot — say that gene has a
$p$-value more extreme than chance predicts, i.e. is a candidate for a genuine lane effect.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A qq-plot where points track the diagonal for most genes, then peel upward in the extreme tail">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="280" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <path d="M45,175 L70,160 L95,145 L120,130 L145,115 L165,102" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M165,102 L185,80 L205,55 L220,35 L232,22" fill="none" stroke="darkorange" stroke-width="2.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">theoretical quantile (uniform / no lane effect)</text>
  <text x="16" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 100)">observed quantile</text>
  <text x="150" y="45" font-size="11" fill="darkorange">a few genes peel away from y = x</text>
</svg>
<figcaption>The bulk of genes track the dashed diagonal, consistent with a uniform
$p$-value distribution and no lane effect; the handful that bend away in the upper-right tail are
the genes flagged as showing a lane effect. This is the shape used to read every panel of Marioni
et al.'s Figure 2.</figcaption>
</figure>

## Testing several lanes at once: a Poisson model

Comparing lanes pairwise cannot easily pool evidence across more than two lanes, so the study also
fit a model to all the lanes for a sample simultaneously. Let $x_{ijk}$ be the number of reads
mapped to gene $j$, in the $k$th lane of sample $i$. Model these as independent Poisson random
variables,
$$x_{ijk} \sim \text{Poisson}(\mu_{ijk}), \qquad \mu_{ijk} = c_{ik}\,\lambda_{ijk},$$
where $\lambda_{ijk}$ is constrained to sum to 1 across genes $j$ within a given lane. Here $c_{ik}$
is the overall rate at which lane $k$ of sample $i$ produces reads (its sequencing depth), and
$\lambda_{ijk}$ is the *relative* rate at which reads land on gene $j$ in that lane — the lane's
expression profile, stripped of its overall depth. A lane effect, in this language, is exactly
$\lambda_{ijk}$ changing with $k$: the same sample's relative expression profile drifting from lane
to lane. The null hypothesis of no lane effect is that $\lambda_{ijk}$ is constant across the $L$
lanes for a given sample, i.e. every lane is estimating the same underlying $\lambda_{ij}$ up to its
own depth $c_{ik}$.

For each gene, the study computed a goodness-of-fit statistic comparing the $L$ observed counts
against the counts a single shared rate $\lambda_{ij}$ would predict. This is the same construction
as any Pearson goodness-of-fit statistic — compare each lane's observed count to the count expected
under one common rate fitted from the pooled data — and it carries $L-1$ degrees of freedom for the
same reason a goodness-of-fit statistic over $L$ categories always loses one degree of freedom to a
fitted constraint: the $L$ expected counts are pegged to match the same total as the $L$ observed
counts once the single common rate is estimated. Under the null of no lane effect, the statistic is
therefore $\chi^2$ on $L-1$ degrees of freedom, and a qq-plot of these per-gene statistics against
$\chi^2_{L-1}$ quantiles again lets deviation from $y=x$ be read off as evidence of a lane effect —
now driven by *extra-Poisson* variation (more spread across lanes than a single Poisson rate would
produce) rather than by an imbalanced $p$-value.

## Reading Figure 2

The figure has four qq-plot panels, in the same $-\log$-vs-quantile style described above, each
with points above the 95th percentile marked in one colour and points above the 99.5th in another,
so the reader can see how much of the tail is unusual.

- **Panel A** — the hypergeometric-test $p$-values for one pair of lanes sequencing the same
  sample at the same concentration (kidney, Run 1 lane 1 vs. Run 2 lane 2). Points track the
  diagonal closely, with only a small handful bending away at the extreme end.
- **Panel B** — the same test, but for two lanes sequencing the same sample at *different*
  concentrations (kidney, Run 1 lane 1 vs. Run 2 lane 4). The departure from the diagonal is far
  larger and starts much earlier in the tail.
- **Panels C and D** — the multi-lane goodness-of-fit statistic for the kidney sample sequenced at
  3 pM, plotted against $\chi^2$ quantiles with 4 degrees of freedom (so five lanes were compared
  at once), shown at two different scales — the full range in C, and a zoomed-in view of the bulk
  of the distribution in D. The liver sample showed a similar pattern.

Across the 22 pairwise comparisons between lanes running the same sample at the same concentration,
consistently fewer than 0.5% of genes showed the very small $p$-values that indicate a clear lane
effect — true both for lanes compared within one sequencing run and across two different runs,
though cross-run comparisons showed slightly more such genes (the study notes that larger
experiments would be needed to pin down run-to-run variability more precisely). The multi-lane
Poisson test told the same story from the other direction: only about 0.5% of genes showed strong
evidence of extra-Poisson variation across lanes.

## What the concentration comparison shows

The contrast between panels A and B is the substantive point. Two lanes of the *same sample at the
same concentration* look, for all but a tiny fraction of genes, like two random splits of one pool
of reads — almost exactly what the Poisson sampling model with no lane effect predicts. Two lanes
of the same sample at *different* concentrations do not: far more genes show $p$-values too small
to be explained by sampling error alone. So whatever is producing the disagreement is tied to
concentration, not to which physical lane a sample happened to run in — the lanes themselves are,
to a good approximation, doing what a pure Poisson counting process would do.

## Sources

- `docs/omics-statistics/statomics/sga21/images_sequencing/marioni_fig2.md` (statOmics/SGA21
  repository, commit `0ad787d4cc2bb2f4636440840a8a923cf6c09839`, licensed CC BY-NC-SA 4.0) — the
  sole input for this chapter, including its embedded figure image. That page is itself a
  model reconstruction of `images_sequencing/marioni_fig2.pdf`, a PDF with no extractable text
  layer, and is marked there as "reconstructed": the prose may paraphrase the original and its
  equations are flagged unverified. This chapter follows its equations and numbers as given, but
  they carry that same caveat one level further back.
- No slides, transcript or exercises were supplied for this chapter.
- The excerpt is drawn from a paper by Marioni and colleagues assessing the technical
  reproducibility of RNA-seq (its figure and file are named "Marioni fig2" and the running text
  describes exactly this comparison of lanes, runs and concentrations for kidney and liver
  samples); the paper's full title, venue and year are not stated anywhere in the supplied
  fragment and are not asserted here. A companion excerpt from the same source, `marioni_fig1.md`
  in the same directory, was not supplied as input to this chapter.

---

[← 13. RNA-seq versus Microarray Reproducibility](13-rna-seq-versus-microarray-reproducibility.md) · [Contents](index.md) · [15. Experimental design →](15-experimental-design.md)
