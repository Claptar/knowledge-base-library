---
title: 2 Materials and methods
source: https://doi.org/10.1093/bioinformatics/btz726/
source_file: sources/papers/tang-2020-baynorm/tang-2020-baynorm.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `tang-2020-baynorm.jats` from [papers/tang-2020-baynorm](https://doi.org/10.1093/bioinformatics/btz726/) — papers · tang-2020-baynorm, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Materials and methods

A scRNA-seq dataset is typically represented in a matrix of dimension *P* × *Q*, where *P* denotes the total number of genes observed and *Q* denotes the total number of cells studied. The element *x_(ij)* ($i \in \left\{ 1,2,\ldots,P \right\}$ and $j \in \left\{ 1,2,\ldots,Q \right\}$) in the matrix represents the number of transcripts reported for the *i*th gene in the *j*th cell. This is equal to the total number of sequencing reads mapping to that gene in that cell for a non-unique molecular identifier (UMI) protocol. For UMI-based protocols this is equal to the number of individual UMIs mapping to each gene (Parekh *et al.*, 2018; Smith *et al.*, 2017). The matrix can include data from different groups or batches of cells, representing different biological conditions. This can be represented as a vector of labels for the cell groups or conditions (*C_(j)*). bayNorm generates for each gene (*i*) in each cell (*j*) a posterior distribution of original expression counts ($x_{\mathit{ij}}^{0}$), given the observed scRNA-seq read count for that gene (*x_(ij)*) (Fig. 1a).

![](https://doi.org/10.1093/bioinformatics/btz726/)

A binomial model of mRNA capture is consistent with the statistics of raw experimental scRNA-seq data. (**a**) Cartoon illustration of the bayNorm approach. Only a fraction of the total number of mRNAs present in the cell is captured during scRNA-seq library preparation. This occurs with a global probability called capture efficiency (*β*). Using cell-specific estimates of *β*, bayNorm aims at recovering the original number of mRNA of each gene present in each cell. Comparisons between raw experimental scRNA-seq data from the Klein study (Klein *et al.*, 2015) and synthetic data obtained using the Binomial\_bayNorm (orange), Binomial\_Splatter (blue) or Splatter (Zappia *et al.*, 2017) (green) simulation protocols (see Supplementary Note S2 for details). (**b**) Variance versus mean expression relationship. (**c**) Dropout rates versus mean expression relationship (note that Binomial\_Splatter and Binomial\_bayNorm are on top of each other in this panel). The dotted line shows the $e^{( - \text{Mean}~\text{expression})}$ function. (**d**) Distribution of dropout values per gene. (**e**) Distribution of dropout values per cell. (Color version of this figure is available at *Bioinformatics* online.)

A common approach for normalizing scRNA-seq data is based on the use of a global scaling factor (*s_(j)*), ignoring any gene-specific biases (for a recent review see Vallejos *et al.*, 2017). The normalized data ${\widetilde{x}}_{\mathit{ij}}$ is obtained by dividing the raw data for each cell *j* by its global scaling factor *s_(j)*:

$${\widetilde{x}}_{\mathit{ij}} = \frac{x_{\mathit{ij}}}{s_{j}}$$

In bayNorm, we implement global scaling using a Bayesian approach to infer the original transcript counts in each cell. We assume given the original number of transcripts in the cell ($x_{\mathit{ij}}^{0}$), the number of transcripts observed (*x_(ij)*) follows a Binomial model with probability *β_(j)* (Klein *et al.*, 2015), which we refer to as capture efficiency and it represents the probability of original transcripts in the cell to be observed for a cell with average size (or average transcript content). The capture efficiencies are proportional to global scaling factors normalized by an estimate of mean capture efficiency $\overline{\beta}$ (the average fraction of original transcripts that are observed across all cells) for the experiment and correct for cell-to-cell variation in transcript capture and original transcript content (see Supplementary Note S1). In addition, we assume that the original number or true count of the *i*th gene in the *j*th cell ($x_{\mathit{ij}}^{0}$) follows Negative Binomial distribution with parameters mean (*μ*) and size (or dispersion parameter, *ϕ*), such that: $$\left. \Pr(x_{\mathit{ij}}^{0} = n \middle| \phi_{i},\mu_{i}) = \frac{\Gamma(n + \phi_{i})}{\Gamma(\phi_{i})n!}\left( \frac{\phi_{i}}{\mu_{i} + \phi_{i}} \right)^{\phi_{i}}\left( \frac{\mu_{i}}{\mu_{i} + \phi_{i}} \right)^{n}. \right.$$

So, overall we have the following model:

$$\begin{array}{ll}
 & \left. x_{\mathit{ij}} \middle| x_{\mathit{ij}}^{0} \sim \text{Binom}(x_{\mathit{ij}}^{0}\operatorname{,~}\text{prob} = \beta_{j}), \right. \\
 & {x_{\mathit{ij}}^{0} \sim \text{NB}(\text{mean} = \mu_{i}\operatorname{,~}\text{size} = \phi_{i}).}
\end{array}$$

Using the Bayes rule, we have the following posterior distribution of original number of mRNAs for each gene in each cell:

$$\underset{\text{Posterior}}{\underset{︸}{\Pr\left( x_{ij}^{0} \middle| x_{ij},\beta_{j},\mu_{i},\phi_{i} \right)}} = \frac{\overset{\text{Likelihood}}{\overset{︷}{\Pr\left( x_{ij} \middle| x_{ij}^{0},\beta_{j} \right)}} \times \overset{\text{Prior}}{\overset{︷}{\Pr\left( x_{ij}^{0} \middle| \mu_{i},\phi_{i} \right)}}}{\underset{\text{Marginal~likelihood}}{\underset{︸}{\Pr\left( x_{ij} \middle| \mu_{i},\phi_{i},\beta_{j} \right)}}}$$

The prior parameters *μ* and *ϕ* of each gene were estimated using an empirical Bayesian method by pooling information across cells as discussed in detail in Supplementary Note S1. The estimation is termed ‘global’, if priors informed by combining all cells in the study regardless of their conditions or batch (*C_(j)*) and is termed ‘local’, if the prior is estimated by pooling information across specific cell groups (*C_(j)*).

The marginal likelihood for gene *i* in cell *j* is

$$\begin{matrix}
\left. \Pr(x_{\mathit{ij}} \middle| \mu_{i},\phi_{i},\beta_{j}) = \sum\limits_{n = 0}^{+ \infty}\underset{\text{Binomial}}{\underset{︸}{\begin{pmatrix}
n \\
x_{\mathit{ij}}
\end{pmatrix}\beta_{j}^{x_{ij}}\left( 1-\beta_{j} \right)^{n-x_{\mathit{ij}}}}} \right. \\
{\times \underset{\text{Negative~Binomial}}{\underset{︸}{\begin{pmatrix}
{n+\phi_{i}-1} \\
{\phi_{i}-1}
\end{pmatrix}\left( \frac{\phi_{i}}{\mu_{i}+\phi_{i}} \right)^{\phi_{i}}\left( \frac{\mu_{i}}{\mu_{i}+\phi_{i}} \right)^{n}}}} \\
{= \underset{\text{Negative~Binomial}}{\underset{︸}{\begin{pmatrix}
{x_{\mathit{ij}}+\phi_{i}-1} \\
{\phi_{i}-1}
\end{pmatrix}\left( \frac{\phi_{i}}{\mu_{i}\beta_{j}+\phi_{i}} \right)^{\phi_{i}}\left( \frac{\mu_{i}\beta_{j}}{\mu_{i}\beta_{j}+\phi_{i}} \right)^{x_{\mathit{ij}}}}},}
\end{matrix}$$

which follows from using

$$\begin{pmatrix}
{n + \phi_{i} - 1} \\
{\phi_{i} - 1}
\end{pmatrix}\begin{pmatrix}
n \\
x_{\mathit{ij}}
\end{pmatrix} = \begin{pmatrix}
{x_{\mathit{ij}} + \phi_{i} - 1} \\
{\phi_{i} - 1}
\end{pmatrix}\begin{pmatrix}
{n + \phi_{i} - 1} \\
{n - x_{\mathit{ij}}}
\end{pmatrix},$$

and

$$\begin{matrix}
{\sum\limits_{n = x_{\mathit{ij}}}^{+ \infty}z^{n}\begin{pmatrix}
{\phi_{i} + n - 1} \\
{n - x_{\mathit{ij}}}
\end{pmatrix} = \sum\limits_{m = 0}^{+ \infty}z^{m + x_{\mathit{ij}}}\begin{pmatrix}
{\phi_{i} + m + x_{\mathit{ij}} - 1} \\
m
\end{pmatrix}} \\
{= \frac{z^{x_{\mathit{ij}}}}{{(1 - z)}^{\phi_{i} + x_{\mathit{ij}}}},}
\end{matrix}$$

with $z = \frac{\mu_{i}}{\mu_{i} + \phi_{i}}\left( 1 - \beta_{j}) \right.$ in Equation (4). Hence we have that the number of transcripts reported for the *i*th gene in the *j*th cell

$$x_{\mathit{ij}} \sim \text{NB}(\text{mean} = \mu_{i}\beta_{j},\text{size} = \phi_{i}),$$

has a Negative Binomial distribution with mean $\mu_{i}\beta_{j}$ and size *ϕ_(i)*.

It can also be shown that the posterior distribution of $x_{\mathit{ij}}^{0}$ is a shifted Negative Binomial distribution. To sample from the posterior distribution, we note that the original count can be expressed as

$$x_{\mathit{ij}}^{0} = x_{\mathit{ij}} + \zeta_{\mathit{ij}},$$

where *ζ_(ij)* is the *lost* count satisfying

$$\zeta_{\mathit{ij}} \sim \text{NB}\left( \text{mean} = \frac{\mu_{i}(1 - \beta_{j})(x_{\mathit{ij}} + \phi_{i})}{\mu_{i}\beta_{j} + \phi_{i}},\text{size} = x_{\mathit{ij}} + \phi_{i} \right).$$

The posterior mean and variance then evaluate to

$$E\lbrack x_{\mathit{ij}}^{0}\rbrack = x_{\mathit{ij}}\frac{\mu_{i} + \phi_{i}}{\mu_{i}\beta_{j} + \phi_{i}} + \mu_{i}\frac{\phi_{i} - \phi_{i}\beta_{j}}{\mu_{i}\beta_{j} + \phi_{i}},$$

$$\text{Var}\lbrack x_{\mathit{ij}}^{0}\rbrack = \frac{(x_{\mathit{ij}} + \phi_{i})\mu_{i}(1 - \beta_{j})(\mu_{i} + \phi_{i})}{{(\phi_{i} + \mu_{i}\beta_{j})}^{2}}.$$

Note that when *ϕ_(i)* is small, the mean of posterior tends to $\frac{x_{\mathit{ij}}}{\beta_{j}}$. After estimating the posterior distribution for each gene in each cell, we can either sample a certain number of draws from it (3D array output, see Supplementary Fig. S1) or extract the mean or maximum a posteriori probability (MAP; Gelman *et al.*, 2014; 2D array output, see Supplementary Fig. S1). More details on the use of Binomial distribution and estimation of *β* and priors can be found in the Supplementary Note S1 and pseudo code (Algorithm 1) in the Supplementary Note.

---

[← 1 Introduction](01-1-introduction.md) · [Up: contents](index.md) · [3 Results →](03-3-results.md)
