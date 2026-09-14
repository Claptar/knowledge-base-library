---
title: 6. Additional details and topics (optional)
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit6-parallel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Additional details and topics (optional)

**Source:** [`units/unit6-parallel.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Setting the number of threads (cores used) in threaded code (including parallel linear algebra in R)

In general, threaded code will detect the number of cores available on a
machine and make use of them. However, you can also explicitly control
the number of threads available to a process.

For most threaded code (that based on the openMP protocol), the number
of threads can be set by setting the OMP_NUM_THREADS environment
variable (VECLIB_MAXIMUM_THREADS on a Mac). E.g., to set it for four
threads in the bash shell:

```bash
export OMP_NUM_THREADS=4
```

Do this before starting your R or Python session or before running your
compiled executable.

Alternatively, you can set OMP_NUM_THREADS as you invoke your job, e.g.,
here with R:

```bash
OMP_NUM_THREADS=4 R CMD BATCH --no-save job.R job.out
```


## Important warnings about use of threaded BLAS

### Speed and threaded BLAS

In many cases, using multiple threads for linear algebra operations will
outperform using a single thread, but there is no guarantee that this
will be the case, in particular for operations with small matrices and
vectors. You can compare speeds by setting OMP_NUM_THREADS to different
values. In cases where threaded linear algebra is slower than
unthreaded, you would want to set OMP_NUM_THREADS to 1.

More generally, if you are using the parallel tools in Section 4 to
simultaneously carry out many independent calculations (tasks), it is
likely to be more effective to use the fixed number of cores available
on your machine so as to split up the tasks, one per core, without
taking advantage of the threaded BLAS (i.e., restricting each process to
a single thread).

### Conflicts between openBLAS and various R functionality

In the past, I've seen various issues arising when using threaded linear
algebra. In some cases when the parallelization uses forking, I have
seen cases where R hangs and doesn't finish the linear algebra
calculation.

I've also seen a conflict between threaded linear algebra and R
profiling (recall the discussion of profiling in the efficient R tutorial).

Some solutions are to set OMP_NUM_THREADS to 1 to prevent the BLAS from
doing threaded calculations or to use parallelization approaches that
avoid forking.

---

[← 5. Illustrating the principles in specific case studies](07-5-illustrating-the-principles-in-specific-case-studies.md) · [Up: contents](index.md) · [7. Using Dask in Python →](09-7-using-dask-in-python.md)
