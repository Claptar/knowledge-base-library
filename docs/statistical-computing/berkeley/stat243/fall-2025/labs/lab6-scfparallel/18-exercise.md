---
title: Exercise
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab6-scfparallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exercise

**Source:** [`labs/lab6-scfparallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

You can either do 1. on your local machine and transfer the file to the SCF
cluster, or you can do it remotely. 2 - 4 should be done on the SCF.

1. Create a submission `submit_boot.sh` that will execute the code in `boot_proc.py`.
  To do this I suggest copying the text from `submit_py.sh` and updating a couple
  lines:
  - Change `job-name` to whatever you want to call this job.
  - Change time to `00:10:00` just in case your code runs longer than one minute.
  - Change the `--cpus-per-task` to 3. This is where you are telling Slurm to
  execute in parallel on 3 CPUs.
  - Change the last line from `python boot_serial.py` to `python boot_proc.py`.

2. Call `sbatch submit_boot.sh` to execute the python script `boot_proc.py`.

3. Use `squeue` to verify the job is complete and check that the execution worked by examining the `ex.out` file.

4. Note that the number of Dask workers in `boot_proc.py` and `boot_dist.py` is
  hard-coded. In many cases, it would be better for this value to be set
  dynamically based on an appropriate Slurm environment variable. Make this
  small adjustment to those files and verify it works as intended.

## Acknowledgements

This lab was developed by Andrew Vaughn and James Duncan for R, adapted to
python by Ahmed Eldeeb and slightly adjusted for the Fall 2025 semester.

---

[← you can find your job ID using squeue](17-you-can-find-your-job-id-using-squeue.md) · [Up: contents](index.md)
