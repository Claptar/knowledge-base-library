---
title: association with weather on count and log scale
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# association with weather on count and log scale

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

barplot(table(Bikeshare$weathersit))
boxplot(bikers ~ weathersit, data=Bikeshare,
        xlab = "Weather", ylab = "Bikers")
boxplot(log1p(bikers) ~ weathersit, data=Bikeshare,
        xlab = "Weather", ylab = "Log (bikers +1)")

---

[← load and preview the dataset](07-load-and-preview-the-dataset.md) · [Up: contents](index.md) · [association with humidity on count and log scale →](09-association-with-humidity-on-count-and-log-scale.md)
