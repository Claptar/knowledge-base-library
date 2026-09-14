---
title: Parallel job submission
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Parallel job submission

**Source:** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If you are submitting a job that uses multiple cores or nodes, you may need to carefully specify the resources you need. The key flags for use in your job script are:

- `--nodes` (or `-N` ): indicates the number of nodes to use

- `--ntasks-per-node` : indicates the number of tasks (i.e., processes) one wants to run on each node

- `--cpus-per-task` (or `-c` ): indicates the number of cpus to be used for each task

In addition, in some cases it can make sense to use the `--ntasks` (or `-n` ) option to indicate the total number of tasks and let the scheduler determine how many nodes and tasks per node are needed. In general `--cpus-per-task` will be 1 except when running threaded code.

When setting up parallel R code, you can find out how many cores there are on the node assigned to you with:

```
ncores<-Sys.getenv("SLURM_CPUS_ON_NODE")
```

In addition to SLURM_CPUS_ON_NODE here are some of the variables that may be useful: SLURM_NTASKS, SLURM_CPUS_PER_TASK, SLURM_NODELIST, SLURM_NNODES.

---

[← Submitting a batch job](10-submitting-a-batch-job.md) · [Up: contents](index.md) · [Monitoring jobs and the job queue →](12-monitoring-jobs-and-the-job-queue.md)
