---
title: Problem 2. Library Complexity (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 2. Library Complexity (5 points)

**Source:** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Imagine you are responsible for sequencing DNA samples for your lab's latest important experiment. Using extensive simulations, you know that you need to observe at least 12 million unique molecules in order to test your current hypothesis. From previous experience, you know that each time a DNA library is constructed from a sample, it will contain exactly 40 million unique molecules (selected perfectly at random). You also know that C. elegans, your model organism, has a genome size of approximately 100 million base pairs.

You can have your sample sequenced in units called lanes. Each lane gives you 10 million reads, and a library can be sequenced on as many lanes as you want. However, ever-protective of your grant money, you want to achieve your experimental goals in the most efficient way possible. Suppose that each sample collection and library preparation step costs $500 and that each sequencing lane costs $1000.

- **(A) (2 pt.)** Assume that each molecule in the library had equal probability of being sequenced. What is the most cost-effective experimental design (number of libraries and lanes sequenced for each library) for achieving your goal of observing 12 million unique molecules? Show your work.

3

- **(B) (3 pt.)** Now suppose that there is variation in the selection probabilities across each molecule, which follows a negative binomial distribution with rate lambda = 0.25 (10 million reads divided by 40 million molecules) and variance factor k = 2 (estimated from previous experiments). What is the most cost-effective experimental design for this situation? Show your work and comment on any differences between the two cases.

_Hint_ : A more common formulation of the negative binomial distribution is in terms of failures n and a success probability p. This conversion is found in the lecture slides.

---

[← 02 questions pset2 ques Part 03 —](03-02-questions-pset2-ques-part-03.md) · [Up: contents](index.md) · [Problem 3. Differential gene expression (4 points) →](05-problem-3-differential-gene-expression-4-points.md)
