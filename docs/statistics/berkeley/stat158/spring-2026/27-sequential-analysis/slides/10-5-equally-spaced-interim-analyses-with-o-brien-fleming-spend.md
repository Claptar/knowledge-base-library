---
title: 5 equally-spaced interim analyses with O'Brien-Fleming spending
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 equally-spaced interim analyses with O'Brien-Fleming spending

**Source:** [`27-sequential-analysis/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

gs <- gsDesign(k = 5, test.type = 2, alpha = 0.025, beta = 0.1, sfu = sfLDOF)

interim_times <- c(200, 400, 600, 800, 1000)

gsd_df <- do.call(rbind, lapply(seq_along(interim_times), function(i) {
  t      <- interim_times[i]
  x      <- phi[1:t]
  mu     <- mean(x)
  se     <- sd(x) / sqrt(t)
  z_crit <- gs$upper$bound[i]   # GSD-adjusted critical value at this look
  data.frame(t = t, ate = mu,
             lo = mu - z_crit * se,
             hi = mu + z_crit * se,
             z_crit = round(z_crit, 2))
}))

ggplot(gsd_df, aes(x = t)) +
  geom_errorbar(aes(ymin = lo, ymax = hi), width = 30, color = "steelblue", linewidth = 0.8) +
  geom_point(aes(y = ate), color = "steelblue", size = 3) +
  geom_text(aes(y = hi, label = paste0("z=", z_crit)), vjust = -0.6, size = 3) +
  geom_hline(yintercept = tau, color = "red",   linetype = "dashed") +
  geom_hline(yintercept = 0,   color = "black", linetype = "dotted") +
  scale_x_continuous(breaks = interim_times) +
  labs(
    x        = "Interim analysis (n)",
    y        = "Estimated ATE",
    title    = "Group Sequential Design (O'Brien-Fleming): CIs at interim looks",
    subtitle = "Red dashed = true ATE; z labels = GSD-adjusted critical value"
  ) +
  theme_minimal() + p1_plot +
  plot_layout(widths = c(7, 5))
```

<figure>

</figure>

---

[← Group Sequential Designs](09-group-sequential-designs.md) · [Up: contents](index.md) · [Conclusion →](11-conclusion.md)
