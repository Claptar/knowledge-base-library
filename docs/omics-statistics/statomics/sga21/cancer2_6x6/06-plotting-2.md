---
title: plotting 2
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd
source_file: sources/statomics-sga21/cancer2_6x6.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# plotting 2

**Source:** [`cancer2_6x6.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

p2 <- ggplot(pePlotDf, aes(x = colname, y = value, fill = outcome)) +
 geom_boxplot(outlier.shape = NA) + geom_point(position = position_jitter(width = .1),
                                               aes(shape = rowname)) +
 scale_shape_manual(values = 1:nrow(pePlotDf)) +
 labs(title = protName, x = "sample", y = "peptide intensity (log2)") + theme_minimal()
 facet_grid(~assay)
print(p2)
}
```

---

[← plotting](05-plotting.md) · [Up: contents](index.md)
