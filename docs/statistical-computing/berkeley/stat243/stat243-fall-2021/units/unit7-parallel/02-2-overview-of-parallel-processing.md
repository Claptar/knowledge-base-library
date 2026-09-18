---
title: 2 Overview of parallel processing
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit7-parallel.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit7-parallel.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Overview of parallel processing

## 2.1 Computer architecture

Computers now come with multiple processors for doing computation. Basically, physical constraints have made it harder to keep increasing the speed of individual processors, so the chip industry is now putting multiple processing units in a given computer and trying/hoping to rely on implementing computations in a way that takes advantage of the multiple processors.

Everyday personal computers usually have more than one processor (more than one chip) and on a given processor, often have more than one core (multi-core). A multi-core processor has multiple processors on a single computer chip. On personal computers, all the processors and cores share the same memory.

Supercomputers and computer clusters generally have tens, hundreds, or thousands of 'nodes', linked by a fast local network. Each node is essentially a computer with its own processor(s) and memory. Memory is local to each node (distributed memory). One basic principle is that communication between a processor and its memory is much faster than communication between processors with different memory. An example of a modern supercomputer is the Cori supercomputer at Lawrence Berkeley National Lab, which has 12,076 nodes, and a total of 735,200 cores. Each node has either 96 or 128 GB of memory for a total of 1.3 PB of memory.

For our purposes, there is little practical distinction between multi-processor and multi-core situations. The main issue is whether processes share memory or not. In general, I won’t distinguish between cores and processors. We’ll just focus on the number of cores on given personal computer or a given node in a cluster.

## 2.2 Some useful terminology:

• *cores*: We’ll use this term to mean the different processing units available on a single machine or node of a cluster.

• *nodes*: We’ll use this term to mean the different computers, each with their own distinct memory, that make up a cluster or supercomputer.

• *processes*: instances of a program(s) executing on a machine; multiple processes may be executing at once. A given program may start up multiple processes at once. Ideally we have no more processes than cores on a node.

• *workers*: the individual processes that are carrying out the (parallelized) computation. We’ll use worker and process interchangeably.

• *tasks*: individual units of computation; one or more tasks will be executed by a given process on a given core.

• *threads*: multiple paths of execution within a single process; the OS sees the threads as a single process, but one can think of them as 'lightweight' processes. Ideally when considering the processes and their threads, we would the same number of cores as we have processes and threads combined.

• *forking*: child processes are spawned that are identical to the parent, but with different process IDs and their own memory. In some cases if objects are not changed, the objects in the child process may refer back to the original objects in the original process, avoiding making copies.

• *sockets*: some of R’s parallel functionality involves creating new R processes (e.g., starting processes via *Rscript*) and communicating with them via a communication technology called sockets.

• *scheduler*: a program that manages users’ jobs on a cluster.

• *load-balanced*: when all the cores that are part of a computation are busy for the entire period of time the computation is running.

## 2.3 Distributed vs. shared memory

There are two basic flavors of parallel processing (leaving aside GPUs): distributed memory and shared memory. With shared memory, multiple processors (which I’ll call cores for the rest of this document) share the same memory. With distributed memory, you have multiple nodes, each with their own memory. You can think of each node as a separate computer connected by a fast network.

### 2.3.1 Shared memory

For shared memory parallelism, each core is accessing the same memory so there is no need to pass information (in the form of messages) between different machines. However, unless one is using threading (or in some cases when one has processes created by forking), objects will still be copied when creating new processes to do the work in parallel. With threaded computations, multiple threads can access object(s) without making explicit copies. But in some programming contexts one needs to be careful that the threads on different cores doesn’t mistakenly overwrite places in memory that are used by other cores (this is not an issue in R).

We’ll cover two types of shared memory parallelism approaches in this unit:

• threaded linear algebra
• multicore functionality

**Threading** Threads are multiple paths of execution within a single process. If you are monitoring CPU usage (such as with *top* in Linux or Mac) and watching a job that is executing threaded code, you’ll see the process using more than 100% of CPU. When this occurs, the process is using multiple cores, although it appears as a single process rather than as multiple processes.

Note that this is a different notion than a processor that is hyperthreaded. With hyperthreading a single core appears as two cores to the operating system.

### 2.3.2 Distributed memory

Parallel programming for distributed memory parallelism requires passing messages between the different nodes. The standard protocol for doing this is MPI, of which there are various versions, including *openMPI*.

While there are various R packages (e.g., *Rmpi* and the *pbdR* packages) that use MPI behind the scenes, we’ll only cover distributed memory parallelization via the future package and Dask, which don’t use MPI.

## 2.4 Some other approaches to parallel processing

### 2.4.1 GPUs

GPUs (Graphics Processing Units) are processing units originally designed for rendering graphics on a computer quickly. This is done by having a large number of simple processing units for massively parallel calculation. The idea of general purpose GPU (GPGPU) computing is to exploit this capability for general computation.

Most researchers don’t program for a GPU directly but rather use software (often machine learning software such as Tensorflow, PyTorch, or Caffe) that has been programmed to take advantage of a GPU if one is available.

### 2.4.2 Spark and Hadoop

Spark and Hadoop are systems for implementing computations in a distributed memory environment, using the MapReduce approach, as discussed in Unit 8.

### 2.4.3 Cloud computing

Amazon (Amazon Web Services’ EC2 service), Google (Google Cloud Platform’s Compute Engine service) and Microsoft (Azure) offer computing through the cloud. The basic idea is that they rent out their servers on a pay-as-you-go basis. You get access to a virtual machine that can run various versions of Linux or Microsoft Windows server and where you choose the number of processing cores you want. You configure the virtual machine with the applications, libraries, and data you need and then treat the virtual machine as if it were a physical machine that you log into as usual. You can also assemble multiple virtual machines into your own virtual cluster and use platforms such as Spark on the cloud

---

[← 1 Some scenarios for parallelization](01-1-some-scenarios-for-parallelization.md) · [Up: contents](index.md)
