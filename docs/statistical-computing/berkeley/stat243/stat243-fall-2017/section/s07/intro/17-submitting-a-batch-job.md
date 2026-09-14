---
title: Submitting a batch job
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s07/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Submitting a batch job

**Source:** [`section/s07/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Or you can submit a job to run in the background.

Let's see how to submit a simple job. If your job will only use the resources on a single node, you can do the following.


Here's an example job script that you can run.


        #!/bin/bash
        # Job name:
        #SBATCH --job-name=test
        #
        # Account:
        #SBATCH --account=ic_stat243
        #
        # Partition:
        #SBATCH --partition=savio
        #
        # Wall clock limit (30 seconds here):
        #SBATCH --time=00:00:30
        #
        ## Command(s) to run:
        module load r/3.2.5 ggplot2
        R CMD BATCH --no-save file.R file.out


Now let's submit and monitor the job:

```
sbatch job.sh

squeue -j <JOB_ID>

wwall -j <JOB_ID>
```

When setting up parallel R code, you can find out how many cores there are on the node assigned to you with:

```
ncores <- Sys.getenv("SLURM_CPUS_ON_NODE")
```

Note that except for the *savio2_htc*  and *savio2_gpu* partitions, all jobs are given exclusive access to the entire node or nodes assigned to the job (and your account is charged for all of the cores on the node(s).

---

[← Time limits](16-time-limits.md) · [Up: contents](index.md) · [Parallel job submission →](18-parallel-job-submission.md)
