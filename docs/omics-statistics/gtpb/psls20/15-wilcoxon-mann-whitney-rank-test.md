---
title: "15. Wilcoxon-Mann-Whitney Rank Test"
course: "GTPB Psls20"
chapter: 15
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Wilcoxon-Mann-Whitney Rank Test

## What this covers

This chapter covers why you might give up on the two-sample $t$-test in favour of a test built on
**ranks**, how the resulting Wilcoxon rank-sum statistic and Mann-Whitney $U$ statistic are
constructed, why they turn out to be the same test in disguise, and how to read the result without
committing to the assumption that the two distributions differ only by a shift. It assumes the
reader already has the two-sample $t$-test, the idea of a permutation test, and can compute an
expectation and a variance for a simple statistic under a stated null.

## Why give up on the $t$-test?

The classical toolbox — the $t$-test, its $p$-value $\mathrm{P}_0[\,|T| \geq |t|\,]$, its 95% CI —
is only exactly correct when the assumptions behind it hold: normally distributed data (or a large
enough sample) and, for a two-sample comparison, equal variance across groups. If either is
violated, the null distribution used to read off the $p$-value is the wrong one, and the stated
95% coverage of the CI is not the true coverage.

There is a subtlety in how much this matters, though. Asymptotically the $t$-test is close to
non-parametric: as the sample size grows, the central limit theorem pulls the sampling distribution
of the mean toward normal regardless of the shape of the population it came from, so the
normality assumption stops driving the answer. The real problem is a *small-sample* problem — and
small samples are exactly the case where you cannot check the assumption by eye anyway.

When the assumptions do hold, the parametric approach is not merely simpler, it is strictly better:
more efficient (more power at the same sample size, or a tighter CI) and more flexible (it extends
more easily to complex designs). Non-parametric methods are the fallback for when that efficiency
cannot be bought because the assumptions it rests on cannot be checked.

### The motivating example: cholesterol after a stroke

Cholesterol concentration in blood was measured for two groups: five heart patients, two days after
a stroke, and five healthy subjects. The question is whether cholesterol concentration differs on
average between the two groups. A boxplot and a normal QQ-plot of the data show possible outliers,
but with only five observations per group there is no realistic way to *assess* the distributional
assumptions the $t$-test would need — five points do not tell you whether a population is normal or
whether two populations share a variance. This is the situation rank-based tests are for: small
groups, assumptions that cannot be checked, and (as it turns out below) possible outliers that a
mean-based statistic is sensitive to but a rank-based one is not.

## Ranks

A rank test starts by replacing the data with their ranks. For observations $Y_1, \ldots, Y_n$ with
no ties, the rank of $Y_i$ is

$$
R_i = R(Y_i) = \#\{\, Y_j : Y_j \leq Y_i,\ j = 1, \ldots, n \,\}.
$$

The smallest observation gets rank 1, the second-smallest rank 2, and so on up to the largest,
which gets rank $n$. Replacing values by ranks is what buys robustness to outliers: an
extreme value only ever contributes the ranks $1$ or $n$, however far out it sits.

**Ties.** Sometimes two or more observations share a value. Take
$403, 507, 507, 610, 651, 651, 651, 830, 900$: the value $507$ occurs twice and $651$ occurs three
times. Assigning plain ranks would be ambiguous, so tied values are given the average of the ranks
they would have occupied — a **midrank**:

$$
R_i = \frac{\#\{\,Y_j \leq Y_i\,\} + \bigl(\#\{\,Y_j < Y_i\,\} + 1\bigr)}{2}.
$$

For the sequence above this gives ranks $1,\ 2.5,\ 2.5,\ 4,\ 6,\ 6,\ 6,\ 8,\ 9$: the two copies of
$507$ split the ranks $2$ and $3$ between them, and the three copies of $651$ split ranks
$5, 6, 7$ into $6$ each.

**Ranks of a pooled sample.** For a two-sample comparison, let $Y_{ij}$, $i = 1, \ldots, n_j$, be
the observations of treatment group $j = 1, 2$. Pool the two groups into a single sequence
$Z_1, \ldots, Z_n$ with $n = n_1 + n_2$, and rank *that* combined sequence. Every observation now
carries a rank that says where it sits relative to *all* the data, not just its own group — which
is exactly what lets a rank statistic compare the two groups.

<figure>
<svg viewBox="0 0 480 210" role="img" aria-label="Ten pooled observations from two groups, sorted along a value axis, with their ranks and which group each falls in">
  <line x1="40" y1="140" x2="440" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <text x="440" y="165" font-size="12" fill="currentColor">value</text>
  <g font-size="12" fill="currentColor">
    <circle cx="60" cy="140" r="7" fill="none" stroke="currentColor"/>
    <circle cx="100" cy="140" r="7" fill="none" stroke="currentColor"/>
    <circle cx="140" cy="140" r="7" fill="darkorange" stroke="currentColor"/>
    <circle cx="180" cy="140" r="7" fill="none" stroke="currentColor"/>
    <circle cx="220" cy="140" r="7" fill="none" stroke="currentColor"/>
    <circle cx="260" cy="140" r="7" fill="darkorange" stroke="currentColor"/>
    <circle cx="300" cy="140" r="7" fill="darkorange" stroke="currentColor"/>
    <circle cx="340" cy="140" r="7" fill="darkorange" stroke="currentColor"/>
    <circle cx="380" cy="140" r="7" fill="none" stroke="currentColor"/>
    <circle cx="420" cy="140" r="7" fill="darkorange" stroke="currentColor"/>
  </g>
  <g font-size="12" fill="currentColor" text-anchor="middle">
    <text x="60" y="175">1</text>
    <text x="100" y="175">2</text>
    <text x="140" y="175">3</text>
    <text x="180" y="175">4</text>
    <text x="220" y="175">5</text>
    <text x="260" y="175">6</text>
    <text x="300" y="175">7</text>
    <text x="340" y="175">8</text>
    <text x="380" y="175">9</text>
    <text x="420" y="175">10</text>
  </g>
  <circle cx="55" cy="20" r="6" fill="none" stroke="currentColor"/>
  <text x="70" y="24" font-size="12" fill="currentColor">group 2</text>
  <circle cx="160" cy="20" r="6" fill="darkorange" stroke="currentColor"/>
  <text x="175" y="24" font-size="12" fill="currentColor">group 1</text>
</svg>
<figcaption>Schematic, not the actual cholesterol data: ten pooled observations sorted by value.
Each point's rank is its position in the pooled order. Group 1's points sit toward the high end,
so the sum of its ranks (here 3+6+7+8+10 = 34) exceeds group 2's (1+2+4+5+9 = 21) even though the
two sums must always add to $\tfrac12 n(n+1) = 55$ — this imbalance is exactly what a rank-sum
statistic is built to detect.</figcaption>
</figure>

## The Wilcoxon rank-sum test

Simultaneously developed by Wilcoxon, and by Mann and Whitney, this test goes by three names —
**Wilcoxon–Mann–Whitney**, **Wilcoxon rank-sum test**, **Mann–Whitney $U$ test** — for what turns
out to be one test.

**Hypotheses.** Under $H_0$ the two groups have the same distribution, $H_0: f_1 = f_2$. Under the
alternative used first, the distributions differ only in location:
$H_1: \mu_1 \neq \mu_2$. This alternative is a **location-shift** assumption — the two populations
are the same shape, just moved — and it will be relaxed once the Mann–Whitney statistic gives a
better way to state the conclusion.

**Test statistic.** The classical $t$-test statistic is built from the difference in sample means,
$\bar Y_1 - \bar Y_2$. The rank version replaces the raw values by their ranks in the pooled sample
$R_{ij} = R(Y_{ij})$ and takes the same kind of difference:

$$
T = \frac{1}{n_1}\sum_{i=1}^{n_1} R(Y_{i1}) - \frac{1}{n_2}\sum_{i=1}^{n_2} R(Y_{i2}).
$$

Under $H_0$ the average rank in each group should be about the same, so $T$ should be close to
zero; under $H_1$ the mean ranks differ and $T$ moves away from zero.

Because the total of all ranks is fixed —

$$
S_1 + S_2 = 1 + 2 + \cdots + n = \tfrac12 n(n+1),
$$

— knowing $S_1 = \sum_{i=1}^{n_1} R(Y_{i1})$, the **rank sum** of group 1, is enough: $S_2$ and
hence $T$ follow immediately. So the test only needs to track one number, $S_1$ (or equivalently
$S_2$) — which is where the name *rank-sum test* comes from.

**Exact test by permutation.** The null distribution of $S_1$ can be obtained exactly, by
permutation: under $H_0$ every assignment of the $n$ pooled ranks to the two groups is equally
likely, so the reference distribution is just that of $S_1$ over all such reassignments. For a
given $n$ with no ties the pooled ranks are always $1, 2, \ldots, n$, so for fixed $n_1, n_2$ the
permutation distribution of $S_1$ is *always the same distribution* — it doesn't depend on the data
at all, only on the two sample sizes. Historically this made the test attractive because the
reference distribution could be tabulated once; with modern computing power, being able to
tabulate it in advance matters much less, since it can simply be recomputed by permutation for any
given $n_1, n_2$.

**Standardized statistic and the large-sample approximation.** It is common to use the standardized
version of the rank-sum statistic,

$$
T = \frac{S_1 - \mathrm{E}_0[S_1]}{\sqrt{\mathrm{Var}_0[S_1]}},
$$

where, under $H_0$,

$$
\mathrm{E}_0[S_1] = \tfrac12 n_1(n+1), \qquad \mathrm{Var}_0[S_1] = \tfrac{1}{12} n_1 n_2 (n+1).
$$

As $\min(n_1, n_2) \to \infty$ under $H_0$, this standardized statistic converges to $N(0,1)$ — so
for large enough samples a normal approximation can stand in for the exact permutation
distribution.

## The Mann–Whitney $U$ statistic and the probabilistic index

There is a second, equivalent way to build the same test. In the absence of ties, define

$$
U_1 = \sum_{i=1}^{n_1}\sum_{k=1}^{n_2} \mathrm{I}\{\, Y_{i1} \geq Y_{k2} \,\},
$$

where $\mathrm{I}\{\cdot\}$ is $1$ if the statement is true and $0$ otherwise. $U_1$ simply counts,
over every pair of one observation from group 1 and one from group 2, how often the group-1
observation is at least as large as the group-2 one.

$U_1$ and $S_1$ carry exactly the same information: it can be shown that

$$
U_1 = S_1 - \tfrac12 n_1(n_1+1).
$$

Because this is a fixed linear relationship, $U_1$ is itself a rank statistic, and an exact test
built on $U_1$ is equivalent to one built on $S_1$ — they always reject on the same data.

**Why bother with $U_1$ at all, then?** Because it carries a better interpretation. Let $Y_1, Y_2$
be single random draws from populations $1$ and $2$. Then

$$
\frac{1}{n_1 n_2}\,\mathrm{E}[U_1] = \mathrm{P}[Y_1 \geq Y_2].
$$

So dividing $U_1$ by the number of pairs compared, $n_1 n_2$, estimates the probability that a
random observation from group 1 is at least as large as a random observation from group 2 — the
**probabilistic index**. Under $H_0$, $\mathrm{P}[Y_1 \geq Y_2] = \tfrac12$: neither group tends to
give the larger value.

This is the quantity R's `wilcox.test` actually reports as its test statistic $W$ — the
Mann–Whitney $U_1$, not the Wilcoxon rank sum $S_1$ — which is worth knowing before comparing
software output against a rank sum computed by hand.

**Why this relaxes the location-shift assumption.** The mean-difference reading of the test ($\mu_1
\neq \mu_2$) only makes sense if the two distributions really are shifted copies of one another. The
probabilistic-index reading does not need that: $\mathrm{P}[Y_1 \geq Y_2] \neq \tfrac12$ is a
meaningful alternative to $H_0: f_1 = f_2$ whether or not the shapes match, because it is a
statement about which group tends to produce the larger observation, not about where a shared
distribution has been moved to. So the hypotheses can be restated, distribution-free, as

$$
H_0: F_1 = F_2 \quad \text{vs} \quad H_1: \mathrm{P}[Y_1 \geq Y_2] \neq 0.5.
$$

## Working the cholesterol example

Return to the five heart patients and five healthy subjects. Pooling the ten cholesterol readings
and ranking them gives the ten pooled ranks $1, \ldots, 10$ split between the groups; summing the
ranks landing in each group gives $S_1$ and $S_2$, which must satisfy $S_1 + S_2 = \tfrac12 \cdot
10 \cdot 11 = 55$. Equivalently, $U_1$ can be obtained directly by counting, over all $5 \times 5 =
25$ cross-group pairs, how often a heart-patient value is at least as large as a healthy-subject
value — and the identity $U_1 = S_1 - \tfrac12 n_1(n_1+1) = S_1 - 15$ lets you check the two routes
against each other.

Testing $H_0: f_1 = f_2$ against the location-shift alternative gives a $p$-value below $0.05$, so
$H_0$ is rejected: there is a statistically significant difference between the cholesterol
distributions of the two groups. Read as a shift in means, the conclusion is that heart patients'
mean cholesterol is higher than that of healthy subjects — but that reading rests on the
location-shift assumption, which cannot really be assessed with only five observations per group.

The probabilistic-index reading needs no such assumption: dividing $U_1$ by $n_1 n_2 = 25$
estimates directly the probability that a random heart patient's cholesterol reading exceeds a
random healthy subject's. Because that estimate stays interpretable without the shift assumption,
it is the safer statement to make from data this sparse — the conclusion becomes "a heart patient
is more likely than not to show the higher cholesterol reading," with the probabilistic index as
the point estimate of how much more likely, rather than a claim about the size of a mean shift the
data cannot really support checking.

## Sources

- Notes: [`01-introduction.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd) —
  motivation for non-parametric tests and the cholesterol data setup (boxplot and QQ-plot,
  possible outliers, only 5 observations per group).
- Notes: [`02-rank-tests.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd) —
  rank transformation, midranks under ties, ranks of a pooled two-group sample.
- Notes: [`03-wilcoxon-mann-whitney-test.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd) —
  the rank-sum statistic $S_1$, its permutation and asymptotic null distributions, the
  Mann–Whitney statistic $U_1$, the probabilistic index, and the cholesterol conclusion.

All three files are converted from the same source Rmd
(`theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd` in GTPB/PSLS20, CC BY 4.0), split
into slide-sized sections; no separate transcript or slide deck was supplied for this chapter. The
Rmd's R code chunks compute the actual cholesterol data, the rank sums, $U_1$, and the numeric
$p$-value and probabilistic-index estimate, but the chunks were not evaluated in the supplied
material — only the code and the qualitative conclusion it was used to reach are given, so the
numeric results quoted above are left as the formulas that produce them rather than invented
numbers. No exercises were supplied with this lecture.

---

[← 14. Kruskal-Wallis Test for g Groups](14-kruskal-wallis-test-for-g-groups.md) · [Contents](index.md) · [16. Kruskal-Wallis Test for Groups →](16-kruskal-wallis-test-for-groups.md)
