---
title: 'Data transfer: SCP/SFTP'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Data transfer: SCP/SFTP

We can use the *scp* and *sftp* protocols to transfer files from any login node on the SCF cluster.

For example, we show how to transfer the file `data.csv`.

To transfer that to your directoy on the SCF cluster, the syntax for `scp` is `scp <from-place> <to-place>`

Below are some examples of transferring this file to various locations on the remote machine (your home directory, a folder called data in your home directory, and the tmp folder)

```bash
# to SCF, while on your local machine
scp data.csv andrew_vaughn@arwen.berkeley.edu:~/
scp data.csv andrew_vaughn@arwen.berkeley.edu:~/data/newName.csv
scp data.csv andrew_vaughn@arwen.berkeley.edu:/tmp/
```

Here is how to transfer data from the SCF to your local machine, while on your local machine. This will transfer the `new_name.csv` file to your Desktop with the name `data_scf.csv`

```bash
# from SCF, while on your local machine
scp andrew_vaughn@arwen.berkeley.edu:~/data/new_name.csv ~/Desktop/data_scf.csv
```

One program you can use with Windows is *WinSCP*, and a multi-platform program for doing transfers via SFTP is *FileZilla*. After logging in, you'll see windows for the SCF filesystem and your local filesystem on your machine. You can drag files back and forth.

## Submitting jobs: accounts and partitions

All computations are done by submitting jobs to the scheduling software that manages jobs on the cluster, called SLURM (Simple Linux Utility for Resource Management).

There is nothing you must specify to submit jobs to the SCF cluster, however, there are several options that are good form (more on this below).

## Interactive jobs

You can do work interactively.

For this, you may want to have used the `-Y` flag to ssh if you are running software with a GUI such as MATLAB.

```bash
# ssh -Y SCF_USERNAME@arwen.berkeley.edu
srun --pty /bin/bash          # interactive bash job
srun --pty --x11=first matlab # interactive matlab job
```

To display the graphical windows on your local machine, you'll need X server software on your own machine to manage the graphical windows. For Windows, your options include *eXceed* or *Xming* and for Mac, there is *XQuartz*.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Submitting a batch job →](03-submitting-a-batch-job.md)
