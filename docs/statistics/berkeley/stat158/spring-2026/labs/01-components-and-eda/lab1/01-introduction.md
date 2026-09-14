---
title: Introduction
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/01-components-and-eda/lab1.md
source_file: sources/berkeley-stat158/spring-2026/labs/01-components-and-eda/lab1.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`labs/01-components-and-eda/lab1.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/01-components-and-eda/lab1.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

## Introduction

Welcome to Stat 158! The goal of this exercise is to better understand
the key components of an experiment by comparing concepts from lecture
to a real study. The domain and setting of the research question often
impose unique constraints, leading to different approaches to designing
an experiment. We examine these below, before starting to work with the
data ourselves.

## Understanding the Experiment

We will be working with data from the Karlan and List (2007) study,
which investigates how matching grants affects charitable giving using a
large-scale experiment. Read through the paper while keeping a lookout
for concepts from lecture, and try to understand the motivations for
their design based on their setting and constraints. Use this to answer
the following questions in complete sentences.

1.  Identify and list the four components of the experimental design
    they used, i.e.

    -   The Nature of the Treatments.

    -   Choice of the Experimental Units.

    -   Manner of Assigning Units to Treatments

    -   The Nature of the Response

\
\
\
\
\
\
\
\
\
\

2.  What is the underlying research question? Please be as precise as
    possible.\

\
\
\
\
\

3.  Why does this study use a *natural* field experiment rather than a
    traditional *lab* experiment? List one advantage and disadvantage of
    using natural experiments over lab experiments.\

\
\
\
\
\
\

4.  List any three changes in design you think may benefit the study.
    What are their advantages?

\
\
\
\
\
\
\
\
\

5.  What is the population that the results of this study would
    generalize to? Are there any limitations to this because of the
    design?

\
\
\
\



### Exploratory Data Analysis

The dataset is stored in a `.csv` file. To load it into `R`, you'll need
the `readr` package, which is included inside the `tidyverse`. If you
haven't installed the tidyverse before, you can do so by running
`install.packages("tidyverse")` once.

Once you've installed the package, you can load it by running the
following line.

::: cell
``` {.r .cell-code}

---

[Up: contents](index.md) · [load tidyverse (includes readr for CSVs) →](02-load-tidyverse-includes-readr-for-csvs.md)
