---
title: Data Tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Tidying

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

[← or glimpse(NHANES) to see all the variables in the dataset](03-or-glimpse-nhanes-to-see-all-the-variables-in-the-dataset.md) · [Up: contents](index.md) · [Data wrangling with dplyr →](05-data-wrangling-with-dplyr.md)
