---
title: 'Lecture 2: Measures of Dependence and Stationarity'
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/lectures/dependence/dependence.Rmd
source_file: sources/berkeley-stat153/fall-2024/lectures/dependence/dependence.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 2: Measures of Dependence and Stationarity

**Source:** [`lectures/dependence/dependence.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/lectures/dependence/dependence.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

# Random walk

```r
n = 500 # number of time points
r = 100 # number of repetitions
delta = 0.2 # drift

x0 = matrix(rnorm(n * r), nrow = n)
y0 = matrix(rnorm(n * r) + delta, nrow = n)

x = apply(x0, 2, cumsum)
y = apply(y0, 2, cumsum)

mu_x = apply(x, 1, mean)
mu_y = apply(y, 1, mean)

matplot(x, type = "l", lty = 1, col = rgb(0, 0, 0, 0.2),
        xlab = "t", ylab = "x_t", main = "delta = 0")
lines(mu_x, lty = 1, lwd = 3, col = 1)

matplot(y, type = "l", lty = 1, col = rgb(0.96, 0.28, 0.24, 0.2),
        xlab = "t", ylab = "x_t", main = paste("delta =", delta))
lines(mu_y, lty = 1, lwd = 3, col = 2)
```

# Auto-correlation heatmaps

```r
n = 500
m1 = m2 = matrix(0, n, n)

# Moving avg autocorrelation matrix
m1[row(m1) == col(m1)-2] = 1/3
m1[row(m1) == col(m1)-1] = 2/3
m1[row(m1) == col(m1)] = 1
m1[row(m1) == col(m1)+1] = 2/3
m1[row(m1) == col(m1)+2] = 1/3

# Random walk autocorrelation matrix
for (s in 1:n) {
  for (t in 1:n) {
    m2[s,t] = min(s,t) / sqrt(s*t)
  }
}

# Handy rotate function --- the orientation of R's image() function is to plot
# a heamtap under a ***90 degrees counterclockwise rotation*** of the standard
# way we think of matrices being laid out. So we can use this function below to
# pre-rotate the matrix clockwise by 90 degrees, to effectively undo this and
# have it print in a way that aligns with the standard matrix layout
clockwise90 = function(a) { t(a[nrow(a):1,]) }

# Now for the heatmaps
par(mar = c(2,2,2,2), mfrow = c(1,2))
image(clockwise90(m1), main = "Moving average", xaxt = "n", yaxt = "n")
image(clockwise90(m2), main = "Random walk", xaxt = "n", yaxt = "n")
```

# Covid-19 cross-correlation

```r
# Covid-19 cases and deaths in California, pivot longer
df = cases_deaths_subset |>
  filter(geo_value == "ca") |>
  select(time_value, case_rate_7d_av, death_rate_7d_av) |>
  pivot_longer(cols = c(case_rate_7d_av, death_rate_7d_av)) |>
  mutate(name = recode(name,
                       case_rate_7d_av = "Cases",
                       death_rate_7d_av = "Deaths"))

# Handy function to produce a transformation from one range to another
trans = function(x, from_range, to_range) {
  (x - from_range[1]) / (from_range[2] - from_range[1]) *
    (to_range[2] - to_range[1]) + to_range[1]
}

# Compute ranges of the two signals, and transformations in b/w them
range1 = df |> filter(name == "Cases") |> select("value") |> range()
range2 = df |> filter(name == "Deaths") |> select("value") |> range()
trans12 = function(x) trans(x, range1, range2)
trans21 = function(x) trans(x, range2, range1)

ggplot(bind_rows(
  df |> filter(name == "Cases"),
  df |> filter(name == "Deaths") |> mutate_at("value", trans21)),
  aes(x = time_value, y = value)) +
  geom_line(aes(color = name)) +
  scale_color_manual(values = palette()[c(2,4)]) +
  scale_y_continuous(
    name = "Reported Covid-19 cases per 100k people",
    limits = range1,
    sec.axis = sec_axis(
      trans = trans12,
      name = "Reported Covid-19 deaths per 100k people")) +
  labs(title = "Covid-19 cases and deaths in California", x = "Date") +
  theme_bw() +
  theme(legend.position = "bottom", legend.title = element_blank())

ccf(df |> filter(name == "Cases") |> select(value),
    df |> filter(name == "Deaths") |> select(value),
    lag.max = 40, ylab = "Cross-correlation", main = "")
```

# Speech auto-correlation

```r
plot(speech, type = "l", ylab = "Vocal response")
acf(speech, lag.max = 250, ylab = "Auto-correlation", main = "")
```

---

[Up: contents](../../index.md)
