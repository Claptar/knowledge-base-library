---
title: Initial Parameter Estimates
source: https://doi.org/10.64898/2026.03.04.709349/
source_file: sources/papers/caskey-rich-2026-cellsweep/caskey-rich-2026-cellsweep.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `caskey-rich-2026-cellsweep.pdf` from [papers/caskey-rich-2026-cellsweep](https://doi.org/10.64898/2026.03.04.709349/) — papers · caskey-rich-2026-cellsweep, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Initial Parameter Estimates

**Ambient Profile.** In high-throughput single-cell assays, a large fraction of recovered
barcodes are non-cellular, yet are nonetheless associated with small numbers of molecules
originating from the ambient pool. Because the feature counts for these non-cellular barcodes
originate solely from ambient contamination, these barcodes' feature expression composition
provides an unbiased estimate of the global ambient profile. For these technologies, we estimate
the ambient distribution as the normalized average of counts across all barcodes identified as
empty:

$$\boldsymbol{a}_g = \frac{\sum_e \boldsymbol{C}_{e,g}}{\sum_e \sum_{g'} \boldsymbol{C}_{e,g'}},
\qquad (8)$$

where $e$ indexes the non-cellular barcodes.

Under the assumption that non-cellular barcodes sample independently from a shared ambient pool,
this estimator corresponds to the maximum likelihood estimate of $\boldsymbol{a}$ under a
multinomial sampling model, and is highly stable due to the large number of non-cellular barcodes
typically observed.

**Bulk Contamination Profile.** Across all technologies, a small fraction of global contamination
can arise after pooling during library preparation and amplification. This contamination affects
all barcodes approximately uniformly and can be modeled by a shared background profile
$\boldsymbol{m}$. Because this background reflects the aggregate expression composition of the
entire experiment, we approximate $\boldsymbol{m}$ as the normalized mean expression profile
across all droplets:

$$\boldsymbol{m}_g = \frac{\sum_i \boldsymbol{C}_{i,g}}{\sum_i \sum_{g'} \boldsymbol{C}_{i,g'}}.
\qquad (9)$$

This estimator corresponds to the maximum likelihood estimate of the global background under a
multinomial sampling model and provides a stable initialization for subsequent inference. In
principle, an even more accurate estimate of $\boldsymbol{m}$ could be obtained from molecule
counts prior to barcode collapsing, as bulk contamination is introduced during library preparation
and amplification. However, such information is typically unavailable in standard scRNA-seq
outputs, making the collapsed-count estimator a practical and robust approximation.

**Cell Typing.** The number of cell-types $K$ is specified or estimated from an initial clustering
of the normalized count matrix. The cell-type assignment for each droplet is indicated by the
one-hot cell membership vector $\gamma_i$.

---

[← Methods](05-methods.md) · [Up: contents](index.md) · [Inference via Expectation–Maximization →](07-inference-via-expectation-maximization.md)
