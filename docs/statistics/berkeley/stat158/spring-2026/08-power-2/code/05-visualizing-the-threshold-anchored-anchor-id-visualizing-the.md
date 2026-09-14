---
title: Visualizing the threshold {.anchored anchor-id="visualizing-the-threshold"}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Visualizing the threshold {.anchored anchor-id="visualizing-the-threshold"}

**Source:** [`08-power-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In a two-tailed test at <span class="math inline">\$\\alpha = .05\$</span>, the rejection region is anything less than the .025 quantile and anything more than the .0975 quantile of the null distribution of statistics.

``` {.sourceCode .r .code-with-copy}
left_threshold <- quantile(H_0, .025)
right_threshold <- quantile(H_0, .975)
```

``` {.sourceCode .r .code-with-copy}
data.frame(stat = H_0) |>
  ggplot(aes(x = stat)) +
  geom_histogram() +
  geom_vline(xintercept = c(left_threshold, right_threshold), col = "tomato") +
  theme_bw()
```

    `stat_bin()` using `bins = 30`. Pick better value `binwidth`.

<figure class="figure">
<p><img src="code_files/figure-html/unnamed-chunk-11-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

---

[← Code Part 04 —](04-code-part-04.md) · [Up: contents](index.md) · [Code Part 06 — →](06-code-part-06.md)
