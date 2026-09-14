---
title: the files you need are here
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/06/scf.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# the files you need are here

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

cd stat243-fall-2022/labs/06/
```

:::


As mentioned before, the SCF cluster uses Slurm to schedule jobs. We'll learn
some Slurm commands now.

### Non-interactive jobs: `sbatch`

!!! tip "Tip"
This is the best option when you have a long-running job where no

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

[← or git@github.com:berkeley-stat243/stat243-fall-2022.git if you use SSH with git](10-or-git-github-com-berkeley-stat243-stat243-fall-2022-git-if.md) · [Up: contents](index.md) · [SBATCH OPTIONS →](12-sbatch-options.md)
