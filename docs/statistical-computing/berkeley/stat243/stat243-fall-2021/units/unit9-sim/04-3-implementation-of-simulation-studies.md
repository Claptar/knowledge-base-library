---
title: 3 Implementation of simulation studies
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit9-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit9-sim.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit9-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit9-sim.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Implementation of simulation studies

Luke Miratrix (a UCB Stats PhD alum) has prepared a nice tutorial on carrying out a simulation study, including helpful R code. So if the discussion here is not concrete enough or you want to see how to effectively implement such a study, see *simulation_tutorial_miratrix.pdf* and the similarly named R code file.

## 3.1 Computational efficiency

Parallel processing is often helpful for simulation studies. The reason is that simulation studies are embarrassingly parallel - we can send each replicate to a different computer processor and then collect the results back, and the speedup should scale directly with the number of processors we used. Since we often need to some sort of looping, writing code in C/C++ and compiling and linking to the code from R may also be a good strategy, albeit one not covered in this course.

Handy functions in R include `expand.grid()` to get all combinations of a set of vectors and the `replicate()` function in R, which will carry out the same R expression (often a function call) repeated times. This can replace the use of a for loop with some gains in cleanliness of your code. Storing results in an array is a natural approach.

```r
require(fields)
thetaLevels <- c("low", "med", "hi")
n <- c(10, 100, 1000)
tVsNorm <- c("t", "norm")
levels <- expand.grid(thetaLevels, tVsNorm, n)
## example of replicate() -- generate m sets correlated normals
set.seed(1)
genFun <- function(n, theta = 1){
  u <- rnorm(n)
  x <- runif(n)
  Cov <- exp(-rdist(x)/theta)
  U <- chol(Cov)
  return(cbind(x,crossprod(U, u)))
}
m <- 20
simData <- replicate(m, genFun(100, 1))
dim(simData) # 100 observations by {x, y} values by 20 replicates
## [1] 100   2  20
```

## 3.2 Analysis and reporting

Often results are reported simply in tables, but it can be helpful to think through whether a graphical representation is more informative (sometimes it's not or it's worse, but in some cases it may be much better). Since you'll often have a variety of scenarios to display, using trellis plots in ggplot2 via the `facet_wrap` function will often be a good approach to display how results vary as a function of multiple inputs.

You should set the seed when you start the experiment, so that it's possible to replicate it. It's also a good idea to save the current value of the seed whenever you save interim results, so that you can restart simulations (this is particularly helpful for MCMC) at the exact point you left off, including the random number sequence.

To enhance reproducibility, it's good practice to post your simulation code (and potentially simulated data) on GitHub, on your website, or as supplementary material with the journal. Another person should be able to fully reproduce your results, including the exact random number generation that you did (e.g., you should provide code for how you set the random seed for your randon number generator).

Many journals are requiring increasingly detailed documentation of the code and data used in your work, including code and data for simulations. Here are the American Statistical Association's requirements on documenting computations in its journals:

> "The ASA strongly encourages authors to submit datasets, code, other programs, and/or extended appendices that are directly relevant to their submitted articles. These materials are valuable to users of the ASA's journals and further the profession's commitment to reproducible research. Whenever a dataset is used, its source should be fully documented and the data should be made available as on online supplement. Exceptions for reasons of security or confidentiality may be granted by the Editor. Whenever specific code has been used to implement or illustrate the results of a paper, that code should be made available if possible. [....snip....] Articles reporting results based on computation should provide enough information so that readers can evaluate the quality of the results. Such information includes estimated accuracy of results, as well as descriptions of pseudorandom-number generators, numerical algorithms, programming languages, and major software components used."

---

[← 2 Design of simulation studies](03-2-design-of-simulation-studies.md) · [Up: contents](index.md) · [4 Random number generation (RNG) →](05-4-random-number-generation-rng.md)
