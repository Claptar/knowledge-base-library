---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Introduction

Andrew Vaughn

18 October, 2021

Much of this material comes from the SCF documentation at the SCF homepage.

## Outline

This training session will cover the following topics:

- System capabilities and hardware
  - SCF computing nodes
  - Disk space
- Logging in, data transfer, and software
  - Logging in
  - Data transfer: SCP/SFTP
  - Software modules
- Submitting and monitoring jobs
  - Accounts and partitions
  - Interactive jobs
  - Basic job submission
  - Parallel jobs
  - Monitoring jobs and cluster status
- Exercise

## System Capabilities and Hardware

- The SCF Linux cluster contains 352 cores, separated into 12 nodes and two partitions.
  - *Low partition*
    - 8 nodes
    - 256 total cores
    - each node contains 32 cores and 256 GB of RAM
  - *high partition*
    - 4 nodes
    - 96 total cores
    - each node contains 24 cores and 128 GB of RAM
  - *GPU partition*
    - Tesla K20Xm
    - one node in the high partition
    - 2 CPU cores and 128 GB of RAM (shared with CPU)

## SCF Computing Nodes

The SCF cluster is has several compute nodes, which you can list using `sitehosts compute`. They are also listed on this page.

The nodes are divided into 3 partitions, listed above, with restrictions associated with each. Any job you submit must be submitted to a partition to which you have access.

For the puposes of this class, we only have access to the *low partition*.

## Disk Space

Every account is given 5 GB of disk space. (This can be queried using `quota <account_name>`) This includes your home directory and a `/tmp` directory tied to your account. Space in the `/scratch` partition is available by request only.

## Logging in

You can use login nodes for non-intensive interactive work such as job submission and monitoring, basic compilation, managing your disk space, and transferring data to/from the server.

To login, you need to have software on your own machine that gives you access to a UNIX terminal (command-line) session. These come built-in with Mac (see Applications -> Utilities -> Terminal). For Windows, some options include PuTTY.

Here are instructions for doing this setup, and for logging in.

Login servers include: `arwen`, `beren`, `bilbo`, `gandalf`, `gimli`, `legolas`, `pooh`, `radagast`, `roo`, `shelob`, `springer`, `treebeard`

Then to login:

```
ssh SCF_USERNAME@LOGINSERVER.berkeley.edu
```

Then enter your password.

One can then navigate around and get information using standard UNIX commands such as `ls`, `cd`, `du`, `df`, etc.

---

[Up: contents](index.md) · [Data transfer: SCP/SFTP →](02-data-transfer-scp-sftp.md)
