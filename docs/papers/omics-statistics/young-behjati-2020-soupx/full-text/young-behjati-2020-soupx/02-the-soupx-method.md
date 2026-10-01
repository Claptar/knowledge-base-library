---
title: The SoupX Method
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The SoupX Method

Droplet-based scRNA-seq methods produce counts of unique molecular identifiers (UMIs) for genes in thousands of cells. The aim of an scRNA-seq experiment is to infer the number of molecules present for each type of gene within each cell from these data. However, the observed counts arise from a mixture of mRNAs produced by the captured cell and those present due to background contamination. SoupX aims to remove the contribution of the cell-free mRNA molecules from each cell and recover the true molecular abundance of each gene in each cell.

The algorithm consists of the following 3 steps (summarized in Fig. 1):

1.  Estimate the ambient mRNA expression profile from empty droplets.

2.  Estimate (or manually set) the contamination fraction, the fraction of UMIs originating from the background, in each cell.

3.  Correct the expression of each cell using the ambient mRNA expression profile and estimated contamination.

SoupX produces a modified table of counts, which can be used in place of the original count matrix in any downstream analysis tool.

![](https://doi.org/10.1093/gigascience/giaa151/)

A visual summary of the SoupX method, using data from the PBMC dataset.

To estimate the background expression profile we consider all droplets with <*N*_(emp) UMIs, which we assume unambiguously do not contain cells. The fraction of background expression from gene *g*, *b_(g)*, is then given by,

$$\begin{equation*} b_{g} = \frac{\sum _d n_{g,d}}{\sum _d \sum _g n_{g,d}}, \end{equation*}$$

where *n_(g,\ d)* is the number of counts for gene *g* in droplet *d* and the sum over *d* is taken over all droplets with <*N*_(emp) UMIs (Fig. 1). The species-mixing experiment allows us to compare how accurately *b_(g)* recapitulates the true background expression found within each cell, revealing that any value of *N*_(emp) < 100 produces a good correlation, with the best correlation given when *N*_(emp) < 10 (Supplementary Fig. S2).

The most challenging part of using SoupX is estimating or specifying the number of UMIs in each cell that are contributed by background contamination. In general, the observed number of UMIs for gene *g* in cell *c* is given by

$$\begin{equation*} n_{g,c} = m_{g,c} + o_{g,c}, \end{equation*}$$

where *m_(g,\ c)* are the cell endogenous counts and *o_(g,\ c)* are the counts from the background. We assume that the relative abundance of genes that make up the background does not differ between cells, which allows us to write,

$$\begin{equation*} o_{g,c} = N_c \rho _c b_g, \end{equation*}$$

where *N_(c)* = ∑_(*g*)*n_(g,\ c)*, and ρ_(*c*) is the background contamination fraction. In general *m_(g,\ c)* is unknown and what we are aiming to measure. To proceed, we assume that there is a combination of genes and cells for which *m_(g,\ c)* = 0 exists. The genes for which *m_(g,\ c)* = 0 for a given cell are those genes that are strong negative markers of the cell type *c*. For example, the gene *HBB* is a strong positive marker for erythroid cells (red blood cells) but should not be expressed in any other cell type. So for any cell *c* that is not an erythroid cell, *HBB* will not be expressed (i.e., $m_{HBB,\mathrm{not\ Erythroid}} = 0$).

Given a set of genes/cells for which we can assume that there is no cell endogenous expression (i.e., *m_(g,\ c)* = 0) we calculate the cell-specific contamination fraction,

$$\begin{equation*} \rho _c = \frac{\sum _g n_{g,c}}{N_c \sum _g b_g}, \end{equation*}$$

where the sum is taken across all genes in cell *c* for which it is assumed *m_(g,\ c)* = 0. SoupX optionally uses clustering information to refine the set of cells for which it can be assumed that *m_(g,\ c)* = 0. If it can be shown for any cell *c* in cluster *P* that *m_(g,\ c)* > 0, then it is assumed that *m_(g,\ c)* > 0 for all *c* ∈ *P* (see Supplementary Fig. S1).

If known from prior biological knowledge, the set of genes/cells for which it can be assumed that *m_(g,\ c)* = 0can be provided as input to SoupX. Where this is not known in advance, we provide an automated alternative to estimate the contamination fraction (see Supplementary Fig. S1). The automated approach first identifies markers of each cluster of cells in the data. For each strong marker, it is assumed that *m_(g,\ c)* = 0 for all cells in clusters where the gene is not a marker and the contamination fraction is estimated (Supplementary Fig. S1). Performing this estimation across all strong marker genes provides a set of estimates of the contamination fraction. To obtain a final value, it is assumed that inaccurate estimates will have no preferred value while true estimates will cluster around the true value. The most common value is taken as the final estimate of the contamination fraction (see Fig. 1, Step 2.2).

Having determined the contamination fraction ρ_(*c*) and the background expression profile *b_(g)*, the cell endogenous counts are intuitively given by

$$\begin{equation*} m_{g,c} = n_{g,c} - N_c \rho _c b_g, \end{equation*}$$

where *n_(g,\ c)* are the observed counts, *N_(c)* = ∑_(*g*)*n_(g,\ c)*, and *b_(g)* and ρ_(*c*) are calculated as described above.

Although the intuition of Equation 5 is correct, in practice *m_(g,\ c)* is estimated by maximizing a multinomial likelihood as described in the Supplementary Methods. This procedure is further enhanced when cluster assignments are given, by performing the correction on counts aggregated at the cluster level, then distributing the corrected counts between cells in the cluster in proportion to their size (see Fig. 1). This additional step helps overcome the sparsity of scRNA-seq data, which would otherwise make it impossible to distinguish a single count due to contamination from a single count due to endogenous expression in many circumstances.

The estimated value of *m_(g,\ c)* can then be used in place of *n_(g,\ c)* in any downstream analysis.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Properties of Ambient RNA →](03-properties-of-ambient-rna.md)
