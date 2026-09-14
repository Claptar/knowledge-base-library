---
title: '%% is modulo operator - it gives the remainder'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# %% is modulo operator - it gives the remainder

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In general, there will be collisions, with multiple keys assigned to the same index, but usually there will be a small number of keys associated with a given index or slot, and determining the correct value within a given index/slot (also called a bucket) is fast. Put another way, the hash function distributes the keys amongst an array of buckets and allows one to look up the appropriate bucket quickly based on the computed index value. When the hash table is properly set up, the cost of looking up a value does not depend on the number of key-value pairs stored.

### 7.2 Other approaches to speeding up R

#### 7.2.1 pqR and other R engines

Radford Neal, a prominent statistician/computer scientist has been working on a project called pqR (pretty quick R) to rewrite some aspects of R to make them faster. There are also a few other projects that aim to reimplement the “R engine” such that one could run one’s R code with different back ends.

Here are some of the highlights of pqR in terms of efficiency, as discussed at http://radfordneal.github.io/pqR/:

1. When R runs code such as just below, it actually creates a vector 1,2,....,n, (which can be computationally and memory intensive for large n) and then iterates over the values in the vector. pqR avoids this vector creation. As discussed and illustrated in Section 8, this improvement is incorporated into R 3.5.0 and later versions.

for(i in 1:n) { } vec[1:n]

2. As we’ll see in Section 8.6, R often avoids making copies of objects when it is not necessary. However, the scheme used to do this can be improved so that even fewer copies are made.

3. pqR automatically uses multiple cores for some calculations.

4. pqR avoid some checks for NA and NaN and the like in matrix calculations in which such checking would be slow and it doesn’t make sense to check for them anyway.

69

#### 7.2.2 Byte compiling

R now allows you to compile R code, which goes by the name of byte compiling. Byte-compiled code is a special representation that can be executed more efficiently because it is in the form of compact codes that encode the results of parsing and semantic analysis of scoping and other complexities of the R source code. This byte code can be executed faster than the original R code because it skips the stage of having to be interpreted by the R interpreter.

The functions in the base and stats packages are now byte-compiled by default. (If you print out a function that is byte-compiled, you’ll see something like <bytecode: 0x243a368> at the bottom.

We can byte compile our own functions using cmpfun(). Here’s an example (silly since we we actually do this calculation using vectorized operations):

**library** (compiler); **library** (rbenchmark) f <- **function** (vals){ x <- **as.numeric** (NA) **length** (x) <- **length** (vals) **for** (i **in seq_along** (vals)) x[i] <- **exp** (vals[i]) **return** (x) } fc <- **cmpfun** (f) fc # notice the indication that the function is byte compiled. ## function(vals){ ## x <- as.numeric(NA) ## length(x) <- length(vals) ## for(i in seq_along(vals)) x[i] <- exp(vals[i]) ## return(x) ## } ## <bytecode: 0x4ca5dd0> x <- **rnorm** (100000) **benchmark** ( **f** (x), **fc** (x), y <- **exp** (x), replications = 5) ## test replications elapsed relative user.self ## 2 fc(x) 5 0.080 2.10 0.080 ## 1 f(x) 5 0.082 2.16 0.084 ## 3 y <- exp(x) 5 0.038 1.00 0.040

70

|##|sys.self|user.child|sys.child|
|---|---|---|---|
|##|2<br>0|0|0|
|##|1<br>0|0|0|
|##|3<br>0|0|0|


You can compile an entire source file with cmpfile(), which produces a .Rc file. You then need to use loadcmp() to load in the .Rc file, which runs the code.

Unfortunately, in my experience, byte compiling doesn’t usually speed things up much. As experienced R programmers we would never write the unvectorized code above.

### 7.3 Challenges

One or more of these challenges may appear on a problem set.

Challenge 1: Here’s a calculation of the sort needed in mixture component modeling. I have a vector of n observations. I need to find the likelihood of each observation under each of p mixture components (i.e., what’s the likelihood if it came from each of the components). So I should produce a matrix of n rows and p columns where the value in the ith row, jth column is the likelihood of the ith observation under the jth mixture component. The idea is that the likelihoods for a given observation are used in assigning observations to clusters. A naive implementation is:

lik <- **matrix** ( **as.numeric** (NA), nr = n, nc = p) **for** (j **in** 1:p) lik[ , j] <- **dnorm** (y, mns[j], sds[j])

Note that dnorm() can handle matrices and vectors as the observations and as the means and sds, so there are multiple ways to do this.

Challenge 2: Here’s a calculation of the sort needed in a mixed membership model, where each observation is associated with some number of components. Suppose you have


for a large number of observations, n. I give you a vector of µ values and a ragged list of weights (i.e., the number of weights varies by observation) and a ragged list of IDs identifying the cluster corresponding to each weight (note mi varies by observation). Figure out how to calculate the vector of means, �k<sup>w</sup> i,k<sup>µ</sup> ID[i,k]<sup>asfastaspossible.Supposethatm</sup> i<sup>nevergetstoobig(butµ</sup> might have many elements) - could this help you? Part of thinking this through involves thinking about how you want to store the information so that the calculations can be done quickly. The data

71

file mixed-member.Rda contains example data for two scenarios: Scenario A has many µ values and Scenario B has few µ values.

Challenge 3: Write code that simulates a random walk in two dimensions for n steps. First write out a straightforward implementation that involves looping. Then try to speed it up. The cumsum() function may be helpful.

Challenge 4: Determine if it’s faster to subset based on vector of indices or a vector of logicals. Determine if it matters how big the original object is and how large the subset is, as well as whether the vector of indices is ordered.

Challenge 5: Figure out how to improve the efficiency of the following code chunk, which is part of a likelihood calculation for a student’s PhD research. Some test data is in likLoops.Rda.

**for** (i **in** 1:n) { **for** (j **in** 1:n) { **for** (z **in** 1:K) { **if** (theta.old[i, z]*theta.old[j, z] == 0){ q[i, j, z] <- 0 } **else** { q[i, j, z] <- theta.old[i, z]*theta.old[j, z] / Theta.old[i, j] } } } } theta.new <- theta.old **for** (z **in** 1:K) { theta.new[,z] <- **rowSums** (A*q[,,z])/ **sqrt** ( **sum** (A*q[,,z])) }

Challenge 6: Another problem involving a computation from a student’s PhD research. The following is the probability mass function for an overdispersed binomial random variable:


where the denominator serves as a normalizing constant to ensure this is a valid probability mass function. How would one efficiently code the computation of the denominator? For our purposes

72

here you can take n = 2000, p = 0.3 and φ = 0.5 when you need to actually run your code.

Challenge 7: And yet another problem from a student’s PhD research (this one from a discussion just a few weeks ago).

The goal is to write a very fast function for selecting a random sample of size k from a population of size n.

There are two algorithms:

1. PIKK algorithm: Generate n random numbers and choose the elements of the population corresponding to the k smallest numbers.

2. Fisher-Yates-Knuth-Durstenfeld shuffle algorithm: This involves considering each element in turn and swapping it with a random element later in the set. Then return the first k.

Here are implementations of the two algorithms. Can we speed up either of them without resorting to coding in a faster language or directly using sample() (which calls out to a fast C function)?

PIKK <- **function** (n, k) { ## return indices of the sample of size k **sort** ( **runif** (n), index.return = TRUE)$ix[1:k] } FYKD <- **function** (n, k) { indices <- **seq_len** (n) **for** (i **in** 1:n) { j = **sample** (i:n, 1) tmp <- indices[i] indices[i] <- indices[j] indices[j] <- tmp } **return** (indices[1:k]) }

Challenge 8: Suppose we have a matrix in which each row is a vector of probabilities that add to one, and we want to generate a categorical sample based on each row. E.g., the first row might be (0.9, 0.05, 0.05) and the second row might be (0.1, 0.85, .0.5). When we generate the first sample, it is very likely to be a 1 and the second sample is very likely to be a 2. We could do this using a for loop over the rows of the matrix, and the sample() function, but that is a lot slower than some other ways we might do it. How can we do it faster?

73

n <- 100000 p <- 5 ## number of categories ## way to generate a random matrix of row-normalized probabilities: tmp <- **exp** ( **matrix** ( **rnorm** (n*p), nrow = n, ncol = p)) probs <- tmp / **rowSums** (tmp) smp <- **rep** (0, n) ## loop by row and use sample() **set.seed** (1) **system.time** ( **for** (i **in seq_len** (n)) smp[i] <- **sample** (p, 1, prob = probs[i, ]))

---

[← 7 Efficiency](55-7-efficiency.md) · [Up: contents](index.md) · [8 Evaluating memory use →](57-8-evaluating-memory-use.md)
