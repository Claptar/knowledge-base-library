---
title: Overview
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Overview

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

References:

-   [Tutorial on parallel processing using Python's Dask and R's future packages](https://computing.stat.berkeley.edu/tutorial-dask-future)
-   [Tutorial on parallelization in various languages, including use of PyTorch and JAX in Python](https://computing.stat.berkeley.edu/tutorial-parallelization)

!!! tip "Tip"
This unit will be fairly Linux-focused as most serious parallel
computation is done on systems where some variant of Linux is running.
The single-machine parallelization discussed here should work on Macs
and Windows, but some of the details of what is happening under the hood
are different for Windows.
:::

As context, let's consider some ways we might be able to achieve faster computation:

  - better algorithms: This has been quite important in many areas of science but is not the focus here.
  - more computationally-efficient implementations of an algorithm: This was a topic in Unit 5.
  - faster computers: When CPUs were getting faster at a rapid pace (Moore's Law) this was quite important, but that's no longer the case for CPUs. However, GPU technology is improving rapidly.
  - "more" computers: We can try to exploit more processors (more CPUs, more GPU threads, more compute nodes) for a given computation. That is the topic of this Unit.

---

[Up: contents](index.md) · [1. Some scenarios for parallelization →](02-1-some-scenarios-for-parallelization.md)
