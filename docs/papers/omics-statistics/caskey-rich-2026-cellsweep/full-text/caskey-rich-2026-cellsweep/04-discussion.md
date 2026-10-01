---
title: Discussion
source: https://doi.org/10.64898/2026.03.04.709349/
source_file: sources/papers/caskey-rich-2026-cellsweep/caskey-rich-2026-cellsweep.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `caskey-rich-2026-cellsweep.pdf` from [papers/caskey-rich-2026-cellsweep](https://doi.org/10.64898/2026.03.04.709349/) — papers · caskey-rich-2026-cellsweep, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Discussion

Ambient and bulk contamination systematically distort scRNA-seq measurements and can compromise
biological interpretation. Existing correction strategies often trade modeling rigor for
computational efficiency, leaving a gap between deep generative approaches and lightweight
heuristic methods. CellSweep bridges this gap by providing a fast, interpretable generative
framework for routine decontamination.

CellSweep adopts an explicit probabilistic model whose parameters correspond directly to
biologically meaningful quantities. Inference proceeds via the EM algorithm over mixture
components representing cell-type expression, ambient RNA, and global bulk contamination. Unlike
deep generative models such as CellBender and scAR, which rely on neural networks and variational
inference, CellSweep performs direct likelihood-based optimization. This formulation provides
both interpretability and substantial computational advantages: CellSweep runs in minutes on a
CPU for typical datasets and requires no specialized hardware.

Beyond denoising, CellSweep provides a per-cell estimate of ambient contamination, $\hat\alpha_i$,
which serves as a quantitative indicator of cell quality. In practice, this metric identifies
low-quality or noisy cells and clusters not reliably detected by conventional filtering heuristics
such as UMI thresholds or mitochondrial content. Owing to its speed, minimal hyperparameter tuning
required, and low sensitivity to initialization choices, CellSweep can be applied robustly across
diverse datasets with minimal user intervention. These properties support treating ambient and
bulk correction as a routine preprocessing step rather than a specialized adjustment.

Across a range of technologies, species, cell counts, and experimental conditions—including
droplet-based, well-based, spatial, and single-nucleus datasets—CellSweep consistently improved
marker specificity and reduced cross-sample contamination. Sensitivity analyses demonstrated
robustness to clustering resolution, noncellular barcode identification strategy, and subsampling
of noncellular barcodes (Fig. S9-11). Even under aggressive subsampling, results remained stable
until ~10,000 noncellular barcodes, supporting the practical reliability of the method across
preprocessing pipelines (Fig. S11). If a dataset has fewer than ~10,000 noncellular barcodes, we
recommend using our alternative CellSweep model instead.

Future directions include both methodological extensions and downstream applications. On the
modeling side, incorporating doublet detection directly into the generative framework would
enable joint inference of contamination and multiplet structure, particularly in dense
droplet-based experiments. Further improvements to the alternative ambient-learning regime to
recover idempotency and increase statistical power will enhance robustness on datasets lacking
non-cellular barcodes.

An especially important direction is the systematic study of how ambient and bulk decontamination
influence downstream machine learning models. Large-scale single-cell atlases are increasingly
used to train foundation models, representation learning frameworks, and predictive classifiers.
Because these models are sensitive to structured noise, ambient contamination may be implicitly
encoded in learned embeddings, decision boundaries, and inferred regulatory programs. Applying
CellSweep prior to model training provides an opportunity to quantify how removing structured
technical signal alters learned representations, improves predictive performance, and enhances
biological interpretability. Ongoing work in our group focuses on retraining and benchmarking
machine learning models on CellSweep-processed datasets to assess the extent to which
decontamination changes model behavior at scale.

Together, these directions position CellSweep not only as a preprocessing tool, but as a
foundation for more reliable statistical and machine learning analyses of single-cell data.

In summary, CellSweep provides a fast, interpretable, and broadly applicable solution for
separating biological signal from structured technical noise in single-cell data. As datasets
continue to grow in size and complexity, methods that combine statistical transparency with
computational efficiency will be essential, and CellSweep offers a practical foundation for this
goal.

## Data Availability

- hgmm_12k: 10x hgmm_12k
- kidney_nuclei_10k: 10x Kidney Nuclei 10k
- pbmc_mouse_5k: 10x Mouse PBMC 5k
- pbmc8k: 10x PBMC 8k
- pbmc33k: 10x PBMC 33k
- melanoma: 10x Melanoma 10k
- 8-cubed founder strains (Rebboah et al., 2026): IGVF 8-Cubed SPLiT-seq
- ATAC-seq: 10x ATAC Mixture
- Smart-seq2: GSE132044 (GEO)

## Code Availability

The CellSweep Python package is available at https://github.com/pachterlab/cellsweep, along with
notebooks to reproduce all analysis in this study.

## Author Contributions

Conceptualization, I.H., motivated by observations of R.W. and A.M. Methodology, M.C., J.R., L.P.,
and I.H. Investigation, L.P. and I.H. Visualization, M.C., J.R., L.P., and I.H. Funding
acquisition, A.M., L.P., and I.H. Project administration and supervision, L.P. and I.H.
Writing—original draft, M.C. and J.R. Writing—review and editing, M.C., J.R., R.W., A.M., L.P.,
and I.H.

| Metric | CellBender | DecontX | scAR | SoupX | CellSweep |
| --- | --- | --- | --- | --- | --- |
| Human-Mouse denoising | ✓ | X | ✓ | X | ✓ |
| PBMC Marker Cleanup (dotplots) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Idempotent | X | ✓ | ✓ | ✓ | ✓ |
| Runtime on CPU (min) | 180 | 3 | 200 | 2 | 1 |
| Simulation PPV | 0.985 | 0.981 | 0.686 | 0.980 | 0.981 |
| Doesn't predict bigger counts | ✓ | ✓ | X | ✓ | ✓ |

**Table 1.** Comparison of scRNA-seq denoising tools.

## Acknowledgments

We thank the Pachter Lab for helpful feedback at the start of the project. The project was funded
by the Caltech Bioinformatics Resource Center (CBRC) and the Impact of Genomic Variation on
Function (IGVF) Consortium under award number UM1HG012077. Thanks to the CBRC and the IGVF
consortium for financial and resource support for this project.

---

[← Results](03-results.md) · [Up: contents](index.md) · [Methods →](05-methods.md)
