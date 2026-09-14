---
title: Monitoring jobs and the job queue
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Monitoring jobs and the job queue

**Source:** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The basic command for seeing what is running on the system is `squeue` :

```
squeue
```

```
squeue-uSCF_USERNAME
```

To see what nodes are available in a given partition:

```
sinfo-plow
sinfo-phigh
sinfo-pgpu
```

You can cancel a job with `scancel` .

```
scancelYOUR_JOB_ID
```

The SCF has some tips about monitoring your job.

---

[← Parallel job submission](11-parallel-job-submission.md) · [Up: contents](index.md) · [Exercise →](13-exercise.md)
