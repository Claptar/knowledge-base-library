---
title: 2 Thompson sampling
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_14_Adaptive_Clinical_Trial_and_Reinforcement_Learning.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_14_Adaptive_Clinical_Trial_and_Reinforcement_Learning.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Thompson sampling

**Source:** [`notes/Lecture_14_Adaptive_Clinical_Trial_and_Reinforcement_Learning.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_14_Adaptive_Clinical_Trial_and_Reinforcement_Learning.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Thompson sampling is an algorithm for online decision problems where actions are taken sequentially in a manner that must balance between exploiting what is known to maximize immediate performance and investing to accumulate new information that may improve future performance.

Given we have developed some understanding of Bayesian Statistics. Let’s look into Thompson Sampling with a simple example. Suppose there are two treatments available to us. The first treatment _A_ has a success rate of _pA_ , and the second treatment _B_ has a success rate of _pB_ . Both rates are unknown, but are fixed overtime while patients are enrolling in the trial.

The medical practitioner has some prior belief about success rates and assume


Then, on the first day when the trial starts, there are _N_ 1 patients enrolled in the trial. For a patient _i_ , we sample


4

We assign the patient _i_ with the treatment that has a higher chance of “success:”


We observe the patient treatment assignments and associated outcomes, denoted as _{Yi, Di}_<sup>_N_</sup> _i_ =1<sup>1where</sup>


Therefore, the “observed rewards” for treatment _A_ and _B_ are defined the sum of patients who positively responded to the treatment:


The posterior distribution can then be updated:


From the second day onwards, we repeat the above procedure until the last day of trial enrolment. Notice here compared to the patients who arrive on the first day, second onwards-patients have a higher chance on average to receive the treatment that has a higher success rate.

Compared to the Greedy algorithm, from the second day onwards, there is no “randomness” introduced into the treatment assignment strategy. Because all patients who arrive on the second day are going to be assigned to the more successful treatment, in the sense that


Clearly, when the success treatment we identify at the first day singled out solely by chance, the second day patients are all enrolled in the wrong arm. This issue is quite intuitive: Think about choosing your favourite restaurant problem?

Although the above procedure serves our goal to maximize the patients welfare, but it brings in new issues in constructing valid confidence intervals in a frequentist sense. Think about the simple difference in mean estimator:


is this estimator still a “good” estimator? See Xu et al. (2013) for more discussion.

5

---

[← 1 Bayesian statistics](01-1-bayesian-statistics.md) · [Up: contents](index.md) · [References →](03-references.md)
