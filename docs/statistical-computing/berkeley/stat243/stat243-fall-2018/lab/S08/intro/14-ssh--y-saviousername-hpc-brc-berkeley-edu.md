---
title: ssh -Y SAVIOUSERNAME@hpc.brc.berkeley.edu
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ssh -Y SAVIOUSERNAME@hpc.brc.berkeley.edu

**Source:** [`lab/S08/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

srun -A ic_stat243 -p savio2  --nodes=1 -t 10:00 --pty bash
env | grep SLURM  ## see what environment variables are set by SLURM

---

[← Interactive jobs](13-interactive-jobs.md) · [Up: contents](index.md) · [now execute on the compute node →](15-now-execute-on-the-compute-node.md)
