---
title: 'Lecture 7: Exponential Smoothing With Trend and Seasonality'
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/lectures/ets/ets.Rmd
source_file: sources/berkeley-stat153/fall-2024/lectures/ets/ets.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 7: Exponential Smoothing With Trend and Seasonality

**Source:** [`lectures/ets/ets.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/lectures/ets/ets.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(dev = c("png", "pdf"), fig.path = "fig/",
                     cache = TRUE, autodep = TRUE, cache.comments = TRUE)
```

# Load packages

```r
library(tidyverse)
library(astsa)
library(fpp3)
library(epidatasets)
```

# Internet useage

```r
www = as_tsibble(WWWusage)

# Fit models
www_fit = www |>
  model(SES = ETS(value ~ error("A") + trend("N") + season("N")),
        Holt = ETS(value ~ error("A") + trend("A") + season("N")),
        Damped = ETS(value ~ error("A") + trend("Ad") + season("N")))

# Make forecasts
www_fit |>
  forecast(h = 10) |>
  mutate(.model = factor(.model, levels = c("SES", "Holt", "Damped"))) |>
  autoplot(www) +
  labs(x = "Minute", y = "Number of users",
       title = "Internet usage per minute") +
  facet_grid(vars(.model)) + theme_bw() +
  theme(legend.position = "bottom", legend.title = element_blank())

# Inspect fitted coefficients
www_fit |> select(SES) |> coef()
www_fit |> select(Holt) |> coef()
www_fit |> select(Damped) |> coef()
```

# Australian holiday travel

```r
holiday = tourism |>
  filter(Purpose == "Holiday") |>
  summarize(Trips = sum(Trips)/1e3)

# Fit Holt-Winters model
holiday_fit = holiday |>
  model(HoltWinters = ETS(Trips ~ error("A") + trend("A") +
                            season("A", period = 4)))

# Make forecasts
holiday_fit |> forecast(h = "3 years") |>
  autoplot(holiday) +
  labs(y = "Overnight trips (millions)",
       title =" Australian holiday travel") + theme_bw()
```

# ETS decomposition

```r
# Fit additive and multiplicative Holt-Winters
holiday_fit = holiday |>
    model(
      HWAdd = ETS(Trips ~ error("A") + trend("A") +
                    season("A", period = 4)),
      HWMult = ETS(Trips ~ error("A") + trend("A") +
                     season("M", period = 4)))

# Inspect fitted coefficients---note that gamma is really tiny in both models,
# which means that the seasonal pattern doesn't change much over time
holiday_fit |> select(HWAdd) |> coef()
holiday_fit |> select(HWMult) |> coef()

# An example of how we would pull out the components
holiday_fit |> select(HWAdd) |> components() |> head(10)

# Plot the decomposition according to the components
library(gridExtra)
g1 = holiday_fit |> select(HWAdd) |> components() |> autoplot() +
  labs(title = "Holt-Winters: additive seasonality", subtitle = NULL) +
  theme_bw()
g2 = holiday_fit |> select(HWMult) |> components() |> autoplot() +
  labs(title = "Holt-Winters: multiplicative seasonality", subtitle = NULL) +
  theme_bw()
grid.arrange(g1, g2, ncol = 2)
```

---

[Up: contents](../../index.md)
