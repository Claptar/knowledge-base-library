---
title: 5 Implementation of simulation studies
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit10-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit10-sim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Implementation of simulation studies

**Source:** [`units/unit10-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit10-sim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Computational efficiency**

Parallel processing is often helpful for simulation studies. The reason is that simulation studies are embarrassingly parallel - we can send each replicate to a different computer processor and then collect the results back, and the speedup should scale directly with the number of processors we used. Since we often need to some sort of looping, writing code in C/C++ and compiling and

16

linking to the code from R may also be a good strategy, albeit one not covered in this course.

Handy functions in R include _expand.grid()_ to get all combinations of a set of vectors and the _replicate()_ function in R, which will carry out the same R expression (often a function call) repeated times. This can replace the use of a _for_ loop with some gains in cleanliness of your code. Storing results in an array is a natural approach.

**require** (fields) thetaLevels <- **c** ("low", "med", "hi") n <- **c** (10, 100, 1000) tVsNorm <- **c** ("t", "norm") levels <- **expand.grid** (thetaLevels, tVsNorm, n) _## example of replicate() -- generate m sets correlated normals_ **set.seed** (0) genFun <- **function** (n, theta = 1){ u <- **rnorm** (n) x <- **runif** (n) Cov <- **exp** (- **rdist** (x)/theta) U <- **chol** (Cov) **return** ( **cbind** (x, **crossprod** (U, u))) } m <- 20 simData <- **replicate** (m, **genFun** (100, 1)) **dim** (simData) _# 100 observations by {x, y} values by 20 replicates_ ## [1] 100 2 20

### **5.2 Analysis and reporting**

Often results are reported simply in tables, but it can be helpful to think through whether a graphical representation is more informative (sometimes it’s not or it’s worse, but in some cases it may be much better).

You should set the seed when you start the experiment, so that it’s possible to replicate it. It’s also a good idea to save the current value of the seed whenever you save interim results, so that you can restart simulations (this is particularly helpful for MCMC) at the exact point you left off, including the random number sequence.

To enhance reproducibility, it’s good practice to post your simulation code (and potentially

17

data) on your website or as supplementary material with the journal. One should report sample sizes and information about the random number generator.

Here are JASA’s requirements on documenting computations:

“Results Based on Computation - Papers reporting results based on computation should provide enough information so that readers can evaluate the quality of the results. Such information includes estimated accuracy of results, as well as descriptions of pseudorandom-number generators, numerical algorithms, computers, programming languages, and major software components that were used.”

18

---

[← 4 Design of simulation studies](05-4-design-of-simulation-studies.md) · [Up: contents](index.md)
