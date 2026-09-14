---
title: set up data frames with relevant predictor variables' values.
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# set up data frames with relevant predictor variables' values.

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

dfA <- data.frame(weathersit = factor("light rain/snow"),
                    hr = factor(17),
                    humc = 0.357)
dfB <- data.frame(weathersit = factor("clear"),
                    hr = factor(8),
                    humc = 0)

---

[← association with hour on count and log scale](10-association-with-hour-on-count-and-log-scale.md) · [Up: contents](index.md) · [calculate estimated average number of bikers →](12-calculate-estimated-average-number-of-bikers.md)
