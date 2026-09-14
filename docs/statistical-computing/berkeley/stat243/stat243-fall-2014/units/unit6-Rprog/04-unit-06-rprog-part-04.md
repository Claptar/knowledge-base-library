---
title: Unit 06 — Rprog Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 04 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|**be**|**nchmark**(x[5e+05], xL|[[5e+05]], x|Env[["50|0000"]],|xEnv$"50000|0", replicatio|
|---|---|---|---|---|---|---|
|##|test|replications|elapsed|relative|user.self|sys.self|
|##|1<br>x[5e+05]|10000|0.040|1.333|0.036|0.004|
|##|3 xEnv[["500000"]]|10000|0.042|1.400|0.044|0.000|
|##|4<br>xEnv$"500000"|10000|0.046|1.533|0.044|0.000|
|##|2<br>xL[[5e+05]]|10000|0.030|1.000|0.028|0.000|
|##|user.child sys.ch|ild|||||
|##|1<br>0|0|||||
|##|3<br>0|0|||||
|##|4<br>0|0|||||
|##|2<br>0|0|||||


13

#### **1.2.6 pqR and other R engines**

Radford Neal, a prominent statistician/computer scientist has been working on a project called _pqR_ (pretty quick R) to rewrite some aspects of R to make them faster. There are also a few other projects that aim to reimplement the “R engine” such that one could run one’s R code with different back ends.

Here are some of the highlights of _pqR_ in terms of efficiency, as discussed at http://radfordneal.github.io/pqR/:

1. When R runs code such as just below, it actually creates a vector 1,2,....,n, (which can be computationally and memory intensive for large n) and then iterates over the values in the vector. pqR avoids this vector creation.

for(i in 1:n) { } vec[1:n]

2. As we’ll see in Section 3.5, R often avoids making copies of objects when it is not necessary. However, the scheme used to do this can be improved so that even fewer copies are made.

3. pqR automatically uses multiple cores for some calculations.

4. pqR avoid some checks for NA and NaN and the like in matrix calculations in which such checking would be slow and it doesn’t make sense to check for them anyway.

#### **1.2.7 Byte compiling**

R now allows you to compile R code, which goes by the name of byte compiling. Byte-compiled code is a special representation that can be executed more efficiently because it is in the form of compact codes that encode the results of parsing and semantic analysis of scoping and other complexities of the R source code. This byte code can be executed faster than the original R code because it skips the stage of having to be interpreted by the R interpreter.

The functions in the _base_ and _stats_ packages are now byte-compiled by default. (If you print out a function that is byte-compiled, you’ll see something like _<bytecode: 0x243a368>_ at the bottom.

We can byte compile our own functions using _cmpfun()_ . Here’s an example (silly since we we actually do this calculation using vectorized operations):

**library** (compiler) **library** (rbenchmark) f <- **function** (x) { **for** (i **in** 1: **length** (x)) x[i] <- x[i] + 1

14

**return** (x) } fc <- **cmpfun** (f) fc _# notice the indication that the function is byte compiled._ ## function(x) { ## for (i in 1:length(x)) x[i] <- x[i] + 1 ## return(x) ## } ## <bytecode: 0x2490a788> x <- **rnorm** (1e+05) **benchmark** ( **f** (x), **fc** (x), x <- x + 1, replications = 5) ## test replications elapsed relative user.self sys.self user.child ## 2 fc(x) 5 0.173 86.5 0.176 0.00 0 ## 1 f(x) 5 11.620 5810.0 11.549 0.02 0 ## 3 x <- x + 1 5 0.002 1.0 0.004 0.00 0 ## sys.child ## 2 0 ## 1 0 ## 3 0

You can compile an entire source file with _cmpfile()_ , which produces a _.Rc_ file. You then need to use _loadcmp()_ to load in the _.Rc_ file, which runs the code.

Unfortunately, in my experience, byte compiling doesn’t usually speed things up much. As experienced R programmers we would never write the unvectorized code above.

### **1.3 Challenges**

One or more of these challenges may appear on a problem set.

**Challenge 1** : Here’s a calculation of the sort needed in mixture component modeling. I have a vector of _n_ observations. I need to find the likelihood of each observation under each of _p_ mixture components (i.e., what’s the likelihood if it came from each of the components). So I should produce a matrix of _n_ rows and _p_ columns where the value in the _i_ th row, _j_ th column is the likelihood of the _i_ th observation under the _j_ th mixture component. The idea is that the likelihoods for a given observation are used in assigning observations to clusters. A naive implementation is:

15

«chunk14aa, eval=FALSE» lik <- matrix(NA, nr = n, nc = p) for(j in 1:p) lik[ , j] <- dnorm(y, mns[j], sds[j]) @

Note that _dnorm()_ can handle matrices and vectors as the observations **and** as the means and sds, so there are multiple ways to do this.

**Challenge 2** : Here’s a calculation of the sort needed in a mixed membership model, where each observation is associated with some number of components. Suppose you have _yi ∼N_ (<sup>�</sup><sup>_m_</sup> _k_ =1<sup>_iwi,kµID_[</sup><sup>_i,k_]</sup><sup>_, σ_2)</sup> for a large number of observations, _n_ . I give you a vector of _µ_ values and a ragged list of weights and a ragged list of IDs identifying the cluster corresponding to each weight (note _mi_ varies by observation). Figure out how to calculate the vector of means,<sup>�</sup> _k_<sup>_w_</sup> _i,k_<sup>_µ_</sup> _ID_ [ _i,k_ ]<sup>as fast as possible.</sup> Suppose that _mi_ never gets too big (but _µ_ might have many elements) - could this help you? Part of thinking this through involves thinking about how you want to store the information so that the calculations can be done quickly.

**Challenge 3** : Write code that simulates a random walk in two dimensions for _n_ steps. First write out a straightforward implementation that involves looping. Then try to speed it up. The _cumsum()_ function may be helpful.

**Challenge 4:** Determine if it’s faster to subset based on vector of indices or a vector of logicals. Determine if it matters how big the original object is and how large the subset is, as well as whether the vector of indices is ordered.

**Challenge 5:** Figure out how to efficiency improvements in the following code chunk, which is part of a likelihood calculation for a student’s PhD research.

**for** (i **in** 1:n) { **for** (j **in** 1:n) { **for** (z **in** 1:K) { **if** (theta.old[i, z] * theta.old[j, z] == 0) { q[i, j, z] <- 0 } **else** { q[i, j, z] <- theta.old[i, z] * theta.old[j, z]/Theta.old[i, j] } } } } theta.new <- theta.old **for** (z **in** 1:K) { theta.new[, z] <- **rowSums** (A * q[, , z])/ **sqrt** ( **sum** (A * q[, , z]))

16

<mark>}</mark>

---

[← Unit 06 — Rprog Part 03 —](03-unit-06-rprog-part-03.md) · [Up: contents](index.md) · [2 Advanced topics in working with functions →](05-2-advanced-topics-in-working-with-functions.md)
