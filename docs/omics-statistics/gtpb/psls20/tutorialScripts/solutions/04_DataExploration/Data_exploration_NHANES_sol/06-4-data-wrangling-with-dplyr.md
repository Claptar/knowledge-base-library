---
title: 4 Data wrangling with dplyr
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Data wrangling with dplyr

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

``` {.sourceCode .r}
library(dplyr)
```

The `dplyr` package provides us with a large set of functions for handling our data. We refer to the preliminary\_tidyverse.Rmd file for a more detailed description of these functions.

The most important `dplyr` functions to remember are:

| `dplyr` verbs | Description |
|----|----|
| `select()` | select columns |
| `filter()` | filter rows |
| `arrange()` | re-order or arrange rows |
| `mutate()` | create new columns |
| `summarize()` | summarize values |
| `group_by()` | allows for group operations in the “split-apply-combine” concept |

In addition, `dplyr` uses the pipe operator `%>%` to use the output of one function as an input to the next function. Instead of nesting functions (reading from the inside to the outside), the idea of of piping is to read the functions from left to right.

## <span class="header-section-number">4.1</span> Select and filter

Here we will demonstrate the `dplyr` functionalities with a couple of small examples.

Let’s say we want to investigate how many subjects are 1. men that 2. are older than 18 years old, 3. are taller than 150 cm, and 4. have weight of less than 80kg

``` {.sourceCode .r}
NHANES %>%
  select(c("Gender","Age","Weight","Height")) %>% ## select the columns of interest
  filter(Gender == "male",
         Age > 18,
         Height > 150,
         Weight < 80) %>% ## filter observations (rows) based on the required values
  nrow()
```

    ## [1] 1286

Filtering the dataset based on thee three filtering criteria retain 3.601 subjects. Note that the `select` step was not strictly necessary, but since we could answer the question based on only these 4 columns, there is no need to retain the the rest of the data (if this is the only question).

## <span class="header-section-number">4.2</span> Arrange

Next question; Within the Race1 category of Hispanics, select men that are not married and display the first five by descending height.

**Hint**: use the `desc()` function inside of `arrange()` to order rows in a descending order. Use the base R function `head` to display the first five.

``` {.sourceCode .r}
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  arrange(desc(Height)) %>%
  head(n=5)
```

    ## # A tibble: 5 x 4
    ##   Race1    Gender MaritalStatus Height
    ##   <chr>    <chr>  <chr>          <dbl>
    ## 1 Hispanic male   NeverMarried    197.
    ## 2 Hispanic male   NeverMarried    190.
    ## 3 Hispanic male   NeverMarried    182.
    ## 4 Hispanic male   NeverMarried    181.
    ## 5 Hispanic male   NeverMarried    180.

We have successfully combined three of the main `dplyr` functionalities. Let’s try to explore another one!

## <span class="header-section-number">4.3</span> Mutate

Assume that we don’t trust the BMI values in our dataset and we decide to calculate them ourselves. BMI is typically calculated by taking a person’s weight (in kg) and dividing it by the its height (in m) squared. Based on this rule, generate a new column, BMI\_self, for the subset of the NHANES dataset that we obtained from the previous question. To create new columns, we will use the `mutate()` function in `dplyr`.

``` {.sourceCode .r}
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height","Weight","BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight/(Height/100)**2)
```

    ## # A tibble: 107 x 7
    ##    Race1    Gender MaritalStatus Height Weight   BMI BMI_self
    ##    <chr>    <chr>  <chr>          <dbl>  <dbl> <dbl>    <dbl>
    ##  1 Hispanic male   Divorced        177.  114.   36.3     36.3
    ##  2 Hispanic male   Divorced        177.  114.   36.3     36.3
    ##  3 Hispanic male   NeverMarried    190.  125.   34.7     34.7
    ##  4 Hispanic male   NeverMarried    176.  161.   52.1     52.1
    ##  5 Hispanic male   LivePartner     164.   88.2  32.8     32.8
    ##  6 Hispanic male   LivePartner     164.   88.2  32.8     32.8
    ##  7 Hispanic male   NeverMarried    162.   78.5  30.0     30.0
    ##  8 Hispanic male   Divorced        173.   95.4  31.8     31.8
    ##  9 Hispanic male   LivePartner     179.   92.8  28.9     28.9
    ## 10 Hispanic male   LivePartner     179.   92.8  28.9     28.9
    ## # ... with 97 more rows

Note that now we need to include the *Weight* and *BMI* columns in the `select` statement, because we need that input for the `mutate` function. Good news: It turns out that the BMI column in the original dataset was computed correctly after all! But now we are interested in the mean value of the BMI\_Self column. This requires a fifth `dplyr` function: `summarize()`.

## <span class="header-section-number">4.4</span> summarize

Given the filtering of the question above, compute the mean value of the BMI\_self column.

``` {.sourceCode .r}
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height","Weight","BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight/(Height/100)**2) %>%
  summarize(avg_BMI_self = mean(BMI_self, na.rm = TRUE))
```

    ## # A tibble: 1 x 1
    ##   avg_BMI_self
    ##          <dbl>
    ## 1         28.8

``` {.sourceCode .r}
## the addition argument na.rm = TRUE makes sure to remove missing
## values for the purpose of calculating the mean
```

For this particular subset of the data, we find an average BMI value of 28.59 kg/m\*\*2.

There are many other summary statistics you could consider such `sd()`, `min()`, `median()`, `max()`, `sum()`, `n()` (returns the length of vector), `first()` (returns first value in vector), `last()` (returns last value in vector) and `n_distinct()` (number of distinct values in vector). We will elaborate on these functions later.

Note that choosing the most informative summary statistic is very important! This can be shown with the following example;

\*\* change location to github location \*\* \![/Users/jg/Desktop/PhD/Teaching/Lisbon\_2020/psls20/data/Figure\_partners.png){width=60%}

In this study, men and woman were asked about their “ideal number of partners desired over 30 years”. While almost all subjects desired a number between 0 and 50, three male subjects selected a number above 100. These three *outliers* in the data can have a large impact on the data analysis, especially when we work with summary statistics that are sensitive to these outliers.

When we look at the *mean*, for instance, we see that on average woman desire 2.8 partners, while men desire 64.3 partners on average, suggesting a large discrepancy between male and female desires.

However, if look at a more *robust* summary statistic such as the *median*, we see that the result is 1 for both men and woman. It is clear that the mean value was completely distorted by the three outliers in the data.

Another example of a more robust summary statistic is the *geometric mean*.

## <span class="header-section-number">4.5</span> Group

We have already combined 5 very important functions. Here we will add a final one: `group_by()`.

The `group_by()` verb is and incredibly powerful function in `dplyr`. It allows us, for example, to calculate summary statistics for different groups of observations.

If we take our example from above, let’s say we want to split the data frame by some variable (e.g. `MaritalStatus`), apply a function (`mean`) to a column (e.g. BMI\_self) of the individual
data frames and then combine the output back into a summary data frame.

``` {.sourceCode .r}
NHANES %>%
  select(c("Race1", "Gender","MaritalStatus","Height","Weight","BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight/(Height/100)**2) %>%
  group_by(MaritalStatus) %>% ##  group the subjects by their marital status
  summarize(avg_BMI_self = mean(BMI_self, na.rm = TRUE)) ## calculate the mean BMI_self value of each group
```

    ## # A tibble: 5 x 2
    ##   MaritalStatus avg_BMI_self
    ##   <chr>                <dbl>
    ## 1 Divorced              28.4
    ## 2 LivePartner           29.0
    ## 3 NeverMarried          28.1
    ## 4 Separated             31.4
    ## 5 Widowed               30.6

We have successfully combined six of the most important `dplyr` functionalities!

Now that we have all the required functions for importing, tidying and wrangling data in place, we will learn how to visualize our data with the ggplot2 package.

---

[← 3 Data Tidying](05-3-data-tidying.md) · [Up: contents](index.md) · [5 Data Visualization →](07-5-data-visualization.md)
