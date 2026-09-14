---
title: SBATCH OPTIONS
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/06/scf.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# SBATCH OPTIONS

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

################

#SBATCH --job-name=example # job name for queue (optional)
#SBATCH --partition=low    # partition (optional, default=low)
#SBATCH --error=ex.err     # file for stderr (optional)
#SBATCH --output=ex.out    # file for stdout (optional)
#SBATCH --time=00:01:00    # max runtime of job hours:minutes:seconds
#SBATCH --nodes=1          # use 1 node
#SBATCH --ntasks=1         # use 1 task
#SBATCH --cpus-per-task=1  # use 1 CPU core

###################

---

[← the files you need are here](11-the-files-you-need-are-here.md) · [Up: contents](index.md) · [Command(s) to run →](13-command-s-to-run.md)
