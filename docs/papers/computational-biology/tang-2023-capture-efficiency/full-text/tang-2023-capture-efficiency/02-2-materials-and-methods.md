---
title: 2 Materials and Methods
source: https://doi.org/10.1093/bioinformatics/btad395/
source_file: sources/papers/tang-2023-capture-efficiency/tang-2023-capture-efficiency.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `tang-2023-capture-efficiency.jats` from [papers/tang-2023-capture-efficiency](https://doi.org/10.1093/bioinformatics/btad395/) — papers · tang-2023-capture-efficiency, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Materials and Methods

## 2.1 Theory and model {#sec6}

The classical model for stochastic gene expression is the so-called telegraph model (Fig. 1a). It is known that the chemical master equation of the telegraph model results in a Beta-Poisson distribution for the mRNA at steady state (Peccoud and Ycart 1995, Raj *et al.* 2006, Iyer-Biswas *et al.* 2009).

![](https://doi.org/10.1093/bioinformatics/btad395/)

![](https://doi.org/10.1093/bioinformatics/btad395/)

Model of stochastic gene expression and the effect of the cell size and sequencing capture efficiency on observed transcript count distributions. (a) An illustration of the telegraph model of stochastic gene expression and its associated parameters. The gene switches between an inactive and active state, and mRNAs are transcribed only from the active state. (b) Illustration of downsampling in scRNA-seq with a constant $\beta = 0.5$. (Note that in reality, $\beta$ tends to be smaller and varies across the cells.) The effective transcription rate ($k_{\text{syn}}^{\text{eff}}$) is proportional to the cell size in the original transcript counts (right) and both the cell size and capture efficiency in the observed counts (right). (c) Distributions of original mRNA counts in cells with constant size for three specific parameter sets for the telegraph model (left) and their corresponding downsampled distribution (right). The distribution of cell-specific capture efficiencies ($\beta$) used in downsampling is illustrated in the middle upper arrow (sampled from a log-normal distribution as described in Supplementary Section S1.3.3). The challenge lies in using the downsampled observed count distribution that is also affected by variability in the capture efficiency and cell size to infer the parameters of the original distribution (middle lower arrow).

However, the statement that the telegraph model results in a simple Beta-Poisson distribution is only valid in the absence of any extrinsic noise and cell cycle effects when considering a gene with a constant transcription rate ($k_{\text{syn}}$). These assumptions do not hold true for real-world applications. As discussed in the introduction, gene expression is coupled to cell size and is, therefore, affected by the cell cycle (Battich *et al.* 2015, Sun *et al.* 2020). Moreover, we have recently shown that the telegraph model satisfies the so-called stochastic concentration homeostasis condition when the transcription rate scales with cell size (*s*) (Thomas and Shahrezaei 2021). This notion implies that the transcript counts ($X_{ij}$) of gene *i* in cell *j* in a population of growing and dividing cells (Fig. 1) is distributed as follows: where $s_{j}$ is the cell size, and $k_{x,i}' = k_{x,i}/(\phi_{i} + \alpha)$ denotes the gene-specific synthesis and promoter switching rates scaled by the effective degradation rate. The latter comprises the gene-specific degradation rate $\phi_{i}$ and the exponential growth rate $\alpha$ of the population.

$$\begin{array}{l}
{X_{ij} \sim \text{Poisson}(s_{j}k_{\text{syn},i}'p_{i}),} \\
{p_{i} \sim \text{Beta}(k_{\text{on},i}',k_{\text{off},i}'),}
\end{array}$$

During scRNA-seq, only a fraction of transcripts in each cell is captured. As we have recently demonstrated, the transcript counts observed in scRNA-seq data can be well-modelled by a binomial model with a cell-specific capture efficiency (probability) denoted by $\beta_{j}$ (Tang *et al.* 2020). Intuitively, the binomial model is a natural choice as each transcript in a given cell is captured with the same cell-specific probability $\beta_{j}$. Notably, the binomial model can explain the statistics of drop-out events without the need to invoke any zero-inflation models (Tang *et al.* 2020, Svensson 2020).

Using this binomial model, one can show that the distribution of observed transcripts ($x_{ij}$) in a cell of size $s_{j}$ and capture efficiency $\beta_{j}$ still follows the Beta-Poisson distribution but with a scaled effective synthesis rate: with $k_{\text{syn},i}^{\text{eff}}(\beta,s) = \beta_{j}s_{j}k_{\text{syn},i}'$ denoting an effective transcription rate for the observed counts. The observed counts *x* are necessarily lower than the actual original counts *X* and we therefore also refer to these as the downsampled counts. The dependence of the actual and observed transcript distributions on $\beta$ and *s* is illustrated in Fig. 1b and c. This distribution then represents the correct likelihood function that should be used in the inference of kinetic rates from scRNA-seq data as it takes the biological variability introduced by the cell size and technical variability introduced by the capture efficiency into account. In the following, the kinetic rates of the model are defined relative to the effective decay rate, and as we are dealing with snap-shot data (and assuming a steady state), we will omit the primes on the scaled rates.

$$\begin{array}{l}
{x_{ij} \sim \text{Poisson}(k_{\text{syn},i}^{\text{eff}}(\beta_{j},s_{j})p_{i}),} \\
{p_{i} \sim \text{Beta}(k_{\text{on},i}',k_{\text{off},i}')}
\end{array}$$

Detailed descriptions of the likelihood-based and simulation-based inference methods used in our study can be found in Supplementary Section S1.

---

[← 1 Introduction](01-1-introduction.md) · [Up: contents](index.md) · [3 Results →](03-3-results.md)
