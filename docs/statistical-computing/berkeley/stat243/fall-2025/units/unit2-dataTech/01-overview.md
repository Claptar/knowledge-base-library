---
title: Overview
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Overview

```r
#| echo: false
reticulate::use_python('/usr/local/linux/miniforge-3.13/bin/python')
```

```python
#| echo: false
import os, io
import numpy as np
import pandas as pd
import subprocess

## So that all objects are printed without explicit `print`.
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

```

References (see [syllabus](../../syllabus/index.md) for links):

-   Adler
-   Nolan and Temple Lang, XML and Web Technologies for Data Sciences with R.
-   Murrell, Introduction to Data Technologies.
-   SCF tutorial: [Working with large datasets in SQL, R, and Python](https://computing.stat.berkeley.edu/tutorial-databases/)

(Optional) Videos:

There are four videos from 2020 in the bCourses Media Gallery that you
can use for reference if you want to:

1.  Text files and ASCII
2.  Encodings and UTF-8
3.  HTML
4.  XML and JSON

Note that the videos were prepared for a version of the course that used
R, so there are some differences from the content in the current version of
the unit that reflect translating between R and Python. I'm not sure how
helpful they'll be, but they are available.

!!! note "Note"
This document  uses the `knitr` engine and the Quarto configuration `ipynb-shell-interactivity: all`, so that output from all Python code in a chunk will print in the rendered document and the output will be interspersed with the code in the chunk rather than printed all at the end of the code chunk.
:::

---

[Up: contents](index.md) · [1. Data storage and file formats on a computer →](02-1-data-storage-and-file-formats-on-a-computer.md)
