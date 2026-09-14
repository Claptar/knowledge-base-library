---
title: treated students in treated households
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/32-interference-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/32-interference-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# treated students in treated households

**Source:** [`32-interference-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/32-interference-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

ybar_1_0 <- attendance |>
  filter(treated_household == 1, treated_student == 1) |>
  summarize(avg_y = mean(Y)) |>
  pull()
ybar_1_0
```

    [1] 0.8799312

## Simulated School Attendance {data-id="quarto-animate-title"}

    # A tibble: 40,000 × 5
       household_id student_id treated_household treated_student     Y
              <int>      <int>             <dbl>           <dbl> <dbl>
     1            1          1                 0               0 0.802
     2            1          2                 0               0 0.859
     3            2          1                 0               0 0.778
     4            2          2                 0               0 0.838
     5            3          1                 1               0 0.891
     6            3          2                 1               1 0.956
     7            4          1                 1               0 0.924
     8            4          2                 1               1 0.975
     9            5          1                 1               1 0.897
    10            5          2                 1               0 0.902
    # ℹ 39,990 more rows

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}

---

[← Simulated School Attendance](02-simulated-school-attendance.md) · [Up: contents](index.md) · [their untreated siblings →](04-their-untreated-siblings.md)
