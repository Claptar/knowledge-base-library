---
title: 2 Threading, particularly for linear algebra
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit7-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Threading, particularly for linear algebra

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 What is the BLAS?**

The BLAS is the library of basic linear algebra operations (written in Fortran or C). A fast BLAS can greatly speed up linear algebra relative to the default BLAS on a machine. Some fast BLAS libraries are

- Intel’s _MKL_ ; may be available for educational use for free

- _OpenBLAS_ ; open source and free

- AMD’s _ACML_ ; free

- _vecLib_ for Macs; provided with your Mac

In addition to being fast when used on a single core, all of these BLAS libraries are threaded - if your computer has multiple cores and there are free resources, your linear algebra will use multiple cores, provided your program is linked against the threaded BLAS installed on your machine and

4

provided the environment variable OMP_NUM_THREADS is not set to one. (Macs make use of VECLIB_MAXIMUM_THREADS rather than OMP_NUM_THREADS.)

On the SCF, R is linked against OpenBLAS.

### **2.2 Using threading**

Threading in R is limited to linear algebra, provided R is linked against a threaded BLAS. Here’s some code that illustrates the speed of using a threaded BLAS:

_## be careful here - I'm having problems with ## this package causing R to crash... # require(RhpcBLASctl) ## alternatively just start R multiple times having ## set OMP_NUM_THREADS outside of R_ Z <- **matrix** ( **rnorm** (5000^2), 5000) _## blas_set_num_threads(4)_ **system.time** ({ X <- **crossprod** (Z) _# Z^t Z produces pos.def. matrix_ U <- **chol** (X) _# U^t U = X_ }) _# user system elapsed # 7.216 1.096 2.219 ## blas_set_num_threads(1)_ **system.time** ({ X <- **crossprod** (Z) U <- **chol** (X) }) _# user system elapsed # 6.360 0.204 6.563_

Here the elapsed time indicates that using four threads gave us a three fold (3x) speedup in terms of real time, while the user time indicates that the threaded calculation took a bit more total

5

processing time (combining time across all processors) because of the overhead of using multiple threads.

Note that the code also illustrates use of an R package ( _RhpcBLASctl_ ) that can control the number of threads from within R.

### **2.3 Setting the number of threads (cores used)**

In general, threaded code will detect the number of cores available on a machine and make use of them. However, you can also explicitly control the number of threads available to a process.

For most threaded code (that based on the openMP protocol), the number of threads can be set by setting the OMP_NUM_THREADS environment variable (VECLIB_MAXIMUM_THREADS on a Mac). E.g., to set it for four threads in the bash shell:

<mark>export OMP_NUM_THREADS=4</mark>

Do this before starting your R or Python session or before running your compiled executable. Alternatively, you can set OMP_NUM_THREADS as you invoke your job, e.g., here with R:

<mark>OMP_NUM_THREADS=4 R CMD BATCH --no-save job.R job.out</mark>

### **2.4 Important warnings about use of threaded BLAS**

#### **2.4.1 Speed and threaded BLAS**

In many cases, using multiple threads for linear algebra operations will outperform using a single thread, but there is no guarantee that this will be the case, in particular for operations with small matrices and vectors. Testing with openBLAS suggests that sometimes a job may take more time when using multiple threads; this seems to be less likely with ACML. This presumably occurs because openBLAS is not doing a good job in detecting when the overhead of threading outweights the gains from distributing the computations. You can compare speeds by setting OMP_NUM_THREADS to different values. In cases where threaded linear algebra is slower than unthreaded, you would want to set OMP_NUM_THREADS to 1.

More generally, if you are using the parallel tools in Section 3 to simultaneously carry out many independent calculations (tasks), it is likely to be more effective to use the fixed number of cores available on your machine so as to split up the tasks, one per core, without taking advantage of the threaded BLAS (i.e., restricting each process to a single thread).

6

#### **2.4.2 Conflicts between openBLAS and various R functionality**

In the past, I’ve seen various issues arising when using threaded linear algebra. In some cases when the parallelization uses forking (we’ll see when this is the case later in the unit), I have seen cases where R hangs and doesn’t finish the linear algebra calculation.

I’ve also seen a conflict between threaded linear algebra and R profiling (recall the discussion of profiling in Unit 4).

Some solutions are to set OMP_NUM_THREADS to 1 to prevent the BLAS from doing threaded calculations or to use parallelization approaches that avoid forking.

### **2.5 Using an optimized BLAS on your own machine(s)**

To use an optimized BLAS with R, talk to your systems administrator, see Section A.3 of the R Installation and Administration Manual or see these instructions to use vecLib BLAS from Apple’s Accelerate framework on your own Mac.

---

[← 1 Overview](02-1-overview.md) · [Up: contents](index.md) · [3 Basic parallelized loops/maps/apply →](04-3-basic-parallelized-loops-maps-apply.md)
