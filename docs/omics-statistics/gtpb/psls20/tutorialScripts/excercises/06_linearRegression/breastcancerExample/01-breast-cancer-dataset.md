---
title: Breast cancer dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Breast cancer dataset

**Source:** [`tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[Up: contents](index.md) · [Research question →](02-research-question.md)
