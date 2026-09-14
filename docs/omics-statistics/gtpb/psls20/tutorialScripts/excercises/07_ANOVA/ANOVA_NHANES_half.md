---
title: 'Tutorial 7.3: ANOVA in the NHANES dataset'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_NHANES_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_NHANES_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Tutorial 7.3: ANOVA in the NHANES dataset

**Source:** [`tutorialScripts/excercises/07_ANOVA/ANOVA_NHANES_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_NHANES_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

To experiment more with the concepts of ANOVA, we will perform a short analysis on the NHANES dataset.

# The NHANES dataset

The National Health and Nutrition Examination Survey (NHANES) contains data that has been collected since 1960. For this tutorial, we will make use of the data that were collected between 2009 and 2012, for 10.000 U.S. civilians. The dataset contains a large number of physical, demographic, nutritional and life-style-related parameters.

# Goal

In the NHANES dataset, one of the columns is named `HealthGen`.
HealthGen is a self-reported rating of a participant's health
in general terms. HealthGen is reported for participants aged 12
years or older. It is a factor with the following levels:
Excellent, Vgood, Good, Fair, or Poor.

We want to assess if the systolic blood pressure
value (take column `BPSys1`) is equal between the five self-reported
health categories. To this end, we will use an ANOVA analysis
(if the required assumptions are met).

# Load the required libraries

```r
```

# Data import

```r
```

# Data Exploration

To get a more informative and intuitive visualization, you can:

1. Filter out subjects with NA values for HealthGen or BPSys1
2. Set HealthGen to a factor and relevel it to Poor --> Excellent

**Hint:** The second task can be achieved by using the `mutate`,
`as.factor` and `fct_relevel` functions.

```r
```


1. What do you observe from the data exploration?

2. How will you model the data?

3. Translate the research question in a null and alternative hypothesis

4. Which test will you use to assess the research hypothesis?

5. Formulate the assumptions of the test and assess the assumptions using diagnostic
plots.

6. If all assumptions to perform the test are met, complete the analysis and
formulate a proper conclusion. If the assumptions are not met (immediately), can
you think about the concepts we discussed in the theory to tackle this issue?

---

[Up: contents](../../../index.md)
