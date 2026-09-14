---
title: Approaches to Motif Finding
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Approaches to Motif Finding

**Source:** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Enumerative (‘dictionary’)

- search for a _k_ mer/set of _k_ mers/regular expression that is statistically over-represented

- Probabilistic Optimization (e.g., Gibbs sampler)

- stochastic search of the space of possible PSPMs

- Deterministic Optimization (e.g., MEME)

   - deterministic search of space of possible PSPMs

13

#### **What the motif landscape might look like**


<!-- Start of picture text -->
14<br><!-- End of picture text -->

14

##### **Monte Carlo Algorithms**

The Gibbs motif sampler is a **Monte-Carlo algorithm**

Photograph of people playing craps removed due to copyright restrictions.

- **General definition:** class of computational algorithms that rely on repeated random sampling to compute their results

- **Specific definition:** randomized algorithm where the computational resources used are bounded but the answer is not guaranteed to be correct 100% of the time

###### Related to

- **Las Vegas algorithm** - a randomized algorithm that always gives correct results (or informs about failure)

15

Example: The Gibbs Motif Sampler The likelihood function for a set of sequences  _s_  with motif locations _A_


<!-- Start of picture text -->
background<br>freq. vector<br>weight matrix<br><br> | Θ,θ<br>P ( s  ,  A B )  =<br>∏ θ B , s k  ,1  × ... ×θ B ,  s k  , Ak −1  × Θ1,  × Θ2,  × ... × Θ8,  ×θ B ,  s k  , Ak =8 × ... ×θ B ,  L<br>k s k , A k s k , A k +1  s k , A k + 7<br>s k<br>= “actactgtatcgtactgactgattaggccatgactgcat”<br>Motif location A k<br>Lawrence et al.  Science  1993<br><!-- End of picture text -->

16

- The Gibbs Sampling Algorithm In Words I Given **N** sequences of length **L** and desired motif width **W:**

   - 1) Choose a starting position in each sequence at random:

      - **a1** in seq 1, **a2** in seq 2, …, **aN** in sequence **N**

   - 2) Choose a sequence at random from the set (say, seq 1).

   - 3) Make a weight matrix model of width **W** from the sites in all sequences _except_ the one chosen in step 2.

   - 4) Assign a probability to each position in seq 1 using the weight matrix model constructed in step 3:

      - **p** = { **p1** , **p2** , **p3** , …, **pL-W+1** }

Lawrence et al. _Science_ 1993

17

---

[← Statistical (Shannon) Entropy](02-statistical-shannon-entropy.md) · [Up: contents](index.md) · [Gibbs Sampling Algorithm I →](04-gibbs-sampling-algorithm-i.md)
