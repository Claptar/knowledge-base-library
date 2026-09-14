---
title: Inference
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/19-blocking/slides.html
source_file: sources/berkeley-stat158/spring-2026/19-blocking/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Inference

**Source:** [`19-blocking/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/19-blocking/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## A Model for Data from <span class="math inline">\$CB\[1$$\$</span>

<span class="math display">\\$$ Y\_i = \\mu + \\alpha\_{j(i)} + \\beta\_{k(i)} + \\epsilon\_i \\$$</span>

Estimates:

- <span class="math inline">\$\\hat{\\mu} = \\hat{\\bar{Y}}\$</span>
- <span class="math inline">\$\\hat{\\alpha}\_{j(i)} = \\hat{\\bar{Y}}\_{j(i)} - \\hat{\\mu}\$</span>
- <span class="math inline">\$\\hat{\\beta}\_{k(i)} = \\hat{\\bar{Y}}\_{k(i)} - \\hat{\\mu}\$</span>

Note: <span class="math inline">\$CB$$\]\$</span> doesn’t have enough data to estimate interactions (would need replicates: <span class="math inline">\$GCB\[$$\$</span>)

## Design - Analysis Mismatch

## Taps Model-based Inference

Additive model (no interaction)

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- aov(taps ~ person + drug, taps_df)
summary(anova_results)
```

                Df Sum Sq Mean Sq F value   Pr(>F)
    person       3   5478  1826.0   33.00 0.000399 ***
    drug         2    872   436.0    7.88 0.020967 *
    Residuals    6    332    55.3
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

## Taps Model-based Inference

Additive model with interactions

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- aov(taps ~ person * drug, taps_df)
summary(anova_results)
```

                Df Sum Sq Mean Sq
    person       3   5478  1826.0
    drug         2    872   436.0
    person:drug  6    332    55.3

## Taps Model-based Inference

Analyzing like a <span class="math inline">\$CR$$1$$\$</span>

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- aov(taps ~ drug, taps_df)
summary(anova_results)
```

                Df Sum Sq Mean Sq F value Pr(>F)
    drug         2    872   436.0   0.675  0.533
    Residuals    9   5810   645.6

## Taps Randomization-based Inference

Calculating the observed test statistic.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- aov(taps ~ person + drug, taps_df)
obs_f_stat <- summary(anova_results)[[1]]$`F value`[2]
obs_f_stat
```

    [1] 7.879518

##

Resampling within blocks.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
taps_df |>
  group_by(person) |>
  mutate(Y = sample(taps))
```

    # A tibble: 12 × 4
    # Groups:   person [4]
        taps person drug      Y
       <dbl> <fct>  <fct> <dbl>
     1    11 1      P        20
     2    20 1      T        11
     3    26 1      C        26
     4    83 2      C        56
     5    56 2      P        83
     6    71 2      T        71
     7    41 3      T        41
     8    15 3      P        34
     9    34 3      C        15
    10    32 4      T         6
    11    13 4      C        13
    12     6 4      P        32

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
taps_df |>
  group_by(person) |>
  mutate(Y = sample(taps))
```

    # A tibble: 12 × 4
    # Groups:   person [4]
        taps person drug      Y
       <dbl> <fct>  <fct> <dbl>
     1    11 1      P        11
     2    20 1      T        26
     3    26 1      C        20
     4    83 2      C        71
     5    56 2      P        83
     6    71 2      T        56
     7    41 3      T        41
     8    15 3      P        15
     9    34 3      C        34
    10    32 4      T         6
    11    13 4      C        32
    12     6 4      P        13

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
block_shuffle <- function() { # specific to taps_df
  sim_df <- taps_df |>
    group_by(person) |>
    mutate(Y = sample(taps))

  anova_results <- aov(Y ~ person + drug, sim_df)
  f_stat <- summary(anova_results)[[1]]$`F value`[2]
  f_stat
}

replicate(10, block_shuffle())
```

     [1]  0.9714129  6.7621622  0.1908127  0.2007089  2.9653179  1.8777853
     [7]  1.8127915  1.1256425 12.8769231  5.8965517

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(500, block_shuffle())
```

##




##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
mean(null_stats > obs_f_stat)
```

    [1] 0.036

## Randomization-based vs Model-based

Randomization-based:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
mean(null_stats > obs_f_stat)
```

    [1] 0.036

Model-based

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- aov(taps ~ person + drug, taps_df)
summary(anova_results)
```

                Df Sum Sq Mean Sq F value   Pr(>F)
    person       3   5478  1826.0   33.00 0.000399 ***
    drug         2    872   436.0    7.88 0.020967 *
    Residuals    6    332    55.3
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

---

[← Study 2: Drugs and Tapping](04-study-2-drugs-and-tapping.md) · [Up: contents](index.md)
