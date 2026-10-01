---
title: "36. Confounding and Multiple Regression"
course: "GTPB Psls20"
chapter: 36
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 36. Confounding and Multiple Regression

## What this covers

This chapter works through a single worked example — the FEV (forced expiratory volume) dataset
used in the PSLS20 course — to show two things at once: how a two-group comparison can have the
*wrong sign* because of a confounding variable, and how a multiple linear regression, built up and
then pruned by forward selection, recovers the correct effect. It assumes the reader already knows
simple linear regression (`lm()`, one predictor, reading a residual plot) and can read a boxplot and
a scatterplot matrix; it does not re-derive least squares or the mechanics of the $F$-test.

## The data and the question

The dataset records FEV — how much air a child can force out of their lungs, in litres — for 606
children aged 6 to 17, together with each child's `age`, `height`, `gender`, and `smoking` status
(smoker or non-smoker). The question the analysis is built to answer is simple to state and, as it
turns out, easy to get backwards: **does smoking affect FEV in children?**

## Tidying before looking

Two small changes to the raw table matter before any plotting starts:

```r
fev <- fev %>%
  mutate(gender = as.factor(gender)) %>%
  mutate(smoking = as.factor(smoking)) %>%
  mutate(height_cm = height * 2.54)
```

`gender` and `smoking` are recoded as factors rather than left as numeric or character codes, so
that R treats them as categories in a model rather than as quantities to be added and averaged.
`height`, recorded in inches, gets a second column `height_cm` — purely a matter of the units the
audience thinks in, not something that changes any later analysis.

## A marginal comparison with the wrong sign

A scatterplot matrix of `log(fev)`, `age`, `height_cm`, `gender` and `smoking` shows strong pairwise
associations everywhere: age with height, age with FEV, height with FEV, gender with height, gender
with FEV. That density of correlation is the warning sign for what follows.

Plotted on its own, FEV by smoking status looks like smokers have **higher** FEV than non-smokers —
the opposite of what smoking should do to lung function. The explanation is not in the smoking
variable at all: a boxplot of age against smoking shows that the smokers in this sample are
concentrated among the *older* children (unsurprisingly — very few of the six-year-olds smoke). Age
on its own drives FEV up sharply, so a group that is disproportionately older will show a higher
average FEV for that reason alone, regardless of any effect of smoking itself. Age here is a
**confounder**: it affects both whether a child is recorded as a smoker and what their FEV is, so a
comparison that does not hold it fixed attributes age's effect to smoking.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Schematic scatter of FEV against age, showing smokers concentrated at older ages and sitting below the age trend, yet averaging higher than non-smokers overall">
  <rect x="165" y="20" width="145" height="180" fill="firebrick" fill-opacity="0.08"/>
  <line x1="40" y1="200" x2="310" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="200" x2="40" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="175" y="215" text-anchor="middle" font-size="12" fill="currentColor">age</text>
  <text x="14" y="110" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 14 110)">FEV</text>
  <polyline points="50,175 70,165 90,155 110,145 130,135 150,125 170,115 190,108 210,100 230,92 250,85 270,78 290,70"
            fill="none" stroke="currentColor" stroke-width="1" stroke-opacity="0.45"/>
  <g fill="currentColor">
    <circle cx="50" cy="175" r="3"/><circle cx="70" cy="165" r="3"/><circle cx="90" cy="155" r="3"/>
    <circle cx="110" cy="145" r="3"/><circle cx="130" cy="135" r="3"/><circle cx="150" cy="125" r="3"/>
    <circle cx="170" cy="115" r="3"/><circle cx="190" cy="108" r="3"/><circle cx="210" cy="100" r="3"/>
    <circle cx="230" cy="92" r="3"/><circle cx="250" cy="85" r="3"/><circle cx="270" cy="78" r="3"/>
    <circle cx="290" cy="70" r="3"/>
  </g>
  <g fill="firebrick">
    <circle cx="175" cy="125" r="3.5"/><circle cx="195" cy="118" r="3.5"/><circle cx="215" cy="110" r="3.5"/>
    <circle cx="235" cy="102" r="3.5"/><circle cx="255" cy="95" r="3.5"/><circle cx="275" cy="88" r="3.5"/>
    <circle cx="290" cy="82" r="3.5"/>
  </g>
  <circle cx="250" cy="35" r="3" fill="currentColor"/>
  <text x="258" y="39" font-size="11" fill="currentColor">non-smoker</text>
  <circle cx="250" cy="52" r="3.5" fill="firebrick"/>
  <text x="258" y="56" font-size="11" fill="firebrick">smoker</text>
</svg>
<figcaption>Schematic of the confound: FEV rises with age for everyone (the faint trend line). Smokers
(shaded band) appear only at the older ages, and each smoker sits below the trend for their own age —
the true, negative effect. But because the whole smoker group is shifted toward ages where FEV is
naturally high, its unadjusted average FEV comes out above the non-smokers' average, reversing the
sign. This is the pattern the FEV data actually shows.</figcaption>
</figure>

The fix is visible as soon as the comparison is stratified: a boxplot of FEV against age (treated as
a factor), coloured by smoking status and split into panels by gender, reverses the picture
completely — within an age-and-gender stratum, smokers now show *lower* FEV, as expected. Holding
age, height and gender fixed while comparing smokers to non-smokers is exactly what a multiple
regression does automatically, for every combination of the covariates at once, rather than one
stratum at a time.

## Building the regression model

The response is `log(fev)`, not `fev` — the log transform is needed to meet the assumptions of
linear regression for this outcome (this is asserted in the exercise as the modelling starting
point, not derived here). The starting model includes every plausible covariate and every two-way
interaction between them:

```r
full_formula <- log(fev) ~ age + height_cm + smoking + gender +
  smoking:age + smoking:height_cm + smoking:gender +
  age:height_cm + age:gender + height_cm:gender

lm_full <- lm(full_formula, data = fev)
```

Before trusting anything about individual terms in this model, two checks matter. First,
`table(fev$gender, fev$smoking)` — a check that every combination of gender and smoking status is
represented by enough children, since an interaction term is meaningless if one of its cells is
nearly empty. Second, the variance inflation factor, `car::vif()`, on the fitted model: age, height
and gender are themselves strongly correlated (the scatterplot matrix already showed this), and once
correlated predictors and their interactions sit in the same model, the individual coefficient
$p$-values become unreliable even where the model as a whole fits well. VIF quantifies how much a
coefficient's variance is inflated by its correlation with the other predictors in the model, and is
the standard diagnostic for this.

## Pruning the model: forward selection

Rather than trimming the full interaction model term by term, the exercise builds it up from
nothing, adding one term at a time. Starting from the empty (intercept-only) model, `add1()` tests,
for every candidate term still outside the model, whether adding it improves the fit significantly
(by an $F$-test comparing the two nested models):

```r
subfev <- fev[, -3]                    # drop height in inches, keep height_cm
m1 <- lm(log(fev) ~ 1, subfev)         # empty model
add1(m1, scope = full_formula, data = subfev, test = "F")
```

The procedure, run against the same `full_formula` scope at each step:

1. From the empty model, **height_cm** has the most significant contribution (lowest AIC, most
   significant $F$-test) — add it.
2. With height_cm in the model, **age** is now the most significant addition — add it.
3. With height_cm and age in the model, **smoking** is again significant — add it.
4. With height_cm, age and smoking all in the model, none of the remaining candidates — including
   `gender` and every two-way interaction in the scope — reaches significance at the 5% level.
   Selection stops here.

The model forward selection settles on is

$$y_i = \beta_0 + \beta_a x_{ia} + \beta_h x_{ih} + \beta_{s1} x_{is1} + \epsilon_i,$$

a main-effects-only model in age ($a$), height ($h$) and smoking ($s$), with no gender term and no
interactions surviving.

## Checking the assumptions

The selected model is refit and its diagnostic plots examined:

```r
lm_full <- lm(log(fev) ~ age + height_cm + smoking, data = fev)
plot(lm_full)
```

Four assumptions are checked, each against one of the standard `plot.lm` panels:

1. **Independence of observations** — judged met: children who are similar in age, height and
   smoking status will tend to have more similar FEV, but that similarity is exactly what age,
   height and smoking as predictors already account for, so it does not show up as dependence in
   what is left over (the residuals).
2. **Linearity** between the response and the predictors — met, from the residuals-versus-fitted
   plot.
3. **Normality** of the residuals — met, from the normal Q–Q plot.
4. **Homoscedasticity** (constant residual variance) — met, from the scale–location plot.

With all four judged acceptable, the coefficients of this model can be read as estimates of the
effect of each predictor, holding the others fixed.

## Reading the final model

```r
Anova(lm_full, type = 3)
coefficients(lm_full)
confint(lm_full)
```

- **Age.** Adjusting for height and smoking, log FEV increases with age; the 95% confidence
  interval for the age coefficient is $[0.0173,\ 0.0317]$, and the effect is highly significant
  ($p = 6.0\times10^{-11}$).
- **Height.** Adjusting for age and smoking, log FEV increases with height (in cm); the 95%
  confidence interval is $[0.0156,\ 0.0183]$, again highly significant ($p < 2.2\times10^{-16}$).
- **Smoking.** Adjusting for age and height, log FEV is *lower* for smokers than non-smokers; the
  95% confidence interval, $[-0.0965,\ -0.0138]$, lies entirely below zero, and the effect is
  significant at the 5% level ($p = 0.009$).

That last line is the payoff of the whole exercise: once age and height are held fixed, smoking's
association with FEV flips sign relative to the naive, unadjusted comparison at the start of the
chapter. The multiple regression does not just add covariates for completeness — it is what
recovers the direction of the effect the marginal comparison got wrong.

## Sources

- Both source files are from the GTPB PSLS20 course, "Multiple regression: FEV" exercise
  (`tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd`, CC BY 4.0):
  - Data description, tidying steps, and the exploratory plots showing the age/smoking confound —
    `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2/01-data-tidying.md`.
  - The full interaction model, VIF check, forward selection, assumption checks and the final
    coefficient interpretation —
    `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2/02-analysis.md`.
- The exercise text refers to an earlier file, `Data_exploration_FEV.Rmd`, where the same
  "smokers look higher on FEV" pattern was first noticed by plotting FEV against smoking alone;
  that file was not supplied as input to this chapter.
- The analysis file's script also contains a fragment computing marginal effects with the `margins`
  package against a subset called `fev_11_15`, which is neither defined nor explained in the
  supplied material, and is omitted here for that reason.

---

[← 35. Linear Regression on the FEV Dataset](35-linear-regression-on-the-fev-dataset.md) · [Contents](index.md) · [37. Multiple Regression and Confounding: FEV →](37-multiple-regression-and-confounding-fev.md)
