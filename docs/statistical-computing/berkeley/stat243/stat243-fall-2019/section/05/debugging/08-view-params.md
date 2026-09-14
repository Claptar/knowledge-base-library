---
title: view params
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/05/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# view params

**Source:** [`section/05/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

params

#pull out broken one
foo <- try(lm(y ~ x, data = data[data$cats == 15, ]))
foo

---

[← unless you're running Rscript, then idk](07-unless-you-re-running-rscript-then-idk.md) · [Up: contents](index.md) · [check what it is →](09-check-what-it-is.md)
