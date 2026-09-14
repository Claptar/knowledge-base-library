---
title: loop over all contrasts of interest
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# loop over all contrasts of interest

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

ttList <- list()
for(cc in 1:ncol(L)){
  ttList[[cc]] <- topTable(fit2, coef=cc, number=nrow(dge))
}
names(ttList) <- colnames(L)
nDE <- unlist(lapply(ttList, function(x) sum(x$adj.P.Val <= 0.05)))
nDE
```

---

[← OHT DPN interaction](24-oht-dpn-interaction.md) · [Up: contents](index.md)
