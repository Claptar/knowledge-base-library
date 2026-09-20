---
title: "17. Multiple Regression with Interactions"
course: "StatOmics Sga21"
chapter: 17
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Multiple Regression with Interactions

## What this covers

This chapter works through a single worked example — testing whether the expression of the gene
KPNA2 is associated with breast-cancer histologic grade — to show how a linear model with two
categorical predictors and their interaction is built, interpreted, and used to answer a set of
specific biological questions. It assumes you already know ordinary linear regression (fitting by
least squares, reading an ANOVA table) and the idea of a dummy (indicator) variable; what it adds is
how to read the *coefficients* of such a model as fold changes, and how to test a hypothesis that is
not a single coefficient but a combination of several.

## The study and the question

Histologic grade is a well-established prognostic factor in breast cancer, and the gene KPNA2 is
known to be associated with poor prognosis. The tutorial's data set records, for a set of tumour
samples, the expression of KPNA2, the histologic grade (grade 1 or grade 3), and lymph node status
(`0` if the lymph nodes were unaffected, `1` if they had to be surgically removed). The samples are
not just split by grade — they are split by grade *and* node status, so it is natural to ask not one
question but several:

- Is KPNA2 expression different between grade 3 and grade 1 tumours in patients with unaffected
  lymph nodes?
- Is it different between grade 3 and grade 1 tumours in patients with affected lymph nodes?
- Is it different between affected and unaffected lymph nodes, among grade 1 tumours?
- Is it different between affected and unaffected lymph nodes, among grade 3 tumours?
- Does the grade effect itself depend on node status (equivalently, does the node effect depend on
  grade)? — this is the question of whether grade and node *interact*.

A single two-sample test cannot answer all five at once, because grade and node status are crossed:
every patient falls into one of four combinations (grade 1/node 0, grade 3/node 0, grade 1/node 1,
grade 3/node 1), and the questions above are all comparisons between these four group means. That is
exactly what a linear model with two factors and an interaction term is for.

## Exploring the data: why work on the log scale

Plotting expression against the four grade-by-node combinations suggests, informally: an effect of
grade, an effect of node status, and — because the size of the apparent grade effect looks different
in the node-0 and node-1 groups — a possible interaction. It also suggests a mean–variance relation:
groups with higher average expression look more spread out.

Fitting `gene ~ grade * node` directly and inspecting the residual diagnostics confirms the
mean–variance relation (the spread of residuals grows with the fitted mean) and shows a QQ-plot that
deviates from normality. Both problems are addressed by working with $\log_2$-transformed expression
instead of raw expression: refitting `log2(gene) ~ grade * node` gives residual variance that is
roughly constant across the four groups, and a QQ-plot that no longer shows deviations from
normality. This is the usual reason to log-transform an intensity-type measurement before fitting a
linear model — not to change what is being asked, but to make the two things a linear model assumes
(constant variance, normal errors) hold.

An `Anova(fit, type = "III")` on the log-scale fit shows a very significant grade $\times$ node
interaction. That already answers the fifth question above — the size of the grade effect *does*
depend on node status — but it does not, by itself, say how the other four comparisons come out.
For that you need the model's coefficients directly.

## A model with two factors and their interaction

Write $x_{g3}$ for the dummy variable that is $1$ for a grade-3 tumour and $0$ for grade 1, and
$x_{n1}$ for the dummy variable that is $1$ when the lymph nodes were affected and $0$ otherwise.
The model for the $\log_2$-transformed expression $y$ is

$$
y = \beta_0 + \beta_{g3} x_{g3} + \beta_{n1} x_{n1} + \beta_{g3n1}\, x_{g3} x_{n1},
$$

with $\beta_0$ the intercept, $\beta_{g3}$ the main effect of grade, $\beta_{n1}$ the main effect of
node, and $\beta_{g3n1}$ the interaction between them. Because there are exactly four combinations of
grade and node, this model has exactly four free parameters and reproduces the four group means
exactly — it does not smooth or borrow information across groups, it just gives the four means names
that can be combined and tested.

Setting $x_{g3}, x_{n1}$ to $0$ or $1$ in turn gives the $\log_2$ mean expression $\hat\mu$ in each of
the four groups:

- $\log_2 \hat\mu_{g1n0} = \hat\beta_0$
- $\log_2 \hat\mu_{g3n0} = \hat\beta_0 + \hat\beta_{g3}$
- $\log_2 \hat\mu_{g1n1} = \hat\beta_0 + \hat\beta_{n1}$
- $\log_2 \hat\mu_{g3n1} = \hat\beta_0 + \hat\beta_{g3} + \hat\beta_{n1} + \hat\beta_{g3n1}$

Subtracting pairs of these gives exactly the four comparisons the questions above ask for, each as a
$\log_2$ fold change (FC):

$$
\log_2\widehat{FC}_{g3n0-g1n0} = \hat\beta_{g3}, \qquad
\log_2\widehat{FC}_{g3n1-g1n1} = \hat\beta_{g3} + \hat\beta_{g3n1},
$$

$$
\log_2\widehat{FC}_{g1n1-g1n0} = \hat\beta_{n1}, \qquad
\log_2\widehat{FC}_{g3n1-g3n0} = \hat\beta_{n1} + \hat\beta_{g3n1}.
$$

The interaction coefficient is the difference between the two grade fold changes (equivalently,
between the two node fold changes):

$$
\log_2\frac{\widehat{FC}_{g3n1-g1n1}}{\widehat{FC}_{g3n0-g1n0}}
= \log_2\frac{\widehat{FC}_{g3n1-g3n0}}{\widehat{FC}_{g1n1-g1n0}}
= \hat\beta_{g3n1}.
$$

This is the algebraic content of "the grade effect depends on node status": if $\beta_{g3n1}=0$, the
grade fold change is the same number in both node strata, and the node fold change is the same
number in both grade strata — the two factors act additively on the $\log_2$ scale. If
$\beta_{g3n1}\neq 0$, they do not, and $\beta_{g3n1}$ is exactly the size of the discrepancy.

<figure>
<svg viewBox="0 0 360 230" role="img" aria-label="Interaction plot: mean log2 expression against grade, one line per node status, with non-parallel slopes">
  <line x1="50" y1="200" x2="330" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="200" x2="50" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="190" y="220" text-anchor="middle" font-size="12" fill="currentColor">histologic grade</text>
  <text x="20" y="110" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 20 110)">log2 KPNA2 expression</text>
  <text x="100" y="215" text-anchor="middle" font-size="12" fill="currentColor">grade 1</text>
  <text x="280" y="215" text-anchor="middle" font-size="12" fill="currentColor">grade 3</text>

  <line x1="100" y1="175" x2="280" y2="55" stroke="currentColor" stroke-width="2"/>
  <circle cx="100" cy="175" r="3.5" fill="currentColor"/>
  <circle cx="280" cy="55" r="3.5" fill="currentColor"/>
  <text x="285" y="52" font-size="12" fill="currentColor">node 0</text>

  <line x1="100" y1="120" x2="280" y2="70" stroke="currentColor" stroke-width="2" stroke-dasharray="6 4"/>
  <circle cx="100" cy="120" r="3.5" fill="currentColor"/>
  <circle cx="280" cy="70" r="3.5" fill="currentColor"/>
  <text x="285" y="80" font-size="12" fill="currentColor">node 1</text>
</svg>
<figcaption>The pattern behind the interaction test: the node-1 line starts above the node-0 line at
grade 1 (a node effect there) but the two lines converge by grade 3 (little node effect there),
because the rise from grade 1 to grade 3 is steeper for node 0 than for node 1. Parallel lines would
mean no interaction; a gap that changes size is the interaction.</figcaption>
</figure>

## From coefficients to fold changes

Because $y$ is on the $\log_2$ scale, exponentiating a coefficient with base 2 converts a
*difference* of $\log_2$ means into a *fold change* of the original expression values, and
exponentiating the intercept gives the geometric mean expression of the reference group (grade 1,
node 0). This is why the tutorial computes `2^fit$coef` and `2^confint(fit)` rather than reading the
raw coefficients: $2^{\hat\beta_0}$ is a geometric mean expression level, $2^{\hat\beta_{g3}}$ is how
many times higher expression is in grade 3 than grade 1 (at node 0), and so on. A negative exponent,
$2^{-\hat\beta_{g3n1}}$, reads as "how many times *lower*" — used here because the tutorial states
the interaction as the grade fold change being lower in node-1 patients than in node-0 patients,
which is the reciprocal of the ratio computed above.

`ExploreModelMatrix::VisualizeDesign` is used at this point to display the design (model) matrix for
`gene ~ grade * node` directly — a way of checking, before trusting the numbers, exactly which linear
combination of coefficients corresponds to which group mean, which is precisely the correspondence
worked out above.

## Turning questions into contrasts

Only two of the four group comparisons are single model coefficients ($\beta_{g3}$ and $\beta_{n1}$,
the comparisons at node 0 and at grade 1 respectively). The other two, and the interaction itself,
are *linear combinations* of coefficients — a hypothesis about such a combination is called a
**contrast**. Testing a contrast needs its own standard error, because the coefficients involved are
correlated; that is why the tutorial does not simply add two numbers read off the summary table, but
forms the contrasts explicitly and evaluates them together with the `multcomp` package:

| Question | Contrast | Hypothesis |
|---|---|---|
| Grade effect at node 0 | `grade3` | $H_0: \beta_{g3}=0$ |
| Grade effect at node 1 | `grade3 + grade3:node1` | $H_0: \beta_{g3}+\beta_{g3n1}=0$ |
| Node effect at grade 1 | `node1` | $H_0: \beta_{n1}=0$ |
| Node effect at grade 3 | `node1 + grade3:node1` | $H_0: \beta_{n1}+\beta_{g3n1}=0$ |
| Interaction | `grade3:node1` | $H_0: \beta_{g3n1}=0$ |

`glht` (generalised linear hypotheses) fits all five contrasts from the same model in one call and
corrects the five resulting p-values for multiple testing, since answering the biological question
means asking all five, and none of them was singled out in advance — exactly the setting in which a
multiplicity correction is needed.

## What the contrasts show

Putting the five tests together answers the questions the tutorial opened with:

- The grade effect is extremely significant in **both** node strata ($p \ll 0.001$ at node 0 and at
  node 1): grade-3 tumours show higher KPNA2 expression than grade-1 tumours regardless of node
  status, though — see below — not by the same amount.
- The node effect is significant among grade-1 tumours (affected lymph nodes go with higher
  expression), but **not** significant among grade-3 tumours: node status matters for grade-1
  tumours and stops mattering for grade-3 tumours.
- The interaction is significant: the grade-3-vs-grade-1 fold change is smaller in patients with
  affected lymph nodes than in patients with unaffected lymph nodes. Equivalently (same coefficient,
  same test), the node-1-vs-node-0 fold change is smaller in grade-3 tumours than in grade-1 tumours.
  This is the numerical form of the pattern in the figure above: the two lines are not parallel, and
  the gap between them narrows going from grade 1 to grade 3.

The overall `Anova(type="III")` test and the individual `grade3:node1` contrast are two routes to the
same conclusion — the omnibus test says *some* interaction effect is present, and the contrast pins
down which one, giving it a size and a confidence interval on the fold-change scale.

## Sources

- `multipleRegression_KPNA2/01-data-analysis.md` — the KPNA2/breast-cancer background, the
  grade-by-node data-exploration plot, the residual diagnostics motivating the $\log_2$ transform,
  the `Anova(type="III")` interaction test, and the five research questions.
- `multipleRegression_KPNA2/02-interpretation-of-model-parameters-and-statistical-tests.md` — the
  model equation, the correspondence between coefficients and group means/fold changes,
  `ExploreModelMatrix::VisualizeDesign`, and the five contrasts evaluated with `multcomp::glht`.
- `multipleRegression_KPNA2/03-conclusion.md` — the stated conclusions for each of the five
  hypotheses.

All three are sections of a single worked tutorial, "Breastcancer Gene Expression Study: KPNA2
gene", from the StatOmics *Statistical Genomics* (SGA21) course (CC BY-NC-SA 4.0). The tutorial's
R Markdown source computes exact fold-change values, confidence intervals and p-values through
inline, unevaluated R expressions (`` `r round(...)` ``, `` `r format(...)` ``); those expressions
were never knitted in the converted material, so the precise numbers are not reproduced here — only
the direction and significance the surrounding prose states directly.

---

[← 16. Mass Spectrometry Basics for Proteomics](16-mass-spectrometry-basics-for-proteomics.md) · [Contents](index.md) · [18. Import Data and Preprocessing →](18-import-data-and-preprocessing.md)
