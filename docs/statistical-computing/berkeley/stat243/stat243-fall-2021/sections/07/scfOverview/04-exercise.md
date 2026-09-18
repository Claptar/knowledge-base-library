---
title: Exercise
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Exercise

1) Create a submission `bootSub` that will execute the code in `boot.R`. To do this I suggest copying the text from `exSubR` and updating a couple lines:
   - Change job-name to whatever you want to call this job
   - Change `rEx.err` and `rEx.out` to `boot.err` and `boot.out`. Note these files can be useful for fixing bugs, particuarily when excecuting shell scripts. These files show errors and output printed to the terminal.
   - Change time to 00:10:00 just in case your code runs longer than one minute.
   - Change the cpus per task to 3. This is where you are telling SLURM to execute in parallel on 3 nodes.
   - Change the last line `R CMD BATCH --no-save boot.R boot.Rout`. The `boot.Rout` file will contain all of code, messages, errors, etc. from the R session.
2) Transfer the files `boot.R` and `bootSub` to your SCF account. This can be done using `scp` before logging onto the SCF cluster (see examples above)
   - Note, there are other ways to transfer files. For example, one other option would be to clone the repo for this class onto your SCF account after logging in.
3) Call `sbatch bootSub` to excecute the R script `boot.R`.
4) Check that the excecution worked by examining the `.Rout` file.
5) If you have time:
   - Update parallel code to be execute with the future package to compare the results.

---

[← Submitting a batch job](03-submitting-a-batch-job.md) · [Up: contents](index.md)
