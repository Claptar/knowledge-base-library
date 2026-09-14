---
title: Monitoring jobs and the job queue
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Monitoring jobs and the job queue

**Source:** [`lab/S08/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

The basic command for seeing what is running on the system is `squeue`:
```
squeue
squeue -u SAVIO_USERNAME
squeue -A ic_stat243
```

To see what nodes are available in a given partition:
```
sinfo -p savio
sinfo -p savio2_gpu
```

You can cancel a job with `scancel`.
```
scancel YOUR_JOB_ID
```

For more information on cores, QoS, and additional (e.g., GPU) resources, here's some syntax:
```
squeue -o "%.7i %.12P %.20j %.8u %.2t %.9M %.5C %.8r %.3D %.20R %.8p %.20q %b"
```

We provide some [tips about monitoring your job](http://research-it.berkeley.edu/services/high-performance-computing/tips-using-brc-savio-cluster).

---

[← Command(s) to run](30-command-s-to-run.md) · [Up: contents](index.md) · [Exercise →](32-exercise.md)
