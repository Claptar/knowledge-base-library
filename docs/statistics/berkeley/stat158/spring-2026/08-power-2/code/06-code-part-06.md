---
title: Code Part 06 —
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Code Part 06 —

**Source:** [`08-power-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

The only thing that changes to find the sampling distribution under <span class="math inline">\$H\_A\$</span> is the schedule.

``` {.sourceCode .r .code-with-copy}
H_A <- rand_stats(schedule = my_true_sched, d_i = d_i, reps = 5000)
```

We can now visualize these side-by-side.

``` {.sourceCode .r .code-with-copy}
data.frame(stat = c(H_0, H_A),
           type = factor(c(rep("Null", length(H_0)),
                           rep("Alt", length(H_A))))) |>
  ggplot(aes(x = stat, fill = type)) +
  geom_histogram(position = "identity", alpha = .3) +
  geom_vline(xintercept = c(left_threshold, right_threshold), col = "tomato") +
  theme_bw()
```

    `stat_bin()` using `bins = 30`. Pick better value `binwidth`.

<figure class="figure">
<p><img src="code_files/figure-html/unnamed-chunk-13-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

---

[← Visualizing the threshold {.anchored anchor-id="visualizing-the-threshold"}](05-visualizing-the-threshold-anchored-anchor-id-visualizing-the.md) · [Up: contents](index.md) · [Calculate Power {.anchored anchor-id="calculate-power"} →](07-calculate-power-anchored-anchor-id-calculate-power.md)
