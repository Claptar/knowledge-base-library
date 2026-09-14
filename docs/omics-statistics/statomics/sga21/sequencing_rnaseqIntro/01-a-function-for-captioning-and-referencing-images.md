---
title: A function for captioning and referencing images
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# A function for captioning and referencing images

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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
if(!"DESeq2" %in% installed.packages()[,1]){
  BiocManager::install("DESeq2")
}
if(!"scales" %in% installed.packages()[,1]){
  install.packages("scales")
}
```

In this lecture we will start working with a real bulk RNA-seq dataset from [Haglund *et al.* (2012)](https://academic.oup.com/jcem/article/97/12/4631/2536573). After importing the data, we will be working our way through four major challenges which, together, will form a full RNA-seq differential expression (DE) analysis pipeline where the result of our analysis will be a(n ordered) list of genes that we find to be differently expressed between our conditions of interest. The four main challenges we will look into are

 - Choice of modeling assumptions (distribution).
 - Normalization.
 - Parameter estimation under a limited information setting.
 - Statistical inference under high dimensionality (many genes).

---

[Up: contents](index.md) · [Experimental design, data import and data exploration →](02-experimental-design-data-import-and-data-exploration.md)
