---
title: 1 Efficiency
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Efficiency

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In general, make use of R’s built-in functions, as these tend to be implemented internally (i.e., via compiled code in C or Fortran). In particular, if R is linked to optimized BLAS and Lapack code (e.g. Intel’s _MKL_ , _OpenBLAS_ [on the SCF Linux servers], AMD’s _ACML_ [on the SCF Linux cluster, _vecLib_ for Macs [on the SCF Macs]), you should have good performance (potentially comparable to Matlab and to coding in C). Sometimes you can figure out a trick to take your problem and transform it to make use of the built-in functions.

Note that I run a lot of MCMCs so I pay attention to making sure my calculations are fast as they are done repeatedly. Similarly, one would want to pay attention to speed when doing large simulations and bootstrapping, and in some cases for optimization. And if you’re distributing code, it’s good to have it be efficient. But in other contexts, it may not be worth your time. Also, it’s good practice to code it transparently first to reduce bugs and then to use tricks to speed it up and make sure the fast version works correctly.

Results can vary with with your system setup and version of R, so the best thing to do is figure out where the bottlenecks are in your code (e.g., with _Rprof()_ or just some basic use of _system.time()_ and _benchmark()_ ), and then play around with alternative specifications. And as you gain more experience, you’ll get some intuition for what approaches might improve speed, but

1

even with experience I find myself often surprised by what matters and what doesn’t. It’s often worth trying out a bunch of different ideas; _system.time()_ and _benchmark()_ are your workhorse tools in this context.

First, let’s see some tools for assessing the speed of your code.

### **1.1 Tools for assessing efficiency**

#### **1.1.1 Benchmarking**

_system.time()_ is very handy for comparing the speed of different implementations.

n <- 1000 x <- **matrix** ( **rnorm** (n^2), n) **system.time** ({ mns <- **rep** (NA, n) **for** (i **in** 1:n) mns[i] <- **mean** (x[i, ]) }) ## user system elapsed ## 0.032 0.000 0.034 **system.time** ( **rowMeans** (x)) ## user system elapsed ## 0.000 0.000 0.003

The _rbenchmark_ package provides a nice wrapper function, _benchmark()_ , that automates speed assessments.

**library** (rbenchmark) _# speed of one calculation_ n <- 1000 x <- **matrix** ( **rnorm** (n^2), n) **benchmark** ( **crossprod** (x), replications = 10, columns = **c** ("test", "elapsed", ## test elapsed replications ## 1 crossprod(x) 0.577 10 _# comparing different approaches to a task_

2

**benchmark** ({ mns <- **rep** (NA, n) **for** (i **in** 1:n) mns[i] <- **mean** (x[i, ]) }, **rowMeans** (x), replications = 10, columns = **c** ("test", "elapsed", "replications" ## test ## 1 {\n mns <- rep(NA, n)\n for (i in 1:n) mns[i] <- mean(x[i, ])\n} ## 2 rowMeans(x) ## elapsed replications ## 1 0.280 10 ## 2 0.032 10

#### **1.1.2 Profiling**

The _Rprof()_ function will show you how much time is spent in different functions, which can help you pinpoint bottlenecks in your code.

Here’s a function that works with a correlation matrix such as one might have for time series data.

makeTS <- **function** (param, len) { times <- **seq** (0, 1, length = len) dd <- **rdist** (times) C <- **exp** (-dd/param) U <- **chol** (C) white <- **rnorm** (len) **return** ( **crossprod** (U, white)) }

**library** (fields) **Rprof** ("makeTS.prof") out <- **makeTS** (0.1, 1000) **Rprof** ( **NULL** ) **summaryRprof** ("makeTS.prof")

Here’s the result for the _makeTS()_ function from the demo code file:

3

|$by.self<br>self.time|self.pct|total.time|total.pct||
|---|---|---|---|---|
|".Call"<br>0.38|48.72|0.38|48.72||
|".Fortran"<br>0.22|28.21|0.22|28.21||
|"matrix"<br>0.08|10.26|0.30|38.46||
|"exp"<br>0.08|10.26|0.08|10.26||
|"/"<br>0.02|2.56|0.02|2.56||
|$by.total<br>tot|al.time|total.pct se|lf.time se|lf.pct|
|"makeTS"|0.78|100.00|0.00|0.00|
|".Call"|0.38|48.72|0.38|48.72|
|"chol.default"|0.38|48.72|0.00|0.00|
|"chol"|0.38|48.72|0.00|0.00|
|"standardGeneric"|0.38|48.72|0.00|0.00|
|"matrix"|0.30|38.46|0.08|10.26|
|"rdist"|0.30|38.46|0.00|0.00|
|".Fortran"|0.22|28.21|0.22|28.21|
|"exp"|0.08|10.26|0.08|10.26|
|"/"|0.02|2.56|0.02|2.56|
|$sample.interval [1]|0.02||||


$sampling.time [1] 0.78

_Rprof()_ tells how much time was spent in each function alone (the _“self”_ columns) and aggregating the time spent in a function and all of the functions that it calls (the _“total”_ columns). Usually the former is going to be more useful, but in some cases we need to decipher what is going on based on the latter.

Let’s figure out what is going on here. The self time tells us that _.Call_ (a call to C code), _.Fortran_ (a call to Fortran code) and _matrix()_ take up most of the time. Looking at the total time and seeing in _chol.default()_ that _.Call_ is used (you would have to go in and look at the _La_chol()_ function to figure this out) and in _rdist()_ that _.Fortran()_ and _matrix()_ are used we can infer that about 49% of the time is being spent in the Cholesky and 38% in the _rdist()_ calculation, with 10% in _exp()_ . As we increase the number of time points, the time taken up by the Cholesky would increase since that calculation is order of _n_<sup>3</sup> while the others are order _n_<sup>2</sup> (more in the linear algebra unit).

Apparently there is a memory profiler in R, _Rprofmem()_ , but it needs to be enabled when R is compiled (i.e., installed on the machine), because it slows R down even when not used. So I’ve never gotten to the point of playing around with it.

**Warning** : _Rprof()_ conflicts with threaded linear algebra, so you will need to set OMP_NUM_THREADS to 1 to disable threaded linear algebra if you profile code that involves linear algebra. More about this in the unit on parallel processing.

4

### **1.2 Strategies for improving efficiency**

#### **1.2.1 Fast initialization**

It is very inefficient to iteratively add elements to a vector, matrix, data frame, array or list (e.g., iteratively using _c()_ , _cbind()_ , _rbind()_ , etc.). Instead, create the full object in advance (this is equivalent to variable initialization in compiled languages) and then fill in the appropriate elements. The reason is that when R appends to an existing object, it creates a new copy and as the object gets big, this gets slow when one does it a lot of times. Here’s an illustrative example, but of course we would not fill a vector like this because we would in practice use vectorized calculations.

n <- 1000 fun1 <- **function** (n) { x <- 1 **for** (i **in** 2:n) x <- **c** (x, i) **return** (x) } fun2 <- **function** (n) { x <- **rep** ( **as.numeric** (NA), n) **for** (i **in** 1:n) x[i] <- i } **benchmark** ( **fun1** (n), **fun2** (n), replications = 10, columns = **c** ("test", "elapsed" "replications")) ## test elapsed replications ## 1 fun1(n) 0.017 10 ## 2 fun2(n) 0.012 10

It’s not necessary to use _as.numeric()_ above though it saves a bit of time. **Challenge** : figure out why I have as.numeric(NA) and not just NA.

We can actually speed up the initialization (though in most practical circumstances, the second approach here would be overkill):

n <- 1e+06 **benchmark** (x <- **rep** ( **as.numeric** (NA), n), { x <- **as.numeric** (NA) **length** (x) <- n }, replications = 10, columns = **c** ("test", "elapsed", "replications"))

5

|##||test|elapsed|rep|lications|
|---|---|---|---|---|---|
|## 2 {\n|x <- as.numeric(NA)\n|length(x) <- n\n}|0.018||10|
|## 1|x <- rep|(as.numeric(NA), n)|0.090||10|


For matrices, start with the right length vector and then change the dimensions

nr <- nc <- 2000 **benchmark** (x <- **matrix** ( **as.numeric** (NA), nr, nc), { x <- **as.numeric** (NA) **length** (x) <- nr * nc **dim** (x) <- **c** (nr, nc) }, replications = 10, columns = **c** ("test", "elapsed", "replications")) ## ## 2 {\n x <- as.numeric(NA)\n length(x) <- nr * nc\n dim(x) <- c(nr, ## 1 x <- matrix(as.numeric(NA), ## elapsed replications ## 2 0.062 10 ## 1 0.485 10

For lists, we can do this

<mark>myList <-</mark> **<mark>vector</mark>** <mark>("list", length = n)</mark>

#### **1.2.2 Vectorized calculations**

One key way to write efficient R code is to take advantage of R’s vectorized operations.

n <- 1e+06 x <- **rnorm** (n) **system.time** (x2 <- x^2) ## user system elapsed ## 0.000 0.000 0.002 x2 <- **as.numeric** (NA) **system.time** ({ **length** (x2) <- n

6

**for** (i **in** 1:n) { x2[i] <- x[i]^2 } }) _# how many orders of magnitude slower?_ ## user system elapsed ## 2.304 0.000 2.317

So what is different in how R handles the calculations above that explains the disparity? The vectorized calculation is being done natively in C in a for loop. The for loop above involves executing the for loop in R (involving a bunch of overhead because R is an interpreted language) with repeated calls to C code at each iteration. You can usually get a sense for how quickly an R call will pass things along to C by looking at the body of the relevant function(s) being called and looking for _.Primitive_ , _.Internal_ , _.C, .Call_ , or _.Fortran_ . Let’s take a look at the code for ‘ _+_ ‘, _mean.default()_ , and _chol.default()_ .

Many R functions allow you to pass in vectors, and operate on those vectors in vectorized fashion. So before writing a for loop, look at the help information on the relevant function(s) to see if they operate in a vectorized fashion.

line <- **c** ("Four score and 7 years ago, this nation") startIndices = **seq** (1, by = 3, length = **nchar** (line)/3) **substring** (line, startIndices, startIndices + 1) ## [1] "Fo" "r " "co" "e " "nd" "7 " "ea" "s " "go" " t" "is" "na" "io"

**Challenge** : Consider the chi-squared statistic involved in a test of independence in a contingency table:


where _fi·_ =<sup>�</sup> _j_<sup>_f_</sup> _ij_<sup>.Writethisinavectorizedwaywithoutanyloops.Notethat’vectorized’</sup> calculations also work with matrices and arrays.

Vectorized operations can also be faster than built-in functions, and clever vectorized calculations even better, though sometimes the code is uglier:

x <- **rnorm** (1e+06)

**benchmark** (truncx <- **ifelse** (x > 0, x, 0), { truncx <- x

7

truncx[x < 0] <- 0

}, truncx <- x * (x > 0), replications = 10, columns = **c** ("test", "elapsed", "replications"))

|##|||test|elapsed|rep|lications|
|---|---|---|---|---|---|---|
|##|1|truncx|<- ifelse(x > 0, x, 0)|3.502||10|
|##|2 {\n|truncx <- x\n|truncx[x < 0] <- 0\n}|0.405||10|
|##|3||truncx <- x * (x > 0)|0.127||10|


The demo code (see also Section 4.2 of Unit 4) has a surprising example where combining vectorized calculations with a _for_ loop is actually faster than using _apply()_ . The goal is to remove rows of a large matrix that have any NAs in them.

Additional tips:

- If you do need to loop over dimensions of a matrix or array, if possible loop over the smallest dimension and use the vectorized calculation on the larger dimension(s).

- Looping over columns is likely to be faster than looping over rows given column-major ordering.

- You can use direct arithmetic operations to add/subtract/multiply/divide a vector by each column of a matrix, e.g. A*b, multiplies each column of _A_ times a vector _b_ . If you need to operate by row, you can do it by transposing the matrix.

Caution: relying on R’s recycling rule in the context of vectorized operations, such as is done when direct-multiplying a matrix by a vector to scale the rows, can be dangerous as the code is not transparent and poses greater dangers of bugs. If it’s needed to speed up a calculation, the best approach is to (1) first write the code transparently and then compare the efficient code to make sure the results are the same and (2) comment your code.

Question: What do the points above imply about how to choose to store values in a matrix? How would you choose what should be the row dimension and what should be the column dimension?

#### **1.2.3 Using** **_apply()_ and specialized functions**

Another core efficiency strategy is to use the _apply()_ functionality. Even better than _apply()_ for calculating sums or means of columns or rows (it also can be used for arrays) is _{row,col}{Sums,Means}_ :

8

n <- 3000 x <- **matrix** ( **rnorm** (n * n), nr = n) **system.time** (out <- **apply** (x, 1, mean)) ## user system elapsed ## 0.308 0.020 0.332 **system.time** (out <- **rowMeans** (x)) ## user system elapsed ## 0.024 0.000 0.025

We can ’ _sweep_ ’ out a summary statistic, such as subtracting off a mean from each column, using _sweep()_

**system.time** (out <- **sweep** (x, 2, STATS = **colMeans** (x), FUN = "-")) ## user system elapsed ## 0.549 0.084 0.633

Here’s a trick for doing it based on vectorized calculations, remembering that if we subtract a vector from a matrix, it subtracts each element of the vector from all the elements in the corresponding ROW.

**system.time** (out2 <- **t** ( **t** (x) - **colMeans** (x))) ## user system elapsed ## 0.332 0.072 0.406 **identical** (out, out2) ## [1] TRUE

As I mentioned in Unit 4, using versions of _apply()_ with lists may or may not be faster than looping but generally produces cleaner code. Whether looping is slower will depend on whether a substantial part of the work is in the overhead of the looping or in the time required by the function evaluation on each of the elements. If you’re worried about speed, it’s a good idea to benchmark the _apply()_ variant against looping.

9

#### **1.2.4 Matrix algebra efficiency**

Often calculations that are not explictly linear algebra calculations can be done as matrix algebra. The following can be done faster with _rowSums()_ , so it’s not a great example, but this sort of trick does come in handy in surprising places.

mat <- **matrix** ( **rnorm** (500 * 500), 500) **benchmark** ( **apply** (mat, 1, sum), mat %*% **rep** (1, **ncol** (mat)), **rowSums** (mat), columns = **c** ("test", "elapsed", "replications"))

---

[Up: contents](index.md) · [Unit 06 — Rprog Part 02 — →](02-unit-06-rprog-part-02.md)
