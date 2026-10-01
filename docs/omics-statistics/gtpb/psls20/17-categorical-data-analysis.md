---
title: "17. Categorical Data Analysis"
course: "GTPB Psls20"
chapter: 17
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Categorical Data Analysis

## What this covers

Every model so far in this course has had a continuous response. This chapter turns to a
categorical one: a count, a yes/no outcome, a genotype. It answers four related questions — is a
single proportion different from a reference value, are two *paired* proportions different, are two
*unpaired* (independent-sample) proportions different, and how do we bring a categorical or
continuous predictor to bear on a binary outcome in one model. It assumes the standard hypothesis
testing toolkit (null and alternative hypotheses, p-values, the central limit theorem, confidence
intervals) and, for the last section, familiarity with how a linear model and its ANOVA/F-test work
for a continuous response — logistic regression reuses that machinery on a different scale.

## The Bernoulli and binomial models

Take a binary outcome $X$: $X=1$ for a "success" (a boy is born, an event occurs), $X=0$ otherwise.
This is modelled with the **Bernoulli distribution**,
$$X_i \sim B(\pi), \qquad B(\pi) = \pi^{X_i}(1-\pi)^{1-X_i},$$
with a single parameter $\pi$. Its mean and variance are both determined by $\pi$:
$$\text{E}[X_i] = \pi, \qquad \text{Var}[X_i] = \pi(1-\pi).$$
$\pi$ is the population proportion of successes, and the natural estimator from a sample of $n$
independent draws is the sample mean,
$$\hat\pi = \bar X = \frac{1}{n}\sum_{i=1}^n X_i.$$

The running example is the **Saksen study**: a closed population (little migration) in which 3175
of 6155 unborn children observed were boys. Is the probability of a male birth really $1/2$?

Working with $\bar X$ directly is awkward, so instead work with the **sum** $S = n\bar X$, the total
number of successes. Its distribution follows from counting: with two independent children, each
of the four outcomes $(0,0),(0,1),(1,0),(1,1)$ has probability $1/4$ under $\pi=1/2$, so the sum
$S=x_1+x_2$ takes value $0$ with probability $1/4$, value $1$ with probability $1/2$ (two ways to
get it), and value $2$ with probability $1/4$. The general pattern, for $n$ independent draws each
with success probability $\pi$, is the **binomial distribution**:
$$P(S=k) = \binom{n}{k}\pi^k(1-\pi)^{n-k}, \qquad k=0,1,\ldots,n,$$
where $\binom{n}{k} = n!/(k!(n-k)!)$ counts the number of orderings that give $k$ successes. $S$ is
binomial with parameters $n$ (number of draws) and $\pi$ (success probability per draw); this is the
model for any count built out of an underlying binary response — wild type versus mutant, infected
versus not — whenever the question is about comparing proportions or risks between groups.

## Testing a single proportion: the binomial test

For the Saksen data, $\hat\pi = 3175/6155 \approx 51.6\%$. Is that far enough from $1/2$ to reject
$$H_0: \pi = 1/2 \quad\text{vs}\quad H_1: \pi \neq 1/2\,?$$

Under $H_0$, $S$ is $\text{Binomial}(n,\pi_0)$ with $\pi_0=1/2$, so its exact distribution is known
and no approximation is needed. Let $s_0 = n\pi_0$ be the expected count under $H_0$ and
$\delta = |S - s_0|$ the observed deviation. The two-sided p-value is the total probability, under
$H_0$, of a deviation from $s_0$ at least as extreme as the one observed:
$$p = \text{P}_0\big[S \geq s_0+\delta\big] + \text{P}_0\big[S \leq s_0-\delta\big].$$
When $\pi_0 = 1/2$ the binomial distribution is symmetric, so the two tails are equal; this symmetry
breaks down for $\pi_0 \neq 1/2$, and the formula above (rather than "double one tail") is the one
that still works.

For the Saksen study, $s_0 = 6155\times 0.5 = 3077.5$ and $\delta = |3175-3077.5| = 97.5$, so the two
tail cutoffs are $s_0+\delta = 3175$ and $s_0-\delta = 2980$. Summing the binomial mass beyond each
cutoff gives $\text{P}_0[S\geq 3175] \approx 0.0067$ and $\text{P}_0[S\leq 2980]\approx 0.0067$, for
a two-sided $p \approx 0.013$. At the 5% significance level this rejects $H_0$: it is very unlikely
to see this many more boys than girls in a random sample if the two sexes were equally frequent.

<figure>
<svg viewBox="0 0 340 210" role="img" aria-label="Binomial null distribution of S with the two tails defining the two-sided p-value shaded">
  <line x1="20" y1="160" x2="325" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="325,160 316,155 316,165" fill="currentColor"/>
  <polyline points="20,158 60,150 100,120 140,60 170,40 200,60 240,120 280,150 320,158" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M20,160 L20,158 L60,150 L100,120 L100,160 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M240,160 L240,120 L280,150 L320,158 L320,160 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="170" y1="40" x2="170" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="100" y1="120" x2="100" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="240" y1="120" x2="240" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="34" text-anchor="middle" font-size="12" fill="currentColor">s0</text>
  <text x="100" y="175" text-anchor="middle" font-size="11" fill="currentColor">s0 &#8722; &#948;</text>
  <text x="240" y="175" text-anchor="middle" font-size="11" fill="currentColor">s0 + &#948; (observed)</text>
  <text x="45" y="196" text-anchor="middle" font-size="11" fill="currentColor">P(S&#8804;s0&#8722;&#948;)</text>
  <text x="300" y="196" text-anchor="middle" font-size="11" fill="currentColor">P(S&#8805;s0+&#948;)</text>
  <text x="170" y="207" text-anchor="middle" font-size="12" fill="currentColor">S (number of boys)</text>
</svg>
<figcaption>The two-sided p-value of the binomial test is the combined probability in the two tails
of the null distribution of S beyond s0&#177;&#948;; the tails are equal only when &#960;0=1/2.</figcaption>
</figure>

This test is implemented directly by `binom.test(x, n, p)` in R, and it is worth noting explicitly:
**the test for a proportion is equivalent to a one-sample t-test for binary data.**

### Confidence interval for a proportion

The standard error of $\hat\pi$ follows from $\text{Var}[X]=\pi(1-\pi)$:
$$\text{SE}_{\bar X} = \sqrt{\frac{\pi(1-\pi)}{n}}, \qquad\text{estimated by}\qquad
\widehat{\text{SE}}_{\bar X} = \sqrt{\frac{\hat\pi(1-\hat\pi)}{n}}.$$
For the Saksen data $\widehat{\text{SE}} \approx 0.0064$, and a normal-theory (CLT-based) 95% CI is
$$\hat\pi \pm 1.96\,\widehat{\text{SE}}_{\hat\pi} \approx [0.503,\ 0.528].$$
This normal approximation can be poor in small samples; `binom.test` also returns an exact interval
(via `$conf.int`) that does not rely on the CLT and should be preferred when $n$ is small.

Putting the test and the interval together: at the 5% level the gender of an unborn child in the
Saksen population is more likely to be male than female, with an estimated probability of a male
birth of about 51.6% (95% CI roughly [50.3%, 52.8%]).

## Comparing two proportions on paired data: McNemar's test

Paired binary data arise when the *same* individual is measured twice — before and after an
exposure, or under two conditions — so the analysis has to account for the pairing rather than
treating the two measurements as independent samples.

**Example.** Rogovin et al. (2017) tested whether female Campbell dwarf hamsters prefer gentle over
aggressive males, and whether that preference depends on the environment. Each female was tested
twice: once while housed in a hostile environment (high density, food shortage, competition), once
in a friendly one, each time recording whether she chose the aggressive male. The paired results for
34 females:

| | friendly: aggressive | friendly: non-aggressive |
|---|---|---|
| **hostile: aggressive** | $e=3$ | $f=17$ |
| **hostile: non-aggressive** | $g=1$ | $h=13$ |

Only the **discordant pairs** ($f$ and $g$) — where the choice differed between environments — carry
information about whether the environment matters; a female who chose the same way in both settings
contributes nothing to a *difference*. The absolute risk difference between the two environments'
probability of choosing an aggressive male is
$$\widehat{\text{ARD}} = \hat\pi_1 - \hat\pi_0 = \frac{e+f}{n} - \frac{e+g}{n} = \frac{f-g}{n},$$
with standard error
$$\text{SE}_{\widehat{\text{ARD}}} = \frac{1}{n}\sqrt{f+g - \frac{(f-g)^2}{n}}.$$
Here $\widehat{\text{ARD}} = (17-1)/34 = 0.471$ and $\text{SE} = 0.0952$, giving a 95% CI (via the
CLT) of $0.471 \pm 1.96(0.0952) = [0.284,\ 0.658]$.

**McNemar's test** targets the same discordant pairs directly. Among a random discordant pair, the
probability that it is of type $f$ (aggressive chosen in the hostile environment) rather than type
$g$ is estimated by $f/(f+g)$; under $H_0$ (environment has no effect on choice) this probability is
$1/2$, and $f$ itself is $\text{Binomial}(n=f+g, \pi=0.5)$ under $H_0$, so
$$\text{SE}_{f/(f+g)} \overset{H_0}{=} \frac{\sqrt{f+g}}{2}
\quad\Longrightarrow\quad
z = \frac{f-(f+g)/2}{\sqrt{f+g}/2} = \frac{f-g}{\sqrt{f+g}},$$
an asymptotic one-sample z-test, valid when $fg/(f+g) \geq 5$. **McNemar's test is the analogue of
the paired t-test for binary variables**, implemented as `mcnemar.test`. With only $f+g=18$
discordant pairs here the normal approximation is not ideal, so the exact test is preferred:
`binom.test(x=f, n=f+g, p=0.5)`.

Either way the conclusion is the same: partner choice is extremely significantly associated with
the environment ($p<0.001$); the probability of choosing an aggressive male is on average 47.1
percentage points higher when the female resides in a hostile environment (95% CI [28.4%, 65.8%]).

## Comparing two proportions on unpaired data

**Example.** Is a polymorphism in the *BRCA1* gene associated with breast cancer? A retrospective
case-control study genotyped 800 breast cancer cases and 572 controls at the Pro/Leu locus:

| Genotype | Controls | Cases | Total |
|---|---|---|---|
| Pro/Pro | 266 ($a$) | 342 ($d$) | 608 |
| Pro/Leu | 250 ($b$) | 369 ($e$) | 619 |
| Leu/Leu | 56 ($c$) | 89 ($f$) | 145 |
| **Total** | 572 | 800 | 1372 |

Because this is a **case-control** design, the number of cases and controls was fixed by the
investigator rather than reflecting how common breast cancer actually is in the population, so risks
and risk *differences* for the disease cannot be estimated directly from these data. What can be
compared is the proportion carrying Leu/Leu among cases versus controls: $\hat\pi_1 = f/(d+e+f) =
89/800 = 11.1\%$ among cases and $\hat\pi_0 = c/(a+b+c) = 56/572 = 9.8\%$ among controls, a relative
risk of exposure of $11.1/9.8 = 1.14$. That says the Leu/Leu genotype is 14% more common among cases
than controls — but it does not directly say how much higher the risk of *breast cancer* is for
Leu/Leu carriers, since it conditions on disease status rather than on genotype.

The **odds**, $\text{Odds} = p/(1-p)$, resolves this. Odds range over $(1,\infty)$... more precisely
over $(0,\infty)$, equal $1$ exactly when $p=1/2$, and increase with $p$ — the usual "how much more
likely to win than lose" from gambling. Here the odds on Leu/Leu are $f/(d+e) = 89/711 = 0.125$
among cases and $c/(a+b) = 56/516 = 0.109$ among controls, giving an **odds ratio**
$$\text{OR}_{\text{Leu/Leu}} = \frac{f/(d+e)}{c/(a+b)} = 1.15.$$
The odds ratio is a **symmetric** statistic: algebraically,
$\text{OR}_{\text{Leu/Leu}} = \frac{f(a+b)}{c(d+e)}$ is exactly the same expression that would be
obtained for the *disease* odds ratio, $\text{OR}_{\text{case}} = \frac{f/c}{(d+e)/(a+b)}$, had the
study instead sampled at random from the population. So even though the case-control design rules
out estimating absolute risks, the odds ratio for breast cancer given Leu/Leu versus other genotypes
*can* be estimated from it, and equals 1.15: the odds of breast cancer are 15% higher for women with
the Leu/Leu genotype. This is exactly why the odds ratio, not the risk ratio, is the standard summary
for a case-control study.

### Pearson's chi-square test for independence

Whether that 15% is more than sampling noise is answered by testing association in the 2$\times$2
table (Leu/Leu vs. other genotype, by case/control status):

| | Controls | Cases | Total |
|---|---|---|---|
| other | 516 | 711 | 1227 |
| Leu/Leu | 56 | 89 | 145 |
| **Total** | 572 | 800 | 1372 |

$$H_0: \text{no association between genotype } X \text{ and outcome } Y \quad\text{vs}\quad
H_1: X \text{ and } Y \text{ are associated}.$$

The row and column totals describe only the *marginal* distributions of $X$ and $Y$ separately, not
their association. Under $H_0$ (independence), the expected count in cell $(i,j)$ is
$$E_{ij} = \frac{(\text{row total}_i)(\text{column total}_j)}{n},$$
and the test statistic compares observed to expected counts across all four cells:
$$X^2 = \sum_{ij} \frac{\big(|O_{ij}-E_{ij}| - 0.5\big)^2}{E_{ij}} \overset{H_0}{\longrightarrow} \chi^2_{df=1}.$$
The subtraction of $0.5$ is a **continuity correction** (Yates' correction), needed because $O_{ij}$
is discrete while the $\chi^2_1$ distribution is continuous; omitting it gives the plain **Pearson
chi-squared test**. A large $X^2$ counts against $H_0$: reject at level $\alpha$ when $X^2$ exceeds
the $(1-\alpha)$-quantile of $\chi^2_1$, and the p-value is $P_0[\chi^2_1 \geq x^2]$. Both versions
are available via `chisq.test(table, correct = TRUE/FALSE)`.

Even with the correction, the $\chi^2_1$ approximation is only trustworthy when **no expected cell
count under $H_0$ falls below 5**. When that fails, use **Fisher's exact test** instead
(`fisher.test`), which tests the same hypotheses without relying on the large-sample approximation.

### Extension to $r\times c$ tables

The same logic extends to a categorical predictor and/or outcome with more than two levels: with $r$
row categories and $c$ column categories,
$$X^2 = \sum_{ij} \frac{(O_{ij}-E_{ij})^2}{E_{ij}} \overset{H_0}{\longrightarrow} \chi^2_{(r-1)(c-1)}$$
(no continuity correction here). This is **Pearson's $\chi^2$ test**, the categorical analogue of
one-way ANOVA. Applying it to the full $3\times 2$ genotype table (Pro/Pro, Pro/Leu, Leu/Leu by
case/control) via `chisq.test`, the conclusion at the 5% level is that the *BRCA1* variant is **not**
significantly associated with breast cancer overall — a different question, and a different answer,
from the 2$\times$2 comparison restricted to Leu/Leu versus the rest.

## Logistic regression

The chi-square and odds-ratio machinery above tests and quantifies association for a single
categorical predictor. **Logistic regression** generalises this to a full regression framework for a
binary outcome, allowing continuous and/or categorical (dummy-coded) predictors together, in direct
analogy to how ANOVA and linear regression share one linear-model framework for continuous outcomes.
Observations are assumed independent Bernoulli, and it is the *log-odds* — not the probability
itself — that is modelled linearly:
$$Y_i \sim B(\pi_i), \qquad \log\frac{\pi_i}{1-\pi_i} = \beta_0 + \beta_1 X_{i1} + \cdots + \beta_p X_{ip}.$$
Modelling the log-odds rather than $\pi_i$ directly is what keeps the fitted probability inside
$(0,1)$ automatically, however large or small the linear predictor becomes — the exponential/logistic
transform back to $\pi_i$ saturates at 0 and 1 rather than running off to $\pm\infty$.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Logistic curve mapping an unbounded linear predictor to a fitted probability between 0 and 1">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="170" x2="30" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="20" x2="300" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <path d="M40,158 C90,155 140,155 165,100 C190,45 240,42 290,40" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="165" y1="95" x2="165" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="30" y1="95" x2="165" y2="95" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="18" y="24" text-anchor="end" font-size="11" fill="currentColor">1</text>
  <text x="18" y="174" text-anchor="end" font-size="11" fill="currentColor">0</text>
  <text x="18" y="99" text-anchor="end" font-size="11" fill="currentColor">0.5</text>
  <text x="165" y="184" text-anchor="middle" font-size="12" fill="currentColor">linear predictor (&#946;0+&#946;1x)</text>
  <text x="12" y="95" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 12 95)">&#960;</text>
</svg>
<figcaption>The logit link folds an unbounded linear predictor into a fitted probability between 0
and 1 &#8212; the S-shaped curve underlying the beetle dose-mortality model below.</figcaption>
</figure>

### Categorical predictor: BRCA1 revisited

A $k$-level factor needs $k-1$ dummy variables, exactly as in ANOVA. For the three *BRCA1* genotypes,
with Pro/Pro as reference:
$$x_{i1} = \mathbb{1}[\text{Pro/Leu}], \qquad x_{i2} = \mathbb{1}[\text{Leu/Leu}], \qquad
\log\frac{\pi_i}{1-\pi_i} = \beta_0+\beta_1 x_{i1}+\beta_2 x_{i2}.$$
The intercept is the log-odds of cancer in the reference group, and each slope is a log **odds
ratio** against the reference:
$$\log\text{ODDS}_{\text{Pro/Pro}}=\beta_0,\quad
\log\text{ODDS}_{\text{Pro/Leu}}=\beta_0+\beta_1,\quad
\log\text{ODDS}_{\text{Leu/Leu}}=\beta_0+\beta_2,$$
$$\log\frac{\text{ODDS}_{\text{Pro/Leu}}}{\text{ODDS}_{\text{Pro/Pro}}}=\beta_1, \qquad
\log\frac{\text{ODDS}_{\text{Leu/Leu}}}{\text{ODDS}_{\text{Pro/Pro}}}=\beta_2,$$
so the fitted coefficients translate directly into odds and odds ratios. The overall (omnibus) test
of whether genotype matters at all is a likelihood-ratio chi-square test (`anova(model, test =
"Chisq")`), which — as it should, since both are testing the same association — gives a p-value very
close to the Pearson chi-square test on the contingency table, and again does not reach significance
here. Had it been significant, pairwise post-hoc comparisons (e.g. Tukey-adjusted via `glht`) would
identify which specific odds ratios differ from 1, with confidence intervals computed on the
log-odds-ratio scale and then exponentiated back to odds ratios. As a check, the resulting
Leu/Leu-vs-Pro/Pro odds ratio recovers the value computed by hand from the raw table,
$\text{OR} = \frac{89 \times 266}{56 \times 342} \approx 1.24$ — logistic regression is reproducing
the contingency-table analysis, not replacing it with something different. This inference relies on
large-sample (asymptotic) theory throughout, unlike the exact binomial and Fisher tests above.

### Continuous predictor: beetle mortality

**Example.** Does the concentration of carbon disulfide (CS$_2$) affect beetle mortality? In 32
independent trials, one beetle was exposed to one of eight CS$_2$ concentrations and scored as dead
($y=1$) or alive ($y=0$). The model is
$$\log\frac{\pi_i}{1-\pi_i} = \beta_0 + \beta_1 x_i, \qquad x_i = \text{dose}.$$
The fitted intercept is very negative ($\approx -53.2$), i.e. essentially zero odds of mortality at
dose zero — but this is a large extrapolation, since the lowest dose actually tested in the data is
well above zero. The fitted slope gives an odds ratio of $\exp(0.3013) = 1.35$ per unit increase in
dose: a beetle exposed to 1 mg/l more CS$_2$ than another has, on average, 1.35 times the odds of
dying. The effect is highly significant, and the fitted probability curve — the sigmoid of the
figure above, evaluated along the dose range — rises from near 0 to near 1 across the tested
concentrations, tracking the observed proportion dead at each dose.

## Sources

- Bernoulli/binomial setup, the Saksen boy/girl example, the binomial test for a single proportion,
  and the CI on a proportion:
  `docs/omics-statistics/gtpb/psls20/theory/10-categoricalDataAnalysis/01-test-for-a-proportion.md`.
- Paired data, the hamster mate-choice example, absolute risk difference and McNemar's test:
  `docs/omics-statistics/gtpb/psls20/theory/10-categoricalDataAnalysis/02-test-for-association-between-two-qualitative-variables.md`.
- Unpaired data, the BRCA1 case-control example, odds/odds ratios, and Pearson's chi-square/Fisher's
  exact test (2x2 and r x c):
  `docs/omics-statistics/gtpb/psls20/theory/10-categoricalDataAnalysis/03-unpaired-observations.md`.
- Logistic regression, both the categorical (BRCA1) and continuous (beetle CS2) predictor cases:
  `docs/omics-statistics/gtpb/psls20/theory/10-categoricalDataAnalysis/04-logistic-regression.md`.

All four files are split sections of a single source, `theory/10-categoricalDataAnalysis.Rmd` from
the GTPB "Practical Statistics for the Life Sciences" 2020 course (CC BY 4.0); no separate slide
deck, transcript, or problem set was supplied for this chapter. The source is an unrendered R
Markdown file, so numeric results quoted here that appear in it only as inline R code (not as typed
prose) were recomputed directly from the stated raw counts to match the described method; results
that appear as typed conclusions in the source are quoted as given.

---

[← 16. Kruskal-Wallis Test for Groups](16-kruskal-wallis-test-for-groups.md) · [Contents](index.md) · [18. One-Way ANOVA on Cuckoo Eggs →](18-one-way-anova-on-cuckoo-eggs.md)
