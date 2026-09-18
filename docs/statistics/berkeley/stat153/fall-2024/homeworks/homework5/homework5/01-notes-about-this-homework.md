---
title: Notes about this homework
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework5/homework5.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`homeworks/homework5/homework5.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd) — berkeley-stat153 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Notes about this homework

```r
knitr::opts_chunk$set(cache = TRUE, autodep = TRUE, cache.comments = TRUE)
```

\raggedright

The total number of points possible for this homework is 48. The number of
points for each question is written below, and questions marked as "bonus" are
optional (points awarded for bonus problems can be used to earn back points that
you may have lost on other parts of this homework but will not put you above
full credit). Submit the **knitted pdf file** from this Rmd to Gradescope.

If you collaborated with anybody for this homework, put their names here:

This homework is an exercise in Covid-19 forecasting. You will build some basic
forecasters of Covid-19 deaths at the national (U.S.) level, based on frameworks
you've learned in the last few lectures: ARIMA and ETS. You should know that, in
true (prospective) Covid-19 forecasting, the situation is much harder than the
one you are facing in this homework. This is because of **data revisions**: the
forecasters in true (prospective) Covid-19 forecasting did not have access to
the same data in real-time that you have access to now, in retrospect. Instead,
they had access to preliminary data that was subject to revisions, sometimes
very large and irregular ones, making forecasting much harder. See, e.g.,
[McDonald et al. (2021)](https://www.pnas.org/doi/10.1073/pnas.2111453118),
for a discussion of the impact of revisions on forecasting.

Also, in most operational forecasting enterprises, epidemic/pandemic forecasting
included, we would typically be trying to leverage exogenous signals and sources
of information to guide to our forecasts (beyond statistical models like ARIMA
or ETS which only rely on historical information about the target of interest).
Here we will pursue this only in limited fashion, at the end of this homework.

---

[Up: contents](index.md) · [Covid-19 cases and deaths →](02-covid-19-cases-and-deaths.md)
