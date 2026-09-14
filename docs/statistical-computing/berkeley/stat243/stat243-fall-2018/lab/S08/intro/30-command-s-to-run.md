---
title: Command(s) to run
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Command(s) to run

**Source:** [`lab/S08/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

module load java spark/2.1.0 python/3.5
source /global/home/groups/allhands/bin/spark_helper.sh
spark-start
spark-submit --master $SPARK_URL $HOME/stat243-fall-2018/units/test_batch.py
spark-stop
```

When you write your code, you may need to specify information about the number of cores to use. (Though you shouldn't need to do this when using Spark on Savio. SLURM will provide a variety of variables that you can use in your code so that it adapts to the resources you have requested rather than being hard-coded.

In addition to SLURM_CPUS_ON_NODE here are some of the variables that may be useful: SLURM_NTASKS, SLURM_CPUS_PER_TASK, SLURM_NODELIST, SLURM_NNODES.

---

[← Wall clock limit](29-wall-clock-limit.md) · [Up: contents](index.md) · [Monitoring jobs and the job queue →](31-monitoring-jobs-and-the-job-queue.md)
