---
title: Unit 07 — bigData Part 17 —
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 07 — bigData Part 17 —

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

langSummary = sqlContext.sql("SELECT lang, count(*) as n FROM wikiHits GROUP BY lang ORDER BY n desc limit 20") # 38 minutes
results = langSummary.collect()

---

[← have one partition because one file per partition is written out](16-have-one-partition-because-one-file-per-partition-is-written.md) · [Up: contents](index.md) · [Unit 07 — bigData Part 18 — →](18-unit-07-bigdata-part-18.md)
