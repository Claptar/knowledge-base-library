---
title: Submitting a batch job
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Submitting a batch job

**Source:** [`lab/S08/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Or you can submit a job to run in the background.

Let's see how to submit a simple job. If your job will only use the resources on a single node, you can do the following.


Here's an example job script (see also *example_loo.sh*) that you can run. *example_loo.R* does leave-one-out cross-validation in parallel using R's foreach package, with the *registerDoParallel* function telling R how many CPUs to use. You can think of *foreach* simply as a for loop where the output of the loop is (usually) a list that contains the results of each iteration's calculation.

```
#!/bin/bash

---

[← Time limits](16-time-limits.md) · [Up: contents](index.md) · [Job name →](18-job-name.md)
