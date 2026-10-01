---
title: 7 Discussion
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 7 Discussion

In spite of the indistinguishability of negative binomial distributions produced by intrinsic and
extrinsic noise, the behavior of downstream processed gene products is substantially divergent.
Specifically, we report inequality between the two models' lower moments. Even given identical
nascent marginals, it is impossible to produce identical mature marginals, and by extension full
joint distributions, using the two models. More dramatically, it is impossible for the solutions'
mature marginals even to share more than one low-order moment.

In practice, if experimental joint or marginal copy-number distributions are available, it is
possible to use relative likelihood testing to choose the better-fitting model. The relevant test
statistic is $\lambda = \frac{\mathcal{L}_i(\hat{\Theta}_i)}{\mathcal{L}_e(\hat{\Theta}_e)}$, where
$\mathcal{L}_z(\hat{\Theta}_z)$, $z \in \{i,e\}$ is the value of the likelihood function of the
intrinsic or extrinsic model at the maximum likelihood joint parameter estimate. No closed-form
joint maximum likelihood estimators are available for either model; however, estimation by
numerical optimization is straightforward, especially starting at the moment-based estimates
reported above. The two models' qualitative behaviors are illustrated in Figure 2. We use the
Gillespie algorithm [47] to simulate both systems given identical nascent distributions ($r=1.8$,
$p=\frac{12}{13}$) and downstream processing rates ($\beta=0.5$, $\gamma=0.4$). The solutions are
dramatically different. As expected from the analytical moments, the extrinsic noise model gives a
much more correlated joint distribution. However, despite identical marginal mature expectations,
the extrinsic model has a longer tail, yielding a higher variance for that species. This drastic
disagreement between distributions confirms that multimodal data is sufficient to distinguish
between the two hypothesized sources of stochasticity. In addition to the theoretical and
qualitative results, we provide simulation routines for both noise models. Furthermore, to
facilitate comparison with discrete copy-number data, we report analytical marginal and joint
distributions implied by the formulation of the system with extrinsic noise; their agreement with
the simulation is shown in Figure 2. These distributions, along with moment-based initial parameter
estimates, can be directly used for inference and hypothesis testing against other models.

Given the modeling-based insight into model identifiability, we suggest that multimodal data
collection presents a valuable route to the identification of noise models. Specifically, we
anticipate increased relevance for single-cell RNA sequencing, which has been challenging to
integrate with experimental controls for the noise sources. Therefore, we suggest that experimental
improvements in the detection of the nascent transcriptome, as well as theoretical improvements in
the modeling of technical noise, would allow identification of sources of biological stochasticity
on a genome-wide scale. Finally, the discrete modeling framework we discuss is immediately
interpretable in terms of biophysical parameters.

**Figure 2:** (a-c) Distributions for the intrinsic noise model with $b=12$, $k_i=0.9$, $\beta=0.5$,
and $\gamma=0.4$, generated using $10^4$ simulations. (a) Nascent marginal (gray region: copy-number
histogram; orange line: analytical solution). (b) Mature marginal (gray region: copy-number
histogram; orange line: analytical solution). (c) Joint distribution (points: cells; color:
$\log_{10}$ analytical solution, lighter color corresponds to higher probability mass). (d-f)
Distributions for the extrinsic noise model with $\alpha = k_i\beta^{-1}$, $\eta = (b\beta)^{-1}$,
$\beta=0.5$, and $\gamma=0.4$, generated using $10^4$ simulations. (d) Nascent marginal (gray
region: copy-number histogram; orange line: analytical solution). (e) Mature marginal (gray region:
copy-number histogram; orange line: analytical solution). (f) Joint distribution (points: cells;
color: $\log_{10}$ analytical solution, lighter color corresponds to higher probability mass).

## 8 Code Availability

MATLAB and Python code that can be used to reproduce Figure 2, including the simulation and
plotting routines, is available at https://github.com/pachterlab/GP_2020_2.

## 9 Acknowledgments

The DNA, pre-mRNA, and mature mRNA illustrations used in Figure 1, modified from [20], are
derivatives of the DNA Twemoji by Twitter, Inc., used under CC-BY 4.0. G.G. and L.P. are partially
funded by NIH U19MH114830.

---

[← 6 Experimental opportunities and limitations](06-6-experimental-opportunities-and-limitations.md) · [Up: contents](index.md) · [References →](08-references.md)
