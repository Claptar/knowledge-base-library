---
title: MDM2 / TP53 / Apoptosis
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# MDM2 / TP53 / Apoptosis

MDM2 $\to$ TP53 $\to$ Apoptosis

MDM2: DNA $\to$ mRNA $\to$ Protein $\to$ Active Protein
TP53: DNA $\to$ mRNA $\to$ Protein $\to$ Active Protein $\to$ Apoptosis

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

Vaske C J et al. Bioinformatics 2010;26:i237-i245
© The Author(s) 2010. Published by Oxford University Press.

---

Copy Number Alterations
Gene Expression
Sample 1
Sample 2
Sample 3

• Goal:
– Estimate probability that pathways are active
– Use log likelihood ratio

$$L(i,a) = \log\left(\frac{P(D, x_i = a \mid \Phi)}{P(D, x_i \ne a \mid \Phi)}\right) - \log\left(\frac{P(x_i = a \mid \Phi)}{P(x_i \ne a \mid \Phi)}\right)$$
$$= \log\left(\frac{P(D \mid x_i = a, \Phi)}{P(D \mid x_i \ne a, \Phi)}\right).$$

Parameters estimated by EM from experimental data

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.
Vaske C J et al. Bioinformatics 2010;26:i237-i245

---

## Manually constructed

Known pathways:
• Convert to a directed graph
• Each edge is labeled as either positive or negative based on influence
• Define joint probability

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

---

## Defining joint probability

### Expected state:
• Majority vote of parent variables
• If a parent is connected by a positive edge it contributes a vote of +1 times its own state to the value of the factor.
• If the parent is connected by a negative edge, then the variable votes -1 times its own state.

$$\phi_i(x_i, \text{Parents}(x_i)) = \begin{cases} 1 - \epsilon & x_i \text{ is the expected state from Parents}(x_i) \\ \frac{\epsilon}{2} & \text{otherwise.} \end{cases}$$

$\epsilon$ was set to 0.001

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

---

## Defining factors manually

$$\phi_i(x_i, \text{Parents}(x_i)) = \begin{cases} 1 - \epsilon & x_i \text{ is the expected state from Parents}(x_i) \\ \frac{\epsilon}{2} & \text{otherwise.} \end{cases}$$

$\epsilon$ was set to 0.001

Logic:
• AND: The variables connected to $x_i$ by an edge labeled 'minimum' get a single vote, and that vote's value is the minimum value of these variables
• OR: The variables connected to $x_i$ by an edge labeled 'maximum' get a single vote, and that vote's value is the maximum value of these variables, creating an OR-like connection.
• Votes of zero are treated as abstained votes.
• If there are no votes the expected state is zero. Otherwise, the majority vote is the expected state, and a tie between 1 and -1 results in an expected state of -1 to give more importance to repressors and deletions.

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

---

## Defining factors manually

$$\phi_i(x_i, \text{Parents}(x_i)) = \begin{cases} 1 - \epsilon & x_i \text{ is the expected state from Parents}(x_i) \\ \frac{\epsilon}{2} & \text{otherwise.} \end{cases}$$

$\epsilon$ was set to 0.001

Logic:
• AND: The variables connected to $x_i$ by an edge labeled 'minimum' get a single vote, and that vote's value is the minimum value of these variables
• OR: The variables connected to $x_i$ by an edge labeled 'maximum' get a single vote, and that vote's value is the maximum value of these variables, creating an OR-like connection.

Compared to Bayesian networks, factor graphs provide an more intuitive way to represent these regulatory steps

Source: Vaske, Charles J., Stephen C. Benz, et al. "Inference of Patient-specific Pathway Activities from Multi-dimensional Cancer Genomics Data Using PARADIGM." Bioinformatics 26, no. 12 (2010): i237-i45.

---

## Joint probability of graph

$$\phi_i(x_i, \text{Parents}(x_i)) = \begin{cases} 1 - \epsilon & x_i \text{ is the expected state from Parents}(x_i) \\ \frac{\epsilon}{2} & \text{otherwise.} \end{cases}$$

$$P(X) = \frac{1}{Z} \prod_{j=1}^m \phi_j(X_j), \quad \longleftarrow \text{Product over all } m \text{ factors } \phi_j$$

$$Z = \prod_j \sum_{S \sqsubseteq X_j} \phi_j(S)$$

$S \sqsubseteq X \quad \text{Setting of variables = possible values}$

---

## Marginal

$$P(x_i = a \mid \Phi) = \frac{1}{Z} \prod_{j=1}^m \sum_{S \sqsubseteq A_i(a) X_j} \phi_j(S)$$

$\{S \sqsubseteq_D X\}$ Set of all possible assignments to the variables $X$ consistent with data $D$

$A_i(a)$ represents the singleton assignment set $\{x_i = a\}$
$\Phi$ Full specified factor graph

## Likelihood

$$P(x_i = a, D \mid \Phi) = \frac{1}{Z} \prod_{j=1}^m \sum_{S \sqsubseteq A_i(a) \cup D X_j} \phi_j(S)$$

---

---

[← Messages flow up from leaves](01-messages-flow-up-from-leaves.md) · [Up: contents](index.md) · [A →](03-a.md)
