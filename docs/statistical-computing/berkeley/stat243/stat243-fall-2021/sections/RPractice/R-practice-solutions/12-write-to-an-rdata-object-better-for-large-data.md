---
title: write to an RData object, better for large data
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice-solutions.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# write to an RData object, better for large data

**Source:** [`sections/RPractice/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

data_list <- list(earnings, m1, x, my_lm)
save(data_list, file = "../data_list.RData")
```

To load the .RData file you can use the ```load()``` function.

---

[← writing to a text file](11-writing-to-a-text-file.md) · [Up: contents](index.md)
