---
title: P2 – Analysis of Chromatin Structure (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/05-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P2 – Analysis of Chromatin Structure (5 points)

**(A)** Suppose we reduced the number of Segway states to be fewer than the true number of distinct patterns of chromatin marks. How might the resulting labels under this model be different?
As we are attempting to model the same data using fewer labels, we might expect that labels with similar chromatin mark profiles would be merged.

**(B)** The $C$, $M$, $t$, and $J$ variables in the Segway model implement a 'countdown' function, one of the core features of Segway. How might these countdown variables improve on a simple HMM model in modeling the underlying genomic states?
A traditional HMM doesn't allow tuning for state duration. In the case where we train with a large number of labels, we might expect results to incomprehensible with frequent switching between states. The countdown variables allow us to enforce our beliefs on how long a segment should be – such as allowing a long minimum segment length.

Suppose we remove the $C$, $M$, $t$, and $J$ countdown variables from the Segway model for the remainder of this problem.

**(C)** Draw the resulting graphical model.

**(D)** Assuming that $J$ is a binary variable that either forces the label to change or prevents it from changing and we allow for 50 segment labels, describe how the conditional probability table for the segment label variables has changed between the old model and this new model in terms of the number of parameters.
Previously, Q_t (the segment label variable) was dependent on J_t and Q_t-1. As a result, the conditional probability table could be viewed as consisting of $2*50-2 = 98$ parameters (normalize along each 'row' of the conditional probability table).

However, due to the nature of J_t, we can be more specific. If $J_t = 0$ (we prevent a label change), we know that the entry for Q_t-1 will be 1 and all the remaining entries will be 0. Likewise, if $J_t = 1$ (we force a label change), we know that the entry for Q_t-1 will be 0 and the remaining entries must sum to 1 giving 48 parameters for this row.

Now, with the dependence on J_t removed, the table only consists of $50-1 = 49$ parameters – that is, it only depends on the previous state. Many students said the number of parameters was halved, which was also accepted.

Furthermore, some students also considered the fact that there must be one such table for each of the 50 possible values $Q$ can take on, whereas the above analysis basically assumes $Q$ is a binary variable.

**(E)** Which other core feature of the Segway model does this new model retain that is not present in a simple HMM model?
We still retain the observed variable which indicates whether data at a time point is defined or undefined. As a result, we still retain the ability to handle missing data.

---

[← P1 – Network Statistics (10 points)](01-p1-network-statistics-10-points.md) · [Up: contents](index.md) · [P3 – Heritability (5 points) →](03-p3-heritability-5-points.md)
