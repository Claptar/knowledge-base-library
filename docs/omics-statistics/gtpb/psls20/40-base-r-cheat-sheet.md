---
title: "40. Base R Cheat Sheet"
course: "GTPB Psls20"
chapter: 40
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 40. Base R Cheat Sheet

## What this covers

This chapter is a reference sheet, not a worked lecture: it collects the base R syntax that the
rest of the course relies on, so that a specific command can be looked up while working through
the statistics material rather than relearned from scratch each time. It assumes only that R and
RStudio are installed, and it does not motivate *why* each function exists — for that, see the
data-analysis chapters that actually use these commands. What follows groups the commands by task:
getting help, working with vectors, control flow, reading and writing data, matrices, lists, data
frames, strings, factors, fitting simple statistical models, probability distributions, plotting
and dates.

## Getting help

### Accessing the help files

- `?mean` — get help for a particular function.
- `help.search('weighted mean')` — search the help files for a word or phrase.
- `help(package = 'dplyr')` — find help for a package.

### More about an object

- `str(iris)` — get a summary of an object's structure.
- `class(iris)` — find the class an object belongs to.

## Using libraries

- `install.packages('dplyr')` — download and install a package from CRAN.
- `library(dplyr)` — load the package into the session, making all its functions available.
- `dplyr::select` — use a particular function from a package without loading the whole package.
- `data(iris)` — load a built-in dataset into the environment.

## Working directory

- `getwd()` — find the current working directory (where inputs are found and outputs are sent).
- `setwd('C://file/path')` — change the current working directory.

RStudio *projects* are the more reliable way to do this: opening a project sets the working
directory to the folder the project lives in, so paths inside a script stay valid regardless of
where RStudio was launched from.

## Vectors

### Creating vectors

| Code | Result | Description |
| :--- | :--- | :--- |
| `c(2, 4, 6)` | `2 4 6` | Join elements into a vector |
| `2:6` | `2 3 4 5 6` | An integer sequence |
| `seq(2, 3, by=0.5)` | `2.0 2.5 3.0` | A sequence with an arbitrary step |
| `rep(1:2, times=3)` | `1 2 1 2 1 2` | Repeat a whole vector |
| `rep(1:2, each=3)` | `1 1 1 2 2 2` | Repeat each element of a vector |

### Vector functions

- `sort(x)` — return `x` sorted.
- `rev(x)` — return `x` reversed.
- `table(x)` — see counts of each value.
- `unique(x)` — see the distinct values.

### Selecting vector elements

Elements can be selected by position, by value, or (for named vectors) by name.

**By position**

| Code | Description |
| :--- | :--- |
| `x[4]` | The fourth element. |
| `x[-4]` | All but the fourth. |
| `x[2:4]` | Elements two to four. |
| `x[-(2:4)]` | All elements except two to four. |
| `x[c(1, 5)]` | Elements one and five. |

**By value**

| Code | Description |
| :--- | :--- |
| `x[x == 10]` | Elements equal to 10. |
| `x[x < 0]` | All elements less than zero. |
| `x[x %in% c(1, 2, 5)]` | Elements in the set $\{1, 2, 5\}$. |

**Named vectors**

| Code | Description |
| :--- | :--- |
| `x['apple']` | The element named `'apple'`. |

## Programming: loops, conditionals and functions

The three control-flow constructs and function definition follow the same pattern in R as in most
languages: a keyword, a condition or sequence in parentheses, and a body in braces.

**For loop**

```r
for (variable in sequence){
  Do something
}
```

Example:

```r
for (i in 1:4){
  j <- i + 10
  print(j)
}
```

**While loop**

```r
while (condition){
  Do something
}
```

Example:

```r
while (i < 5){
  print(i)
  i <- i + 1
}
```

**If statement**

```r
if (condition){
  Do something
} else {
  Do something different
}
```

Example:

```r
if (i > 3){
  print('Yes')
} else {
  print('No')
}
```

**Function definition**

```r
function_name <- function(var){
  Do something
  return(new_variable)
}
```

Example:

```r
square <- function(x){
  squared <- x*x
  return(squared)
}
```

### Conditions

The comparisons used inside `if` and `while` conditions:

| Code | Description | Code | Description |
| :--- | :--- | :--- | :--- |
| `a == b` | Are equal | `a >= b` | Greater than or equal to |
| `a != b` | Not equal | `a <= b` | Less than or equal to |
| `a > b` | Greater than | `is.na(a)` | Is missing |
| `a < b` | Less than | `is.null(a)` | Is null |

## Reading and writing data

Each reader function has a matched writer:

| Input | Output | Description |
| :--- | :--- | :--- |
| `df <- read.table('file.txt')` | `write.table(df, 'file.txt')` | Read and write a delimited text file. |
| `df <- read.csv('file.csv')` | `write.csv(df, 'file.csv')` | Read and write a comma-separated value file — a special case of `read.table`/`write.table`. |
| `load('file.RData')` | `save(df, file = 'file.Rdata')` | Read and write an R data file, a file format specific to R. |

## Data types

Base R distinguishes logical, numeric, character and factor types, and conversion moves in one
direction along a fixed order — it is always possible to go from a *higher* type in the table below
to a *lower* one, but not reliably the other way:

| Type | Example | Description |
| :--- | :--- | :--- |
| `as.logical` | `TRUE, FALSE, TRUE` | Boolean values (`TRUE` or `FALSE`). |
| `as.numeric` | `1, 0, 1` | Integers or floating-point numbers. |
| `as.character` | `'1', '0', '1'` | Character strings — generally preferred to factors. |
| `as.factor` | `'1', '0', '1'`, levels `'1', '0'` | Character strings with a preset, fixed set of levels — needed for some statistical models. |

## Maths and summary functions

| Code | Description | Code | Description |
| :--- | :--- | :--- | :--- |
| `log(x)` | Natural log. | `sum(x)` | Sum. |
| `exp(x)` | Exponential. | `mean(x)` | Mean. |
| `max(x)` | Largest element. | `median(x)` | Median. |
| `min(x)` | Smallest element. | `quantile(x)` | Percentage quantiles. |
| `round(x, n)` | Round to `n` decimal places. | `rank(x)` | Rank of elements. |
| `signif(x, n)` | Round to `n` significant figures. | `var(x)` | Variance. |
| `cor(x, y)` | Correlation. | `sd(x)` | Standard deviation. |

## Variable assignment

Assignment uses `<-`, and typing a bare name at the console prints its value:

```r
> a <- 'apple'
> a
[1] 'apple'
```

## The environment

- `ls()` — list all variables currently in the environment.
- `rm(x)` — remove `x` from the environment.
- `rm(list = ls())` — remove every variable from the environment.

RStudio's *Environment* panel is a way to browse these variables without typing `ls()`.

## Matrices

- `m <- matrix(x, nrow = 3, ncol = 3)` — create a matrix from `x`.
- `m[2, ]` — select a row.
- `m[ , 1]` — select a column.
- `m[2, 3]` — select a single element.
- `t(m)` — transpose.
- `m %*% n` — matrix multiplication.
- `solve(m, n)` — find $x$ in $m \cdot x = n$.

## Lists

A list is a collection of elements that need not all be the same type:

```r
l <- list(x = 1:5, y = c('a', 'b'))
```

| Code | Description |
| :--- | :--- |
| `l[[2]]` | The second element of `l` itself. |
| `l[1]` | A new list containing only the first element. |
| `l$x` | The element named `x`. |
| `l['y']` | A new list containing only the element named `y`. |

The distinction between `[[ ]]` and `[ ]` matters throughout: double brackets pull the element out,
single brackets return a smaller list.

## Data frames

A data frame is a special case of a list in which every element (column) has the same length —
this is what makes it behave like a table:

```r
df <- data.frame(x = 1:3, y = c('a', 'b', 'c'))
```

| x | y |
| :--- | :--- |
| 1 | a |
| 2 | b |
| 3 | c |

Because a data frame is *both* a list of columns and a table of rows and columns, it can be
subset either way.

**Understanding a data frame**

- `View(df)` — see the full data frame.
- `head(df)` — see the first 6 rows.
- `nrow(df)` — number of rows.
- `ncol(df)` — number of columns.
- `dim(df)` — number of rows and columns together.

**Matrix-style subsetting** (by row and column position): `df[ , 2]`, `df[2, ]`, `df[2, 2]`.

**List-style subsetting** (by column): `df$x`, `df[[2]]`.

**Combining data frames**: `cbind` binds columns together side by side; `rbind` stacks rows.

The **dplyr** package covers the same operations with a more readable syntax and is worth using
alongside base R for data frame work.

## Strings

- `paste(x, y, sep = ' ')` — join multiple vectors together, element by element.
- `paste(x, collapse = ' ')` — join the elements of a single vector into one string.
- `grep(pattern, x)` — find regular-expression matches in `x`.
- `gsub(pattern, replace, x)` — replace matches in `x` with a string.
- `toupper(x)` / `tolower(x)` — convert case.
- `nchar(x)` — number of characters in a string.

The **stringr** package offers a more consistent set of string functions built on the same ideas.

## Factors

- `factor(x)` — turn a vector into a factor; the levels and their order can be set explicitly.
- `cut(x, breaks = 4)` — turn a numeric vector into a factor by cutting it into sections (bins).

## Statistics

- `lm(x ~ y, data=df)` — fit a linear model.
- `glm(x ~ y, data=df)` — fit a generalised linear model.
- `summary(...)` — get detailed information out of a fitted model.
- `t.test(x, y)` — test for a difference between two means.
- `pairwise.t.test(...)` — t-test for paired data.
- `prop.test(...)` — test for a difference between proportions.
- `aov(...)` — analysis of variance.

## Probability distributions

Every named distribution in R comes with the same family of four functions, distinguished by
their first letter — `r` for a random draw, `d` for the density, `p` for the cumulative
distribution, `q` for the quantile:

| Distribution | Random variates | Density function | Cumulative distribution | Quantile |
| :--- | :--- | :--- | :--- | :--- |
| Normal | `rnorm` | `dnorm` | `pnorm` | `qnorm` |
| Poisson | `rpois` | `dpois` | `ppois` | `qpois` |
| Binomial | `rbinom` | `dbinom` | `pbinom` | `qbinom` |
| Uniform | `runif` | `dunif` | `punif` | `qunif` |

## Plotting

- `plot(x)` — values of `x` in order.
- `plot(x, y)` — values of `x` against `y`.
- `hist(x)` — a histogram of `x`.

The **ggplot2** library is the richer alternative used for the course's own figures.

## Dates

Base R's date handling is not covered here beyond noting that it exists; the **lubridate** library
is the recommended tool for working with dates.

## Sources

- `docs/omics-statistics/gtpb/psls20/background_material/r-cheatsheet.md` — the course's Base R
  Cheat Sheet (background material, CC BY 4.0), reconstructed from
  `background_material/r-cheatsheet.pdf` in the GTPB/PSLS20 repository. The conversion notes that
  it was produced by a model reading a PDF with no text layer, so it is treated here as reference
  material rather than a verified source. The **dplyr**, **stringr**, **ggplot2** and **lubridate**
  packages are mentioned as further tools but their own documentation is not part of this material.

---

[← 39. KPNA2 Gene Expression Study](39-kpna2-gene-expression-study.md) · [Contents](index.md) · [41. The R Markdown Workflow →](41-the-r-markdown-workflow.md)
