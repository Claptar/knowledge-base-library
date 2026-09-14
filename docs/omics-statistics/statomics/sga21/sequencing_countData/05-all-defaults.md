---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/irlsScheme.png")
```
Figure: Finding the root of the score function using Newton-Raphson optimization. The Figure shows estimation of a single $\beta$ parameter. The black solid line is the Score function evaluated at $\beta$. An initial estimate of $\beta$ is 2.25, which is represented by the dotted line. The value of the score function of this initial value is $S(\beta^k)$. The first derivative of the score function at that point, evaluated at $\beta = 2.25$, is represented by the solid blue line and is given by $\frac{\partial S(\beta)}{\partial \beta}$. The value of $\beta$ where the solid blue line crosses zero is the new estimate for $\beta$, namely $\beta^{k+1}$ which has a value of 1.4. The difference between $\beta^{k+1}$ and $\beta^{k}$ is given by $\left \{ \frac{ \partial S(\beta)}{ \partial \beta}   \right \}^{-1} S(\beta^k)$. This procedure is iterated until a convergence in the $\beta$ estimate is met.

### Generalized linear models in `R`

 - In order to get familiar with GLMs, we will fit a Poisson GLM in `R`, using the `Bikeshare` dataset as part of the `ISLR2` package. This dataset records how many bikes were being used from a bike-sharing service, every hour of the day over a full year (365 days).
 - Full information of the dataset is provided [here](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset). Variables of interest for us are:

    - `bikers`: Discrete count variable; the number of bikes being used that hour.
    - `hum`: Continuous variable ranging between 0 and 1; normalized humidity.
    - `hr`: Categorical variable between 0 and 23; the hour of the day. One could also consider this variable to be numeric and model it as such, but the data exploration will show that's not appropriate.
    - `weathersit`: Categorical variable; the weather condition of that hour, with

      1. Clear, Few clouds, Partly cloudy.
      2. Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist.
      3. Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds.
      4. Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog.

 ---

```r

---

[← Modeling count data: Generalized linear models](04-modeling-count-data-generalized-linear-models.md) · [Up: contents](index.md) · [if ISLR2 isn't installed, install it →](06-if-islr2-isn-t-installed-install-it.md)
