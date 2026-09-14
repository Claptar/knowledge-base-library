---
title: 2 Parallelization
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Parallelization

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Overview**

A lot of parallel processing follows a master-slave paradigm. There is one master process that controls one or more slave processes. The master process sends out tasks and data to the slave processes and collects results back.

One comment about parallelized code is that it can be difficult to debug because communication problems can occur in addition to standard bugs. Debugging may require some understanding of the communication that goes on between processors. If you can first debug your code on one processor, that can be helpful.

### **2.2 Threading**

One form of shared-memory parallel processing is _threading_ . Here an algorithm is implemented across multiple “light-weight” processes called _threads_ in a shared memory situation. Threads are multiple paths of execution within a single process. One can write one’s own code to make use

3

of threading, e.g., using the _openMP_ protocol for C/C++/Fortran. For our purpose we’ll focus on using pre-existing code or libraries that are threaded, specifically threaded versions of the BLAS.

In R, the basic strategy is to make sure that the R installation uses a threaded BLAS so that standard linear algebra computations are done in a threaded fashion. We can do this by linking R to a threaded BLAS library. Details can be found in Section A.3.1.5 of the R administration manual or talk to your system administrator.

Note that in R, the threading only helps with linear algebra operations (but the _pqR_ engine seeks to change this - see my brief mention of _pqR_ in Unit 6). In contrast, Matlab uses threading for a broader range of calculations.

#### **2.2.1 The BLAS**

The BLAS is the library of basic linear algebra operations (written in Fortran or C). A fast BLAS can greatly speed up linear algebra relative to the default BLAS on a machine. Some fast BLAS libraries are Intel’s _MKL_ , AMD’s _ACML_ , Apple’s _VecLib_ and the open source (and free) _openBLAS_ (formerly _GotoBLAS_ ). All of these BLAS libraries are now threaded - if your computer has multiple cores and there are free resources, your linear algebra will use multiple cores, provided your program is linked against the specific BLAS. Using _top_ (on a machine other than the cluster), you’ll see the process using more than 100% of CPU. inconceivable! The default BLAS on the SCF Linux compute servers is _openBLAS_ and on the SCF Linux cluster is _ACML_ . The SCF Macs use _VecLib_ , but this is not the default on Macs; ask me if you’d like more information on setting it up on your Mac.

**require** (RhpcBLASctl) _## Loading required package: RhpcBLASctl_ Z <- **matrix** ( **rnorm** (5000^2), 5000) **omp_set_num_threads** (1) **system.time** ({ X <- **crossprod** (Z) _# Z^t Z produces pos.def. matrix_ U <- **chol** (X) }) _# U^t U = X_ ## user system elapsed ## 15.929 0.072 16.073

4

**omp_set_num_threads** (4) **system.time** ({ X <- **crossprod** (Z) U <- **chol** (X) }) ## user system elapsed ## 22.949 0.108 6.997

#### **2.2.2 Fixing the number of threads (cores used)**

In general, if you want to limit the number of threads used, you can set the OMP_NUM_THREADS UNIX environment variable (VECLIB_MAXIMUM_THREADS on a Mac. This can be used in the context of R or C code that uses BLAS or your own threaded C code, but this does not work with Matlab. In the UNIX bash shell, you’d do this as follows (e.g. to limit to 3 cores) (do this before starting R):

export OMP_NUM_THREADS=3 # or “setenv OMP_NUM_THREADS 1” if using csh/tcsh

#### **2.2.3 Problems with the threaded BLAS in R**

All of these problems can be alleviated by setting OMP_NUM_THREADS to 1.

1. There is a conflict between forking in R and the threaded BLAS that in some cases affects _foreach_ (when using the _multicore_ and _parallel_ backends), _mclapply()_ , and (only if _cluster()_ is set up with forking (not the default)) _par{L,S,}apply()_ . The result is that if linear algebra is used within your parallel code, R hangs. This affects both _openBLAS_ and _ACML_ under certain circumstances, so affects the SCF Linux machines. Alternatively, you can use MPI as the parallel backend (via _doMPI_ in place of _doMC_ or _doParallel_ ). You may also be able to convert your code to use _par{L,S,}apply()_ [with the default PSOCK type] and avoid _foreach_ entirely.

2. There is also a conflict between threaded BLAS and R profiling, so if you are using _Rprof()_ , you may need to set OMP_NUM_THREADS to one.

#### **2.2.4 It may not make sense to use the threaded BLAS**

In many cases, using multiple threads for linear algebra operations will outperform using a single thread, but there is no guarantee that this will be the case, in particular for operations with

5

small matrices and vectors. Testing with _openBLAS_ suggests that sometimes a job may take more time when using multiple threads; this seems to be less likely with ACML. This presumably occurs because openBLAS is not doing a good job in detecting when the overhead of threading outweights the gains from distributing the computations. You can compare speeds by setting OMP_NUM_THREADS to different values. In cases where threaded linear algebra is slower than unthreaded, you would want to set OMP_NUM_THREADS to 1.

More generally, if you have an embarrassingly parallel job, it is likely to be more effective to use the fixed number of multiple cores you have access to to split along the embarrassingly parallel dimension without taking advantage of the threaded BLAS (i.e., restricting each process to a single thread).

Therefore I recommend that you test any large jobs to compare performance with a single thread vs. multiple threads. Only if you see a substantive improvement with multiple threads does it make sense to have OMP_NUM_THREADS be greater than one.

### **2.3 Embarrassingly parallel (EP) problems**

An EP problem is one that can be solved by doing independent computations as separate processes without communication between the processes. You can get the answer by doing separate tasks and then collecting the results. Examples in statistics include

1. simulations with many independent replicates

2. bootstrapping

3. stratified analyses

The standard setup is that we have the same code running on different datasets. (Note that different processes may need different random number streams, as we will discuss in the Simulation Unit.)

To do parallel processing in this context, you need to have control of multiple processes. Note that on a shared system with queueing software set up, this will generally mean requesting access to a certain number of processors and then running your job in such a way that you use multiple processors.

In general, except for some modest overhead, an EP problem can ideally be solved with 1 _/p_ the amount of time for the non-parallel implementation, given _p_ processors. This gives us a speedup of _p_ , which is called linear speedup (basically anytime the speedup is of the form _cp_ for some constant _c_ ).

One difficulty is load balancing. We’d like to make sure each slave process finishes at the same time. Often we can give each process the same amount of work, but if we have a mix of faster

6

and slower processors, things become more difficult. To the extent it is possible to break up a job into many small tasks and have processors start new tasks as they finish off old tasks, this can be effective, but may involve some parallel programming.

**Question** : What do you think the tradeoffs are between breaking up a problem into many small subtasks vs. a few large subtasks?

In the next section, we’ll see a few approaches in R for dealing with EP problems.

### **2.4 Parallelization with communication**

If we do not have an EP problem, we have one that involves some sort of serial calculation. As a result, different processes need to communicate with each other. There are standard protocols for such communication, with _MPI_ being most common. You can use C libraries that implement these protocols. While MPI has many functions, a core of 6-10 functions (basic functions for functionality such as sending and receiving data between processes - either master-slave or slaveslave) are what we mostly need.

R provides the _Rmpi_ library, which allows you to do message passing in R. It has some drawbacks, but may be worth exploring if you have a non-EP problem and don’t want to learn C. Installing _Rmpi_ may be tricky and on institutional machines will require you talk to your systems administrator. _Rmpi_ is a basic building block for other parallel processing functionality such as the _doMPI_ backend to _foreach_ and for _SNOW_ .

For non-EP problems, the primary question is how the speed of the computation scales with _p_ . This will generally be much worse than 1 _/p_ . Furthermore, as _p_ increases, if communication must increase as well, then the speedup can be much worse. Your work can become communicationbound rather than CPU-bound. Whenever messages are sent, there is a cost that scales with the number of message sent (called _latency_ ) and a cost that scales with the amount of data that is passed in those messages.

The term high-performance computing (HPC) is the term associated with tools and theory for doing parallel processing involving this sort of communication.

---

[← 1 Computer architecture](02-1-computer-architecture.md) · [Up: contents](index.md) · [3 Explicit parallel code in R →](04-3-explicit-parallel-code-in-r.md)
