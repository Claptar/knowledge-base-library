---
title: Lab Part 05 —
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/03-power-and-extrapolation/lab.md
source_file: sources/berkeley-stat158/spring-2026/labs/03-power-and-extrapolation/lab.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lab Part 05 —

**Source:** [`labs/03-power-and-extrapolation/lab.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/03-power-and-extrapolation/lab.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

subgroup_data <- subset(data_randomized, age_group == "50-59")

# sub_diff <- with(subgroup_data,
#                  mean(response[treatment==?]) -
#                    mean(response[treatment==?]))

sub_sd <- sd(subgroup_data$response)

power.t.test(
  delta = sub_diff,
  sd = sub_sd,
  sig.level = 0.05,
  power = 0.8,
  type = "two.sample",
  alternative = "two.sided"
)

---

[← Data Analysis](04-data-analysis.md) · [Up: contents](index.md) · [Repeat for other two subgroups →](06-repeat-for-other-two-subgroups.md)
