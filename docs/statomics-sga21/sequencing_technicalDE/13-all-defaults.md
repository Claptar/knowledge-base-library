---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/limmaVoomWeights.png")
```

## limma-voom analysis of parathyroid data

`limma` has an extensive user's guide which can be accessed via `limma::limmaUsersGuide()`.

```r
library(limma)
library(edgeR)
se <- readRDS("data/seParathyroid.rds")
se
design <- model.matrix(~treatment*time+patient,
                       data=colData(se))

keep <- filterByExpr(se, design)
table(keep)
filtCounts <- assays(se)$counts[keep,]

dge <- DGEList(counts=filtCounts)

---

[← All defaults](12-all-defaults.md) · [Up: contents](index.md) · [normalize just as in edgeR →](14-normalize-just-as-in-edger.md)
