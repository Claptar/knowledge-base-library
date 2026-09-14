---
title: Time and Hardness
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Time and Hardness

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

group_means <- paper |>
  group_by(time, hard) |>
  summarize(avg_strength = mean(strength))
group_means
```

    # A tibble: 6 × 3
    # Groups:   time [2]
      time  hard  avg_strength
      <fct> <fct>        <dbl>
    1 3hrs  2             198.
    2 3hrs  4             197.
    3 3hrs  8             197.
    4 4hrs  2             200.
    5 4hrs  4             198.
    6 4hrs  8             198.

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Time and Pressure](05-time-and-pressure.md) · [Up: contents](index.md) · [Time and Hardness →](07-time-and-hardness.md)
