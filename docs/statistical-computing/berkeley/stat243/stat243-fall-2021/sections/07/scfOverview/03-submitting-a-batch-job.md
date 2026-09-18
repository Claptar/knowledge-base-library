---
title: Submitting a batch job
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Submitting a batch job

Or you can submit a job to run in the background.

Let's see how to submit a simple job. If your job will only use the resources on a single node, here's an example job submission script, *exSub* in the section folder:

```bash
#!/bin/bash

####################
# SBATCH OPTIONS
####################
#SBATCH --job-name=example    # job name fore queue, default may be u$
#SBATCH --partition=low       # high/low/gpu, default if empty is low
#SBATCH --error=ex.err        # error file, default if empty is slurm$
#SBATCH --output=ex.out       # standard out file, no default
#SBATCH --time=00:01:00       # optional, max runtime of job hours:minutes:seconds
#SBATCH --nodes=1             # only use 1 node, MPI option
#SBATCH --ntasks=1            # how many tasks to start
#SBATCH --cpus-per-task=1     # number of cores to use, multi-core/mu$

####################
# What to run
####################

./example.sh
```

This script runs the following bash script, *example.sh* in the section folder:

```bash
#!/bin/bash

# set file name
fileName="testFile.txt"

# create file
touch $fileName

# intro message
echo "I'm your new test script!" >> $fileName
echo >> $fileName
echo >> $fileName

# fill it with some things
for i in {1..10}
do
echo $i >> $fileName
done

# finish it out
echo >> $fileName
echo >> $fileName
echo "All Finished!" >> $fileName
```

Now let's submit and monitor the job:

```bash
sbatch exSub

squeue -u <SCF_USERNAME>
```

## Parallel job submission

If you are submitting a job that uses multiple cores or nodes, you may need to carefully specify the resources you need. The key flags for use in your job script are:

- `--nodes` (or `-N`): indicates the number of nodes to use
- `--ntasks-per-node`: indicates the number of tasks (i.e., processes) one wants to run on each node
- `--cpus-per-task` (or `-c`): indicates the number of cpus to be used for each task

In addition, in some cases it can make sense to use the `--ntasks` (or `-n`) option to indicate the total number of tasks and let the scheduler determine how many nodes and tasks per node are needed. In general `--cpus-per-task` will be 1 except when running threaded code.

When setting up parallel R code, you can find out how many cores there are on the node assigned to you with:

```r
ncores <- Sys.getenv("SLURM_CPUS_ON_NODE")
```

In addition to `SLURM_CPUS_ON_NODE` here are some of the variables that may be useful: `SLURM_NTASKS`, `SLURM_CPUS_PER_TASK`, `SLURM_NODELIST`, `SLURM_NNODES`.

## Monitoring jobs and the job queue

The basic command for seeing what is running on the system is `squeue`:

```bash
squeue
squeue -u SCF_USERNAME
```

To see what nodes are available in a given partition:

```bash
sinfo -p low
sinfo -p high
sinfo -p gpu
```

You can cancel a job with `scancel`.

```bash
scancel YOUR_JOB_ID
```

The SCF has some tips about monitoring your job.

---

[← Data transfer: SCP/SFTP](02-data-transfer-scp-sftp.md) · [Up: contents](index.md) · [Exercise →](04-exercise.md)
