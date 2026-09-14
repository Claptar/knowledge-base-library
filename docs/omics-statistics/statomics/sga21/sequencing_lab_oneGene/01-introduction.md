---
title: Introduction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd
source_file: sources/statomics-sga21/sequencing_lab_oneGene.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`sequencing_lab_oneGene.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
# A function for captioning and referencing images
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
```


```r
suppressPackageStartupMessages(library(SummarizedExperiment))
se <- readRDS("data/seParathyroid.rds")
```


```r
## extract data from one gene
y <- assays(se)$counts[5,]

## extract covariates for each sample
treatment <- colData(se)$treatment
table(treatment)
time <- colData(se)$time
table(time)
patient <- colData(se)$patient
table(patient)

table(patient, treatment, time)

boxplot((y/colSums(assays(se)$counts)) ~ interaction(treatment, time))
## dotplot for each treatment, matching patient samples
df <- data.frame(y=y,
                 treatment=treatment,
                 time=time,
                 patient=patient)
ggplot(df, aes(x=time, y=y)) +
  geom_point() +
  geom_line(aes(group = patient)) +
  facet_grid(.~treatment) +
  theme_classic()
```


# Poisson GLM

```r
m <- glm(y ~ treatment*time + patient,
         family = "poisson")
plot(m) # Extra-Poisson variation?
```

## Check overdispersion

```r
ePearson <- resid(m, type="pearson")
n <- length(y)
p <- length(coef(m))
sum(ePearson^2) / (n-p) # huge overdispersion.
```

# Negative binomial model

```r
library(MASS)
mNB <- glm.nb(y ~ treatment*time + patient)
plot(mNB)
summary(mNB)
```


## Statistical inference

We will test seven different contrasts.

```r
L <- matrix(0, nrow = length(coef(mNB)), ncol = 7)
rownames(L) <- names(coef(mNB))
colnames(L) <- c("DPNvsCON24", "DPNvsCON48",
                 "OHTvsCON24", "OHTvsCON48",
                 "DPNvsCONInt", "OHTvsCONInt",
                 "OHTvsDPNInt")
# DPN vs control at 24h
L[2,"DPNvsCON24"] <- 1
# DPN vs control at 48h
L[c(2,8),"DPNvsCON48"] <- 1
# OHT vs control at 24h
L[3,"OHTvsCON24"] <- 1
# OHT vs control at 48h
L[c(3,9),"OHTvsCON48"] <- 1
# DPN control interaction
L[8,"DPNvsCONInt"] <- 1
# OHT control interaction
L[9,"OHTvsCONInt"] <- 1
# OHT DPN interaction
L[c(9,8),"OHTvsDPNInt"] <- c(1, -1)

L
```

---

[Up: contents](index.md) · [Wald test →](02-wald-test.md)
