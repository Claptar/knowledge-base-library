---
title: 5 Additional details and topics
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Additional details and topics

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Limitations in Windows**

Forking in R is not possible on Windows, so parallelization on Windows would generally need to use approaches based on sockets and not based on forking.

### **5.2 Setting the number of threads (cores used) in threaded code (including parallel linear algebra in R)**

In general, threaded code will detect the number of cores available on a machine and make use of them. However, you can also explicitly control the number of threads available to a process.

For most threaded code (that based on the openMP protocol), the number of threads can be set by setting the OMP_NUM_THREADS environment variable (VECLIB_MAXIMUM_THREADS

20

on a Mac). E.g., to set it for four threads in the bash shell:

<mark>export OMP_NUM_THREADS=4</mark>

Do this before starting your R or Python session or before running your compiled executable. Alternatively, you can set OMP_NUM_THREADS as you invoke your job, e.g., here with R:

<mark>OMP_NUM_THREADS=4 R CMD BATCH --no-save job.R job.out</mark>

### **5.3 Important warnings about use of threaded BLAS**

#### **5.3.1 Speed and threaded BLAS**

In many cases, using multiple threads for linear algebra operations will outperform using a single thread, but there is no guarantee that this will be the case, in particular for operations with small matrices and vectors. Testing with openBLAS suggests that sometimes a job may take more time when using multiple threads; this seems to be less likely with ACML. This presumably occurs because openBLAS is not doing a good job in detecting when the overhead of threading outweights the gains from distributing the computations. You can compare speeds by setting OMP_NUM_THREADS to different values. In cases where threaded linear algebra is slower than unthreaded, you would want to set OMP_NUM_THREADS to 1.

More generally, if you are using the parallel tools in Section 4 to simultaneously carry out many independent calculations (tasks), it is likely to be more effective to use the fixed number of cores available on your machine so as to split up the tasks, one per core, without taking advantage of the threaded BLAS (i.e., restricting each process to a single thread).

#### **5.3.2 Conflicts between openBLAS and various R functionality**

In the past, I’ve seen various issues arising when using threaded linear algebra. In some cases when the parallelization uses forking, I have seen cases where R hangs and doesn’t finish the linear algebra calculation.

I’ve also seen a conflict between threaded linear algebra and R profiling (recall the discussion of profiling in Unit 4).

Some solutions are to set OMP_NUM_THREADS to 1 to prevent the BLAS from doing threaded calculations or to use parallelization approaches that avoid forking.

21

### **5.4 Other packages for parallelization in R**

#### **5.4.1 The** **_future_ package**

The _future_ package and related packages ( _future.apply_ , _future.batchtools_ ) are an entire system for doing computations in parallel in an integrated system where you can write your code once and then deploy it in multiple different parallelization contexts by simply changing some initial code that controls how the parallelization is done.

#### **5.4.2 The** **_partools_ package**

_partools_ is a new package developed by Norm Matloff at UC-Davis. He has the perspective that Spark/Hadoop are not the right tools in many cases when doing statistics-related work and has developed some simple tools for parallelizing computation across multiple nodes, also referred to as _Snowdoop_ . The tools make use of the key idea in Hadoop of a distributed file system and distributed data objects but avoid the complications of trying to ensure fault tolerance, which is critical only on very large clusters of machines.

#### **5.4.3** **_pbdR_**

_pbdR_ is an effort to enhance R’s capability for distributed memory processing called pbdR (http://rpbd.org). For an extensive tutorial, see the pbdDEMO vignette (https://github.com/wrathematics/pbdDEMO/blob/master/inst/doc/pbdDEMOguide.pdf?raw=true). _pbdR_ is designed for SPMD processing in batch mode, which means that you start up multiple processes in a non-interactive fashion using mpirun. The same code runs in each R process so you need to have the code behavior depend on the process ID.

_pbdR_ provides the following capabilities:

- the ability to do some parallel apply-style computations (this section),

- the ability to do distributed linear algebra by interfacing to _ScaLapack_ , and

- an alternative to _Rmpi_ for interfacing with MPI.

Personally, I think the second of the three is the most exciting as it’s a functionality not readily available in R or even more generally in other readily-accessible software.

22

---

[← 4 Illustrating the principles in specific case studies](05-4-illustrating-the-principles-in-specific-case-studies.md) · [Up: contents](index.md)
