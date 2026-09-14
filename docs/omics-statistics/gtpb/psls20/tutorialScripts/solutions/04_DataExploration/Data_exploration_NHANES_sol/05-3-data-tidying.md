---
title: 3 Data Tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Data Tidying

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

``` {.sourceCode .r}
library(tidyverse)
```

    ## -- Attaching packages ---- tidyverse 1.2.1 --

    ## v ggplot2 3.2.1     v purrr   0.3.3
    ## v tibble  2.1.3     v dplyr   0.8.2
    ## v tidyr   0.8.3     v stringr 1.4.0
    ## v ggplot2 3.2.1     v forcats 0.4.0

    ## -- Conflicts ------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

\*\* Important \*\* If you are not familiar yet with the concepts of tidy data, have a look at the preliminary\_tidyverse.Rmd file!

If we consider our `NHANES` dataframe, we see it is already in a tidy format, as;

- Each variable forms a column.
- Each observation forms a row.
- Each type of observational unit forms a table.

Each row contains all of the information on a single subject (US civilian) in the study.

In the next tutorial, we will work with a dataset on the effects of a certain drug, *captopril*, on the systolic and diastolic blood pressure of patients. This will not be a *tidy* dataset. As such, the details of tidying data with tidyverse will be described there

---

[← or glimpse(NHANES) to see all the variables in the dataset](04-or-glimpse-nhanes-to-see-all-the-variables-in-the-dataset.md) · [Up: contents](index.md) · [4 Data wrangling with dplyr →](06-4-data-wrangling-with-dplyr.md)
