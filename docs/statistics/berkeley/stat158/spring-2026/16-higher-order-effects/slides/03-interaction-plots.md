---
title: Interaction Plots
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Interaction Plots

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Two-way Interaction Plots

You’ll need at least one interaction plot for each pairwise combination of factors (1 for CR$$2$$, 3 for CR$$3$$).

- Calculate the mean response over every treatment combination of the two factors.
- Plot those means on the y axis, with the first factor on the x and the second factor differentiated by color, linetype or shape.
- Draw lines between the means with the same level of the second factor.

> Parallel lines indicate *no interaction*.

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
paper
```

       strength hard time pressure
    1     196.6    2 3hrs      400
    2     196.0    2 3hrs      400
    3     198.5    4 3hrs      400
    4     197.2    4 3hrs      400
    5     197.5    8 3hrs      400
    6     196.6    8 3hrs      400
    7     197.7    2 3hrs      500
    8     196.0    2 3hrs      500
    9     196.0    4 3hrs      500
    10    196.9    4 3hrs      500
    11    195.6    8 3hrs      500
    12    196.2    8 3hrs      500
    13    199.8    2 3hrs      650
    14    199.4    2 3hrs      650
    15    198.4    4 3hrs      650
    16    197.6    4 3hrs      650
    17    197.4    8 3hrs      650
    18    198.1    8 3hrs      650
    19    198.4    2 4hrs      400
    20    198.6    2 4hrs      400
    21    197.5    4 4hrs      400
    22    198.1    4 4hrs      400
    23    197.6    8 4hrs      400
    24    198.4    8 4hrs      400
    25    199.6    2 4hrs      500
    26    200.4    2 4hrs      500
    27    198.7    4 4hrs      500
    28    198.0    4 4hrs      500
    29    197.0    8 4hrs      500
    30    197.8    8 4hrs      500
    31    200.6    2 4hrs      650
    32    200.9    2 4hrs      650
    33    199.6    4 4hrs      650
    34    199.0    4 4hrs      650
    35    198.5    8 4hrs      650
    36    199.8    8 4hrs      650

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Exploratory Data Analysis](02-exploratory-data-analysis.md) · [Up: contents](index.md) · [Time and Pressure →](04-time-and-pressure.md)
