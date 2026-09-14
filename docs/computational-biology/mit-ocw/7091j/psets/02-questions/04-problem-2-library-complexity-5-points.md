---
title: Problem 2. Library Complexity (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 2. Library Complexity (5 points)

**Source:** `psets/02-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Imagine you are responsible for sequencing DNA samples for your lab's latest important experiment. Using extensive simulations, you know that you need to observe at least 12 million unique molecules in order to test your current hypothesis. From previous experience, you know that each time a DNA library is constructed from a sample, it will contain exactly 40 million unique molecules (selected perfectly at random). You also know that C. elegans, your model organism, has a genome size of approximately 100 million base pairs.

You can have your sample sequenced in units called lanes. Each lane gives you 10 million reads, and a library can be sequenced on as many lanes as you want. However, ever-protective of your grant money, you want to achieve your experimental goals in the most efficient way possible. Suppose that each sample collection and library preparation step costs $500 and that each sequencing lane costs $1000.

- **(A) (2 pt.)** Assume that each molecule in the library had equal probability of being sequenced. What is the most cost-effective experimental design (number of libraries and lanes sequenced for each library) for achieving your goal of observing 12 million unique molecules? Show your work.

Consider one library.  Compute M = K(L)*C = (1-exp(-N/40M))*40M. One lane: 8.8M unique reads ($1500)     (1-poisspdf(0,.25))*40 ** Two lanes: 15.7M unique reads ($2500)     (1-poisspdf(0,.5))*40 Consider two libraries:

When considering the 2<sup>nd</sup> library, all calculations for the number of unique reads within the 2<sup>nd</sup> library are the same (the same number of reads are coming off the sequencer and the average coverage L for these reads is the same). However, we only add 60% of them to the unique reads from the 1<sup>st</sup> library to get the total unique reads over both libraries since on average 40% of the reads in the 2<sup>nd</sup> library will have already been covered by the 1<sup>st</sup> library. Therefore: One lane each: 8.8M unique reads from first library, 8.8M*0.6=5.3M from second = 14.1M ($3000)

Two lanes from 1<sup>st</sup> library, one lane from the 2<sup>nd</sup> : too expensive - ($4000)

4

- **(B) (3 pt.)** Now suppose that there is variation in the selection probabilities across each molecule, which follows a negative binomial distribution with rate lambda = 0.25 (10 million reads divided by 40 million molecules) and variance factor k = 2 (estimated from previous experiments). What is the most cost-effective experimental design for this situation? Show your work and comment on any differences between the two cases.

_Hint_ : A more common formulation of the negative binomial distribution is in terms of failures n and a success probability p. This conversion is found in the lecture slides.

Same as (A) but we compute K(L) with the NB distribution. We know that p=L/(L + 1/k) and vary L with the number of lanes. Note: if using the Matlab or Mathematica implementations of the NegBin, you should actually use 1- _p_ if calculating _p_ as mentioned in lecture.

One library:

($1500) One lane: 7.34M unique reads (1-nbinpdf(0,0.5,2/3))*40 ($2500) Two lanes: 11.7M unique reads (1-nbinpdf(0,0.5,0.5))*40 *($3500) Three lanes: 14.7M unique reads (1-nbinpdf(0,0.5,0.4))*40

Two libraries:

($3000) One lane each: 7.34M + 4.4M = 11.74M unique reads (not enough) First library: 7.34M unique reads as above Second library: 4.4M unique reads   (1-nbinpdf(0,0.5,2/3))*40*0.6 Two lanes (one library) then one (second library): over 12 million unique reads but too expensive

---

[← 02 questions Part 03 —](03-02-questions-part-03.md) · [Up: contents](index.md) · [Problem 3. Differential gene expression (4 points) →](05-problem-3-differential-gene-expression-4-points.md)
