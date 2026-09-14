---
title: plotting 2
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd
source_file: sources/statomics-sga21/cptac_robust.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# plotting 2

**Source:** [`cptac_robust.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

p2 <- ggplot(pePlotDf, aes(x = colname, y = value, fill = condition)) +
  geom_boxplot(outlier.shape = NA) +
  geom_point(
    position = position_jitter(width = .1),
    aes(shape = rowname)) +
  scale_shape_manual(values = 1:nrow(pePlotDf)) +
  labs(title = protName, x = "sample", y = "peptide intensity (log2)") +
  theme(axis.text.x = element_text(angle = 70, hjust = 1, vjust = 0.5)) +
  facet_grid(~assay)
print(p2)
}
```

Note, that the yeast protein is only covered by 3 peptides.
Only one peptide is picked up in condition A.
This peptide is also only once observed in spike-in condition B.
This puts a considerable burden upon the inference and could be avoided by more stringent filtering.

---

[← plotting](05-plotting.md) · [Up: contents](index.md) · [Session Info →](07-session-info.md)
