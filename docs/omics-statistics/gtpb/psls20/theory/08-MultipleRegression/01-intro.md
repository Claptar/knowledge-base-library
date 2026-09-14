---
title: Intro
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd
source_file: sources/gtpb-psls20/theory/08-MultipleRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Intro

**Source:** [`theory/08-MultipleRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Until now: one outcome $Y$ and a single  predictor $X$.
- Often useful to use multiple predictors to model the response. e.g

1. Association between X and Y is affected by confounder: Smoking and age by youngsters are confounded and they both affect the lung capacity
2. Which group of variables is associated with a given outcome. E.g Habitat and human activity on the biodiversity of the rain forest. (Size, age, height of the wood $\rightarrow$ assess all effects simultaneously.
3. Prediction of outcome for individuals: use as many predictive information simultaneously. E.g prediction of risk on mortality is used on a daily basis in intensive care units to prioritise patient care.

$\rightarrow$ Extend simple linear regression to multiple predictors.

---

## Prostate cancer example

- Prostate specific antigen (PSA) and a number of clinical variables for 97 males with radical prostatectomy.
- Association of PSA by

    - tumor volume (lcavol)
    - prostate weight (lweight)
    - age
    - benign prostate hypertrophy  (lbph)
    - seminal vesicle invasion (svi)
    - capsular penetration (lcp)
    - Gleason score (gleason)
    - precentage gleason score 4/5 (pgg45)

---

```r
prostate<-read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/prostate.csv")
prostate
prostate$svi<-as.factor(prostate$svi)
```

---

```r
library(GGally)
prostate %>% select(-pgg45)  %>% ggpairs()
```

---

---

[Up: contents](index.md) · [Additive multiple linair model →](02-additive-multiple-linair-model.md)
