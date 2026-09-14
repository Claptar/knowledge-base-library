---
title: CONTRASTIVE DIMENSIONALITY REDUCTION FOR DIFFERENTIAL VARIANCE
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# CONTRASTIVE DIMENSIONALITY REDUCTION FOR DIFFERENTIAL VARIANCE

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One of the first steps in a scRNA-seq workflow is to reduce the dimension of observations from tens of thousands of genes to a lower dimension, with the underlying assumption that cells can be described by modules of correlated genes that are co-expressed. These lower dimension cell representations can then be assigned to discrete groups that display similar gene expression profiles and classified as belonging to a certain cell type by the expression of known cell type marker genes [49]. Perhaps the most commonly employed method for dimensional reduction is principal component analysis (PCA), first proposed in the early twentieth century [50, 51], which finds linear combinations of features (e.g., genes) that best preserve the variance of the observations in the lower dimension. This takes advantage of the variance inherent in single-cell observations by preserving it: features highly weighted in PCA are those that display variability across cells.

However, _contrasting_ the variability of observations, and the features driving it, in settings for which target and background datasets are available is a powerful way to move beyond the mean and suggest features as having differential variance between conditions. This chapter summarizes work on developing the theory and methods for contrastive principal component analysis of genomics data via the Rayleigh quotient and associated generalized eigenproblems, useful for single-cell genomics but also for data science more generally.

### **2.1 The Rayleigh Quotient for Genomics**

This section summarizes content from [44] by M.C.<sup>∗</sup> , K.J.<sup>∗</sup> and L.P.<sup>∗</sup> , where ∗ denotes co-first authorship. M.C., K.J., and L.P. developed the methods, produced the results and drafted the manuscript.

Contrastive learning methods can be powerful tools for genomics, enabling the identification of signals in an experiment via dimension reduction while reducing noise using a control. One such approach is contrastive PCA (cPCA) [52] and its extensions [53, 54], which attempt to maximize variance of target samples while minimizing variance of background samples. However, the cPCA objective

9

involves a subtraction of target and background covariance matrices, which leads to non-physical negative variances. A more natural objective for contrastive principal component analysis that retains positive variance relationships involves the ratio of covariance matrices formulated via a Rayleigh quotient, analogous in form to PCA itself and many existing dimensional objectives.

### **Principal Component Analysis and Other Rayleigh Quotient Instantiations**

Principal Component Analysis (PCA) refers to the identification of a sequence of subspaces of a Euclidean vector space that provide optimal low-dimensional linear approximations to a high-dimensional dataset [50, 51]. Formally, given centered data vectors _𝑥_ 1 _, . . . , 𝑥𝑛_ ∈ R<sup>_𝑑_</sup> with sample covariance matrix Σ<sup>ˆ</sup> , PCA seeks unit vectors _𝑣_ 1 _, . . . , 𝑣 𝑘_ that maximize


The vectors { _𝑣𝑖_ } _𝑖_<sup>_𝑘_</sup> =1<sup>thatmaximizeRPCA(</sup><sup>_𝑣_)aretheeigenvectorsofΣˆ,andthe</sup> corresponding eigenvalues represent the variances explained along each direction. The _𝑘_ -dimensional subspace spanned by the first _𝑘_ eigenvectors maximizes the total projected variance and equivalently minimizes the mean-squared reconstruction error among all _𝑘_ -dimensional linear subspaces.

The quantity RPCA( _𝑣_ ) is a special case of the Rayleigh quotient, which, for two square matrices _𝐴_ and _𝐵_ , is defined as


When both _𝐴_ and _𝐵_ are symmetric and _𝐵_ is positive definite, the maxima of (2.2) satisfy the generalized eigenvalue problem _𝐴𝑣_ = _𝜆𝐵𝑣_ [55] (see the subsection on solving _𝜌_ pCA below).

Many other dimension-reduction and signal-extraction problems can be formulated as a Rayleigh quotient maximization. For example, Fisher linear discriminant analysis (LDA; [56, 57]) maximizes the Rayleigh quotient


where _𝑆𝐵_ is a between-class scatter matrix and _𝑆𝑊_ is a within-class scatter matrix. Maximizing RLDA( _𝑣_ ) yields directions that best separate classes by maximizing inter-class variance while minimizing intra-class variance.

10

Recently, contrastive PCA (cPCA; [52]) proposed to identify patterns present in one dataset but not another. The method seeks components that exhibit high variance in a target dataset while exhibiting low variance in a background dataset. The original publication defines cPCA as the eigendecomposition of a contrastive "covariance" matrix,


where Σ<sup>ˆ</sup> _𝑇_ and Σ<sup>ˆ</sup> _𝐵_ are the sample target and background covariance matrices, respectively, and _𝛼>_ 0 is a tunable contrast parameter. Note that while the sum of covariance matrices is always a covariance matrix, the difference of covariance matrices may not be positive semidefinite; _𝐶𝛼_ can have negative eigenvalues, thus suggesting non-physical variances.

We propose rather maximizing the ratio of the target to background projection variances by solving the Rayleigh quotient problem


This yields non-negative variance ratios without requiring a tuning parameter _𝛼_ . The Rayleigh quotient is also scale invariant (scaling either covariance matrix by a positive constant rescales all eigenvalues but leaves the eigenvectors, and therefore = the contrastive subspace, unchanged, i.e., for _𝑎, 𝑏>_ 0, R _𝜌_ PCA( _𝑣_ ; _𝑎_ Σ<sup>ˆ</sup> _𝑇 , 𝑏_ Σ<sup>ˆ</sup> _𝐵_ ) _<u>𝑎</u>_ ⪰ Σ<sup>ˆ(2)</sup> or Σ<sup>ˆ(1)</sup> ⪯ Σ<sup>ˆ(2)</sup> _𝑏_<sup>R</sup><sup>_𝜌_PCA(</sup><sup>_𝑣_));andmonotonic(ifΣˆ</sup> _𝑇_<sup>(1)</sup> _𝑇 𝐵 𝐵_<sup>,thenR</sup> _𝜌_<sup>(1</sup> PCA<sup>)(</sup><sup>_𝑣_)≥</sup> R<sup>(2)</sup> _𝜌_ PCA<sup>(</sup><sup>_𝑣_)).This means that increasing the target variance or decreasing the back-</sup> ground variance never decreases the Rayleigh quotient. Furthermore, the cPCA objective (2.4) can be derived as a Taylor approximation (under a strong assumption) of the _𝜌_ PCA objective [44].

We thus propose the Rayleigh quotient objective as the correct method for contrastive principal component analysis. The Rayleigh quotient (2.2) is frequently referred to as _𝜌_ ; we therefore adopt the term _𝜌_ PCA to highlight the fact that _𝜌_ PCA extends PCA via a Rayleigh quotient where the matrix in the denominator is not necessarily the identity. Furthermore, the term _𝜌_ PCA rather than just _𝜌_ is intended to convey that the method is more than just the solution of the quotient (computing generalized eigenvalues and eigenvectors of covariance matrices derived from data); _𝜌_ PCA includes the projections of the data onto the subspaces spanned by the generalized eigenvectors. Below we provide details on how to solve the _𝜌_ PCA objective.

11

### **Solving** _𝜌_ **PCA**

The _𝜌_ PCA objective (2.5) seeks to find


where Σ<sup>ˆ</sup> _𝑇_ and Σ<sup>ˆ</sup> _𝐵_ denote the empirical target and background covariances, respectively, and Σ<sup>ˆ</sup> _𝐵_ is assumed to be positive definite (if empirical target covariance matrices are not positive definite, regularization such as Tikhonov shrinkage can be applied [44]). That is, a direction _𝑣_ in which the target variance is maximized while the background variance is minimized. Because the quotient is homogeneous in _𝑣_ , scaling _𝑣_ by any nonzero constant does not change the objective. Therefore, we can impose a normalization constraint, leading to the equivalent constrained optimization problem


The constraint specifies unit variance in the background so that the maximization measures relative rather than absolute variance. To solve this constrained problem, we introduce a Lagrange multiplier _𝜆_ and define the Lagrangian


Taking the gradient with respect to _𝑣_ and setting it equal to zero yields


Equation (2.9) is a generalized eigenvalue problem, and its solutions ( _𝑣, 𝜆_ ) satisfy the stationarity condition of the Rayleigh quotient. The eigenvectors _𝑣_ corresponding to the largest generalized eigenvalues _𝜆_ define the directions along which the target variance is maximized relative to the background variance. Each eigenvalue _𝜆𝑖_ represents the ratio of target-to-background variance along its associated direction _𝑣𝑖_ .

This extends naturally to multiple dimensions. Let _𝑉_ = [ _𝑣_ 1 _, . . . , 𝑣𝑑_ ] ∈ R<sup>_𝐷_×</sup><sup>_𝑑_</sup> denote the matrix whose columns are the top _𝑑_ generalized eigenvectors of (Σ<sup>ˆ</sup> _𝑇 ,_ Σ<sup>ˆ</sup> _𝐵_ ), and let Λ = diag( _𝜆_ 1 _, . . . , 𝜆𝑑_ ) be the diagonal matrix of the associated eigenvalues. The multidimensional generalization of the Rayleigh quotient replaces the scalar ratio by a trace ratio, yielding the objective


12


<!-- Start of picture text -->
a Target data  𝜌= 𝑣 𝑣!! Σ Σ%% " !𝑣 𝑣 b 𝜃= 90 ∘ PC T  1 c 90 ∘<br>Projected data<br>GE 1<br>𝑝 features PC B  2<br>𝜃= 0 ∘<br>Background data  90 ∘<br>𝑝 features<br>𝑝 features<br>PC B  2<br>GE 1<br>PCT 2<br>PC T  1<br>GE 2<br>B  1PC<br> samples𝑛<br>(𝜌) B  2PC GE 1 T  1PC<br>samples𝑛+ 𝑚<br>samples𝑚<br><!-- End of picture text -->

Figure 2.1: _𝜌_ PCA finds directions that maximize target variance while minimizing background variance. **a,** _𝜌_ PCA is useful in a setting in which there are target datasets of interest with axes of interesting variation and background datasets with different axes of variation that should be removed before analysis. In the following example, the sample size _n = m = 1,000_ and the feature size _p=2_ . **b,** _𝜌_ PCA (black dashed line) finds the direction that maximizes the ratio of the target variance (direction of maximum target variance, dashed blue line) while minimizing the background variance (direction of minimum background variance, red dashed line). **c,** Variance of target (blue) and background (red) data projected on lines that pass through the origin from 0<sup>◦</sup> to 180<sup>◦</sup> , with the ratio of target to background variance (Rayleigh Quotient) shown below. Dashed lines correspond to the directions from **b** .

which is equivalent to maximizing tr( _𝑉_<sup>⊤</sup> Σ<sup>ˆ</sup> _𝑇𝑉_ ) subject to the constraint of background orthonormality _𝑉_<sup>⊤</sup> Σ<sup>ˆ</sup> _𝐵𝑉_ = _𝐼𝑑_ . Introducing a symmetric matrix of Lagrange multipliers Λ, the stationarity condition of the Lagrangian


with respect to _𝑉_ gives


or equivalently,


This is the matrix form of the generalized eigenvalue equation: each column of _𝑉_ is an eigenvector of (Σ<sup>ˆ</sup> _𝑇 ,_ Σ<sup>ˆ</sup> _𝐵_ ) and each diagonal entry of Λ its corresponding eigenvalue. The optimal _𝑉_ consists of the _𝑑_ generalized eigenvectors associated with the largest eigenvalues, which together span the _𝜌_ PCA subspace. This subspace maximizes the total target variance relative to background variance, and the constraint _𝑉_<sup>⊤</sup> Σ<sup>ˆ</sup> _𝐵𝑉_ = _𝐼𝑑_ ensures that the learned directions remain mutually orthogonal under the background inner product, _𝑣𝑖_<sup>⊤Σ</sup><sup>_𝐵𝑣𝑗_= 0 for</sup><sup>_𝑖_≠</sup><sup>_𝑗_.</sup>

13


<!-- Start of picture text -->
a b<br>𝜌PCA<br>c GE 1<br>𝜶= 𝟐𝟖. 𝟗𝟒<br>𝜶= 𝟎. 𝟎<br>𝜶= 𝟒𝟗𝟐. 𝟑𝟗<br>𝜶= 𝟔𝟐𝟑. 𝟓𝟓<br>Contrastive PC1<br>GE 2<br>Contrastive PC2<br><!-- End of picture text -->

Figure 2.2: _𝜌_ PCA recovers structure in biological subgroups without requiring parameter tuning or prohibitively long runtimes. **a,** Original Fig. 3a from [52] showing PCA and cPCA projections of protein expression from mice exposed to shock therapy, some of which developed Down Syndrome (DS) and some of which did not (non-DS). **b,** _𝜌_ PCA recovers separation of the two subgroups without searching over the contrastive parameter _𝛼_ . **c,** cPCA by default outputs projections at four values of _𝛼_ , with no guidance on how to select the best value.

### **Comparing** _𝜌_ **PCA and cPCA**

Given the heuristics and approximations underlying cPCA, we hypothesized that _𝜌_ PCA would be more effective at finding a projection that maximizes variance in a target dataset while minimizing variance in a background dataset.

To directly compare cPCA to _𝜌_ PCA on biological data, we applied _𝜌_ PCA to a dataset consisting of protein expression measurements from mice exposed to shock therapy [52], some of which developed Down Syndrome (DS) and some of which did not (non-DS). As reported in [52], performing PCA on the shock-treated mice data does not reveal distinct protein expression between those that developed Down Syndrome and those that did not. Introducing as a background protein expression measurements from non-DS mice that had not received shock therapy, _𝜌_ PCA finds an effective projection without any parameter tuning (Fig 2.2). cPCA projections reported in [52] as well as those obtained when running cPCA with default parameters produce different projections at different values of _𝛼_ , without clear guidance

14

given on how to choose the best value. Moreover, in an improvement with respect to cPCA, the _𝜌_ PCA projection shows different protein expression patterns between the DS and non-DS mice (Fig 2.2).

### _𝜌_ **PCA for Biological Discovery**

To demonstrate the interpretability and scalability of _𝜌_ PCA, we performed an analysis of a large single-nucleus RNA-seq dataset profiling kidney in mice [58]. We applied _𝜌_ PCA to a target dataset of four female mice with a "background" of four male mice in order to identify cell type specific variation in female gene expression that is distinct from the variation in males. After filtering out low quality nuclei and selecting highly expressed and highly variable genes dataset, we analyzed 2,000 genes from 47,798 female nuclei and 42,142 male nuclei of 17 different cell types. While a typical analysis might focus on genes that are differentially expressed (mean or rank differences) between male and female cell types, _𝜌_ PCA provides a new interpretation of sexually dimorphic gene expression as genes that are _variable_ primarily in the target group (female) and not in the background group (male).

The coefficients (loadings) of _𝜌_ PCA generalized eigenvectors are analogous to PCA loadings, but in this case highlight genes displaying variation among females that is absent from males (Fig. 2.3). These genes are not identified in a standard application of PCA: unsurprisingly, the genes with the highest loadings on GE 1 and GE 2 are not the genes with the highest loadings on PC 1 and PC 2 (Fig. 2.3a).

The variance of projected samples onto each generalized eigenvector also yields insights intothe particular celltype driving themain axes offemale specific variation. We projected male and female nuclei onto the first and second GEs and calculated the variance per cell type and sex (for all cell types, see Supplementary Fig. 2 in [44]). We then took the ratio of female to male variance, which is the Rayleigh quotient _𝜌_ of each GE. We find that GE 1 has the highest female to male Rayleigh quotient in proximal tubule (PT) epithelial cells, while GE 2 has the highest ratio in adipocytes (Fig. 2.3b,c, with absolute variances shown in Supp. Fig. 3 of [44]). As the first generalized eigenvector is the axis that explains the most variation in the target after having accounted for variation in the background, this suggests that of the tested cell types, females show the most unique variability in PT epithelial cells. This is consistent with previous studies: the PT is known to show strong sexually dimorphic gene expression patterns, reported to be regulated by hormone receptors (androgen and estrogen) [59, 60].

15


<!-- Start of picture text -->
a b<br>Proximal Tubule Epithelial Cells<br>Adipocytes<br>GE 1  GE 2  PC 1  PC 2  Loading<br>magnitude 𝜌  (Female variance / Male variance)<br>c d Top gene, GE  1  Top gene, GE  2  Top gene, PC  1  Top gene, PC  2<br>Proximal tubule  Proximal Tubule Epithelial Cells<br>epithelial cells<br>𝜌= 53.3 𝜌= 10.6<br>GE 1 GE 2 Variance: Mean: 2.180 2.026  0.356          3.550 1.292  0.840            0.050          0.058           0.029          0.034            0.066   0.039 0.3340.218  0.019     0.014<br>Adipocytes<br>Adipocytes<br>𝜌= 18.0 𝜌= 16.4<br>GE 1 GE 2 Variance: 0.039Mean: 0.023 0.1410.061 0.952  0.596  0.623          0.811           0.302           0.715  0.845    0.589         0.044           0.062            0.132 0.068<br>Top GE  genes<br>Cell type<br>Top PC  genes<br>Cell density Expression<br>Cell density Expression<br><!-- End of picture text -->

Figure 2.3: _𝜌_ PCA analysis of snRNA-seq data from male and female mice reveals genes driving female-specific variation across cell types that PCA fails to identify. **a,** Loadings for the three genes with the greatest magnitude loadings on the first and second generalized eigenvectors (GE 1 and GE 2 respectively) and the first and second principal components (PC 1 and PC 2 respectively): _𝜌_ PCA highly weights different genes than PCA. **b,** The ratios of variance of female to male nuclei projected onto the first and second GEs for 16 cell types in the kidney. GE 1 separates female proximal tubule epithelial cells, while GE 2 has the highest variance ratio for adipocytes. **c,** Histogram of male and female proximal tubule epithelial cells (orange) and adipocytes (green) projected onto the first and second generalized eigenvectors. **d,** _Acsm2_ (gene with the highest magnitude on GE 1), _Erbb4_ (gene with the highest magnitude on GE 2), _Meis2_ (gene with the highest magnitude on PC 1), and _Slit2_ (gene with the highest magnitude on PC 2) expression in male and female nuclei, separated by cell type (proximal tubule epithelial cells, top row, and adipocytes, bottom row).

As expected, the male and female specific expression patterns for the genes driving GE 1 and GE 2 show strong differences in variance. The counts distributions for _Acsm2_ (top gene for GE 1) and _Erbb4_ (top gene for GE 2) are indeed more variable in females than in males in PT epithelial cells and adipocytes, respectively (Fig. 2.3d), while the top genes for PC 1 ( _Meis2_ ) and PC 2 ( _Slit2_ ) do not show clear differences in variation. It is interesting that while _Acsm2_ is more variable in females than in males in the PT, it has a lower mean expression in females than males. While this gene has been previously noted to have male-biased expression in PT cells [61], _𝜌_ PCA identifies that it displays female specificity in the second moment. This variance across cells in females is interesting in light of [62], which suggests that _Acsm2_ is controlled by androgen in PT cells; each cell may be responding to differences in hormone concentration across the PT. While _ErbB4_ , the gene that codes for the

16

receptor protein-tyrosine kinase with roles in cell signaling and growth, is not as well studied, another growth-regulating receptor of the _ErbB_ family, _ErbB1_ , is known to have sex-biased expression in the kidney and to be sensitive to changes in sex hormones [63]. These examples illustrate the potential of _𝜌_ PCA as a computational approach for identifying genes whose cell-to-cell variation may have functional significance [64].

### **Discussion**

Indeed, it is no accident that the _𝜌_ PCA objective has been used for dimension reduction since the introduction of LDA in 1936 [56], and has been rediscovered in various fields. For example, the extraction of common spatial patterns method (CSP) of [65] at its core involves maximizing a Rayleigh quotient, where the target and background covariance matrices are derived from two distinct signal conditions [66]. The resulting generalized eigenvectors define spatial filters that maximize variance in one condition while minimizing variance in the other. CSP has become one of the most popular algorithms for brain computer interface design [67]. One reason that maximizing the _𝜌_ PCA objective works well in practice is that _𝜌_ PCA can be viewed as a restricted Gaussian maximum-likelihood estimator analogous to classical LDA [68, 69]. In this view, target and background data arise from Gaussians whose covariances differ by a structured latent component, and the _𝜌_ PCA solution is the large-sample maximum-likelihood solution. This probabilistic interpretation differs fundamentally from the contrastive latent variable model of Severson, Ghosh, and Ng [70], in which both target and background distributions are generated by shared and condition-specific latent variables and the full joint likelihood is maximized. The models of [68] and [69] provide asymptotic insight into _𝜌_ PCA, in contrast to the finite-sample likelihood maximization of probabilistic PCA [71]. Moreover, the expectation–maximization (EM) algorithm of [69] offers an analog of the EM algorithm of [72] for probabilistic PCA.

The _𝜌_ PCA method is also powerful due to its efficiency and scalability, making it much more suited to genomics applications than cPCA. We found that _𝜌_ PCA is much faster than cPCA. For example, in an analysis of a dataset with 10,000 samples and 1,000 features, cPCA takes almost two minutes to run, while _𝜌_ PCA runs in only a few seconds on the same machine, a speedup of two orders of magnitude. The difference in runtime between _𝜌_ PCA and cPCA is even more dramatic as the number of samples and features increases (Fig. 2.4). Analyzing data at increasingly large scales, such as single-cell RNA sequencing data with hundreds of thousands, or

17


<!-- Start of picture text -->
a b<br>cPCA<br>𝜌PCA<br>cPCA<br>𝜌PCA<br>1,000 features<br><!-- End of picture text -->

Figure 2.4: We use snRNA-seq data from mouse kidney to illustrate that _𝜌_ PCA is orders of magnitude faster than cPCA and remains efficient as **a,** number of samples (with fixed 2,000 features) and **b,** number of features (with fixed 1,000 samples in target and 1,000 samples in background) grow. Note that when samples have more than 1,000 features, cPCA first performs PCA to restrict the number of features to 1,000 (black dashed line).

even millions, of cells and genes, would require prohibitively long run times with cPCA.

In summary, the Rayleigh quotient provides an effective unifying principle for linear contrastive learning. This observation can lead to a consolidation of contrastive methods across fields.

18

### **2.2 Solving the Rayleigh Quotient for Functional Data**

In the previous section, it was described how contrastive PCA problems can be written as solutions to generalized eigenvalue problems that maximize particular instantiations of the Rayleigh quotient. In this section, we discuss how understanding this framework leads to useful and creative extensions of _𝜌_ PCA; i.e., solving the Rayleigh quotient in the space of basis function coefficients (f- _𝜌_ PCA) to find modes of variation in functional data. This extension expands the scope of contrastive PCA while unifying disparate fields of contrastive dimensional reduction and functional methods within a single conceptual and mathematical framework. We showcase the utility of this extension with an analysis of gene expression in immune response to vaccination.

This section summarizes content from [45] by M.C.<sup>∗</sup> , K.J.<sup>∗</sup> and L.P.<sup>∗</sup> , where ∗ denotes co-first authorship. M.C., K.J., and L.P. developed the methods, produced the results and drafted the manuscript. M.C. worked on functional _𝜌_ PCA, while K.J. worked on spatial _𝜌_ PCA.

### **Functional PCA**

Functional PCA (fPCA) is a technique that extends PCA to reduce the dimensionality of data that can be represented as curves or functions over a continuous domain (e.g., time or space) by finding dominant “modes of variation” [73, 74]. In this setting, _𝑛_ independent observations _𝑋𝑖_ ( _𝑡_ ) _, ..., 𝑋𝑛_ ( _𝑡_ ) are considered realizations of a square-integrable stochastic process _𝑋_ ( _𝑡_ ) over the continuous variable _𝑡_ . Let _𝜇_ ( _𝑡_ ) = _𝐸_ [ _𝑋_ ( _𝑡_ )] and _𝑐_ ( _𝑠, 𝑡_ ) = Cov( _𝑋_ ( _𝑠_ ) _, 𝑋_ ( _𝑡_ )) = _𝐸_ [( _𝑋_ ( _𝑠_ ) − _𝜇_ ( _𝑠_ ))( _𝑋_ ( _𝑡_ ) − _𝜇_ ( _𝑡_ ))] be the mean function and covariance function of the process _𝑋_ ( _𝑡_ ), respectively. The covariance operator _𝐶_ : _𝐿_<sup>2</sup> (T) → _𝐿_<sup>2</sup> (T) acts on square-integrable functions _𝑓_ ( _𝑠_ ) ∈ _𝐿_<sup>2</sup> (T) as


As _𝐶_ is compact, self-adjoint (symmetric, or _𝑐_ ( _𝑠, 𝑡_ ) = _𝑐_ ( _𝑡, 𝑠_ )), and positive semidefinite (∫T ∫T<sup>_𝑓_(</sup><sup>_𝑠_)</sup><sup>_𝑐_(</sup><sup>_𝑠, 𝑡_)</sup><sup>_𝑓_(</sup><sup>_𝑡_)</sup><sup>_𝑑𝑠𝑑𝑡_≥0), by Mercer’s theorem, the function</sup><sup>_𝑐_(</sup><sup>_𝑠, 𝑡_)</sup> can be expressed as


19

where the _𝜙𝑘_ are the eigenfunctions of _𝐶_ satisfying _𝐶𝜙𝑘_ = _𝜆𝑘 𝜙𝑘_ and _𝜆_ 1 ≥ _𝜆_ 2 ≥ _..._ ≥ 0. The orthonormality of eigenfunctions requires ∫T<sup>_𝜙𝑘_(</sup><sup>_𝑡_)</sup><sup>_𝜙𝑙_(</sup><sup>_𝑡_)</sup><sup>_𝑑𝑡_= 0 for</sup><sup>_𝑘_≠</sup><sup>_𝑙_and</sup> ∫T<sup>_𝜙𝑘_(</sup><sup>_𝑡_)</sup><sup>_𝜙𝑙_(</sup><sup>_𝑡_)</sup><sup>_𝑑𝑡_= 1 for</sup><sup>_𝑘_=</sup><sup>_𝑙_.</sup>

fPCA seeks to find orthogonal functions that capture the most variation in _𝑋_ ( _𝑡_ ), or, analogously to PCA, maximize the variance of the integral inner product (the process projected onto the new function):


Recalling the eigendecomposition of _𝐶_ , the functions that capture the most variation are the eigenfunctions _𝜙𝑘_ ( _𝑡_ ), which form a basis for _𝐿_<sup>2</sup> such that each process _𝑋𝑖_ ( _𝑡_ ) can be written as


Each observation _𝑖_ has weights _𝜃𝑖𝑘_ associated with each eigenfunction _𝑘_ that capture how strongly the eigenfunction contributes to the observation.

Practically, fPCA is implemented in one of two ways. In the first approach, observations are sampled on a grid of points over the continuous variable, and traditional PCA is employed on the resulting matrices. The eigenvectors can be interpolated between discrete features to produce eigenfunctions over a continuous feature space [74]. In the second approach, samples are first represented as combinations of a finite set of basis functions (e.g., B-splines, monomials, or Fourier coefficients). PCA is then performed on the coefficients of the bases (taking into account the non-orthogonality of basis functions if necessary) to find eigenvector coefficients for the set of basis functions [74, 75].

fPCA has been adapted to various settings. For example, it has been used to fit observations sampled at irregular or sparse time-points by smoothing covariance and mean functions [76], combined with mixed-effect models [77], and applied to adjust for known covariates [78]. A recent attempt to implement a contrastive version with

20

target and background functional data has been proposed that mimics the contrastive PCA method of [52] by subtracting from the target covariance function a weighted version of the background covariance function [79]. This approach to contrastive fPCA inherits the same problems as the [52] contrastive PCA method [44], including the issue that a difference of positive semi-definite matrices may not be positive semidefinite, and requiring a tunable contrastive parameter that can produce arbitrary eigenfunctions [45]. We show that contrastive functional dimension reduction can be achieved more naturally by performing _𝜌_ PCA in the space of basis coefficients, as shown in Figure 2.5A, leading to meaningful modes of variation present in target curves and absent in background curves.

### **Solving f-** _𝜌_ **PCA**

The f- _𝜌_ PCA method solves the Rayleigh Quotient generalized eigenproblem for functional data. We consider _𝑛_ independent observations _𝑋𝑖_ ( _𝑡_ ) _, ..., 𝑋𝑛_ ( _𝑡_ ) of some square-integrable stochastic process _𝑋_ ( _𝑡_ ), which we are interested in as a target process, and _𝑚_ independent observations _𝑌𝑖_ ( _𝑡_ ) _, ...,𝑌𝑚_ ( _𝑡_ ) of a different square-integrable stochastic process _𝑌_ ( _𝑡_ ), which we treat as a background process.

Let _𝜇𝑍_ ( _𝑡_ ) = _𝐸_ [ _𝑍_ ( _𝑡_ )] and _𝑐𝑍_ ( _𝑠, 𝑡_ ) = Cov( _𝑍_ ( _𝑠_ ) _, 𝑍_ ( _𝑡_ )) = _𝐸_ [( _𝑍_ ( _𝑠_ ) − _𝜇𝑍_ ( _𝑠_ ))( _𝑍_ ( _𝑡_ ) − _𝜇𝑍_ ( _𝑡_ ))] be the mean and covariance functions of the processes _𝑍_ ( _𝑡_ ), where _𝑍_ ∈ { _𝑋,𝑌_ } indicates target or background, respectively. The covariance functions are kernelsfortargetandbackgroundcovarianceoperators: ( _𝐶𝑍 𝑓_ )( _𝑡_ ) = ∫T<sup>_𝑐𝑍_(</sup><sup>_𝑠, 𝑡_)</sup><sup>_𝑓_(</sup><sup>_𝑠_)</sup><sup>_𝑑𝑠_.</sup> We seek to find functions _𝜙_ ( _𝑡_ ) that maximize the Rayleigh quotient:


requiring that _𝐶𝑌_ is positive definite on its domain, or ⟨ _𝐶𝑌 𝑓, 𝑓_ ⟩ _>_ 0 for non-zero functions _𝑓_ (e.g., covariance operators for non-degenerate Gaussian processes [80]).

**Discrete domain:** In practice, when functional observations have been measured at _𝑝_ discrete points, or _𝑋_ ∈ R<sup>_𝑛_×</sup><sup>_𝑝_</sup> and _𝑌_ ∈ R<sup>_𝑚_×</sup><sup>_𝑝_</sup> , target and background sample covariance matrices Σ<sup>ˆ</sup> _𝑋_ and Σ<sup>ˆ</sup> _𝑌_ can be calculated and the discrete _𝜌_ PCA objective solved [44]:


21

for discrete eigenvectors _𝑣_ ∈ R<sup>_𝑝_</sup> . These eigenvectors can be interpolated between discrete features for continuous support [74].

**Basis representation** : Alternatively, and commonly when data is irregularly or sparsely sampled, the Rayleigh quotient can be solved using a basis function representation for samples, as in functional PCA [74]. Full details are included in the associatedpublication’sSupplementalMethods[45]. Briefly, _𝐵_ ( _𝑡_ ) = ( _𝑏_ 1( _𝑡_ ) _, ..., 𝑏𝐷_ ( _𝑡_ ))<sup>_𝑇_</sup> , a set of linearly independent basis functions, are fit to each sample:


All _𝑛_ observations can be written in matrix form, _𝑋_ ( _𝑡_ ) = _𝐴𝑋 𝐵_ ( _𝑡_ ), where the matrix _𝐴𝑋_ ∈ R<sup>_𝑛_×</sup><sup>_𝐷_</sup> contains _𝑛_ rows, one per observation, of coefficients for the _𝐷_ basis functions. The background can be similarly fit and represented as _𝑌_ ( _𝑡_ ) = _𝐴𝑌 𝐵_ ( _𝑡_ ). The Rayleigh quotient is then optimized to find eigenvectors **w** in coefficient space, using the bases’ Gram matrix _𝐺_ ∈ R<sup>_𝐷_×</sup><sup>_𝐷_</sup> with entries _𝐺 𝑘𝑙_ = ∫T<sup>_𝑏𝑘_(</sup><sup>_𝑡_)</sup><sup>_𝑏𝑙_(</sup><sup>_𝑡_)</sup><sup>_𝑑𝑡_to</sup> account for possible non-orthogonality of functions:


The resulting coefficient vectors **w** are then converted back to the original data space to find eigenfunctions _𝑣_ ( _𝑡_ ) = **w**<sup>_𝑇_</sup> _𝐺_<sup>1/2</sup> _𝐵_ ( _𝑡_ ).

### **f-** _𝜌_ **PCA Application to Longitudinal Bulk RNA-seq**

Measurement of blood transcriptomes is an effective way to profile immunological responses before and after vaccination, with the goal of guiding the design of vaccination protocols for best conferred protection and reduction of adverse events [82]. To demonstrate the ability of f- _𝜌_ PCA (Fig. 2.5A) to extract functional patterns from longitudinal data, we applied it to bulk RNA-seq samples collected over a twoweek time course before and after a first and second dose of COVID-19 mRNA vaccines [81]. In the study, blood from 23 subjects was sampled immediately before, for 9 days after and 14 days after vaccination (a total of 11 time points) for both an initial “primer” and a secondary “booster” vaccination (Fig. 2.5B). The original study performed gene set enrichment analyses on the first and second doses

22


Figure 2.5: **A.** Diagram of functional _𝜌_ PCA (f- _𝜌_ PCA) using a basis representation. Target and background samples are measured at discrete time points, then fit to a set of basis functions to approximate the underlying continuous process. Functional _𝜌_ PCA calculates the covariance of the fit coefficients, accounting for non-orthogonality of basis functions using the Gram matrix of basis functions, then finds solutions to the Rayleigh quotient. Generalized eigenfunctions are recovered by converting the obtained generalized eigenfunctions back to original data space (e.g., time). **B.** We applied f- _𝜌_ PCA to longitudinal bulk RNA-seq conducted on patients before and after a first (“primer”) and second (“booster”) dose of a COVID-19 mRNA vaccine (diagram adapted from [81]). **C.** Ratio of the variance of target (“booster”) samples projected onto the first found eigenfunction to background (“primer”) samples projected onto the first eigenfunction for 86 interferon genes. **D.** For four genes with the largest target to background variance ratio, we show the gene expression values of primer and booster samples (mean line and shaded standard deviation over the samples indicated), the values over time of the first eigenfunction (f-GE1 weight), and violin plots of the distributions of target and background samples projected onto the first eigenfunction (fGE1 score). Target samples’ projections display higher variance than background samples.

23

separately. They subsequently compared the number and function of significant gene modules to understand how primer and booster responses differed. We applied f- _𝜌_ PCA to contrast the two time courses jointly, using the first dose as “background” and the second dose as “target,” and identified key genes that differ between the doses.

[81] report that a set of interferon genes (referred to as module A28 [83, 81]) have the most significant response in the first three days after primer administration. Focusing on this set, we obtained fit basis functions to the normalized expression profile for each gene. We then performed f- _𝜌_ PCA on the gene profiles that passed quality control for a total of 86 genes with contrastive analyses (Fig. 2.5C). The first eigenfunctions have high values at the points in time most variable in the booster that are not variable in the primer (Fig. 2.5D); for the analyzed interferon genes, there is a peak at the initial administration, consistent with the original paper’s observation that after the second dose “the interferon response was noticeably sharper in comparison to the response observed following the first dose and peaked on day 1 instead of day 2” [81]. We also projected fit samples onto the discovered first eigenfunctions for these genes and calculated the ratio of variance of booster samples to primer samples, finding that genes display a range of target and background sample separability (Fig. 2.5C).

The four genes with the highest booster to primer variance ratio, _GBP2, ISG20, SP110_ , and _LAP3_ , have previously been associated with SARS-CoV-2 (for expression profiles over all fit samples, see Supp. Fig. S4 of [45]). _GBP2_ , which codes for the GTPase guanylate-binding protein 2, inhibits the cleavage of the SARS-CoV-2 spike protein, thus affecting membrane fusion and viral entry [84]. Interferonstimulated gene 20 (coded for by _ISG20_ ) is an antiviral RNA exonuclease that has degraded RNA vectors derived from SARS-CoV-2 replicons [85]. _SP110_ was identified as significantly associated with extreme COVID-19 phenotypes [86]; and _LAP3_ , shown to have increased expression during COVID-19 infection [87], also exhibits poly(A)-tail elongation in patients with COVID-19 compared to controls [88]. These examples demonstrate that f- _𝜌_ PCA can be used to contrast two time courses of gene expression immune response in a single analysis, a complementary approach to performing post hoc comparisons of two separate analyses.

24

### **Discussion**

We have shown that f- _𝜌_ PCA identifies modes of variation that distinguish two groups of functional observations. Crucially, f- _𝜌_ PCA can operate in the space of basis function coefficients in addition to on discrete measurements, producing eigenfunctions that are directly interpretable as temporal modes of variation. The result is that f- _𝜌_ PCA is well-suited for experimental designs involving paired and sequential conditions, such as dose comparisons or longitudinal case-control studies. In cases where the goal is to identify functional differences in the response between groups, f- _𝜌_ PCA unifies the comparative analysis rather than requiring pairwise posthoc tests. Moreover, f- _𝜌_ PCA can, in principle, be extended to joint analysis of several features, incorporated as multivariate functional observations rather than treated independently. However, such an extension requires a framework for performing tensor SVD that retains the spectral properties of its lower dimensional counterparts. This remains an area of active research [89].

The Rayleigh quotient formulation of _𝜌_ PCA extends this approach by providing a mechanism for performing contrastive analysis and by unifying these problems analytically, showing that they can be interpreted as the same generalized eigenvalue problem. Finally, the examples presented in this work demonstrate that both methods can recover biologically relevant signals from complex genomic datasets. We anticipate that this practical, flexible approach will find broad utility across biological domains.

25

_C h a p t e r 3_

---

[← INTRODUCTION](06-introduction.md) · [Up: contents](index.md) · [BIOPHYSICAL MODELS FOR STOCHASTIC TRANSCRIPTION →](08-biophysical-models-for-stochastic-transcription.md)
