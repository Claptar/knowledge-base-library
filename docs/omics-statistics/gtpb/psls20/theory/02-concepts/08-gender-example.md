---
title: Gender Example
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd
source_file: sources/gtpb-psls20/theory/02-concepts.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Gender Example

**Source:** [`theory/02-concepts.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(NHANES)
NHANES %>% ggplot(aes(x=Gender)) + geom_bar()
```

- Gender is a binary variable.
- It thus follows a Bernoulli distibution.
- The parameter of a Bernoulli distribution is the mean $\pi$.
- We can estimate $\pi$ based on the sample using the sample mean $\bar x = \sum\limits_{i=1}^n x_i$
- Note, that the sample mean is also a random variable! It also varies from sample to sample!

```r
NHANES$Gender %>% head
```

- Note, that Gender is a factor and that the females are the reference class (first class).
- R by default uses the level which comes first in the alfabet as the reference class.
- We can recode the Gender using a 0 and 1 coding.
- When we use the as.numeric() function the factor Gender is transformed in a numeric value. It has two values 1 or 2. 1 stands for the first level (females) and 2 for the second level males. If we subtract 1 from it we have a 0 and 1 encoding (0 for females and 1 for males).

```r
NHANES<-NHANES %>% mutate(gender=as.numeric(Gender)-1)
mean(NHANES$gender)
```

- Note, that due to the encoding the sample mean is an estimate for the fraction of males in the population.

- Always be careful with the encoding!

---

---

[← Sample](07-sample.md) · [Up: contents](index.md) · [Direct cholesterol example →](09-direct-cholesterol-example.md)
