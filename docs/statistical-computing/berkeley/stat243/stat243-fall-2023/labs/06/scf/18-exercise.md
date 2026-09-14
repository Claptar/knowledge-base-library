---
title: Exercise
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/06/scf.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exercise

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

You can either do 1. on your local machine and transfer the file to the SCF
cluster, or you can do it remotely. 2 - 4 should be done on the SCF.

1. Create a submission `submitBoot.sh` that will execute the code in `boot_proc.py`.
  To do this I suggest copying the text from `submit_py.sh` or `submitR.sh` and updating a couple
  lines:
  - Change `job-name` to whatever you want to call this job.
  - Change time to `00:10:00` just in case your code runs longer than one minute.
  - Change the `--cpus-per-task` to 3. This is where you are telling Slurm to
  execute in parallel on 3 CPUs.
  - Change the last line `python boot_serial.py`.

1. Call `sbatch submitBoot.sh` to execute the R script `boot_proc.py`.

2. Check that the execution worked by examining the `py.out` file.

---

[← you can find your job ID using squeue](17-you-can-find-your-job-id-using-squeue.md) · [Up: contents](index.md)
