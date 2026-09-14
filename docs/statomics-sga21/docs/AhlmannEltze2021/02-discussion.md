---
title: Discussion
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf
source_file: sources/statomics-sga21/docs/AhlmannEltze2021.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Discussion

**Source:** [`docs/AhlmannEltze2021.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We have described and compared three conceptually different preprocessing approaches for singlecell data. We find that the popular shifted log transformation in combination with principal component analysis performs well. We present theoretical evidence for using the related acosh transformation or using a larger pseudo-count _c_ = 1 _/_ (4 _α_ ) for the shifted logarithm. However, in the benchmark, we find only a slight performance benefit for the two alternatives.

The residual-based variance-stabilizing transformation approach first suggested by Hafemeister and Satija (2019) has nice theoretical properties. It stabilizes the variance across all genes and is not affected by variations of the size factor. However, the linear nature of the Pearson residuals-based transformation reduces its suitability for comparisons of the data of a gene across cells (such as differential expression analysis between cell subpopulations, or visualization)—there is no variance stabilization across cells, only across genes. As an alternative, we considered using non-linear residuals like randomized quantile residuals. However, in our benchmark, neither method excelled at identifying the _k_ nearest neighbors.

The recent proposal by Breda et al. (2021) to use the inferred latent expression state as a transformation is appealing because it is biologically interpretable and does not need any tunable parameters. Sanity performs well at identifying the _k_ nearest neighbors. It has two potential downsides: first, the fact that Sanity outputs not just one, but two values per gene and cell (mean and standard deviation) requires corresponding downstream processing, or conversely complicates feeding its output into generic methods that expect one number per gene and cell. Second, Sanity’s inference approach is computationally expensive: in our applications, 1 _,_ 000 _−_ 10 _,_ 000 _×_ slower than the alternative transformation approaches.

The results of our analysis differ from previously reported results. Lause et al. (2021) benchmarked different gene selection and transformation approaches and claimed that the Pearson residuals-based transformation outperforms alternative approaches. They used a dataset with known cell types (Zheng et al., 2017) and added a synthetic rare cell type population by copying the expression data for 50 B cells and injecting 10 genes exclusively expressed in this

population. The Pearson residuals-based gene selection and transformation successfully distinguished this synthetic B cell population from the real B cells. In contrast, the square root-based gene selection and transformation combination (i.e., the closest equivalent to our delta methodbased transformations) failed to distinguish the synthetic from the real B cells because none of the 10 synthetic marker genes were among the 2,000 selected highly variable genes. Lause et al. (2021) compared the methods using the average F1-score across cell types, which is sensitive to poor performance in one cell type and thus shows a strong benefit to using Pearson residuals. However, in terms of accuracy (mean of correctly classified cells) or F1-score weighted by cell type size, the square root-based gene selection and transformation outperform the Pearson residuals.

The results from Lause et al. (2021) do not show that the Pearson residual variancestabilizing transformation necessarily outperforms alternative transformations, but they stress the danger of prematurely removing important genes. In our benchmark, we avoided this problem by using all genes instead of selecting only highly variable ones. Of course, this increases the runtime of the PCA step, but that is rarely the computational bottleneck.

There has been considerable development in the space of preprocessing methods for single-cell RNA-seq data. Somewhat to our surprise, the shifted logarithm still performs among the best for preprocessing, but crucially only if combined with a dimensionality reduction method like PCA and an appropriate number of latent dimensions. Thus, in the future, we expect that new methods will shift away from simple variance stabilization to transformations that work well specifically in combination with PCA.

Ultimately, the approach of “preprocessing” (i.e., size-factor normalization and transformation) and subsequent application of generic statistical models has fundamental limitations, and we expect greater innovation from statistical models that integrate the biases and sampling phenomena in the measurement process with the biological effects (clusters, gradients, trajectories, differential expression, _. . ._ ) of interest.

6

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Availability →](03-availability.md)
