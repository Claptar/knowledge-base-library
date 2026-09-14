---
title: Breast cancer dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Breast cancer dataset

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Subset of study https://doi.org/10.1093/jnci/djj052

- 32 breast cancer patients with estrogen recepter positieve tumor that had tamoxifen chemotherapy. Variabels:

    - grade: histological grade of tumor (grade 1 vs 3),
    - node: lymph node status  (0: not affected, 1: lymph nodes affected and removed),
    - size: tumor size in cm,
    - ESR1 and S100A8 gene expression in tumor biopsy (microarray technology)


```r
brca <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/breastcancer.csv")
brca
```

- For didactical reasons we first remove 3 outliers in the S100A8 expression data.
- Later in the lecture we will show how to properly deal with all data.


```r
brca %>% ggplot(aes(x="",y=S100A8)) +
geom_boxplot()
```

---

```r
library(GGally)
brcaSubset<-brca %>% filter(S100A8<2000)
brcaSubset[,-(1:4)] %>% ggpairs()
```

## Association between ESR1 and S100A8 expressie

- ESR1 in $\pm$ 75% of breast cancer tumors.

    - Expression of ER gene positive for treatment: tumor responds to hormone therapy
    - Tamoxifen interacts with ER and modulates gene expression.

- Proteins of S100 family often dysregulated in cancer

      - S100A8 expressie represses immune systeem in tumor en creates an environment of inflamation that promotes tumor growth.

- Assess association between ESR1 and S100A8 expression.

1. pipe dataset to ggplot
2. select data `ggplot(aes(x=ESR1,y=S100A8))`
3. add points `geom_point()`
4. add smooth line `geom_smooth()`

```r
brcaSubset %>%
  ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth()
```

---

[Up: contents](index.md) · [Lineair Regression →](02-lineair-regression.md)
