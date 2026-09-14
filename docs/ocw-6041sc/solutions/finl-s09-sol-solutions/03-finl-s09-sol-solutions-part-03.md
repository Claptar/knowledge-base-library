---
title: Finl s09 sol solutions Part 03 —
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/finl-s09-sol-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Finl s09 sol solutions Part 03 —

**Source:** `solutions/finl-s09-sol-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (c) (4 points.) If it is Spring today, will the chain converge to steady-state probabilities? If so, compute the steady-state probability for each state. If not, explain why these probabilities do not exist. Show your work.

Solution: The Markov chain will stay in the recurrent class {Sp, Su, B}, and


      -    πG = 0

      -

      - πF + πW + πG + πSp + πSu + πB = 1

   - ⇒ πF = 0, πW = 0, πG = 0, πSp = 1/5, πSu = 2/5, πB = 2/5.

- (d) (5 points.) If it is Fall today, what is the probability that Bitter Cold will never arrive in the future? Show your work.

Solution: Let aF and aW be the probabilities that Bitter Cold will never arrive starting from Fall and Winter, respectively. This is equivalent to the Markov chain ends up in G.


<!-- Start of picture text -->
⇒  aF = 3/4.<br><!-- End of picture text -->

14

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

- (e) (5 points.) If it is Fall today, what is the expected number of days till either Summer or Golden Sunshine arrives for the first time? Show your work.

Solution: Let µF and µW be expected number of days till either Summer or Golden Sunshine arrives for the first time, respectively.


15

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

Problem 7 (12 pts. total)

A newscast covering the final baseball game between Sed Rox and Y Nakee becomes noisy at the crucial moment when the viewers are informed whether Y Nakee won the game.

Let a be the parameter describing the actual outcome: a = 1 if Y Nakee won, a = −1 otherwise. There were n viewers listening to the telecast. Let Yi be the information received by viewer i (1 ≤ i ≤ n). Under the noisy telecast, Yi = a with probability p, and Yi = −a with probability 1 − p. Assume that the random variables Yi are independent of each other.

The viewers as a group come up with a joint estimator


(a) (6 points.) Find limn→∞ P(Zn = a) assuming that p > 0.5 and a = 1. Show your work.

Solution: Note that


(b) (6 points.) Find limn→∞ P(Zn = a), assuming that p = 0.5 and a = 1. Show your work.

Solution: Note that


16

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Finl s09 sol solutions Part 02 —](02-finl-s09-sol-solutions-part-02.md) · [Up: contents](index.md)
