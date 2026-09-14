---
title: Monitoring jobs and the job queue
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Monitoring jobs and the job queue

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The basic command for seeing what is running on the system is `squeue`:
```
squeue
squeue -u SCF_USERNAME
squeue -A s243
```

To see what nodes are available in a given partition:
```
sinfo -p low
sinfo -p high
sinfo -p gpu
```

You can cancel a job with `scancel`.
```
scancel YOUR_JOB_ID
```

For more information on cores, QoS, and additional (e.g., GPU) resources, here's some syntax:
```
squeue -o "%.7i %.12P %.20j %.8u %.2t %.9M %.5C %.8r %.3D %.20R %.8p %.20q %b"
squeue -p low,high,gpu -o "%.14i %.6P %.20j %.12u %.2t %.11l %.11M %.11V %.5C \
%.8r %.6D %.20R %.13p %8q %b"
```

We provide some [tips about monitoring your job](http://research-it.berkeley.edu/services/high-performance-computing/tips-using-brc-savio-cluster).

---

[← Parallel job submission](14-parallel-job-submission.md) · [Up: contents](index.md) · [Exercise →](16-exercise.md)
