---
title: Data wrangling with dplyr
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data wrangling with dplyr

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(dplyr)
```


The `dplyr` package provides us with a large set of
functions for handling our data. We refer to the
preliminary_tidyverse.Rmd file for a more detailed
description of these functions.

The most important `dplyr` functions to remember are:

`dplyr` verbs | Description |
--- | ------------------------------------------------------------------------------------ |
`select()` | select columns  |
`filter()` | filter rows |
`arrange()` | re-order or arrange rows |
`mutate()` | create new columns |
`summarize()` | summarize values |
`group_by()` | allows for group operations in the "split-apply-combine" concept |

In addition, `dplyr` uses the pipe operator `%>%` to
use the output of one function as an input to the next
function. Instead of nesting functions (reading from the
inside to the outside), the idea of of piping is to
read the functions from left to right.

## Select and filter

Here we will demonstrate the `dplyr` functionalities with
a couple of small examples.

Let's say we want to investigate how many subjects are
1. men that
2. are older than 18 years old,
3. are taller than 150 cm, and
4. have weight of less than 80kg

```r
NHANES %>%
  select(c("Gender","Age","Weight","Height")) %>% ## select the columns of interest
  filter(Gender == "male",
         Age > 18,
         Height > 150,
         Weight < 80) %>% ## filter observations (rows) based on the required values
  nrow()
```

Filtering the dataset based on thee three filtering criteria
retain 3.601 subjects. Note that the `select` step was not
strictly necessary, but since we could answer the question
based on only these 4 columns, there is no need to retain the
the rest of the data (if this is the only question).

## Arrange

Next question; Within the Race1 category of Hispanics, select
men that are not married and display the first five by
descending height.

**Hint**: use the `desc()` function inside of
`arrange()` to order rows in a descending order.
Use the base R function `head` to display the first
five.

```r
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  arrange(desc(Height)) %>%
  head(n=5)
```

We have successfully combined three of the main `dplyr`
functionalities. Let's try to explore another one!

## Mutate

Assume that we don't trust the BMI values in our dataset
and we decide to calculate them ourselves. BMI is typically
calculated by taking a person's weight (in kg) and dividing
it by the its height (in m) squared. Based on this rule,
generate a new column, BMI_self, for the subset of the
NHANES dataset that we obtained from the previous question.
To create new columns, we will use the `mutate()` function
in `dplyr`.

```r
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height","Weight","BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight/(Height/100)**2)
```

Note that now we need to include the _Weight_ and _BMI_
columns in the `select` statement, because we need that
input for the `mutate` function. Good news: It turns out
that the BMI column in the original dataset was computed
correctly after all! But now we are interested in the
mean value of the BMI_Self column. This requires a fifth
`dplyr` function: `summarize()`.


## summarize

Given the filtering of the question above, compute the mean
value of the BMI_self column.

```r
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height","Weight","BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight/(Height/100)**2) %>%
  summarize(avg_BMI_self = mean(BMI_self, na.rm = TRUE))
## the addition argument na.rm = TRUE makes sure to remove missing
## values for the purpose of calculating the mean
```

For this particular subset of the data, we find an
average BMI value of 28.59 kg/m**2.

There are many other summary statistics you
could consider such `sd()`, `min()`, `median()`,
`max()`, `sum()`, `n()` (returns the length of vector),
`first()` (returns first value in vector),
`last()` (returns last value in vector) and
`n_distinct()` (number of distinct values in vector).
We will elaborate on these functions later.

Note that choosing the most informative summary statistic
is very important! This can be shown with the following example;

** change location to github location **
![/Users/jg/Desktop/PhD/Teaching/Lisbon_2020/psls20/data/Figure_partners.png){width=60%}

In this study, men and woman were asked about their
"ideal number of partners desired over 30 years".
While almost all subjects desired a number between 0 and 50,
three male subjects selected a number above 100.
These three _outliers_ in the data can have a large impact on
the data analysis, especially when we work with summary
statistics that are sensitive to these outliers.

When we look at the _mean_, for instance, we see that on average
woman desire 2.8 partners, while men desire 64.3 partners on average,
suggesting a large discrepancy between male and female desires.

However, if look at a more _robust_ summary statistic such as
the _median_, we see that the result is 1 for both men and woman.
It is clear that the mean value was completely distorted by the
three outliers in the data.

Another example of a more robust summary statistic is
the _geometric mean_.


## Group

We have already combined 5 very important functions. Here
we will add a final one: `group_by()`.

The `group_by()` verb is and incredibly powerful
function in `dplyr`. It allows us, for example,
to calculate summary statistics for different
groups of observations.

If we take our example from above, let's say
we want to split the data frame by some variable
(e.g. `MaritalStatus`), apply a function (`mean`)
to a column (e.g. BMI_self) of the individual
data frames  and then combine the output back into
a summary data frame.

```r
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height","Weight","BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight/(Height/100)**2) %>%
  group_by(MaritalStatus) %>% ##  group the subjects by their marital status
  summarize(avg_BMI_self = mean(BMI_self, na.rm = TRUE)) ## calculate the mean BMI_self value of each group
```

We have successfully combined six of the most important
`dplyr` functionalities!

Now that we have all the required functions for
importing, tidying and wrangling data in place,
we will learn how to visualize our data with the
ggplot2 package.

---

[← Data Tidying](04-data-tidying.md) · [Up: contents](index.md) · [Data Visualization →](06-data-visualization.md)
