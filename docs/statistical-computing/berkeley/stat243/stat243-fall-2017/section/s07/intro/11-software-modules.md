---
title: Software modules
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s07/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Software modules

**Source:** [`section/s07/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

A lot of software is available on Savio but needs to be loaded from the relevant software module before you can use it.

```
module list  # what's loaded?
module avail  # what's available
```

One thing that tricks people is that the modules are arranged in a hierarchical (nested) fashion, so you only see some of the modules as being available *after* you load the parent module. Here's how we see the Python packages that are available.

```
which R

module avail
module load r/3.2.5
which R
module avail
module load ggplot2
R
library(ggplot2)
```

Note that once Savio switches to the SL7 operating system circa December, all Python and R packages will be directly available as soon as either the Python or R module is loaded.

---

[← from Savio, while on your local machine](10-from-savio-while-on-your-local-machine.md) · [Up: contents](index.md) · [Submitting jobs: accounts and partitions →](12-submitting-jobs-accounts-and-partitions.md)
