---
title: The six algorithmic settings for HMMs One path All paths
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The six algorithmic settings for HMMs One path All paths

**Source:** `lectures/04-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1.  Scoring x, one path

P(x,π) Prob of a path, emissions

3. Viterbi decoding

   - π* = argmaxπ P(x,π)

Most likely path

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

6. Unsupervised learning. Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

2.  Scoring x, all paths

P(x) = Σπ P(x,π)

Prob of emissions, over all paths

4.  Posterior decoding

- π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

Path containing the most likely state at any time point.

6.  Unsupervised learning

   - Λ* = argmaxΛ ΣπP(x,π|Λ)

Baum-Welch training, over all paths

24

**3. DECODING: What was the sequence of hidden states?**

Given: Model parameters ei(.), aij Given: Sequence of emissions x

Find:

Sequence of hidden states π

25

## **Finding the optimal path**

- We can now evaluate any path through hidden states, given the emitted sequences

- How do we find the best path?

- Optimal substructure!  Best path through a given state is:

   - Best path to previous state

   - Best transition from previous state to this state

   - Best path to the end state

-  Viterbi algortithm

   - Define Vk(i) = Probability of the most likely path through state i=k

   - Compute Vk(i+1) as a function of maxk’ { Vk’(i) }

   - Vk(i+1) = ek(xi+1) * maxj ajk Vj(i)

      -  Dynamic Programming

26

Photograph of Andrew J. Viterbi removed due to copyright restrictions.

27

## **Finding the most likely path**


<!-- Start of picture text -->
1  1  1  1<br>…<br>2  2  2  2<br>…<br>…  …  …  …<br>K  K  K K<br>…<br>x1 x2 x3 xN<br><!-- End of picture text -->


<!-- Start of picture text -->
• Find path * that maximizes total joint probability P[ x,  ]<br>• P(x,) = a01 * Πi ei(xi)    aii+1<br>start  emission transition<br><!-- End of picture text -->

Slide credit: Serafim Batzoglou

28

## **Calculate maximum P(x,**  **) recursively**


<!-- Start of picture text -->
…<br>…<br>ajk  k  Vk(i)<br>hidden<br>Vj(i-1)  j<br>states<br>ek<br>…<br>observations  x i-1  x i<br>• Assume we know Vj for the previous time step (i-1)<br>• Calculate Vk(i) =     ek(xi)   *   maxj (   Vj(i-1)     ajk    )<br>current max  this emission  max ending  Transition<br>in state j at step i  from state j<br><!-- End of picture text -->

all possible previous states j

Slide credit: Serafim Batzoglou

29

## **The Viterbi Algorithm**


<!-- Start of picture text -->
State 1<br>2<br>Vk(i)<br>K<br><!-- End of picture text -->

x1   x2   x3 ………………………………………..xN

Input: x = x1……xN

**<u>Initialization:</u>**

V0(0)=1, Vk(0) = 0, for all k > 0

**<u>Iteration:</u>**

Vk(i) = eK(xi)  maxj ajk Vj(i-1)

**<u>Termination:</u>**

P(x, *) = maxk Vk(N)

**<u>Traceback:</u>**

Follow max pointers back Similar to aligning states to seq **<u>In practice:</u>**

Use log scores for computation **<u>Running time and space:</u>** Time:    O(K<sup>2</sup> N) Space:  O(KN)

Slide credit: Serafim Batzoglou

30

---

[← The six algorithmic settings for HMMs One path All paths](02-the-six-algorithmic-settings-for-hmms-one-path-all-paths.md) · [Up: contents](index.md) · [The six algorithmic settings for HMMs One path All paths →](04-the-six-algorithmic-settings-for-hmms-one-path-all-paths.md)
