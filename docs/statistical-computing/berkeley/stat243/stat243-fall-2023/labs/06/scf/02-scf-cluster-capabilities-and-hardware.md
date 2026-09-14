---
title: SCF cluster capabilities and hardware
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/06/scf.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# SCF cluster capabilities and hardware

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

!!! tip "Tip"
## Clusters, partitions, and nodes! Oh my!

A **cluster** is a collection of computing **nodes**. A node is analogous to a
laptop or desktop computer, with an operating system, RAM, CPUs, and sometimes
GPUs.

![](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2023/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/images/cluster.png)
[Image source](https://hbctraining.github.io/Intro-to-shell-flipped/lessons/08_HPC_intro_and_terms.html)

 Nodes with similar capabilities or access policies are often grouped together
as a **partition**. This allows cluster users to request the resources they need
-- such as number of CPU **cores** -- from a pool of nodes, rather than specify
a specific one.

:::

The SCF cluster has 1064 cores, across 7 partitions with more than 26 nodes, but
for this class we'll use the `low` partition. It's the default, so you won't
need to do anything special to use it for your jobs (we'll explain how to submit
jobs later on).

The `low` partition has the following resources:

- 8 nodes
- 32 cores per node
- 256 GB RAM per node

The SCF Linux cluster uses a batch job scheduler called
[Slurm](https://en.wikipedia.org/wiki/Slurm_Workload_Manager), commonly used by
large computer centers in both academia and industry. Although the SCF cluster
has much greater computational capacity than our personal computers, it is a
shared resource with many users. With Slurm, the cluster is able to schedule
jobs asynchronously, balancing resource allocations so that everyone gets a
turn. This also means that when you submit a job, it may not run until many
minutes or hours later. Be sure to give yourself enough time!

<!--
## Compute servers

On the other hand, the SCF cluster also has a number of interactive computing
servers. If you've already used `ssh` to access the cluster, then you may
already be familiar with some of them as a subset are also used as login nodes.
After logging, you can run `sitehosts compute` to see which nodes are intended
as computing nodes. Currently:


Before using one of the compute servers, be sure to read through
[Compute Server Policies](https://statistics.berkeley.edu/computing/faqs/what-are-policies-using-compute-servers)
-->

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [Your ~/ on the SCF →](03-your-on-the-scf.md)
