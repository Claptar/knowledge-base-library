---
title: 7 Efficiency
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Efficiency

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In part because R is an interpreted language and in part because R is very dynamic (objects can be modified essentially arbitrarily after being created), R can be slow. Hadley Wickham’s Advanced R book has a section on Performance that discusses this in detail. However, there are a variety of ways that one can write efficient R code.

In general, make use of R’s built-in functions, as these tend to be implemented internally (i.e., via compiled code in C or Fortran). In particular, if R is linked to optimized BLAS and Lapack code (e.g. Intel’s _MKL_ , _OpenBLAS_ [on BCE and the SCF Linux servers], AMD’s _ACML_ [on the SCF Linux cluster, _vecLib_ for Macs [on the SCF Macs]), you should have good performance

63

(potentially comparable to Matlab and to coding in C). Sometimes you can figure out a trick to take your problem and transform it to make use of the built-in functions.

Note that I run a lot of MCMCs so I pay attention to making sure my calculations are fast as they are done repeatedly. Similarly, one would want to pay attention to speed when doing large simulations and bootstrapping, and in some cases for optimization. And if you’re distributing code, it’s good to have it be efficient. But in other contexts, it may not be worth your time. Also, it’s good practice to code it transparently first to reduce bugs and then to use tricks to speed it up and make sure the fast version works correctly.

Results can vary with with your system setup and version of R, so the best thing to do is figure out where the bottlenecks are in your code (e.g., with _Rprof()_ or just some basic use of _system.time()_ and _benchmark()_ ), and then play around with alternative specifications. And as you gain more experience, you’ll get some intuition for what approaches might improve speed, but even with experience I find myself often surprised by what matters and what doesn’t. It’s often worth trying out a bunch of different ideas; _system.time()_ and _benchmark()_ are your workhorse tools in this context.

For material on efficient R coding, including tools for timing and profiling your code to understand where the bottlenecks are, see the tutorial, _Writing efficient R code._

### **7.1 A note on hashing**

In the tutorial on efficient R coding, I mention that looking up objects by name in an R environment occurs via hashing, so it can be very fast. I’ll briefly describe what hashing is here.

A hash function is a function that takes as input some data and maps it to a fixed-length output that can be used as a shortened reference to the data. We’ve seen this in the context of git commits where each commit was labeled with a long base-16 number. This also comes up when verifying files on the Internet. You can compute the hash value on the file you get and check that it is the same as the hash value associated with the legitimate copy of the file.

For our purposes here, hashing can allow one to look up values by their name via a hash table. The idea is that you have a set of key-value pairs (sometimes called a dictionary) where the key is the name associated with the value and the value is some arbitrary object. Hashing allows one to quickly determine an index associated with the key and therefore quickly find the relevant value based on the index. For example, one approach is to compute the hash as a function of the key and then take the remainder when dividing by the number of key-value pairs to get the index. Here’s the procedure in pseudocode:

hash = hashfunc(key)

index = hash %% array_size # %% is modulo operator - it gives the remainder

64

In general, there will be collisions, with multiple keys assigned to the same index, but usually there will be a small number of keys associated with a given index or slot, and determining the correct value within a given index/slot (also called a bucket) is fast. Put another way, the hash function distributes the keys amongst an array of buckets and allows one to look up the appropriate bucket quickly based on the computed index value. When the hash table is properly set up, the cost of looking up a value does not depend on the number of key-value pairs stored.

### **7.2 Other approaches to speeding up R**

#### **7.2.1 pqR and other R engines**

Radford Neal, a prominent statistician/computer scientist has been working on a project called _pqR_ (pretty quick R) to rewrite some aspects of R to make them faster. There are also a few other projects that aim to reimplement the “R engine” such that one could run one’s R code with different back ends.

Here are some of the highlights of _pqR_ in terms of efficiency, as discussed at http://radfordneal.github.io/pqR/:

1. When R runs code such as just below, it actually creates a vector 1,2,....,n, (which can be computationally and memory intensive for large n) and then iterates over the values in the vector. pqR avoids this vector creation.

for(i in 1:n) { } vec[1:n]

2. As we’ll see in Section 8.5, R often avoids making copies of objects when it is not necessary. However, the scheme used to do this can be improved so that even fewer copies are made.

3. pqR automatically uses multiple cores for some calculations.

4. pqR avoid some checks for NA and NaN and the like in matrix calculations in which such checking would be slow and it doesn’t make sense to check for them anyway.

#### **7.2.2 Byte compiling**

R now allows you to compile R code, which goes by the name of byte compiling. Byte-compiled code is a special representation that can be executed more efficiently because it is in the form of compact codes that encode the results of parsing and semantic analysis of scoping and other complexities of the R source code. This byte code can be executed faster than the original R code because it skips the stage of having to be interpreted by the R interpreter.

65

The functions in the _base_ and _stats_ packages are now byte-compiled by default. (If you print out a function that is byte-compiled, you’ll see something like _<bytecode: 0x243a368>_ at the bottom.

We can byte compile our own functions using _cmpfun()_ . Here’s an example (silly since we we actually do this calculation using vectorized operations):

**library** (compiler); **library** (rbenchmark) f <- **function** (x){ **for** (i **in** 1: **length** (x)) x[i] <- x[i] + 1 **return** (x) } fc <- **cmpfun** (f) fc _# notice the indication that the function is byte compiled._ ## function(x){ ## for(i in 1:length(x)) x[i] <- x[i] + 1 ## return(x) ## } ## <bytecode: 0x4f21240> x <- **rnorm** (100000) **benchmark** ( **f** (x), **fc** (x), x <- x + 1, replications = 5) ## test replications elapsed relative user.self ## 2 fc(x) 5 0.032 32 0.032 ## 1 f(x) 5 0.398 398 0.394 ## 3 x <- x + 1 5 0.001 1 0.000 ## sys.self user.child sys.child ## 2 0.000 0 0 ## 1 0.005 0 0 ## 3 0.000 0 0

You can compile an entire source file with _cmpfile()_ , which produces a _.Rc_ file. You then need to use _loadcmp()_ to load in the _.Rc_ file, which runs the code.

Unfortunately, in my experience, byte compiling doesn’t usually speed things up much. As experienced R programmers we would never write the unvectorized code above.

66

### **7.3 Challenges**

One or more of these challenges may appear on a problem set.

**Challenge 1** : Here’s a calculation of the sort needed in mixture component modeling. I have a vector of _n_ observations. I need to find the likelihood of each observation under each of _p_ mixture components (i.e., what’s the likelihood if it came from each of the components). So I should produce a matrix of _n_ rows and _p_ columns where the value in the _i_ th row, _j_ th column is the likelihood of the _i_ th observation under the _j_ th mixture component. The idea is that the likelihoods for a given observation are used in assigning observations to clusters. A naive implementation is:

lik <- **matrix** ( **as.numeric** (NA), nr = n, nc = p) **for** (j **in** 1:p) lik[ , j] <- **dnorm** (y, mns[j], sds[j])

Note that _dnorm()_ can handle matrices and vectors as the observations **and** as the means and sds, so there are multiple ways to do this.

**Challenge 2** : Here’s a calculation of the sort needed in a mixed membership model, where each observation is associated with some number of components. Suppose you have


for a large number of observations, _n_ . I give you a vector of _µ_ values and a ragged list of weights (i.e., the number of weights varies by observation) and a ragged list of IDs identifying the cluster corresponding to each weight (note _mi_ varies by observation). Figure out how to calculate the vector of means, � _k_<sup>_w_</sup> _i,k_<sup>_µ_</sup> _ID_ [ _i,k_ ]<sup>asfastaspossible.Supposethat</sup><sup>_m_</sup> _i_<sup>nevergetstoobig(but</sup><sup>_µ_</sup> might have many elements) - could this help you? Part of thinking this through involves thinking about how you want to store the information so that the calculations can be done quickly. The data file _mixed-member.Rda_ contains example data for two scenarios: Scenario A has many _µ_ values and Scenario B has few _µ_ values.

**Challenge 3** : Write code that simulates a random walk in two dimensions for _n_ steps. First write out a straightforward implementation that involves looping. Then try to speed it up. The _cumsum()_ function may be helpful.

**Challenge 4:** Determine if it’s faster to subset based on vector of indices or a vector of logicals. Determine if it matters how big the original object is and how large the subset is, as well as whether the vector of indices is ordered.

**Challenge 5:** Figure out how to improve the efficiency of the following code chunk, which is part of a likelihood calculation for a student’s PhD research. Some test data is in _likLoops.Rda_ .

67

**for** (i **in** 1:n) { **for** (j **in** 1:n) { **for** (z **in** 1:K) { **if** (theta.old[i, z]*theta.old[j, z] == 0){ q[i, j, z] <- 0 } **else** { q[i, j, z] <- theta.old[i, z]*theta.old[j, z] / Theta.old[i, j] } } } } theta.new <- theta.old **for** (z **in** 1:K) { theta.new[,z] <- **rowSums** (A*q[,,z])/ **sqrt** ( **sum** (A*q[,,z])) }

**Challenge 6** : Another problem involving a computation from a student’s PhD research. The following is the probability mass function for an overdispersed binomial random variable:


where the denominator serves as a normalizing constant to ensure this is a valid probability mass function. How would one efficiently code the computation of the denominator? For our purposes here you can take _n_ = 2000, _p_ = 0 _._ 3 and _φ_ = 0 _._ 5 when you need to actually run your code.

**Challenge 7** : Yet another problem from a student’s PhD research. This is a very simplified version of a bioinformatics problem.

Fact 1: DNA sequencing involves chopping up the long sequence of DNA on a chromosome into many short _reads_ , which may overlap and are of various lengths.

Fact 2: DNA is composed of interspersed chunks of DNA that code for proteins (exons) and chunks that do not code for proteins (introns). The introns are stripped out during creation of the protein.

As part of a workflow, the student needed to determine, for a large number of exons, how many reads each exon overlapped with. The file _exons.Rda_ has position information for the reads (in an

68

object called _reads_ ) as well as position information for a number of exons (in _exons_ ). Each element of _reads_ , which is a list, is a set of short sequences making up a single read. So the challenge is to figure out, for each exon, how many of the reads there are for which the exon overlaps at least one of the short sequences making up the read.

---

[← 1560 bytes](34-1560-bytes.md) · [Up: contents](index.md) · [8 Evaluating memory use →](36-8-evaluating-memory-use.md)
