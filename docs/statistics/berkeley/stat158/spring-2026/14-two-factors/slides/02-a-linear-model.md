---
title: A Linear Model
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/14-two-factors/slides.html
source_file: sources/berkeley-stat158/spring-2026/14-two-factors/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# A Linear Model

**Source:** [`14-two-factors/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/14-two-factors/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Babies Walking

## A linear model

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
m1 <- lm(walk ~ program, data = babies)
summary(m1)
```


    Call:
    lm(formula = walk ~ program, data = babies)

    Residuals:
       Min     1Q Median     3Q    Max
      -2.4   -0.7   -0.2    0.7    2.8

    Coefficients:
                         Estimate Std. Error t value Pr(>|t|)
    (Intercept)           10.2000     0.5831  17.493 7.46e-12 ***
    programRegular         0.4000     0.8246   0.485   0.6342
    programWeekly report   1.2000     0.8246   1.455   0.1649
    programSingle report   1.8000     0.8246   2.183   0.0443 *
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 1.304 on 16 degrees of freedom
    Multiple R-squared:  0.2639,    Adjusted R-squared:  0.1258
    F-statistic: 1.912 on 3 and 16 DF,  p-value: 0.1684

The first level of the factor is the benchmark.

## Applying the zero sum constraint

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
options(contrasts = c("contr.sum", "contr.poly"))
m2 <- lm(walk ~ program, data = babies)
summary(m2)
```


    Call:
    lm(formula = walk ~ program, data = babies)

    Residuals:
       Min     1Q Median     3Q    Max
      -2.4   -0.7   -0.2    0.7    2.8

    Coefficients:
                Estimate Std. Error t value Pr(>|t|)
    (Intercept)  11.0500     0.2915  37.901   <2e-16 ***
    program1     -0.8500     0.5050  -1.683    0.112
    program2     -0.4500     0.5050  -0.891    0.386
    program3      0.3500     0.5050   0.693    0.498
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 1.304 on 16 degrees of freedom
    Multiple R-squared:  0.2639,    Adjusted R-squared:  0.1258
    F-statistic: 1.912 on 3 and 16 DF,  p-value: 0.1684

---

[← Designs with Two Factors](01-designs-with-two-factors.md) · [Up: contents](index.md) · [Study: Battery Lifetime →](03-study-battery-lifetime.md)
