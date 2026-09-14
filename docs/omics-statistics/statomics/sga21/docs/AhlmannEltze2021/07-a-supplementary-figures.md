---
title: A Supplementary Figures
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf
source_file: sources/statomics-sga21/docs/AhlmannEltze2021.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A Supplementary Figures

**Source:** [`docs/AhlmannEltze2021.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **(A) Droplets with RNA solution (technical control)**


<!-- Start of picture text -->
Klein 2015 Svensson 2017 (1) Svensson 2017 (2)<br>ERCC spike−ins<br>10 5 10 5 10 5<br>10 3 10 3 10 3<br>10 10 10<br>10 −1 10 −1 10 −1<br>10 −3 10 −3 10 −3<br>10 −3 10 −1 10 10 3 10 5 10 −3 10 −1 10 10 3 10 5 10 −3 10 −1 10 10 3 10 5<br>Mean (µ) Mean (µ) Mean (µ)<br>(B) Cell line populations (biological control)<br>NIH/3T3 Cells HEK 293T Cells NCI−H1975 Cells GM18502 Cells<br>Cell cycle marker genes.<br>10 5 10 5 10 5 10 5<br>10 3 10 3 10 3 10 3<br>10 10 10 10<br>10 −1 10 −1 10 −1 10 −1<br>10 −3 10 −3 10 −3 10 −3<br>10 −3 10 −1 10 10 3 10 5 10 −3 10 −1 10 10 3 10 5 10 −3 10 −1 10 10 3 10 5 10 −3 10 −1 10 10 3 10 5<br>Mean (µ) Mean (µ) Mean (µ) Mean (µ)<br>Var Var Var=  = µ =µµ<br>Var Var Var=  = µ =µµ<br>Var Var Var=  = µ + =µµ++100  100 100Var Var Var2222µ µ µ=  = µ + =µµ++1  1 1222Var Var 2Varµ µ µ=  = µ + =µµ++0.01  0.01 0.012222µ µ µ<br>Var Var Var=  = µ + =µµ++100  100 100Var Var Var2222µ µ µ=  = µ + =µµ++1  1 1222Var Var 2Varµ µ µ=  = µ + =µµ++0.01  0.01 0.012222µ µ µ<br>Variance Variance Variance<br>Variance Variance Variance Variance<br><!-- End of picture text -->

Suppl. Figure S1: Scatter plot on the log-log scale of the mean and variance per gene for technical and biological control experiments. (A) shows three datasets where endogenous RNA plus a known concentration of the External RNA Control Consortium (ERCC) spike-in standard has been captured in droplets so that the variations of gene’s counts per droplet are purely statistical. The best overdispersion fit for genes with a mean of more than 1 were _α_ = 0 _._ 006, 0 _._ 011, and 0 _._ 015, respectively. (B) shows four immortalized cell line populations that are ostensibly homogeneous (cells from one mouse cell line and three human cell lines). The best overdispersion fit for genes with a mean of more than 1 were _α_ = 0 _._ 12, 0 _._ 07, 0 _._ 16, and 0 _._ 17, respectively. Cell cycle genes (gene ontology term GO:0007049) are highlighted in red; for these, we expect elevated variance even in a homogeneous cell population. The diagonal line with slope 1 (purple) corresponds to the mean-variance relation of a Poisson distribution. The yellow lines indicate quadratic mean-variance relations with different coefficients for the quadratic term (corresponding to Gamma-Poisson distributions). To limit contributions of the sequencing coverage on the variance, only cells between the median and 1 _._ 3 _×_ the median of the size factor are shown.

9

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

##### **Effect of Varying Size Factors on Transformation of Homogeneous Data**


<!-- Start of picture text -->
acosh(2αx + 1) log(x + 1) Pearson Resid. Rand. Quantile Resid.<br>20<br>10<br>0<br>−10<br>−20<br>−20 −10 0 10 20 −20 −10 0 10 20 −20 −10 0 10 20 −20 −10 0 10 20<br>PC 1<br>Size Factor<br>0.5 1.0 2.0<br>PC 2<br><!-- End of picture text -->

Suppl. Figure S2: Plots of the first two principal components of homogeneous data with size factors that vary across cells. We simulated 500 cells and 4000 genes according to the following model


This figure was inspired by Lun (2020).

10

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
Pearson Residulas Rand. Quantile Residuals Sanity<br>7 7 7<br>0 0 0<br>10 −3 10 −2 10 −1 10 0 10 1 10 2 10 −3 10 −2 10 −1 10 0 10 1 10 2 10 −3 10 −2 10 −1 10 0 10 1 10 2<br>log(x + 1) log(x + 1 (4α)) acosh(2αx + 1)<br>7 7 7<br>0 0 0<br>10 −3 10 −2 10 −1 10 0 10 1 10 2 10 −3 10 −2 10 −1 10 0 10 1 10 2 10 −3 10 −2 10 −1 10 0 10 1 10 2<br>Raw Counts<br>10000<br>0<br>10 −3 10 −2 10 −1 10 0 10 1 10 2<br>log10 of gene means<br>Raw Counts Delta method VST Residual VST Sanity<br>variance after transformation<br><!-- End of picture text -->

Suppl. Figure S3: Scatter plots of the variance per gene of the raw counts and after applying the six different transformations. The x-axis shows the logarithmized mean of the raw counts per gene; the y-axis shows the variance per gene after applying the transformations. We sampled 1,000 cells and 1,852 genes from the NIH/3T3 mouse cell line dataset. We chose the genes so that they uniformly cover the log mean expression space. We set _α_ = 0 _._ 12 using the estimate from Suppl. Fig. S1. The horizontal line highlights the target variance of 1.

11

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
A Effect of fixing βs = 1<br>HEK239T Mesmer NIH3T3 PBMC4k Zeisel Zheng<br>20<br>0<br>-20<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Residuals from the default sctransform model<br>B Effect of fixing α = 0.01<br>HEK239T Mesmer NIH3T3 PBMC4k Zeisel Zheng<br>20 Y<br>>1000<br>0 100<br>10<br>-20<br>0<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Residuals from the default sctransform model<br>C Effect of fixing βs = 1 and α = 0.01<br>HEK239T Mesmer NIH3T3 PBMC4k Zeisel Zheng<br>20<br>0<br>-20<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Residuals from the default sctransform model<br>Δ1<br>Δ2<br>Δ3<br><!-- End of picture text -->

Suppl. Figure S4: Scatter plots to assess the importance of estimating _β_ s and/or _α_ in Eq. (4). The x-axis shows the Pearson residuals calculated with _sctransform_ ’s default model (where both _β_ s and _α_ are estimated); the larger the residual, the more the data point is an outlier. The y-axis shows the difference between the residuals from sctransform’s default model and the residuals from a fit with fixed _β_ s = 1 and/or _α_ = 0 _._ 01; the extremer the difference, the more impact fixing that parameter has on the result. In (A), ∆1 is the difference between sctransform’s default model and the offset model ( _β_ s = 1). In (B), ∆2 is the difference between sctransform’s default model and the fixed dispersion model ( _α_ = 0 _._ 01). In (C), ∆3 is the difference between sctransform’s default model and the model suggested by Lause et al. (2021) ( _β_ s = 1 and _α_ = 0 _._ 01).

The facets show 6 different single-cell datasets. From each, we sampled 3,000 genes and 1,000 cells. Each point is colored by the observed count. To fit the offset mode without fixing _α_ , we forked sctransform and extended the provided offset routine from Hafemeister and Satija (2020) to allow estimation of _α_ from the data. The diagonal line visible in the Mesmer, Zeisel, and Zheng data is an artifact from sctransform limiting the maximum value for the residual to<sup>_√_</sup> _<u>n</u>_ <u>.</u>

12

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

### Construction of Randomized Quantile Residuals


<!-- Start of picture text -->
Histogram of Counts CDF of fitted Gamma-Poisson CDF of Standard Normal Randomized Quantile Residuals<br>0 10 20 30 0 10 20 30 -4 -2 0 2 4 -4 -2 0 2 4<br><!-- End of picture text -->

Suppl. Figure S5: Schematic representation of how randomized quantile residuals are constructed. In the first step, a Gamma-Poisson distribution (black line) is fitted to the observed counts. Then, the quantiles of the Gamma-Poisson distribution are matched with the quantiles of a standard normal distribution by comparing their respective cumulative density functions (CDFs). This obtains a mapping from the raw count scale to a new, continuous scale. The two colored bars (orange for _y_ = 2, yellow for _y_ = 21) exemplify this mapping. The non-linear nature of the CDFs ensures that small counts are mapped to a broader range than large counts. This helps to stabilize the variance on the residual scale. Furthermore, the randomization within the mapping sidesteps the discrete nature of the counts.

13

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
The best number of dimensions for PCA is dataset dependent<br>Branched linear manifold Branched random tree<br>1.00<br>0.75<br>Sanity<br>log(x + 1 (4α))<br>0.50 acosh(2αx + 1)<br>log(x + 1)<br>Rand Quantile Resid<br>0.25 Pearson Residuals<br>0.00<br>2 5 10 20 50 100 200 400 2 5 10 20 50 100 200 400<br>#PCA Dimensions #PCA Dimensions<br>Mean KNN Recall<br><!-- End of picture text -->

Suppl. Figure S6: Line plot of the performance (mean recall of the 100 nearest neighbors) depending on the number of dimensions used for the principal component analysis (PCA). The performance of Sanity was included as a reference; it does not depend on the number of PCA dimensions because it is always fitted on the full data.

14

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.


<!-- Start of picture text -->
Duration (Transformation + KNN−search)<br>Branched linear manifold Branched random tree<br>1week<br>1day 10,000 1,000<br>1,000 100<br>1hour<br>100 10<br>10 1<br>1min<br>1<br>1sec<br>loglog((xx + + 1acosh 1)(4(α))2αx + 1) loglog((xx + + 1acosh 1)(4(α))2αx + 1) Sanity loglog((xx + + 1acosh) 1(4(α))2αx + 1) loglog((xx + + 1acosh) 1(4(α))2αx + 1) Sanity<br>Pearson ResidualsRand Quantile Resid Pearson ResidualsRand. Quantile Resid. Pearson ResidualsRand Quantile Resid Pearson ResidualsRand. Quantile Resid.<br>+PCA (20 dim) +PCA (150 dim)<br>Absolute Relative<br><!-- End of picture text -->

Suppl. Figure S7: Bee swarm plot of the CPU time of the transformation and _k_ nearest neighbor (KNN) search for the benchmarks in Fig. 4. The secondary y-axis shows the performance relative to the median time observed when we transform the data with the shifted logarithm and reduce the dimensions using PCA (i.e., 20 and 143 seconds on the two datasets, respectively).

15

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

---

[← References](06-references.md) · [Up: contents](index.md) · [B Appendix →](08-b-appendix.md)
