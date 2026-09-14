---
title: Function that computes power curve for given d and k
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Function that computes power curve for given d and k

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

compute_power_curve <- function(d_val, k_val) {
  theta_max <- 3 * d_val^0.25
  theta_vals <- seq(0, theta_max, length.out = 101)

  critical_chi <- qchisq(0.95, df = d_val)

  tibble(
    d = d_val,
    k = k_val,
    theta = theta_vals,
    chi_power = sapply(theta_vals, function(theta) {
      mu_val <- theta / sqrt(k_val)
      ncp <- k_val * mu_val^2
      pchisq(critical_chi, df = d_val, ncp = ncp, lower.tail = FALSE)
    })
  )
}

---

[← and pass them to OJS as data](04-and-pass-them-to-ojs-as-data.md) · [Up: contents](index.md) · [Pre-compute for a reasonable range of d and k →](06-pre-compute-for-a-reasonable-range-of-d-and-k.md)
