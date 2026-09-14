---
title: Command(s) to run
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/06/scf.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Command(s) to run

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

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
squeue -u jpduncan # use your username, not mine
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

[← SBATCH OPTIONS](12-sbatch-options.md) · [Up: contents](index.md) · [ssh -Y @dorothy.berkeley.edu →](14-ssh--y-dorothy-berkeley-edu.md)
