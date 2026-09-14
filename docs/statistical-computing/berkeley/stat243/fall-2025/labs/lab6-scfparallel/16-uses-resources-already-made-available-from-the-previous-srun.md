---
title: uses resources already made available from the previous srun command
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab6-scfparallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# uses resources already made available from the previous srun command

**Source:** [`labs/lab6-scfparallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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
carefully specify the resources you need. The main key flag for use in your job
script is:

- `--ntasks-per-node`: indicates the number of tasks (i.e., processes) one wants to run on each node

The value passed to `--ntasks-per-node` becomes available through the
`SLURM_NTASKS` environment variable, which can be retrieved in python via:

```python
import os
ntasks = os.getenv("SLURM_NTASKS")
```

### Specifying resources: alternatives

The `--ntasks-per-node` flag is convenient as it does not require the user to
know the actual number of CPUs on each node. It is generally a good choice if
one is simply running parallel code via multiple processes on one node.
However, there are alternatives flags that can be used in conjunction for
finer-grained control:

- `--nodes` (or `-N`): indicates the number of nodes to use
- `--ntasks` (or `-n`): indicates the number of tasks to run, not necessarily on the same node
- `--cpus-per-task` (or `-c`): indicates the number of CPUs to be used for each task

Since specifying `--ntasks` does not guarantee that all the cores will be on a
single node, this can cause problems in the common case of code that works on
one node but not multiple nodes. If one wants to do parallelization at multiple
levels (e.g., multiple processes, each process using multiple threads, such as
for linear algebra), then one would use both `--ntasks-per-node` and
`--cpus-per-task`. In general `--cpus-per-task` will be 1 except when running
threaded code.

The `SLURM_NTASKS` environment variable is set by Slurm when the job starts
running, and therefore can be accessed within your jobs. In addition to
`SLURM_NTASKS` here are some other variables that may be useful:
`SLURM_CPUS_ON_NODE`, `SLURM_CPUS_PER_TASK`, `SLURM_NODELIST`, `SLURM_NNODES`.
An explanation of each one of those can be found on slurm's manual (`man sbatch`).

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
