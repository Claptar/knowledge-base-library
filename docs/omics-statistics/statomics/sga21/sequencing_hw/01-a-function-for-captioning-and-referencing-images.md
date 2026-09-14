---
title: A function for captioning and referencing images
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_hw.Rmd
source_file: sources/statomics-sga21/sequencing_hw.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# A function for captioning and referencing images

**Source:** [`sequencing_hw.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_hw.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

fig <- local({
    i <- 0
    ref <- list()
    list(
        cap=function(refName, text) {
            i <<- i + 1
            ref[[refName]] <<- i
            paste("Figure ", i, ": ", text, sep="")
        },
        ref=function(refName) {
            ref[[refName]]
        })
})
```

```r
suppressPackageStartupMessages({
  library(knitr)
  library(rmarkdown)
  library(ggplot2)
})
if(!"BiocManager" %in% installed.packages()[,1]){
  install.packages("BiocManager")
}
if(!"limma" %in% installed.packages()[,1]){
  BiocManager::install("limma")
}
if(!"edgeR" %in% installed.packages()[,1]){
  BiocManager::install("edgeR")
}
```

---

[Up: contents](index.md) · [Default edgeR analysis →](02-default-edger-analysis.md)
