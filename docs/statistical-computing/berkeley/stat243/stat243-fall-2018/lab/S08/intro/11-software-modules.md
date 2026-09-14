---
title: Software modules
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Software modules

**Source:** [`lab/S08/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

A lot of software is available on Savio but needs to be loaded from the relevant software module before you can use it.

```
module list  # what's loaded?
module avail  # what's available
```

One thing that tricks people is that the modules are arranged in a hierarchical (nested) fashion, so you only see some of the modules as being available *after* you load the parent module. Here's how we see the Python packages that are available.

```
which R

module avail
module load r r-packages
which R
module avail
```

---

[← from Savio, while on your local machine](10-from-savio-while-on-your-local-machine.md) · [Up: contents](index.md) · [Submitting jobs: accounts and partitions →](12-submitting-jobs-accounts-and-partitions.md)
