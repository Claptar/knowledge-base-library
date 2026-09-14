---
title: Time and Pressure and Hardness
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Time and Pressure and Hardness

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

group_means <- paper |>
  group_by(time, pressure, hard) |>
  summarize(avg_strength = mean(strength),
            n = n())
group_means
```

    # A tibble: 18 × 5
    # Groups:   time, pressure [6]
       time  pressure hard  avg_strength     n
       <fct> <fct>    <fct>        <dbl> <int>
     1 3hrs  400      2             196.     2
     2 3hrs  400      4             198.     2
     3 3hrs  400      8             197.     2
     4 3hrs  500      2             197.     2
     5 3hrs  500      4             196.     2
     6 3hrs  500      8             196.     2
     7 3hrs  650      2             200.     2
     8 3hrs  650      4             198      2
     9 3hrs  650      8             198.     2
    10 4hrs  400      2             198.     2
    11 4hrs  400      4             198.     2
    12 4hrs  400      8             198      2
    13 4hrs  500      2             200      2
    14 4hrs  500      4             198.     2
    15 4hrs  500      8             197.     2
    16 4hrs  650      2             201.     2
    17 4hrs  650      4             199.     2
    18 4hrs  650      8             199.     2

Ask: how many observations are we averaging over in each group?

Answer: 2

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

##  {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}

---

[← Pressure and Hardness](09-pressure-and-hardness.md) · [Up: contents](index.md) · [Time and Pressure and Hardness →](11-time-and-pressure-and-hardness.md)
