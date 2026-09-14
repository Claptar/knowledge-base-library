---
title: Estimates
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/31-interference/slides.html
source_file: sources/berkeley-stat158/spring-2026/31-interference/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Estimates

**Source:** [`31-interference/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/31-interference/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

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

Traditional estimates:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
ate_hat_1 <- ybar_1_0 - ybar_0_1 # diff in means within treated households
ate_hat_1
```

    [1] 0.01013676

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
ybar_all_0 <- attendance |>
  filter(treated_student == 0) |>
  summarize(avg_y = mean(Y)) |>
  pull()
ybar_1_0 - ybar_all_0 # diff in means on treated students
```

    [1] 0.02315699

---

[← Simulated School Attendance](06-simulated-school-attendance.md) · [Up: contents](index.md) · [Rand. test under interference →](08-rand-test-under-interference.md)
