---
title: Messages flow up from leaves
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Messages flow up from leaves

• Each vertex waits for messages from all children before computing message to send to parents

• Variable nodes send product of messages from children

• Factor nodes with parent $x$ send the "summary" for $x$ of the product of the children's functions.

(a)
(b)

© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Kschischang, Frank R., Brendan J. Frey, et al. "Factor Graphs and the Sum-product Algorithm." Information Theory, IEEE Transactions on 47, no. 2 (2001): 498-519.

Kschischang, F.R.; Frey, B.J.; Loeliger, H.-A., "Factor graphs and the sum-product algorithm," 2001
http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=910572&isnumber=19638

---

## Belief propagation:

An algorithm known as "Sum-Product" can be used to simultaneously compute **all** marginals!

See citation for details

$\mu_{h_1 \to x}(x)$

$\mu_{x \to f}(x)$

$\mu_{f \to x}(x)$

$\mu_{y_1 \to f}(y_1)$

$n(f) \setminus \{x\}$

$\bar{n}(x) \setminus \{f\}$

© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Kschischang, Frank R., Brendan J. Frey, et al. "Factor Graphs and the Sum-product Algorithm." Information Theory, IEEE Transactions on 47, no. 2 (2001): 498-519.

Kschischang, F.R.; Frey, B.J.; Loeliger, H.-A., "Factor graphs and the sum-product algorithm," 2001
http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=910572&isnumber=19638

---

## Factor graphs in PARADIGM

Variable node, $x$:
three states:
1 activated
0 nominal
-1 deactivated

Factor node, $f$

Edge exists iff $x$ is an argument of $f$

Factor graph

---

## A

* Transcriptional Regulation
* Translational Regulation, Protein Degradation
* Intracellular and Extracellular Signaling

GeneCopy Number $\to$ Expression State $\to$ Protein Level $\to$ Protein Activity

Array CGH, SNP chips $\to$ GeneCopy Number

Transcriptomics $\to$ Expression State

Variable (ellipse)
Factor - interaction term (black square)

Courtesy of Vaske et al. License: CC-BY.
Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

Vaske C J et al. Bioinformatics 2010;26:i237-i245
© The Author(s) 2010. Published by Oxford University Press.

---

## Transcriptional Regulation

Protein $\to$ Activity $\to$ mRNA $\leftarrow$ DNA
Activity $\to$ Protein

## Formation of Complex

Protein, Protein $\to$ Activity, Activity $\to$ AND-like connection $\to$ Complex

## Protein Activation

Protein $\to$ Activity
mRNA $\to$ Protein $\to$ Activity

## Gene Family

Protein, Protein $\to$ Activity, Activity $\to$ OR-like connection $\to$ Gene Family

Courtesy of Vaske et al. License: CC-BY.
Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

Vaske C J et al. Bioinformatics 2010;26:i237-i245
© The Author(s) 2010. Published by Oxford University Press.

---

---

[Up: contents](index.md) · [MDM2 / TP53 / Apoptosis →](02-mdm2-tp53-apoptosis.md)
