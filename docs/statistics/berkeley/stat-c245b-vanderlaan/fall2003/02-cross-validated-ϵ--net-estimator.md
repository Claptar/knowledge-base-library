---
title: CROSS-VALIDATED ϵ -NET ESTIMATOR
source: https://vanderlaan-lab.org/teach-files/fall2003.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/fall2003.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# CROSS-VALIDATED ϵ -NET ESTIMATOR

**Source:** [`fall2003.pdf`](https://vanderlaan-lab.org/teach-files/fall2003.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Mark van der Laan**

Joint work with Sandrine Dudoit, Peter Dimitrov. Division of Biostatistics, University of California, Berkeley. September 6, 2003 Department of Statistics, Neyman Seminar _⃝_ c Copyright 2003, all rights reserved

#### **SELECTION IN REGRESSION**

Let _O_ 1 = ( _Y_ 1 _, W_ 1) _, . . . , On_ = ( _Yn, Wn_ ) be _n_ i.i.d. observations of _O_ = ( _Y, W_ ) _∼ P_ 0, where _Y_ denotes an outcome of interest and _W_ is a _d_ -dimensional vector of covariates. Let _M_ be a model for _P_ 0. Let _ψ_ 0( _w_ ) = _EP_ 0( _Y | W_ ) be the parameter (function) of interest, and let **Ψ** = _{EP_ ( _Y | W_ ) : _P ∈M}_ be the parameter space. Let _L_ ( _O, ψ_ ) be the squared error loss function for a candidate _ψ_ whose expectation is minimized by _ψ_ 0:

= _ψ_ 0 argmin _ψ∈_ **Ψ** _E_ 0 _L_ ( _O, ψ | η_ 0) _._

Let _Pn_ be the empirical distribution of _O_ 1 _, . . . , On_ . Let _ψ_ ˆ _k_ ( _·_ ) = _ψk_ ( _· | Pn_ ) _∈_ **Ψ** , _k_ = 1 _, . . . , K_ ( _n_ ), be a collection of estimators (i.e., algorithms one can apply to data) of _ψ_ 0( _·_ ).

Page 313

**The Selection Problem:** Choose a data adaptive _k_<sup>ˆ</sup> = _k_<sup>ˆ</sup> ( _Pn_ ) so that

_≡ dn_ ( _ψ_<sup>ˆ</sup> _k_ ˆ _, ψ_ 0) _L_ ( _O, ψk_ ˆ( _· | Pn_ )) _− L_ ( _O, ψ_ 0)� _dP_ 0( _O_ ) �� = ( _ψk_ ˆ( _W | Pn_ ) _− ψ_ 0( _W_ ))<sup>2</sup> _dP_ 0( _W_ ) � _→_ 0 _,_ at asymptotically optimal speed.

**THE OPTIMAL BENCHMARK SELECTOR** Let _≡ k_ ˜ _n_ argmin _kdn_ ( _ψ_<sup>ˆ</sup> _k, ψ_ 0) = argmin _k L_ ( _o, ψk_ ( _· | Pn_ )) _dP_ 0( _o_ ) _._ � This optimal benchmark selector (for each given data set) depends on the unknown data generating distribution _P_ 0.

Page 314

Asymptotic equivalence with benchmark selector: Given the _K_ ( _n_ ) candidate estimators, a selector _k_<sup>ˆ</sup> = _k_<sup>ˆ</sup> ( _Pn_ ) is asymptotically equivalent with the optimal benchmark if _dn_ <u>(</u> _ψ_<sup>ˆ</sup> _<u>k</u>_ ˆ _, ψ_ 0) _→_ 1 in probability. _dn_ ( _ψ_<sup>ˆ</sup> _k_ ˜ _n, ψ_ 0) In particular, then it is asymptotically optimal.

Page 315

**THE CROSS-VALIDATION SELECTOR**

Define random vector _Sn ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> for splitting the sample into a validation and a training sample.

_Sn,i_ =

 0 if i-th observation is in the training sample  1 if i-th observation is in the validation sample 

Different choices of _Sn_ cover all types of cross-validation including _V −_ fold cross-validation, monte carlo cross validation (bootstrap cross-validation): e.g. 5-fold cross-validation: _Sn_ has 5 realizations.

Page 316


<!-- Start of picture text -->
Let p  =  n 1 /n be the proportion constituting the validation sample.<br>Let Pn,S 0 n , P n,S  1 n be the empirical distributions of the training and<br>validation sample, respectively.<br>The selector is defined by:<br>k ˆ ≡ argmin kESn L ( o, ψk ( · | Pn,S 0 n )) dP n,S  1 n ( o )<br>�<br>=<br>argmin kESn � ( Yi − ψk ( Wi | Pn,S 0 n ))2 .<br>i : Sn ( i )=1<br><!-- End of picture text -->

Page 317

#### **FINITE SAMPLE RESULT**

Define the distance function for estimators based on training samples of size _n_ (1 _− p_ ):


_k_ ˆ aims to minimize _k → dn_ (1 _−p_ )( ˆ _ψk, ψ_ 0). Denote the minimizer, i.e. the optimal comparable benchmark selector for _n_ (1 _− p_ ) observations, with:


Page 318

Suppose that the loss function _L_ ( _O, ψ_ ) is uniformly bounded by a universal _M_ 1, and

VAR0 _{L_ ( _O, ψ_ ) _− L_ ( _O, ψ_ 0) _} ≤ M_ 2 _E_ 0 _{L_ ( _O, ψ_ ) _− L_ ( _O, ψ_ 0) _} ._ For any _δ >_ 0, we have for a specified constant _C_ ( _M_ 1 _, M_ 2 _, δ_ ) = 2(1 + _δ_ )<sup>2</sup> ( _M_ 1 _/_ 3 + _M_ 2 _/δ_ )

_≤ Edn_ (1 _−p_ )( _ψ_<sup>ˆ</sup> ( _k_<sup>ˆ</sup> ) _, ψ_ 0) (1 + _δ_ ) _Edn_ (1 _−p_ )( _ψ_<sup>ˆ</sup> ( _k_<sup>˜</sup> _n_ (1 _−p_ )) _, ψ_ 0) +<sup>_C_</sup><sup><u>(</u></sup><sup>_M_1</sup><sup>_<u>, M</u>_2</sup><sup>_<u>, δ</u>_</sup><sup><u>) log</u></sup><sup>_K_</sup><sup><u>(</u></sup><sup>_n_</sup><sup><u>)</u></sup> _. np_

Page 319

**COROLLARY: ASYMPTOTIC OPTIMALITY** If _p_ = _p_ ( _n_ ) _→_ 0 slowly enough with sample size, so that log( _K_ <u>(</u> _n_ <u>))</u> _Edn_ ( _ψ_<sup>ˆ</sup> ( _k_<sup>˜</sup> _n_ ) _, ψ_ 0) _→_ 0 _, np_ ( _n_ ) � then _Edn_ <u>(</u> _<u>ψ</u>_<sup>ˆ</sup> <u>(</u> _k_<sup>ˆ</sup> <u>)</u> _<u>, ψ</u>_ 0) _→_ 1 _. Edn_ ( _ψ_<sup>ˆ</sup> ( _k_<sup>˜</sup> _n_ ) _, ψ_ 0) That is, the data adaptive selector _k_<sup>ˆ</sup> is asymptotically equivalent (and thus optimal) with the optimal benchmark selector.

Page 320

**THE ADAPTIVE** _ϵ_ **-NET ESTIMATOR**

**SUB-PARAMETER SPACES** Let **Ψ** _s ⊂_ **Ψ** be sub-parameter spaces indexed by _s ∈{_ 1 _, . . . , K_ 1( _n_ ) _}_ . Let **Ψ** 1 = **Ψ** . **CONSTRUCT** _ϵ_ **-NETS:** For each subspace **Ψ** _s_ , for a given _ϵ >_ 0, let � _ψj_<sup>_ϵ,s, j_= 1</sup><sup>_, . . . , Ns_(</sup><sup>_ϵ_)</sup> � _⊂_ **Ψ** _s_

be an _ϵ_ -net of **Ψ** _s_ . Here _Ns_ ( _ϵ_ ) can be chosen equal to the covering number of ( **Ψ** _s, ∥· ∥_ **Ψ** ).

**MINIMIZE EMPIRICAL RISKS** Let

_n ψϵ,s_ ( _· | Pn_ ) _≡_ argmin _{ψj_<sup>_ϵ,s_</sup> : _j}_ �( _Yi − ψj_<sup>_ϵ,s_(</sup><sup>_Wi_))2</sup><sup>_._</sup> _i_ =1

Page 321

**SELECT** _ϵ, s_ **:** Let (ˆ _ϵ,_ ˆ _s_ ) be the ( _ϵ, s_ ) minimizing cross-validated empirical risk over a set of _K_ ( _n_ )-values: (ˆ _ϵ,_ ˆ _s_ ) _≡_ argmin _ϵ,sESn L_ ( _Y, ψϵ,s_ ( _W | Pn,S_<sup>0</sup> _n_<sup>))</sup><sup>_dP_1</sup> _n,Sn_<sup>(</sup><sup>_Y, W_)</sup><sup>_._</sup> � The adaptive _ϵ_ -net estimator is given by: _ψ_ ( _· | Pn_ ) = _ψϵ,_ ˆ _s_ ˆ( _· | Pn_ ) _._

Page 322

**FINITE SAMPLE RESULT FOR** _ϵ_ **-NET ESTIMATOR** Let


We have for any _δ >_ 0

_Edn_ (1 _−p_ )( _ψ_ ( _· | Pn_ ) _, ψ_ 0) _≤_ (1 + 2 _δ_ )min (1 + 2 _δ_ ) _B_ 0( _ϵ, s_ ) + 2 _C_ ( _M_ 1 _, M_ 2 _, δ_ )<sup>1 + log(</sup><sup>_Ns_</sup><sup><u>(</u></sup><sup>_ϵ_</sup><sup><u>))</u></sup> _ϵ,s_ � _n_ (1 _− p_ ) <u>�</u> _._ +2 _C_ ( _M_ 1 _, M_ 2 _, δ_ )<sup>1 + log(</sup><sup>_K_</sup><sup><u>(</u></sup><sup>_n_</sup><sup><u>))</u></sup> _np_

Page 323

**Adaptivity:** This finite sample inequality in terms of approximation errors of the _ϵ_ -nets and the covering numbers _Ns_ ( _ϵ_ ) implies that the estimator is adaptive, that is, it achieves the optimal rate of convergence for the smallest subspace still containing the true _ψ_ 0.

Page 324

**LARS/LASSSO VERSUS Epsilon-NET ESTIMATOR: SIMULATION**

We simulate data sets from a linear regression _Y ∼ βX_ + _N_ (0 _, σ_<sup>2</sup> ) with _X_ ( _j_ ) _∼ U_ (0 _,_ 1), _j_ = 1 _, ..,_ 10, _σ_<sup>2</sup> = 2, and uniformly distributed regression coefficients _β_ . We generated 2 simulated data sets of various sample sizes, and compared the _ϵ_ -net linear regression estimator of _β_ with the Least-Angle-Linear Regression estimator, (lars) based on residual sum of squares on an independent sample of 10,000 observations. “Lars” which has similar performance as the _L_ 1-penalized regression estimator (Lasso).

Page 325

|Sample size|eps-net|sd.eps-net|lars|sd.lars|
|---|---|---|---|---|
|20|77035.2|33114|183255.2|141810.6|
|50|52000|7143.2|81550.9|39228.6|
|100|45133.5|3447.5|60348.8|20702|
|200|42145.3|912.3|46798.5|7036.4|
|500|40886.5|586.3|43790.7|2394.7|
|1000|40738.6|471.8|43233.9|2702.7|
|2000|40348.2|400.6|40977.5|1095.3|
||Table|11: Sigma=|2||


Page 326

|Sample size|eps-net|sd.eps-net|lars|sd.lars|
|---|---|---|---|---|
|20|73228|17601.2|731493.2|995771.5|
|50|51217.6|5992.5|76624.4|38065.6|
|100|45166.5|3690.1|55813.6|11746.9|
|200|42189.6|1754.1|51473.8|15664.4|
|500|40719.4|640.4|44636.3|6696.1|
|1000|40090.4|691|40724|943.8|
|2000|39987.2|573.7|40409.8|706.6|
||Table|12: Sigma=|2||


Page 327


Page 328


<!-- Start of picture text -->
Mean RSS values of Eps−net and LARS<br>50000 100000 150000 200000 250000 300000<br>Page 329<br>20<br>50<br>100<br>200<br>Number of Observations<br>500<br>LARS Eps−net<br>1000<br>2000<br><!-- End of picture text -->


<!-- Start of picture text -->
Mean RSS values of Eps−net and LARS<br>0 500000 1000000 1500000<br>Page 330<br>20<br>50<br>100<br>200<br>Number of Observations<br>500<br>LARS Eps−net<br>1000<br>2000<br><!-- End of picture text -->

# **CLUSTERING ALGORITHMS and a STATISTICAL FRAMEWORK**

**Mark van der Laan** Division of Biostatistics, UC Berkeley `www.stat.berkeley.edu/~laan` www.bepress.com/ucbbiostat/

- _⃝_ c Copyright 2003, all rights reserved

#### **CLUSTERING**

Consider a collection of _n p_ -dimensional vectors. This can be represented as a _p × n_ -matrix.

As statisticians, we like to think as these _n_ vectors as a random sample consisting of _n_ independently and identically distributed observations of a random vector. For example, this random vector might represent the gene expression profile of a randomly drawn person from a population of cancer patients.

Clustering columns: For each pair of _p_ -dimensional vectors compute a dissimilarity. Let _D_ be the _n × n_ -distance/dissimilarity matrix. Clustering rows: Construct a _p × p_ dissimilarity matrix.

Page 332

A (model free) clustering algorithm maps a distance matrix and a user supplied _K_ into a _n_ -dimensional (or _p_ -dimensional) vector of cluster labels ranging in _{_ 1 _, . . . , k}_ .

A clustering algorithm is defined by maximizing a performance criterian measuring the performance for a given clustering result, where the maximization is over an allowed set of possible cluster results.

Keep in mind, given _K_ :

Different criterian = _⇒_ Different Clusters. Different allowed set = _⇒_ Different Clusters. Differen dissimilarity = _⇒_ Different Clusters. Different criterian/dissimilarity/allowed set = _⇒_ Different VARIABILITY (across sample fluctuations) of clusters.

Page 333

What dissimilarity matrix to use? What clustering algorithm (defined by allowed set and criterian) to use?

Approach: 1) Understand the dissimilarity choice, 2) Understand the criterian and allowed set, 3) Understand variability and 4) Interpret results. Repeat 1–4 for different choices of dissimilarities and clustering algorithms.

Page 334

#### **BOOTSTRAP**

What does variability of clusters mean? **Answer:** In general, variance/variability of the sampling distribution of the clustering algorithm (this is a random vector or matrix) is a measure of spread of this sampling distribution around the true wished clustering result (one would have seen if the sample size is infinitely large).

Consequently, variance of clusters is calculated from a large sample of clustering results where each clustering result is obtained by resampling _n_ vectors, and applying the clustering algorithm. **Measuring variability:** There are a large number of ways of measuring the variance of these resampled clustering results depending on how one measures distance between a sampled clustering result and the aimed clustering result. Some specific

Page 335

proposals, such as cluster specific sensitivity, cluster specific positive predictive value, gene specific membership probabilities (with corresponding cluster-probabillity plot), are provided in van der Laan, Bryan (2001) (www.stat.berkeley.edu/ laan). **How to estimate variability? Resample from an estimate of the true data generating distribution** . For example, resample _n_ vectors from the empirical distribution of the _n_ vectors which puts probability 1 _/n_ on each observation.

This statistical procedure, that is, _resampling with the purpose of estimating the variance of a data analytic result_ , is called Bootstrap.

Page 336

#### **CLUSTERING OF MICROARRAY DATA**

Clustering has important applications in the analysis of gene expression data. Consider a sample of _n_ patients and suppose we collect a _p_ -dimensional gene expression profile on each patient. Important results can be obtained by:

- Clustering of the _p_ genes ( _n_ dimensional vectors).

- Clustering of the _n_ patients ( _p_ dimensional vectors).

- Clustering genes, and within each cluster of genes, cluster patients.

- Clustering genes, reduce each patients’ gene expression profile to the vector of cluster-specific medoids/centers. This vector of medoids can be used as a fingerprint and as a set of predictors of an outcome of interest (e.g. survival).

Page 337

Give example of 3 cancer groups of patients. Clustering genes. What distance would show what clusters of genes? Different algorithms can still show different results. e.g. hierarchical with binary splits! is an example of a constraint allowed set. Also show clustering patients within clusters of genes, we have transparencies on that.

Page 338

#### **DISSIMILARITIES**

Possible dissimilarities between a pair of vectors are:

- EUCLIDEAN DISTANCE

- 1 MINUS CORRELATION

- 1 MINUS ABSOLUTE CORRELATION

- 1 MINUS COSINUS ANGLE

Page 339

#### **VISUALIZATION OF DISTANCE MATRIX**

Assign a color ranging (e.g.) from red (close) to blue (far) to each pairwise distance _dij_ in the _n × n_ -distance matrix. Now, visualize the image.

VISUALIZING CLUSTERS:

- 1) order elements <u>within</u> clusters.

- 2) order clusters

- 3) visualize the <u>reordered</u> distance matrix.

Other visualisation tools: visualize elements in two dimensional plane by projecting on the space spanned by principal components, visualize reordered data matrix.

Page 340

#### **PARTITIONING ALGORITHMS**

Possible partitioning algorithms are:

- PARTITIONING AROUND MEDOIDS(PAM). Choose _K_ centers such that the sum of the distances to the closest center is minimal.

- PARTITIONING AROUND MEDOIDS MAXIMIZING AVERAGE SILHOUETTE. Given the cluster labels, for each element its silhouette is defined as the relative difference between average distance to its own cluster and average distance to the neighboring cluster: this is a number between -1 and 1 (Kaufman and Rousseeuw, 1990). Choose _K_ centers (which define the clusters) so that the sum of the silhouettes is maximal.

- KMEANS. Choose _K_ groups such that the sum of the distances to the closest cluster specific mean is minimal. The typical

Page 341

   - implementation of KMEANS uses the Euclidean Distance.

- SELF-ORGANIZING MAPS. Similar as KMEANS, but it constraints the allowed set of partitions.

- HIERARCHICAL BINARY TOP-DOWN CLUSTERING. One splits the group in two clusters. Subsequently, one splits each of the two clusters in two to obtain 4 clusters and so on.

   - Note, this restricts the class of allowed partitions: e.g., not each possible 4 groups is considered as an allowed clustering result.

Page 342

Discuss a little simulation 3 groups of patients own groups of genes. Illustrate different dissimilarities are going to show different things. Show a picture of clustering results for PAM, PAMSIL.

Page 343

#### **HIERARCHICAL CLUSTERING**

**DOWN-TOP AGGLOMERATIVE** CLUSTERING Start with single element clusters. Collapse the 2 closest clusters into one cluster and repeat this procedure till all elements are together. This produces a hierarchical tree. Each level correponds with a clustering result. Ordering of the clusters is completely determined by the initial ordering.

**NON-BINARY HIERARCHICAL CLUSTERING** Same, but allow partitioning in 2 or more clusters. If one orders the children of each parent cluster by their distance to closest uncle node, then running down the tree yields an <u>ordered list.</u> For details: **Hierarchical Ordered Partitioning and Collapsing Hybrid** (HOPACH) (van der Laan, Pollard, 2002).

Page 344

#### **SELECTION OF NUMBER OF CLUSTERS**

A difficult (ill posed) problem!

Visualization of ordered distance matrix for different number of clusters _K_ is a helpful tool to select number of clusters.

Formally, the idea is to come up with a criteria measuring strenght of a clustering result, which allows comparison of clustering results for different _K_ , so that its maximum defines an “optimal” number of clusters.

The <u>problem</u> is: Different criteria give different ”optimal clustering results”.

A large collection of proposals have been made (for a overview of literature and new proposals, see papers on websites www.stat.berkeley/ dudoit and www.stat.berkeley/ laan)

Page 345

**CRITERIA REQUIRING RESAMPLING** For example, define optimal _K_ in terms of 1) performance of cluster result **as classifier** (Dudoit, Frydland, 2002),

   - 2) **variability** of clusters,

- 3) **statistical significance** of distance between clusters.

- **DIRECT CRITERIAS** For example,

   - 1) **average silhouette** ,

   - 2) **average of cluster specific homogeneities** .

Page 346

#### **STATISTICAL INFERENCE WITH MICROARRAY DATA**

Mark J. van der Laan UC Berkeley, Biostatistics Fred Hutchinson Cancer Institute March 31, 2000 Based on joint paper with Jennifer Bryan.

Page 347

#### **<u>NUMERICAL SUMMARY OF ONE MICROARRAY EXPERIMENT</u>**

Each microarray experiment yields a list _X_ of _p_ ratios representing the relative gene-expression profile.

**TERMINOLOGY:** . _Xj >_ 1: gene _j_ is overexpressed . _Xj <_ 1: gene _j_ is underexpressed . _Xj̸_ = 1: gene _j_ is differentially expressed

Page 348

#### **<u>PARTICULAR TYPE OF EXPERIMENT</u>**

**EXPERIMENT:** Randomly sample (e.g. colon, breast) cancer patients and for each patient

- Extract healthy and cancerous tissue.

- Carry out a microarray experiment to obtain the list of _p_ ratios representing the relative gene-expression profile of cancerous versus healthy tissue for the _p_ genes.

Denote this list of ratios with **X** . Let _Y_ be the list of truncated log-ratios.

DATA SET: Our complete data set consists of _n_ (samplesize) observations _Y_ 1 _, . . . , Yn_ of _Y_ .

**REMARK:** Sample size _n_ (e.g.100) is much smaller than number of genes _p_ (e.g. 100,000)

Page 349

#### **SOME** **<u>QUESTIONS</u> ASKED**

- What subset of the _p_ genes cause cancer in an significant proportion of subjects, or at least are drug development targets?

- What groups of genes are dancing together.

- For the important findings, what is the probability that I can reproduce these findings?

- What sample size do I need?

Page 350

#### **<u>SUBSET PARAMETERS</u>**

Let _≡ EY µ_ Σ _≡ E_ �( _Y − µ_ )( _Y − µ_ )<sup>_⊤_�</sup> = CORRELATION MATRIX OF Σ. _ρ_ Let ( _µ,_ Σ) _→_ **S** ( _µ,_ Σ) _∈{_ 0 _,_ 1 _, . . . , K}_<sup>_p_</sup> be a “subset rule” of interest.

<u>DIFFFERENTIAL EXPRESSION RULES:</u> Given user supplied

Page 351


<!-- Start of picture text -->
δ 1 , δ 2<br>=<br>S ( µ ) {j :  µj > δ 1 }<br>=<br>S ( µ ) {j : max( µj, −µj )  > δ 1 }<br>=<br>S ( µ,  Σ) {j :  µj > δ 1  − q 0 . 7 σj}<br><!-- End of picture text -->

Page 352

#### <u>CLUSTERING RULES:</u>

Given user supplied _δ_ 1 _, δ_ 2

**STEP 1:** Apply _simple rule_ to start with: e.g. Select all _δ_ 1-differentially expressed genes.

**STEP 2:** Compute _distance matrix d_ = ( _dij_ : _i, j_ ) for remaining genes, using distance

_dij_ = 1 _−| ρij | ._

Provide distance matrix to cluster program “Partitioning around Medoids” (PAM, Kaufman and Rousseeuw, 1990). This defines the clusters by the medoids and assigns a cluster-membership to each gene.

**STEP 3:** _Thin out_ the clusters by deleting genes with links (or silhouette) weaker than _δ_ 2. This also deletes False Positives.

#### <u>SUPERVISED CLUSTERING</u>

Find genes highly correlated with known master genes.

Page 353

#### **<u>ESTIMATION AND CONSISTENCY</u>**

Let ( _µn,_ Σ _n, ρn_ ) be the empirical counterparts of ( _µ,_ Σ _, ρ_ ). We estimate _S_ ( _µ,_ Σ) with _S_ ( _µn,_ Σ _n_ ). [Consistency] Let _p_ = _p_ ( _n_ ) be such that _n/_ log( _p_ ( _n_ )) _→∞_ as _n →∞_ and _M < ∞_ . As _n →∞_ , then

sup _|µn,j − µj| →_ 0 in probability _j_ and sup _|_ Σ _n,ij −_ Σ _ij| →_ 0 in probability. _ij_ This implies _P_ ( _S_ ( _µn,_ Σ _n_ ) = _S_ ( _µ,_ Σ)) _→_ 1 if _n →∞_ and _n/_ log( _p_ ( _n_ )) _→∞_ .

Page 354

#### **<u>WHAT SAMPLE SIZE DO I NEED?</u>**

Let _n_<sup>_∗_</sup> be the sample size needed to make sure that with probability 0.95 the observed average expression level of EACH gene is within a DISTANCE _ϵ_ of the TRUTH.

We can derive a closed form lower bound for this sample size in terms of maximal noise level, number of genes, wished precision _ϵ_ .

It depends on the number of genes only through the logarithm of the number of genes!

Similarly, for the correlation matrix.

Thus data mining and fishing expeditions are allowed, just adjust sample size slightly

Page 355

Put here the two sample size slides!

Page 356

#### **<u>NONP. SAMPLE SIZE FORMULA</u>**


With this formula we can compute the sample size for which the probability that “low-differentially expressed genes make it into _S_ ( _µn,_ Σ _n_ )” is smaller than _δ_ = 0 _._ 05.

Page 357

For example, (log(3) _−_ log(2) = 0 _._ 41)

= _n_<sup>_∗_</sup> (100000 _, ϵ_ = 0 _._ 41 _,_ 0 _._ 1 _,_ 2 _,_ 0 _._ 5) 133 = _n_<sup>_∗_</sup> (5000 _, ϵ_ = 0 _._ 1 _,_ 0 _._ 1 _,_ 2 _,_ 0 _._ 5) 1304 = _n_<sup>_∗_</sup> (5000 _, ϵ_ = 0 _._ 5 _,_ 0 _._ 1 _,_ 2 _,_ 0 _._ 5) 77 = _n_<sup>_∗_</sup> (5000 _, ϵ_ = 0 _._ 5 _,_ 0 _._ 01 _,_ 2 _,_ 0 _._ 5) 92 = _n_<sup>_∗_</sup> (5000 _, ϵ_ = 1 _._ 0 _,_ 0 _._ 05 _,_ 2 _,_ 0 _._ 5) 28

Page 358

#### **<u>SIMULATION FOR UNIFORM DIFFERENCES</u>**

Noise Level: Suppose that all genes are independent with standard deviation _σ_ = 0 _._ 5. Sample size: Suppose that we have 150 subjects.

||10|1000|10000|100000|
|---|---|---|---|---|
|Max.Diff.Means|0.08|0.14|0.16|0.18|
|0.9-Quant|0.09|0.16|0.18|0.19|
|Max.Diff.Stdev|0.06|0.10|0.12|0.13|
|0.9-Quant|0.08|0.11|0.13|0.14|


Page 359


<!-- Start of picture text -->
p =10 p =100 p =1000<br>Max.Diff.Cor 0.2 0.31 0.39<br>0.9-Quant 0.23 0.33 0.41<br>If we set n  = 200 , p  = 1000, then DIFCOR=0.34.<br>If we set n  = 1000 , p  = 1000, then DIFCOR=0.15.<br><!-- End of picture text -->

Page 360


<!-- Start of picture text -->
Suppose now that the true correlations between M independent<br>pairs of variables is 0 . 8.<br>10 1000 10000 100000<br>Max.Diff.Cor 0.07 0.15 0.18 0.22<br>0.9-Quant 0.09 0.16 0.2 0.24<br><!-- End of picture text -->

Page 361

Remark that in subset rule we only apply clustering and thus look at correlations for genes which make first cut of. e.g. 300 genes. Since _mun_ is independent of Σ _n_ this is fine. So for knowing how good our correlation matrices for the clusters are we only have to set _p_ = 300.

Page 362

#### **<u>PARTITIONING AROUND MEDOIDS</u>**

- Define a distance matrix for the elements (genes or subjects)to be clustered: e.g. for genes we use correlation or absolute correlation distance.

- Provide distance matrix to cluster program “Partitioning around Medoids” (PAM, Kaufman and Rousseeuw, 1990) and specify number of clusters.

This finds data adaptively the best centers (medoids) of the clusters and assigns a cluster-membership to each element.

- For each element it computes a silhouette measuring how strong it belongs to its cluster.

- Number of clusters is obtained by minimizing average silhouette.

Page 363

put here ALL, AML clustering subjects plots

Page 364

#### **<u>HOW RELIABLE???</u>**

How reliable is the observed structure or observed subset and clusters?

Examples of observed features: 4 genes in the same cluster. Gene has correlation larger than 0.5 with a master gene. Gene is more than 3-fold differentially expressed.

For example, if we repeat the experiment, how _likely_ is it that one can reproduce the findings?

<u>BOOTSTRAP:</u> Simulate an approximation of the experiment many times and find out!

Page 365

#### **<u>CONFIDENCE-LEVEL PARAMETERS OF INTEREST</u>**

Possible parameters of the distribution of _S_<sup>�</sup> _≡_ **S** ( _µn,_ Σ _n_ ) are: **Feature Probabilities:**

Consider an observed feature: e.g. 1) gene _j_ is in the subset estimate. 2) genes _i, j_ were both in the subset estimate. 3) genes _i, j_ were both in the subset estimate and in the same cluster. We can define the corresponding feature probability:

_pj,n_ = _P_ ( _S_<sup>�</sup> _j >_ 0) = _Pij,n P_ ( _S_<sup>�</sup> _i >_ 0 _, S_<sup>�</sup> _j >_ 0) = _Qij,n P_ ( _S_<sup>�</sup> _i_ = _S_<sup>�</sup> _j >_ 0)

RESULT: If _n →∞_ , then these probabilities converge uniformly to the features of the true subset _S_ = **S** ( _µ,_ Σ), even when _p_ = _∞_ .

Page 366

**Performance measures:** “Sensitivity” and “Positive Predictive Value” of _S_<sup>�</sup> :


The distribution of the proportion of “Extreme False Positives” which make it into the subset estimate. **Uniform Distances.** 0.95-quantiles of

Maxdif.mean = max _| µnj − µj | j_ Maxdif.cor = max _| ρn,ij − ρij | . ij_

Page 367

#### **<u>PARAMETRIC BOOTSTRAP</u>**

**RESAMPLING:** We estimate distribution of _S_<sup>�</sup> by resampling from an estimated distribution of the true data generating distribution. Since _S_<sup>�</sup> only depends on the mean and covariance matrix, we want to resample data with the (asymptotically) the right mean and right covariance matrix (and we want NO TIES). **RESAMPLE FROM A MULTIVARIATE NORMAL DISTRIBUTION:**

- Resample _n_ observations _Y_ 1<sup>#</sup><sup>_, . . . , Y_</sup> _n_<sup>#of</sup><sup>_Y_#</sup><sup>_∼Np_(</sup><sup>_µn,_Σ</sup><sup>_n_).</sup> Construct estimate **S** ( _µ_<sup>#</sup> _n_<sup>_,_Σ#</sup> _n_<sup>).</sup>

- Repeat: Obtain _B_ i.i.d observations of **S** ( _µ_<sup>#</sup> _n_<sup>_,_Σ#</sup> _n_<sup>).</sup>

- Computate relevant parameters of this empirical distribution of **S** ( _µ_<sup>#</sup> _n_<sup>_,_Σ#</sup> _n_<sup>).</sup>

Page 368

#### **ASYMPTOTIC VALIDITY:**

Nonparametrically, if _n/_ log( _p_ ( _n_ )) _→∞_ and _M < ∞_ , we have that 1) the bootstrap estimate of the distribution of<sup>_√_</sup> _<u>n</u>_ <u>(</u> _µn − µ_ ) is consistent and 2) _S_ ( _µ_<sup>#</sup> _n_<sup>_,_Σ#</sup> _n_<sup>)convergestothedegeneratedistributionat</sup><sup>_S_(</sup><sup>_µ,_Σ).</sup> Thus the estimated feature probabilities converge to the true features: e.g. _p_<sup>#</sup> _j,n_<sup>_→I_(</sup><sup>_j∈S_).</sup>

Page 369

#### **<u>SIMULATING THE NULL DISTRIBUTION</u>**

To make sure that observed structures are not due to pure noise, one simulates from a multivariate normal distribution with either **1:** No differential expression and no correlations or **2:** No differential expression and observed covariance matrix.

Page 370

#### **<u>SIMULATION STUDY</u>**

SAMPLE SIZE: 60. NUMBER OF GENES: 1500 TRUE COVARIANCE MATRIX: block diagonal with three blocks of correlated genes. SUBSET RULE: PAM-based subset rule with three clusters applied to _δ_ 1-differentially expressed genes. We required sufficiently small distance between medoid or any previously included gene: see table. TRUE SUBSET: Apply subset rule to true ( _µ,_ Σ). TRUE FEATURE PROBABILITIES: _pj_ are the proportion of times gene _j_ falls in subset estimate in the actual simulation. TRUE SENSITIVITY, PPV etc: Similar.

Page 371

SIMULATION: 1) Sample 60 subjects from true distribution. 2) Do the parametric bootstrap (200 resamples) to obtain estimates of the feature probabilities _pj,n_ and other quantaties of interest. 3) repeat 1) and 2) 200 times.


<!-- Start of picture text -->
Mean Correlation<br>Cutoff Cutoff<br>|µj| >  log 2 . 7  ≈ 0 . 99 |ρij| >  0 . 5<br>|S| avg |S � | avg |S �# |<br>30 26.9 26.61<br><!-- End of picture text -->

Page 372


<!-- Start of picture text -->
p = 1500, n = 60 True Bootstrap<br>Sensitivity 0.73 0.78<br>Predictive Value 0.82 0.79<br>Prop. of Ext. False Pos. 0.00 0.00<br>Any Ext. False Pos. 0.00 0.00<br>Expected Lgst. Abs. Dev. 0.46 0.46<br><!-- End of picture text -->

Page 373

we need the table with _pj_ probabilities. show clustering subjects ALL, AML, show probability plot for 9 clusters and show one of cluster plots.

Page 374

---

[← Multivariate Statistical Methods in Genomics](01-multivariate-statistical-methods-in-genomics.md) · [Up: contents](index.md)
