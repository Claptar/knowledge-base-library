---
title: Inference
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/22-latin-squares/slides.html
source_file: sources/berkeley-stat158/spring-2026/22-latin-squares/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Inference

**Source:** [`22-latin-squares/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/22-latin-squares/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Linear Model for LS

<span class="math display">\\$$ Y\_{i} = \\mu + \\alpha\_{j(i)} + \\beta\_{k(i)} + \\delta\_{l(i)} + \\epsilon\_i \\$$</span>

Note:

- This is a three way factorial with no interactions
- Can do an F-test on diet using the sum of squares for diet (<span class="math inline">\$\\hat{\\delta\_{l}}\$</span>)and the residual sum of squares to get an estimate of the error variance.

## Model-Based Inference

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
fit <- aov(milk ~ diet + cow + period, data = milk)
summary(fit)
```

                Df Sum Sq Mean Sq F value Pr(>F)
    diet         2  61.56  30.778   5.653  0.150
    cow          2   0.22   0.111   0.020  0.980
    period       2  16.22   8.111   1.490  0.402
    Residuals    2  10.89   5.444

## Randomization-Based Inference

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
milk
```

    # A tibble: 9 × 4
      cow   period diet   milk
      <fct> <fct>  <fct> <dbl>
    1 1     1      F        23
    2 1     2      P        18
    3 1     3      R        15
    4 2     1      P        16
    5 2     2      R        19
    6 2     3      F        22
    7 3     1      R        21
    8 3     2      F        22
    9 3     3      P        14

How could simulate another data set that could have been realized under this design using the Fisher Sharp Null?

Ask if you can simply permute the Y col? Or the two blocking cols?

The answer is no: the LS imposes a constraint based on the combination of the blocking factors. You need to select a random Latin Square and then assign the observed Y values to the treatments in that square.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

## How to do random assignment in LS

1.  Randomly select a *standard* latin square (treatments in alphabetical order in first row and column).
2.  Randomly assign levels of the first blocking factor to rows.
3.  Randomly assign levels of the second blocking factor to columns.
4.  Randomly assign treatment levels to letters.

##

---

[← Latin Squares](01-latin-squares.md) · [Up: contents](index.md)
