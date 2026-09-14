---
title: uses resources already made available from the previous srun command
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/06/scf.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# uses resources already made available from the previous srun command

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

srun --pty --x11=first matlab # interactive matlab job
```

Here we used the -Y flag to `ssh` to run software with a GUI, such as MATLAB,
which allows the GUI to open in our local machine while still running
computations on the SCF cluster. For this to work, you’ll need X server software
on your own machine to manage the graphical windows. For Windows, your options
include eXceed or Xming and for Mac, there is XQuartz.

#### JupyterHub for RStudio or Jupyter Notebooks

!!! tip "Tip"
This is the best option when you want to interact with the RStudio or Jupyter
GUI while doing your computations or debugging.

:::

The SCF's [JupyterHub](https://jupyter.stat.berkeley.edu/) is another resource
for interactive computing on the SCF, allowing you to use RStudio or Jupyter on
one of the cluster's computing nodes.

### Specifying resources

If you are submitting a job that uses multiple cores or nodes, you may need to
carefully specify the resources you need. The key flags for use in your job
script are:

- `--nodes` (or `-N`): indicates the number of nodes to use
- `--ntasks-per-node`: indicates the number of tasks (i.e., processes) one wants to run on each node
- `--cpus-per-task` (or `-c`): indicates the number of CPUs to be used for each task

In addition, in some cases it can make sense to use the `--ntasks` (or `-n`)
option to indicate the total number of tasks and let the scheduler determine how
many nodes and tasks per node are needed. In general `--cpus-per-task` will be 1
except when running threaded code. When setting up parallel R code, you can find
out how many cores there are on the node assigned to you with:

```r
ncores <- Sys.getenv("SLURM_CPUS_ON_NODE")
```

The `SLURM_CPUS_ON_NODE` environment variable is set by Slurm when the job
starts running, and therefore can be accessed within your jobs. In addition to
`SLURM_CPUS_ON_NODE` here are some other variables that may be useful:
`SLURM_NTASKS`, `SLURM_CPUS_PER_TASK`, `SLURM_NODELIST`, `SLURM_NNODES`.

### Monitoring your jobs

As we saw, the basic command for seeing what is running on the system is `squeue`:

```bash
squeue # this shows all the queued jobs!
squeue -u SCF_USERNAME # this shows your jobs
```

To see what nodes are available in a given partition, you can use `sinfo`:

```bash
sinfo -p low
```

Finally, you can cancel a job with `scancel`.

```bash

---

[← 10 minute time limit](15-10-minute-time-limit.md) · [Up: contents](index.md) · [you can find your job ID using squeue →](17-you-can-find-your-job-id-using-squeue.md)
