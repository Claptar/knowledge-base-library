---
title: Summary of Analysis
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/04/reproducibleResearch.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/04/reproducibleResearch.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Summary of Analysis

**Source:** [`section/04/reproducibleResearch.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/04/reproducibleResearch.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Data was collected, processed, and merged using disparate files available from
the US Census. In particular, the authors had to combine location data using shape
files and distilled demographic data from question P22 in the census, which breaks
down households by family/non-family and the age of the head of household. The
data were merged using census-block identification numbers.

In the Cohort Location Model, the authors argue that changes in households’ housing
careers (i.e. housing consumption, residential mobility and location choices)
across the life span happen in a continuum and therefore they hypothesise that
such changes could create spatial sorting effects within metropolitan areas.

They test their model on the 50 largest US metropolitan regions (core based
statistical areas or CBSAs in the paper), deriving household age and location
from the 2010 Census. Distances were standardized against the farthest area from
each city center $\frac{\text{distance of block}}{\text{max(distance of block)}}$.

As overall household counts are not evenly distributed by the age of the householder,
simple counts of households at each location will not result in fair comparisons.
Therefore, to evaluate the location choices of a given age of a household, they
computed location quotients for each age group at each 1/100 of the standardised distance.

* $HH_{ij}$: Number of households labelled at age-group i and distance j from the city-center
* $HH_{.j}$: Number of households labelled at distance j from the city-center
* $HH_{i.}$: Number of households labelled at age-group i
* $HH_{..}$: Total number of households (in that city)

Location Quotient: $$LQ = \frac{ \big(\frac{HH_{ij}}{HH_{.j}}\big) } { \big(\frac{HH_{i.}}{HH_{..}}\big) }$$

Note: A LQ of 1 denotes that a given age cohort is represented at a given distance
in the same proportion as that age cohort is represented in the entire metropolitan
area. Location quotients (LQs) less (greater) than 1 indicate under(over)-representation
in a given area or at a given distance.

They compare distance from city-center against location quotient, fitting the
relationship using LOESS ("locally-smoothed line of best fit").

\newpage

---

[← Reproducible Research](01-reproducible-research.md) · [Up: contents](index.md) · [Questions →](03-questions.md)
