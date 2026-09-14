---
title: Pressure and Hardness
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Pressure and Hardness

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

group_means <- paper |>
  group_by(pressure, hard) |>
  summarize(avg_strength = mean(strength))
group_means
```

    # A tibble: 9 × 3
    # Groups:   pressure [3]
      pressure hard  avg_strength
      <fct>    <fct>        <dbl>
    1 400      2             197.
    2 400      4             198.
    3 400      8             198.
    4 500      2             198.
    5 500      4             197.
    6 500      8             197.
    7 650      2             200.
    8 650      4             199.
    9 650      8             198.

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Time and Hardness](07-time-and-hardness.md) · [Up: contents](index.md) · [Pressure and Hardness →](09-pressure-and-hardness.md)
