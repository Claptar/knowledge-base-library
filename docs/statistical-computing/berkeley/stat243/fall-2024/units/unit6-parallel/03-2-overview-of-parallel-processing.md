---
title: 2. Overview of parallel processing
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Overview of parallel processing

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Computer architecture

Computers now come with multiple processors for doing computation.
Basically, physical constraints have made it harder to keep increasing
the speed of individual processors, so the chip industry is now putting
multiple processing units in a given computer and trying/hoping to rely
on implementing computations in a way that takes advantage of the
multiple processors.

Everyday personal computers usually have more than one processor (more
than one chip) and on a given processor, often have more than one core
(multi-core). A multi-core processor has multiple processors on a single
computer chip. On personal computers, all the processors and cores share
the same memory.

Supercomputers and computer clusters generally have tens, hundreds, or
thousands of 'nodes', linked by a fast local network. Each node is
essentially a computer with its own processor(s) and memory. Memory is
local to each node (distributed memory). One basic principle is that
communication between a processor and its memory is much faster than
communication between processors with different memory. An example of a
modern supercomputer is the Perlmutter supercomputer at Lawrence Berkeley
National Lab, which has 3072 CPU-only nodes and 1792 nodes with GPUs, and a total of about 500,000 CPU cores. Each
node has 512 GB of memory for a total of 2.3 PB of memory.

For our purposes, there is little practical distinction between
multi-processor and multi-core situations. The main issue is whether
processes share memory or not. In general, I won't distinguish between
cores and processors. We'll just focus on the number of cores on given
personal computer or a given node in a cluster.

## Some useful terminology:

-   *cores*: We'll use this term to mean the different processing units
    available on a single machine or node of a cluster. A given CPU will
    have multiple cores. (E.g, the AMD EPYC 7763 has 64 cores per CPU.)
-   *nodes*: We'll use this term to mean the different computers, each
    with their own distinct memory, that make up a cluster or
    supercomputer.
-   *processes*: instances of a program(s) executing on a machine;
    multiple processes may be executing at once. A given program may
    start up multiple processes at once. Ideally we have no more
    processes than cores on a node.
-   *workers*: the individual processes that are carrying out the
    (parallelized) computation. We'll use *worker* and *process*
    interchangeably.
-   *tasks*: individual units of computation; one or more tasks will be
    executed by a given process on a given core.
-   *threads*: multiple paths of execution within a single process; the
    operating system sees the threads as a single process, but one can think of them
    as 'lightweight' processes. Ideally when considering the processes
    and their threads, we would have the same number of cores available to our code as we have
    processes and threads combined.
-   *forking*: child processes are spawned that are identical to the
    parent, but with different process IDs and their own memory. In some
    cases if objects are not changed, the objects in the child process
    may refer back to the original objects in the original process,
    avoiding making copies.
-   *scheduler*: a program that manages users' jobs on a cluster.
    *Slurm* is a commonly used scheduler.
-   *load-balanced*: when all the cores that are part of a computation
    are busy for the entire period of time the computation is running.
-   *sockets*: some of R's parallel functionality involves creating new
    R processes (e.g., starting processes via `Rscript`) and
    communicating with them via a communication technology called
    sockets.

## Distributed vs. shared memory

There are two basic flavors of parallel processing (leaving aside GPUs):
distributed memory and shared memory. With shared memory, multiple
processors (which I'll call cores for the rest of this document) share
the same memory. With distributed memory, you have multiple nodes, each
with their own memory. You can think of each node as a separate computer
connected by a fast network.

### Shared memory

For shared memory parallelism, each core is accessing the same memory so
there is no need to pass information (in the form of messages) between
different machines. However, unless one is using threading (or in some
cases when one has processes created by forking), objects will still be
copied when creating new processes to do the work in parallel. With
threaded computations, multiple threads can access object(s) without
making explicit copies. But in some programming contexts one needs to be
careful that the threads on different cores doesn't mistakenly overwrite
places in memory that are used by other cores (this is generally not an issue in
Python or R).

We'll cover two types of shared memory parallelism approaches in this
unit:

-   threaded linear algebra
-   multicore functionality

#### Threading

Threads are multiple paths of execution within a single process. If you
are monitoring CPU usage (such as with `top` in Linux or Mac) and
watching a job that is executing threaded code, you'll see the process
using more than 100% of CPU. When this occurs, the process is using
multiple cores, although it appears as a single process rather than as
multiple processes.

Note that this is a different notion than a processor that is
hyperthreaded. With hyperthreading a single core appears as two cores to
the operating system.

### Distributed memory

Parallel programming for distributed memory parallelism requires passing
messages between the different nodes. The standard protocol for doing
this is MPI, of which there are various versions, including `openMPI`.

While there are various Python and R that use MPI behind the scenes, we'll only cover distributed
memory parallelization via `Dask`, which doesn't use
MPI.

## GPUs

GPUs (Graphics Processing Units) are processing units originally
designed for rendering graphics on a computer quickly. This is done by
having a large number of simple processing units for massively parallel
calculation. The idea of general purpose GPU (GPGPU) computing is to
exploit this capability for general computation.

Most researchers don't program for a GPU directly but rather use
software (often machine learning software such as Tensorflow or PyTorch,
or other software that automatically uses the GPU such as JAX)
 that has been programmed to take advantage of a GPU if one is
available. The computations that run on the GPU are run in GPU *kernels*,
which are functions that are launched on the GPU. The overall workflow
runs on the CPU and then particular (usually computationally-intensive
tasks for which parallelization is helpful) tasks are handed off to the GPU.
GPUs and similar devices (e.g., TPUs) are often called "co-processors"
in recognition of this style of workflow.

The memory on a GPU is distinct from main memory on the computer, so
when writing code that will use the GPU, one generally wants to avoid
having large amounts of data needing to be transferred back and forth between
main (CPU) memory and GPU memory. Also, since there is overhead in
launching a GPU kernel, one wants to avoid launching a lot of kernels
relative to the amount of work being done by each kernel.

## Some other approaches to parallel processing

### Spark and Hadoop

Spark and Hadoop are systems for implementing computations in a
distributed memory environment, using the MapReduce approach, as
discussed in Unit 7.

### Cloud computing

Amazon (Amazon Web Services' EC2 service), Google (Google Cloud
Platform's Compute Engine service) and Microsoft (Azure) offer computing
through the cloud. The basic idea is that they rent out their servers on
a pay-as-you-go basis. You get access to a virtual machine that can run
various versions of Linux or Microsoft Windows server and where you
choose the number of processing cores you want. You configure the
virtual machine with the applications, libraries, and data you need and
then treat the virtual machine as if it were a physical machine that you
log into as usual. You can also assemble multiple virtual machines into
your own virtual cluster and use platforms such as databases and Spark on the cloud
provider's virtual machines.

---

[← 1. Some scenarios for parallelization](02-1-some-scenarios-for-parallelization.md) · [Up: contents](index.md) · [3. Parallelization strategies →](04-3-parallelization-strategies.md)
