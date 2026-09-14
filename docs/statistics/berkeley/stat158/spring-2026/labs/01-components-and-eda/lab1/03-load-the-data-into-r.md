---
title: load the data into R
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/01-components-and-eda/lab1.md
source_file: sources/berkeley-stat158/spring-2026/labs/01-components-and-eda/lab1.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# load the data into R

**Source:** [`labs/01-components-and-eda/lab1.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/01-components-and-eda/lab1.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

donations <- read_csv("https://stat158.berkeley.edu/spring-2026/labs/01-components-and-eda/donations.csv")
```
:::

6.  Take some time to acquaint yourself with the data; this process of
    exploratory data analysis is very important. Some basic questions to
    consider:

    -   What do each of the columns and rows represent?
    -   What are the units of measurement?
    -   What datatypes are used for each column?

7.  Often when working with categorical variables in our data, it is
    useful to convert them to the 'factor' data structure in R. This is
    easily done in base R with `df$col <- as.factor(df$col)` or with the
    `mutate()` function in the `tidyverse` . Convert the "treatment" and
    "control" columns to factors.

    ::: cell
    ``` {.r .cell-code}
    # convert columns to factor here
    ```
    :::

8.  Answer the following questions from the data:

    -   Are there any missing values?
    -   How are the data distributed in the sample?
    -   Are there any outlying values?

    Note that, for our purposes, we are interested only in the columns
    labeled "treatment," "control," and "amount." However, you may find
    it interesting to explore the rest of the data. Graphs such as
    barplots and density plots, contingency tables and summary
    statistics may be good starting points.

    ::: cell
    ``` {.r .cell-code}
    # save any exploratory analysis you do here
    ```
    :::

9.  Create a visualization that aims to convey broadly the effect of the
    treatment on the outcome here. This could be in the form of a graph
    or a table. Aim to convey a simple message clearly, and feel free to
    be creative!

    ::: cell
    ``` {.r .cell-code}
    # save the final visualization of treatment effect here
    ```
    :::

---

[← load tidyverse (includes readr for CSVs)](02-load-tidyverse-includes-readr-for-csvs.md) · [Up: contents](index.md)
