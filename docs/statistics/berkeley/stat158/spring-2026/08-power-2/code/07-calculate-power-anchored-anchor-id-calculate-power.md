---
title: Calculate Power {.anchored anchor-id="calculate-power"}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Calculate Power {.anchored anchor-id="calculate-power"}

**Source:** [`08-power-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Let’s calculate the power.

``` {.sourceCode .r .code-with-copy}
power <- mean(H_A > right_threshold | H_A < left_threshold)
power
```

    [1] 0.2366

Let’s combine this into one informative plot.

``` {.sourceCode .r .code-with-copy}
data.frame(stat = c(H_0, H_A),
           type = factor(c(rep("Null", length(H_0)),
                           rep("Alt", length(H_A))))) |>
  mutate(in_reject_region = ifelse(stat > right_threshold | stat < left_threshold, "Reject Null", NA)) |>
  ggplot(aes(x = stat, fill = type, color = in_reject_region)) +
  geom_histogram(position = "identity", alpha = .3) +
  geom_vline(xintercept = c(left_threshold, right_threshold), col = "tomato") +
  scale_color_manual(
    values = c("Reject Null" = "black"),
    na.value = NA,
    guide = "none") +
  labs(title = paste0("Statistical Power: ", round(power, 2)),
       subtitle = paste0("n0 = ", n_0, ", n1 = ", n_1, ", tau = ", tau)) +
  theme_bw()
```

    `stat_bin()` using `bins = 30`. Pick better value `binwidth`.

<figure class="figure">
<p><img src="code_files/figure-html/unnamed-chunk-15-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

---

[← Code Part 06 —](06-code-part-06.md) · [Up: contents](index.md)
