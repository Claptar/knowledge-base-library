---
title: Power {#power-1}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Power {#power-1}

**Source:** [`08-power-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Power {#power-2}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
power <- mean(H_A > right_threshold | H_A < left_threshold)
power
```

    [1] 0.2406

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
n_0 <- 5
n_1 <- 5

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

<figure>

</figure>

---

[← An Alternative Hypothesis](03-an-alternative-hypothesis.md) · [Up: contents](index.md) · [Functions →](05-functions.md)
