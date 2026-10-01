---
title: "11. One-Way ANOVA and Post-Hoc Tests"
course: "GTPB Psls20"
chapter: 11
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. One-Way ANOVA and Post-Hoc Tests

## What this covers

This chapter answers a specific question: when an experiment has *more than two* groups to compare,
how do you test whether their means differ, without either losing power by testing each pair
separately or inflating the false-positive rate by running many tests at once? It builds one-way
analysis of variance (ANOVA) as a linear-regression model with dummy variables, derives the
$F$-test from a decomposition of the sum of squares, and then covers what happens *after* that test
rejects: identifying which groups differ, with the multiple-comparisons correction that makes the
answer trustworthy (Bonferroni, then Tukey). One running example carries the argument throughout:
prostacyclin levels in the blood plasma of rats given three doses of arachidonic acid. The chapter
assumes simple linear regression (least squares, the $t$-test on a coefficient) and the basic
vocabulary of hypothesis testing (null/alternative, $p$-value, type I error).

## The experiment: three doses, one outcome

Researchers wanted to know whether arachidonic acid affects the level of prostacyclin in blood
plasma. They used three doses — low, medium and high — each given to 12 rats, and measured
prostacyclin by an ELISA fluorescence assay. Boxplots and QQ-plots of the three groups support
treating the outcome as approximately normal with a common variance across groups:

$$
Y_i \mid \text{group } j \sim N(\mu_j, \sigma^2), \qquad j = 1, 2, 3.
$$

The scientific question — does dose affect prostacyclin? — becomes a hypothesis about the three
group means:

$$
H_0 : \mu_1 = \mu_2 = \mu_3 \qquad \text{vs.} \qquad H_1 : \exists\, j,k : \mu_j \neq \mu_k.
$$

The obvious way to attack $H_1$ is to split it into pairwise statements, $H_{0jk}: \mu_j = \mu_k$
versus $H_{1jk}: \mu_j \neq \mu_k$, and run a two-sample $t$-test on each pair. That approach is
picked up again later in the chapter, because it fails in a specific and quantifiable way: running
several tests to reach one conclusion inflates the chance of a false positive, and loses power on
top of that. The fix used throughout is to test $H_0: \mu_1 = \mu_2 = \mu_3$ with a *single* test
first, and only afterward ask which groups differ.

## ANOVA as a linear model with dummy variables

The single test comes from writing group membership as a regression. With $g=3$ groups you need
$g - 1 = 2$ dummy variables — one fewer than the number of groups, as in ordinary dummy coding:

$$
x_{i1} = \begin{cases} 1 & \text{observation } i \text{ is in the medium-dose group} \\ 0 & \text{otherwise} \end{cases}
\qquad
x_{i2} = \begin{cases} 1 & \text{observation } i \text{ is in the high-dose group} \\ 0 & \text{otherwise} \end{cases}
$$

so that the low-dose group, with $x_{i1}=x_{i2}=0$, is the *reference group*. The model is

$$
Y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \epsilon_i, \qquad \epsilon_i \stackrel{\text{i.i.d.}}{\sim} N(0,\sigma^2),
$$

which, written out group by group, is

$$
Y_{i \mid L} = \beta_0 + \epsilon_i, \qquad Y_{i \mid M} = \beta_0 + \beta_1 + \epsilon_i, \qquad Y_{i \mid H} = \beta_0 + \beta_2 + \epsilon_i.
$$

Each $\beta$ therefore has a mean-difference reading: $\beta_0 = E[Y_i \mid L]$ is the mean in the
reference group, $\beta_1 = E[Y_i \mid M] - E[Y_i \mid L]$ is the medium-vs-low effect, and $\beta_2
= E[Y_i \mid H] - E[Y_i \mid L]$ is the high-vs-low effect. Writing $\mu_j = E[Y_i \mid \text{group }
j]$, the model says $\mu_1=\beta_0$, $\mu_2=\beta_0+\beta_1$, $\mu_3=\beta_0+\beta_2$, and the
original hypothesis $H_0: \mu_1=\mu_2=\mu_3$ becomes a hypothesis about two regression
coefficients:

$$
H_0 : \beta_1 = \beta_2 = 0.
$$

That is the payoff of the setup: $H_0$ is now a hypothesis inside an ordinary linear model, so every
tool from linear regression — parameter estimates, standard errors, confidence intervals — is
already available, and testing $\beta_1=\beta_2=0$ jointly is a single $F$-test. Generalizing to
$g>3$ groups needs no new idea, only $g-1$ dummy variables instead of $2$. In R this model is fit as
`lm(prostac ~ dose, data = prostacyclin)`.

## Decomposing the sum of squares

As with simple linear regression, the $F$-test falls out of a sum-of-squares identity. The
regression sum of squares is

$$
\text{SSR} = \sum_{i=1}^n (\hat Y_i - \bar Y)^2.
$$

Inside each group, every fitted value is the same number — $\hat\beta_0$ for group L,
$\hat\beta_0+\hat\beta_1$ for group M, $\hat\beta_0+\hat\beta_2$ for group H — and because these are
least-squares estimates of a group-wise-constant mean, that constant is exactly the group's sample
mean. So the sum splits into three group-wise sums, each contributing $n_j$ identical terms:

$$
\text{SSR} = \sum_{i=1}^{n_1}(\bar Y_1 - \bar Y)^2 + \sum_{i=1}^{n_2}(\bar Y_2-\bar Y)^2 + \sum_{i=1}^{n_3}(\bar Y_3-\bar Y)^2,
$$

with $n_1=n_2=n_3=12$ here. In the ANOVA setting this quantity is renamed the **treatment sum of
squares**, $\text{SST}$ (also written $\text{SSBetween}$), because it is entirely a measure of how
far the group means sit from the grand mean — the variability *between* groups. It carries $g-1$
degrees of freedom: $g$ parameters in the full model minus the $1$ parameter (the grand mean) that a
model with only an intercept would need.

The total variability in the data, $\text{SSTot} = \sum_i (Y_i - \bar Y)^2$, decomposes as

$$
\text{SSTot} = \text{SST} + \text{SSE},
$$

where $\text{SSE} = \sum_i (Y_i - \hat Y_i)^2$ is the residual, or **within-group**, sum of squares —
exactly the part SST does not capture. The decomposition is really a statement about a single
observation: its deviation from the grand mean splits exactly into a between-group part and a
within-group part.

<figure>
<svg viewBox="0 0 460 220" role="img" aria-label="Three prostacyclin dose groups with their group means and the grand mean, showing one observation's deviation split into a between-group part and a within-group part">
  <line x1="50" y1="140" x2="360" y2="140" stroke="currentColor" stroke-width="1" stroke-dasharray="5 3"/>
  <text x="26" y="144" font-size="12" fill="currentColor">y&#x0304;</text>

  <line x1="60" y1="178" x2="120" y2="178" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 2"/>
  <circle cx="68" cy="183" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="82" cy="172" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="96" cy="180" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="110" cy="174" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <text x="90" y="200" font-size="12" fill="currentColor" text-anchor="middle">low</text>

  <line x1="170" y1="148" x2="230" y2="148" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 2"/>
  <circle cx="178" cy="142" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="192" cy="152" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="206" cy="146" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="220" cy="150" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <text x="200" y="200" font-size="12" fill="currentColor" text-anchor="middle">medium</text>

  <line x1="280" y1="75" x2="340" y2="75" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 2"/>
  <circle cx="285" cy="95" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="315" cy="90" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="330" cy="68" r="2.5" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="300" cy="100" r="3.5" fill="currentColor"/>
  <text x="310" y="200" font-size="12" fill="currentColor" text-anchor="middle">high</text>
  <text x="304" y="112" font-size="12" fill="currentColor">y&#7522;</text>

  <line x1="300" y1="100" x2="360" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="340" y1="75" x2="360" y2="75" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>

  <line x1="362" y1="140" x2="368" y2="140" stroke="currentColor" stroke-width="1"/>
  <line x1="362" y1="75" x2="368" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="368" y1="140" x2="368" y2="75" stroke="currentColor" stroke-width="2"/>
  <text x="373" y="112" font-size="12" fill="currentColor">between</text>

  <line x1="384" y1="75" x2="390" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="384" y1="100" x2="390" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="390" y1="75" x2="390" y2="100" stroke="currentColor" stroke-width="2"/>
  <text x="394" y="92" font-size="12" fill="currentColor">within</text>

  <line x1="406" y1="140" x2="412" y2="140" stroke="currentColor" stroke-width="1"/>
  <line x1="406" y1="100" x2="412" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="412" y1="140" x2="412" y2="100" stroke="currentColor" stroke-width="2"/>
  <text x="416" y="124" font-size="12" fill="currentColor">total</text>
</svg>
<figcaption>One observation y&#7522; in the high-dose group (H), against the grand mean y&#x0304; and its own
group mean y&#x0304;&#7522; (subscript H). The total deviation splits exactly into a between-group part and a
within-group part — the identity behind SSTot = SST + SSE.</figcaption>
</figure>

## The F-test and the ANOVA table

Two mean squares follow from the two sums of squares: $\text{MST} = \text{SST}/(g-1)$ measures
variability *between* groups, and $\text{MSE} = \text{SSE}/(n-g)$ measures variability *within*
groups (i.e. the residual variance $\sigma^2$). Comparing them gives the test statistic:

$$
F = \frac{\text{MST}}{\text{MSE}}, \qquad F \sim F_{g-1,\,n-g} \text{ under } H_0.
$$

For the prostacyclin data, $g=3$ and $n=36$, so under $H_0$, $F \sim F_{2,33}$. The calculation is
usually laid out as an ANOVA table:

| | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
|---|---|---|---|---|---|
| Treatment (dose) | $g-1$ | SST | MST | $F$ | $p$ |
| Error | $n-g$ | SSE | MSE | | |

produced in R by `anova(model1)`.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="F-distribution density with the rejection region shaded to the right of the critical value">
  <line x1="30" y1="170" x2="350" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="355" y="174" font-size="12" fill="currentColor">F</text>

  <path d="M30,170 C55,170 65,60 95,58 C130,55 155,100 185,128 C215,150 260,166 340,169" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <path d="M195,170 L195,135 C215,150 260,166 340,169 L340,170 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>

  <line x1="195" y1="170" x2="195" y2="135" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="150" y="188" font-size="12" fill="currentColor">F crit (95%)</text>

  <line x1="230" y1="170" x2="230" y2="156" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="233" y="150" font-size="12" fill="currentColor">observed f</text>

  <text x="95" y="145" font-size="12" fill="currentColor">accept</text>
  <text x="300" y="150" font-size="12" fill="currentColor">reject</text>
</svg>
<figcaption>The null distribution of F = MST/MSE, with the 5% rejection region shaded. For the
prostacyclin data the observed F falls well out in that tail, so the omnibus null &#956;1=&#956;2=&#956;3
is rejected.</figcaption>
</figure>

Once the omnibus test rejects, the *same* fitted model — `summary(model1)` — already reports the
estimated coefficients $\hat\beta_1$ (medium vs. low) and $\hat\beta_2$ (high vs. low), each with its
own $t$-test. It is tempting to read the answer to "which groups differ" straight off that table,
but those individual p-values do not account for the fact that two comparisons were read off the
same fit at once — the multiple-testing problem returns here in a slightly different guise, and is
the subject of the next section.

## After the F-test: which groups actually differ?

Rejecting $H_0: \mu_1=\mu_2=\mu_3$ only says that *some* pair of means differs, not which. The
natural next step is the naive method flagged earlier: split the hypothesis into pairwise
comparisons $H_{0jk}: \mu_j=\mu_k$ and test each with a two-sample $t$-test,

$$
T_{jk} = \frac{\bar Y_j - \bar Y_k}{S_p\sqrt{\tfrac{1}{n_j}+\tfrac1{n_k}}}, \qquad S_p^2 = \frac{(n_j-1)S_j^2+(n_k-1)S_k^2}{n_j+n_k-2},
$$

using only the two groups $j$ and $k$. But ANOVA already assumes all $g$ groups share one residual
variance $\sigma^2$, so throwing away the third group's data to estimate $S_p^2$ is wasteful. Using
$\text{MSE}$ from the full model instead — pooling information across *all* groups — is more
efficient and gives more residual degrees of freedom:

$$
T_{jk} = \frac{\bar Y_j - \bar Y_k}{\sqrt{\text{MSE}}\sqrt{\tfrac1{n_j}+\tfrac1{n_k}}} \sim t_{n-g}.
$$

This is what `pairwise.t.test(prostac, dose, "none")` computes. The problem is what happens when
several of these are run at the $\alpha$ significance level and a conclusion is drawn from whichever
one comes out significant.

**A simulation makes the failure concrete.** Simulate data from an ANOVA model with $g=3$ groups
where the means really are equal ($H_0$ true), run all $m=3$ pairwise $t$-tests, and reject the
*global* null the moment any one of the three p-values drops below $\alpha=5\%$. Repeated over many
simulated datasets, the fraction of false rejections comes out at more than twice the nominal $5\%$.
The effect worsens with more groups: with $g=5$ (so $m=10$ pairwise tests), the same procedure has a
type I error rate of $28.0\%$ against a target of $5\%$.

This is the **multiplicity problem**: a classical p-value can be compared to $\alpha$ only when the
conclusion rests on that one p-value. Here the decision — "are the means all equal?" — is really
based on $m=g(g-1)/2$ p-values at once, and the risk of at least one crossing the threshold by
chance grows with $m$.

## Controlling the family-wise error rate

When $m>1$ tests feed a single decision, the relevant error rate is not the per-test $\alpha$ but
the **family-wise error rate (FWER)**, $\alpha_F$ — the probability of *at least one* false positive
among all $m$ tests, computed under the assumption that all $m$ null hypotheses are true. A typical
target is $\alpha_F=0.05$.

**Bonferroni correction.** If the $m$ tests were independent, each run at level $\alpha$,

$$
\alpha_F = P[\text{at least one type I error}] = 1-(1-\alpha)^m \le m\alpha.
$$

Five independent tests at $\alpha=5\%$ already give $\alpha_F \approx 25\%$; running them at
$\alpha=1\%$ instead brings $\alpha_F$ back down to about $5\%$. The Bonferroni correction controls
$\alpha_F$ by setting the per-test level to $\alpha=\alpha_F/m$ — equivalently, by comparing
*adjusted p-values* $\tilde p = \min(m\times p,\,1)$ to $\alpha_F$ directly, or by reporting
$(1-\alpha_F/m)\times100\%$ confidence intervals.

For the prostacyclin data ($m=3$ pairwise comparisons), `pairwise.t.test(..., p.adjust.method =
"bonferroni")` — or the equivalent call through `glht()` in the `multcomp` package — leaves the
qualitative conclusions unchanged but scales every raw p-value up by a factor of $3$, and the FWER
is now genuinely controlled near $5\%$. Repeating the simulation with the correction applied
confirms it works, and shows its cost: for $g=5$ groups the achieved FWER comes out at $4.1\%$,
*below* the $5\%$ target. Bonferroni is conservative — the bound $1-(1-\alpha)^m \le m\alpha$ is not
tight once the tests are correlated, as pairwise comparisons drawn from the same ANOVA fit are — and
being conservative costs power: some real differences will be missed.

**Tukey's method.** A less conservative alternative built specifically for all-pairwise comparisons
of means. Rather than a fixed union-bound correction, it approximates the null distribution of the
post-hoc test statistic by simulation, so the adjusted p-values and confidence intervals it returns
can shift very slightly if the analysis is rerun. How that null distribution is built falls outside
the scope of this chapter, but Tukey's method is the default multiple-comparisons procedure in R's
`multcomp` package — `glht(model1, linfct = mcp(dose = "Tukey"))`, then `summary()` and `confint()`
— and is what should be reached for ahead of a hand-rolled Bonferroni correction.

## Conclusions for the prostacyclin example

Putting the pieces together, the recommended order of analysis is:

1. **Test the omnibus null first**, with the ANOVA $F$-test. It uses all the data at once, needs no
   multiple-testing correction (it is a single test of a single hypothesis), and has more power than
   jumping straight to pairwise comparisons.
2. **Only if that test rejects**, follow up with pairwise comparisons — corrected for multiplicity,
   by Tukey's method rather than uncorrected $t$-tests.

For the prostacyclin data this gives: an extremely significant effect of arachidonic acid dose on
mean prostacyclin concentration ($p<0.001$ from the ANOVA $F$-test). The Tukey-corrected post-hoc
comparisons show the high-dose group's mean prostacyclin concentration is significantly higher than
both the low-dose and the medium-dose groups (both comparisons $p<0.001$), while the difference
between the medium- and low-dose groups is not significant. All the post-hoc p-values and
confidence intervals are Tukey-adjusted for the three-way comparison, which is what makes them safe
to read individually.

## Sources

All sections come from one underlying course file in `gtpb-psls20`, *Analysis of Variance*
(`theory/07-Anova.Rmd`, [GitHub](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd)),
licensed CC BY 4.0, split into five converted notes pages:

- Problem setup, data exploration and hypotheses — `01-prostacyclin-example.md`
- The dummy-variable regression model and parameter interpretation — `02-analyse-of-variance.md`
- Sum-of-squares decomposition, the $F$-test and the ANOVA table — `03-sum-of-squares-and-anova.md`
- Naive pairwise $t$-tests, the multiplicity simulation, Bonferroni and Tukey — `04-post-hoc-analysis-multiple-comparisons-of-means.md`
- The worked conclusion for the prostacyclin data — `05-conclusions-prostacyclin-example.md`

The supplied material is the R Markdown source with its code chunks unexecuted: plotting code and
inline result placeholders (fitted coefficients, exact p-values, the simulated type-I-error rate
for $g=3$ pairwise tests, the specific confidence-interval widths in the conclusion) never evaluated
to numbers. Only the results the source states directly in prose — the $g=5$-group simulation
figures ($28.0\%$ naive, $4.1\%$ Bonferroni), the factor-of-three p-value scaling, and the direction
and significance pattern of the final comparisons — are reported here; no numeric value not present
in the source has been invented.

---

[← 10. Linear Regression Case Studies](10-linear-regression-case-studies.md) · [Contents](index.md) · [12. ANOVA Case Studies →](12-anova-case-studies.md)
