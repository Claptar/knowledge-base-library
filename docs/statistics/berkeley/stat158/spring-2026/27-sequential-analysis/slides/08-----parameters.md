---
title: '--- Parameters ---'
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# --- Parameters ---

**Source:** [`27-sequential-analysis/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

set.seed(7)
n <- 1e3; p0 <- 0.4; p1 <- 0.6; e <- 0.5
tau <- p1 - p0

Z   <- rbinom(n, 1, e)
Y   <- ifelse(Z == 1, rbinom(n, 1, p1), rbinom(n, 1, p0))
phi <- Z * Y / e - (1 - Z) * Y / (1 - e)

cs  <- robbins_confseq(phi)

ns     <- 1:n
mu_hat <- cumsum(phi) / ns
clt_hw <- qnorm(0.975) * running_sd(phi) / sqrt(ns)

df <- data.frame(
  t      = ns,
  ate    = mu_hat,
  cs_lo  = cs$lower, cs_hi = cs$upper,
  clt_lo = mu_hat - clt_hw,
  clt_hi = mu_hat + clt_hw
)[50:n, ]

p1_plot <- ggplot(df, aes(t)) +
  geom_ribbon(aes(ymin = cs_lo, ymax = cs_hi), alpha = 0.2, fill = "steelblue") +
  geom_line(aes(y = ate), color = "steelblue") +
  geom_hline(yintercept = tau, color = "red", linetype = "dashed") +
  scale_x_continuous(breaks = seq(0, max(df$t), by = 100)) +
  labs(x = "n", y = "Estimated ATE", title = "Asymptotic CS (valid)",
       subtitle = "Anytime-valid: accounts for peeking") +
  theme_minimal()

p2_plot <- ggplot(df, aes(t)) +
  geom_ribbon(aes(ymin = clt_lo, ymax = clt_hi), alpha = 0.2, fill = "coral") +
  geom_line(aes(y = ate), color = "coral") +
  geom_hline(yintercept = tau, color = "red", linetype = "dashed") +
  scale_x_continuous(breaks = seq(0, max(df$t), by = 100)) +
  labs(x = "n", y = "Estimated ATE", title = "CLT CI (invalid for peeking)",
       subtitle = "Too narrow: misses true ATE when you peek") +
  theme_minimal()

p1_plot + p2_plot +
  plot_layout(widths = c(1, 1)) &
  plot_annotation(
    title    = sprintf("CS vs CLT CI | p0=%.1f, p1=%.1f, tau=%.1f", p0, p1, tau),
    subtitle = "Red dashed line = true ATE",
    theme = theme(
      plot.title    = element_text(size = 14, face = "bold", margin = margin(b = 6)),
      plot.subtitle = element_text(size = 11, margin = margin(b = 12))
    )
  )
```

<figure>

</figure>

- Note this plot is different than the log-likelihood plot.

## Artillery Example

- Wald wanted a method that allowed him to stop monitoring the moment he could reject.
- Confidence sequences extend this from testing to confidence bands.
- What if you were more flexible?

---

[← Confidence Sequences](07-confidence-sequences.md) · [Up: contents](index.md) · [Group Sequential Designs →](09-group-sequential-designs.md)
