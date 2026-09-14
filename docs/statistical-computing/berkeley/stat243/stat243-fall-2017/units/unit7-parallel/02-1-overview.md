---
title: 1 Overview
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit7-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Overview

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Computer architecture**

Computers now come with multiple processors for doing computation. Basically, physical constraints have made it harder to keep increasing the speed of individual processors, so the chip industry is now putting multiple processing units in a given computer and trying/hoping to rely on implementing computations in a way that takes advantage of the multiple processors.

Everyday personal computers usually have more than one processor (more than one chip) and on a given processor, often have more than one core (multi-core). A multi-core processor has multiple processors on a single computer chip. On personal computers, all the processors and cores share the same memory.

Supercomputers and computer clusters generally have tens, hundreds, or thousands of ’nodes’, linked by a fast local network. Each node is essentially a computer with its own processor(s) and memory. Memory is local to each node (distributed memory). One basic principle is that communication between a processor and its memory is much faster than communication between

1

processors with different memory. An example of a modern supercomputer is the Edison supercomputer at Lawrence Berkeley National Lab, which has 5,586 nodes, each with two processors and each processor with 12 cores, giving 134,064 total processing cores. Each node has 64 GB of memory for a total of 357 TB of memory.

There is little practical distinction between multi-processor and multi-core situations. The main issue is whether processes share memory or not. In general, I won’t distinguish between cores and processors. We’ll just focus on the number of cores on given personal computer or a given node in a cluster.

### **1.2 Some useful terminology:**

- cores: We’ll use this term to mean the different processing units available on a single node.

- nodes: We’ll use this term to mean the different computers, each with their own distinct memory, that make up a cluster or supercomputer.

- processes: computational tasks executing on a machine; multiple processes may be executing at once. A given program may start up multiple processes at once. Ideally we have no more processes than cores on a node.

- threads: multiple paths of execution within a single process; the OS sees the threads as a single process, but one can think of them as ’lightweight’ processes. Ideally when considering the processes and their threads, we would the same number of cores as we have processes and threads combined.

- forking: child processes are spawned that are identical to the parent, but with different process IDs and their own memory.

- sockets: some of R’s parallel functionality involves creating new R processes (e.g., starting processes via _Rscript_ ) and communicating with them via a communication technology called sockets.

### **1.3 Distributed vs. shared memory**

There are two basic flavors of parallel processing (leaving aside GPUs): distributed memory and shared memory. With shared memory, multiple processors (which I’ll call cores for the rest of this document) share the same memory. With distributed memory, you have multiple nodes, each with their own memory. You can think of each node as a separate computer connected by a fast network.

2

#### **1.3.1 Shared memory**

For shared memory parallelism, each core is accessing the same memory so there is no need to pass information (in the form of messages) between different machines. But in some programming contexts one needs to be careful that activity on different cores doesn’t mistakenly overwrite places in memory that are used by other cores.

We’ll cover two types of shared memory parallelism approaches in this unit:

- threaded linear algebra

- multicore functionality

**Threading** Threads are multiple paths of execution within a single process. If you are monitoring CPU usage (such as with _top_ in Linux or Mac) and watching a job that is executing threaded code, you’ll see the process using more than 100% of CPU. When this occurs, the process is using multiple cores, although it appears as a single process rather than as multiple processes.

Note that this is a different notion than a processor that is hyperthreaded. With hyperthreading a single core appears as two cores to the operating system.

#### **1.3.2 Distributed memory**

Parallel programming for distributed memory parallelism requires passing messages between the different nodes. The standard protocol for doing this is MPI, of which there are various versions, including _openMPI_ .

The R package _Rmpi_ implements MPI in R. The _pbdR_ packages for R also implement MPI as well as distributed linear algebra (linear algebra calculations across nodes). In addition, there are various ways to do simple parallelization of multiple computational tasks (across multiple nodes) that use MPI and other tools on the back-end without users needing to understand them. We won’t cover distributed memory parallelization in this Unit, but we will touch on a flavor of it via Spark in Unit 8.

### **1.4 Some other approaches to parallel processing**

#### **1.4.1 GPUs**

GPUs (Graphics Processing Units) are processing units originally designed for rendering graphics on a computer quickly. This is done by having a large number of simple processing units for massively parallel calculation. The idea of general purpose GPU (GPGPU) computing is to exploit this capability for general computation. In spring 2016, I gave a workshop on using GPUs.

3

Most researchers don’t program for a GPU directly but rather use software (often machine learning software such as Tensorflow or Caffe) that has been programmed to take advantage of a GPU if one is available.

#### **1.4.2 Spark and Hadoop**

Spark and Hadoop are systems for implementing computations in a distributed memory environment, using the MapReduce approach. We’ll see this in the next unit.

#### **1.4.3 Cloud computing**

Amazon (Amazon Web Services’ EC2 service), Google (Google Cloud Platform’s Compute Engine service) and Microsoft (Azure) offer computing through the cloud. The basic idea is that they rent out their servers on a pay-as-you-go basis. You get access to a virtual machine that can run various versions of Linux or Microsoft Windows server and where you choose the number of processing cores you want. You configure the virtual machine with the applications, libraries, and data you need and then treat the virtual machine as if it were a physical machine that you log into as usual. You can also assemble multiple virtual machines into your own virtual cluster and use platforms such as Spark on the cloud provider’s virtual machines.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Threading, particularly for linear algebra →](03-2-threading-particularly-for-linear-algebra.md)
