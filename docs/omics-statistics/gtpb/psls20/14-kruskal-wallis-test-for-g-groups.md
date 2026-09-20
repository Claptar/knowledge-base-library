---
title: "14. Kruskal-Wallis Test for g Groups"
course: "GTPB Psls20"
chapter: 14
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Kruskal-Wallis Test for g Groups

## What this covers

This chapter asks how to test for a difference among more than two groups when the assumptions
behind the one-way ANOVA $F$-test — normality and equal variance within each group — are in doubt,
and there are too few observations per group to check them reliably. The answer is the
Kruskal-Wallis (KW) test, a rank-based analogue of the ANOVA $F$-test, worked through a genotoxicity
study on rats. It assumes the reader already has the one-way ANOVA decomposition of variability
into a between-groups sum of squares (SST) and a within-groups sum of squares (SSE), and the idea
of a permutation test. It also uses the two-sample Wilcoxon-Mann-Whitney (WMW) test and its $U$
statistic in the follow-up analysis, without re-deriving them here.

## The motivating example: DMH genotoxicity

The study assesses the genotoxicity of 1,2-dimethylhydrazine dihydrochloride (DMH), as required by
an EU testing directive. Twenty-four rats are split into four groups of six, each given a different
daily dose of DMH: control, low, medium, high. Genotoxicity is read off the liver, using a *comet
assay*: DNA strand breaks are visualised, and the length of the resulting "comet tail" is a proxy
for the amount of strand breakage, measured on liver cells taken from each rat. The applied
question is whether DNA damage differs with DMH dose.

A boxplot of comet length against dose, and a normal QQ-plot faceted by dose, are used to check the
usual ANOVA assumptions. Two things go wrong at once:

- the control group's boxplot shows a visibly smaller spread than the treated groups — a strong
  hint that the groups do not share a common variance;
- with only six rats per group, there is not enough data to check *either* assumption
  (normality, equal variance) with any confidence — six points barely constrain a QQ-plot.

That combination is exactly what should push the analysis toward a method that does not lean on
those assumptions in the first place.

## From the $F$-test to a rank statistic

Write the classical one-way ANOVA $F$-statistic, for $g$ groups and $n$ observations in total, as

$$
F = \frac{\text{SST}/(g-1)}{\text{SSE}/(n-g)} = \frac{\text{SST}/(g-1)}{(\text{SSTot}-\text{SST})/(n-g)},
$$

using $\text{SSE} = \text{SSTot} - \text{SST}$, where

$$
\text{SST} = \sum_{j=1}^g n_j\left(\bar Y_j - \bar Y\right)^2
$$

is the between-groups sum of squares.

The point that matters for what follows: $\text{SSTot}$ depends only on the set of measured values
$\mathbf{y}$, not on which unit is assigned to which group. So if you were to test the null
hypothesis by a *permutation test* — repeatedly reshuffling which rat's measurement is attached to
which dose group and recomputing the statistic — $\text{SSTot}$ never changes across permutations.
With $\text{SSTot}$ held fixed, $F$ is an increasing function of $\text{SST}$ alone, so ranking
permutations by $F$ gives exactly the same permutation $p$-value as ranking them by $\text{SST}$.
That means $\text{SST}$ on its own is a perfectly good test statistic for a permutation test — no
need to compute the full $F$ ratio.

The Kruskal-Wallis test is built by applying this same construction not to the raw measurements,
but to their **ranks** (assuming no ties). Pool all $n$ observations, rank them $1$ through $n$,
and let $\bar R_j$ be the mean rank within group $j$. Because the ranks are just a permutation of
$1,\dots,n$, their overall mean is fixed no matter how they fall among the groups:

$$
\bar R = \frac{1}{n}(1+2+\cdots+n) = \frac{n+1}{2}.
$$

The between-groups sum of squares computed on ranks is then

$$
\text{SST}_{\text{rank}} = \sum_{j=1}^g n_j\left(\bar R_j - \bar R\right)^2
 = \sum_{j=1}^g n_j\left(\bar R_j - \frac{n+1}{2}\right)^2,
$$

and the Kruskal-Wallis statistic rescales it:

$$
KW = \frac{12}{n(n+1)} \sum_{j=1}^g n_j\left(\bar R_j - \frac{n+1}{2}\right)^2.
$$

The constant $\frac{12}{n(n+1)}$ is chosen precisely so that $KW$ has a simple asymptotic null
distribution: under $H_0$, as $\min(n_1,\dots,n_g)\to\infty$,

$$
KW \longrightarrow \chi^2_{g-1},
$$

a chi-squared distribution on $g-1$ degrees of freedom — the same degrees of freedom that sit in
the numerator of the $F$-test.

Because $KW$ is built entirely from ranks, its *exact* permutation null distribution depends only
on the group sizes $n_1,\dots,n_g$, not on the values themselves. That means the exact test can, in
principle, be computed once and reused for any dataset with those group sizes, rather than relying
on the large-sample $\chi^2$ approximation.

## Stating the alternative hypothesis

The null hypothesis is always that all $g$ groups are drawn from the same distribution,
$H_0: f_1 = \cdots = f_g$. How the *alternative* should be phrased depends on what kind of
difference between groups is being assumed:

- If the groups can be assumed to differ only by a **location shift** — same shape, same spread,
  just shifted — then rejecting $H_0$ licenses a statement about means:
  $$H_1: \text{at least two of the group means are different.}$$
- If a location shift cannot be assumed — as here, where the control group's spread visibly
  differs from the treated groups' — that statement is not justified. The alternative then has to
  be phrased in terms of a **probabilistic index** instead:
  $$H_1: \exists\, j,k \in \{1,\dots,g\} : P\!\left[Y_j \geq Y_k\right] \neq 0.5,$$
  i.e. for some pair of groups, a random observation from one group is not equally likely to
  exceed a random observation from the other.

For the DMH data the location-shift assumption is exactly the one the diagnostics called into
question, so the second, weaker phrasing is the one the example uses.

## Applying the test to the DMH data

Running `kruskal.test(length ~ dose, data = dna)` computes the $KW$ statistic and reports a
$p$-value from the asymptotic $\chi^2$ approximation; at the $5\%$ level this rejects $H_0$.

But the same worry that made the ANOVA assumptions hard to check applies here too: with only six
rats per group, the large-sample $\chi^2$ approximation to $KW$'s null distribution is not
trustworthy. The R package `coin` provides an exact (Monte Carlo) alternative:

```r
library(coin)
kwPerm <- kruskal_test(length ~ dose, data = dna,
                        distribution = approximate(B = 100000))
```

This simulates the permutation null distribution directly — 100,000 random relabellings of dose
group to rat, recomputing $KW$ each time — instead of relying on the asymptotic approximation. The
conclusion is that the DNA damage measurements differ across DMH dose with extreme significance.

## Posthoc comparisons: which groups, and how

Rejecting the $g$-group null only says *some* pair of groups differs; it does not say which. The
standard follow-up is pairwise two-sample Wilcoxon-Mann-Whitney (WMW) tests between every pair of
groups, with the resulting $p$-values corrected for multiple testing — here with Holm's method, via
`pairwise.wilcox.test(dna$length, dna$dose)`.

For the DMH data: every treated dose group (low, medium, high) is significantly different from
control, but the three treated groups are not significantly different from one another.

Because a mean-difference summary is not well justified here (location shift is in doubt), the
size of each pairwise difference is instead reported as the probabilistic index
$P[Y_j \geq Y_k]$, estimated from the WMW test's $U$ statistic — the count, over all pairs of one
observation from each of the two groups, of how often the group-$j$ value exceeds the group-$k$
value — normalised by the number of such pairs:

$$
\widehat{P}[Y_j \geq Y_k] = \frac{U}{n_j\, n_k}.
$$

`pairwise.wilcox.test` does not report $U$ itself, so it has to be recovered pair by pair, running
`wilcox.test()` on each pair of groups and dividing its `statistic` by the product of the two
group sizes:

```r
nGroup <- table(dna$dose)
probInd <- combn(levels(dna$dose), 2, function(x) {
  test <- wilcox.test(length ~ dose, subset(dna, dose %in% x))
  test$statistic / prod(nGroup[x])
})
```

## Conclusion of the DMH study

- There is an extremely significant difference in the distribution of DNA-damage measurements
  across DMH dose ($p < 0.001$, KW test).
- DNA damage is more likely under every DMH dose than under control (all pairwise $p = 0.013$, WMW
  tests, Holm-corrected).
- The estimated probability that a DMH-exposed rat shows more damage than a control rat is $100\%$
  in this dataset — a confidence interval around that probabilistic index is beyond the scope of
  the course.
- There are no significant differences in comet length among the three DMH concentrations
  themselves.
- So DMH already shows a genotoxic effect at the lowest dose tested.

## Sources

- Notes: `theory/09-NonparametericStatistics-KruskalWallis.Rmd`, GTPB "Practical Statistics for the
  Life Sciences" (PSLS20, 2020), theory unit 9 — converted and split as
  [`01-comparison-of-groups.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-KruskalWallis.Rmd)
  (the DMH setup, comet assay, and the diagnostic boxplot/QQ-plot discussion) and
  [`02-kruskal-wallis-rank-test.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-KruskalWallis.Rmd)
  (the $F$-to-rank-statistic derivation, the KW statistic, the hypothesis statements, and the
  posthoc/probabilistic-index analysis), both CC BY 4.0. No separate slide deck or lecture
  transcript was supplied for this chapter; these two pages, an R Markdown lecture handout, are the
  whole of the supplied material.
- Not supplied: the underlying `dna.txt` dataset (only the code that reads it from a URL was
  given), the comet-assay photograph linked in the source, and the sibling theory unit on the
  two-sample Wilcoxon-Mann-Whitney test and its $U$ statistic, which this chapter's posthoc
  analysis relies on but does not itself re-derive.

---

[← 13. Multiple Linear Regression](13-multiple-linear-regression.md) · [Contents](index.md) · [15. Wilcoxon-Mann-Whitney Rank Test →](15-wilcoxon-mann-whitney-rank-test.md)
