---
title: 'Stat243: Problem Set 4, Due Monday Oct. 14'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps4.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/ps/ps4.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 4, Due Monday Oct. 14

**Source:** [`ps/ps4.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps4.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 3, 2019

Comments:

- This covers the second half of Unit 5.

- It’s due at 2 pm on Monday October 14, **both submitted as a PDF to bCourses as well as committed to your Github repository** .

- Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

- The formatting requirements are the same as previous problem sets.

- Note that for problems 1 and 4, you will be inspecting the addresses of objects and determining the copying that takes place. The results when knitting and results in RStudio may differ from results when running R outside of RStudio. If you see inconsistencies, the correct answer is obtained when running R outside of RStudio. So if there are inconsistencies, you may need to include a screenshot or copy the output from the R console into your solution as comments in your code.

## **Problems**

1. Item #4 of Section 6.10 of Unit 5 talks about the idea of a _closure_ as a function that has data associated with it. This builds on the ideas we talked about when discussing scoping. The following code embeds the value of ’x’ inside the function as variable named ’data’.

x <- 1:10 f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) data <- 100 **myFun** (3) ## [1] 3 6 9 12 15 18 21 24 27 30 x <- 100 **myFun** (3) ## [1] 3 6 9 12 15 18 21 24 27 30

1

- (a) What is the maximum number of copies that exist of the vector 1:10 during the execution of _f()?_ Why?

- (b) Use _serialize()_ to generate a sequence of bytes that store the information in the closure. Is the size of the serialized object the size you would expect given your answer to (a)? If not, can you explain what is happening? For this part of the problem, make _x_ a large enough vector that your answer concentrates on the number of bytes involved in the numeric vector rather than in the function itself or any overhead for storing R objects.

- (c) It seems unnecessary to have the “data <- input” line, so let’s try the following.

x <- 1:10 f <- **function** (data){ g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) data <- 100 **myFun** (3) **## Error in myFun(3): object ’x’ not found**

Explain what is happening and why this doesn’t work to embed a constant data value into the function. Recall our discussion of when function arguments are evaluated.

   - (d) Can you figure out a way to make the code in part (c) work without explicitly creating a copy of the vector as in the original code? If you do that, how big is the resulting serialized closure?

2. Challenge 5 of Section 7.3 of Unit 5.

The following is real code for maximizing the likelihood function of a statistical model, written by a Statistics grad student. The goal is to improve the efficiency of this R code (also available in ps4.R). There are a number of improvements that can be made; in particular the code should not need three nested for loops. Consider also whether there are any calculations that are done repeatedly that need only be done once. Report the time it takes before and after your improvements. Compared to this code, I was able to achieve a 12-fold speedup. Also, the style of the code can be improved (though you should probably keep the names of objects somewhat similar to what they currently are to assist comparing between the two versions of the code). _ps4prob2.Rda_ provides values for _A_ , _k_ , and _n_ .

**load** ('ps4prob2.Rda') _# should have A, n, K_ ll <- **function** (Theta, A) { sum.ind <- **which** (A==1, arr.ind=T) logLik <- **sum** ( **log** (Theta[sum.ind])) - **sum** (Theta) **return** (logLik) } oneUpdate <- **function** (A, n, K, theta.old, thresh = 0.1) { theta.old1 <- theta.old Theta.old <- theta.old %*% **t** (theta.old) L.old <- **ll** (Theta.old, A)

2

q <- **array** (0, dim = **c** (n, n, K)) **for** (i **in** 1:n) { **for** (j **in** 1:n) { **for** (z **in** 1:K) { **if** (theta.old[i, z]*theta.old[j, z] == 0){ q[i, j, z] <- 0 } **else** { q[i, j, z] <- theta.old[i, z]*theta.old[j, z] / Theta.old[i, j] } } } } theta.new <- theta.old **for** (z **in** 1:K) { theta.new[,z] <- **rowSums** (A*q[,,z])/ **sqrt** ( **sum** (A*q[,,z])) } Theta.new <- theta.new %*% **t** (theta.new) L.new <- **ll** (Theta.new, A) converge.check <- **abs** (L.new - L.old) < thresh theta.new <- theta.new/ **rowSums** (theta.new) **return** ( **list** (theta = theta.new, loglik = L.new, converged = converge.check)) } _# initialize the parameters at random starting values_ temp <- **matrix** ( **runif** (n*K), n, K) theta.init <- temp/ **rowSums** (temp) _# do single update_ out <- **oneUpdate** (A, n, K, theta.init) _# in the real code, oneUpdate was called repeatedly in a while loop # as part of an iterative optimization to find a maximum likelihood estimator_

3. Challenge 2 of Section 7.3 of Unit 5.

Suppose you have a mixed membership model, _yi ∼N_ (<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_iwi,jµID_</sup> _i,j_<sup>_, σ_2), for a large number of</sup> observations, _i_ = 1 _, . . . , n_ , where _µ_ = ( _µ_ 1 _, . . . , µK_ ). In this model, each observation belongs to multiple clusters, where each cluster has its own mean. Please write code to do the following using the objects in _mixedMember.Rda_ (see https://www.stat.berkeley.edu/ _∼_ paciorek/transfer/mixedMember.Rda). There are two test cases:

- (A) _K_ , the number of components, is large but there are a limited number of components per observation, i.e., max _i_ ( _mi_ ) is not large.

- (B) _K_ is small.

3

For each case, _mixedMember.Rda_ provides a vector containing the _µ_ values, a list of weights, and a list of IDs that map how the weights correspond to the components of the mean vector. For example, for person 1, one might have weights _w_ 1 _,_ 1 = 0 _._ 3, _w_ 1 _,_ 2 = 0 _._ 5, and _w_ 1 _,_ 3 = 0 _._ 2 and IDs _ID_ 1 _,_ 1 = 2 _, ID_ 1 _,_ 2 = 22, _ID_ 1 _,_ 3 = 31, indicating that we need to calculate _w_ 1 _,_ 1 _µ_ 2 + _w_ 1 _,_ 2 _µ_ 22 + _w_ 1 _,_ 3 _µ_ 31.

- (a) Write a line of code using _sapply()_ that will calculate<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_iwi,jµID_</sup> _i,j_<sup>for all the observations.</sup>

- (b) Set up data objects (in whatever format you choose) and write efficient code that uses those objects to calculate<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_iwi,jµID_</sup> _i,j_<sup>under case A.</sup>

- (c) Set up data objects (in whatever format you choose) and write efficient code that uses those objects to calculate<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_iwi,jµID_</sup> _i,j_<sup>under case B.</sup>

- (d) Compare speed for the two test cases using the three different variants of the code using R’s benchmarking tools. For Case A, your code in (b) should give roughly one order of magnitude speed-up compared to your code in (a). For Case B, your code in (c) should give between one and two orders of magnitude speed up relative to your code in (a).

Note, your code for setting up the data objects in parts (b) and (c) does NOT count toward your computational efficiency. The idea is to get the data in the form you want it, implicitly assuming that this would only be done once, but the calculation of the weighted sum would be done repeatedly. Also, your solution should be able to keep the _muA_ and _muB_ vectors as they are. Hints: Consider how you can fully vectorize the calculation and/or convert the problem to a simple matrix algebra calculation. For both case A and case B you should be able to set up matrices to hold the data and efficiently do the computation on matrices rather than on lists.

4. This question explores memory use and copying with lists.

   - (a) Consider a list of numeric vectors. Modify an element of one of the vectors. Can R make the change in place, without creating a new list or a new vector?

   - (b) Next, make a copy of the list and determine if there any copy-on-change going on. When a change is made to one of the vectors in one of the lists, is a copy of the entire list made or just of the relevant vector?

   - (c) Run the following code in a new R session. The result of _.Internal(inspect())_ and of _object.size()_ conflict with each other. In reality only ~80 MB is being used, as can be seen with _gc()_ . Explain why this is the case.

**gc** () tmp <- **list** () x <- **rnorm** (1e7) tmp[[1]] <- x tmp[[2]] <- x **.Internal** ( **inspect** (tmp)) **object.size** (tmp) **gc** ()

- (d) Suppose you grow a list in the inefficient way we discussed for vectors in the efficient R tutorial as seen below. Given what you’ve learned above about the structure of a list, if at the end you have _n_ elements in the list, how many bytes are unnecessarily copied (relative to the situation of you creating an empty list of length _n_ in advance) when running the following code?

4

n <- 10 myList <- **list** () **for** (i **in** 1:n) { myList[[i]] <- **rnorm** (20) }

5

---

[Up: contents](../index.md)
