---
title: Unit 05 — programming Part 42 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 42 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can compile an entire source file with _cmpfile()_ , which produces a _.Rc_ file. You then need to use _loadcmp()_ to load in the _.Rc_ file, which runs the code. Unfortunately, in my experience, byte compiling doesn’t usually speed things up much.

### **7.4 Challenges**

We’ll work on some of these challenges in class. In addition, one or more of these challenges will appear on PS4.

**Challenge 1** : Here’s a calculation of the sort needed in mixture component modeling. I have a vector of _n_ observations. I need to find the likelihood of each observation under each of _p_ mixture components (i.e., what’s the likelihood if it came from each of the components). (In this case, the the likelihood is simply the normal density of the observation given the mean and standard deviation of the component normal distribution.) So I should produce a matrix of _n_ rows and _p_ columns where the value in the _i_ th row, _j_ th column is the likelihood of the _i_ th observation under the _j_ th mixture component. The idea is that the likelihoods for a given observation are used in assigning observations to clusters. A naive implementation is:

lik <- **matrix** ( **as.numeric** (NA), nr = n, nc = p) **for** (j **in** 1:p) lik[ , j] <- **dnorm** (y, mns[j], sds[j])

Note that _dnorm()_ can handle matrices and vectors as the observations **and** as the means and sds, so there are multiple ways to do this. Try to figure out the fastest way to do this, amongst the options of looping over the mixture components, looping over the observations, using vector-

78

ized operations that recycle the observations, using vectorized operations that recycle the mixture components, etc.

**Challenge 2** : Here’s a calculation of the sort needed in a mixed membership model, where each observation is associated with some number of components. Suppose you have


for a large number of observations, _n_ . I give you a vector of _µ_ = ( _µ_ 1 _, . . . , µK_ ) values and a ragged list of weights (i.e., the number of weights varies by observation) and a ragged list of IDs identifying the cluster corresponding to each weight (note _mi_ varies by observation). Figure out how to calculate the vector of means,<sup>�</sup> _j_<sup>_w_</sup> _i,j_<sup>_µ_</sup> _ID_ [ _i,j_ ]<sup>asfastaspossible.Supposethat</sup><sup>_m_</sup> _i_<sup>never</sup> gets too big (but _µ_ might have many elements) - could this help you? Part of thinking this through involves thinking about how you want to store the information so that the calculations can be done quickly. The data file _mixedMember.Rda_ contains example data for two scenarios: Scenario A has many _µ_ values and Scenario B has few _µ_ values.

**Challenge 3** : Write code that simulates a random walk in two dimensions for _n_ steps. First write out a straightforward implementation that involves looping. Then try to speed it up. The _cumsum()_ function may be helpful.

**Challenge 4:** Determine if it’s faster to subset based on vector of indices or a vector of logicals. Determine if it matters how big the original object is and how large the subset is, as well as whether the vector of indices is ordered.

**Challenge 5:** Figure out how to improve the efficiency of the following code chunk, which is part of an iterative optimization of a log-likelihood for a student’s PhD research. Some test data is in _likLoops.Rda_ .

ll <- **function** (Theta, A) { sum.ind <- **which** (A==1, arr.ind=T) logLik <- **sum** ( **log** (Theta[sum.ind])) - **sum** (Theta) **return** (logLik) }

oneUpdate <- **function** (A, n, K, theta.old, thresh = 0.1) { theta.old1 <- theta.old Theta.old <- theta.old %*% **t** (theta.old) L.old <- **ll** (Theta.old, A) q <- **array** (0, dim = **c** (n, n, K))

79

**for** (i **in** 1:n) { **for** (j **in** 1:n) { **for** (z **in** 1:K) { **if** (theta.old[i, z]*theta.old[j, z] == 0){ q[i, j, z] <- 0 } **else** { q[i, j, z] <- theta.old[i, z]*theta.old[j, z] / Theta.old[i, j] } } } } theta.new <- theta.old **for** (z **in** 1:K) { theta.new[,z] <- **rowSums** (A*q[,,z])/ **sqrt** ( **sum** (A*q[,,z])) } Theta.new <- theta.new %*% **t** (theta.new) L.new <- **ll** (Theta.new, A) converge.check <- **abs** (L.new - L.old) < thresh theta.new <- theta.new/ **rowSums** (theta.new) **return** ( **list** (theta = theta.new, loglik = L.new, converged = converge.check)) } _# initialize the parameters at random starting values_ temp <- **matrix** ( **runif** (n*K), n, K) theta.init <- temp/ **rowSums** (temp) _# do single update_ out <- **oneUpdate** (A, n, K, theta.init) _# in the real code, oneUpdate was called repeatedly in a while loop # as part of an iterative optimization to find a maximum likelihood estimator_

**Challenge 6** : Another problem involving a computation from a student’s PhD research. The

80

following is the probability mass function for an overdispersed binomial random variable:


where the denominator serves as a normalizing constant to ensure this is a valid probability mass function. How would one efficiently code the computation of the denominator? For our purposes here you can take _n_ = 2000, _p_ = 0 _._ 3 and _φ_ = 0 _._ 5 when you need to actually run your code.

**Challenge 7** : And yet another problem from a student’s PhD research (this one from a discussion just a few weeks ago).

The goal is to write a very fast function for selecting a random sample of size k from a population of size n.

There are two algorithms:

1. PIKK algorithm: Generate n random numbers and choose the elements of the population corresponding to the k smallest numbers.

2. Fisher-Yates-Knuth-Durstenfeld shuffle algorithm: This involves considering each element in turn and swapping it with a random element later in the set. Then return the first k.

Here are implementations of the two algorithms. Can we speed up either of them without resorting to coding in a faster language or directly using _sample()_ (which calls out to a fast C function)?

PIKK <- **function** (n, k) { _## return indices of the sample of size k_ **sort** ( **runif** (n), index.return = TRUE)$ix[1:k] } FYKD <- **function** (n, k) { indices <- **seq_len** (n) **for** (i **in** 1:n) { j = **sample** (i:n, 1) tmp <- indices[i] indices[i] <- indices[j] indices[j] <- tmp }

81

**return** (indices[1:k]) }

**Challenge 8:** Suppose we have a matrix in which each row is a vector of probabilities that add to one, and we want to generate a categorical sample based on each row. E.g., the first row might be (0.9, 0.05, 0.05) and the second row might be (0.1, 0.85, .0.5). When we generate the first sample, it is very likely to be a 1 and the second sample is very likely to be a 2. We could do this using a for loop over the rows of the matrix, and the _sample()_ function, but that is a lot slower than some other ways we might do it. How can we do it faster?

n <- 100000 p <- 5 _## number of categories ## way to generate a random matrix of row-normalized probabilities:_ tmp <- **exp** ( **matrix** ( **rnorm** (n*p), nrow = n, ncol = p)) probs <- tmp / **rowSums** (tmp) smp <- **rep** (0, n) _## loop by row and use sample()_ **set.seed** (1) **system.time** ( **for** (i **in seq_len** (n)) smp[i] <- **sample** (p, 1, prob = probs[i, ]) )

---

[← 7 Efficiency](41-7-efficiency.md) · [Up: contents](index.md) · [8 Evaluating memory use →](43-8-evaluating-memory-use.md)
