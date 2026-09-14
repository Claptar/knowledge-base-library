---
title: Data tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data tidying

**Source:** [`tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
head(poison)
```

We can see a couple of things in the data that can
be improved upon:

1. Capitalize the fist column name
2. Set the Species column as a factor
3. Change the speciec factor levels from 0, 1 and 2 to
Dojofish, Goldfish and Zebrafish. Hint: use the fct_recode
function.
4. Add the variable log.Surv_time: we already saw in previous
tutorials that this transfromation is required to obtain
normally distributed data.

```r
poison <- poison %>%
  rename("Species" = "species") %>%
  mutate(Species = as.factor(Species)) %>%
  mutate(Species = fct_recode(Species, Dojofish = "0", Goldfish = "1", Zebrafish = "2")) %>%
  mutate(log.Surv_time = log(Surv_time))

poison
```

---

[← Import the data](03-import-the-data.md) · [Up: contents](index.md) · [Data exploration →](05-data-exploration.md)
