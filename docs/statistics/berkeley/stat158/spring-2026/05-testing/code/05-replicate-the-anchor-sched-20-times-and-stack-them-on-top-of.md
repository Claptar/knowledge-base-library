---
title: replicate the anchor sched 20 times and stack them on top of one another
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html
source_file: sources/berkeley-stat158/spring-2026/05-testing/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# replicate the anchor sched 20 times and stack them on top of one another

**Source:** [`05-testing/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/05-testing/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

all_partitions_df <- map_dfr(1:nrow(permmat), ~ my_null_sched, .id = "partition") |>
  mutate(partition = factor(partition, levels = as.character(1:20), ordered = TRUE))

---

[← calculate ATE-hat for every partition](04-calculate-ate-hat-for-every-partition.md) · [Up: contents](index.md) · [add the unique permutations as a new column and find yi, the observed responses →](06-add-the-unique-permutations-as-a-new-column-and-find-yi-the.md)
