---
title: 1 Computer architecture
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Computer architecture

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Computers now come with multiple processors for doing computation. Basically, physical constraints have made it harder to keep increasing the speed of individual processors, so the chip industry is now putting multiple processing units in a given computer and trying/hoping to rely on implementing computations in a way that takes advantage of the multiple processors.

Everyday personal computers often have more than one processor (more than one chip) and on a given processor, often have more than one core (multi-core). A multi-core processor has multiple processors on a single computer chip. On personal computers, all the processors and cores share the same memory.

Supercomputers and computer clusters generally have tens, hundreds, or thousands of ’nodes’, linked by a fast local network. Each node is essentially a computer with its own processor(s) and memory. Memory is local to each node (distributed memory). One basic principle is that communication between a processor and its memory is much faster than communication between processors with different memory. An example of a modern supercomputer is the Jaguar supercomputer at Oak Ridge National Lab, which has 18,688 nodes, each with two processors and each processor

1

with 6 cores, giving 224,256 total processing cores. Each node has 16 Gb of memory for a total of 300 Tb.

There is little practical distinction between multi-processor and multi-core situations. The main issue is whether processes share memory or not. In general, I won’t distinguish between cores and processors. We’ll just focus on the number of cores on given personal computer or a given node in a cluster.

### **1.1 Distributed vs. shared memory**

There are two basic flavors of parallel processing (leaving aside GPUs): distributed memory and shared memory. With shared memory, multiple processors (which I’ll call cores for the rest of this document) share the same memory. With distributed memory, you have multiple nodes, each with their own memory. You can think of each node as a separate computer connected by a fast network.

Parallel programming for distributed memory parallelism requires passing messages between the different nodes. The standard protocol for doing this is MPI, of which there are various versions, including _openMPI_ . The R package _Rmpi_ implements MPI in R.

With shared memory parallelism, each core is accessing the same memory so there is no need to pass messages. But one needs to be careful that activity on different cores doesn’t mistakenly overwrite places in memory that are used by other cores. We’ll focus on shared memory parallelism here in this unit, though _Rmpi_ will come up briefly.

### **1.2 Types of memory**

In this course we’ve talked some about computer memory without distinguishing between main memory and the cache. The cache is a small amount of memory that can be accessed very quickly by the processing units, much more quickly than the main memory. The data in the cache is generally data that was previously retrieved from memory or recently computed. One principal for writing efficient code is to write code that makes effective use of the cache by using data that is already in the cache. In this course we won’t discuss this further given time constraints.

Note that there are different levels of cache, with L1 cache accessed more quickly than L2 cache and in turn L3 cache.

### **1.3 Graphics processing units (GPUs)**

GPUs were formerly a special piece of hardware used by gamers and the like for quickly rendering (displaying) graphics on a computer. They do this by having hundreds of processing units and breaking up the computations involved in an embarrassingly parallel fashion (i.e., without

2

inter-processor communication). For particular tasks, GPUs are very fast. Nowadays GPUs are generally built onto PC motherboards whereas previously they were on a video card.

Researchers (including some statisticians) are increasingly looking into using add-on GPUs to do massively parallel computations with inexpensive hardware that one can easily add to one’s existing machine. This has promise. However, some drawbacks in current implementations include the need to learn a specific programming language (similar to C) and limitations in terms of transferring data to the GPU and holding information in the memory of the GPU.

For more information you can see this workshop material that I presented in spring 2014.

### **1.4 Cloud computing**

Amazon (through its EC2 service) and other companies (Google and Microsoft now have similar products) offer computing through the cloud. The basic idea is that they rent out their servers on a pay-as-you-go basis. You get access to a virtual machine that can run various versions of Linux or Microsoft Windows server and where you choose the number of processing cores you want. You configure the virtual machine with the applications, libraries, and data you need and then treat the virtual machine as if it were a physical machine that you log into as usual. You can also assemble multiple virtual machines into your own virtual cluster. For some basic information on this, SCF has the following tutorial.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Parallelization →](03-2-parallelization.md)
