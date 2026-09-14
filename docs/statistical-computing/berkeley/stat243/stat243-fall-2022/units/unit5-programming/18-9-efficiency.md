---
title: 9. Efficiency
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 9. Efficiency

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Interpreters and compilation

### Why are interpreted languages slow?

Compiled code runs quickly because the original code has been translated into instructions (machine language) that the processor can understand (i.e., zeros and ones). In the process of doing so, various checking and lookup steps are done once and don't need to be redone when running the compiled code.

In contrast, when one runs code in an interpreted language such as R or Python, the interpreter needs to do all the checking and lookup each time the code is run. This is required because the types and locations in memory of the variables could have changed.

We'll focus on R in the following discussion, but most of the concepts apply to other interpreted languages (that said, R is particularly dynamic as illustrated below in Section 10 of this Unit).

For example, consider this code:

```r
x <- 3
x*7
x <- 'hi'
x*3
```

Because of dynamic typing, when the interpreter sees `x*3` it needs to check if `x` is something that can be multiplied by 3, including dealing with the fact that `x` could be a vector with many numbers in it. In addition it needs to (using scoping rules) look up the value of `x`. (Consider that `x` might not even exist at the point that `x*3` is called.) Only then can the multiplication happen.

Let's consider writing a loop:

```r
for(i in 1:10) {
  if(runif(1) > 0) x <- 'hi'
  if(runif(1) > 0.5) rm(x)
  x[i] <- exp(x[i])
}
```

There is no way around the fact that because of how dynamic this is, the interpreter needs to check if `x` exists, if it is a vector of sufficient length, if it contains numeric values, and it needs to go retrieve the required value, EVERY TIME the `exp()` is executed. Now the code above is unusual, and in most cases, we wouldn't have the if() statements that modify `x`. So you could imagine a process by which the checking were done on the first iteration and then not needed after that -- that gets into the idea of just-in-time compilation, discussed later.

The R interpreter is a C function so in some sense everything that happens is running as compiled code, but there are lots more things being done to accomplish a given task using interpreted code than if the task had been written directly in code that is compiled. By analogy, consider talking directly to a person in a language you both know compared to talking to a person via an interpreter who has to translate between two languages. Ultimately, the same information gets communicated (hopefully!) but the number of words spoken and time involved is much greater.

When running more complicated functions, there is often a lot of checking that is part of the function itself.
For example, consider all the checking in the `lm` function before it gets to calling `lm.fit()` to do the
actual linear algebra needed to produce the least squares solution. Or consider the checking involved in `mean.default`
before it finally calls R's internal `mean` function, which runs compiled C code.
Hadley Wickham's Advanced R book has a [section on performance](https://adv-r.hadley.nz/perf-improve.html) that discusses this in detail.

We can flip the question on its head and ask what operations in an interpreted language will execute quickly. In R, these include:

- operations that call out to compiled C code via `.Primitive()` or `.Internal()`
- linear algebra operations (these call out to compiled C or Fortran code provided by the BLAS and LAPACK software packages)
- vectorized calls rather than loops in R
   - vectorized calls generally run loops in compiled C code rather than having the loop run in R
   - that means that the interpreter doesn't have to do all the checking discussed above for every iteration of the loop


### Compilation

#### Overview

Compilation is the process of turning code in a given language (such a C++) into machine code. Machine code is the code that the processor actually executes. The machine code is stored in the executable file, which is a binary file. The history of programming has seen ever great levels of abstraction, so that humans can write code using syntax that is easier for us to understand, re-use, and develop building blocks that can be put together to do complicated tasks. For example assembly language is a step above machine code. Languages like C and Fortran provide additional abstraction beyond that. The Stastics 750 class at CMU has a [nice overview](https://36-750.github.io/tools/computer-architecture/#how-programs--aka-apps--run) if you want to see more details.

Note that interpreters such as R are themselves programs -- the R interpreter is a C program that has been compiled. It happens to be a program that processes R code. The interpreter doesn't turn R code into machine code, but the interpreter itself is machine code.

#### Just-in-time (JIT) compilation

Standard compilation (ahead-of-time or AOT compilation) happens before any code is executed and can involve a lot of optimization to produce the most efficient machine code possible.

In contrast, just-in-time (JIT) compilation happens at the time that the code is executing. JIT compilation is heavily used in Julia, which is very fast (in some cases as fast as C). JIT compilation involves translating to machine code as the code is running. One nice aspect is that the results are cached so that if code is rerun, the compilation process doesn't have to be redone. So if you use a language like Julia, you'll see that the speed can vary drastically between the first time and later times you run a given function during a given session.

One thing that needs to be dealt with is type checking. As discussed above, part of why an interpreter is slow is because the type of the variable(s) involved in execution of a piece of code is not known in advance, so the interpreter needs to check the type. In JIT systems, there are often type inference systems that determine variable types.

JIT compilation can involve translation from the original code to machine code or translation of bytecode (see next section) to machine code.

#### Byte compiling (optional)

Functions in R and R packages are byte compiled. What does that mean?
Byte-compiled code is a special representation that can be
executed more efficiently because it is in the form of compact codes
that encode the results of parsing and semantic analysis of scoping and
other complexities of the R source code. This byte code can be executed
faster than the original R code because it skips the stage of having to
be interpreted by the R interpreter.

If you print out a function that is byte-compiled, you'll
see something like `<bytecode: 0x243a368>` at the bottom.

```r
mean
```

We can byte compile our own functions using `cmpfun()`. Here's an
example (silly since as experienced R programmers, we would use
vectorized calculation here rather than this unvectorized code.)

```r
library(compiler); library(rbenchmark)
f <- function(vals){
    x <- as.numeric(NA)
    length(x) <- length(vals)
    for(i in seq_along(vals)) x[i] <- exp(vals[i])
    return(x)
}
fc <- cmpfun(f)
fc # notice the indication that the function is byte compiled.
x <- rnorm(100000)
benchmark(f(x), fc(x), y <- exp(x), replications = 5)
```

Unfortunately, in my experience (as illustrated above), byte compiling doesn't usually speed
things up much. I'm not sure why.

You can compile an entire source file with `cmpfile()`, which produces a
`.Rc` file. You then need to use `loadcmp()` to load in the `.Rc` file,
which runs the code.


## Benchmarking and profiling

The [efficient R tutorial](https://berkeley-scf.github.io/tutorial-efficient-R/timing) discusses strategies for timing and profiling R code.

Recall that it's a waste of time to optimize code before you determine  (1) that the code is too slow for how it will be used and (2) which are the slow steps on which to focus your attempts to speed the code up. A 100x speedup in a step that takes 1% of the time will speed up the overall code by very little.

## Writing efficient R code

The [efficient R tutorial](https://berkeley-scf.github.io/tutorial-efficient-R/efficiency) discusses strategies for improving the efficiency of R code. We'll discuss a variety of these strategies, including:

- Pre-allocating memory rather than growing objects iteratively
- Vectorization and use of fast matrix algebra
- Consideration of loops vs. map operations
- Speed of lookup operations, including hashing
- Effectively using the CPU cache

## Hashing (including name lookup)

In the tutorial on efficient R coding, it mentions that looking up objects
by name in an R environment occurs via hashing, so it is very fast.
I'll briefly describe what hashing is here, because it is a commonly-used
strategy in programming in general.

A hash function is a function that takes as input some data and maps it
to a fixed-length output that can be used as a shortened reference to
the data. (The function should be deterministic, always returing the same
output for a given input.) We've seen this in the context of git commits where each
commit was labeled with a long base-16 number. This also comes up when
verifying files on the Internet. You can compute the hash value on the
file you get and check that it is the same as the hash value associated
with the legitimate copy of the file.

While there are various uses of hashing, for our purposes here, hashing can allow one to look up values by their
name via a hash table. The idea is that you have a set of key-value
pairs (sometimes called a dictionary) where the key is the name
associated with the value and the value is some arbitrary object.
You want to be able to quickly find the value/object quickly.

Hashing allows one to quickly determine an index associated with the key
and therefore quickly find the relevant value based on the index. For
example, one approach is to compute the hash as a function of the key
and then take the remainder when dividing by the number of possible results
(here the fact that the result is a fixed-length output is important) to get the index.
Here's the procedure in pseudocode:

```
    hash = hashfunc(key)
    index = hash %% array_size
    ## %% is modulo operator - it gives the remainder
```

In general, there will be collisions -- multiple keys will be assigned to the
same index. However with a good hash function, usually there will be a small number of keys associated
with a given bucket. So each bucket will contain a list of a small number of values and the associated keys.
(The buckets might contain the actual values or they might contain the addresses of where the values are actually stored
if the values are complicated objects.) Then determining the correct value (or the required address) within
a given bucket is fast even with simple linear search through the items one by one.
Put another way, the
hash function distributes the keys amongst an array of buckets and
allows one to look up the appropriate bucket quickly based on the
computed index value. When the hash table is properly set up, the cost
of looking up a value does not depend on the number of key-value pairs
stored.

R uses hashing to look up the value of a variable based on the variable name in a given environment, including the frames of functions and the global environment. This allows R to retrieve objects very quickly.

## Efficiency challenges

We'll work on some of these challenges in class. In addition, one or
more of these challenges will appear on PS4.

Some things to think about in trying to write more efficient code (or improve the efficiency of existing code) in R and more generally include:

  - avoid repeated calculations, particularly in a loop
     - save (i.e., cache) the result in an object
     - move repeated calculations outside of loops
        - watch out for calculations in a loop that don't involve all the indices of the loop(s)
  - avoid entirely unneeded calculations
     - e.g., consider `diag(X%*%Y)`
  - avoid calculations where you know the answer
     - e.g., any part of a computation where you multiply by or add zero or multiply by one
  - use vectorization in interpreted languages
  - consider the order of operations
  - combine operations when possible (e.g., use of `crossprod`)


**Challenge 1**: Here's a calculation of the sort needed in mixture
component modeling. I have a vector of $n$ observations. I need to find
the likelihood of each observation under each of $p$ mixture components
(i.e., what's the likelihood if it came from each of the components).
(In this case, the the likelihood is simply the normal density of the
observation given the mean and standard deviation of the component
normal distribution.) So I should produce a matrix of $n$ rows and $p$
columns where the value in the $i$th row, $j$th column is the likelihood
of the $i$th observation under the $j$th mixture component. The idea is
that the likelihoods for a given observation are used in assigning
observations to clusters. A naive implementation is:

```r
lik <- matrix(as.numeric(NA), nr = n, nc = p)
for(j in 1:p) lik[ , j] <- dnorm(y, mns[j], sds[j])
```

Note that `dnorm()` can handle matrices and vectors as the observations
**and** as the means and sds, so there are multiple ways to do this. Try
to figure out the fastest way to do this, amongst the options of looping
over the mixture components, looping over the observations, using
vectorized operations that recycle the observations, using vectorized
operations that recycle the mixture components, etc.

**Challenge 2**: Here's a calculation of the sort needed in a mixed
membership model, where each observation is associated with some number
of components. Suppose you have
$$y_{i}\sim\mathcal{N}(\sum_{j=1}^{m_{i}}w_{i,j}\mu_{ID[i,j]},\sigma^{2})$$
for a large number of observations, $n$. I give you a vector of
$\mu=(\mu_{1},\ldots,\mu_{K})$ values and a ragged list of weights
(i.e., the number of weights varies by observation) and a ragged list of
IDs identifying the cluster corresponding to each weight (note $m_{i}$
varies by observation). Figure out how to calculate the vector of means,
$\sum_{j}w_{i,j}\mu_{ID[i,j]}$ as fast as possible. Suppose that $m_{i}$
never gets too big (but $\mu$ might have many elements) - could this
help you? Part of thinking this through involves thinking about how you
want to store the information so that the calculations can be done
quickly. The data file `mixedMember.Rda` contains example data for two
scenarios: Scenario A has many $\mu$ values and Scenario B has few $\mu$
values.

**Challenge 3**: Write code that simulates a random walk in two
dimensions for $n$ steps. First write out a straightforward
implementation that involves looping. Then try to speed it up. The
`cumsum` function may be helpful.

**Challenge 4:** Determine if it's faster to subset based on vector of
indices or a vector of logicals. Determine if it matters how big the
original object is and how large the subset is, as well as whether the
vector of indices is ordered.

**Challenge 5:** Figure out how to improve the efficiency of the
following code chunk, which is part of an iterative optimization of a
log-likelihood for a student's PhD research. Some test data is in
`likLoops.Rda`.

```r
ll <- function(Theta, A) {
  sum.ind <- which(A==1, arr.ind=T)
  logLik <- sum(log(Theta[sum.ind])) - sum(Theta)
  return(logLik)
}

oneUpdate <- function(A, n, K, theta.old, thresh = 0.1) {
  theta.old1 <- theta.old
  Theta.old <- theta.old %*% t(theta.old)
  L.old <- ll(Theta.old, A)
  q <- array(0, dim = c(n, n, K))

  for (i in 1:n) {
    for (j in 1:n) {
      for (z in 1:K) {
        if (theta.old[i, z]*theta.old[j, z] == 0){
          q[i, j, z] <- 0
        } else {
          q[i, j, z] <- theta.old[i, z]*theta.old[j, z] /
            Theta.old[i, j]
        }
      }
    }
  }
  theta.new <- theta.old
  for (z in 1:K) {
    theta.new[,z] <- rowSums(A*q[,,z])/sqrt(sum(A*q[,,z]))
  }
  Theta.new <- theta.new %*% t(theta.new)
  L.new <- ll(Theta.new, A)
      converge.check <- abs(L.new - L.old) < thresh
  theta.new <- theta.new/rowSums(theta.new)
  return(list(theta = theta.new, loglik = L.new,
              converged = converge.check))
}

---

[← 8. Memory and copies](17-8-memory-and-copies.md) · [Up: contents](index.md) · [initialize the parameters at random starting values →](19-initialize-the-parameters-at-random-starting-values.md)
