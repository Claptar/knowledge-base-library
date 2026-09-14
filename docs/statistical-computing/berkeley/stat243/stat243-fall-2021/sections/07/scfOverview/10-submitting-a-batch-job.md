---
title: Submitting a batch job
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Submitting a batch job

**Source:** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Or you can submit a job to run in the background.

Let’s see how to submit a simple job. If your job will only use the resources on a single node, here’s an example job submission script, _exSub_ in the section folder:

3

```
#!/bin/bash
```

```
####################
#SBATCHOPTIONS
####################
#SBATCH--job-name=example#jobnameforequeue,defaultmaybeu$
#SBATCH--partition=low#high/low/gpu,defaultifemptyislow
#SBATCH--error=ex.err#errorfile,defaultifemptyisslurm$
#SBATCH--output=ex.out#standardoutfile,nodefault
#SBATCH--time=00:01:00#optional,maxruntimeofjob
#SBATCH--nodes=1#onlyuse1node,MPIoption
#SBATCH--ntasks=1#howmanytaskstostart
#SBATCH--cpus-per-task=1#numberofcorestouse,multi-core/mu$
```

```
#jobnameforequeue,defaultmaybeu$
#high/low/gpu,defaultifemptyislow
#errorfile,defaultifemptyisslurm$
#standardoutfile,nodefault
#optional,maxruntimeofjobhours:minutes:seconds
#onlyuse1node,MPIoption
#howmanytaskstostart
```

```
####################
#Whattorun
####################
./example.sh
```

This script runs the following bash script, _example.sh_ in the section folder:

```
#!/bin/bash
#setfilename
fileName="testFile.txt"
#createfile
touch$fileName
#intromessage
echo"I’myournewtestscript!">>$fileName
echo>>$fileName
echo>>$fileName
#fillitwithsomethings
foriin{1..10}
do
echo$i>>$fileName
done
#finishitout
echo>>$fileName
echo>>$fileName
echo"AllFinished!">>$fileName
```

Now let’s submit and monitor the job:

```
sbatchexSub
squeue-u<SCF_USERNAME>
```

4

---

[← Interactive jobs](09-interactive-jobs.md) · [Up: contents](index.md) · [Parallel job submission →](11-parallel-job-submission.md)
