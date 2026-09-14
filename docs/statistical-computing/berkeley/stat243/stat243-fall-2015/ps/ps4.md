---
title: Ps 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps4.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/ps/ps4.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 04 —

**Source:** [`ps/ps4.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps4.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 4, Due Monday 10/12

September 30, 2015

Comments:

- This covers Unit 4 (Sections 6-8) and Unit 5.

- It’s due at the start of class on 10/12, on paper and via Github.

- As usual, your solution should mix textual description of your solution, code, and example output.

- Please note my comments in the syllabus about when to ask for help and about working together.

- Please give the names of any other students that you worked with on the problem set.

## **Problems**

1. As we’ll see in the simulation unit, random numbers on a computer are not truly random. They are numbers generated deterministically in a way that they appear random. In fact, the generator is periodic - at some point the sequence of random numbers starts to repeat itself. The _set.seed_ function chooses a position in that periodic sequence by setting the value of the _.Random.seed_ variable. If you call _set.seed()_ with the same input argument you will generate the same sequence of random numbers. When using R’s default Mersenne twister random number generator, .Random.seed[2] will give information about the position within the periodic sequence. Every time you generate a new random uniform number, that position will increment by one.

   - (a) The following code was an attempt by me to save the position of the generator to a file and then to read it back in within a function and be able to start generating random numbers where I left off when I saved the position to the file. This code does not work because of a scoping issue.

**set.seed** (0) **runif** (1) ## [1] 0.8966972 **save** (.Random.seed, file = 'tmp.Rda') **runif** (1) ## [1] 0.2655087 **load** ('tmp.Rda') **runif** (1) ## [1] 0.2655087

1

tmp <- **function** () { **load** ('tmp.Rda') **runif** (1) } **tmp** () ## [1] 0.3721239

Using R’s debugging tools, determine what the problem is. Your written solution should describe how you used the debugging tools and should show a printout of the _tmp_ function that includes any lines of code that you inserted for debugging.

   - (b) In light of your understanding of R’s scoping rules, revise the code so that it works. I.e., when runif(1) is called in _tmp()_ , it should give the same result as when runif(1) was called just after the _save()_ .

2. The following example comes from a problem encountered by a Statistics graduate student for his thesis work. He needed to compute the likelihood for an overdispersed binomial random variable with the following probability mass function (pmf):


where the denominator serves as a normalizing constant to ensure this is a valid probability mass function. Your job is to write code to evaluate the denominator of _P_ ( _Y_ = _y_ ). In the graduate student’s work, he needs to evaluate _P_ ( _Y_ = _y_ ) many many times, so efficient calculation of the denominator is important. For our purposes here you can take _p_ = 0 _._ 3 and _φ_ = 0 _._ 5 when you need to actually run your function.

   - (a) First, write code to evaluate the denominator using _apply()/lapply()/sapply()_ . Make sure to calculate all the terms in _f_ ( _k_ ; _n, p, φ_ ) on the log scale to avoid numerical issues, before exponentiating and summing. Describe briefly what happens if you don’t do the calculation on the log scale. Hint: ?Special in R will tell you about a number of useful functions. Also, recall that 0<sup>0</sup> = 1.

   - (b) Now write code to do the calculation in a fully vectorized fashion with no loops or _apply()_ functions. Using the benchmarking tools discussed in the tutorial on efficient R code, compare the relative timing of (a) and (b) for some different values of _n_ ranging in magnitude from around 10 to around 2000.

   - (c) (Extra credit) Extra credit may be given based on whether your code is as fast as my solution. I’d suggest using _Rprof()_ to assess the steps in your code for (b) that are using the most time and focusing your efforts on increasing the speed of those parts of the code.

3. Suppose you have a model, _yi ∼N_ (<sup>�</sup><sup>_m_</sup> _k_ =1<sup>_iwi,kµID_</sup> _i,k_<sup>_, σ_2),for a large number of observations,</sup><sup>_i_=</sup> 1 _, . . . , n_ . Please write code to do the following using the objects in _mixedMember.Rda_ (see the _units_ directory of the class repository). There are two test cases:

   - (A) _K_ , the number of components, is large but there are a limited number of components per observation, i.e., max _i_ ( _mi_ ) is not large.

2

- (B) _K_ is small.

For each case, _mixedMember.Rda_ provides a vector containing the _µ_ values, a list of weights, and a list of IDs that map how the weights correspond to the components of the mean vector. E.g. for person 1, one might have weights _w_ 1 _,_ 1 = 0 _._ 3, _w_ 1 _,_ 2 = 0 _._ 5, and _w_ 1 _,_ 3 = 0 _._ 2 and IDs _ID_ 1 _,_ 1 = 2 _, ID_ 1 _,_ 2 = 22, _ID_ 1 _,_ 3 = 31, indicating that we need to calculate _w_ 1 _,_ 1 _µ_ 2 + _w_ 1 _,_ 2 _µ_ 22 + _w_ 1 _,_ 3 _µ_ 31.

- (a) Write a line of code using _sapply()_ that will calculate<sup>�</sup><sup>_m_</sup> _k_ =1<sup>_iwi,kµID_</sup> _i,k_<sup>for all the observations.</sup>

- (b) Set up data objects (in whatever format you choose) and write efficient code that uses those objects to calculate<sup>�</sup><sup>_m_</sup> _k_ =1<sup>_iwi,kµID_</sup> _i,k_<sup>under case A.</sup>

- (c) Set up data objects (in whatever format you choose) and write efficient code that uses those objects to calculate<sup>�</sup><sup>_m_</sup> _k_ =1<sup>_iwi,kµID_</sup> _i,k_<sup>under case B.</sup>

- (d) Compare speed for the two test cases using the three different variants of the code using R’s benchmarking tools. For Case A, your code in (b) should give roughly one order of magnitude speed-up compared to your code in (a). For Case B, your code in (c) should give between one and two orders of magnitude speed up relative to your code in (a).

Note, your code for setting up the data objects in parts (b) and (c) does NOT count toward your computational efficiency. The idea is to get the data in the form you want it, implicitly assuming that this would only be done once, but the calculation of the weighted sum would be done repeatedly. Also, your solution should be able to keep the _muA_ and _muB_ vectors as they are.

Hints: (1) we saw a trick for setting up data structures for this kind of scenario in class. (2) Consider how you can fully vectorize the calculation and/or convert the problem to a simple matrix algebra calculation.

4. Consider a linear regression with 1 million observations and 3 covariates/predictors (4 counting the intercept). You can generate a test dataset using _rnorm()_ , creating 4 individual vectors, one for y and three for the covariates and fit the model with lm(y ~ x1 + x2 + x3). In your explorations, please use _mem_used()_ rather than _gc()_ as this seems to give more interpretable results here.

   - (a) Use the tools we’ve seen to figure out how much total memory is in use in _lm()_ at the point at which _lm.fit()_ is called. How much additional memory use is this compared to the memory used in the global environment to store the observations and covariates?

   - (b) Figure out where the major uses of memory are in _lm()_ leading up to the call to _lm.fit()_ . You can ignore any objects that are no bigger than 10% of the size of the vector of observations. Why are some of the vectors and matrices larger than 8 bytes per number? I’m not expecting a perfect answer here – R carries out some fairly involved manipulations to reduce memory – but you should be able to get the big picture of where additional memory gets used. If there seem to be contradictions in what you are seeing, you can report those contradictions without figuring out exactly what is going on.

   - (c) If you were rewriting the _lm()_ function to not use as much memory, what could you do to reduce memory use before calling _lm.fit()_ ? Motivational note: obviously with 1 million observations and three covariates, memory use is not a problem on a modern machine, but consider if you had hundreds of millions of observations.

   - (d) Extra credit may be given for particularly detailed explanations of how R is using memory leading up to the call to _lm.fit()_ . Extensive use of _.Internal(inspect())_ is likely to be needed here.

3

---

[Up: contents](../index.md)
