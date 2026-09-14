---
title: Time and Pressure
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Time and Pressure

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

group_means <- paper |>
  group_by(time, pressure) |>
  summarize(avg_strength = mean(strength),
            n = n())
group_means
```

    # A tibble: 6 × 4
    # Groups:   time [2]
      time  pressure avg_strength     n
      <fct> <fct>           <dbl> <int>
    1 3hrs  400              197.     6
    2 3hrs  500              196.     6
    3 3hrs  650              198.     6
    4 4hrs  400              198.     6
    5 4hrs  500              199.     6
    6 4hrs  650              200.     6

Before showing the output of the code, ask: how many units are being averaged over in each group here?

Answer: 6.

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

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Interaction Plots](03-interaction-plots.md) · [Up: contents](index.md) · [Time and Pressure →](05-time-and-pressure.md)
