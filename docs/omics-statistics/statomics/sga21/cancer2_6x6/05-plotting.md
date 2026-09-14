---
title: plotting
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd
source_file: sources/statomics-sga21/cancer2_6x6.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# plotting

**Source:** [`cancer2_6x6.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

p1 <- ggplot(data = pePlotDf,
      aes(x = colname, y = value, group = rowname)) +
   geom_line() + geom_point() +  theme_minimal() +
   facet_grid(~assay) + ggtitle(protName)
print(p1)

---

[← Data Analysis](04-data-analysis.md) · [Up: contents](index.md) · [plotting 2 →](06-plotting-2.md)
