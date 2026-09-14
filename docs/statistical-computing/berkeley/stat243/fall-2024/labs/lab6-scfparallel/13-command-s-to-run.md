---
title: Command(s) to run
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab6-scfparallel.qmd
source_file: sources/berkeley-stat243/fall-2024/labs/lab6-scfparallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Command(s) to run

**Source:** [`labs/lab6-scfparallel.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab6-scfparallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

###################

./example.sh
```

The `example.sh` script creates a file called `testFile.txt` and appends some
output to that file. Note that since `submit.sh` is itself a bash script, you
could have just put the contents of `example.sh` directly in `submit.sh`, but it
is good practice to keep your computational code separate from your Slurm
batch submission scripts.

Now we can submit the job using the Slurm command `sbatch`:

```bash
sbatch submit.sh
```

Once you run that, your job will be queued. To check it's status, you can use `squeue`:

```bash
squeue -u <scf-username> # use your username, not mine
```

And now you wait. Go get a cup of coffee or get some rest! Then check back
later.

### Interactive jobs

!!! tip "Tip"
Interactive jobs are the best option when you need to do many short but
computationally intensive tasks which require your hands at the keyboard.

:::

#### `srun`

!!! tip "Tip"
This is the best option when you want to work at the Linux command line and
don't need a GUI, e.g. when debugging components of larger non-interactive job.

:::

To run an interactive job via Slurm, you can use the `srun` command:

```bash

---

[← SBATCH OPTIONS](12-sbatch-options.md) · [Up: contents](index.md) · [ssh -Y @gandalf.berkeley.edu →](14-ssh--y-gandalf-berkeley-edu.md)
