---
title: "31. Working on the SCF Cluster"
course: "Berkeley Stat 243"
chapter: 31
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 31. Working on the SCF Cluster

## What this covers

This chapter answers a practical question: how do you actually get work done on a shared university
compute cluster rather than your own laptop? It walks through the Statistical Computing Facility
(SCF) Linux cluster used in this course — what hardware you get, how to log in and move files onto
it, and how to submit and monitor jobs through its scheduler, SLURM. It assumes only that you can
work at a command-line shell; nothing else from the course is required.

## The cluster: hardware and partitions

The SCF cluster is a Linux cluster of 352 cores spread across 12 nodes. The nodes are grouped into
two **partitions**, and every job you submit must be submitted to a partition you have access to:

- **Low partition** — 8 nodes, 256 cores total, each node with 32 cores and 256 GB of RAM.
- **High partition** — 4 nodes, 96 cores total, each node with 24 cores and 128 GB of RAM. One node
  in this partition also carries a Tesla K20Xm GPU, sharing its 2 CPU cores and 128 GB of RAM with
  ordinary CPU work.

For this course, you only have access to the **low partition**. You can list the cluster's compute
nodes at any time with `sitehosts compute`.

Every account gets 5 GB of disk space, covering both your home directory and a per-account `/tmp`
directory; you can check your usage with `quota <account_name>`. Extra space in `/scratch` is
available only by request.

## Logging in

The cluster is reached through **login nodes**, meant for light, non-intensive work: submitting and
watching jobs, basic compilation, managing your files, and moving data to and from the server. Heavy
computation belongs on a compute node via the scheduler, not on the login node itself.

To connect you need a terminal that can open a UNIX shell session — built into macOS
(Applications → Utilities → Terminal), or a client such as PuTTY on Windows. The login servers are:

```
arwen, beren, bilbo, gandalf, gimli, legolas, pooh, radagast, roo, shelob, springer, treebeard
```

Log in with:

```bash
ssh SCF_USERNAME@LOGINSERVER.berkeley.edu
```

and enter your password when prompted. Once connected, you navigate and inspect the filesystem with
the standard UNIX commands: `ls`, `cd`, `du`, `df`, and so on.

## Moving files: scp and sftp

Files travel to and from any SCF login node over the `scp` and `sftp` protocols. `scp` has the form

```bash
scp <from-place> <to-place>
```

so, run from your own machine, to push a local file `data.csv` up to the cluster:

```bash
# to SCF, while on your local machine
scp data.csv andrew_vaughn@arwen.berkeley.edu:~/
scp data.csv andrew_vaughn@arwen.berkeley.edu:~/data/newName.csv
scp data.csv andrew_vaughn@arwen.berkeley.edu:/tmp/
```

and, still from your own machine, to pull a remote file back down — this copies
`~/data/new_name.csv` on the cluster to your Desktop, renaming it `data_scf.csv`:

```bash
# from SCF, while on your local machine
scp andrew_vaughn@arwen.berkeley.edu:~/data/new_name.csv ~/Desktop/data_scf.csv
```

If you would rather not use the command line for transfers, *WinSCP* (Windows) and *FileZilla*
(cross-platform, over SFTP) give you a two-pane graphical view — one pane for the SCF filesystem,
one for your local machine — and you drag files between them.

## Submitting work: SLURM

All computation on the cluster runs through **SLURM** (Simple Linux Utility for Resource Management),
the scheduling software that decides which job runs on which node and when. Nothing is strictly
required to submit a job, but several options below are good practice to set explicitly rather than
rely on defaults.

### Interactive jobs

For interactive work, ask the scheduler for a shell on a compute node directly:

```bash
srun --pty /bin/bash          # interactive bash job
srun --pty --x11=first matlab # interactive matlab job
```

If the interactive program has a graphical interface — MATLAB in the second example — you need to
have logged in with X11 forwarding enabled (`ssh -Y SCF_USERNAME@arwen.berkeley.edu`), and you need
X server software running locally to display the windows: *eXceed* or *Xming* on Windows, *XQuartz*
on macOS.

### Batch jobs

More commonly you submit a job to run unattended in the background. A batch job is a shell script
whose header lines, each beginning `#SBATCH`, tell the scheduler what resources to reserve and how
to handle the job's output. Here is an example submission script, `exSub`:

```bash
#!/bin/bash

####################
# SBATCH OPTIONS
####################
#SBATCH --job-name=example    # job name fore queue, default may be u$
#SBATCH --partition=low       # high/low/gpu, default if empty is low
#SBATCH --error=ex.err        # error file, default if empty is slurm$
#SBATCH --output=ex.out       # standard out file, no default
#SBATCH --time=00:01:00       # optional, max runtime of job hours:minutes:seconds
#SBATCH --nodes=1             # only use 1 node, MPI option
#SBATCH --ntasks=1            # how many tasks to start
#SBATCH --cpus-per-task=1     # number of cores to use, multi-core/mu$

####################
# What to run
####################

./example.sh
```

(A couple of the inline comments above are cut off in the source material; the intent — a default
job name, a default error-file name, and a note about multi-core use — is clear from context even
though the exact wording is not fully recoverable.)

`exSub` runs the script `example.sh`, which does nothing more elaborate than writing a small text
file:

```bash
#!/bin/bash

# set file name
fileName="testFile.txt"

# create file
touch $fileName

# intro message
echo "I'm your new test script!" >> $fileName
echo >> $fileName
echo >> $fileName

# fill it with some things
for i in {1..10}
do
echo $i >> $fileName
done

# finish it out
echo >> $fileName
echo >> $fileName
echo "All Finished!" >> $fileName
```

You submit and then watch the job with:

```bash
sbatch exSub
squeue -u <SCF_USERNAME>
```

### Requesting resources for a parallel job

A job that needs more than one core or more than one node has to say so explicitly, using flags in
the `#SBATCH` header (or on the `srun`/`sbatch` command line):

- `--nodes` (or `-N`) — number of nodes to use.
- `--ntasks-per-node` — number of tasks (processes) to run on each node.
- `--cpus-per-task` (or `-c`) — number of CPUs given to each task.
- `--ntasks` (or `-n`) — total number of tasks, letting the scheduler work out how to spread them
  across nodes.

As a rule, leave `--cpus-per-task` at 1 unless the code you are running is itself multi-threaded —
that flag exists to give a single task more than one core, not to run more copies of the task.

Once a job is running, SLURM exposes what it was actually granted through environment variables you
can read from inside the job. In R, for instance, you find the number of cores available on your
assigned node with:

```r
ncores <- Sys.getenv("SLURM_CPUS_ON_NODE")
```

Other variables set the same way include `SLURM_NTASKS`, `SLURM_CPUS_PER_TASK`, `SLURM_NODELIST`,
and `SLURM_NNODES`.

### Monitoring and cancelling jobs

To see what is running or queued:

```bash
squeue            # everyone's jobs
squeue -u SCF_USERNAME   # just yours
```

To see which nodes are free in a given partition:

```bash
sinfo -p low
sinfo -p high
sinfo -p gpu
```

and to cancel a job you no longer want running:

```bash
scancel YOUR_JOB_ID
```

## Exercises

1. Create a submission script `bootSub` that runs the code in `boot.R`. Start from `exSubR` and
   change:
   - the job name to something of your choosing;
   - the error and output files (`rEx.err`, `rEx.out`) to `boot.err` and `boot.out` — useful for
     debugging, particularly for shell-script errors, since they capture everything printed to the
     terminal;
   - the time limit to `00:10:00`, in case the job runs longer than a minute;
   - `--cpus-per-task` to 3, so SLURM knows to give the job three cores to run in parallel on;
   - the final line, to `R CMD BATCH --no-save boot.R boot.Rout` — the resulting `boot.Rout` file
     will hold all of the code, messages, and errors from the R session.
2. Transfer `boot.R` and `bootSub` to your SCF account, either with `scp` before logging in, or by
   some other means (for example, cloning the class repository onto your SCF account after logging
   in).
3. Submit the job with `sbatch bootSub`.
4. Confirm it worked by examining the `.Rout` file.
5. If you have time: rewrite the parallel part of the code to use the `future` package instead, and
   compare the results.

## Sources

All of this chapter is drawn from a single lecture handout, *Introduction* (SCF training session),
Andrew Vaughn, stat243, Fall 2021, section 07, 18 October 2021 — supplied here as four converted
pages:

- `sections/07/scfOverview/01-introduction.md` — system capabilities, hardware, disk space, and
  logging in.
- `sections/07/scfOverview/02-data-transfer-scp-sftp.md` — `scp`/`sftp` transfer, and the start of
  the SLURM material (accounts, partitions, interactive jobs).
- `sections/07/scfOverview/03-submitting-a-batch-job.md` — batch job scripts, parallel resource
  requests, and monitoring commands.
- `sections/07/scfOverview/04-exercise.md` — the end-of-session exercise.

No slide deck or transcript was supplied separately; these pages are themselves a model's
reconstruction of a PDF handout (`sections/07/scfOverview.pdf`) that had no extractable text layer,
so the prose is a paraphrase in places and a couple of inline comments in the batch-script example
are visibly truncated in the source. The handout itself points to further material it does not
reproduce: the SCF's own documentation and homepage, a separate SCF page with setup and login
instructions, the SCF's tips on monitoring jobs, and the files referenced in the exercise
(`exSubR`, `boot.R`) which were not included among the supplied pages.

---

[← 30. Assignment: regex problems](30-assignment-regex-problems.md) · [Contents](index.md) · [32. Scheduling information →](32-scheduling-information.md)
