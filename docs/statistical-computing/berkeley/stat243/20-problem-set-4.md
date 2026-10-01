---
title: "20. Problem Set 4"
course: "Berkeley Stat 243"
chapter: 20
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. Problem Set 4

## What this covers

This chapter collects Problem Set 4 of Stat 243 (Statistical Computing for Statistics and Data
Science), as assigned in the Fall 2024 and Fall 2025 offerings of the course. The problems draw on
Unit 5, Sections 7-9: writing decorators, especially for memoization; how Python stores and copies
list and string objects in memory; the computational complexity of matrix operations and how
vectorization reduces it; and using vectorized numpy code (and, for extra credit, Jax) in place of
a Python-level loop. It assumes the reader already has the lecture material on closures and
decorators, Python's object and reference model, counting computational complexity, and numpy
vectorization and timing/profiling tools, none of which is reproduced here. Two of the four
problems were revised between the two offerings; both versions are given below since each draws on
the same material in a different way.

## Exercises

1. **Memoization decorator.** Memoization of a function means storing (caching) the value produced
   for a given input, and returning the cached result instead of rerunning the function when the
   same input recurs. It is worth doing when a calculation is expensive and will plausibly be
   repeated on an input already seen — a common situation in recursive algorithms that solve a
   large problem by combining solutions to overlapping subproblems. (For instance, given a
   genealogy of parent-child relationships, finding all descendants of a person by recursively
   finding the descendants of each child: if the descendants of one child have already been
   computed, memoization avoids recomputing them.)

   Write a decorator that implements memoization. It should handle functions with either one or
   two arguments — write one decorator, not two. You may assume the arguments are simple objects
   such as numbers or strings. As part of your solution, explain whether you need to use
   `nonlocal` in this case.

   Test your decorator on simple cases, such as applying the log-gamma function to a number, and
   multiplying two numbers together. These may not be realistic use cases, since the lookup itself
   can take longer than the calculation it replaces — check this by timing the memoized version
   against the direct calculation. Take care to time such fast calculations accurately (see the
   Unit 5 notes on timing).

2. **How Python stores list and string objects.**

   *Fall 2024 version — lists of numbers.* Experiment with creating lists of real-valued numbers
   of different lengths, and work out how much memory is used per reference (per element of the
   list), excluding the memory used by the values themselves. Repeat with lists of more
   complicated objects and see whether the behaviour is the same.

   Use the list `.copy` method on a list of numbers and on a list containing more complicated
   objects (including a nested list or a dictionary). Compare what happens when you modify
   elements at different levels of nesting, and relate what you find to `help(list.copy)` and to
   what you know about how lists are structured internally.

   Consider the lists

   ```python
   my_int = 1
   my_real = 1.0
   my_string = 'hat'

   xi = [1, my_int, my_int, 2]
   yi = [1, my_int, my_int, 2]
   xr = [1.0, my_real, my_real, 2.0]
   yr = [1.0, my_real, my_real, 2.0]

   xc = ['hat', my_string, my_string, 'dog']
   yc = ['hat', my_string, my_string, 'dog']
   ```

   What differs about how the elements of these lists are stored?

   *Fall 2025 version — strings.* Consider the lists

   ```python
   a = ['abc', 'xyz', 'def', 'ghi']
   b = ['abc'] * 4
   ```

   Determine what storage, if any, is reused in building the two lists.

   Then work out how much memory is used to store a list of strings: (i) how much memory a single
   string takes, including any metadata, and how this scales with the string's length; (ii) how
   much memory the list object's own metadata takes; and (iii) how memory scales with the number
   of elements, i.e. the cost of the references themselves. Work this out experimentally, from
   lists of different lengths and strings of different lengths, rather than from Python's internal
   documentation.

3. **Efficient trace of a matrix product.** Suppose you want the trace of a matrix product
   $A = XY$, i.e. $\sum_{i=1}^{n} A_{ii}$, where $X$ and $Y$ are both $n \times n$. A naive
   implementation is `np.sum(np.diag(X @ Y))`.

   a. What is the computational complexity of the naive implementation — $O(n)$, $O(n^2)$, or
      $O(n^3)$? (Count multiplications only, and ignore additions.) Why is the naive approach
      wasteful?
   b. Write Python code that computes the trace much more efficiently, using vectorized matrix
      operations rather than `map` or a list comprehension. What is the complexity of your
      solution?
   c. Plot the scaling of the naive and improved implementations as a function of $n$.
   d. (Extra credit) Implement the efficient version in Jax (see Unit 5, Section 9) and compare
      its timing to the numpy version, both with and without `jax.jit()`.

4. **Vectorizing a loop that samples or sums over many cases.**

   *Fall 2024 version — categorical sampling.* Suppose each column of a matrix is a vector of
   probabilities summing to one, and you want to draw one sample from the categorical distribution
   given by each column — e.g. a column $(0.9, 0.05, 0.05)$ should usually produce a $0$ (using
   Python's 0-based indexing), and a column $(0.1, 0.85, 0.05)$ should usually produce a $1$. The
   direct approach loops over columns and calls `np.random.choice()`:

   ```python
   import numpy as np
   import time

   n = 100000
   p = 5

   # Generate a random matrix and calculate probabilities.
   np.random.seed(1)
   tmp = np.exp(np.random.randn(p, n))
   probs = tmp / tmp.sum(axis=0)

   smp = np.zeros(n, dtype=int)

   # Generate sample by column.
   np.random.seed(1)
   start = time.time()
   for i in range(n):
       smp[i] = np.random.choice(p, size=1, p=probs[:, i])[0]
   print(f"Loop by column time: {round(time.time() - start, 2)} seconds.")
   ```

   but this is slow, since it is a Python-level loop over many columns.

   a. Consider transposing the matrix and looping over rows instead. Why might you expect this to
      be faster? Is it? Does numpy's `apply` functionality help?
   b. How can you do this much faster still — multiple orders of magnitude — by exploiting
      vectorization? (Hint: think about how uniform random numbers can be used to sample from a
      categorical distribution, rather than looping over columns or rows at all.)

   *Fall 2025 version — an overdispersed binomial log-likelihood.* This problem asks you to
   compute efficiently a log-likelihood that arose from a PhD student's research: the probability
   mass function of an overdispersed binomial random variable,

   $$
   P(Y = y; n, p, \phi) = \frac{f(y; n, p, \phi)}{\sum_{k=0}^{n} f(k; n, p, \phi)},
   $$

   $$
   f(k; n, p, \phi) = \binom{n}{k} \frac{k^k (n-k)^{n-k}}{n^n}
   \left(\frac{n^n}{k^k (n-k)^{n-k}}\right)^{\phi} p^{k\phi} (1-p)^{(n-k)\phi},
   $$

   where the denominator normalizes $f$ into a valid probability mass function. Take
   $n = 10000$, $p = 0.3$, $\phi = 0.5$ when you need to actually run your code, and recall that
   $0^0 = 1$.

   a. Write a first version that uses `map`/apply-style operations: a function that computes $f$
      for a single value of $k$, applied across all the terms of the sum. Do all the arithmetic on
      the log scale and exponentiate only just before summing, to avoid the overflow and underflow
      discussed in Unit 8.
   b. Now vectorize the computation using numpy arrays, and compare its timing to the
      non-vectorized version from (a).
   c. Use timing and profiling tools to find which steps are slow, and improve them — watch for
      repeated calculations and operations that do not need to be done at all. Compare the timing
      to your vectorized version from (b).

## Sources

- Problem 1, problem 3, and the Fall 2024 forms of problems 2 and 4 are from Problem Set 4, Stat
  243, Fall 2024
  ([`ps/ps4.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/ps/ps4.qmd)).
- The Fall 2025 forms of problems 2 and 4 are from Problem Set 4, Stat 243, Fall 2025
  ([`ps/ps4.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/ps/ps4.qmd)).
- No slides or lecture transcript were supplied for this chapter. Both problem sets point to
  material not contained in the problem statements themselves: the "Unit 5 notes" on timing
  (problem 1), Unit 5 Section 9 on Jax (problem 3d), and Unit 8 on numerical overflow and
  underflow (problem 4, Fall 2025 version).

---

[← 19. Problem Set 3](19-problem-set-3.md) · [Contents](index.md) · [21. Parallel Jobs on Shared Clusters →](21-parallel-jobs-on-shared-clusters.md)
