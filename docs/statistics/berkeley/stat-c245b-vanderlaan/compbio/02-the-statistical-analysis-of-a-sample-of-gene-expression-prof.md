---
title: The Statistical Analysis of a Sample of Gene Expression Profiles
source: https://vanderlaan-lab.org/teach-files/compbio.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/compbio.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Statistical Analysis of a Sample of Gene Expression Profiles

**Source:** [`compbio.pdf`](https://vanderlaan-lab.org/teach-files/compbio.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##### ABSTRACT

Recent developments in microarray technology make it possible to capture the gene expression profiles for thousands of genes at once. With this data researchers are tackling problems ranging from the identification of “cancer genes” to the formidable task of adding functional annotations to our rapidly-growing gene databases. Specific research questions suggest patterns of gene expression that are interesting and informative (e.g. genes with large variance or groups of genes that are highly correlated). Cluster analysis and related techniques are proving to be very useful. We add to this the visualisation of the clusters by visualizing an ordered distance matrix van der Laan and Pollard (2001). However, such exploratory methods alone do not provide the opportunity to engage in _statistical inference_ . Given the high-dimensionality (thousands) and small sample sizes ( _<_ 30) encountered in these datasets, an honest assessment of sampling variability is crucial and can prevent the over-interpretation of spurious results. van der Laan, Bryan (2001) describe a statistical framework that encompasses many of the analytical goals in gene expression analysis; this framework is completely compatible with many of the current approaches and, in fact, can increase their utility. We propose the use of a deterministic rule, applied to the parameters of the gene expression distribution, to select a target subset of genes that are of biological interest. In addition to subset membership, the target subset can include information about relationships between genes, such as clustering. This target subset presents an interesting parameter that we can estimate by applying the rule to the sample statistics of microarray data. The parametric bootstrap based on a multivariate normal model, or the nonparametric bootstrap based on resampling from the observed data, is used to estimate the distribution of these estimated subsets and relevant summary measures of this sampling distribution are proposed. We focus, in particular, on rules that operate on the mean and covariance. Using Bernstein’s Inequality, we obtain consistency of the subset estimates, under the assumption that the sample size converges faster to infinity than the logarithm of the number of genes. We also provide a conservative sample size formula guaranteeing that the sample mean and sample covariance matrix are _uniformly_ within a distance _ϵ >_ 0 of the population mean and covariance. The practical performance of the method using a cluster-based subset rule is illustrated with a simulation study. The method is illustrated with an analysis of a publicly available leukemia data set.

11

### **2.1 Introduction**

#### **2.1.1 Microarray context**

Microarray studies are swiftly becoming a very significant and prevalent tool in biomedical research. The microarray technology allows researchers to monitor the expression of thousands of genes simultaneously. A readable introduction to microarrays can be found in Marshall (1999) and a more technical overview is given in the “The Chipping Forecast” [1999].

By comparing gene expression profiles across cells that are at different stages in some process, in distinct pathological states, or under different experimental conditions, researchers gain insight into the roles and reactions of various genes. For example, one can compare healthy cells to cancerous cells within subjects in order to learn which genes tend to be over (or under) expressed in the diseased cells; regulation of such genes could produce effective cancer treatment and/or prophylaxis. DeRisi et al. (1996) suppressed the tumorigenic properties of human melanoma cells and compared gene expression profiles among “normal” and modified melanoma cells; this experiment allowed investigators to study the differential gene expression that is associated with tumor suppression. Data analysis methods appropriate for microarray data are surveyed by Claverie (1999), Eisen et al. (1998), and Herwig et al. (1999).

Recent microarray studies have relied heavily on clustering procedures. Eisen et al. (1998) apply a hierarchical cluster analysis algorithm to an empirical correlation matrix and Golub et al. (1999) use a neural network algorithm called self-organizing maps (SOM) which, like K-means clustering and the partitioning around medoids (PAM) of Kaufman and Rousseeuw (1990), places objects into a fixed number of clusters. We feel that such approaches suffer from two deficiencies, which we address in this chapter. First, since these techniques are used in a purely data exploratory manner, they lack important notions such as parameter, parameter estimate, consistency and confidence. Second, techniques that are purely descriptive and _ad hoc_ make it difficult to design a study to meet particular goals.

#### **2.1.2 Overview of the statistical method**

For a randomly sampled subject or organism (from some population) we measure with the microarray experiment (as described previously) a relative gene expression profile for _p_ genes in one cell sample relative to a control cell sample. Let **X** be the _p_ -dimensional column vector of ratios representing the relative gene expression profile for a subject or cell line randomly drawn from a well-defined population. Suppose that we observe _n_ i.i.d. copies **X** 1 _, . . .,_ **X** _n_ of this random vector **X** , for example, one for each of _n_ randomly sampled subjects.

In the dataset that originally motivated this work, the population of interest is human colon cancer patients and for each subject we have a sample of healthy colon tissue (control) and colon tumor tissue (test). From such data, we want to find a subset of genes for which differential expression is associated with cancer. Below, we will show that two sample data sets or paired sample data sets can be naturally transformed to a one sample data set. For example, in the dataset we analyze in section 2.9, the population of interest is human acute leukemia patients described by Golub et al. (1999). The data actually arise from a microarray technology slightly different than the cDNA arrays described above, namely, an oligonucleotide produced by Affymetrix. In any case, the dataset contains expression profiles for patients with two distinct types of leukemia, namely ALL and AML. One can now define **X** as the gene expression profile of a ALL patient relative to the mean profile among the AML patients. Our data analysis in section 2.9 focuses on finding genes whose expression best distinguishes the two tumor classes

12

and are, therefore, useful in diagnosis.

In light of the typical scientific goals, we generally wish to find (1) genes that are _differentially expressed_ , e.g. expression is different in the test sample relative to the control, and (2) groups of genes which are _significantly correlated with each other_ . We are interested in genes whose expression levels tend to vary together, because such genes might be part of the same causal mechanism.

Since k-fold over-expression represents the opposite of k-fold under-expression, it is natural to use a logarithmic transformation: let _Yj_<sup>_∗_=log(</sup><sup>_Xj_)</sup><sup>_j_=1</sup><sup>_, . . ., p_.Inaddition,tocontrolthe</sup> effect of outliers and to obtain nonparametric consistency results proved later in this paper, we also propose to truncate the log-ratios by a user-supplied constant _M_ :


Another additional truncation would be to examine centered data _Yj_<sup>_∗−µ_�</sup><sup>_∗_</sup> _j_<sup>andtruncateall</sup> observations that were, for example, greater than 3 standard deviations in absolute value. Let **Y** be the column vector with component _j_ being equal to _Yj_ , _j_ = 1 _, . . ., p_ . Denote the expectation, covariance, and correlation of **Y** by **_µ_** , **Σ** , and **_ρ_** , respectively.

We do not require that **Y** is a gene expression profile, but it can be any high dimensional vector. In particular, if one is interested in finding binding sites on the regularitory DNA-region of a gene which predict gene expression, then it is preferable to define **Y** as a transformation of a gene expression profile defined by the DNA-sequence of the regularitory region. For example, each component of **Y** might correspond with a word of bases _{A, C, T, G}_ of length 6 and measure its importance in predicting gene expression for the randomly sampled subject or organism. The latter approach is studied in chapter 4 (Keles, van der Laan, Eisen, 2001). For the sake of clarity, in this chapter we will treat **Y** as a vector or gene expression profiles.

Suppose that we know **_µ_** and **Σ** , and that subject matter experts believe that certain patterns of gene expression distinguish specific genes as important. Then a natural question is “How should we select a subset ( **_µ_** _,_ **Σ** ) _→_ **S** ( **_µ_** _,_ **Σ** ) of genes that merit special attention?” We might also wish to regard **S** ( **_µ_** _,_ **Σ** ) as a set of genes that is subdivided into several groups labeled from 1 to _K_ . We can identify such a subset **S** ( **_µ_** _,_ **Σ** ) by a _p_ -vector **S** whose components take values in _{_ 0 _, . . ., K}_ . If _Sj_ = 0, then gene _j_ is excluded from the subset and if _Sj_ = _k_ , _k ∈{_ 1 _, . . ., K}_ , then gene _j_ is included in the subset and carries label _k_ . At times, we will also describe the subset as a set of gene indices _j_ , _j ∈{_ 1 _, . . ., p}_ ; this is equivalent to setting _Sj_ = 0 for genes not in the subset and to some integer between 1 and _K_ otherwise. Hereinafter _S ≡_ **S** ( **_µ_** _,_ **Σ** ) will represent the target subset of genes that we wish to distinguish as important.

As an example of a very simple rule, one could define **S** ( _·, ·_ ) as _{j_ : _µj > C}_ , for some _C >_ 0. A more sophisticated subset rule would be to (1) select those genes which are at least 3-fold differentially expressed w.r.t. the geometric mean (i.e. only include gene _j_ if _|µj| >_ log 3); and (2) construct a correlation-distance matrix for these differentially expressed genes from the appropriate elements of **_ρ_** ; and (3) apply a clustering algorithm to (some function of) this distance-matrix; and possibly (4) only include those genes in **S** that are closest to the cluster centers. In fact, most of the analytical techniques currently being applied to gene expression data (for example Eisen et al., 1998; Golub et al., 1999) operate on the mean and covariance and are, therefore, perfect candidates for the type of subset rule considered here. It is not necessary for the subset rule to eliminate genes at all, although it generally advantageous to do so. Even if the rule simply applies labels that have a stable meaning – for example, by employing a

13

supervised clustering technique that find clusters around pre-specified genes – the methods we propose would allow the analyst to assess the stability of these clusters.

Given a well-defined subset rule **S** ( _·, ·_ ), a natural estimate of the target subset _S_ is **S** � _n ≡_ **S** ( **_µ_** � _n,_ **Σ** � _n_ ), where **_µ_** � _n_ and **Σ** � _n_ are the sample mean and covariance, respectively, of the (truncated) data. We prove the consistency of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) and **S** ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) (see section 2.4) _nonparametrically_ when _n/_ log( _p_ ( _n_ )) _→∞_ and _M < ∞_ . The case where _p_ = _∞_ and _p >> n_ is extremely relevant, as microarray experiments already produce data on 20000 genes and in the future we will encounter datasets with all human genes (estimated to be between 35000 and 140000). In stark contrast, sample sizes often fall below 30. We also provide a nonparametric sample size formula that guarantees with probability at least 0 _< γ <_ 1 that the maximal difference between **_µ_** � _n_ and **_µ_** is smaller than _ϵ_ and similarly for **Σ**<sup>�</sup> _n_ and **Σ** . If one is willing to assume that **Y** _∼ N_ ( **_µ_** _,_ **Σ** ) has a multivariate normal distribution, then the truncation is not needed, but we aim to be as nonparametric as possible.

The sampling distribution of the estimated subsets **S**<sup>�</sup> _n_ provides valuable information for the analyst. One might wish to choose the sample size and/or subset rule in order to ensure the reproducibility of certain results or to realize some other performance measure. As an example of a feature we would hope to see reproduced in samples, consider a gene _j_ that appears in _S_ . For a particular data-generating distribution, sample size _n_ , and subset rule **S** ( _·, ·_ ), there is a probability _pj_ that gene _j_ will appear in the estimated subset **S**<sup>�</sup> _n_ produced by a randomly drawn sample; we will call such probabilities _pj_ “single-gene probabilities”. If the single-gene probabilities are low for many of the genes in _S_ , we might choose to increase the sample size or select a subset rule that is easier to estimate. If the single-gene probabilities are generally high, we might proceed with the study and, when we observe estimates of _pj_ that are close to 1, feel confident that those genes are in _S_ .

Since we want to determine the membership of a specific set, it is natural to apply conventional measures of test quality, such as sensitivity and positive predictive value, to any procedure we devise. In this context, sensitivity is the proportion of the target subset that also falls in the estimated subset and positive predictive value is the proportion of the estimated subset that is also in the target subset.

Determining single-gene probabilities and the distribution of subset quality measures requires knowledge of the actual sampling distribution of **S**<sup>�</sup> _n_ . In order to estimate these quantities we use the parametric or nonparametric bootstrap. In general, the asymptotic validity of the parametric bootstrap requires that the chosen parametric model be correct. However, as long as we choose a parametric model that places no constraints on ( **_µ_** _,_ **Σ** ), even when it is incorrect, the parametric bootstrap will still consistently estimate the degenerate limit distribution of _S_ ( _µn, Sigman_ ) and _S_ ( _µn_ ). Specifically, we use as parametric model the multivariate normal model **Y** _∼ N_ ( **_µ_** _,_ **Σ** ) and, based on the data we have seen, we believe this to be a reasonable choice after truncation.

The bootstrap (Efron and Tibshirani, 1993) was first used to investigate the reproducibility of certain features of phylogenetic trees by Felsenstein (1985). Efron and Tibshirani (1998) later took up this problem more generally and termed it the “problem of regions”. They ask: given an interesting feature in an observed descriptive statistic, how confident can we be that this feature is present in the data-generating distribution? Efron and Tibshirani also link this confidence measure, in certain settings, to frequentist _p_ -values and Bayesian a posteriori probabilities.

14

#### **2.1.3 Application to paired and unpaired comparisons**

Now suppose we have two sets of relative gene expression measurements ( **X** _,_ **Y** ) on a common set of _p_ genes that we wish to compare. Such data can arise under two different scenarios: paired and unpaired. In the paired scenario, we have two observations on each subject. For example, gene expression might be measured on a cell line at two different time points in the cell cycle relative to a baseline. Or we might observe the same subject before and after treatment. Perou et al. (2000), for example, analyzed gene expression in human breast cancer tumors before and after chemotherapy using a common reference sample. In the unpaired scenario, we have observations on subjects drawn from two subpopulations of subjects (possibly with different numbers of observations in each subsample). Golub et al., for example, used gene expression data to distinguish between acute lymphoblastic leukemia (ALL) and acute myeloid leukemia (AML).

We might want to focus on genes that appear to be very differently expressed in the two data sets. One approach is to simply analyze the two data sets separately and compare the clustering patterns. Another approach is to combine the two data sets into one data set. The way we do this depends on the scenario that generated the data. In the paired scenario, we can form a _p_ -dimensional vector of log ratios, log ( **X** _i/_ **Y** _i_ ), by dividing the relative expression for a subject at one time point by that at the other before taking the log. In the unpaired scenario, we can form a _p_ -dimensional vector of log ratios by dividing the relative expression for a subject by the geometric mean relative expression for all subjects in the other subpopulation before taking the log so that we get log ( **X** _i/µ_ ˆ _Y_ ). For both scenarios, the empirical mean of the combined data set is the difference between the two sample means of the log ratios in the two separate data sets.

### **2.2 The estimated subset and the bootstrap**

#### **2.2.1 Subset rules**

We propose several simple, but easily interpretable, subset rules and all are simply functions of the parameters ( **_µ_** _,_ **Σ** ). We have found it natural to divide the subset rule into three phases: (1) a pre-screen in which certain genes are eliminated; (2) a mid-rule in which inter-relationships between genes are sought; and (3) a post-screen in which even more genes are eliminated. We emphasize that it is not necessary to employ all three phases of the rule and, therefore, a clustering algorithm alone can be regarded as an example of such a rule, whenever the distance metric is a function of ( **_µ_** _,_ **Σ** ). For example, this is the case with Euclidean distance, correlation distance, the modified correlation distance proposed by Eisen et al. (1998), and principal component based metrics. From now on, we denote the distance between genes _i_ and _j_ by _Dij_ , the _p_ by _p_ symmetric matrix of such distances by **D** , and we assume that **D** is determined by ( **_µ_** _,_ **Σ** ).

Table 2.1 presents examples of the rules and metrics one can work with. A common requirement for inclusion in the subset is _differential expression_ and we use the pre-screen to retain only those with sufficient evidence of differential expression. The table presents pre-screens that range from very simple cutoffs to those that determine whether a certain proportion _p_ of the population exhibits a sufficient level log( _δ_ 1) of over and/or under (determines expression. We then seek groups of genes that tend to be coexpressed; a clustering algorithm, such as PAM (Kaufman and Rousseeuw, 1990, chap. 2), is a typical mid-rule, but many other clustering and neural network algorithms are also suitable. Finally, since clustering algorithms place all objects

15

Table 2.1: Subset rule examples.

|Pre-screen|Distance metric|Mid-rule|Post-screen|
|---|---|---|---|
|_µj_<br>_>_<br>log(_δ_1)|Euclidean<br>dis-<br>tance|PAM|_Dij < δ_2,|
|_|µj|_<br>_>_<br>log(_δ_1)|1_−|ρij|,_1_−ρij_|PAM,<br>with<br>fixed<br>medoids|for some cluster cen-<br>ter _i_|
|_|µj| >_|1 - Eisen’s modi-<br>fied|Self-organizing maps|_silhouettej > δ_2|
|log(_δ_1)<br>+<br>_σj_Φ<sup>_−_1</sup>(_p_)|correlation|Hierarchical clustering<br>K-means clustering|(part of PAM out-<br>put)|


into clusters, even if there is little evidence to favor one cluster assignment over another, we often use the post-screen to retain only those genes that appear to be well-matched to their cluster. One could use actual distances to cluster centers or members to make this determination or, as in the case of the “silhouettes” in PAM, there may be other useful output from the clustering procedure one can exploit.

#### **2.2.2 Partitioning Around Medoids (PAM).**

A particular subset rule _S_ ( _µ,_ Σ) is based on the output of the clustering procedure PAM (Kaufman and Rousseeuw, 1990, chap. 2), which takes as input a dissimilarity matrix **D** based on any distance metric. Let _Dij_ denote the dissimilarity between genes _i_ and _j_ where each gene is represented by an _n_ dimensional vector. Possible dissimilarities which are functions of Σ between these two _n_ -dimensional vectors are:


where


It is of interest to note that the 1 _− ρ_<sup>0</sup> _ij_<sup>equals 2timesthesquaredeuclideandistanceofthetwo</sup> vectors standardized to have euclidean norm 1. This distance was used in Eisen et al. (1998), and it has been our experience that it is a sensible choice in many applications.

Let _K_ be the number of clusters ( _i.e._ : the number of causal mechanisms we believe to be operating). Given _K_ , PAM selects _K_ potential medoids, calculates for each gene its distance to the closest of these potential medoids and minimizes over the vector of _K_ potential medoids the sum of these distances over all genes. The solution of this minimization problem is a vector of _K_ medoids. Each medoid identifies a cluster, defined as the genes which are closer to this medoid

16

than to any of the other _K −_ 1 medoids. Like any clustering routine which solves a minimization problem, PAM often converges to one of the many local minima, which is not necessarily the global solution. For example, by randomly permutating the rows of the data matrix, we can produce different choices of medoids and possibly different clustering labels for some genes which lie between one or more clusters. As a solution, we recommend randomly permutating the data matrix a large number of times to produce different starting values, rerunning PAM each time, and selecting the medoids which give the smallest sum of distances.

One can consider _K_ as given or it can be data-adaptively selected, for example, by maximizing the average silhouette as recommended by Kaufman and Rousseeuw. The silhouette for a gene is calculated as follows. For each gene _j_ , calculate _aj_ which is the average dissimilarity of gene _j_ with each other member of gene _j_ ’s cluster. For each gene _j_ and each cluster _k_ that is not gene _j_ ’s cluster, calculate _bjk_ , which is defined as the average dissimilarity of gene _j_ with the members of cluster _k_ . Let _bj ≡_ min _k bjk_ , where the minimum is taken over all clusters _k_ that are not gene _j_ ’s cluster. Finally, the silhouette of gene _j_ is defined by the formula:


Note that the largest this can be is 1, which occurs only if there is no dissimilarity within gene _j_ ’s cluster ( _i.e._ : _aj_ = 0). The other extreme is -1. Heuristically, the silhouette measures how well matched an object is to the other objects in its own cluster versus how well matched it would be if it were moved to another cluster.

The (minimal) output of PAM consists of two vectors: (1) a _p_ -dimensional vector **c** , where _cj_ = _k_ indicates that gene _j_ belongs to cluster _k_ , and (2) a _K_ -dimensional vector **m** , where _mk_ = _j_ indicates that the medoid of cluster _k_ is gene _j_ , where _j ∈{_ 1 _, . . ., p}_ and _k ∈{_ 1 _, . . ., K}_ . An attractive property of PAM is that the clusters are identified by the medoids, which are genes themselves, and it has been our experience that the medoids are stable representations of the clusters.

**Comparison with k-means** One of the most well known partitioning methods is k-means. In the k-means algorithm the observations are classified as belonging to one of _k_ groups. Group membership is determined by calculating the centroid for each group, the multidimensional version of the mean, and assigning each observation to the group with the closest centroid. The centroids are calculated by minimizing the sum over all elements of the squared-euclidean distance to its closest centroid. PAM has 2 crucial advantages relative to k-means. Firstly, k-means only allows clustering with respect to the euclidean distance, while PAM accepts any dissimilarity matrix as input. Secondly, PAM is more robust because it minimizes a sum of dissimilarities instead of a sum of _squared_ euclidean distances. The latter is particularly important in the context of clustering genes when many genes do not really belong to any cluster so that most clusters contain many badly clustered genes. In this situation the centroids of k-means will be heavily affected by the badly clustered genes, while the medoids are much more robust elements of the clusters. It has been our experience that the medoid-genes typically represent the strongly clustered component of the cluster.

### **2.3 Visualisation of clusters.**

We propose to visualize the clusters by 1) ordering the clusters 2) ordering the elements within the clusters and 3) visualising the ordered dissimilarity matrix with colors such as red (genes

17

are close) and green (genes are far apart). To be concrete, let’s consider the visualisation of the clusters of genes as obtained with PAM. Let _PAM_ ( _data, k, d_ ) represent the output of PAM when we give it the data set “data”, number of clusters _k_ and distance metric _d_ . Since the clusters are defined by the medoids one can order the clusters by just ordering the corresponding medoids.

**Ordering medoids.** We propose to order the medoids by building a hierarchical tree from the medoids with PAM as follows. Let “medoids.data” be the _k_ by _n_ matrix containing the _k_ medoids. Initially, we apply _PAM_ ( _medoids.data,_ 2 _, d_ ) and label the two clusters with clust1 and clust2. For each of the two clusters we can now define the neighboring cluster “clust-next”. Subsequently, at each node we apply PAM again with say _k_ = 2 and we now order the _k_ new clusters by their distance with respect to medoid of “clust-next” going from maximal distance to smallest distance if “clust-next” is to the right and from smallest distance to maximal distance if “clust-next” is to the left. In this way each level of the tree has an ordered list or clusters. By running down the tree until each cluster is of size one, we obtain a unique ordering of the _k_ medoids. Note that this ordering is based on the same dissimilarity measure as we used to cluster the original data set.

We also implemented the following ordering based on minimizing a criteria. Consider a particular ordering of medoids. For component _i_ and _j_ in this ordered list we have a distance _d_ ( _i, j_ ) between these two corresponding medoids. Compute now the empirical correlation between the distance _j − i_ in the list and the actual distance _d_ ( _i, j_ ) over all pairs ( _i, j_ ) _, i < j_ . We now compute the ordering of medoids which minimizes this empirical correlation. In all our data set examples the hierarchical PAM ordering of medoids corresponded with this optimized ordering of the medoids, but we do not claim they generally agree.

**Ordering genes within cluster.** Given the ordering of clusters, it remains to cluster the genes within the clusters. We choose to order the genes within each of cluster by either (i) their distance with respect to the medoid of that cluster so that the badly clustered genes end up at the edge of these clusters or (ii) their distance with respect to the medoid of the neighboring cluster.

#### **2.3.1 The parametric and nonparametric bootstrap.**

In order to establish the variability and reproducibility of the clustering output _S_ ( _µn,_ Σ _n_ ) ( _e.g._ the clusters in level _l_<sup>_∗_</sup> of the tree), we propose to run the parametric or nonparametric bootstrap. This involves repeatedly sampling _n_ observations _Y_ 1<sup>#</sup><sup>_, . . ., Y_</sup> _n_<sup>#from a multivariate normal distri-</sup> bution _N_ ( _µn,_ Σ _n_ ) (van der Laan and Bryan (2001)) or from the empirical distribution which puts mass 1 _/n_ on each of the original observations _Y_ 1 _, . . ., Yn_ . One estimates the distribution (and, in particular, the variance) of the clustering output _S_ ( _µn,_ Σ _n_ ), with the empirical distribution of _S_ ( _µn_<sup>#</sup><sup>_,_Σ#</sup> _n_<sup>).</sup>

Above we defined output _S_ ( _µn,_ Σ _n_ ) obtained by applying the PAM program to the empirical mean and covariance matrix _µn,_ Σ _n_ . In order to carry out the bootstrap it is important that _S_ ( _µn,_ Σ _n_ ) is defined as a deterministic rule applied to the data or a summary of the data ( _µn,_ Σ _n_ ): if the clustering output was based on visual inspection steps, then these need to be automated in order to satisfactorily carry out the bootstrap. Now, we carry out precisely the same procedure in each bootstrap sample.

Another clustering output is to simply apply PAM with fixed medoids. Since we have seen that the selection of medoids (but not so much the cluster assignments) may be dependent on the original order of the genes in the data set, it makes sense to select good medoids in the initial clustering as we have suggested above and then continue to use these in the bootstrap.

18

In order to establish the cluster variability when fixing the medoids, one fixes the medoids in the bootstrap. Note that this bootstrap avoids estimating the variability in the selection of the medoids. Nonetheless, it provides information about important components of the cluster variability. Since the medoids are the same in each bootstrap sample, we can keep track of the proportion of times a gene falls in each cluster. In other words, for each gene one keeps track of the proportion of times among the bootstrap samples the gene fell into each of the clusters. **?** propose a cluster-probability plot to summarize these statistics which provides a visual way to inspect the cluster reproducibility. These bootstrap cluster-specific probabilities can be used to order the genes within the clusters so that the badly clustered genes can be removed or end up at the edge of the clusters.

If the ordering of the clusters is not a parameter of interest, one might enforce an ordering of the bootstrapped clusters corresponding as close as possible to the ordering in _S_ ( _µn,_ Σ _n_ ) by comparing their medoids. In this way, one aims at measuring the variability of the actual clusters instead of the ordering. One can also plot the distance matrix ”distance( _k_ ( _l_<sup>_∗_</sup> ))” for a number of bootstrap samples and inspect the variability of the cluster structures visually.

**Specifics on the parametric bootstrap.** Our goal is to estimate the distribution of **S** � _n ≡_ **S** ( **_µ_** � _n,_ � **Σ** _n_ ) _∈{_ 0 _, . . ., K}_<sup>_p_</sup> , where ( **_µ_** � _n,_ **Σ** � _n_ ) are the observed mean and covariance matrix of a size _n_ sample from a _Np_ ( _M_ )( **_µ_** _,_ **Σ** ) distribution, where we will treat _K_ as fixed. The parametric bootstrap described below could also be used to address uncertainty of a data adaptively determined _K_ . The parametric bootstrap estimates the distribution of **S**<sup>�</sup> _n_ with the distribution of **S** � _n ≡_ **S** ( **_µ_** � _n,_ � **Σ** _n_ ), where ( **_µ_** � _n,_ **Σ** � _n_ ) are the observed mean and covariance matrix of a size _n_ sample from a _Np_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ). From this point on, sample quantities (first-generation draws from the datagenerating distribution) will be indicated by hats and bootstrap quantities (second-generation draws from statistics of an observed first-generation sample) with tildes.

When we draw from a _Np_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ), we will be faced with a singular covariance matrix **Σ**<sup>�</sup> _n_ when _n_ is smaller than _p_ . In that case we add to the diagonal elements of **Σ**<sup>�</sup> _n_ an arbitrarily small number _λ >_ 0, which produces a nonsingular covariance matrix that is extremely close to **Σ** � _n_ . This ensures that we are sampling from a well-defined distribution.

So, for _b_ = 1 _, . . ., B_ ( _B_ large), we draw _n_ observations (i.e. microarrays) **Y**<sup>�</sup> 1<sup>_b, . . .,_</sup><sup>**Y**�</sup> _n_<sup>_b_from</sup> _Np_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ), compute the observed statistics ( **_µ_** � _n_<sup>_b,_</sup><sup>**Σ**�</sup> _bn_<sup>), and record the estimated bootstrap subset</sup> **S** �<sup>_b_</sup> _n_<sup>=</sup><sup>**S**(</sup><sup>**_µ_**�</sup> _n_<sup>_b,_�</sup><sup>**Σ**</sup> _bn_<sup>).Thisprovidesuswith</sup><sup>_B_realizations</sup><sup>**S**�</sup> _n_<sup>1</sup><sup>_, . . .,_�</sup><sup>**S**</sup><sup>_B_</sup> _n_<sup>of</sup><sup>**S**�</sup><sup>_n_=</sup><sup>**S**(</sup><sup>**_µ_**�</sup> _n_<sup>_,_�</sup><sup>**Σ**</sup><sup>_n_).Weuse</sup> this observed distribution as an estimate of the distribution of **S**<sup>�</sup> _n_ and, for _n_ large enough, one can view the sampling distribution of **S**<sup>�</sup> _n_ as an estimate of the distribution of **S**<sup>�</sup> _n_ = **S** ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ).

##### **Important features of the sampling distribution.**

To be specific, consider one of the cluster-based subset rules. Because of the high dimensionality of **S**<sup>�</sup> _n_ , we limit our focus to certain aspects of the empirical distribution of **S**<sup>�</sup> _n_ . Note that the values and/or distributions of the quantities defined in this section certainly depend on the sample size _n_ ; we will employ notation with and without the _n_ , depending on the context.

19

Indicate the size of a set _A_ by _|A|_ . Let


The quantities _pj_ , _Pij_ , and _Qij_ are referred to collectively as “feature-specific probabilities”. The random variables _sens_ and _ppv_ are will be called “quality measures”. It is important to note that the concepts of sensitivity and predictive value as employed here differ from their epidemiological counterparts, in that the _p_ genes are not assumed to be i.i.d. Since these quantities are functions of the estimated subset, the distribution of sensitivity and positive predictive value are to be considered when evaluating a proposed subset rule.

The significance of sensitivity is rather obvious, but we would like to emphasize the importance of positive predictive value as well. If scientists use the estimated subset **S**<sup>�</sup> _n_ as a means for selecting a relatively small set of genes for intensive study, it is crucial that the predictive value be high, since a great deal of time and money could be wasted otherwise. This is especially relevant when _p_ is very large. Since an estimated subset for which 50% of the genes are false positives might not be considered usable, information on the predictive value of the estimated subset could alert researchers to the need to collect more data or to choose a different subset rule.

The bootstrap analogue of the above feature-specific probabilities is the empirical frequency in the bootstrap replicates of the appropriate event. Likewise the bootstrap estimate of the distribution of a quality measure will be based on the appropriate empirical proportions. For example, _p_ � _j_ = _p_ � _j,n_ = _B_<sup>1</sup> � _b_<sup>_I_(</sup><sup>_S_�</sup> _j_<sup>_b>_0)and</sup> _sens_<sup>�</sup><sup>_b_</sup> = _sens_ �<sup>_b_</sup> _n_<sup>=</sup><sup>_|_</sup><sup>**S**�</sup><sup>_∩_</sup><sup>**S**�</sup><sup>_b|/|_</sup><sup>**S**�</sup><sup>_|_.Allofthesequantities</sup> are retained in the bootstrap. For practical reasons, we focus on the single-gene probabilities, _pj_ , and sort the genes in descending order based on this. We report the top-ranked genes and ensure that all members of **S**<sup>�</sup> _n_ are included. In such a list, the genes which fall “deep” into the target subset _S_ will typically appear before the genes which barely qualified for inclusion into _S_ . The scientist can begin carefully investigating the top ranked genes.

In some settings, there may be a subset of genes that are not only excluded from the target subset _S_ , but are regarded as particularly unsuitable for further study. The definition of such genes is completely up to the user, but will generally correspond to genes that lie _far_ outside the target subset. We will denote this subset by _L_ , which is a subset of _S_<sup>_c_</sup> , the complement of _S_ . For example, one might regard the set _L_ = _{j_ : _|µj| < Dµ}_ , where _Dµ < Cµ_ , as particularly inappropriate for further study. The proportion of such genes in the estimated subset is of great interest; we will refer to this quantity as the “proportion of extremely false positives” or _pefp_ . If this proportion is always very low, one can be reasonably confident that the top ranked genes of the reported subset contain no extremely false positives. We define _ξj_ = _ξj_ ( **_µ_** _,_ **Σ** ) = 1 if gene _j_ is in _L_ and _ξj_ = 0 otherwise, _j_ = 1 _, . . ., p_ . Now, the proportion of extremely false positives ( _pefp_ ) for the estimated subset **S**<sup>�</sup> _n_ can be defined as:


As with sensitivity and predictive value, we can use the parametric bootstrap to estimate the

20

expectation _E_ ( _pefp_ ) and variance Var( _pefp_ ). Note that if _L_ = _S_<sup>_c_</sup> , _pefp_ is simply one minus the positive predictive value. Therefore, _pefp_ becomes interesting only when _L_ is considerably smaller than _S_<sup>_c_</sup> .

Other important quantities of interest are the 0.95-quantiles of _|_ **_µ_** � _n −_ **_µ_** _| ≡_ max _j |µ_ � _nj − µj |_ and max _i,j |_ **_ρ_** � _n −_ **_ρ_** _|_ . It should also be noted that one could replace the PAM procedure described above with some “supervised” clustering method that allows the analyst to specify the cluster centers. If the centers were fixed at genes of known function, the clusters have a coherent meaning throughout the bootstrap. In that case, we can also track how often each gene appears in each fixed-center cluster and, thereby, obtain information on cluster stability.

##### **Interpretation of the output of the parametric bootstrap.**

By relying on asymptotic properties established in Section 2.4, we can view the relative frequencies ( � _pj, P_<sup>�</sup> _ij, Q_<sup>�</sup> _ij_ ) as estimates of the probabilities ( _pj, Pij, Qij_ ). Consider now the situation in which _n_ is too small to reasonably assume that ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) is close to ( **_µ_** _,_ **Σ** ). In this case, it does not follow that the distribution of **S**<sup>�</sup> _n_ is close to the distribution of **S**<sup>�</sup> _n_ . It is our experience that the results of the parametric bootstrap are still valuable. One can simply interpret the results as a simulation study for estimation of **S**<sup>�</sup> _n_ when sampling from _N_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ). Findings of such a simulation study (such as a low predictive value) will demonstrate the difficulty of estimating _S_ with the given sample size _n_ . In particular, one can run the parametric bootstrap for several subset rules and thereby determine which types of subsets can be reasonably estimated with the available sample size.

### **2.4 Asymptotic theory.**

Our proposed method for analyzing gene expression data reports an estimated subset **S**<sup>�</sup> _n ≡_ **S** ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) and bootstrap estimates of the feature-specific probabilities and other quantities, such as the distribution of sensitivity and predictive value. In this section we prove the consistency of **S** � _n_ and thereby the consistency of the bootstrap estimate of its distribution under appropriate conditions. Additionally, we provide a sample size formula that controls the probability of the estimated subset containing any extremely false positives.

Because _p_ is typically much larger than _n_ , we are interested in the performance of **S**<sup>�</sup> _n_ and the parametric bootstrap when _p_ ( _n_ ) _≫ n_ . Clearly, if _p_ is fixed at some finite value, our method will be valid for some sufficiently large _n_ ; but we are concerned with the case where _p_ is essentially infinite. If _S_ is a fixed (in _p_ ) finite subset, which is a reasonable assumption, we have that _P_ ( _S ⊆_ **S**<sup>�</sup> _n_ ) (or, alternatively, the sensitivity) converges to 1 as the sample size converges to infinity. This is true regardless of the rate at which _p_ ( _n_ ) converges to infinity. However, the positive predictive value still may not converge to one (i.e. the number of false positives may not converge to zero). It is not enough for the target subset to be merely _contained_ in the sample subset; we want the two sets to be identical with probability tending to one. To achieve this convergence, we require uniform consistency of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) for ( **_µ_** _,_ **Σ** ). In summary, for a typical subset rule **S** ( _·, ·_ ) and under the assumption that there are no subset elements on the boundary, uniform consistency of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) for ( **_µ_** _,_ **Σ** ) implies that _P_ ( **S**<sup>�</sup> _n_ = _S_ ) _→_ 1 as _n →∞_ .

In order to control the error in **S**<sup>�</sup> _n_ as an estimate of _S_ one needs to control the uniform distance between ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) and ( **_µ_** _,_ **Σ** ). In particular, if one wants to control the probability of finding extremely false positives in **S**<sup>�</sup> _n_ , then one needs ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) to be within a specified distance _ϵ_ from the true ( **_µ_** _,_ **Σ** ), where _ϵ_ will depend on the definition of an extremely false positive. For

21

example, consider the simple subset rule **S** ( **_µ_** ) = _{j_ : _µj >_ log 3 _}_ . Then one might define an extremely false positive as a gene _j_ with _µj <_ log 2. In this case, given a small user-supplied number _δ >_ 0, one wants to choose the sample size _n_ such that the probability that the uniform distance between **_µ_** � _n_ and **_µ_** is smaller than _ϵ_ = log 3 _−_ log 2 _≈_ 0 _._ 41 is larger than 1 _− δ_ .

The next two theorems establish the uniform consistency of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) (and, therefore, **S**<sup>�</sup> ) and provide a sample size formula, respectively; both proofs rely on Bernstein’s Inequality for sums of independent mean-zero random variables. Recall that (see van der Vaart and Wellner, 1996, page 102): If _Z_ 1 _, . . ., Zn_ are independent, have range within [ _−W, W_ ], and have zero means, then


for _v ≥_ var( _Z_ 1 + _. . ._ + _Zn_ ).

**Theorem 2.4.1 (Consistency)** _Let p_ = _p_ ( _n_ ) _be such that n/_ log( _p_ ( _n_ )) _→∞ as n →∞ and M < ∞ (recall that M bounds the absolute value of the underlying data). As n →∞, then_


_and_


_This implies the following: Suppose that the subset rule_ ( **_µ_** _,_ **Σ** ) _→_ **S** ( **_µ_** _,_ **Σ** ) _is continuous in the sense that if, for the sequence_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) _(p_ ( _n_ ) _vectors and p_ ( _n_ ) _× p_ ( _n_ ) _matrices, respectively),_


_Then for any ϵ >_ 0 _,_


_For example, consider subset rule 2.5, defined in section 2.2, indexed by user-supplied Cµ and Cρ. If there exists an ϵ >_ 0 _such that_


_then, for such a subset rule, we have_


**Theorem 2.4.2 (Sample Size Formula)** _Let ϵ >_ 0 _,_ 1 _> δ >_ 0 _, and the number of genes p be given. Let σ_<sup>2</sup> _be an upper bound of_ max _j σj_<sup>2</sup><sup>_andletW>_0</sup><sup>_beaconstantsuchthat_</sup> _P_ ( _Yj − µj ∈_ [ _−W, W_ ]) = 1 _, for all j. Define n_<sup>_∗_</sup> ( _p, ϵ, δ, W, σ_<sup>2</sup> ) _as follows:_


_If n > n_<sup>_∗_</sup> _, then_


_Similarly, if n > n_<sup>_∗_</sup> ( _p_<sup>2</sup> _, ϵ, δ, W_<sup>2</sup> _, σ_ Σ<sup>2)</sup><sup>_,whereσ_</sup> Σ<sup>2</sup><sup>_isanupperboundofthevarianceofYiYj,then_</sup> _P_ (max _|_ Σ<sup>�</sup> _ij −_ Σ _ij| > ϵ_ ) _< δ. ij_

22

The consistency of **S** ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) is a direct consequence of the uniform consistency of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ). We will prove the uniform consistency of **_µ_** � _n_ . For a particular component of **_µ_** � _n_ , application of Bernstein’s Inequality gives:


Since _P_ ( _∪j Aj_ ) _≤_<sup>�</sup> _j_<sup>_P_(</sup><sup>_Aj_),wehaveanupperboundontheprobabilitythattheuniform</sup> distance from **_µ_** � _n_ to **_µ_** exceeds _ϵ >_ 0:


The expression on the right converges to zero if _n/_ log( _p_ ( _n_ )) _→∞_ as _n →∞_ . A similar argument holds for **Σ**<sup>�</sup> _n_ .

The _n_<sup>_∗_</sup> in theorem 2.4.2 is precisely the solution obtained when we set the right-hand expression of (2.3) equal to 0 _< δ <_ 1 and solve for _n_ . If one assumes independence of genes, then _P_ (max _j |µ_ � _j − µj | ≤ ϵ_ ) =<sup>�</sup> _j_<sup>_P_(</sup><sup>_|µ_�</sup><sup>_j−µj| ≤ϵ_).ByapplyingBernstein’sInequalitytoeachterm</sup> of the product, one obtains the same sample size formula as above, to first order approximation. Therefore, this sample size formula is as sharp as Bernstein’s Inequality. In a similar fashion as for the mean, one obtains such a sample size formula for _P_ (max _ij |EY_<sup>�</sup> _iYj − EYiYj | > ϵ_ ) _< δ_ and thus for _P_ (max _ij |_ Σ<sup>�</sup> _ij −_ Σ _ij| > ϵ_ ) _< δ_ . In this case the summation is over _p_ ( _p −_ 1) _/_ 2 elements and _YiYj_ is bounded by _W_<sup>2</sup> .□

If _p_ increases from _p_ 1 to _p_ 2, then _n_<sup>_∗_</sup> ( _p_ ) increases by a magnitude log( _p_ 2 _/p_ 1) _/c_ and, if _p_ is large, then the derivative _dp_<sup>_dn∗_(</sup><sup>_p_) = 1</sup><sup>_/_(</sup><sup>_cp_) actually converges to zero.Therefore the sample size</sup> is heavily driven by the factor 1 _/c_ . Consider the example given above and suppose we want the probability of including any extremely false positives to be less than 0 _._ 1. Suppose that _p_ = 5000, that the maximal variance is 0 _._ 5 and that the truncation level _W_ is 1 _._ 4 (twice the maximal standard deviation). Application of theorem 2.4.2 says that, if _n > n_<sup>_∗_</sup> (5000 _,_ 0 _._ 41 _,_ 0 _._ 1 _,_ 1 _._ 4 _,_ 0 _._ 5) _≈_ 95, then _P_ (sup _j |µ_ � _j − µj| >_ 0 _._ 41) _<_ 0 _._ 1). Note that the effect of a huge increase in _p_ on the required sample size is minor: e.g. _n_<sup>_∗_</sup> (100000 _,_ 0 _._ 41 _,_ 0 _._ 1 _,_ 1 _._ 4 _,_ 0 _._ 5) = 120.

To convey a general sense of the implications of this sample size formula, we provide a few examples:


If we set the right-hand expression of (2.3) equal to _δ_ and solve for _ϵ_ , we obtain a 1 _−δ_ - _uniform confidence band for µ_ with radius _ϵ_ for each component:


23

It is better to construct a confidence band by first scaling the data to have variance one ( _i.e._ apply the formula to _Yj /σj_ and use _σ_<sup>2</sup> = 1 in (2.4)) and then returning to the original scale by multiplying the radius _ϵ_ with _σj_ for each gene:


In the above _σj_ can be estimated with its empirical counterpart _σ_ � _jn_ , _j_ = 1 _, . . ., p_ .

Figure 2.1 illustrates visually the implications of this sample size formula for several realistic scenarios. In the top panel we have set _ϵ_ = 1 and in the bottom _ϵ_ = 0 _._ 58. Decreasing the tolerable distance _ϵ_ , holding all other constants fixed, increases the required sample size. The noise levels implied by the values of _σ_ in the range [0.5, 1.0] are typical for the data sets we have seen. We note that the sample size formula is actually quite conservative. It makes no assumptions about the correlation between the _p_ genes and, when there is a significant amount of correlation, the true dimension of the problem can be much smaller than _p_ . In practice, given the highly correlated microarray data, we see that the sample size formula produces extremely false positive rates much lower than the nominal rate of _δ_ .

**Bonferoni simultaneous confidence interval.** Suppose one is concerned with setting _ϵ_ such that _P_ (max _j | µjn −µj | /_ ( _σj/_<sup>_√_</sup> _n_ ) _> ϵ_ ) _< δ_ for a small number _δ_ such as 0 _._ 05. Once this number is obtained then that yields a simultanous confidence band _µjn ± ϵσj /_<sup>_√_</sup> _n_ which contains with probability 1 _−δ_ all _µj_ simultaneously. It is easy to show that if all _µjn_ , _j_ = 1 _, . . ., p_ , are pairwise independent, then _ϵ ≈ q_ 1 _−δ/_ (2 _p_ ), where _qr_ = Φ<sup>_−_1</sup> ( _r_ ) is the _r_ -th quantile of the standard normal cumulative distribution function Φ. This choice of _ϵ_ is referred to as the Bonferoni adjustment, which is thus conservative if the _µjn_ happen to be dependent.

**Bootstrapped simultaneous confidence interval.** Let _q_ be chosen so that the distribution of the resampled _µn_<sup>#issuchthat</sup><sup>_P_</sup> _n_<sup>#(max</sup> _j |µσ_<sup>#</sup> _jnjn_<sup>_−_</sup> _/_<sup>_√µjn_</sup> _n_<sup>_|_</sup> _> q_ ) = 0 _._ 05, i.e. the proportion of times _|µ_<sup>#</sup> _jn_<sup>_−µjn|_</sup> across all bootstrapped samples that max _j σjn/_<sup>_√_</sup> _n > q_ is smaller than or equal to 0.05. Now, a simultaneous 0 _._ 95-confidence interval for _µ_ is given by _µjn ± q ∗ σjn/_<sup>_√_</sup> _n_ . The validity of this confidence interval relies on the consistency of the bootstrap and therefore it will be of interest to test its validity in a simulation study. The advantage of this simultaneous confidence interval is that it exploits the dependencies between the components of _µn_ and will therefore be less conservative than the Bonferoni simultaneous confidence interval.

#### **2.4.1 Consistency of the bootstrap.**

Given this consistency of **S**<sup>�</sup> _n_ , we are now concerned with the asymptotic behavior of the featurespecific probabilities as _n →∞_ . To be able to prove such a theorem, we need to consider a specified simple subset rule. For simplicity, we consider


This rule seeks genes that are over expressed and that have a large correlation with at least one other over expressed gene. Theorem 2.4.3 demonstrates that these probabilities converge to one (zero) when the appropriate feature is present (absent) in the target subset. For example, for genes _j_ such that _Sj >_ 0, we have that _pj →_ 1.

24

## Sample Size Requirements


<!-- Start of picture text -->
epsilon = 1, confidence level = 0.8<br>Sigma =  1<br>Sigma =  0.75<br>Sigma =  0.5<br>0 2000 4000 6000 8000 10000<br>Number of genes<br>epsilon = 0.58, confidence level = 0.8<br>Sigma =  1<br>Sigma =  0.75<br>Sigma =  0.5<br>0 2000 4000 6000 8000 10000<br>Number of genes<br>/home/jenny/research/gene_chip/prose/stat_sin_paper/samplesize.eps<br>120<br>80<br>60<br>Sample Size 40<br>20<br>0<br>120<br>80<br>60<br>Sample Size 40<br>20<br>0<br><!-- End of picture text -->

Figure 2.1: Sample size requirements for different situations.

25

**Theorem 2.4.3** _Consider the simple subset rule 2.5. Let p_ = _∞ and M < ∞. Assume that Cµ and Cρ are chosen so that the boundary condition (∗) of theorem 2.4.1 holds. Then the feature specific probabilities pj,n and Pij,n converge uniformly in i, j to the corresponding featureindicators I_ ( _j ∈S_ ) _and I_ (( _i, j_ ) _∈S_ ) _, as n →∞._

The following theorem proves consistency of the bootstrap estimates of the feature specific probabilities under the condition that _n/_ log( _p_ ( _n_ )) _→∞_ .

**Theorem 2.4.4** _Consider the simple subset rule (2.5). Let M < ∞. Assume that Cµ and Cρ are chosen so that the boundary condition (∗) of theorem 2.4.1 holds. If n/_ log( _p_ ( _n_ ) _converges to infinity, then p_ � _j,n and P_<sup>�</sup> _ij,n converge in probability uniformly in_ ( _i, j_ ) _to the feature-indicators I_ ( _j ∈S_ ) _and I_ (( _i, j_ ) _∈S_ ) _._

In order to establish asymptotic consistency of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) and validity of the bootstrap at a non-degenerate level, we have proven an infinite dimensional central limit theorem for<sup>_√_</sup> _n_ ( _µn − µ_ ) _V ar_ , in which the latter are treated as elements of an infinite dimensional Hilbert space with a weighted Euclidean norm . Subsequently, we prove nonparametric asymptotic validity of the parametric bootstrap for the purpose of estimating the limiting distribution of<sup>_√_</sup> _n_ ( _µn − µ_ ). Similarly, this can be proved for<sup>_√_</sup> _n_ (Σ _n −_ Σ) if one assumes the multivariate normal model. These proofs can be found in van der Laan and Bryan (2001).

In order to show formally that the parametric bootstrap is consistent for ( **_µ_** _,_ **Σ** ), one first establishes that<sup>_√_</sup> _n_ ( _µn−µ_ ) _V ar_ converges in distribution to a Gaussian process as random elements of some Banach (or Hilbert) space endowed with the Borel sigma algebra. Subsequently, one shows that the bootstrap empirical process (sampling from _N∞_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ))<sup>_√_</sup> _n_ ( _µn − µ_ ) _V arBoot_ converges in distribution to the same Gaussian process. If the latter holds, then one says that the bootstrap method is asymptotically valid for estimation of the distribution of ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ), considered as random elements of the Banach space.

Let **R**<sup>_∞_</sup> ( _λ_ 1) be the Hilbert space of infinite-dimensional vectors with inner-product _⟨x, y⟩_ 1 = � _j_<sup>_xjyjλ_1</sup><sup>_j_,whereitisassumedthat�</sup> _j_<sup>_λ_1</sup><sup>_j<∞_.Thenwecanview</sup><sup>_√_</sup> _n_ ( _µn − µ_ ) as a random element of the Hilbert space **R**<sup>_∞_</sup> ( _λ_ ). Similarly, let **R**<sup>_∞_</sup> ( _λ_ 2) be the Hilbert space of infinite dimensional vectors with inner-product _⟨x, y⟩_ 2 =<sup>�</sup> _ij_<sup>_xijyijλ_2</sup><sup>_,ij_,whereitisassumedthat</sup> � _ij_<sup>_λ_2</sup><sup>_ij< ∞_.Then we can view</sup><sup>_√_</sup> _n_ (Σ _n−_ Σ) as a random element of **R**<sup>_∞_</sup> ( _λ_ 2). The potential limiting distribution of<sup>_√_</sup> _n_ ( _µn −µ_ ) is determined by the multivariate CLT for any finite dimensional sub-vector of<sup>_√_</sup> _n_ ( _µn − µ_ ) and is thus a Gaussian process _Z_ 1 = ( _Z_ 1( _j_ ) : _j_ = 1 _, . . .,_ ). Similarly, the potential limiting distribution of<sup>_√_</sup> _n_ (Σ _n −_ Σ) is a Gaussian process _Z_ 2 = ( _Z_ 2( _ij_ ) : _i, j_ ). In Hilbert spaces an infinite dimensional central limit theorem follows from the point-wise central limit theorem and a rather weak tightness condition (see Appendix). We have the following functional central limit theorem for **_µ_** � _n_ and **Σ**<sup>�</sup> _n_ .

**Theorem 2.4.5** _Let M < ∞. We have that_<sup>_√_</sup> _n_ ( _µn − µ_ ) _V ar converges in distribution to the Gaussian process_ ( _Z_ 1 _, Z_ 2) _as random elements in_ **R**<sup>_∞_</sup> ( _λ_ 1) _×_ **R**<sup>_∞_</sup> ( _λ_ 2) _endowed with the Borel sigma algebra._

The following theorem proves that the bootstrap estimate of the distribution of<sup>_√_</sup> _n_ ( _µn − µ_ ) is asymptotically consistent.

**Theorem 2.4.6** _Let M < ∞ and let_ **_µ_** � _n be the empirical mean vector based on sampling from N∞_ ( **_µ_** � _n,_ **Σ**<sup>�</sup> _n_ ) _. We have that_<sup>_√_</sup> _n_ ( **_µ_** � _n −_ **_µ_** � _n_ ) _converges in distribution to the Gaussian process Z_ 1 _(of theorem 2.4.5 above) as random elements in_ **R**<sup>_∞_</sup> ( _λ_ 1) _._

26

We can also prove asymptotic validity of the parametric bootstrap for<sup>_√_</sup> _n_ (Σ _n −_ Σ), but that requires assuming that _Y ∼ N∞_ ( **_µ_** _,_ **Σ** ).

### **2.5 Data analysis**

We examine a data set which is an example of an unpaired comparison with observations from two subpopulations. We extracted a publicly available data set from the data base accompanying Ross et al. (2000). The authors performed microarray experiments on 60 human cancer cell lines (the NCI60) derived from tumors from a variety of tissues and organs by researchers from the National Cancer Institute’s Developmental Therapeutics Program. The data set includes gene expression measurements for 9,703 cDNAs representing approximately 8,000 unique transcripts. Each tumor sample was cohybridized with a reference sample consisting of an equal mixture of twelve of the cell lines chosen to maximize diversity. We used the normalized tumor:reference ratios, as in Ross et al. (2000). These were transformed to a log10 scale and truncated above and below, so that any ratio representing greater than 20-fold over- or under-expression was set to log10(20).

For this comparative analysis, we selected two very different types of cancer from those included in the NCI60: melanoma and breast. We created a data set with all samples from these two types of cancer, which included seven breast and eight melanoma cell lines. Next, we applied an initial subset rule in order to reduce the size of the data set for computational reasons only. We retained those genes where at least 30% of all cell lines had a ratio corresponding with greater than 2-fold over- or under-expression. Using a 30% cut-off, a gene differentially expressed in one type of cancer and not the other would still be included. There were 3500 genes in the resulting data set. This data set was divided into two smaller data sets consisting of the cell lines from each type of cancer. These data sets were analyzed separately and also combined into one data set by dividing the melanoma ratios by the geometric mean breast ratios before taking the log. Unless otherwise noted, we are working with the single, combined data set containing 3500 genes and eight observations.

One goal of the analysis is to identify genes differently expressed in melanoma relative to breast cancer; such genes help us to understand the biological characterization of different cancers and may lead to new cancer-specific treatments. Another goal revisited in chapter 3 is to study clustering patterns in the data set in order to discover information about how the genes involved in tumors work together.

#### **2.5.1 Selecting differently expressed genes**

A common approach to selecting differently expressed genes is to retain those genes whose absolute mean log ratios are greater than some cut-off value. In order to account for variance as well as mean expression, one can standardize the log ratios by dividing them by their genespecific standard errors before taking the mean. These standardized means can be compared to the quantiles of a standard normal distribution on an individual basis. For the combined data set, _p_<sup>_∗_</sup> = 1731 genes were significantly differently expressed at the _α_ = 0 _._ 05 level (cut-off value= _z_ 1 _−_<sup>_α_</sup> 2<sup>_/√_</sup> _n_ = 0 _._ 69). Since we are in a multiple comparisons setting, it is advisable to adjust the cut-off value. The Bonferoni adjusted cut-off value was 1.53 and produced a much smaller subset of _p_<sup>_∗_</sup> = 605 differently expressed genes. As mentioned above, the Bonferoni adjustment is sharp if the genes are independent, but is conservative otherwise.

27

An alternative, less conservative approach is to derive a cut-off value from an appropriate null distribution with zero means and the true covariance structure. A parametric method is to generate a large number of samples from a multivariate normal distribution _N_ (0 _, ρ_ ), where _ρ_ is the correlation matrix, and select a cut-off value such that no more than 1 _−_<sup>_α_</sup> 2<sup>ofsampleshave</sup> any differently expressed genes. The correlation matrix _ρ_ can be estimated by the empirical correlation matrix. A non-parametric method is to standardize the observed data so that each gene has mean zero and variance one, then generate a large number of bootstrap samples from this data (resampling cell lines with replacement), and use these to compute the cut-off value such that no more than 1 _−_<sup>_α_</sup> 2<sup>ofsampleshaveanydifferentlyexpressedgenes.Forboththe</sup> parametric and non-parametric methods, a less stringent approach is to choose the cut-off value such that on average any sample is expected to have no more than 1 _−_<sup>_α_</sup> 2<sup>ofgenesdifferently</sup> expressed. We used the nonparametric bootstrap with the more stringent criteria and obtained a subset of _p_<sup>_∗_</sup> = 889 genes. The cut-off value was 1.17, which lies between the value which ignores the multiple comparisons and the too strict Bonferoni adjusted value.

### **2.6 Simulation to assess variability of empirical relative gene expression and empirical pairwise distance between genes.**

Let **X** be the _p_ -dimensional column vector of gene-specific relative gene expressions representing the relative gene expression profile for a randomly drawn subject. Thus we observe _n_ i.i.d. copies **X** 1 _, . . .,_ **X** _n_ of this random vector **X** . The total data set “Gene-ID”, **X** 1 _, . . .,_ **X** _n_ , can be represented by an array with _p_ rows and _n_ columns.

Let _Y_ = log( **X** ) be the vector of truncated log-ratios and _Y_ 1 _, . . ., Yn_ are the i.i.d observations of the _p_ -dimensional vector _Y_ . In these experiments we are particularly concerned with estimation of


and the corresponding _p_ by _p_ correlation matrix _ρ_ which one can compute from Σ:


In particular, our subset rules _S_ ( _µ,_ Σ) maps these unknown parameters into a subset of genes which is believed to be of interest for drug-development.

Let _µn,_ Σ _n, ρn_ be the empirical counterpart of _µ,_ Σ _, ρ_ . In practice the subset of genes we are going to select is _S_ ( _µn,_ Σ _n_ ). Therefore this estimated subset will only be close to the wished subset if _µn_ and Σ _n_ are close to _µ_ and Σ-respectively. For example, if _µnj_ deviates more than log(3) _−_ log(2) from the true _µj_ , then the fact that _µnj >_ log(3) (i.e. it is 3-fold differentially expressed on average among the selected patients) does not imply that gene _j_ is in truth 2-fold differentially expressed. Therefore we are interested in determining a sample size so that we can trust that the true means and true correlation are within a reasonable distance from the observed means and correlations for each of the _p_ genes.

A subset rule can still have a good performance when there are some highly wrong empirical correlations. In particular, one can design a subset rule which protects oneself against false

28

Table 2.2: Quantiles of standard deviations _σj_ , _j_ = 1 _, . . ., p_ based on data set of a 12 coloncancer patients using truncation _M_ = log(5) = 1 _._ 6 _, M_ = log(7 _._ 5) = 2 and _M_ = log(10) = 2 _._ 3, respectively.

|M|0.5|0.7|0.9|max|
|---|---|---|---|---|
|1.6|0.48|0.55|0.67|1.38|
|2|0.51|0.60|0.74|1.55|
|2.3|0.52|0.62|0.78|1.74|


positives due to high empirical correlations. To start with one can just use a higher rate of initial screening so that it becomes much harder to make it into the clustering routine. For example, one only selects highly differentially expressed genes (so that one end up clustering e.g. only 100 genes) or one only selects genes with relatively small standard deviation. Moreover, we can thin out the clusters by requiring strong correlations with the centers (medoids) of the clusters: in this way, a gene which happens to have a strong correlation with various genes while in truth it is not correlated at all might still not make the subset since it needs to be strongly related with the actual center of the cluster. Suppose that one is interested in determining which genes among _m ≤ p_ selected genes cluster with a _given_ gene. In this case one just needs to estimate _m_ pairwise correlations of genes with the given gene. The bootstrap can be used to compare various subset rules w.r.t to their performance in finding the correct subset of genes and the number of false positives.

In this section we study the distribution of the maximal difference (over all _p_ genes) between true and observed averages, true and observed standard deviations and true and observed correlations under various sample sizes. In order to do this at an appropriate noise level we use a noise level observed in an actual data set of 12 colon cancer patients. In order to create a worst case scenario and to protect outselves against false positives we will determine these distributions in the context that all genes are unrelated: if many genes are correlated than the true dimension of the problem can be much lower than _p_ . We also study the performance of empirical correlations when the true correlation is high in order to determine how well we can do in discovering all highly correlated genes.

The observed noise level in a data set depends on the truncation level _M_ one uses: the larger _M_ the larger the noise level. We first compute the 0.5,0.7,0.9-quantile and maximum of the _p_ standard deviations of the by _M_ truncated log-ratios of a colon-cancer data set with 12 patients. Table 2.2 reports these quantiles for _M_ = log(5) _,_ log(7) _,_ log(10).

#### **2.6.1 Sample sizes for estimation of the population mean.**

Consider a _p_ = 10000 dimensional vector of log-relative gene-expressions where each component is truncated by _M_ . Let _σj_ be the standard deviation of component _j_ and let _σ_ = max _j σj_ . The following function computes the sample size


such that with probability 1 _− δ_ the maximal difference max _j | µnj − µj |_ over _p_ genes is smaller than _ϵ_ .

29

Table 2.3: Consider a _p_ = 10 _,_ 000 dimensional vector of log-relative gene-expressions where each component is truncated by _M_ . Let _σj_ be the standard deviation of component _j_ and let _σ_ = max _j σj_ . The following table gives the sample sizes such that with probability 0.95 the maximal difference max _j | µnj − µj |_ over _p_ = 10000 genes is smaller than _ϵ_ . We provide this sample size for _M_ = log(5) _,_ log(7 _._ 5) _,_ log(10, corresponding 0.5,0.7,0.9,1-quantiles of the _p_ -standard deviations as observed in the colon-cancer data set and _ϵ ∈{_ 0 _._ 1 _,_ 0 _._ 2 _, . . .,_ 1 _}_ .

|M,Sigma|0.1|0.2|0.3|0.4|0.5|0.6|0.7|0.8|0.9|1|
|---|---|---|---|---|---|---|---|---|---|---|
|1.6,0.48|732|217|112|72|51|39|32|26|23|20|
|1.6,0.55|918|264|133|83|59|45|36|29|25|22|
|1.6,0.67|1296|358|175|107|74|55|43|35|30|25|
|1.6,1.38|5051|1297|592|341|224|159|120|94|76|63|
|2,0.51|843|254|132|85|61|47|38|32|27|24|
|2,0.60|1101|318|161|101|72|54|44|36|31|26|
|2,0.74|1585|439|214|131|91|68|53|44|37|31|
|2,1.55|6370|1636|746|430|282|201|151|118|96|79|
|2.3,0.52|895|273|143|93|67|52|42|36|31|27|
|2.3,0.62|1189|347|176|111|79|61|48|40|34|30|
|2.3,0.78|1767|491|240|148|102|77|60|49|41|35|
|2.3,1.74|8009|2052|934|538|352|250|188|147|118|98|


Table 2.4: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal difference max _j∈{_ 1 _,...,p} | µnj − µj |_ between _p_ = 10 _,_ 000 sample means and true means. Here _µnj_ is the sample mean of logratios based on _n_ observations with _N_ ( _muj, sigma_ = 0 _._ 55) distribution, _j_ = 1 _, . . .,_ 10000.

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.56|0.59|0.63|
|n=30|0.40|0.41|0.43|
|n=60|0.28|0.29|0.31|
|n=100|0.22|0.22|0.24|
|n=150|0.18|0.19|0.20|


Since _n_<sup>_∗_</sup> only depends on _p_ through log( _p_ ) the effect of _p_ on the required sample size _n_<sup>_∗_</sup> is very minimal. For example, suppose the noise level is _σ_ = 0 _._ 55, _M_ = log(5) and one wants to be sure that the sample means of _p_ genes are within a distance _ϵ_ = 0 _._ 5 of the true means, then the required sample size for _p_ = 1 is 17 and the required sample size for _p_ = 100000 is 69.

The following table 2.3 provides now these sample sizes for _M_ = log(5) _,_ log(7 _._ 5) _,_ log(10) and the values of _σ_ as computed in the table above.

This sample size formula is a conservative formula since it holds for any data generating distribution function. We will now carry out a simulation to determine the distribution of max _j∈{_ 1 _,...,p} | µnj − µj |_ for _p_ = 10 _,_ 000 at a noise level corresponding with the 0.7-quantile of the _σnj_ ’s we observed in a coloncancer patient data set at truncation level _M_ = log(5). In all these simulations we assume that all _p_ genes are uncorrelated which corresponds with a worst case scenario. For example, if _n_ = 15, then with probability 0.9, each of the 10,000 observed averages are within a distance 0 _._ 63 of the truth.

30

Table 2.5: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal dif **f** erence max _j∈{_ 1 _,...,p} | σnj − σj |_ between _p_ = 10 _,_ 000 sample standard deviations and true standard deviations. Here _σnj_ is the sample standard deviations of logratios based on _n_ observations with _N_ ( _muj, sigma_ = 0 _._ 55) distribution, _j_ = 1 _, . . .,_ 10000.

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.40|0.43|0.46|
|n=30|0.28|0.3|0.31|
|n=60|0.2|0.21|0.22|
|n=100|0.15|0.16|0.18|
|n=150|0.13|0.13|0.14|


Table 2.6: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal dif **f** erence max _i<j∈{_ 1 _,...,p} | ρn,ij − ρij |_ of the sample correlations and true correlations which are equal to zero. Here _ρn,ij_ is the sample correlation of uncorrelated logratios for genes _i_ and _j_ with standard deviation _σ_ = 0 _._ 55 and _p_ = 1000.

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.92 0.93 0.94|||
|n=30|0.76 0.77 0.77|||
|n=60|0.58 0.59 0.6|||
|n=100|0.46|0.47|0.48|
|n=150|0.38|0.39|0.41|


#### **2.6.2 Sample size for estimation of the standard deviations.**

Various interesting subset rules rely on estimates of the gene-specific standard deviations _σj_ . Therefore it is also of interest to know with high certainty that the true standard deviation is within a reasonable distance from the observed standard deviation.

#### **2.6.3 Sample size for estimation of the correlations.**

If a pair of genes have an observed correlation larger than a certain number, then that might be an important finding in the process of drug development. For example, one might find that an unknown gene has a large correlation with a gene which is well known (from the literature) to be an important cause of cancer. In that case, one might decide to carry out experiments controlling this unknown gene. In addition, if one observes clusters of genes in the data then that will be interpreted as that genes are working together. Our cluster routines are purely functions of the observed correlations and can thus only be trusted if we do a good job in estimating the true correlation matrix of the genes we decided to cluster. Note that we typically only cluster a subset of all _p_ genes: for example, we might just cluster all 3-fold differentially expressed genes. Therefore we are particularly interested to know what sample size we need to estimate a 300 by 300 (if we cluster 300 genes) or at most 1000 by 1000 correlation matrix. Table 2.6 reports the performance in estimation of a 1000 by 1000 diagonal correlation matrix (i.e. all correlations are zero). Table 2.7 reports the performance in estimation of a 300 by 300 diagonal correlation matrix (i.e. all correlations are zero).

Suppose now that all the true correlations one is interested in are high. Now, one might

31

Table 2.7: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal dif **f** erence max _i<j∈{_ 1 _,...,p} | ρn,ij − ρij |_ of the sample correlations and true correlations which are equal to zero. Here _ρn,ij_ is the sample correlation of uncorrelated logratios for genes _i_ and _j_ with standard deviation _σ_ = 0 _._ 55 and _p_ = 300.

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.87|0.89|0.91|
|n=30|0.69|0.71|0.73|
|n=60|0.52|0.54|0.57|
|n=100|0.42|0.42|0.43|
|n=150|0.33|0.34|0.34|


Table 2.8: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal difference max _j∈{_ 1 _,...,p} | ρn,j − ρj_ = 0 _._ 8 _|_ of the _p_ = 100 _,_ 000 sample correlations and true correlations. Here _ρn,j_ is the sample correlation based on n observations of _X ∼ N_ (0 _,_ 0 _._ 55), _Y_ with _Y_ = 0 _._ 445 _X_ + _N_ (0 _,_ 0 _._ 2) so that the true correlation between _X_ and _Y_ is 0.77.

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|1.1|1.1|1.2|
|n=30|0.59|0.61|0.64|
|n=60|0.35|0.36|0.38|
|n=100|0.24|0.25|0.27|
|n=150|0.18|0.18|0.19|


want to be able to discover them all as highly correlated pairs of genes. Table 2.8 provides the performance in estimating 100,000 highly correlated pairs simultaneously at various sample sizes.

Suppose now that all the true correlations one is interested in are high. Now, one might want to be able to discover them all as highly correlated pairs of genes. Table 2.8 provides the performance in estimating 100,000 highly correlated pairs simultaneously at various sample sizes.

Suppose now that one gene _j_<sup>_∗_</sup> is given and one just wants to estimate the the _p_ correlations _ρjj∗_ with this gene _j_<sup>_∗_</sup> , _j_ = 1 _, . . ., p_ . Tables 2.9 and 2.10 provides the performance in estimating _p_ zero-correlations for various sample sizes and _p_ = 1000 _,_ 300. Table 2.11 provides the performance in estimation of _p_ = 300 high correlations for various sample sizes.

### **2.7 Simulation to assess clustering performance**

The goal of this simulation study is to explore the performance of **S**<sup>�</sup> _n_ and the bootstrap in the context of a known data-generating distribution. We are particularly interested in assessing the difficulty of applying cluster labels in the presence of genes that belong to no cluster and how that is affected by sample size. The simulation shows that it is beneficial to screen unrelated genes prior to applying a clustering algorithm. We also see that unrelated genes tend to depress conventional measures of the clustering strength. Lastly, it is apparent that post-screens affected by isolated extreme values, such as the smallest entries in a column of a correlation matrix, will require large sample sizes to achieve good performance of **S**<sup>�</sup> and alternative screens should be

32

Table 2.9: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal difference max _j∈{_ 1 _,...,p} | ρn,jj_<sup>_∗_</sup> _− ρjj_<sup>_∗_</sup> _|_ of the _p_ = 1000 sample observed correlations and true correlations with a fixed gene _j_<sup>_∗_</sup> . Here _ρn,jj_<sup>_∗_</sup> is the sample correlation based on n observations of _Xj∗ ∼ N_ (0 _,_ 0 _._ 55), _Yj ∼ N_ (0 _,_ 0 _._ 55).

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.78|0.8|0.85|
|n=30|0.58|0.61|0.67|
|n=60|0.43|0.45|0.49|
|n=100|0.33|0.35|0.37|
|n=150|0.27|0.29|0.31|


Table 2.10: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal difference max _j∈{_ 1 _,...,p} | ρn,jj_<sup>_∗_</sup> _− ρjj_<sup>_∗_</sup> _|_ of the _p_ = 300 sample observed correlations and true correlations with a fixed gene _j_<sup>_∗_</sup> . Here _ρn,jj_<sup>_∗_</sup> is the sample correlation based on n observations of _Xj∗ ∼ N_ (0 _,_ 0 _._ 55), _Yj ∼ N_ (0 _,_ 0 _._ 55).

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.72|0.74|0.79|
|n=30|0.55|0.57|0.61|
|n=60|0.38|0.41|0.44|
|n=100|0.3|0.32|0.36|
|n=150|0.25|0.26|0.28|


Table 2.11: Below we report the median, 0.7-quantile and 0.9 quantile of the distribution of the maximal difference max _j∈{_ 1 _,...,p} | ρn,jj_<sup>_∗_</sup> _− ρjj_<sup>_∗_</sup> _|_ of the _p_ = 300 sample observed correlations and true correlations with a fixed gene _j_<sup>_∗_</sup> . Here _ρn,jj_<sup>_∗_</sup> is the sample correlation based on n observations of _Xj∗ ∼ N_ (0 _,_ 0 _._ 55), _Yj_ = 0 _._ 445 _Xj∗_ + _Zj_ , _Zj ∼ N_ (0 _,_ 0 _._ 55), so that the true correlations are 0.77.

|n|0.5-q|0.7-q|0.9-q|
|---|---|---|---|
|n=15|0.34|0.45|0.65|
|n=30|0.22|0.27|0.36|
|n=60|0.15|0.18|0.21|
|n=100|0.12|0.14|0.17|
|n=150|0.092|0.11|0.13|


33

considered.

#### **2.7.1 Data-generating distribution**

We create a data-generating distribution by assuming a multivariate normal model and selecting the parameters ( **_µ_** _,_ **Σ** ). The first priority is to impose a cluster structure; in particular, we want _K_ = 3 clusters of genes. There are three clusters – cluster A, cluster B, and cluster C – and each contains 100 genes. Each cluster has a core set of genes that are more highly correlated with one another and a more weakly correlated set of peripheral genes. The genes in a given cluster have no correlation to genes in the other clusters. The clustered genes are embedded in a set of 300 other genes that have absolutely no correlation with other genes at all. The correlation matrix of the full set of 600 genes **_ρ_** is block diagonal. With this set-up we are trying to simulate what seems to be an important data structure: a fraction of the genes being studied are involved in the phenomenon of interest and even break down into several well-defined clusters, but there are many “noisy” genes on the array, which are not involved and whose presence makes it difficult to find the relevant clusters.

The mean expression levels are also set with the cluster structure in mind. The noisy genes have means near zero, with some individual genes exhibiting a mild amount of differential expression. Cluster A contains genes that are over-expressed, many quite strongly. Most genes in Cluster B are differently expressed, with slightly more being under-expressed than overexpressed. Cluster C contains genes with a wide range of expressions. Gene-specific standard deviations have different distributions for each cluster and for the noisey genes. Throughout this section, we use yellow for cluster A, violet for cluster B, and blue for cluster C.

#### **2.7.2 Subset rule**

The subset rule is applied to the true mean and covariance (not simulated data), so that we can examine properties of the target subset _S_ . The rule we use is typical of those applied in many microarray data analyses: first, screen for differently expressed genes and then apply cluster analysis. We will exclude genes with an absolute mean _|µj| <_ log2 1 _._ 5 = 0 _._ 58, which corresponds to 1.5-fold differential expression. Of the 600 genes, 318 are retained and 282 are excluded based on this screen.

The remaining 318 genes are provided to a cluster analysis routine, with the dissimilarity between two genes defined as 1 minus the absolute value of the correlation. For a fixed number of clusters _K_ , a partitioning method finds the best grouping and, by exploring different values of _K_ , we can assess the evidence for different _K_ values (see Kaufman and Rousseeuw, 1990, chap. 1, sect. 3). It is also valuable to have a way to assign meaning to a particular cluster label _k_ ; most scientific papers that employ cluster analysis to analyze microarray data discuss the unifying theme of the genes found in each cluster. In the context of one data set, any clustering algorithm will likely yield at least one partition that can be interpreted. However, when one views a data set and its clustering as just one realization of a stochastic phenomenon, it is desirable to have a way to enforce a coherent meaning for cluster label _k_ . The cluster centers that are important in most partitioning methods play this role very well. By fixing cluster centers, one can ensure it is sensible to compare genes with label _k_ from one realization of the experiment to the next. Lastly, we prefer an algorithm called “partitioning around medoids” (PAM) (Kaufman and Rousseeuw, 1990, chap. 2) to k-means because we like being able to use any distance metric and we prefer that cluster centers be one of the underlying objects (in this

34

Table 2.12: Average Silhouettes for _K_ = 2 _,_ 3 _,_ 4 in simulation study.

|Which<br>genes?|K|Overall<br>Avg.<br>Silh.|Cluster<br>1|Cluster<br>2|Cluster<br>3|Cluster<br>4|
|---|---|---|---|---|---|---|
|318|2|0.09|0.06|0.17|||
|genes|3|0.13|0.12|0.17|0.11||
|(67 noise)|4|0.09|0.12|0.02|0.04|0.11|
|251|2|0.07|0.03|0.17|||
|genes|3|0.09|0.04|0.17|0.10||
|(no noise)|4|0.05|0.04|0.06|0.02|0.10|


case, a gene) instead of an average of objects, a quantity that is difficult to interpret and less robust to outliers.

Given any partition, Kaufman and Rousseeuw (1990) define for each object a quantity called the silhouette, which reflects how well-matched an object is in its cluster versus the next closest cluster. Silhouettes take values in the interval [ _−_ 1 _,_ 1], with 1 corresponding to a perfect match. Silhouettes are a valuable tool for assessing what is basically the goodness-of-fit for a clustering. For a given data set and clustering method, silhouettes can be compared for different numbers of clusters in order to choose the optimal number. There were 251 genes in clusters A, B, and C that passed the differential expression screen (318 - 251 = 67 noise genes pass the screen, but have silhouettes of zero). Silhouettes were examined for _K_ = 2 _,_ 3 _,_ and 4. When _K_ = 2, we see that cluster B is fully recovered, while clusters A and C are lumped together. When _K_ = 3, which we know to be the correct value of _K_ , and we see that PAM recovers the underlying clusters. When _K_ = 4, clusters A and C are fully recovered and Cluster B is split into two. The lack of evidence for _K_ = 4 is apparent in the erratic, even negative, silhouettes for genes in cluster B. The core versus periphery structure of the underlying clusters is also reflected in the silhouettes. Table 2.12 presents average silhouettes for these clusterings, with and without the 67 noise genes that pass the differential expression screen. We see that the overall average silhouette is highest at the correct value of _K_ , which is 3, regardless of the presence of the noise genes. But the noise genes have a dampening effect on the silhouettes in general. This points out the benefit of eliminating all unrelated genes prior to attempting any type of cluster analysis.

After clustering the genes, we chose to apply one last screen in another attempt to eliminate uninteresting genes. The goal is to remove genes that are not particularly well-matched to their cluster. We used two different approaches, one based on pairwise dissimilarities and one based on silhouettes. The dissimilarity screen DYS works in this manner: the cluster center (or “medoid”) is automatically included. Any gene with a dissimilarity of less than 0.655 with the cluster center is included. Any gene with a dissimilarity of less than 0.655 with any previously included gene is also included. This last step is repeated until no changes occur. The silhouette screen SILH includes all genes with a silhouette greater than 0.08. Both of the screens result in target subsets _S_ containing 150 genes. Table 2.13 presents target subset _S_ membership by true cluster membership for both screens.

To summarize the subset rule, the genes were first screened for differential expression by requiring that _|µj| >_ 0 _._ 58. The remaining 318 genes are clustered by PAM, with the cluster number _K_ = 3. The cluster centers are noted and will be fixed in future analyses. In light of the clustering, genes are screened again based either on dissimilarities or silhouettes to yield a

35

Table 2.13: Target subset membership by true cluster membership.

|||Targe|t Subs|et _Sj_ =|||
|---|---|---|---|---|---|---|
|True|0|1|2|3|_>_0|All|
|DYS screen|||||||
|Noise|300||||0|300|
|Cluster A|50|50|||50|100|
|Cluster B|27||73||73|100|
|Cluster C|73|||27|27|100|
||450|50|73|27|150|600|
|SILH screen|||||||
|Noise|300||||0|300|
|Cluster A|71|29|||29|100|
|Cluster B|12||88||88|100|
|Cluster C|67|||33|33|100|
||450|29|88|33|150|600|


final subset containing 150 genes and their cluster labels.

#### **2.7.3 Sampling distribution of S**<sup>�</sup> _n_

We generated 100 samples of size _n_ = 25 _,_ 50 _,_ and 150 from the chosen data-generating distribution _N_ (( **_µ_** _,_ **Σ** )) and applied the two subset rules described above. Based on these samples, we can estimate the reappearance probabilities _pj_ and _p_<sup>_k_</sup> _j_<sup>.InFigure</sup><sup>**??**,weexaminetheeffect</sup> of sample size in the DYS screen. The results are somewhat counter-intuitive but illustrate an important phenomenon. At the series of sample sizes considered here ( _n_ = 25 _,_ 50 _,_ 150), overall _pj_ tend to decrease for all genes. Average _pj_ within different values of _S_ are presented in the lower left panel. But it is important to examine the cluster-specific reappearance probabilities. The top panel presents this information for 4 typical genes, one for each value of _S_ , and the lower right panel presents averages within values of _S_ . We see that, while overall _pj_ may be declining, the correct cluster-specific _p_<sup>_k_</sup> _j_<sup>areclimbingsteadily.Oneexpectsthat,hadweadded</sup> a larger sample size such as _n_ = 300, even the overall _pj_ would begin to increase as _n_ does.

The results of this simulation demonstrate that the mean requires much less data to estimate than the covariance structure. For all sample sizes, the expected number of genes passing the differential expression screen is very close to the true number of 318. It is approximately 325, 323, and 321 for _n_ = 25 _,_ 50 _,_ and 150, respectively. From other simulations not reported here, in which the subset rule consists solely of the differential expression screen, we know that both sensitivity and positive predictive value at this stage are extremely high (between 0.95 and 0.99) and, therefore, the _correct_ genes are almost always passing this initial screen at all sample sizes. The problem occurs in the clustering and DYS screen – that is, the steps of the subset rule that depend on the covariance. At _n_ = 25, many genes are misclassified into the incorrect cluster, but frequently pass the dissimilarity screen due to sampling variability in the covariance. Since a gene can pass this screen by exhibiting even one extremely small pairwise distance, it is almost always passed for small samples. Therefore, the probability of appearing in the **S**<sup>�</sup> _n_ has significant contributions from all three cluster-specific probabilities _p_<sup>1</sup> _j_<sup>_, p_2</sup> _j_<sup>,and</sup><sup>_p_3</sup> _j_<sup>.Thiscanbeseeninthe</sup> first stacked column for each of the 4 genes highlighted in the top panel of Figure **??** . As the

36

Table 2.14: Cluster-wide quality measures for the DYS rule in the simulation study.

||n = 25|n = 50|n = 150|
|---|---|---|---|
|E_{_Sens_}_|0.98|0.97|0.77|
|E_{_PPV_}_|0.45|0.50|0.84|
|E_{_PEFP_}_|0.00|0.00|0.00|
|PAFP|0.48|0.09|0.00|


sample size increases to 50 and 150, this misclassification decreases and _pj_ becomes dominated by the correct cluster-specific probability. This can be seen in the second and third stacked columns. These simulation results suggest a modification of the DYS screen in which a gene must have a sufficiently small dissimilarity specifically with the cluster center.

The behavior described above is also apparent in subset-wide measures of quality, reported in Table 2.14. As expected, the sensitivity decreases at these sample sizes, but the positive predictive value increases. Once again, we conjecture that the sensitivity would increase for _n >_ 150. Extremely false positives were defined as genes with absolute mean expression less than log2 1 _._ 1 _≈_ 0 _._ 14. The expected proportion of extremely false positives (E _{_ PEFP _}_ ) is essentially zero for all _n_ and the probability of any extremely false positives (PAFP) decreases as _n_ grows.

The situation is quite different for the subset rule SILH that screens based on the silhouettes. Summary information on _pj_ and _p_<sup>_k_</sup> _j_<sup>isdepictedgraphicallyinFigure</sup><sup>**??**.</sup> It is immediately apparent that the reappearance probabilities are much lower in general than those seen with the DYS rule. This is due to the fact that, compared to the silhouettes produced by the true block diagonal correlation matrix, the silhouettes in observed data are lower. The average silhouette in the target subset _S_ is 0.09. The expected average silhouette in the sample subset **S**<sup>�</sup> is 0.02. The non-zero empirical correlation that arises between even unrelated genes has the effect of making the clustering appear to be less strong. Therefore, when applying the silhouette cutoff to a clustering based on a finite amount of data, we are left with a smaller set of genes. The average size of **S**<sup>�</sup> _n_ is approximately 32, 27, and 43 for _n_ = 25 _,_ 50 _,_ and 150, respectively. Both the expected subset size and the _pj_ and _p_<sup>_k_</sup> _j_<sup>seem to grow very slowly as the sample size increases.We</sup> have also noted here and in other analyses that the values of the silhouettes are very dependent on the dimension of the data set (number of genes), so that universal cutoff values as described in Kaufman and Rousseeuw (1990) are not appropriate in the gene expression context. One screen that may be more useful than absolute cutoffs based on silhouettes is to always retain a fixed number of top-ranked genes based on silhouettes or estimated cluster-specific probabilities. If one wishes to test the significance of a silhouette, we propose using a simulation from an appropriate null distribution (i.e.: one with no clustering).

Table 2.15 presents subset-wide measures of quality for the SILH rule. Both sensitivity and positive predictive value increase with _n_ and the probability of any false positive is extremely small even at _n_ = 25 and quickly falls to zero.

We are also interested in the actual gene-specific probabilities _pj_ and _p_<sup>_k_</sup> _j_<sup>.Forgenesin</sup><sup>_S_</sup> for the DYS rule, although the overall _pj_ decrease, the correct cluster-specific probabilities _p_<sup>_k_</sup> _j_ increase with _n_ . In fact, at _n_ = 150, essentially no genes appear in **S**<sup>�</sup> carrying the incorrect cluster label. This observation supports the above discussion of the DYS rule. Consistent with the above findings regarding the stringency of the silhouette-based screen, we see relatively low _pj_ , which grow very slowly with _n_ , for the SILH rule. The misclassification of genes is practically

37

Table 2.15: Cluster-wide quality measures for the SILH rule in the simulation study.

||n = 25|n = 50|n = 150|
|---|---|---|---|
|E_{_Sens_}_|0.18|0.18|0.28|
|E_{_PPV_}_|0.86|0.98|0.99|
|E_{_PEFP_}_|0.00|0.00|0.00|
|PAFP|0.04|0.00|0.00|


impossible with this rule.

#### **2.7.4 Bootstrap results**

For each of the 100 size _n_ samples generated from the data-generating distribution _N_ (( **_µ_** _,_ **Σ** )), we carried out the parametric bootstrap as described in van der Laan and Bryan (2001). Since the simulated data is multivariate normal distributed here, the use of this distribution in the bootstrap is appropriate. The empirical distribution of the bootstrap subsets allows us to estimate interesting features of the sampling distribution of **S**<sup>�</sup> . The probability of gene _j_ appearing in **S**<sup>�</sup> _n_ , i.e. _pj_ , is estimated by the proportion of bootstrap subsets in which gene _j_ appears. An analogous approach leads to estimates of _p_<sup>_k_</sup> _j_<sup>.Figures</sup><sup>**??**and</sup><sup>**??**plottruereappearance</sup> probabilities against average bootstrap probabilities for the DYS and SILH rules, respectively.

In finite samples, the expected bootstrap probabilities are biased estimators of the true probabilities. For certain simple rules, this bias is relatively straightforward to quantify and is discussed in **?** ). For complicated rules such as DYS and SILH, the only relevant result is that, as _n →∞_ , the expected bootstrap probabilities will approach 1 for genes in _S_ and 0 for all other genes. Graphically, this means that as _n →∞_ , we will eventually see points only at (0,0) and (1,1). But for finite _n_ , plots such as **??** and **??** are the best way to understand the relationship between the expected bootstrap and true reappearance probabilities.

#### **2.7.5 Distribution of the sample mean**

For a fixed _n_ and _δ_ , the formula stated below in equation 2.4.2 can be solved for the _ϵ_ such that the probability of even one component of the _p_ -dimensional sample mean **_µ_** � _n_ varying by more than _ϵ_ from the corresponding component of the true mean **_µ_** is less than 0 _< δ <_ 1. The sample size is quite conservative, since it does not exploit the correlation among the genes. That is, when one computes values of _ϵ >_ 0 as described below, the actual probability of max _j |µ_ � _j − µj | > ϵ_ is much less then _δ_ . Table 2.16 illustrates this and also shows that one can use a value of _σ_ that is much smaller than the actual maximum of the gene-specific log ratio standard deviations and still see favorable results. In all instances, _n_ = 25 and _M_ = 5.

An alternative, less conservative approach to determining the sample size needed for a certain precision is to perform simulations utilizing the correlation structure in the data. By the central limit theorem, we have that the sample mean _µ_ **ˆ** is asymptotically distributed _N_ ( _µ_ **ˆn** _,_ **Σ**<sup>**ˆ**</sup> **n** ). By simulating from this distribution, we can determine the sample sizes needed for different levels of precision. Non-parametric simulations could also be employed.

38

Table 2.16: Demonstration that the sample size formula is conservative.

|Nominal _δ_|_ϵ_|Actual _δ_|_σ_|
|---|---|---|---|
|0.05|2.64|0.000|max_j σj_ = 2_._06|
|0.50|2.27|0.000|max_j σj_ = 2_._06|
|0.20|1.52|0.005|75-th quantile of _σj_ = 0_._89|
|0.40|1.14|0.030|25-th quantile of _σj_ = 0_._37|
|0.80|1.01|0.055|0.25|


#### **2.7.6 Conclusions**

These simulations illustrate some important issues encountered in cluster analysis of gene expression data. In particular, we see that sampling variability of the covariance structure and the presence of unrelated genes can have a strong impact on partitioning algorithms and measures of cluster strength and stability. We have found that pre- and post-screening of the genes helps to avoid some of these problems. The simulations show that screens based on differential expression are accurate even for small sample sizes, whereas screens based on the covariance are harder to estimate accurately. One drawback of screening the genes, however, is that important or interesting genes can be excluded along with the “noisy” genes we wish to remove.

In response to this issue, we have developed an algorithm called Hierarchical Ordered Partitioning And Collapsing Hybrid (HOPACH), which incorporates both partitioning and agglomerative steps in order to identify clustering patterns in the data even in the presence of many unrelated genes. We have conducted simulations which illustrate that this methodology does better than simple partitioning or agglomerative methods at identifying small clusters in the presence of many noisy genes (van der Laan and Pollard (2001)). In Section 2.5 we outline the HOPACH method and apply it to a cell line data set with two subpopulations. We also demonstrate methods for selecting differently expressed genes using a null distribution.

### **2.8 Simulations to compare different bootstrap methods.**

We report here on a simulation study carried out in Pollard and van der Laan (2001). The nonparametric bootstrap has the advantage of being computationally much easier than the parametric bootstrap. In addition, the nonparametric bootstrap avoids distributional assumptions about the parameter of interest, whereas the estimation of the distribution of<sup>_√_</sup> _n_ (Σ _n −_ Σ) using the parametric bootstrap is only consistent under the model assumption. There is reason to believe, however, that the parametric bootstrap might perform better in the gene-expression context, where the number of observations _n_ is typically very small relative to the dimension _p_ (number of genes). The performance of the bootstrap is measured by how well the distribution of _θn_<sup>#approximates thedistribution of</sup><sup>_θ_</sup> _n_<sup>.Itis clear thatthis performanceis mainly dependent</sup> on how close **P** _n_ is to _P_ . Our initial feeling was that in this setting, the empirical distribution _Pn_ (i.e. nonparametric bootstrap) might be an inappropriate estimate of _P_ . Another fact of interest is that the nonparametric bootstrap is known to be inconsistent in various low-dimensional examples, while the parametric bootstrap is consistent under minimal additional assumptions given that the parametric model is correct Gin´e and Zinn (1990).

With these ideas in mind, we conducted a simulation study to assess the asymptotic validity of the nonparametric, convex, and parametric bootstraps for estimating the distribution of a

39

gene clustering parameter. We used _p_ = 3000 genes and _n_ = 40 samples. These choices reflect typical dimensions of the data matrix _X_ (possibly after prescreening) as seen in commercial and academic settings. In order to investigate the effect of asymptotics on our results, we repeated the simulations using _n_ = 250 samples.

#### **2.8.1 Simulation: Multivariate Normal Data (with diagonal covariance)**

This simulation investigates gene clustering. The true data generating distribution was chosen to be a multivariate normal with diagonal covariance matrix so that the genes were uncorrelated. For simplicity, a fourth of the genes was generated from each of four distributions: _N_ (0 _._ 5 _,_ 0 _._ 25), _N_ ( _−_ 0 _._ 5 _,_ 0 _._ 5), _N_ (1 _,_ 1), _N_ ( _−_ 1 _,_ 0 _._ 75). The summary measures of interest were selected to be the 0.9 quantile of the maximum absolute difference in the mean vector, median vector, and correlation matrix. These measures give a good indication of how far a distribution is from the truth.

In order to define the “true” values of the summary measures, a large number _N_ draws from the true distribution were compared to the known mean, median and correlation. Results were compared for _N_ = 100 _,_ 1000 _,_ 10000 and showed little dependence on _N_ so that _N_ = 100 was deemed sufficient. Next, a single draw from the true distribution was identified as the ”observed” data and the three types of bootstrap were performed with convex repeated for _d_ = 0 _._ 1 _,_ 0 _._ 3 _,_ 0 _._ 5. In each case, _B_ = 100 bootstrap samples were generated from which the 0.9 quantiles were calculated. In order to investigate the variability of these measures, we repeated each simulation twenty times with _n_ = 40, obtaining twenty sets of 0.9 quantiles. From these, we calculated a mean and standard deviation. The coefficient of variation was on the order of 2.5% for the mean, 3.0% for the median and 1.25% for the correlation. These values were sufficiently small that we chose to use the results from just one simulation of _B_ = 100 bootstrap samples in each case.

Table 2.17 shows the results of Simulation 1. We found that the bootstrap is good at _n_ = 250 and a little conservative at _n_ = 40. At both sample sizes, the bootstrap performed poorly for the median, which is a known result. It is interesting to note that in contrast to our hypothesis, the nonparametric bootstrap actually performed well relative to the convex and parametric bootstrap. We had expected the convex bootstrap, a smoothed version of the nonparametric, to perform consistently better than the nonparametric, but instead found that the convex was more biased for the mean than the nonparametric, performing best when _d_ was smallest ( _d_ = 0 is equivalent to nonparametric).

This simulation suggests that the nonparametric and parametric bootstraps can be used to assess the variability of summary measures of gene clustering (see also van der Laan and Bryan (2001)). Since estimated variability in the means is quite accurate and estimated variability in the correlation is accurate at _n_ = 250 and conservative at _n_ = 40, then we should be able to assess the variability of subset rules of the form _S_ ( _µ,_ Σ) accurately (or at least conservatively) for reasonable sample sizes.

40

||0.9 qua|ntile of maxi|mum absolute difference|
|---|---|---|---|
|Parameter:|Mean|Median|Correlation|
|n=40||||
|True distribution|0.60|0.74|0.75|
|Nonparametric|0.60|0.98|0.89|
|Convex d=0.1|0.59|0.97|0.89|
|Convex d=0.3|0.54|0.86|0.88|
|Convex d=0.5|0.50|0.78|0.87|
|Parametric|0.63|0.93|0.84|
|n=250||||
|True distribution|0.25|0.30|0.35|
|Nonparametric|0.26|0.38|0.36|
|Convex d=0.1|0.23|0.34|0.36|
|Convex d=0.3|0.21|0.30|0.36|
|Convex d=0.5|0.20|0.27|0.36|
|Parametric|0.24|0.36|0.35|


Table 2.17: Results of Simulation 1 for gene clustering. _B_ = 100 i.i.d. bootstrap samples were used in each simulation. Every bootstrap sample included _n_ = 40 or _n_ = 250 observations of a 3000-dimensional gene expression vector. The 0.9 quantile of the maximum absolute difference in each summary measure is reported.

### **2.9 Data Analysis in Human Acute Leukemia**

Golub et al. (1999) analyze gene expression data in human acute leukemias to demonstrate a proposed method for discovering cancer classes (within a broader cancer diagnosis such as leukemia) and for predicting the class membership of a new tumor. The primary data consists of profiles for 38 leukemia patients, 27 of which have acute lymphoblastic leukemia (ALL) and 11 of which have acute myeloid leukemia (AML). For each patient there is a gene expression profile obtained from hybridization of bone marrow RNA to Affymetrix oligonucleotide microarrays. With oligonucleotide arrays, a specific probe (DNA fragment) is deposited on each spot on the array in a fixed quantity. With the cDNA arrays described earlier, there is much less control over the amount of probe placed on the array and that is the main reason for hybridizing two samples at once. By competitive hybridization, we can measure _relative_ expression and avoid relying on the absolute intensity measured from one sample alone. This technical distinction means that one can actually interpret the raw intensities from an Affymetrix chip and compare them from one patient to another.

We use our methodology to search for the subset of genes that are the best classifiers for diagnosis. It is clinically important and, apparently, difficult to distinguish the two tumor classes. Obviously, we want to look for genes which are differentially expressed in ALL patients versus AML patients. Since there is no natural pairing of measurements, we have chosen to form a reference AML expression for each gene by taking the geometric mean of the intensities across all 11 subjects. We use this as the denominator and form a ratio for each gene for all 27 ALL patients. Therefore _n_ = 27 and, after data pre-processing recommended by Golub et al. (1999), we have _p_ = 5925 genes.

41

Table 2.18: Data analysis bootstrap results on subset quality.

||Avg Boot|strap Estimate|
|---|---|---|
||_K_ = 2|_K_ = 3|
|Sensitivity|0.88|0.88|
|Positive Predictive Value|0.85|0.84|
|Prop. of Ext. False Pos.|0.00|0.00|
|Any Ext. False Pos.|0.00|0.00|
|0.90 quantile of max abs dev. (mean)|1.20|1.25|
|0.90 quantile of max abs dev. (std dev’n)|3.34|3.31|
|0.90 quantile of max abs dev. (corr)|1.00|1.00|
|0.90 quantile of max abs dev. (covar)|11.15|10.93|


We retained genes with at least 3-fold differential expression, which translates into an absolute log-ratio mean of at least 1.585. Of the original 5925 genes, 147 passed this pre-screen. We then ran PAM for several cluster numbers. The distance _Dij_ between genes _i_ and _j_ was defined as one minus the modified correlation proposed by Eisen et al. (1998). This quantity is obtained when one uses the normal formula for correlation _ρij_ = _σij /σiσj_ but replaces the means _µi_ and _µj_ with a user-specified reference value (in this case zero) in the usual calculation of covariance and standard deviation (e.g. _σij_<sup>_′_=</sup><sup>_E_(</sup><sup>_YiYj_),</sup><sup>_σ_</sup> _j_<sup>_′_=</sup> � _E_ ( _Yi_<sup>2),and</sup><sup>_ρ′_</sup> _ij_<sup>=</sup><sup>_σ_</sup> _ij_<sup>_′/σ_</sup> _i_<sup>_′σ_</sup> _j_<sup>_′_).</sup> As recommended by Kaufman and Rousseeuw we chose the number of clusters _K_ by inspecting the average silhouette widths for various values of _K_ . For _K_ = 2 _,_ 3, and 4, the average silhouette widths were 0 _._ 87 _,_ 0 _._ 74, , and 0 _._ 24 respectively (for _K_ = 5 _, . . .,_ 9, average silhouettes widths were consistently below 0 _._ 24). We decided to run the bootstrap for both _K_ = 2 and _K_ = 3 and omitted the post-screen in both cases. Genes with absolute mean less than 0 _._ 07, which corresponds to 1.05-fold differential expression or less, were deemed particularly unsuitable as classifiers and 1415 genes met this criterion in the observed data. We carried out 100 bootstrap iterations and, once the medoids for the observed data were found, the cluster centers were fixed at these medoids throughout the bootstrap.

Table 2.18 provides basic quality measures for the bootstrap subsets. We see that sensitivity and positive predictive value are high (around 85%) for both bootstraps and we see no extremely false positives. Figure **??** presents the single-gene proportions from the bootstrap both the _K_ = 2 and _K_ = 3 cases; the length of each horizontal bar represents the number of bootstrap iterations in which a particular gene appears in the bootstrap subset. Since the cluster centers were fixed, we can also report the stability of cluster labels and the relative frequency of each label is depicted by the shading within the horizontal bars. We see that, when increasing the cluster number from 2 to 3, in fact we split one existing cluster into two and leave one cluster untouched. In both cases, the genes in the estimated subset reappear extremely often and almost always carry the same label as in the estimated subset. Overall, the stability of these clusters is quite strong. This is confirmed by the cluster-specific quality measures presented in table 2.19.

42

Table 2.19: Data analysis bootstrap results on cluster stability.

||_K_|= 2 Bo|otstrap Avg.||_K_|= 3 Bo|otstrap Avg.||
|---|---|---|---|---|---|---|---|---|
|Cluster|Medoid|Size|Sensitivity|Pred.|Medoid|Size|Sensitivity|Pred.|
|||||Value||||Value|
|1|1936|106.2|0.90|0.89|1936|106.3|0.89|0.89|
|2|5706|47.6|0.85|0.78|2227|13.9|0.83|0.76|
|3|||||3816|34.2|0.81|0.75|
|||153.8|0.88|0.85|1|154.3|0.88|0.84|


43

44

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Bibliography →](03-bibliography.md)
