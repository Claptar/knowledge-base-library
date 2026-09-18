---
title: The NHANES dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The NHANES dataset

In this tutorial, we will learn how to import, tidy, wrangle and
visualize data. We will work with one specific dataset;

The National Health and Nutrition Examination Survey (NHANES)
contains data that has been collected since 1960. For this tutorial,
we will make use of the data that were collected between 2009 and
2012, for 10.000 U.S. civilians. The dataset contains a large number of
physical, demographic, nutritional and life-style-related parameters.

However, before we can actually start working with data, we will need to
learn how to import the required datasets into our Rstudio environment.

## Data Import  with the `readr` R package

```r
library(readr)
```

Let's try reading in some data. We will begin by
reading in the `NHANES.csv` dataset.

```r
NHANES <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv")
```

```r
head(NHANES) ## take a look at the first rows of the dataset
```

```r
tail(NHANES) ## take a look at the last rows of the dataset
```

```r
#knitr::kable(NHANES[c(1,4,5,6,7,8),c(1,3,4,7,17,20,21,25)],format = "markdown")
NHANES[c(1,4,5,6,7,8),c(1,3,4,7,17,20,21,25)] ## take a look at a subset of the dataset
```

### Take a `glimpse()` at your data

The glimpse function allows us to (obviously) take
a first, informative glimpse at our data. The function
is part of the `dplyr`, which we will explore in much
more detail below!

```r
dplyr::glimpse(NHANES[,1:10])
# or glimpse(NHANES) to see all the variables in the dataset
```

## Data Tidying

```r
library(tidyverse)
```

** Important **
If you are not familiar yet with the concepts of tidy data,
have a look at the preliminary_tidyverse.Rmd file!

If we consider our `NHANES` dataframe, we see it is already in
a tidy format, as;

* Each variable forms a column.
* Each observation forms a row.
* Each type of observational unit forms a table.

Each row contains all of the information on
a single subject (US civilian) in the study.

In the next tutorial, we will work with a dataset on the
effects of a certain drug, _captopril_, on the systolic
and diastolic blood pressure of patients. This will not be
a _tidy_ dataset. As such, the details of tidying data
with tidyverse will be described there

---

[Up: contents](index.md) · [Data wrangling with dplyr →](02-data-wrangling-with-dplyr.md)
