---
title: 2. Software for Proteomics Data Analysis 2021 (PDA21)
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/software.Rmd
source_file: sources/statomics-sga21/software.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`software.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/software.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2. Software for Proteomics Data Analysis 2021 (PDA21)

[](https://creativecommons.org/licenses/by-nc-sa/4.0)

- Install [R version 4.1 or higher] (https://cran.r-project.org/)
- Install [Rstudio](https://www.rstudio.com/products/rstudio/download/)
- Install *msqrob2*, start R and run the following command.

```
if(!requireNamespace("BiocManager", quietly = TRUE)) {
 install.packages("BiocManager")
}
BiocManager::install("msqrob2")
```

- Participants who want to use the graphical user interface (GUI) can install the msqrob2gui shiny app, start R and run the following commands

```
if(!requireNamespace("BiocManager", quietly = TRUE)) {
 install.packages("BiocManager")
}
if(!requireNamespace("remotes", quietly = TRUE)) {
 BiocManager::install("remotes")
}
BiocManager::install("statomics/msqrob2gui")
```

- check if your installation is working with the following example
library(msqrob2)

```
data(pe)
pe <- aggregateFeatures(pe,i="peptide",fcol="Proteins",name="protein")
pe <- msqrob(pe,i="protein",formula=~condition,modelColumnName="rlm")
getCoef(rowData(pe[["protein"]])$rlm[[1]])
```

- For testing our package without installation: you can launch an R studio interface in an R docker along with bioconductor packages for proteomics that is running on top of one of our github repositories.

[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/statOmics/shinyTest/master?urlpath=rstudio)

---

[Up: contents](index.md)
