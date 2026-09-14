---
title: P1 - Bayesian Networks (7 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# P1 - Bayesian Networks (7 points)

**Source:** `psets/04-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You are given two different Bayesian network structures 1 and 2, each consisting of 5 binary random variables A, B, C, D, E. Each variable corresponds to a gene, whose expression can be either “ON” or “OFF”.


**Network 1**


**Network 2**

**(A – 2 points)** In class, we covered the chain rule of probability for Bayes Nets, which allows us to factor the joint probability over all the variables into terms of conditional probabilities. For each of the following cases, factor P(A,B,C,D,E) according to the independencies specified and give the **minimum** number of parameters required to fully specify the distribution.

- (i) A,B,C,D,E are all mutually independent

   - P(A,B,C,D,E) = P(A)P(B)P(C)P(D)P(E)

   - 5 parameters (probability that each of the 5 genes is ON, independent of others)

- (ii) A,B,C,D,E follow the independence assumptions of **Network #1** above

   - P(A,B,C,D,E) = P(A)P(B)P(C|A)P(D|A,B)P(E|A,C,D)

   - 16 parameters: 1 for P(A), 1 for P(B), 2 for P(C|A), 4 for P(D|A,B), and 8 for

- P(E|A,C,D)

- (iii) A,B,C,D,E follow the independence assumptions of **Network #2** above

   - P(A,B,C,D,E) = P(A)P(B|A)P(C|A)P(D|A,B)P(E|D)

   - 11 parameters: 1 for P(A), 2 for P(B|A), 2 for P(C|A), 4 for P(D|A,B), 2 for P(E|D)

- (iv) no independencies

   - P(A,B,C,D,E) cannot be simplified

   - 2<sup>5</sup> - 1= 31 parameters (there are 32 combinations of A,B,C,D,E, must sum to 1)

2

**(B – 3 points)** Using **Network #2** and the probabilities given below, calculate the probability of the following: ⎧

---

[← Python Scripts](02-python-scripts.md) · [Up: contents](index.md) · [(i) P(A=ON, B=ON, C=ON, D=ON, E=ON) →](04-i-p-a-on-b-on-c-on-d-on-e-on.md)
