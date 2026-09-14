---
title: Regression Adjustments
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/36-adjustments/slides.html
source_file: sources/berkeley-stat158/spring-2026/36-adjustments/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Regression Adjustments

**Source:** [`36-adjustments/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/36-adjustments/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Meadowfoam

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
meadowfoam
```

    # A tibble: 24 × 3
       flowers time  intensity
         <dbl> <chr>     <dbl>
     1    62.3 late        150
     2    77.4 late        150
     3    55.3 late        300
     4    54.2 late        300
     5    49.6 late        450
     6    61.9 late        450
     7    39.4 late        600
     8    45.7 late        600
     9    31.3 late        750
    10    44.9 late        750
    # ℹ 14 more rows

Let’s say that only `time` was randomly assigned and `intensity` was another variable that was recorded that we know is a good predictor of `flowers`.

## What we’ve been doing

Since `time` is the only experimental factor, we would fit this model:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
options(contrasts=c("contr.sum","contr.poly"))
m1 <- lm(flowers ~ time, data = meadowfoam)
summary(m1)$coef
```

                 Estimate Std. Error   t value     Pr(>|t|)
    (Intercept) 56.137500   2.556552 21.958286 1.874990e-16
    time1        6.079166   2.556552  2.377877 2.652621e-02

## Adjust for intensity

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
m_full <- lm(flowers ~ intensity + time, data = meadowfoam)
m_no_time <- lm(flowers ~ intensity, data = meadowfoam)
summary(m_full)$coef
```

                   Estimate Std. Error   t value     Pr(>|t|)
    (Intercept) 77.38500017 2.99815637 25.810862 2.166375e-17
    intensity   -0.04047143 0.00513237 -7.885525 1.036787e-07
    time1        6.07916641 1.31477854  4.623719 1.463777e-04

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
summary(m_no_time)$coef
```

                   Estimate  Std. Error   t value     Pr(>|t|)
    (Intercept) 77.38500017 4.161186173 18.596861 6.059011e-15
    intensity   -0.04047143 0.007123293 -5.681562 1.029503e-05

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova(m_no_time, m_full)
```

    Analysis of Variance Table

    Model 1: flowers ~ intensity
    Model 2: flowers ~ intensity + time
      Res.Df     RSS Df Sum of Sq      F    Pr(>F)
    1     22 1758.19
    2     21  871.24  1    886.95 21.379 0.0001464 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

## Cautions

When fitting regression models to experimental data:

1.  Non-experimental variables have no causal interpretation.

2.  Regression adjustments generally should not be used in very small datasets (<span class="math inline">\$N &lt; 20\$</span>) because df are better spent estimating causal effects.

---

[← Study: Meadowfoam](02-study-meadowfoam.md) · [Up: contents](index.md) · [Collinearity →](04-collinearity.md)
