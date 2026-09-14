---
title: Submitting a batch job
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Submitting a batch job

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Or you can submit a job to run in the background.

Let's see how to submit a simple job. If your job will only use the resources on
a single node, here's an example job submission script, *exSub* in the section folder:
```r
cat exSub
```

This script runs the following bash script, *example.sh* in the section folder:
```r
cat example.sh
```

Now let's submit and monitor the job:

```
sbatch exSub

squeue -j <JOB_ID>
```

---

[← ssh -Y SCFUSERNAME@arwen.berkeley.edu](12-ssh--y-scfusername-arwen-berkeley-edu.md) · [Up: contents](index.md) · [Parallel job submission →](14-parallel-job-submission.md)
