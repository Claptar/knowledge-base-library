---
title: write to an RData object, better for large data
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/01/solutions/R-practice-solutions.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# write to an RData object, better for large data

**Source:** [`sections/01/solutions/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

data_list <- list(earnings, m1, x, my_lm)
save(data_list, file = "../data_list.RData")
```

To load the .RData file you can use the ```load()``` function.

---

[← writing to a text file](11-writing-to-a-text-file.md) · [Up: contents](index.md)
