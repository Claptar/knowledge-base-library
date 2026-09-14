---
title: add the unique permutations as a new column and find yi, the observed responses
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html
source_file: sources/berkeley-stat158/spring-2026/05-testing/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# add the unique permutations as a new column and find yi, the observed responses

**Source:** [`05-testing/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

all_partitions_df <- all_partitions_df |>
  mutate(d_i = as.vector(t(permmat)),
         y_i = Y_1 * d_i +  Y_0 * (1 - d_i))
all_partitions_df
```

    # A tibble: 120 × 5
       partition   Y_0   Y_1   d_i   y_i
       <ord>     <dbl> <dbl> <dbl> <dbl>
     1 1            15    15     0    15
     2 1            15    15     0    15
     3 1            19    19     0    19
     4 1            20    20     1    20
     5 1            20    20     1    20
     6 1            15    15     1    15
     7 2            15    15     0    15
     8 2            15    15     0    15
     9 2            19    19     1    19
    10 2            20    20     0    20
    # ℹ 110 more rows

``` {.sourceCode .r .code-with-copy}

---

[← replicate the anchor sched 20 times and stack them on top of one another](05-replicate-the-anchor-sched-20-times-and-stack-them-on-top-of.md) · [Up: contents](index.md) · [calculate ATE-hat for every partition →](07-calculate-ate-hat-for-every-partition.md)
