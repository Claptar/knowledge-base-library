---
title: 7 Job Control
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Job Control

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Starting a job** When you run a command in a shell by simply typing its name, you are said to be running in the foreground. When a job is running in the foreground, you can’t type additional commands into that shell session, but there are two signals that can be sent to the running job through the keyboard. To interrupt a program running in the foreground, use C-c; to quit a program, use C-\. While modern windowed systems have lessened the inconvenience of tying up a shell with foreground processes, there are some situations where running in the foreground is not adequate.

The primary need for an alternative to foreground processing arises when you wish to have jobs continue to run after you log off the computer. In cases like this you can run a program in the background by simply terminating the command with an ampersand ( _&_ ). However, before putting a job in the background, you should consider how you will access its results, since _stdout_ is not preserved when you log off from the computer. Thus, redirection (including redirection of _stderr_ ) is essential when running jobs in the background. As a simple example, suppose that you wish to run an R script, and you don’t want it to terminate when you log off. (Note that this can also be done using R CMD BATCH, so this is primarily an illustration.)

> R --no-save < code.R > code.Rout 2>&1 &

If you forget to put a job in the background when you first execute it, you can do it while it’s running in the foreground in two steps. First, suspend the job using the **C-z** signal. After receiving the signal, the program will interrupt execution, but will still have access to all files and other resources. Next, issue the _bg_ command, which will put the stopped job in the background.

**Listing and killing jobs** Since only foreground jobs will accept signals through the keyboard, if you want to terminate a background job you must first determine the unique process id (PID) for the process you wish to terminate through the use of the _ps_ command. For example, to see all the jobs running on a particular computer, you could use a command like:

> ps -aux

Among the output after the header (shown here) might appear a line that looks like this: USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND paciorek 11998 97.0 39.1 1416644 1204824 pts/16 R+ Jul27 1330:01 /usr/lib64/R/bin/exec/R

In this example, the _ps_ output tells us that this R job has a PID of _11998_ , that it has been running for 1330 minutes (!), is using 97% of CPU and 39% of memory, and that it started on July 27. You could then issue the command:

> kill 11998

or, if that doesn’t work

7

> kill -9 11998

to terminate the job. Another useful command in this regard is _killall_ , which accepts a program name instead of a process id, and will kill all instances of the named program. E.g.,

> killall R

Of course, it will only kill the jobs that belong to you, so it will not affect the jobs of other users. Note that the _ps_ and _kill_ commands only apply to the particular computer on which they are executed, not to the entire computer network. Thus, if you start a job on one machine, you must log back into that same machine in order to manage your job.

**Monitoring jobs and memory use** The _top_ command also allows you to monitor the jobs on the system and in real-time. In particular, it’s useful for seeing how much of the CPU and how much memory is being used, as well as figuring out a PID as an alternative to _ps_ . You can also renice jobs (see below) and kill jobs from within top: just type _r_ or _k_ , respectively, and proceed from there.

One of the main things to watch out for is a job that is using close to 100% of memory and much less than 100% of CPU. What is generally happening is that your program has run out of memory and is using virtual memory on disk, spending most of its time writing to/from disk, sometimes called _paging_ or _swapping_ . If this happens, it can be a very long time, if ever, before your job finishes.

**Nicing a job** The most important thing to remember when starting a job on a machine that is not your personal machine is how to be a good citizen. This often involves ’nicing’ your jobs. This is required on the SCF machines, but the compute servers should automatically nice your jobs. Nicing a job puts it at a lower priority so that a user working at the keyboard has higher priority in using the CPU. Here’s how to do it, giving the job a low priority of 19, as required by SCF:

> nice -19 R CMD BATCH --no-save code.R code.Rout &

If you forget and just submit the job without nicing, you can reduce the priority by doing:

> renice +19 11998

where _11998_ is the PID of your job.

On many larger UNIX cluster computers, all jobs are submitted via a job scheduler and enter a queue, which handles the issue of prioritization and jobs conflicting. Syntax varies by system and queueing software, but may look something like this for submitting an R job: > bsub -q long R CMD BATCH --no-save code.R code.Rout # just an example; this will not work on the SCF network

8

---

[← 6 Redirection](06-6-redirection.md) · [Up: contents](index.md) · [8 Aliases →](08-8-aliases.md)
