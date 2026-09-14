---
title: ssh -Y SAVIOUSERNAME@hpc.brc.berkeley.edu
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s07/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ssh -Y SAVIOUSERNAME@hpc.brc.berkeley.edu

**Source:** [`section/s07/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

srun -A ic_stat243 -p savio2  --nodes=1 -t 10:00 --pty bash
env | grep SLURM  ## see what environment variables are set by SLURM

---

[← Interactive jobs](13-interactive-jobs.md) · [Up: contents](index.md) · [now execute on the compute node →](15-now-execute-on-the-compute-node.md)
