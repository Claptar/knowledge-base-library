---
title: "34. Structuring a Simulation Study"
course: "Berkeley Stat 243 Fall 2024"
chapter: 34
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 34. Structuring a Simulation Study

## What this covers

This chapter works through what survives of Luke Miratrix's tutorial on structuring a Monte Carlo
simulation study in R. It answers a narrow, practical question: given an estimator or a hypothesis
test whose behavior you want to characterize, what is the general shape of the code that finds out —
write a function that produces one simulated result, run it many times, summarize across the runs,
and then vary the parameters and repeat. It assumes you can already write an R function and know the
mechanics of a one-sample $t$-test.

The source converted for this chapter is a single fragment: the tutorial's overview and the opening
lines of its first case study. The rest — the actual simulation loop, the power analysis, and the
estimator comparison the overview promises — was not recovered from the source PDF, so this chapter
records only what the fragment itself establishes and is explicit about where it stops.

## The shape of a simulation study

The tutorial frames a simulation study as a small pipeline rather than a one-off script. First you
write a function that, given a set of parameters, generates one fake dataset and returns whatever
result you care about (an estimate, a $p$-value, a confidence interval). Once that function exists
and is trusted, you call it many times to build up a distribution of that result under known,
controlled conditions — conditions you chose because you know the truth (the true mean, the true
effect, the true shape of the error distribution) and can therefore judge how well the method
recovered it. The final step generalizes this from a single fixed parameter setting to a grid of
settings, turning a single simulation into what the tutorial calls a **multi-factor simulation
experiment**: the same generate-and-summarize function run once for every combination of parameters
of interest, so that the effect of each factor on performance can be read off afterward.

The document previews three case studies built on this pattern:

- the performance of the one-sample $t$-test under violations of the normality assumption it relies on;
- a power analysis for a single estimator, examining how it behaves across a range of circumstances;
- a comparison of three estimators of central tendency — the mean, the trimmed mean, and the median —
  for estimating the center of a distribution.

Only the first of these is present in the material available here, and only its opening step.

The script depends on **tidyverse** for the data-handling and summarizing steps that follow (`library( tidyverse )`), which the source notes is used for "cleaner code and some nice shortcuts," pointing the
reader to *R for Data Science* for more on the package itself.

A technical aside in the source is worth flagging for anyone reading the original `.R` file directly
rather than the compiled tutorial: comments beginning `#+` are `knitr` chunk directives controlling
how a block of code is run and displayed, and comments beginning `#'` are treated as markdown prose
when the file is compiled with `knitr::spin()`. That is the mechanism by which a plain R script
becomes a readable PDF tutorial — the prose you are reading and the code that produces the results
live in the same file.

## Coverage, and a first look at the $t$-test

The first case study asks how well the one-sample $t$-test's confidence interval performs.
**Coverage** is defined as the chance that a confidence interval, constructed by the test's usual
procedure, actually contains the true parameter value. A nominal 95% confidence interval is supposed
to have coverage close to 95%; the point of simulating is to check whether it really does once the
data stop being exactly normal, which is the assumption the interval's derivation leans on.

Before building the repeated-sampling machinery that would estimate coverage, the tutorial starts
by running the test once, on a single simulated dataset, to see what a single call looks like:

```r
# make fake data
dat = rnorm( 10, mean=3, sd=1 )

# conduct the test
tt = t.test( dat )
tt
```

```
##
## 	One Sample t-test
##
## data:  dat
## t = 10.134, df = 9, p-value = 3.202e-06
## alternative hypothesis: true mean is not equal to 0
##
```

Here `dat` is ten draws from a normal distribution with a known true mean of 3 and standard deviation
1, and `t.test` runs the ordinary one-sample $t$-test against a null of mean zero — which is why the
$t$-statistic is large and the $p$-value tiny: the data were generated with a true mean far from the
null. This single call is the building block the overview describes generalizing: wrap it in a
function of the generating parameters (here, sample size, mean, and standard deviation), call that
function many times, and record — for each call — whether the resulting confidence interval covered
the true mean of 3. The fraction of calls where it did is the simulated coverage. The fragment of the
source available here stops at this single call, before that repeated-sampling step is written out.

## Sources

- Notes: `simulation_tutorial_miratrix.md` (Luke Miratrix, *A Quick Guide to Conducting a Simulation
  Study*, 2017-04-18), from `berkeley-stat243/stat243-fall-2021/units/simulation_tutorial_miratrix.pdf`,
  CC0-1.0. The converted file is explicitly marked as reconstructed from a PDF with no usable text
  layer, and covers only the Overview section and the opening lines of "Simulation 1: the performance
  of the $t$-test" — through the single-call example above. The document's own overview names two
  further case studies, a power analysis and a comparison of the mean, trimmed mean, and median as
  estimators of central tendency, and the tutorial's own account of how it computes and checks coverage
  by repeated simulation, none of which is present in the converted material and none of which is
  reconstructed here.

---

[← 33. A Pie Chart To Critique](33-a-pie-chart-to-critique.md) · [Contents](index.md) · [35. Course Structure and Policies →](35-course-structure-and-policies.md)
