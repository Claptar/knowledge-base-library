---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit6-parallel.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

[PDF](index.md){.btn .btn-primary}

References:

-   [Tutorial on parallel processing using Python's Dask and R's future packages](https://berkeley-scf.github.io/tutorial-dask-future)


This unit will be fairly Linux-focused as most serious parallel
computation is done on systems where some variant of Linux is running.
The single-machine parallelization discussed here should work on Macs
and Windows, but some of the details of what is happening under the hood
are different for Windows.

As context, let's consider some ways we might be able to achieve faster computation:

  - better algorithms: This has been quite important in many areas of science but is not the focus here.
  - more computationally-efficient implementations of an algorithm: This was a topic in Unit 5.
  - faster computers: When CPUs were getting faster at a rapid pace (Moore's Law) this was quite important, but that's no longer the case for CPUs. However, GPU technology is improving rapidly.
  - "more" computers: We can try to exploit more processors (more CPUs, more GPU threads, more compute nodes) for a given computation. That is the topic of this Unit.

---

[Up: contents](index.md) · [1. Some scenarios for parallelization →](02-1-some-scenarios-for-parallelization.md)
