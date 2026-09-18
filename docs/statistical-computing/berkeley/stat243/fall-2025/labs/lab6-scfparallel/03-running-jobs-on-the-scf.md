---
title: Running jobs on the SCF
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab6-scfparallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`labs/lab6-scfparallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Running jobs on the SCF

!!! tip "Tip"
For this section, you'll need to have some of [this week's
materials](https://github.com/berkeley-stat243/fall-2025/tree/main/labs/lab6-scfparallel)
in your home directory on the SCF cluster.

To get them, you can (and probably should) clone the course repo to your home directory
on the SCF cluster:

```bash
# first ssh to an SCF login node: ssh <scf-username>@<host-name>.berkeley.edu

cd ~/ # or a subdirectory if you prefer

git clone https://github.com/berkeley-stat243/fall-2025.git
# or git@github.com:berkeley-stat243/fall-2025.git if you use SSH with git

# the files you need are here
cd fall-2025/labs/lab6-scfparallel/
```

:::

As mentioned before, the SCF cluster uses Slurm to schedule jobs. We'll learn
some Slurm commands now.

## Non-interactive jobs: `sbatch`

!!! tip "Tip"
This is the best option when you have a long-running job that does not require any
interaction to complete.

:::

The first command is `sbatch`. To use `sbatch`, you will first create a bash
script (you can do this on the SCF cluster if you know how to use a shell text
editor like `nano`, or just do it locally and transfer the file to the SCF via
one of the methods discussed before).

In the course repo, you will find an example bash script called `submit.sh`.
Here's what it contains:

```bash
#!/bin/bash

################
# SBATCH OPTIONS
################

#SBATCH --job-name=example # job name for queue (optional)
#SBATCH --partition=low    # partition (optional, default=low)
#SBATCH --error=ex.err     # file for stderr (optional)
#SBATCH --output=ex.out    # file for stdout (optional)
#SBATCH --time=00:01:00    # max runtime of job hours:minutes:seconds
#SBATCH --nodes=1          # use 1 node
#SBATCH --ntasks=1         # use 1 task
#SBATCH --cpus-per-task=1  # use 1 CPU core

###################
# Command(s) to run
###################

./example.sh
```

The `example.sh` script creates a file called `testFile.txt` and appends some
output to that file. Note that since `submit.sh` is itself a bash script, you
could have just put the contents of `example.sh` directly in `submit.sh`, but it
is good practice to keep your computational code separate from your Slurm
batch submission scripts.

Now we can submit the job using the Slurm command `sbatch`:

```bash
sbatch submit.sh
```

Once you run that, your job will be queued. To check its status, you can use `squeue`:

```bash
squeue -u <scf-username> # use your username, not mine
```

And now you wait. Go get a cup of coffee or get some rest! Then check back
later.

## Interactive jobs

!!! tip "Tip"
Interactive jobs are the best option when you need to do many short but
computationally intensive tasks which require your hands at the keyboard.

:::

### `srun`

!!! tip "Tip"
This is the best option when you want to work at the Linux command line and
don't need a GUI, e.g. when debugging components of a larger non-interactive job.

:::

To run an interactive job via Slurm, you can use the `srun` command:

```bash
# ssh -Y <scf-username>@gandalf.berkeley.edu

# 10 minute time limit
srun  -t 00:10:00 -N 1 -n 1 -c 1 --pty /bin/bash

# uses resources already made available from the previous srun command
srun --pty --x11=first matlab # interactive matlab job
```

Here we used the -Y flag to `ssh` to run software with a GUI, such as MATLAB,
which allows the GUI to open in our local machine while still running
computations on the SCF cluster. For this to work, you’ll need X server software
on your own machine to manage the graphical windows. For Windows, your options
include eXceed or Xming and for Mac, there is XQuartz.

### JupyterHub for RStudio or Jupyter Notebooks

!!! tip "Tip"
This is the best option when you want to interact with the RStudio or Jupyter
GUI while doing your computations or debugging.

:::

The SCF's [JupyterHub](https://jupyter.stat.berkeley.edu/) is another resource
for interactive computing on the SCF, allowing you to use RStudio or Jupyter on
one of the cluster's computing nodes.

## Specifying resources

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

## Specifying resources: alternatives

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

## Monitoring your jobs

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
# you can find your job ID using `squeue`
scancel YOUR_JOB_ID
```

See the "How to Monitor Jobs" section of the SCF's documentation on [this page](https://statistics.berkeley.edu/computing/servers/cluster) for some more info.

---

[← Your ~/ on the SCF](02-your-on-the-scf.md) · [Up: contents](index.md) · [Exercise →](04-exercise.md)
