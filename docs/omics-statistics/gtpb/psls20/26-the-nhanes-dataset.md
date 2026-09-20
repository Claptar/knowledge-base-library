---
title: "26. The NHANES Dataset"
course: "GTPB Psls20"
chapter: 26
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 26. The NHANES Dataset

## What this covers

This chapter works through one dataset from start to finish: the National Health and Nutrition
Examination Survey (NHANES). It covers reading the data into R, checking that it is already in
"tidy" form, wrangling it with the six core `dplyr` verbs and the pipe operator, and visualizing
one variable and then two with `ggplot2`. It ends with a worked example that uses everything
together: building a normal reference interval for systolic blood pressure. It assumes basic R
and the idea of tidy data (each variable a column, each observation a row, each observational unit
a table) — a fuller treatment of tidy data is referenced in the course material but not covered
here.

## The dataset

NHANES has been collected in the US since 1960. The slice used in this chapter covers 2009–2012,
roughly 10,000 civilians, with a large number of physical, demographic, nutritional and
lifestyle-related variables recorded per person.

```r
library(readr)
NHANES <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv")
head(NHANES)
tail(NHANES)
```

`dplyr::glimpse()` is a quick way to see, for a handful of columns at a time, what type each
variable is and what its first few values look like — useful as a first orientation before any
analysis:

```r
dplyr::glimpse(NHANES[, 1:10])
```

**Is it tidy?** A dataset is tidy when each variable forms a column, each observation forms a row,
and each type of observational unit forms a table. NHANES already satisfies this: one row per
subject, one column per measured variable. That will not be true of every dataset in the course —
a later dataset on the blood-pressure drug captopril is *not* tidy, and the work of tidying it is
done when that dataset is introduced, not here.

## Wrangling with dplyr

Six verbs cover almost everything you need for reshaping a data frame:

| Verb | Does |
| --- | --- |
| `select()` | choose columns |
| `filter()` | choose rows |
| `arrange()` | reorder rows |
| `mutate()` | create new columns |
| `summarize()` | collapse values to a summary |
| `group_by()` | apply the above per group ("split–apply–combine") |

`dplyr` chains these with the pipe operator `%>%`, which takes the output of one step and feeds it
in as the input of the next. Instead of nesting function calls and reading from the inside out, a
pipe reads left to right, in the order the operations actually happen.

### select and filter

How many subjects are men, older than 18, taller than 150 cm, and weigh less than 80 kg?

```r
NHANES %>%
  select(c("Gender", "Age", "Weight", "Height")) %>%
  filter(Gender == "male", Age > 18, Height > 150, Weight < 80) %>%
  nrow()
```

This returns 3,601 subjects. The `select()` step is not strictly required — `filter()` would work
on the full table — but it is good practice to drop columns you don't need once you know which
ones answer the question.

### arrange

Within the `Race1 == "Hispanic"` category, take unmarried men and show the five tallest:

```r
NHANES %>%
  select(c("Race1", "Gender", "MaritalStatus", "Height")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  arrange(desc(Height)) %>%
  head(n = 5)
```

`arrange()` sorts ascending by default; wrapping the column in `desc()` sorts descending, and
`head(n = 5)` then keeps the first five rows.

### mutate

Suppose you don't trust the `BMI` column and want to recompute it yourself. BMI is weight in kg
divided by height in metres, squared. `mutate()` adds the result as a new column without dropping
the ones you started with:

```r
NHANES %>%
  select(c("Race1", "Gender", "MaritalStatus", "Height", "Weight", "BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight / (Height / 100)**2)
```

`Weight` and `BMI` have to be added back into the `select()` list here, because `mutate()` needs
`Weight` and `Height` as inputs, and `BMI` is kept so the recomputed column can be checked against
it. It turns out the original `BMI` column was correct all along.

### summarize

To go from a column of `BMI_self` values to a single number — its mean — use `summarize()`:

```r
NHANES %>%
  select(c("Race1", "Gender", "MaritalStatus", "Height", "Weight", "BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight / (Height / 100)**2) %>%
  summarize(avg_BMI_self = mean(BMI_self, na.rm = TRUE))
```

For this subset, the mean is 28.59 kg/m². `na.rm = TRUE` tells `mean()` to drop missing values
before averaging rather than propagate them as `NA`. Other summary functions built the same way
include `sd()`, `min()`, `median()`, `max()`, `sum()`, `n()` (length of the vector), `first()`,
`last()`, and `n_distinct()` (number of distinct values).

### Choosing the right summary statistic

Which summary you compute matters, and the wrong one can hide the actual shape of the data. In one
NHANES question, men and women were asked their "ideal number of partners desired over 30 years."
Almost every subject answered somewhere between 0 and 50 — except three male subjects, who answered
above 100. Those three points are enough to distort a summary statistic that is sensitive to
extreme values: the *mean* desired number of partners comes out to 2.8 for women and 64.3 for men,
suggesting an enormous discrepancy. The *median*, which is robust to a few extreme points, is 1 for
both sexes. The mean was not describing a real difference between men and women; it was describing
three outliers. The geometric mean is another statistic that resists distortion by extreme values
in the same way the median does. The lesson generalizes: before reporting a summary statistic,
check whether it is being driven by the bulk of the data or by a handful of extreme points.

### group_by

`group_by()` splits a data frame by one or more variables, applies a function within each group,
and returns the combined per-group results — the "split–apply–combine" pattern. Adding it to the
chain above computes the mean `BMI_self` separately for each level of `MaritalStatus`:

```r
NHANES %>%
  select(c("Race1", "Gender", "MaritalStatus", "Height", "Weight", "BMI")) %>%
  filter(MaritalStatus != "Married", Race1 == "Hispanic", Gender == "male") %>%
  mutate(BMI_self = Weight / (Height / 100)**2) %>%
  group_by(MaritalStatus) %>%
  summarize(avg_BMI_self = mean(BMI_self, na.rm = TRUE))
```

## Visualizing one variable with ggplot2

Base R has plotting functions (`plot()`, `boxplot()`, `hist()`, `qqplot()`, ...) that are fast for
a quick look at data. `ggplot2` is used through the rest of the course instead, because it makes
it comparatively easy for a beginner to build more complex, more legible plots.

The same variable — BMI, for the first 100 subjects with a non-missing value — is shown three
different ways below, and each reveals something the others don't.

### Dotplot

```r
NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n = 100) %>%
  ggplot(aes(x = BMI)) +
  geom_dotplot(method = "histodot")
```

Each subject's BMI is a point on the x-axis; points that fall in the same narrow bin stack up the
y-axis, so the height of a stack is a count. In the bin $[29.5, 30)$ there are 4 subjects. A plot
can be built "on the fly" like this, or stored as an object so extra layers can be added afterward:

```r
p <- NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n = 100) %>%
  ggplot(aes(x = BMI)) +
  geom_dotplot(method = "histodot")

p <- p + xlab("BMI (kg/m2)") + theme_bw()
p
```

Only store a plot you intend to reuse or add to later — otherwise it is wasted storage. The
dotplot does not show the mean or median directly; those have to be read off, or computed, in
addition to it.

### Histogram

```r
NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n = 100) %>%
  ggplot(aes(x = BMI)) +
  geom_histogram()
```

This carries the same information as the dotplot — the same bin $[29.5, 30)$ still contains 4
subjects — but the count is read directly off the bar height rather than counted point by point.
It still says nothing about the mean or median on its own.

### Boxplot

```r
NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n = 100) %>%
  ggplot(aes(x = "", y = BMI)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2)
```

<figure>
<svg viewBox="0 0 300 220" role="img" aria-label="Anatomy of a boxplot, showing the box, whiskers, and a point beyond the whisker plotted as an outlier">
  <line x1="40" y1="20" x2="40" y2="200" stroke="currentColor" stroke-width="1" opacity="0.35"/>
  <line x1="140" y1="188" x2="140" y2="156" stroke="currentColor" stroke-width="1.5"/>
  <line x1="125" y1="188" x2="155" y2="188" stroke="currentColor" stroke-width="1.5"/>
  <rect x="110" y="110" width="60" height="46" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="110" y1="130" x2="170" y2="130" stroke="currentColor" stroke-width="2"/>
  <line x1="140" y1="110" x2="140" y2="78" stroke="currentColor" stroke-width="1.5"/>
  <line x1="125" y1="78" x2="155" y2="78" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="132" cy="30" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <g font-size="11" fill="currentColor">
    <circle cx="118" cy="145" r="2" opacity="0.6"/>
    <circle cx="162" cy="118" r="2" opacity="0.6"/>
    <circle cx="150" cy="165" r="2" opacity="0.6"/>
    <circle cx="128" cy="100" r="2" opacity="0.6"/>
    <text x="180" y="34" text-anchor="start">maximum, but beyond the</text>
    <text x="180" y="47" text-anchor="start">whisker — plotted as a point,</text>
    <text x="180" y="60" text-anchor="start">not merged into the whisker</text>
    <text x="180" y="82" text-anchor="start">upper whisker</text>
    <text x="180" y="114" text-anchor="start">75% (Q3)</text>
    <text x="180" y="134" text-anchor="start">median</text>
    <text x="180" y="154" text-anchor="start">25% (Q1)</text>
    <text x="180" y="192" text-anchor="start">lower whisker = minimum</text>
    <text x="10" y="205" text-anchor="start" font-size="10" opacity="0.6">low</text>
    <text x="10" y="30" text-anchor="start" font-size="10" opacity="0.6">high</text>
  </g>
</svg>
<figcaption>The box spans the interquartile range with the median marked inside; whiskers extend
to the most extreme non-outlying values on either side. A point beyond the whisker — here the true
maximum of the sample — is drawn individually as an outlier rather than stretching the whisker out
to reach it.</figcaption>
</figure>

The boxplot is arguably the most informative default: it shows the same distributional shape as
the histogram, it displays several summary statistics explicitly (median, interquartile range,
whiskers, outliers), and adding `geom_jitter()` overlays every individual data point on top of it.
Its one disadvantage relative to the dotplot or histogram is that you cannot read off, from the
figure alone, how many subjects fall within a given interval — usually not the thing you need most.

## Visualizing two variables

For two variables, the scatterplot is the baseline choice.

```r
NHANES %>%
  ggplot(aes(x = Height, y = Weight)) +
  geom_point() +
  xlab("Height (cm)") +
  ylab("Weight (kg)")
```

`geom_point()` silently drops rows with a missing `Height` or `Weight`. Mapping a third variable
onto an aesthetic such as colour is a simple way to add a dimension to the same plot:

```r
NHANES %>%
  ggplot(aes(x = Height, y = Weight, color = Gender)) +
  geom_point() +
  xlab("Height (cm)") +
  ylab("Weight (kg)")
```

## Combining dplyr and ggplot2

Because both use the pipe, a `dplyr` chain can filter the data immediately before it is drawn.
Restricting the same scatterplot to white, married adults, and adding some further `ggplot2`
customization — manual colours, a white background, a title, a different point shape, and fixed
axis limits — gives:

```r
NHANES %>%
  filter(Age >= 18, Race1 == "White", MaritalStatus == "Married") %>%
  ggplot(aes(x = Height, y = Weight, color = Gender)) +
  geom_point(shape = 17, size = 1) +
  ggtitle("Height versus Weight") +
  xlab("Height (cm)") +
  ylab("Weight (kg)") +
  xlim(0, 220) +
  ylim(0, 220) +
  scale_color_manual(values = c("red", "blue")) +
  theme_bw()
```

This is only a small slice of what `ggplot2` can do. Which plot type is most informative depends
on the question being asked of the data, not on habit — a point returned to later in the course
with a more elaborate example.

## Worked example: a reference interval for systolic blood pressure

**Goal.** Use NHANES to set up a reference interval for systolic blood pressure (`BPSysAve`).

**Why.** A later dataset in the course concerns captopril, a drug tested on 15 patients who have
*elevated* blood pressure. Before a value can be called elevated, there has to be an interval of
values considered normal to compare it against — and NHANES, a large survey rather than a trial, is
the right dataset to build that interval from.

**Step 1 — restrict to complete, comparable data.** First keep only subjects with no missing value
across a battery of relevant variables (race, smoking, BMI category, age, hard-drug use, general
health, gender, alcohol use, the three individual systolic readings, sleep trouble) — this retains
4,660 subjects. Restrict further to ages 40–65 (2,522 subjects), and drop duplicated subject IDs, since
some subjects appear more than once in this wave of the survey (1,467 subjects). A histogram of
`BPSysAve` on this group has a long right tail — not normal. That is common for biological
variables: it is easier to be extreme on the high side than on the low side, especially when the
variable is bounded below by zero.

A methodological aside sits behind `BPSysAve` itself: it is the average of up to three repeated
systolic readings per subject. Averaging repeated measurements on the same person is only valid
when everyone being compared has the same number of repeats. If the counts differ — some subjects
have all three readings, others fewer — the resulting averages are heteroscedastic: an average of
fewer readings is noisier than an average of more, so treating them as directly comparable data
points is no longer correct. That is the reason the earlier filtering step requires all three
individual `BPSys` readings to be present before averaging.

**Step 2 — restrict to a healthy subgroup.** Requiring normality on the *whole* population is the
wrong ambition, since it mixes healthy and unhealthy blood pressures together. Restricting to a
"healthy" subgroup — defined here as a non-smoker, with no diabetes, no hard-drug use, no sleep
trouble, general health not rated "poor", and BMI in the WHO normal-to-overweight band ($18.5$ to
$29.9$ kg/m²) — leaves 275 subjects.

**Step 3 — check normality with a QQ-plot, not just a histogram.** A QQ-plot ("quantile–quantile
plot") compares the quantiles of the observed data against the quantiles a normal distribution
would produce. If the data are normal, the points fall approximately on a straight line; curvature
away from the line is a deviation from normality.

```r
NHANES %>%
  filter( /* the same completeness and age filters as above */ ) %>%
  distinct(ID, .keep_all = TRUE) %>%
  filter(Smoke100n == "Non-Smoker", Diabetes == "No", HardDrugs == "No",
         HealthGen != "Poor", SleepTrouble == "No",
         BMI_WHO %in% c("18.5_to_24.9", "25.0_to_29.9")) %>%
  ggplot(aes(sample = BPSysAve)) +
  geom_qq() +
  geom_qq_line()
```

Even on the healthy subgroup, the QQ-plot shows a slight right skew.

**Step 4 — transform, then re-check.** Log-transforming often symmetrizes a right-skewed
biological variable. The base-2 log is a convenient choice here because a difference of exactly 1
on the log2 scale corresponds to exactly doubling on the original scale:

$$\log_2 B - \log_2 A = \log_2(B/A) \implies \text{a gap of } 1 \text{ means } 2^1 = 2,$$

i.e. $B$ is twice $A$. Repeating the QQ-plot on $\log_2(\text{BPSysAve})$ shows the points falling
close to the line: on the log2 scale, blood pressure in the healthy subgroup is approximately
normal.

**Step 5 — build the interval on the transformed scale, then transform back.** With approximate
normality established on the log2 scale, the usual normal-theory 95% interval — sample mean plus
or minus two sample standard deviations — is computed there, and only then exponentiated
($2^{(\cdot)}$) back to the original mmHg scale:

```r
summary_NHANES <- NHANES %>%
  filter( /* same filters as above */ ) %>%
  distinct(ID, .keep_all = TRUE) %>%
  filter(Smoke100n == "Non-Smoker", Diabetes == "No", HardDrugs == "No",
         HealthGen != "Poor", SleepTrouble == "No",
         BMI_WHO %in% c("18.5_to_24.9", "25.0_to_29.9")) %>%
  mutate(BPSysAveLog = BPSysAve %>% log2) %>%
  summarize_at("BPSysAveLog",
               list(mean = ~mean(., na.rm = TRUE),
                    sd   = ~sd(., na.rm = TRUE),
                    n    = function(x) x %>% is.na %>% `!` %>% sum)) %>%
  mutate(se = sd / sqrt(n))
```

giving a reference interval $[\bar{x} - 2s,\ \bar{x} + 2s]$ on the log2 scale, and
$[2^{\bar{x} - 2s},\ 2^{\bar{x} + 2s}]$ mmHg after back-transforming — the interval of systolic
blood pressure considered "normal" for this population, against which the captopril patients'
values will later be judged. (The source material leaves the numeric endpoints as an unevaluated
inline computation rather than a fixed number, so they are not reproduced here; running the code
above on the full dataset produces them.) For context, the tutorial notes that the clinical
literature typically treats 140 mmHg as the upper limit of a normal systolic reading — a number to
compare the computed interval against, not to substitute for it.

## Sources

- The NHANES dataset, data import and the tidy-data check:
  [`01-the-nhanes-dataset.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd)
  (GTPB PSLS20, `Data_exploration_NHANES.Rmd`, CC BY 4.0).
- `dplyr` verbs, the pipe operator, and the partners/mean-vs-median example:
  [`02-data-wrangling-with-dplyr.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd)
  (same source Rmd).
- `ggplot2` single- and two-variable visualization and the systolic blood pressure reference
  interval: [`03-data-visualization.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd)
  (same source Rmd).
- The lecture material refers to, but does not itself contain, two further pieces the course
  uses elsewhere: a `preliminary_tidyverse.Rmd` on the concepts of tidy data, and
  `Data_exploration_captopril.Rmd`, the non-tidy blood-pressure drug dataset used both as the
  tidying exercise and as a more elaborate visualization example. A figure referenced in the
  "choosing a summary statistic" section (`Figure_partners.png`, illustrating the partners-desired
  outliers) is described in the source text but the image file itself was not supplied with these
  materials.

---

[← 25. Exploring the FEV Dataset](25-exploring-the-fev-dataset.md) · [Contents](index.md) · [27. Exploring the Captopril Dataset →](27-exploring-the-captopril-dataset.md)
