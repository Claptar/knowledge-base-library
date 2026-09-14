---
title: Factor graphs in PARADIGM
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Factor graphs in PARADIGM

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Variable node, _x:_ three states: 1 activated 0 nominal -1 deactivated


<!-- Start of picture text -->
x3<br>f<br>x1 x2<br><!-- End of picture text -->

Factor graph

Factor node, _f_

Edge exists iff x is an argument of f


Courtesy of Vaske et al. License: CC-BY.

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

**Vaske C J et al. Bioinformatics 2010;26:i237-i245**


© The Author(s) 2010. Published by Oxford University Press.


Courtesy of Vaske et al. License: CC-BY. Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

###### **Vaske C J et al. Bioinformatics 2010;26:i237-i245**


© The Author(s) 2010. Published by Oxford University Press.


Courtesy of Vaske et al. License: CC-BY. Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

**Vaske C J et al. Bioinformatics 2010;26:i237-i245**


© The Author(s) 2010. Published by Oxford University Press.


Courtesy of Vaske et al. License: CC-BY.

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

- Goal:

   - Estimate probability that pathways are active

   - Use log likelihood ratio


Parameters estimated by EM from experimental data

**Vaske C J et al. Bioinformatics 2010;26:i237-i245**

Manually constructed Known pathways:


- •Convert to a directed graph •Each edge is labeled as either positive or negative based on influence

- •Define joint probability


Courtesy of Vaske et al. License: CC-BY. Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

###### Defining joint probability


Courtesy of Vaske et al. License: CC-BY. Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

**Expected state:**

- •Majority vote of parent variables

- •If a parent is connected by a positive edge it contributes a vote of +1 times its own state to the value of the factor.

- •If the parent is connected by a negative edge, then the variable votes −1 times its own state.

ϵ was set to 0.001

###### Defining factors manually


###### ϵ was set to 0.001

Courtesy of Vaske et al. License: CC-BY. Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

- Logic:

- •AND: The variables connected to _xi_ by an edge labeled ‘minimum’ get a single vote, and that vote's value is the minimum value of these variables

- •OR: The variables connected to _xi_ by an edge labeled ‘maximum’ get a single vote, and that vote's value is the maximum value of these variables, creating an OR-like connection.

- •Votes of zero are treated as abstained votes.

- •If there are no votes the expected state is zero. Otherwise, the majority vote is the expected state, and a tie between 1 and −1 results in an expected state of −1 to give more importance to repressors and deletions.

###### Defining factors manually

ϵ was set to 0.001

###### Logic:

•AND: The variables connected to _xi_ by an edge labeled ‘minimum’ get a single vote, and that vote's value is the minimum value of these variables


Courtesy of Vaske et al. License: CC-BY. Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." _Bioinformatics_ 26, no. 12 (2010): i237-i45.

•OR: The variables connected to _xi_ by an edge labeled ‘maximum’ get a single vote, and that vote's value is the maximum value of these variables, creating an OR-like connection.

Compared to Bayesian networks, factor graphs provide an more intuitive way to represent these regulatory steps

---

[← In our setting](06-in-our-setting.md) · [Up: contents](index.md) · [Joint probability of graph →](08-joint-probability-of-graph.md)
