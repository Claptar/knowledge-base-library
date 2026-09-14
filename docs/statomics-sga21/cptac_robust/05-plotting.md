---
title: plotting
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd
source_file: sources/statomics-sga21/cptac_robust.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# plotting

**Source:** [`cptac_robust.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

p1 <- ggplot(data = pePlotDf,
       aes(x = colname, y = value, group = rowname)) +
    geom_line() +
    geom_point() +
    theme(axis.text.x = element_text(angle = 70, hjust = 1, vjust = 0.5)) +
    facet_grid(~assay) +
    ggtitle(protName)
print(p1)

---

[← Data Analysis](04-data-analysis.md) · [Up: contents](index.md) · [plotting 2 →](06-plotting-2.md)
