---
title: '3. Breastcancer Gene Expression Study: KPNA2 gene'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/multipleRegression_KPNA2_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/multipleRegression_KPNA2_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Breastcancer Gene Expression Study: KPNA2 gene

**Source:** [`tutorialScripts/excercises/08_multipleRegression/multipleRegression_KPNA2_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/multipleRegression_KPNA2_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(include = TRUE, comment = NA, echo = TRUE,
                      message = FALSE, warning = FALSE)
library(tidyverse)
```

#Background
Background: Histologic grade in breast cancer provides clinically important prognostic information. Researchers examined whether histologic grade was associated with gene expression profiles of breast cancers and whether such profiles could be used to improve histologic grading. In this tutorial we will assess the association between histologic grade and the expression of the KPNA2 gene that is known to be associated with poor BC prognosis.
The patients, however, do not only differ in the histologic grade, but also on their lymph node status.
The lymph nodes were not affected (0) or chirugically removed (1).


#Data analysis
##Import KPNA2 data in R
```r
kpna2 <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/kpna2.txt")
kpna2
```

##Transform the variable grade and node to a factor
```r
```

##Data exploration
Histologic grade and lymph node status can be associated with the kpna2 gene expression. Moreover, it is also possible that the differential expression associated with histological grade is different in patients that have unaffected lymph nodes and patients for which the lymph nodes had to be removed.

```r
```

What does the plot suggests

## Model

1. Specify the model, interpret each model parameter in the model.
2. Formulate the relevant research questions
3. Translate them in a null and alternative hyptheses.
4. Perform the hypothesis tests  and calculate the confidence intervals.

# Formulate your conclusions in terms of the research question

---

[Up: contents](../../../index.md)
