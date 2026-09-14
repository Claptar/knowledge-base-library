---
title: Exercise
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/06/scf.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exercise

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

You can either do 1. on your local machine and transfer the file to the SCF
cluster, or you can do it remotely. 2 - 4 should be done on the SCF.

1. Create a submission `submitBoot.sh` that will execute the code in `boot.R`.
  To do this I suggest copying the text from `submitR.sh` and updating a couple
  lines:
  - Change `job-name` to whatever you want to call this job.
  - Change `rEx.err` and `rEx.out` to `boot.err` and `boot.out`. Note these
  files can be useful for fixing bugs, particularly when executing shell scripts.
  These files show errors and output printed to the terminal.
  - Change time to `00:10:00` just in case your code runs longer than one minute.
  - Change the `--cpus-per-task` to 3. This is where you are telling Slurm to
  execute in parallel on 3 CPUs.
  - Change the last line `R CMD BATCH --no-save boot.R boot.Rout`. The
`boot.Rout` file will contain all of code, messages, errors, etc. from the R
session.

2. Call `sbatch submitBoot.sh` to execute the R script `boot.R`.

3. Check that the execution worked by examining the `.Rout` file.

4. Time allowing: Update the parallel code to use the `future` package
   and compare the results.

---

[← you can find your job ID using squeue](17-you-can-find-your-job-id-using-squeue.md) · [Up: contents](index.md)
