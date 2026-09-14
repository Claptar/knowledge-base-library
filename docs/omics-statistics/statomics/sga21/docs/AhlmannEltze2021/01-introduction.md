---
title: Introduction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf
source_file: sources/statomics-sga21/docs/AhlmannEltze2021.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`docs/AhlmannEltze2021.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

# Transformation and Preprocessing of Single-Cell RNA-Seq Data

Constantin Ahlmann-Eltze<sup>_⋆_</sup> and Wolfgang Huber<sup>_⋆_</sup>

> _⋆_ Genome Biology Unit, EMBL, Heidelberg, 69117, Germany.

June 24, 2021

##### **Abstract**

The count table, a numeric matrix of genes _×_ cells, is a basic input data structure in the analysis of single-cell RNA-seq data. A common preprocessing step is to adjust the counts for variable sampling efficiency and to transform them so that the variance is similar across the dynamic range. These steps are intended to make subsequent application of generic statistical methods more palatable. Here, we describe three transformations (based on the delta method, model residuals, or inferred latent expression state) and compare their strengths and weaknesses. We conclude with an outlook on future needs for the development of transformations for single-cell count data.

**Software:** An R package implementing the delta method and residual-based variancestabilizing transformations is available on github.com/const-ae/transformGamPoi. **Contact:** constantin.ahlmann@embl.de

Single-cell RNA sequencing count tables are heteroskedastic, which means that counts for highly expressed genes vary more than for lowly expressed genes; accordingly, a change in a gene’s counts from 0 to 100 between different cells is more relevant than, say, a change from 1,000 to 1,100. Analyzing heteroskedastic data is challenging because standard statistical methods typically perform best for data with uniform variance. Conversely, on heteroskedastic data, in general:

estimates between two conditions are more precise the higher the involved mean parameters. Fig. 1B shows kernel-smoothed densities of the log2 fold changes between the counts from the red vs. green, and green vs. blue distributions. The latter is more precise because the coefficient of variation (that is, the standard deviation divided by the mean) of the Poisson distribution decreases with the mean (Appendix B.1).

- generic statistical tests become unreliable,

- least sum of squares regression estimates are unbiased but imprecise, and their standard errors are wrong (Wooldridge, 2013),

- classification and clustering become less accurate.

In Fig. 1, we provide a schematic example. We show the probability mass functions of three Poisson distributions with different means. We see that the standard deviation for the blue distribution ( _µ_ = 64) is four times larger than that of the red distribution ( _µ_ = 4).

It is important to keep in mind that although a higher mean implies more variance, fold change

Statistical approaches that explicitly model the sampling distribution of the data—a theoretically and empirically well-supported and widely used choice is the Gamma-Poisson distribution(Gr¨un et al., 2014; Svensson, 2020; Kharchenko, 2021)—overcome the problem of heteroskedasticity, but the parameter inference of such models can be fiddly and computationally expensive (Townes, 2019; Ahlmann-Eltze and Huber, 2020). Instead, a popular choice is to use variance-stabilizing transformations as a preprocessing step, and subsequently to use the many existing statistical methods that, implicitly or explicitly, assume uniform variance for best performance (Amezquita et al., 2020; Kharchenko, 2021).

1

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
A µ = 4 B<br>4<br>µ = 16<br>2<br>µ = 64<br>0<br>0 25 50 75 100 vs vs<br>Counts Contrast<br>ObservedChangeFoldlog2<br><!-- End of picture text -->

Figure 1: Example of heteroskedastic data. (A) shows the probability mass functions of three Poisson distributions with different means, such that the log2 fold change between the green and red means, as well as between the blue and green means, is 2. (B) shows the smoothed log2 fold changes between the red vs. the green, and the green vs. the blue distributions. The shaded areas show the range between the 5% and 95% quantiles.


<!-- Start of picture text -->
g(y)<br>3<br>2<br>1<br>y<br>0<br>0 10 20<br>log(y + 1<br>(4α)) + a<br>acosh(2 α y + 1)<br>s y<br><!-- End of picture text -->

Figure 2: Graph of the three delta methodbased variance-stabilizing transformations that are most relevant for count data. The curves are shown for overdispersion parameter _α_ = 0 _._ 1. We chose the offset a = log(4 _α_ ) in the shifted logarithm and the scaling s = 2<sup>_√_</sup> _<u>α</u>_ in the square-root transformation to match the acosh transformation. The points highlight integer values on the abscissa.

### **Delta method**

Variance-stabilizing transformations based on the delta method promise an easy fix for heteroskedasticity where the variance only depends on the mean. Instead of working with the raw counts _Y_ , we apply a non-linear function _g_ ( _Y_ ) designed to make the variances (and possibly, higher moments) more similar across the dynamic range (Bartlett, 1947).

The Gamma-Poisson distribution implies a quadratic mean-variance relation of Var[ _Y_ ] = _µ_ + _αµ_<sup>2</sup> , where _µ_ is the mean and _α_ is the overdispersion (i.e., the additional variation compared to a Poisson distribution). Given this meanvariance relation, we can use the delta method (Dorfman, 1938) to find the variance-stabilizing transformation


The shifted log transformation


is a good approximation for Eq. (1) if the pseudocount is _c_ = 41 _α_<sup>(seeFig.2andAppendixB.2).</sup> The shifted log transformation is the most popular pre-processing method for single-cell data. However, it is conventionally used with pseudocount _c_ = 1 (Butler et al., 2018; Amezquita et al., 2020). Instead, we recommend either using a larger pseudo-count, as _α_ is typically in the range of 0.01 to 0.16 (Suppl. Fig. S1), which implies a choice of _c_ in the range of 25 to 1 _._ 6; or directly using the acosh-based transformation, since the approximation deteriorates for _α ≪_ 0 _._ 01.

One problem with variance-stabilizing transformations based on the delta method are the so-called _size factors_ . These parameters, of which there is one per cell, adjust simultaneously for variable cell sizes and for variable efficiency with

2

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

which molecules are sampled from the pool of all mRNAs of a cell during the measurement process (Lun et al., 2016). To correct the data for varying size factors, conventionally, the counts are divided by suitably estimated size factors before the variance-stabilizing transformation is applied (Love et al., 2014; Amezquita et al., 2020). However, this operation does not completely remove the confounding effect of the size factors: e.g., in a low-dimensional embedding of the cells, the cells may still separate by size factor instead of possibly more interesting biological differences (Suppl. Fig. S2). Intuitively, the trouble stems from the fact that the division scales large counts from cells with large size factors and small counts from cells with small size factors to the same value, although small counts after scaling are more variable. In Appendix B.3, we explore the problem more formally.

A second problem with variance-stabilizing transformations based on the delta method is, as Warton (2018) points out, that transformations cannot reasonably be expected to stabilize the variance of small counts (compare with Suppl. Fig. S3).

### **Pearson residuals**

Hafemeister and Satija (2019) suggested a different approach to variance stabilization, which promises to address the confounding effect of the size factors and effectively stabilize the variance also for small counts. They use Pearson residuals


where _µ_ and _α_ come from a Gamma-Poisson generalized linear model fit for each gene _i_


where _j_ is the cell index, _βi_ 0 is the intercept, _sj_ is the cell-specific size factor, and _βi_ s is the corresponding size factor coefficient. Note that the denominator in Eq. (3) is the standard deviation of a Gamma-Poisson random variable with parameters _µ_ and _α_ .

The generalized linear model incorporates the size factors and removes their confounding effect (Suppl. Fig. S2). Furthermore, the transformation, using the gene-wise mean and standard deviation estimate, ensures that also the

variances of lowly expressed genes are stabilized (Suppl. Fig. S3).

Although _sctransform_ (the implementation of the Pearson residual method provided by Hafemeister and Satija (2019)) performed well in a recent benchmark (Germain et al., 2020), there has been a debate around its statistical model. Lause et al. (2021) argued that neither the estimation of _βi_ s nor the estimation of one overdispersion per gene are necessary. Instead, Lause et al. (2021) suggested treating the log-size factors as offsets (i.e., fixing _βi_ s = 1) and fixing the overdispersion to _α_ = 0 _._ 01, because that is roughly the overdispersion they observed in experiments where an RNA solution is homogeneously encapsulated in droplets. Hafemeister and Satija (2020) responded that estimating a gene-wise coefficient for the size factor “allows sctransform to adapt to artifacts and biases” and that fixing the overdispersion to a small value over-emphasizes the variation of highly abundant housekeeping genes.

Estimating a size factor coefficient per gene or treating it as fixed has little impact on the resulting residuals. Both Lause et al. (2021) and Hafemeister and Satija (2020) state that the resulting residuals are similar. We confirm that the question of how the overdispersion is chosen is more important. In Suppl. Fig. S4, we compare the effect of using the offset model or a fixed overdispersion against the sctransform model across six single-cell datasets. We find that the impact of using the offset model is negligible compared to the choice of the overdispersion.

So how should the overdispersion be estimated or fixed? It turns out that there is no unique correct, or universally optimal answer: it depends on the biological question that the analyst wants to ask. Lause et al. (2021) based their suggestion on the analysis of droplets all loaded from the same RNA solution. This can be considered a technical control experiment, and we confirm that _α_ = 0 _._ 01 describes the overdispersion for such data well (Suppl. Fig. S1A). However, a technical control experiment is not the only possible reference frame.

To complement the analysis of Lause et al. (2021), we analyzed the overdispersion found in cells from immortalized cell lines, which one can consider biological replicates (Suppl. Fig. S1B). The data from these cells show more overdispersion than that of the droplets with RNA solution,

3

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
Marker Gene Distribution after Transformation<br>Raw Counts log(x + 1) log(x + 1 (4α)) acosh(2αx + 1) Pearson Resid. Rand. Quant. Resid. Sanity<br>0 400 800 1200 0.0 2.5 5.0 7.5 2 3 4 5 6 0 2 4 0 10 −10 0 10 −7.5 −5.0 −2.5 0.0<br>0 1000 2000 3000 0 3 6 3 5 0.0 2.5 5.0 0 20 40 −10 0 10 20 −6 −4 −2 0<br>0 5 10 15 0.0 2.5 2.0 2.5 3.0 0.0 0.5 1.0 1.5 0 10 20 0 5 −15 −10 −5 0<br>cells of the cell type associated with the marker gene other cells<br>Sftpc<br>Scgb1a1<br>Ear2<br><!-- End of picture text -->

Figure 3: Histograms of the raw gene counts and the transformed values, for six different transformation approaches, for three cell-type marker genes in a mouse lung dataset (Angelidis et al., 2019). The color of the bars indicates whether a cell is of the cell type associated with the marker gene (Sftpc for type II pneumocytes, Scgb1a1 for club and goblet cells, Ear2 for alveolar macrophages). For visual clarity, we down-sampled the other cells (grey) to match the number of those from the marked cell type.

and the overdispersion differs from gene to gene. This is not surprising, as even in an ostensibly homogeneous cell population, there are real biological differences between cells, e.g., cell cycle stage.

For the analyst, the question remains how to set the overdispersion.

- If any variation larger than the one expected due to Poisson sampling is considered interesting, it is natural to fix the overdispersion to _α_ = 0 or, allowing for some slack, to a small value like _α_ = 0 _._ 01 as Lause et al. (2021) suggested.

- If the interest lies in genes whose variation is higher than that in the majority of genes of similar expression level, a robust approach is that of Hafemeister and Satija (2019), who fit a trend line through the mean-overdispersion relation.

- If one wants to level any gene-wise overdispersion differences, e.g., if the interest lies in expression patterns of genes across cells, irrespective of each gene’s absolute variability, one could use the gene-wise maximum likelihood overdispersion estimates.

An important drawback of the Pearson residuals is that they fail to stabilize the variance if a gene’s true expression strongly differs between cell subpopulations, as shown in Fig. 3. The figure shows the expression pattern of three cell type marker genes after applying differ-

ent variance-stabilizing transformations. Unlike the delta method-based, non-linear variancestabilizing transformations, the Pearson residuals fail to reduce the variance within the highexpression subpopulations, because the Pearson residuals are a linear transformation per gene (Eq. (3)). This means that while Pearson residuals successfully rescale the data from different genes relative to each other, heteroskedasticity in the data of a gene across cells remains and may obstruct tasks like clustering, mixture modelling or differential expression analysis.

An alternative is to combine the idea of delta method-based variance-stabilizing transformations with the generalized linear modelresidual approach by using non-linear residuals. We suggest using, for example, randomized quantile residuals (Dunn and Smyth, 1996). (Suppl. Fig. S5 shows how they are constructed.) Same as Pearson residuals, randomized quantile residuals stabilize the variance for small counts (Suppl. Fig. S3), but also stabilize the variance for one gene across cells (Fig. 3).

### **Latent expression state**

An alternative approach, which is not directly concerned with finding a variance stabilizing transformation, aims to infer the latent expression state for each cell and gene. This is the idea used in differential expression tools like _edgeR_ and _DESeq2_ (Robinson et al., 2009; Love et al., 2014). It was recently developed further by Breda et al. (2021), who suggest using it as a data trans-

4

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
K−nearest neighbor recall on simulated data<br>Branched linear manifold Branched random walk<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>Delta method VST Residual VST Delta method VST + PCA Residual VST + PCA Sanity<br>loglog((xx + + 1acosh 1)(4(α))2αx + 1) loglog((xx + + 1acosh 1)(4(α))2αx + 1) Sanityloglog((xx + 1 +) 1acosh(4α))(2αx + 1) loglog((xx + 1 +) 1acosh(4α))(2αx + 1) Sanity<br>Pearson ResidualsRand Quantile Resid Pearson ResidualsRand. Quantile Resid. Pearson ResidualsRand Quantile Resid Pearson ResidualsRand. Quantile Resid.<br>+PCA (20 dim) +PCA (150 dim)<br>Mean KNN Recall<br><!-- End of picture text -->

Figure 4: Bee swarm plot of the method performance for the eleven transformation methods discussed in this paper. We measure the performance as the percentage of correctly identified 100 nearest neighbors for each cell. We simulated two branching datasets: (1) each branch is a linear interpolation between two points, (2) each branch is a random walk (i.e., using the same kind of dataset as Breda et al. (2021)). On the linear manifold dataset, we used the first 20 principal components; on the random walk dataset, we used 150. The simulated overdispersion for the linear manifold dataset was _α_ = 0 _._ 01 and for the random walk _α_ = 0. For the transformations, we chose a mismatched overdispersion of _α_ = 0 _._ 05 for both datasets.

#### formation.

Breda et al. (2021) posit that each cell is characterized by a latent expression state, for which we observe a corrupted picture through the mRNA counts. To account for the uncertainty of the inferred expression state, they choose a Bayesian inference approach. Given a count matrix, their method _Sanity_ infers a matrix of posterior distributions, which they represent using two matrices of real numbers: the distributions’ means and standard deviations. The inferred posterior for a specific gene and cell is a function of the observed count, the cell’s size factor, and the gene’s overall expression across all cells. A larger size factor implies more precision in the inference of the latent state of that cell. The gene’s expression pattern is used to regularize the inference. Breda et al. (2021) show that the regularization suppresses Poisson noise and that their method does a better job estimating the variance per gene on simulated data and data without biological signal.

Furthermore, Breda et al. (2021) include a benchmark that shows that Sanity is the best method for identifying the _k_ nearest neighbors of a cell. However, we find that the delta method-

based and residual-based variance-stabilizing transformations perform similarly well if we reduce the dimensions of the input data using principal component analysis (PCA) before searching for the _k_ nearest neighbors (Fig. 4). The dimension reduction has the effect of averaging out uncorrelated noise, and serves a similar purpose as the regularization step of Sanity. However, unlike Sanity, the PCA-based approach requires the choice of the number of dimensions, which can greatly affect the performance (Suppl. Fig. S6).

A limitation of Sanity is that it is slow compared to the other transformations (Suppl. Fig. S7). In our analysis, Sanity needed 1 _,_ 000 _−_ 10 _,_ 000 _×_ more CPU time. The exact performance difference, of course, depends on the size of the dataset, the number of nearest neighbors, and the number of dimensions used in PCA, but in general, Sanity’s _k_ nearest neighbor search scales quadratically with the number of cells, because Sanity estimates all cell-by-cell distances. In contrast, the other transformations can be combined with approximate nearest neighbor search algorithms like random projection trees (Dasgupta and Freund, 2008), which scale linearly with the number of cells.

5

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

---

[Up: contents](index.md) · [Discussion →](02-discussion.md)
