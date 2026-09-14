---
title: MDS plot
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# MDS plot

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

plotMDS(se,
        labels = treatment,
        col=as.numeric(patient))

## hard to see influence of experimental factors due to large between-patient variation
## we could also make an MDS plot per patient to take a look.
for(kk in 1:4){
  id <- which(patient == kk)
  plotMDS(se[,id],
        labels = paste0(treatment[id],"_",time[id]),
        col=as.numeric(time[id]))
}
```

```r

---

[← library size distribution](12-library-size-distribution.md) · [Up: contents](index.md) · [Explain concept of MDS: preserve Euclidean distance from high to low dim. →](14-explain-concept-of-mds-preserve-euclidean-distance-from-high.md)
