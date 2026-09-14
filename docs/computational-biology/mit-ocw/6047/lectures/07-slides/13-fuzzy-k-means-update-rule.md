---
title: Fuzzy K-means update rule
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fuzzy K-means update rule

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Re-assign** each point **x** i **Update** center **μ** k to the **weighted** to **<u>all</u>** centers, **<u>weighted by distance</u> mean** of the points assigned to it: _b b_  For each point calculate the _n_   **x x x μ** _k_ ( 1)  i P( **μ** _k_ | i )  P( **μ** _k_ | i ) probability of membership x with label ji x with label ji for each category K:

Regular K-Means is a special case of fuzzy k-means where:  1 if **x** i is closest to **μ** _k_ P(label K | **x** i, **μ** _k_ )  0 **otherwise**  19

P(label K | **x** i, **μ** _k_ )

###### **Today: Gene Expression Clustering & Classification**

###### **1. Introduction to gene expression analysis**

   - Technology: microarrays vs. RNAseq. Resulting data matrices

   - Supervised (Clustering) vs. unsupervised (classification) learning

**2. K-means clustering (clustering by partitioning)**

   - Algorithmic formulation: Update rule, optimality criterion. Fuzzy k-means.

   - Machine learning formulation: Generative models, Expectation Maximization.

**3. Hierarchical Clustering (clustering by agglomeration)**

   - Basic algorithm, Distance measures. Evaluating clustering results

**4. Naïve Bayes classification (generative approach to classification)** – Discriminant function: class priors, and class-conditional distributions

   - Training and testing, Combine mult features, Classification in practice

**5. (optional) Support Vector Machines (discriminative approach)** – SVM formulation, Margin maximization, Finding the support vectors

   - Non-linear discrimination, Kernel functions, SVMs in practice

20

## K-Means as a Generative Model


<!-- Start of picture text -->
Model of P(X,Labels)  Observations<br>Generate<br>m 2<br>x i<br>Estimate<br>m 1<br><!-- End of picture text -->


<!-- Start of picture text -->
Samples drawn from normal distributions<br>with unit variance - a  Gaussian Mixture Model<br>2<br>  <br>1   x i u j  <br> <br>P  x i | u j  exp  <br>2  2<br> <br> <br><!-- End of picture text -->

**Given only samples, how do we estimate max lik model params: (1) centroid definitions, (2) point assignments?**

21

###### **EM solution: iteratively estimate one from the other**

E step: If centers are known  Estimate memberships M step: If assignments known  Compute centroids


<!-- Start of picture text -->
Max lik  Labeled<br>m 2?<br>M<br>centers  points<br>x i<br>m 1 ?  Labels?<br>Known  Assign<br>E<br>centers  points<br>Choose μk and labels that maximize P(data|model)<br><!-- End of picture text -->

**Solution is exactly the k-means algorithm!**

22

###### M step: assignments known  compute centroids

m **2? Max lik Labeled x** i **centers**<sup>**M**</sup> m **1 ? points** **_Choose μk and labels that maximize P(data|model)_**    1 2  1     arg max log   P  **x** _i_ | **μ**  arg max    **x** _i_ **u**   log   **μ**  i  **μ** _i_  2  2   **Seeking the max likelihood estimate of the cluster mean** 2 **Solution is the**   arg min  <mark></mark> **x** _i_ **u** <mark></mark> **centroid of the xi μ** _i_

**Equivalent**

**EM solution**

###### **K-means solution**

23

#### E step: centers known  Estimate memberships


<!-- Start of picture text -->
m 2?<br>x i<br>m 1 ?  Known  E  Assign<br>centers  points<br><!-- End of picture text -->

###### **_Choose μk and labels that maximize P(data|model)_**

2 1  <u></u> **x** _i_  **u** _k_ <u></u>  2     arg max Pk  **x** _i_ | **μ** _i_  arg max exp   arg min <mark></mark> **x** _i_ **u** _k_ <mark></mark> k k 2  2 k     **Seeking the label k that Solution is the maximizes likelihood of point nearest center**

**Solution is the nearest center**


**Equivalent**

**EM solution**

**K-means solution**

24

###### **Algorithmic vs. machine learning formulations**

||**K-m**|**eans**|**Fuzzy K**|**-means**|
|---|---|---|---|---|
||algorithmic<br>formulation|probabilistic<br>interpretation|algorithmic<br>formulation|probabilistic<br>interpretation|
|**Initialization**|Initialize K<br>centers**μ**k|Initialize model<br>parameters|Initialize K<br>centers**μ**k|Initialize model<br>parameters|
|**E-step:**<br>Estimate prob<br>of hidden labels<br>(point<br>assignments to<br>classes)|Assign**x**ilabel<br>ofnearest<br>center<br>distance<br><br><br>2<br>,_i k_<br>_i_<br>_k_<br>_d_<br><br><br>**x**<br>**μ**|Estimatemost<br>likely missing<br>labelgiven<br>previous<br>parameters|Calculate<br>probability of<br>membershipfor<br>each point to<br>each class<br>i<br>P(label K|<br>,<br>)<br>_k_<br>**x μ**|Estimate<br>probability over<br>missing labels<br>given previous<br>parameters|
|**M-step:**Update<br>params to max<br>likelihood<br>estimates given<br>assignments|Move**μ**kto<br>centroidof all<br>points with that<br>label|Choose new<br>max likelihood<br>params given<br>points in label|Move**μ**kto<br>weighted<br>centroidof all<br>points, each<br>weighted by<br>P(label)|Choose new<br>params to<br>maximize<br>expected<br>likelihoodgiven<br>label estimates|
|**Iteration**|Iterate|Iterate|Iterate|Iterate|


###### **<mark>P(x|Model)</mark>** **_<mark>guaranteed</mark>_** **<mark>to increase each iteration of EM algo</mark>**

25

#### **EM is much more general than fuzzy K-means**

**σblue>σgreen**

**Original Data**

**K-means solution**

**Full EM model**

**K-means solution** Cluster sizes **Uniform** priors Spread of points **Unit** distance function Cluster shape **Symmetric** Label K-means: Pick **max** assignment Fuzzy: Full **density**

**EM generalization** Class priors **_P(_** _classi_ **_<u>)</u>_** _Gaussian (μi,_ **_σi_** _<u>)</u>_


EM: Full **density** Gibbs: **sample** <u>posterior 26</u>

#### **Three options for assigning points, and their parallels across K-means, HMMs, Motifs**

|**ate rule**|**Update**<br>**assignments**<br>**(E step)**|**Algorit**<br>**in eac**<br>|**hm implementi**<br>**h of the three**<br>|**ng E step**<br>**settings **<br>|**Update**<br>**model**<br>**parameters**|
|---|---|---|---|---|---|
|**Upd**|**Estimate hidden**<br>**labels**|**Expression**<br>**clustering**|**HMM**<br>**learning**|**Motif**<br>**discovery**|**(M step)**<br>**max**<br>|
|The|hidden label is:|Cluster labels|State path π|Motif positions|**likelihood**|
|Pick a best|Assign each point<br>to best label|**K-means:**<br>Assign each<br>point to nearest<br>cluster|**Viterbi**<br>**training:**label<br>sequence with<br>best path|**Greedy:**Find<br>best motif match<br>in each sequence|Average of<br>those points<br>assigned to<br>label|
|Average all|Assign each point<br>to all labels,<br>probabilistically|**Fuzzy K-**<br>**means:**Assign<br>to all clusters,<br>weighted by<br>proximity|**Baum-Welch**<br>**training:**label<br>sequence w all<br>paths (posterior<br>decoding)|**MEME:**Use all<br>positions as a<br>motif occurrence<br>weighed by motif<br>match score|Average of all<br>points,<br>weighted by<br>membership|
|Sample one|Pick one label at<br>random, based on<br>their relative<br>probability|**N/A:**Assign to<br>a random<br>cluster, sample<br>by proximity|**N/A:**Sample a<br>single label for<br>each position,<br>according to<br>posteriorprob.|**Gibbs sampling:**<br>Use one position<br>for the motif, by<br>sampling from the<br>match scores|Average of<br>those points<br>assigned to<br>label(a<br>sample)|


27

###### **Today: Gene Expression Clustering & Classification**

###### **1. Introduction to gene expression analysis**

   - Technology: microarrays vs. RNAseq. Resulting data matrices

   - Supervised (Clustering) vs. unsupervised (classification) learning

**2. K-means clustering (clustering by partitioning)**

   - Algorithmic formulation: Update rule, optimality criterion. Fuzzy k-means.

   - Machine learning formulation: Generative models, Expectation Maximization.

**3. Hierarchical Clustering (clustering by agglomeration)**

   - Basic algorithm, Distance measures. Evaluating clustering results

**4. Naïve Bayes classification (generative approach to classification)** – Discriminant function: class priors, and class-conditional distributions

   - Training and testing, Combine mult features, Classification in practice

**5. (optional) Support Vector Machines (discriminative approach)** – SVM formulation, Margin maximization, Finding the support vectors – Non-linear discrimination, Kernel functions, SVMs in practice

28

### **Challenge of K-means: picking K**

- How do we select K?

   - We can always make clusters “more compact” by increasing K

   - e.g. What happens is if K=number of data points?

   - What is a meaningful improvement?

- Hierarchical clustering side-steps this issue

29

---

[← K-means Optimality Criterion](12-k-means-optimality-criterion.md) · [Up: contents](index.md) · [Hierarchical clustering →](14-hierarchical-clustering.md)
