---
title: Model-Based Inference
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/25-random-effects-models/slides.html
source_file: sources/berkeley-stat158/spring-2026/25-random-effects-models/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Model-Based Inference

**Source:** [`25-random-effects-models/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/25-random-effects-models/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## The Data

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
midterms_long
```

    # A tibble: 148 × 5
       student format question section score
       <fct>   <chr>  <chr>    <fct>   <dbl>
     1 1       C      Q21      101         6
     2 1       S      Q23      101         6
     3 2       C      Q21      101         4
     4 2       S      Q23      101         6
     5 3       S      Q21      101         6
     6 3       C      Q23      101         6
     7 4       S      Q21      101         6
     8 4       C      Q23      101         4
     9 5       S      Q21      101         6
    10 5       C      Q23      101         6
    # ℹ 138 more rows

## Model 1: Ignore (almost) all structure

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
m1 <- lm(score ~ format, data = midterms_long)
summary(m1)
```


    Call:
    lm(formula = score ~ format, data = midterms_long)

    Residuals:
        Min      1Q  Median      3Q     Max
    -5.0811 -1.0811  0.9189  1.2162  1.2162

    Coefficients:
                Estimate Std. Error t value Pr(>|t|)
    (Intercept)   4.7838     0.1866  25.641   <2e-16 ***
    formatS       0.2973     0.2638   1.127    0.262
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 1.605 on 146 degrees of freedom
    Multiple R-squared:  0.008621,  Adjusted R-squared:  0.001831
    F-statistic:  1.27 on 1 and 146 DF,  p-value: 0.2617

## Model 2: Add question and section effects

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
m2 <- lm(score ~ format + question + section, data = midterms_long)
summary(m2)
```


    Call:
    lm(formula = score ~ format + question + section, data = midterms_long)

    Residuals:
        Min      1Q  Median      3Q     Max
    -4.9474 -0.9474  0.7860  1.0833  1.3806

    Coefficients:
                Estimate Std. Error t value Pr(>|t|)
    (Intercept)   4.9167     0.2663  18.461   <2e-16 ***
    formatS       0.2973     0.2645   1.124    0.263
    questionQ23  -0.2973     0.2645  -1.124    0.263
    section102    0.0307     0.2646   0.116    0.908
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 1.609 on 144 degrees of freedom
    Multiple R-squared:  0.01733,   Adjusted R-squared:  -0.003138
    F-statistic: 0.8467 on 3 and 144 DF,  p-value: 0.4705

## Model 3: Add student effects

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
m3 <- lm(score ~ format + question + section + student, data = midterms_long)
summary(m3)
```


    Call:
    lm(formula = score ~ format + question + section + student, data = midterms_long)

    Residuals:
        Min      1Q  Median      3Q     Max
    -2.2973 -0.2973  0.0000  0.2973  2.2973

    Coefficients: (1 not defined because of singularities)
                  Estimate Std. Error t value Pr(>|t|)
    (Intercept)  6.000e+00  8.590e-01   6.985 1.18e-09 ***
    formatS      2.973e-01  1.971e-01   1.509  0.13578
    questionQ23 -2.973e-01  1.971e-01  -1.509  0.13578
    section102  -2.862e-15  1.199e+00   0.000  1.00000
    student2    -1.000e+00  1.199e+00  -0.834  0.40692
    student3    -9.658e-16  1.199e+00   0.000  1.00000
    student4    -1.000e+00  1.199e+00  -0.834  0.40692
    student5    -1.739e-15  1.199e+00   0.000  1.00000
    student6    -1.000e+00  1.199e+00  -0.834  0.40692
    student7    -1.307e-15  1.199e+00   0.000  1.00000
    student8    -2.000e+00  1.199e+00  -1.668  0.09957 .
    student9    -3.795e-16  1.199e+00   0.000  1.00000
    student10   -3.000e+00  1.199e+00  -2.503  0.01460 *
    student11   -1.166e-15  1.199e+00   0.000  1.00000
    student12   -6.805e-16  1.199e+00   0.000  1.00000
    student13   -3.000e+00  1.199e+00  -2.503  0.01460 *
    student14   -1.000e+00  1.199e+00  -0.834  0.40692
    student15   -8.830e-16  1.199e+00   0.000  1.00000
    student16   -1.000e+00  1.199e+00  -0.834  0.40692
    student17   -1.000e+00  1.199e+00  -0.834  0.40692
    student18   -1.329e-15  1.199e+00   0.000  1.00000
    student19   -2.000e+00  1.199e+00  -1.668  0.09957 .
    student20   -2.868e-15  1.199e+00   0.000  1.00000
    student21   -3.000e+00  1.199e+00  -2.503  0.01460 *
    student22   -5.878e-16  1.199e+00   0.000  1.00000
    student23   -2.000e+00  1.199e+00  -1.668  0.09957 .
    student24   -7.210e-16  1.199e+00   0.000  1.00000
    student25   -1.430e-15  1.199e+00   0.000  1.00000
    student26   -4.000e+00  1.199e+00  -3.337  0.00134 **
    student27   -1.000e+00  1.199e+00  -0.834  0.40692
    student28   -2.000e+00  1.199e+00  -1.668  0.09957 .
    student29   -1.000e+00  1.199e+00  -0.834  0.40692
    student30   -1.000e+00  1.199e+00  -0.834  0.40692
    student31   -2.000e+00  1.199e+00  -1.668  0.09957 .
    student32   -2.000e+00  1.199e+00  -1.668  0.09957 .
    student33   -4.000e+00  1.199e+00  -3.337  0.00134 **
    student34   -7.627e-16  1.199e+00   0.000  1.00000
    student35   -3.846e-16  1.199e+00   0.000  1.00000
    student36   -1.000e+00  1.199e+00  -0.834  0.40692
    student37    3.978e-16  1.199e+00   0.000  1.00000
    student38   -4.000e+00  1.199e+00  -3.337  0.00134 **
    student39    2.214e-15  1.199e+00   0.000  1.00000
    student40    7.904e-16  1.199e+00   0.000  1.00000
    student41    2.331e-15  1.199e+00   0.000  1.00000
    student42   -1.000e+00  1.199e+00  -0.834  0.40692
    student43   -1.000e+00  1.199e+00  -0.834  0.40692
    student44    1.955e-15  1.199e+00   0.000  1.00000
    student45   -3.000e+00  1.199e+00  -2.503  0.01460 *
    student46   -1.000e+00  1.199e+00  -0.834  0.40692
    student47   -3.000e+00  1.199e+00  -2.503  0.01460 *
    student48   -1.000e+00  1.199e+00  -0.834  0.40692
    student49   -1.000e+00  1.199e+00  -0.834  0.40692
    student50    2.473e-15  1.199e+00   0.000  1.00000
    student51    3.473e-15  1.199e+00   0.000  1.00000
    student52   -1.000e+00  1.199e+00  -0.834  0.40692
    student53   -1.000e+00  1.199e+00  -0.834  0.40692
    student54    1.729e-15  1.199e+00   0.000  1.00000
    student55    3.237e-15  1.199e+00   0.000  1.00000
    student56    2.650e-15  1.199e+00   0.000  1.00000
    student57    1.871e-15  1.199e+00   0.000  1.00000
    student58    8.195e-16  1.199e+00   0.000  1.00000
    student59    1.459e-15  1.199e+00   0.000  1.00000
    student60   -3.000e+00  1.199e+00  -2.503  0.01460 *
    student61   -1.000e+00  1.199e+00  -0.834  0.40692
    student62   -1.000e+00  1.199e+00  -0.834  0.40692
    student63   -4.000e+00  1.199e+00  -3.337  0.00134 **
    student64   -1.000e+00  1.199e+00  -0.834  0.40692
    student65   -1.000e+00  1.199e+00  -0.834  0.40692
    student66    2.729e-15  1.199e+00   0.000  1.00000
    student67    1.846e-15  1.199e+00   0.000  1.00000
    student68   -6.000e+00  1.199e+00  -5.005 3.82e-06 ***
    student69   -2.000e+00  1.199e+00  -1.668  0.09957 .
    student70    8.497e-16  1.199e+00   0.000  1.00000
    student71    1.994e-15  1.199e+00   0.000  1.00000
    student72   -4.000e+00  1.199e+00  -3.337  0.00134 **
    student73    1.876e-15  1.199e+00   0.000  1.00000
    student74           NA         NA      NA       NA
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 1.199 on 72 degrees of freedom
    Multiple R-squared:  0.7273,    Adjusted R-squared:  0.4431
    F-statistic:  2.56 on 75 and 72 DF,  p-value: 4.233e-05

## Model 4: Student as random effect

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(lme4)
m4 <- lmer(score ~ format + question + section + (1 | student), data = midterms_long)
summary(m4)
```

    Linear mixed model fit by REML ['lmerMod']
    Formula: score ~ format + question + section + (1 | student)
       Data: midterms_long

    REML criterion at convergence: 545.6

    Scaled residuals:
        Min      1Q  Median      3Q     Max
    -2.3651 -0.5693  0.3374  0.5854  1.6128

    Random effects:
     Groups   Name        Variance Std.Dev.
     student  (Intercept) 1.152    1.073
     Residual             1.437    1.199
    Number of obs: 148, groups:  student, 74

    Fixed effects:
                Estimate Std. Error t value
    (Intercept)   4.9167     0.2671  18.405
    formatS       0.2973     0.1971   1.509
    questionQ23  -0.2973     0.1971  -1.509
    section102    0.0307     0.3180   0.097

    Correlation of Fixed Effects:
                (Intr) formtS qstQ23
    formatS     -0.369
    questionQ23 -0.369  0.000
    section102  -0.611  0.000  0.000

## Model 4: Student as random effect (continued)

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(lmerTest)
m4 <- lmer(score ~ format + question + section + (1 | student), data = midterms_long)
summary(m4)
```

    Linear mixed model fit by REML. t-tests use Satterthwaite's method [
    lmerModLmerTest]
    Formula: score ~ format + question + section + (1 | student)
       Data: midterms_long

    REML criterion at convergence: 545.6

    Scaled residuals:
        Min      1Q  Median      3Q     Max
    -2.3651 -0.5693  0.3374  0.5854  1.6128

    Random effects:
     Groups   Name        Variance Std.Dev.
     student  (Intercept) 1.152    1.073
     Residual             1.437    1.199
    Number of obs: 148, groups:  student, 74

    Fixed effects:
                Estimate Std. Error       df t value Pr(>|t|)
    (Intercept)   4.9167     0.2671 119.2292  18.405   <2e-16 ***
    formatS       0.2973     0.1971  72.0000   1.509    0.136
    questionQ23  -0.2973     0.1971  72.0000  -1.509    0.136
    section102    0.0307     0.3180  72.0000   0.097    0.923
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Correlation of Fixed Effects:
                (Intr) formtS qstQ23
    formatS     -0.369
    questionQ23 -0.369  0.000
    section102  -0.611  0.000  0.000

---

[← Randomization-based Inference for Crossover Design](02-randomization-based-inference-for-crossover-design.md) · [Up: contents](index.md)
