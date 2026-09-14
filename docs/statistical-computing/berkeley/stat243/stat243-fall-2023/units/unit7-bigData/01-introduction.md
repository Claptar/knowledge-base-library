---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit7-bigData.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

```python
import os, time
```

[PDF](index.md){.btn .btn-primary}

References:

-   [Tutorial on parallel processing using Python's Dask and R's future packages](https://berkeley-scf.github.io/tutorial-dask-future)
-   [Tutorial on working with large datasets in SQL, R, and
    Python](https://berkeley-scf.github.io/tutorial-databases)
-   Murrell: Introduction to Data Technologies
-   Adler: R in a Nutshell
-   [Spark Programming Guide](https://spark.apache.org/docs/latest/programming-guide.html)

I've also pulled material from a variety of other sources, some
mentioned in context below.

Note that for a lot of the demo code I ran the code separately from rendering this document because of the time involved in working
with large datasets.

We'll focus on Dask and databases/SQL in this Unit. The material on using Spark is provided for reference, but you're not responsible for that material.
If you're interested in working with big datasets in R or with tools other than Dask in Python, there is [some material in the tutorial on working with large datasets](https://berkeley-scf.github.io/tutorial-databases/R-and-Python).

---

[Up: contents](index.md) · [1. A few preparatory notes →](02-1-a-few-preparatory-notes.md)
