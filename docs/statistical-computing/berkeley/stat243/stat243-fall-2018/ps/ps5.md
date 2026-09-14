---
title: 'Stat243: Problem Set 5, Due Friday October 19'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps5.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/ps/ps5.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 5, Due Friday October 19

**Source:** [`ps/ps5.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps5.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### October 7, 2018

This covers Unit 6 plus bits and pieces of Units 8 and 9. It’s due **as PDF submitted to bCourses** and submitted via Github at 2 pm on Oct. 19. Some general guidelines on how to present your problem set solutions:

1. Please use Rmd/Rtex as in previous problem sets.

2. Your solution should not just be code - you should have text describing how you approached the problem and what the various steps were.

3. Your PDF submission should be the PDF produced from your Rmd/Rtex. Your Github submission should include the Rtex/Rmd file, any R code files containing chunks that you read into your Rtex/Rmd file, and the final PDF, all named according to the guidelines in _howtos/submitting-electronically.txt_ .

4. Your code should have comments indicating what each function or block of code does, and for any lines of code or code constructs that may be hard to understand, a comment indicating what that code does. You do not need to show exhaustive output but in general you should show short examples of what your code does to demonstrate its functionality.

5. Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

## **Problems**

1. Linear algebra preparation. Before class on Wednesday October 17, please read the first section of Unit 9 (Numerical Linear Algebra) and answer the following question. (Turn in your answer as part of the problem set, but please do it by Wednesday.)

For a symmetric matrix _A_ , we have the following matrix decomposition (the eigendecomposition): _A_ = ΓΛΓ<sup>_⊤_</sup> , where Γ is an orthogonal matrix of (column) eigenvectors, and Λ is a diagonal matrix of eigenvalues. Use the properties discussed in Section 1 to briefly show that _|A|_ is the product of the eigenvalues.

2. Numerical problems in logistic regression. Consider that in logistic regression the linear predictor, _Xiβ_ , (where _Xi_ is the ith row of the predictor matrix, _X_ ) is transformed into a probability using the inverse logistic (expit) transformation.


where


1

This mathematical expression for the _expit_ function doesn’t work numerically on a computer for large values of _z_ . Explain why not and re-express the function such that if implemented in computer code, it is numerically stable.

3. Consider the following estimate of the variance of a set of large numbers with small variance:

**set.seed** (1) z <- **rnorm** (10, 0, 1) x <- z + 1e12 **formatC** ( **var** (z), 20, format = 'f') ## [1] "0.60931443706111987346" **formatC** ( **var** (x), 20, format = 'f') ## [1] "0.60931216345893013386"

Explain why these two estimates agree to only 5 digits when mathematically the variance of _z_ and the variance of _x_ are exactly the same.

4. (This problem makes use of ideas from Unit 8, to be covered at the beginning of the week of Oct. 15, so you may need to wait until then to work on this.) Let’s consider parallelization of a simple linear algebra computation. In your answer, you can assume _m_ = _n/p_ is an integer. Assume you have _p_ cores with which to do the computation.

   - (a) Consider trying to parallelize matrix multiplication, in particular the computation _XY_ where both _X_ and _Y_ are _n × n_ . There are lots of ways we can break up the computations, but let’s keep it simple and consider parallelizing over the columns of _Y_ . Given the considerations we discussed in Unit 8, when you parallelize the matrix multiplication, why might it be better to break up _Y_ into _p_ blocks of _m_ = _n/p_ columns rather than into _n_ individual column-wise computations? Note: I’m not expecting a detailed answer here – a sentence or two is fine.

   - (b) Let’s consider two ways of parallelizing the computation and count (1) the amount of memory used at any single moment in time, when all _p_ cores are doing their calculations, including memory use in storing the result and (2) the communication cost – count the total number of numbers that need to be passed to the workers as well as the numbers passed from the workers back to the master when returning the result. Which approach is better for minimizing memory use and which for minimizing communication?

      - Approach A: divide _Y_ into _p_ blocks of equal numbers of columns, where the first block has columns 1 _, . . . , m_ where _m_ =<sup>_<u>n</u>_</sup> _p_<sup>andsoforth.Pass</sup><sup>_X_andthe</sup><sup>_j_thsubmatrixof</sup><sup>_Y_asthe</sup> _j_ th task out of _p_ total tasks.

      - Approach B: divide _X_ into _p_ blocks of rows, where the first block has rows 1 _, . . . , m_ and _Y_ into _p_ blocks of columns as above. Pass pairs of a submatrix of _X_ and submatrix of _Y_ to the workers, resulting in _p_<sup>2</sup> different tasks that we have to iterate through using our _p_ cores.

Note: in reality parallelized matrix multiplication is done in much more complicated/sophisticated ways – if you’re interested, there is some discussion in these notes from Jim Demmel’s CS class: https://people.eecs.berkeley.edu/ _∼_ demmel/cs267_Spr12/Lectures/lecture11_densela_1_jwd12.ppt

2

---

[Up: contents](../index.md)
