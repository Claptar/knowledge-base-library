---
title: Parallel job submission
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Parallel job submission

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

If you are submitting a job that uses multiple cores or nodes, you may need to
carefully specify the resources you need. The key flags for use in your job script are:

 - `--nodes` (or `-N`): indicates the number of nodes to use
 - `--ntasks-per-node`: indicates the number of tasks (i.e., processes) one wants to run on each node
 - `--cpus-per-task` (or `-c`): indicates the number of cpus to be used for each task

In addition, in some cases it can make sense to use the `--ntasks` (or `-n`) option
to indicate the total number of tasks and let the scheduler determine how many
nodes and tasks per node are needed. In general `--cpus-per-task` will be 1 except
when running threaded code.

When setting up parallel R code, you can find out how many cores there are on the
node assigned to you with:
```
ncores <- Sys.getenv("SLURM_CPUS_ON_NODE")
```
In addition to SLURM_CPUS_ON_NODE here are some of the variables that may be useful:
SLURM_NTASKS, SLURM_CPUS_PER_TASK, SLURM_NODELIST, SLURM_NNODES.

---

[← Submitting a batch job](13-submitting-a-batch-job.md) · [Up: contents](index.md) · [Monitoring jobs and the job queue →](15-monitoring-jobs-and-the-job-queue.md)
