---
title: Logging in
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/scfOverview.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Logging in

**Source:** [`sections/08/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/scfOverview.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There login servers include: `arwen, beren, bilbo, gandalf, gimli, legolas, pooh, radagast, roo, shelob, springer, treebeard`

To login, in your UNIX terminal type:

```
sshSCF_USERNAME@LOGINSERVER.berkeley.edu
```

Then enter your password for your SCF account. One can then navigate around and get information using standard UNIX commands such as `ls` , `cd` , `du` , `df` , etc.

### **Logging out**

To logout you type `logout` in the command line.

### **Data transfer: SCP/SFTP**

We can use the _scp_ and _sftp_ protocols to transfer files from any login node on the SCF cluster.

For example, we show how to transfer the file `data.csv` .

To transfer that to your directoy on the SCF cluster, the syntax for `scp` is `scp <from-place> <to-place>`

Below are some examples of transferring this file to various locations on the remote machine (your home directory, a folder called data in your home directory, and the tmp folder)

```
#toSCF,whileonyourlocalmachine
scpdata.csvzoe_vernon@arwen.berkeley.edu:~/
scpdata.csvzoe_vernon@arwen.berkeley.edu:~/data/new_name.csv
scpdata.csvzoe_vernon@arwen.berkeley.edu:/tmp/
```

Here is how to transfer data from the SCF to your local machine, while on your local machine. This will transfer the `new_name.csv` file to your Desktop with the name `data_scf.csv`

```
#fromSCF,whileonyourlocalmachine
```

```
scpzoe_vernon@arwen.berkeley.edu:~/data/new_name.csv~/Desktop/data_scf.csv
```

2

One program you can use with Windows is _WinSCP_ , and a multi-platform program for doing transfers via SFTP is _FileZilla_ . After logging in, you’ll see windows for the SCF filesystem and your local filesystem on your machine. You can drag files back and forth.

### **Submitting jobs: accounts and partitions**

All computations are done by submitting jobs to the scheduling software that manages jobs on the cluster, called SLURM (Simple Linux Utility for Resource Management).

There is nothing you must specify to submit jobs to the SCF cluster, however, there are several options that are good form (more on this below).

### **Interactive jobs**

You can do work interactively.

For this, you may want to have used the -Y flag to ssh if you are running software with a GUI such as MATLAB.

```
#ssh-YSCF_USERNAME@arwen.berkeley.edu
srun--pty/bin/bash#interactivebashjob
srun--pty--x11=firstmatlab#interactivematlabjob
```

To display the graphical windows on your local machine, you’ll need X server software on your own machine to manage the graphical windows. For Windows, your options include _eXceed_ or _Xming_ and for Mac, there is _XQuartz_ .

This is not something I have much experience with, but if you are interested instructions are available here.

### **Submitting a batch job**

Or you can submit a job to run in the background.

Let’s see how to submit a simple job. If your job will only use the resources on a single node, here’s an example job submission script, _exSub_ in the section folder:

```
#!/bin/bash
```

#### `####################`

```
#SBATCHOPTIONS
####################
#SBATCH--job-name=example#jobnameforequeue,defaultmaybeu$
#SBATCH--partition=low#high/low/gpu,defaultifemptyislow
#SBATCH--error=ex.err#errorfile,defaultifemptyisslurm$
#SBATCH--output=ex.out#standardoutfile,nodefault
#SBATCH--time=00:01:00#hours:minutes:seconds
##SBATCH--nodes=1#onlyuse1node,MPIoption
##SBATCH--ntasks=1#howmanytaskstostart
##SBATCH--cpus-per-task=1#numberofcorestouse,multi-core/mu$
```

```
####################
#Whattorun
####################
```

```
./example.sh
```

3

This script runs the following bash script, _example.sh_ in the section folder:

```
#!/bin/bash
#setfilename
fileName="testFile.txt"
#createfile
touch$fileName
#intromessage
echo"I'myournewtestscript!">>$fileName
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
```

```
squeue-u<SCF_USERNAME>
```

### **Parallel job submission**

If you are submitting a job that uses multiple cores or nodes, you may need to carefully specify the resources you need. The key flags for use in your job script are:

- `--nodes` (or `-N` ): indicates the number of nodes to use

- `--ntasks-per-node` : indicates the number of tasks (i.e., processes) one wants to run on each node

- `--cpus-per-task` (or `-c` ): indicates the number of cpus to be used for each task

In addition, in some cases it can make sense to use the `--ntasks` (or `-n` ) option to indicate the total number of tasks and let the scheduler determine how many nodes and tasks per node are needed. In general `--cpus-per-task` will be 1 except when running threaded code.

When setting up parallel R code, you can find out how many cores there are on the node assigned to you with:

```
ncores<-Sys.getenv("SLURM_CPUS_ON_NODE")
```

In addition to SLURM_CPUS_ON_NODE here are some of the variables that may be useful: SLURM_NTASKS, SLURM_CPUS_PER_TASK, SLURM_NODELIST, SLURM_NNODES.

### **Monitoring jobs and the job queue**

The basic command for seeing what is running on the system is `squeue` :

4

```
squeue
```

```
squeue-uSCF_USERNAME
```

To see what nodes are available in a given partition:

```
sinfo-plow
sinfo-phigh
sinfo-pgpu
```

You can cancel a job with `scancel` . The job ID can be found on the left hand side when looking at the queue.

```
scancelYOUR_JOB_ID
```

The SCF has some tips about monitoring your job.

### **Exercise**

For the exercise in section we want you to get comfortable copying files from your local computer and running paralell computations on the SCF cluster. For this we will use an example from this webpage to compute bootstrap estimates of a coefficient in a logistic regression and compare the timing for a parallelized and non-parallelized version of the code. Your job is execute this code on the SCF.

To accomplish this you will need to complete the following tasks.

#### **Running on SCF**

- 1) Create a submission script `bootSub` that will execute the code in `boot.R` . To do this I suggest copying the text from `exSubR` and updating a couple lines:

   - Change job-name to whatever you want to call this job

   - Change rEx.err and rEx.out to boot.err and boot.out. Note these files can be useful for fixing bugs, particuarily when excecuting shell scripts. These files show errors and output printed to the terminal.

   - Change time to 00:10:00 just in case your code runs longer than one minute.

   - Change the cpus per task to 3. This is where you are telling SLURM to execute in parallel on 3 nodes.

   - Change the last line `R CMD BATCH --no-save boot.R boot.Rout` . The `boot.Rout` file will contain all of code, messages, errors, etc. from the R session.

- 2) Transfer the files `boot.R` and `bootSub` to your SCF account. This can be done using `scp` before logging onto the SCF cluster (see examples above)

   - Note, there are other ways to transfer files. For example, one other option would be to clone the repo for this class onto your SCF account after logging in.

- 3) Call `sbatch bootSub` to excecute the R script `boot.R` .

- 4) Check that the excecution worked by examining the `.Rout` file.

- 5) If you have time:

   - Update parallel code to be execute with the `future` package to compare the results.

5

---

[← Disk Space](05-disk-space.md) · [Up: contents](index.md)
