---
title: Introduction
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```python
#| echo: false
import re, os, sys, time, math
## As of 2024-09-15, I need to use the python/3.11 module to render,
## because of possible bug with libjpeg when using reticulate
## with matplotlib via knitr engine. I want to use knitr
## so that code output is interspersed with code in a chunk.
## But test run in 3.12 first so that can catch any 3.11->3.12 changes.
## Also, I have R chunks and bash chunks (though the latter might be handled with `!`
## if using jupyter.
```

[PDF](index.md){.btn .btn-dark}

!!! note "Note"
2024-10-05: There will be miminal further edits on this unit.
:::

---

[Up: contents](index.md) · [Overview →](02-overview.md)
