---
title: AN EXTRINSIC NOISE MODEL FOR NORMALIZATION
source: https://thesis.library.caltech.edu/17389/
source_file: sources/fang-2025-biophysical-normalisation/Thesis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AN EXTRINSIC NOISE MODEL FOR NORMALIZATION

**Source:** `Thesis.pdf` from [fang-2025-biophysical-normalisation](https://thesis.library.caltech.edu/17389/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Fang, Meichen and Lior Pachter (2025). “Extrinsic biological stochasticity and technical noise normalization of single-cell RNA sequencing data”. In: _bioRxiv_ , p. 2025.05.11.653373. doi: `10.1101/2025.05.11.653373` .

## **3.1 Introduction**

Single-cell RNA sequencing (scRNA-seq) enables genome-wide expression profiling at unprecedented scale, but current data are notoriously noisy, partially due to variability in sequencing depth per cell due to random sampling of libraries during sequencing. This issue becomes particularly acute when the measurement rate is low, and can cause biological signal to be overwhelmed by noise. Therefore, a standard and critical step at the beginning of scRNA-seq analysis is normalization, which is intended to mitigate the effects of technical noise before downstream analysis (Luecken and Theis, 2019). Typically, a global-scaling normalization method is used, which calculates a single normalization factor per cell (cell size factor) using the sum of total counts to adjust for variability in sequencing depth and technical artifacts. This approach is implemented in common packages for scRNA-seq analysis (Wolf, Angerer, and Theis, 2018; Hao et al., 2024; Booeshaghi, Hallgrímsdóttir, et al., 2022). Beyond this, more sophisticated approaches have been developed, including some popular methods that calculate the cell size factor by pooling cells (scran) (Lun, Bach, and Marioni, 2016) or using homogeneously expressed genes (Linnorma) (Yip et al., 2017), introducing multiple cell size factors for different groups of genes (SCnorm) (Bacher et al., 2017), and utilizing negative binomial regression (sctransform) (Hafemeister and Satija, 2019). Regardless of the methods used, the common goal of normalization techniques is to use one or more scaling factors to account for technical variation and try to remove it through methods such as scaling and regression.

We argue that common practices for normalization inadvertently remove extrinsic noise. The concept of extrinsic noise emerged in the study of biological stochasticity in gene expression, and refers to fluctuations in the cellular environment that affect all genes (Elowitz et al., 2002). Applying this concept to scRNA-seq suggests that normalization, particularly scaling, can eliminate biological variance present

19

in extrinsic noise. This may be critical as extrinsic noise of biological origin may carry meaningful signals relevant to specific biological questions. As a result, current normalization procedure tend to diminish biological variation (Gorin and Lior Pachter, 2022a).

To fully extend the concept of extrinsic noise to scRNA-seq, both biological and technical sources of extrinsic noise must be modeled. In fact, both biological and technical extrinsic noise are prominent and have been well characterized. In the context of biological noise (i.e., stochasticity), gene expression variability has been classified into extrinsic and intrinsic components based on their underlying mechanisms (Elowitz et al., 2002). Since extrinsic noise affects all genes within a single cell, the normalized covariance between genes has been identified as an effective measure of extrinsic noise in dual-reporter studies (Swain, Elowitz, and Siggia, 2002; Hilfinger and Paulsson, 2011; Fu and Lior Pachter, 2016). Furthermore, the impact of biological extrinsic noise on transcriptome-wide inference has been explored using a telegraph model, highlighting the importance of accounting for biological extrinsic noise itself, which can also be estimated using normalized covariance (Grima and Esmenjaud, 2024).

On the other hand, technical noise in scRNA-seq experiments has been widely studied since the development of scRNA-seq assays. For example, technical noise has been assessed experimentally using ERCC spike-ins to assess technical variance (Brennecke et al., 2013; Grün, Kester, and Oudenaarden, 2014; Kim, Kolodziejczyk, et al., 2015). ERCC-derived technical noise has been linked to global tube-to-tube variations in sequencing efficiency and a correspondence between technical noise and the observed constant coefficient of variation (CV) for highly expressed transcripts has been noted (Grün, Kester, and Oudenaarden, 2014). Currently, UMI counts are typically modeled using binomial or Poisson distributions, corresponding to Bernoulli or Poisson sampling, respectively, with cell-specific capture rates incorporated to account for detection efficiency variability (Wang et al., 2018; Sarkar and Stephens, 2021; W. Tang et al., 2023; Öcal, 2023). Notably, in the regime of low capture rates, the Poisson distribution approximates the binomial distribution.

Currently, models for scRNA-seq that account for both biological and technical extrinsic noise are typically based on specific gene expression frameworks and often assume that biological extrinsic noise influences particular kinetic parameters (W. Tang et al., 2023; Öcal, 2023). However, a more general model that accounts for extrinsic noise without assuming a specific gene expression form could be valuable.

20

Such a model would allow for flexible characterization and validation of biological intrinsic noise, while generating specific and potentially insightful predictions.

We develop such an extrinsic noise model for scRNA-seq data that combines the results of previous studies to account for both biological and technical sources of noise. We derive a general relationship between observed and intrinsic moments (covariance/variance) under a Bernoulli technical noise model and a scaling assumption for _in vivo_ gene expression. In the specific case where genes are independent and exhibit Poisson intrinsic noise, we show that the extrinsic noise is equal to both the normalized covariance and overdispersion. This extends and unifies two previous approaches: the estimation of extrinsic noise using normalized covariance (Elowitz et al., 2002; Swain, Elowitz, and Siggia, 2002; Hilfinger and Paulsson, 2011; Fu and Lior Pachter, 2016), originally applied to biological noise, and the interpretation of technical variability as a baseline overdispersion observed in pseudocell data (Grün, Kester, and Oudenaarden, 2014), generalizing both to total extrinsic noise in scRNA-seq datasets. We test this equality on RNA solution datasets where counts are intrinsically Poisson-distributed, thereby validating the technical model as well as identifying any abnormalities. Second, when applied to single-cell datasets, this equality enables us to quantify biological and technical extrinsic noise, predict the overdispersion of intrinsically Poisson genes, and identify Poisson genes, whose total expression provides a principled approach for estimating cell size factors. Overall, we demonstrate how a mechanistic and detailed model of extrinsic noise clarifies the normalization step in scRNA-seq analysis and offers new insights into the observed variability in scRNA-seq data.

## **3.2 Results**

## **A single-cell RNA-seq extrinsic noise model**

Modeling extrinsic noise in scRNA-seq requires both a biological model of gene expression and a technical model of scRNA-seq measurement so as to jointly account for biological stochasticity and technical noise (Figure 3.1b). As genes can have very different expression mechanisms and resultant distributions, we do not assume any specific distribution for _in vivo_ counts at first. Instead, we only assume that the means of genes in each cell are proportional to a cellular random variable _𝑐_<sup>_𝑏𝑖𝑜_</sup> , which represents the cell-wise size factor that summarize the biological extrinsic noise. The value of _𝑐_<sup>_𝑏𝑖𝑜_</sup> could be influenced by many factors such as the cell volume and the cell cycle phase. As there could be many unknown sources of cell-to-cell variability, _𝑐_<sup>_𝑏𝑖𝑜_</sup> is a phenomenological parameter that captures the combined effects

21

of various extrinsic factors. We denote the _in vivo_ amount of gene _𝑗_ in cell _𝑖_ by _𝑌𝑖_<sup>_𝑗_andassumeE</sup> � _𝑐𝑖_<sup>_𝑏𝑖𝑜_</sup> � = 1 without loss of generality, this model for biological extrinsic noise means


<!-- Start of picture text -->
where E � 𝑌 𝑗 � = E 𝑐𝑖𝑏𝑖𝑜 E � 𝑌𝑖 𝑗 | 𝑐 𝑖 𝑏𝑖𝑜 is the mean of gene 𝑗 across cells.<br>� � �<br><!-- End of picture text -->


Figure 3.1: **Modeling extrinsic noise in scRNA-seq data** . **a)** Model-based closedloop paradigm. The process begins with the formulation of mechanistic models, followed by rigorous mathematical analysis to generate testable predictions. These predictions are then tested on data, allowing models to be refined or rejected. The cycle repeats with updated models, creating an iterative loop of modeling. **b)** Schematic of the extrinsic noise model. **c)** Predicted relationships among normalized covariance, extrinsic noise, and overdispersion. **d)** Procedure for validating these relationships.

For the technical measurement model, we make much stronger assumptions: we assume a Bernoulli sampling of each transcript in single-cell experiment; this is based on previous studies (Klein et al., 2015) and the assumptions leads to a binomial distribution of observed counts given _in vivo_ counts. This is also the low detection approximation of Poisson sampling (Section 3.4). Similarly, we introduce a cellular

22

random variable _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> to summarize the relative success probability in the binomial distribution. This _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> can be interpreted as affecting relative read depth during sequencing and is independent of the biological model and the _in vivo_ counts. To account for differences in capture efficiency between genes, we introduce a constant capture rate, _𝜆_ , as an unknown constant for each molecular species, which cancels out in normalized quantities. Finally, we denote the observed counts after single cell sequencing by _𝑋_ , this measurement model yields


The two assumptions (Equation 3.1 and Equation 3.2) lead to simple expressions that relate the intrinsic normalized (co)variance to the observed normalized (co)variance (Section 3.4):


where _𝑎, 𝑏_ are gene indices and _𝑐_ = _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> _𝑐_<sup>_𝑏𝑖𝑜_</sup> is the overall size factor for each Cov( _𝑋_<sup>_𝑎_</sup> _,𝑋_<sup>_𝑏_</sup> <u>)</u> cell. We denote E[ _𝑋_<sup>_𝑎_</sup> ] E[ _𝑋_<sup>_𝑏_</sup> ]<sup>as normalized covariance following previous literature</sup> (Hilfinger and Paulsson, 2011), and<sup>Var[</sup><sup>_𝑋𝑎_</sup><sup><u>]−E[</u></sup><sup>_𝑋𝑎_</sup><sup><u>]</u></sup> as normalized variance for conveE[ _𝑋_<sup>_𝑎_</sup> ]<sup>2</sup> nience, since it directly indicates the extent of over-dispersion. The first term on the right hand side (<sup>Var[</sup><sup>_𝑐_</sup><sup><u>]</u></sup> E[ _𝑐_ ]<sup>2) represents the extrinsic noise, representing a combination of</sup> both biological and technical extrinsic noise:


The second terms on the right hand side of Equation 3.3 represent the contribution of intrinsic noise. For example, for two independent and intrinsically PoissonE[Cov( _𝑌_<sup>_𝑎_</sup> _,𝑌_<sup>_𝑏_</sup> | _𝑐_<sup>_𝑏𝑖𝑜_</sup> <u>)]</u> distributed genes, the intrinsic normalized covariance ( ) and norE[ _𝑌_<sup>_𝑎_</sup> ] E[ _𝑌_<sup>_𝑏_</sup> ] E[Var[ _𝑌_<sup>_𝑎_</sup> | _𝑐_<sup>_𝑏𝑖𝑜_</sup> <u>]]−E[</u> _𝑌_<sup>_𝑎_</sup> ] malized variance ( ) would both be 0. Therefore, the second E[ _𝑌_<sup>_𝑎_</sup> ]<sup>2</sup>

23

terms denote the effect of intrinsic normalized (co)variance convoluted with technical extrinsic noise.

The Equation 3.3 leads to two important observations. First, if we assume that genes are intrinsically uncorrelated, the normalized covariance can be used to estimate the extrinsic noise (Figure 3.1c), which is the canonical approach in previous studies on biological extrinsic noise (Swain, Elowitz, and Siggia, 2002; Hilfinger and Paulsson, 2011; Grima and Esmenjaud, 2024; Fu and Lior Pachter, 2016). Although the exact distribution of normalized covariance between uncorrelated gene pairs depends on the distribution of _𝑐_ , it should nevertheless center around the value of extrinsic noise, and we can use the mean/mode of the distribution to estimate the extrinsic noise. If not all but most genes are uncorrelated, the normalized covariance can still provide a reasonable estimate of the extrinsic noise using the mode of the distribution of normalized covariance. The distance between the mode and the mean provides some insight into the correlation between genes since the mode should coincide with the mean if all genes are uncorrelated. Furthermore, if we have an empirical distribution of _𝑐_ , we can verify whether the distribution of the normalized covariance aligns with the model (Figure 3.1d).

Second, if the genes are intrinsically Poisson distributed, then the normalized variance also equals the extrinsic noise (Figure 3.1c). Therefore, after estimating extrinsic noise using normalized covariance between genes, we can test whether each gene is Poisson distributed using this expected equality (Figure 3.1d). Note that the extrinsic noise term in normalized variance contributes to the observed over-dispersion in scRNA-seq data, as it introduces a constant offset visible when plotting the coefficient of variation (CV) against the mean. Therefore, genes are intrinsically less over-dispersed than observed counts might suggest, and it is possible for some genes to not be over-dispersed after taking into account the extrinsic noise. In summary, assuming genes _𝑎_ and _𝑏_ are intrinsically uncorrelated and the superscript _𝑃𝑜𝑖𝑠_ denotes intrinsically Poisson distributed genes, these two observations can be expressed as follows:


This moment relationship can be validated by estimating extrinsic noise and testing Poisson distributed genes (Section 3.4). Notably, the Poisson distribution property is particularly useful for cell size estimation, as the maximum likelihood estimate

24

(MLE) of the cell size for Poisson genes is simply their sum (Section 3.4). In practice, we filter genes based on a mean expression threshold (>0.1), as the normalized (co)variance of low-expression counts tends to be noisy. We then calculate the normalized covariance between the filtered genes to determine the mean and mode (Section 3.4). To determine whether the normalized variance equals the extrinsic noise (average normalized variance), we calculate its bootstrap confidence intervals and the equality holds for a gene if its 95% confidence interval contains the estimated value of extrinsic noise (Section 3.4). We call those genes "Poisson".

In the above derivation, we assume that _𝑐_<sup>_𝑏𝑖𝑜_</sup> and _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> are the same for all genes or species within a single cell. However, this may not be the case and we need to validate it on data. Nevertheless, the model can be extended to cases where multiple _𝑐_<sup>_𝑏𝑖𝑜_</sup> and _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> values exist for different groups of species and genes. In such cases, we simply need to introduce different _𝑐_<sup>_𝑏𝑖𝑜_</sup> and _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> for each group and all equations still hold.

## **Validating the technical noise model with homogeneous RNA solutions**

We first validated our technical noise model and the covariance-variance relationships (Equation 3.3) on scRNA-seq data of homogeneous RNA solution from K562 cells with ERCC using inDrop (Klein et al., 2015). As the RNA solution was homogeneous, the _in vivo_ count for each gene in every droplet followed the same Poisson distribution and was mutually independent (Figure 3.2a). Therefore, there was no biological extrinsic stochasticity, only technical extrinsic noise. The mode of the normalized covariance was expected to be close to the mean and all genes were expected to be Poisson.

We calculated the distribution of normalized covariance within ERCC, mature mRNA and nascent mRNA respectively to see if they shared the same _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> and extrinsic noise (Figure 3.3a). We found that ERCC and endogenous mRNA seemed to have slightly different _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> , as the estimated extrinsic noise value of ERCC was slightly smaller that that of mRNA. Within the endogenous mRNA, the extrinsic noise appeared to be the same. This suggests that the capture mechanism of ERCC in scRNA-seq might be different from endogenous mRNA, though the difference is small.

Next, we tested whether the covariance-variance relationships held for the ERCC, mature mRNA and nascent mRNA respectively. Given the genes are independent, the covariance-variance relationship holds if the Bernoulli sampling model holds.

25


Figure 3.2: **Results for homogeneous RNA solution** . **a)** Schematic of the experiment and model predictions. **b)** Distribution of normalized covariance between gene pairs with mean expression greater than 0.1, shown separately for ERCC, mature mRNA, and nascent mRNA counts. **c)** Overdispersion-mean relationship for genes with mean expression greater than 0.1, for ERCC, mature mRNA, and nascent mRNA counts, respectively. **d)** Cumulative distribution function of _𝑐_<sup>tech</sup> . Gray dots represent the empirical CDF of estimated _𝑐_<sup>tech</sup> using selected Poisson mature mRNA counts. The blue line shows a Gamma distribution fitted by matching the first two moments (mean and variance), and the red line shows a Gaussian distribution with the same mean and variance. **e)** Cumulative distribution function of normalized covariance. Gray dots represent the empirical CDF of normalized covariance for mature mRNA counts shown in **b)** . Using the estimated _𝑐_<sup>tech</sup> values and the mean expression levels of the selected genes, 1,000 bootstrap samples were generated. The purple line indicates the median empirical CDF across bootstrap replicates, and the light purple band represents the 95% confidence interval.

We plotted the normalized variance against mean, and colored Poisson genes on which the relationships held among all genes (Figure 3.2b). We also calculated

26


Figure 3.3: **Supplementary figures for homogeneous RNA solution a)** Distribution of normalized covariance between different species. **b)** Distribution of normalized covariance between Poisson genes of different species. **c)** Comparison of cell size estimators using the sum of total counts and Poisson mature counts. **d)** Distribution of normalized covariance within Poisson mature counts across different mean expression ranges.

the normalized covariance among selected Poisson genes and found that they were consistent (Figure 3.3b). The Bernoulli sampling model seemed to work well for the ERCC and mature mRNA but not for the nascent mRNA: the normalized variance of almost half of the nascent counts was much noisier than predicted, while most of the mature mRNA (90%) was within the 95% confidence intervals (Figure 3.2b). This suggests that the nascent mRNA requires a different measurement model than Bernoulli sampling.

We then sought to characterize _𝑐_ (= _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> ), which represents the cell size factors

27

commonly used in scRNA-seq analysis (Luecken and Theis, 2019). We estimated _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> as the sum of Poisson-distributed mature RNA counts and found that it correlated well with the total count sum, which was expected since there were no differentially expressed genes (Figure 3.3c). As the negative binomial distribution is commonly used to model mRNA counts in both pseudo and real cells, which implies that cell size follows a gamma distribution given a Poisson distribution of _in vivo_ counts, we asked whether _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> indeed followed a gamma distribution. We plotted and compared the empirical cumulative distribution function (CDF) of estimated _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> , computed from the sum of Poisson-distributed mature RNA counts, with the CDFs of gamma and Gaussian distributions that shared the same first two moments as _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> . We found that the distribution of _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> followed a gamma distribution reasonably well, but also fit a Gaussian distribution equally well, if not better (Figure 3.2d), which is consistent with the fact that the gamma distribution approaches the Gaussian distribution when the shape parameter is large.

To assess whether a single _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> was shared across all genes, we compared the empirical CDF of the normalized covariance of mature mRNAs with simulations generated from a Poisson distribution coupled with the empirical distribution of _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> (Figure 3.2e). The empirical CDF was less sharp than the empirical CDF of simulations, which suggested that a single _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> could not fully explain the variability, even for mature mRNA. The single _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> per cell is the average of the distribution of capture rates for different mature mRNAs in a cell. The capture rates did not seem to relate to the expression levels (Figure 3.3d). Nevertheless, based on the consistency between the mean and mode of the normalized covariance among all genes and the selected Poisson genes, we concluded that a single _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> , while not entirely accurate, provided a useful approximation.

In summary, homogeneous RNA solution data revealed that ERCCs, mature mRNAs, and nascent mRNAs are captured through distinct mechanisms, which leads to varying levels of extrinsic noise within ERCCs and endogenous mRNAs and a significantly higher variance in nascent mRNA than would be expected under a simple Bernoulli sampling model. We therefore advocate for more control experiments of this kind to validate technical noise models prior to large-scale data generation.

## **Validating the “biological” extrinsic noise of heterogeneous RNA solution**

To validate our interpretation of extrinsic noise using a heterogeneous RNA solution we examined CEL-seq2 data that contained ERCC spike-ins alongside varying

28

amounts of endogenous RNA (Tian et al., 2019). The experiment comprised eight distinct RNA mixtures extracted from three human lung cancer cell lines, each present at four RNA amounts within different wells (Figure 3.4a). Here, the eight RNA mixtures represented eight cell types and the four RNA amounts. Since cell counts were derived from wells containing RNA in solution, we assumed that they were independent and Poisson distributed. However, the different RNA amounts could give rise to biological extrinsic noise and the cell type specific mean parameters could lead to intrinsic variance and covariance. Assuming that the three human lung cancer cell lines have similar concentrations for most genes, we expected the biological extrinsic noise to arise mostly from the variation of RNA amounts. Var[ _𝑐_<sup>_𝑏𝑖𝑜_</sup> <u>]</u> Specifically, the biological extrinsic noise 2<sup>equals the CV2 of RNA amounts,</sup> E[ _𝑐_<sup>_𝑏𝑖𝑜_</sup> ] which could be calculated to be approximately or slightly above 0.33 based on the experimental design (Section 3.4). Furthermore, those genes that did not vary across the three human lung cancer cell lines were intrinsically Poisson, meaning they had a normalized variance equal to the extrinsic noise, similar to a homogeneous mRNA solution. In contrast, genes that did vary displayed greater dispersion than intrinsically Poisson genes, resulting in a normalized variance that exceeded the extrinsic noise (Prediction in Figure 3.4a).

We estimated the technical extrinsic noise using the ERCC spike-ins, and also estimate the total extrinsic noise using mature mRNA and nascent mRNA respectively, to see if they were the same. The total extrinsic noise differed within mature and nascent mRNA: the estimated extrinsic noise was slightly higher for mature mRNA (0.46) than nascent mRNA (0.42) (Figure 3.4b). The distribution of normalized covariance between mature and nascent mRNA had a similar mode to that of nascent mRNA (Figure 3.5a), indicating that the extrinsic noise of mature mRNA included both components shared with nascent mRNA and components unique to mature mRNA. Most ERCC (92%) and mature mRNA (87%) fell within the 95% confidence intervals and satisfied the Poisson criteria, whereas nascent mRNA counts had a smaller percentage (78%) and were noisier with larger normalized variance (Figure 3.4b). As a consistency check, the normalized covariance between Poisson genes showed similar values, with differences within 0.01 (Figure 3.5b). Based on these observations, we speculate that the capture of mature and nascent mRNA shared similar mechanisms as well as distinct differences, which led to the small difference in extrinsic noise. Importantly, nascent mRNA is likely to require a slightly nosier technical model than Bernoulli sampling.

29


Figure 3.4: **Results for heterogeneous RNA solution** . **a)** Schematic of the experiment and model predictions. **b)** Distribution of normalized covariance between gene pairs with mean expression greater than 0.1, shown separately for ERCC, mature mRNA, and nascent mRNA counts. **c)** Overdispersion-mean relationship for genes with mean expression greater than 0.1, for ERCC, mature mRNA, and nascent mRNA counts, respectively.

Therefore, we used normalized covariance of mature mRNA for calculating the total extrinsic noise and ERCC for the technical extrinsic noise to estimate the biological extrinsic noise based on Equation 3.4. The estimated biological extrinsic noise was 0.35, which was reasonably closed to the expectation (0.33). Then we calculated the total and technical cell size ( _𝑐𝑖_ and _𝑐𝑖_<sup>_𝑡𝑒𝑐ℎ_</sup> ) using the sums of Poisson mature mRNA and ERCC respectively, which were similar to those using total counts (Figure 3.5c). We estimated biological cell size ( _𝑐𝑖_<sup>_𝑏𝑖𝑜_</sup> ) by taking the ratio of _𝑐𝑖_ and _𝑐𝑖_<sup>_𝑡𝑒𝑐ℎ_</sup> , and compared the distribution of _𝑐𝑖_<sup>_𝑏𝑖𝑜_</sup> to the expected distribution from the experimental design (Section 3.4). Cells were centered around the expected values but the variance seemed to be large (Figure 3.5d and e).

## **Decomposing biological and technical extrinsic noise using species-mixing experiments**

Based on the results obtained with RNA in solution, we decided to focus on the mature counts. However, in this context of experiments with individual cells, the logic is reversed. Unlike in RNA solution, where genes can be assumed to follow

30


Figure 3.5: **Supplementary figures for heterogeneous RNA solution a)** Distribution of normalized covariance between different species. **b)** Distribution of normalized covariance between Poisson genes of different species. **c)** Comparison of cell size estimators using the sum of total counts and Poisson mature counts. **d)** Distribution of _𝑐_<sup>tech</sup> and _𝑐_<sup>bio</sup> . The values of _𝑐_<sup>tech</sup> and _𝑐_ are estimated from the total Poisson ERCC counts and mature mRNA counts, respectively. Based on these estimates, _𝑐_<sup>bio</sup> is computed. The brown dots are the theoretical _𝑐_<sup>bio</sup> .

a Poisson distribution in pseudocells, these assumptions do not inherently hold _in vivo_ . Instead, by testing the relationship between extrinsic noise and overdispersion across genes, we identified those genes for which the assumptions of the Poisson distribution hold, at least approximately. This enables genome-scale understanding of gene expression noise and provided an additional piece of evidence in the context

31

of previously inconsistent findings regarding biological variability (Dar et al., 2012; Battich, Stoeger, and Pelkmans, 2015).

Therefore, we used an iterative approach to estimate extrinsic noise and to identify “Poisson” genes (Figure 3.6). Starting with all genes, we calculated the normalized covariance and estimated the extrinsic noise, which was then used to identify genes whose normalized variances were close to the extrinsic noise. Next, we re-estimated the extrinsic noise using the normalized covariance between selected genes and compared it to the previous value. This process was repeated iteratively until the extrinsic noise estimate stabilized (with differences within 10%), though typically, at most one iteration was needed. Therefore, we assumed that these selected genes were independent (on average) and had intrinsic variance similar to a Poisson distribution, so we referred to them as "Poisson". Although their exact distributions may deviate from a Poisson model, these genes were likely to exhibit low variability across cells, rendering them appropriate for estimating cell size.


Figure 3.6: **Procedure on single cell datasets.**

We first sought to characterize the biological and technical contribution of extrinsic noise. To measure technical extrinsic noise, we needed some control RNA in the same cell. Usually, ERCC spike-ins are used as external controls to quantify technical variance. However, here we utilized the ambient mRNA as the control mRNA by leveraging species-mixing experiments, which are commonly used to assess doublet rates. In these scRNA-seq experiments, human and mouse cells are typically mixed, resulting in ambient mRNA from both species in droplets containing cells from only one species. Then the ambient mRNA from the other species serves as an external RNA control for technical extrinsic noise (Figure 3.7a).

In light of this, we calculated the biological and technical extrinsic noise of three 10x human-mouse mixture datasets. We used mature mRNA of the corresponding

32


Figure 3.7: **Extrinsic noise in species-mixing experiments** . **a)** Schematic of the species-mixing experiment. **b)** Overdispersion-mean relationships for human and mouse genes in both human and mouse cells in the 20k Chromium X dataset. **c)** Biological and technical extrinsic noise in three species-mixing experiments.

species to estimate total extrinsic noise, and total ambient mRNA from the other species to estimate technical extrinsic noise. We did not distinguish between nascent and mature and used the total counts when calculating normalized covariance because their counts are low. For example, in droplets containing only human cells, the technical extrinsic noise estimated from mouse ambient mRNA is 0.15, and, similar to RNA solution, the genes were expected to follow a Poisson distribution. In contrast, the total extrinsic noise estimated from human mRNA is 0.24, with fewer than 20% of human transcripts falling within the Poisson range (Figure 3.7b). The differing percentages between ambient and cellular mRNA highlight that only a small fraction of _in vivo_ transcript counts potentially follow a Poisson distribution. Based on the total and technical extrinsic noise, we estimate the biological extrinsic noise based on Equation 3.4, which leads to 0.15 for human cells (Figure 3.7b). Both the biological and technical contributions to extrinsic noise are substantial (Figure 3.7c). The estimated biological extrinsic noise are relatively robust across three datasets, and the mouse cells (NIH3T3) seem to be slightly more homogeneous than human cells (HEK293T).

## **Characterizing extrinsic noise and cell size factors on scRNA-seq data**

Given the non-negligible contribution of biological extrinsic noise even in homogeneous cell lines, we argue that even when biological extrinsic noise cannot be explicitly distinguished due to the absence of control mRNA, a substantial portion

33


Figure 3.8: **Supplementary figures for species-mixing experiments** . **a)** Overdispersion-mean relationships for human and mouse genes in both human and mouse cells in the 10k Chromium X dataset. **b)** Overdispersion-mean relationships for human and mouse genes in both human and mouse cells in the 10k Chromium controller dataset. **c)** Venn diagram of selected Poisson genes across the three datasets.

of the total extrinsic noise likely reflects underlying biological variation and should not be disregarded. Therefore, we applied our procedure to several scRNA-seq datasets and characterized both extrinsic noise and cell size factors.

We first investigated whether extrinsic noise is related to the average abundance of genes, a topic that has been debated in previous studies (Hafemeister and Satija, 2019; Lause, Berens, and Kobak, 2021). For our analysis, we selected the 10x Flex K562 datasets because the probes covering exon junctions yield more abundant and accurate mature mRNA counts. We then plotted the distribution of normalized covariance across genes with varying mean expression levels and found that the modes of the distributions were identical (0.23), with comparable means (Figure 3.9a). The percentage of “Poisson” genes is also comparable to those observed in the species-mixing data (Figure 3.9b). The distributions of normalized covariance

34

across “Poisson” genes with varying mean expression levels also show no difference with the same modes (Figure 3.10a). We concluded that extrinsic noise and the resulting baseline overdispersion are not related to the average abundance of genes.


Figure 3.9: **Extrinsic noise in single cell datasets** . **a)** Distribution of normalized covariance within genes across different mean expression ranges for the K562 10x Flex dataset. **b)** Overdispersion-mean relationship for the K562 10x Flex dataset. **c)** Distribution of normalized covariance for the mESC inDrop dataset. **d)** Distribution of normalized covariance for the mESC 10x 3’ v3 dataset. **e)** Overdispersion-mean relationship for the mESC 10x 3’ v3 dataset. **f)** Cell size along cell cycle. Cell sizes are estimated using Poisson genes from panel e). Cell cycle progression is denoted by cell cycle theta, as reported by Riba et al. (2022). **g)** Distribution of normalized covariance between gene pairs with mean expression greater than 0.1 for the PBMC dataset. **h)** Distribution of normalized covariance between selected Poisson genes for the PBMC dataset. **i)** Overdispersion-mean relationship for the PBMC dataset. **ii)** Sum of total counts against sum of Poisson counts, colored by cell types.

We then investigated whether extrinsic noise is associated with cell cycle progression. To do this, we used mouse embryonic stem cells (mESC) data with inferred cell cycle stages (Riba et al., 2022). We estimated the extrinsic noise (Figure 3.9c) and also compared it to that of mESC inDrop data (Klein et al., 2015), finding that the estimates were similar (Figure 3.9c). This indicates the robustness of the extrinsic noise across different datasets. We selected Poisson genes (Figure 3.9e),

35


Figure 3.10: **Supplementary figures for K562 10x flex dataset** . **a)** Distribution of normalized covariance within Poisson mature counts across different mean expression ranges. **b)** Comparison of cell size estimators using the sum of total counts and Poisson mature counts. r denotes the Pearson correlation coefficient.


Figure 3.11: **Supplementary figures for mESC 10x dataset** . **a)** Distribution of normalized covariance within Poisson mature counts. **b)** Comparison of cell size estimators using the sum of total counts and Poisson mature counts. r denotes the Pearson correlation coefficient.

and estimate _𝑐_ ˆ as the sum of “Poisson” mature RNA counts, which correlates well with the total count sum (Figure 3.11c). We plotted the estimated cell size factors ( ˆ _𝑐_ ) along the inferred transcriptional phase (cell cycle _𝜃_ ) from Riba et al. and observed a clear pattern of cell size variation across the cell cycle (Figure 3.9f), which confirms that the cell cycle contributes to extrinsic noise.

Up to this point, the sum of Poisson counts had shown a perfect correlation with the total counts. However, this may not be the case for heterogeneous cells, i.e., datasets consisting of different cell types. To investigate this, we applied our approach to the peripheral blood mononuclear cells (PBMC) dataset generated using 10x flex technology (10x Genomics, 2024). We found that the extrinsic noise in PBMCs is significantly higher than that observed in homogeneous cell types such as mESC and K562. The distribution of normalized covariance across all genes is right-skewed (Figure 3.9g), suggesting that many genes exhibit positive correlations. On the other hand, the distribution across Poisson genes is more symmetrical, with the mode and mean closely aligned (Figure 3.9h). The percentage of “Poisson” genes remains

36


Figure 3.12: **Supplementary figures for PBMC dataset** . **a)** Procedure for comparing differential expression (DE) analysis results using different cell sizes. **b)** P-values from the Mann–Whitney U test comparing gene expression between monocytes and NK cells, computed after normalizing the data using different cell size estimates. **c)** Correspondence between top 100 genes after two normalizations.

similar (Figure 3.9i). However, the estimated _𝑐_ ˆ as the sum of “Poisson” mature RNA counts no longer aligns well with the total count sum (Figure 3.9j). We used the Leiden algorithm to cluster cells into T cells, Natural killer (NK) cells, B cells, and Monocytes based on marker genes. Different cell types within PBMC appear to have varying ratios of “Poisson” to total counts (Figure 3.9j), likely reflecting the

37


Figure 3.13: **Results for mouse forebrain dataset** . **a)** Distribution of normalized covariance between gene pairs with mean expression greater than 0.1 for the PBMC dataset. **b)** Distribution of normalized covariance between selected Poisson genes for the PBMC dataset. **c)** Overdispersion-mean relationship for the PBMC dataset. **d)** Sum of total counts against sum of Poisson counts, colored by cell types.

presence of highly differentially expressed genes specific to monocytes. Therefore, using “Poisson” counts or total counts will result in different cell size factors. To demonstrate the impact on downstream analysis, we normalized the raw counts using both the total UMI count and the sum of Poisson gene counts, respectively, and performed a Mann–Whitney U test to identify differentially expressed genes between monocytes and natural killer cells. We compared the resulting p-values (Figure 3.12a), and listed the top 100 differentially expressed genes identified under each normalization method for comparison (Figure 3.12b). We found that this phenomenon is dataset-specific and depends on the underlying cellular composition, as demonstrated by the 10x mouse forebrain data (10x Genomics, 2023), where the sum of ’Poisson’ mature RNA counts aligns better with the total count sum (Figure 3.13d).

## **3.3 Discussion**

In this work, we clarify the underlying assumptions of extrinsic noise in scRNA-seq normalization and describe an extrinsic noise model that has only been implicitly recognized in previous studies. This model establishes a direct relationship among normalized covariance, extrinsic noise, and the overdispersion observed in intrinsically Poisson genes. This relationship enables us to validate the model using RNA solution data and to identify genes whose expression variance is consistent with a Poisson distribution. By providing a baseline for overdispersion, extrinsic noise reveals that much of the observed overdispersion in scRNA-seq data can still be explained by genes that are intrinsically Poisson.

Importantly, we have shown how a mechanistic model can lead to testable predictions, and how validating these predictions can either support the model or prompt

38

the development of alternative explanations (Phillips, 2015). Specifically, we found that Bernoulli sampling is applicable only to mature RNA counts, likely due to differences in capture mechanisms between mature and nascent mRNA. Even for mature counts, using a single cell size factor remains a coarse approximation. Furthermore, we observed that the overdispersion in some datasets cannot be fully explained by extrinsic noise, as seen in the case of STORM-seq datasets of K562 cells (Johnson et al., 2022). Despite exhibiting similar levels of extrinsic noise to the 10x Flex dataset in Figure 3.9a (Figure 3.14a), the mean-overdispersion relationship and the behavior of Poisson genes suggest that our model does not apply in this case (Figure 3.14b). Given that the technical noise model may vary across species and technologies, we advocate for more careful assessment in future experimental designs, recommending that the technical noise model be characterized prior to large-scale data generation.


Figure 3.14: **Results for K562 STORM-seq dataset** . **a)** Distribution of normalized covariance between gene pairs with mean expression greater than 0.1. **b)** Overdispersion-mean relationship.

Beyond quantifying biological and technical extrinsic noise, a key motivation for modeling extrinsic noise and cell size is to enhance the accuracy of downstream data analysis. Rather than simply normalizing total counts by cell size, we advocate for explicitly incorporating the cell size factor when modeling variable genes with more complex gene expression models, such as those beyond constitutive expression and Poisson distributions. The cell size estimators derived from Poisson genes can be treated as constants and provided as inputs to the inference process, thereby simplifying the modeling of other variable genes. Because these estimators are based on two orthogonal groups of genes, namely those used for cell size estimation and those being modeled, this approach effectively avoids the issue of "doubledipping" and ensures a more robust and reliable analysis.

We have provided only preliminary insights into extrinsic noise, as our analysis is based on modeling single genes and does not specify a detailed gene expression

39

model. As a result, we cannot determine the exact forms of variance and covariance beyond what is expected from a Poisson distribution. For genes that follow Poisson statistics, all biological extrinsic noise arises from variation in their mean expression levels. In such cases, it is sufficient to decompose extrinsic noise into biological and technical components. However, for more variable genes that exhibit superPoissonian variance, more sophisticated models such as bursty transcription are needed to accurately capture their expression dynamics (Golding et al., 2005). These models introduce additional parameters, such as burst frequency and burst size, to account for the excess variability. While most studies assume that only burst size scales with cell size (Grima and Esmenjaud, 2024; W. Tang et al., 2023; Öcal, 2023), we show that biological extrinsic noise can, in fact, be further decomposed. This allows for a more detailed, quantitative dissection of how each parameter contributes to extrinsic noise (see Section 3.4). We advocate for future studies to adopt more comprehensive modeling approaches in order to deepen our understanding of the sources and mechanisms underlying gene expression variability.

## **3.4 Methods**

## **Extrinsic noise model**

Extrinsic noise is global to a cell and contains both biological and technical components. Therefore, we introduce two random variables to represent biological and technical cell factors. Specifically, for the biological model, we assume that each cell has a random variable _𝑐_<sup>_𝑏𝑖𝑜_</sup> and the mean of every gene is proportional to this value. _𝑐𝑏𝑖𝑜_ could result from the cell volume, cell cycle and factors that effect all genes. Without loss of generality, we assume E [ _𝑐𝑏𝑖𝑜_ ] = 1. Denote the _in vivo_ number of gene j in cell i by _𝑌𝑖_<sup>_𝑗_, and this model for biological extrinsic noise means</sup>


As a consequence of law of total variance, for covariance and variance of gene a and b across cells, we have

40


The first terms on the right-hand side of both equations describe the intrinsic covariance and variance, which depend on and also reflect the gene expression mechanism. The second terms describe the extrinsic noise introduced by _𝑐_<sup>_𝑏𝑖𝑜_</sup> . This separation of intrinsic and extrinsic terms has been addressed in previous studies (Elowitz et al., 2002; Swain, Elowitz, and Siggia, 2002; Hilfinger and Paulsson, 2011).

For a technical noise model, we assume Bernoulli sampling of transcripts in singlecell sequencing experiments, which leads to binomial distribution of observed counts given _in vivo_ counts. Similarly we assume each cell has a random variable _𝑐𝑡𝑒𝑐ℎ_ and the success probability in binomial distribution is proportional to this value. This _𝑐𝑡𝑒𝑐ℎ_ could be interpreted as relative read depth during sequencing and is independent of the biological model and _in vivo_ counts. We introduce a constant capture rate _𝜆_ for each species of molecule so that we can again assume E [ _𝑐𝑡𝑒𝑐ℎ_ ] = 1. Denote the observed counts after single cell sequencing by _𝑋_ , this technical model means


41

Using law of total variance (covariance) gives


and


Therefore,


Plugging in Equation 3.7, we arrive at the expression that connects intrinsic and observed noise under our extrinsic noise model,

42


where _𝑐_ = _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> _𝑐_<sup>_𝑏𝑖𝑜_</sup> is the overall cell factor. This expression is rather general and follows directly from Equation 3.1 and Equation 3.2. The shared constant factors ( _𝑠_ :=<sup>Var[</sup><sup>_𝑐_</sup><sup><u>]</u></sup> E[ _𝑐_ ]<sup>2) denote the extrinsic noise, and potentially explain the constant</sup> offset observed in the plot of the Fano factor against mean for genes. We denote Cov( _𝑌_<sup>_𝑎_</sup> _,𝑌_<sup>_𝑏_</sup> | _𝑐_<sup>_𝑏𝑖𝑜_</sup> <u>)</u> Var[ _𝑌_<sup>_𝑎_</sup> | _𝑐_<sup>_𝑏𝑖𝑜_</sup> <u>]−E[</u> _𝑌_<sup>_𝑎_</sup> ] and by intrinsic covariance and variance. E[ _𝑌_<sup>_𝑎_</sup> ] E[ _𝑌_<sup>_𝑏_</sup> ] E[ _𝑌_<sup>_𝑎_</sup> ]<sup>2</sup>

## **Procedure for estimating extrinsic noise and selecting Poisson genes**

To estimate the extrinsic noise, we calculated the normalized covariance among genes with mean expression greater than 0.1, and used the mode of the resulting distribution. This was computed using histogram bins of width 0.01. The center of the bin with the highest frequency was taken as the estimated value, which was set to exactly two decimal digits by construction of the bin edges.

To select Poisson genes, we calculated the 95% bootstrap interval of overdispersion for each gene based on 1,000 bootstrap samples by default. Then we selected genes whose 95% bootstrap intervals contain the estimated extrinsic noise.

## **Maximum likelihood estimation of cell size**

Let _𝑋_<sup>_𝑗_</sup> _𝑖_<sup>∼Poisson(</sup><sup>_𝑐𝑖𝜇𝑗_) be the observed expression count of gene</sup><sup>_𝑗_in cell</sup><sup>_𝑖_, where</sup> _𝑐𝑖_ is the cell size (scaling factor) for cell _𝑖_ and _𝜇 𝑗_ is the mean of gene _𝑗_ .

The likelihood function for cell _𝑖_ given its gene expression vector { _𝑋𝑖_<sup>_𝑗_}</sup><sup>_𝐺_</sup> _𝑗_ =1<sup>is given</sup> by


The log-likelihood is given by


43

To find the maximum likelihood estimator (MLE) of _𝑐𝑖_ , we differentiated the loglikelihood with respect to _𝑐𝑖_ and set the derivative to zero:


Solving for _𝑐𝑖_ gives the MLE:


## **The expected biological extrinsic noise of the CEL-seq2 data**

The RNA mixture was prepared on a 384-well plate (Supplementary Figure 1a in (Tian et al., 2019)). After processing the SRA files from GEO Series GSE117617 using kb-python (Sullivan, Min, et al., 2025) and filtering out two outlier cells, we obtained a final dataset consisting of 357 cells. The exact biological extrinsic noise is influenced by the RNA amounts of the remaining 357 cells, which remain unknown. However, assuming that the 27 removed cells each had an RNA amount of 3.75 _𝜇_ g, we can estimate a lower bound for the biological extrinsic noise, which is approximately 0.333.

## **Identifiability of parameter-specific extrinsic noise in bursty models**

Here we consider the bursty model, and assume a random variable for the extrinsic noise associated with each parameter. Studying the identifiability of parameterspecific extrinsic noise is crucial, as it can help us understand how biological extrinsic noise influences gene expression. By investigating this aspect, we aim to gain insights into the mechanisms that drive variability in gene expression at the single-cell level.

We consider the following bursty model of nascent and mature mRNA:


where in the first reaction the number of nascent mRNA molecules synthesized in each burst (B) follows a geometric distribution on {0 _,_ 1 _,_ 2 _, ..._ } with a mean of b, referred to as the burst size (Singh and Bokes, 2012). The distribution of nascent is well known to be negative binomial, but the joint distribution of nascent and mature counts is not analytically available. Here, following the framework in (Gorin, Vastola, and Lior Pachter, 2023), we use the generating function method

44

to investigate the identifiablity of extrinsic noise, which can be extended to general gene expression models.

Denotethe _invivo_ nascentandmaturemRNAcountsby _𝑦𝑢_ and _𝑦𝑚_ . Let _𝐺𝑌_ ( _𝑧𝑛, 𝑧𝑚, 𝑡_ ) = � _𝑦𝑛_ � _𝑦𝑚_<sup>_𝑧_</sup> _𝑛_<sup>_𝑦𝑢𝑧_</sup> _𝑚_<sup>_𝑦𝑚𝑃_(</sup><sup>_𝑦_</sup> _𝑛_<sup>_, 𝑦_</sup> _𝑚_<sup>_, 𝑡_) be the generating function.Assuming</sup><sup>_𝛽_≠</sup><sup>_𝛾_, the facto-</sup> rial generating function _𝜙𝑌_ ( _𝑢𝑛, 𝑢𝑚,_ ∞) := log _𝐺𝑌_ ( _𝑢𝑛_ + 1 _, 𝑢𝑚_ + 1 _,_ ∞) is (Singh and Bokes, 2012):


Adding Bernoulli sampling with rate _𝑐_<sup>_𝑡𝑒𝑐ℎ_</sup> _𝜆_ , where _𝜆_ is the species-specific constant, the generating function of observed counts _𝑥_ is


Then, adding parameter-specific extrinsic noise to each parameter, the factorial generating function of observed counts _𝑋𝜙𝑋_ ( _𝑢𝑛, 𝑢𝑚,_ ∞) := log _𝐺 𝑋_ ( _𝑢𝑛_ +1 _, 𝑢𝑚_ +1 _,_ ∞) is


Note that all _𝑐_ values are shared across genes within the same cell. Given the identifiable parameters of Equation 3.14 for _in vivo_ counts _𝑌_ are _𝑏_ , _𝑘_<sup>_<u>𝛽</u>_,</sup><sup>_<u>𝛾</u>_</sup> _𝑘_<sup>(Singh and</sup> Bokes, 2012), the identifiable parameters in Equation 3.16 from observed counts _𝑋_

45

include _𝑏𝜆𝑛_ , _𝑘_<sup>_<u>𝛽</u>_,</sup><sup>_<u>𝛾</u>_</sup> _𝑘_<sup>, and</sup><sup>_𝜆_</sup> _𝜆_<sup>_<u>𝑚</u>_</sup> _𝑛_<sup>, as well as the relative values of</sup><sup>_<u>𝑐</u>_</sup> _𝑐_<sup>_𝛽𝑘_,</sup><sup>_<u>𝑐</u>_</sup> _𝑐_<sup>_𝛾𝑘_, and</sup><sup>_𝑐𝑏𝑐_tech, under</sup> the assumption that


With the use of external RNA controls, it becomes possible to further disentangle _𝑐_<sup>_𝑏_</sup> from _𝑐_<sup>tech</sup> .

## **Data and code availability**

All datasets used in this study are publicly available. Raw FASTQ files were downloaded for each dataset and processed using kb-python version 0.29.1 (Bray et al., 2016; Melsted et al., 2021; Sullivan, Min, et al., 2025), with the nac workflow (Sullivan, Hjörleifsson, et al., 2025). The links to FASTQ files are in Supplementary Table 3.1.

All code used to generate the results and figures in the paper is available at `https: //github.com/pachterlab/FP_2025` .

46

|**Dataset**|**FASTQs**|**Reference**|
|---|---|---|
|Homogeneous RNA so-<br>lution(Indrops v1)|GSM1599501|Klein et al., 2015|
|Heterogeneous<br>RNA<br>solution(CEL-seq2)|GSM3305230|Tian et al., 2019|
|Species-mixing,<br>20k<br>Chromium X (10x 3’<br>v3)|`https://s3-us-west-2.amazonaws.`<br>`com/10x.files/samples/cell-exp/`<br>`6.1.0/20k_hgmm_3p_HT_nextgem_`<br>`Chromium_X/20k_hgmm_3p_HT_`<br>`nextgem_Chromium_X_fastqs.tar`|10x Genomics, 2021c|
|Species-mixing,<br>10k<br>Chromium X (10x 3’<br>v3)|`https://s3-us-west-2.amazonaws.`<br>`com/10x.files/samples/cell-`<br>`exp/6.1.0/10k_hgmm_3p_nextgem_`<br>`Chromium_X/10k_hgmm_3p_nextgem_`<br>`Chromium_X_fastqs.tar`|10x Genomics, 2021b|
|Species-mixing,<br>10k<br>Chromium<br>controller<br>(10x 3’ v3)|`https://s3-us-west-2.amazonaws.`<br>`com/10x.files/samples/cell-`<br>`exp/6.1.0/10k_hgmm_3p_nextgem_`<br>`Chromium_Controller/10k_hgmm_`<br>`3p_nextgem_Chromium_Controller_`<br>`fastqs.tar`|10x Genomics, 2021a|
|K562 (10x flex)|`https://s3-us-west-2.amazonaws.`<br>`com/10x.files/samples/cell-`<br>`exp/7.0.0/10k_K562_singleplex_`<br>`Multiplex/10k_K562_singleplex_`<br>`Multiplex_fastqs.tar`|10x Genomics, 2022|
|mESC(10x 3’ v3)|GSM5111566|Riba et al.,2022|
|mESC(Indrops v1)|GSM1599494|Klein et al.,2015|
|PBMC (10x flex)|`https://s3-us-west-2.amazonaws.`<br>`com/10x.files/samples/cell-`<br>`exp/8.0.0/10k_Human_PBMC_`<br>`TotalSeqB_singleplex_Multiplex/`<br>`10k_Human_PBMC_TotalSeqB_`<br>`singleplex_Multiplex_fastqs.tar`|10x Genomics, 2024|
|Mouse forebrain (10x<br>flex)|`https://cf.10xgenomics.com/`<br>`samples/cell-exp/7.1.0/`<br>`10k_mouse_forebrain_scFFPE_`<br>`singleplex_Multiplex/10k_mouse_`<br>`forebrain_scFFPE_singleplex_`<br>`Multiplex_fastqs.tar`|10x Genomics, 2023|
|K562(STORM-seq)|GSE181544|Johnson et al.,2022|


Table 3.1: **Datasets metadata.** Datasets used for all analyses, with their technology in parentheses, FASTQ files accession links, and references.

47

_C h a p t e r 4_

---

[← STOCHASTIC CHEMICAL REACTION SYSTEMS AND APPROXIMATIONS](07-stochastic-chemical-reaction-systems-and-approximations.md) · [Up: contents](index.md) · [A PROCESS TIME MODEL FOR TRAJECTORY INFERENCE AND RNA VELOCITY →](09-a-process-time-model-for-trajectory-inference-and-rna-veloci.md)
