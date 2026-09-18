---
title: Breast cancer dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Breast cancer dataset

```r
knitr::opts_chunk$set(include = TRUE, comment = NA, echo = TRUE,
                      message = FALSE, warning = FALSE)
library(Rmisc)
library(tidyverse)
```

- Subset of study https://doi.org/10.1093/jnci/djj052

- 32 breast cancer patients with estrogen receptor positive tumour that had tamoxifen chemotherapy. Variables:

    - grade: histological grade of tumour (grade 1 vs 3),
    - node: lymph node status  (0: not affected, 1: lymph nodes affected and removed),
    - size: tumour size in cm,
    - ESR1 and S100A8 gene expression in tumour biopsy (microarray technology)

- ESR1 in active in $\pm$ 75% of breast cancer tumours.

- Expression of ER gene positive for treatment: tumour responds to hormone therapy
    - Tamoxifen interacts with ER and modulates gene expression.

- Proteins of S100 family often dysregulated in cancer

      - S100A8 expression represses immune system in tumour en creates an environment of inflammation that promotes tumour growth.

```r
brca <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/breastcancer.csv")
brca
```

## Research question

Is the expression of the S100A8 gene associated with that of that of the ESR1 gene?

## Data exploration

There are many variables in the data, we will plot all variables in a scatterplot matrix using the GGally package.

```r
#install.packages("GGally")
library(GGally)
brca[,-(1:4)] %>% ggpairs()
```

We now focus on the association between S100A8 expression and the ESR1 expression.

```r
brca %>%
  ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```

The association of S100A and ESR1 does not appear to be linear.

- Concentration measurements are often skewed.
- We will log2 transform the data.

```r
brca %>%
  ggplot(aes(x=ESR1 %>% log2,y=S100A8 %>% log2)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```

Upon log transformation the data are showing a linear association. Is this association strong enough to be able to conclude that the S100A8 gene expression is associated to the ESR1 gene expression?

## Descriptive statistics

We first calculate the Pearson and Spearman correlation based on the original data and the log2 transformed data

Pearson  correlation
```r
brca %>%
  select(S100A8,ESR1) %>%
  mutate(S100A8Log2=S100A8%>%log2,ESR1Log2=ESR1%>%log2) %>%
  cor
```

Spearman correlation
```r
brca %>%
  select(S100A8,ESR1) %>%
  mutate(S100A8Log2=S100A8%>%log2,ESR1Log2=ESR1%>%log2) %>%
  cor(,method = "spearman")
```

Both the Pearson and Spearman correlation are negative. Note, that the Spearman correlation is much larger in absolute value than the Pearson correlation on the original expression measurements. Indeed, the Pearson correlation is affected by the non linear association at the original scale.

On the log scale the Pearson correlation is much higher.
The spearman correlation, however, remains because it is based on rank transformed data.

---

[Up: contents](index.md) · [Model →](02-model.md)
