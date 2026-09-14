---
title: the files you need are here
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab6-scfparallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# the files you need are here

**Source:** [`labs/lab6-scfparallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

cd fall-2025/labs/lab6-scfparallel/
```

:::


As mentioned before, the SCF cluster uses Slurm to schedule jobs. We'll learn
some Slurm commands now.

### Non-interactive jobs: `sbatch`

!!! tip "Tip"
This is the best option when you have a long-running job that does not require any
interaction to complete.

:::

The first command is `sbatch`. To use `sbatch`, you will first create a bash
script (you can do this on the SCF cluster if you know how to use a shell text
editor like `nano`, or just do it locally and transfer the file to the SCF via
one of the methods discussed before).

In the course repo, you will find an example bash script called `submit.sh`.
Here's what it contains:

```bash
#!/bin/bash

################

---

[← or git@github.com:berkeley-stat243/fall-2025.git if you use SSH with git](10-or-git-github-com-berkeley-stat243-fall-2025-git-if-you-use.md) · [Up: contents](index.md) · [SBATCH OPTIONS →](12-sbatch-options.md)
