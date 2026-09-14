---
title: safer way
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# safer way

**Source:** [`section/08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

globals = "base"
future.apply::future_sapply(X = 2:4, FUN = function(exponent){base^exponent})

```


### Using `future_sapply`
(I DO NOT RECOMMEND SAPPLY STATEMENTS)
Sometimes, we only want a simple return value, such as a vector/matrix. Here are
a few examples using the `future_sapply` function.

```r

---

[← should fail, but doesn't](04-should-fail-but-doesn-t.md) · [Up: contents](index.md) · [setup plan →](06-setup-plan.md)
