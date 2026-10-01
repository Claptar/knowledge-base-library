---
title: Methods
source: https://doi.org/10.64898/2026.03.04.709349/
source_file: sources/papers/caskey-rich-2026-cellsweep/caskey-rich-2026-cellsweep.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `caskey-rich-2026-cellsweep.pdf` from [papers/caskey-rich-2026-cellsweep](https://doi.org/10.64898/2026.03.04.709349/) — papers · caskey-rich-2026-cellsweep, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Methods

Given a barcode by feature count matrix, the CellSweep mixture model includes parameters for
cell-type expression, ambient contamination, and bulk contamination, in a fully generative
framework. Each barcode $i$ produces a count vector

$$\boldsymbol{C}_i = (C_{i,1},\ldots,C_{i,G}), \qquad (4)$$

with total counts $T_i = \sum_g \boldsymbol{C}_{i,g}$. Conditional on its total count, we assume
that

$$\boldsymbol{C}_i \sim \text{Multinomial}(T_i, \chi_i), \qquad (5)$$

where $\chi_i \in \mathbb{R}_+^G$ represents the expected normalized feature expression profile of
barcode $i$.

**Mixture Composition.** We model $\chi_i$ as a convex combination of three biologically
interpretable sources:

$$\chi_i = (1-\beta)\left[\alpha_i \boldsymbol{a} + (1-\alpha_i)\sum_{k=1}^{K}\gamma_i^k
\boldsymbol{p}^k\right] + \beta \boldsymbol{m}. \qquad (6)$$

Equivalently,

$$\chi_i = \sum_{k=1}^{K} \chi_i^{(P_k)} + \chi_i^{(A)} + \chi_i^{(M)} \qquad (7)$$

where,

- $\chi_i^{(P_k)} = (1-\beta)(1-\alpha_i)\gamma_i^k \boldsymbol{p}^k$ is the contribution from
  cell-type $k$;
- $\chi_i^{(A)} = (1-\beta)\alpha_i \boldsymbol{a}$ is the contribution from ambient
  contamination;
- $\chi_i^{(M)} = \beta \boldsymbol{m}$ is the contribution from bulk contamination.

Here,

- $\boldsymbol{a} \in \mathbb{R}^G$ is the ambient contamination profile, representing molecular
  contamination from lysed cells/nuclei;
- $\boldsymbol{m} \in \mathbb{R}^G$ is the bulk contamination profile, representing contamination
  introduced after pooling (i.e barcode-swapping and PCR chimeras);
- $\boldsymbol{p}^k \in \mathbb{R}^G$ is the expected expression profile of cell-type $k$;
- $\gamma_i \in \{0,1\}^K$ is the one-hot cell-type membership vector for barcode $i$, where
  $\gamma_i^k = 1$ if barcode $i$ is assigned to cell-type $k$ and $\gamma_i^k = 0$ otherwise;
- $\alpha_i \in [0,1]$ is the fraction of ambient RNA in barcode $i$;
- $\beta \in [0,1]$ is the global bulk contamination fraction.

Each component profile $\boldsymbol{a}, \boldsymbol{m}, \boldsymbol{p}^k$ is normalized such that
$\sum_g \boldsymbol{a}_g = \sum_g \boldsymbol{m}_g = \sum_g \boldsymbol{p}_g^k = 1$. The mixture
weights $\alpha_i$, $\beta$, and $\gamma_i$ thus represent true proportions and ensure that
$\chi_i$ itself is a valid probability vector.

Intuitively, this expression assumes that:

1. Barcode-specific contamination is governed by $\alpha_i$ (ambient RNA fraction);
2. Global contamination is governed by $\beta$ (bulk library noise);
3. The biological cell signal is governed by an underlying cell-type profile indicated by
   $\gamma_i$.

Together, these terms yield an interpretable and flexible mixture model.

**Modeling Assumptions.** The model relies on the following assumptions:

- **Multinomial sampling:** Given the total UMI count $T_i$, counts across genes follow a
  multinomial distribution with probabilities $\chi_i$. This ignores overdispersion but provides
  a tractable and empirically accurate approximation for large counts.
- **Linear mixing:** Counts from cell, ambient, and bulk sources combine additively prior to
  normalization. This reflects the physical mixture of molecules before UMI counting.
- **Fixed number of cell-types:** The dataset contains $K$ latent cell-type expression profiles
  $\{\boldsymbol{p}^k\}$, which are shared across barcodes.
- **Barcode independence:** Each barcode is modeled independently given global parameters
  $(\boldsymbol{a}, \boldsymbol{m}, \{\boldsymbol{p}^k\}, \beta)$.

---

[← Discussion](04-discussion.md) · [Up: contents](index.md) · [Initial Parameter Estimates →](06-initial-parameter-estimates.md)
