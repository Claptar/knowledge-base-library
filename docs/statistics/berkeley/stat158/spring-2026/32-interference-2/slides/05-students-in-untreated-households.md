---
title: students in untreated households
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/32-interference-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/32-interference-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# students in untreated households

**Source:** [`32-interference-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/32-interference-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

ybar_0_0 <- attendance |>
  filter(treated_household == 0) |>
  summarize(avg_y = mean(Y)) |>
  pull()
ybar_0_0
```

    [1] 0.8502641

## Estimates

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
direct_hat <- ybar_1_0 - ybar_0_0
direct_hat
```

    [1] 0.0296671

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
spillover_hat <- ybar_0_1 - ybar_0_0
spillover_hat
```

    [1] 0.01953034

Traditional estimate:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
ate_hat_1 <- ybar_1_0 - ybar_0_1 # diff in means within treated households
ate_hat_1
```

    [1] 0.01013676

## Rand. test under interference

**Question**: How would you do a randomization test for the direct effect of treatment?

1.  Hold outcome for each student fixed.
2.  Reassign households to treatment or control and then students to treatment or control.
3.  Calculate `direct_hat` statistic.
4.  Repeat many times.

---

[← their untreated siblings](04-their-untreated-siblings.md) · [Up: contents](index.md) · [Case Studies →](06-case-studies.md)
