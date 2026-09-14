---
title: A PROCESS TIME MODEL FOR TRAJECTORY INFERENCE AND RNA VELOCITY
source: https://thesis.library.caltech.edu/17389/
source_file: sources/fang-2025-biophysical-normalisation/Thesis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A PROCESS TIME MODEL FOR TRAJECTORY INFERENCE AND RNA VELOCITY

**Source:** `Thesis.pdf` from [fang-2025-biophysical-normalisation](https://thesis.library.caltech.edu/17389/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Fang, Meichen, Gennady Gorin, and Lior Pachter (2025). “Trajectory inference from single-cell genomics data with a process time model”. In: _PLoS Comput. Biol._ 21.1, e1012752. doi: `10.1371/journal.pcbi.1012752` .

## **4.1 Introduction**

Single-cell RNA sequencing (scRNA-seq) has provided unprecedented insights into biological dynamical processes in which cells display a continuous spectrum of states that go beyond the confines of discrete cell types (Griffiths, Scialdone, and Marioni, 2018). Cells appear to be inherently desynchronized in cellular processes and scRNA-seq can potentially capture cells at different positions over the process even if samples are collected at only one time point. The concept of pseudotime has been developed to describe the position of a cell along the underlying process (Trapnell et al., 2014), and trajectory inference (or pseudotemporal ordering) methods aim to solve the inverse problem of inferring the latent pseudotime variable from scRNAseq data. In light of this this concept, hundreds of methods have been developed (Cannoodt, Saelens, and Saeys, 2016; Saelens et al., 2019; Deconinck et al., 2021; Cao et al., 2019; X. Qiu et al., 2017; Wolf, Hamey, et al., 2019; Street et al., 2018; Campbell and Yau, 2016; C. Lin and Bar-Joseph, 2019; Campbell and Yau, 2019; Du et al., 2024). However, with a few exceptions that explicitly model gene expression dynamics (C. Lin and Bar-Joseph, 2019; Campbell and Yau, 2019; Du et al., 2024), trajectory inference methods mostly treat pseudotime as a descriptive concept relying on more or less arbitrary distance metrics in gene expression space. Specifically, there is no well-defined, agreed-upon meaning underlying the notion of pseudotime, and its interpretation is primarily accomplished through qualitative visuals and low dimensional embeddings.

While a descriptive approach can be powerful in exploratory data analysis, the absence of a well-posed definition for a trajectory renders model interpretation and assessment challenging, even conceptually. Firstly, assessing the credibility of results is hard, as fitting can be performed on any dataset and we have limited metrics and ground truth available to gauge the fit quality. Secondly, the interpretation of

48

the inferred trajectory is not straightforward, and downstream analysis based on pseudotime is employed to understand the underlying gene dynamics. However, this need for following analysis to interpret results gives rise to the problem of circularity (Section 2), which becomes evident in the context of an inflated false positive rate in the problem of detecting differentially expressed (DE) genes along pseudotime. The problem of circularity is conceptually challenging and can only be effectively remedied under restrictive assumptions (Neufeld et al., 2023). To illustrate these two points, we applied the procedure of trajectory inference and DE analysis on simulations generated from four clusters and were able to “discover” superficially plausible dynamics (Figure 4.1). As naive an example as it is, it reflects the fact that we do not have a reliable way to determine the validity of trajectory inference results. Though both are false positives, there is a subtle difference between the falsely inferred trajectory (Figure 4.1b) and the inflated false positive rate in DE analysis resulting from circularity (Figure 4.1c): the first one arises when a trajectory model is inferred from cluster data without proper assessment, while circularity stems from the double use of data for fitting and testing (double dipping) (Kriegeskorte et al., 2009). Conversely, adopting a model-based approach has the potential to mitigate this problem. With a clearly defined model of gene expression along a trajectory, the interpretation of parameters and the characterization of errors becomes more straightforward. First of all, model assessment can be conducted in a more principled manner. We can effectively address the first kind of false positive using conceptually simpler approaches, such as comparing our model to cluster models to identify the correct model. In addition, the specific question of interest like finding DE genes can be incorporated directly into the formulation of the model, rendering ad hoc analysis unnecessary. For example, if we have an probabilistic model of trajectories with transcription kinetics parameters, we can directly select DE genes using inferred parameters, without the need to go through the circular process of fitting trajectories and performing DE analysis to find interesting genes. However, we emphasize that the exact p-values still cannot be easily calculated, and circularity persists if we fit trajectories and perform DE test based on the inferred time, which still falls under the issue of double dipping.

Recently, equipped with a kinetic model of RNA dynamics, RNA velocity has emerged as another powerful concept to provide complementary information about dynamic processes (La Manno et al., 2018). By distinguishing unspliced and spliced mRNA counts as derived from unique molecular identifiers (UMIs) and fitting gene-wise parameters under an on-off model of transcription, it is able to

49


<!-- Start of picture text -->
a Negative control data b Pseudotemporal ordering c DE analysis along pseudotime<br>(4 Poisson mixtures  (slingshot) (tradeseq)<br>with read depth noise)<br>False topology DE gene hallucination<br>Lineage 2 Lineage 1<br>Unspliced<br>Spliced<br>Pseudotime along lineage 1<br>Genes<br>Gene 1 counts<br>Cells<br><!-- End of picture text -->

Figure 4.1: **False positive on clusters data** . **a)** Negative control data are simulated from 4 Poisson mixtures with read depth noise. **b)** As an example of false positive, specious trajectory in lower dimensional space was constructed with Slingshot (Street et al., 2018). **c)** Differential genes along pseudotime were selected with tradeSeq (Van den Berge et al., 2020), with the first gene plotted along the blue lineage.

predict the direction of future spliced counts changes. Although a time-dependent gene expression model was explicitly defined in RNA velocity, the time did not have any associated interpretation. Moreover, earlier methods often modeled genes separately with gene-wise times and fit these models after applying a series of ad hoc transformations to count data, which added excessive flexibility and hindered a clear interpretation of the time. As the velocities of different genes had non-comparable scales, they needed to be combined heuristically in a lower-dimensional space to calculate a velocity for a cell (Gorin, Fang, et al., 2022). A natural extension is to integrate the cell-wise time of trajectory inference with the mRNA dynamical model of RNA velocity, which a few methods have successfully implemented with different underlying transcription models (Aivazidis et al., 2023; Gu, Blaauw, and Welch, 2022; Li et al., 2022). Moreover, the recent _VeloCycle_ developed an RNA velocity model for the cell cycle that models unspliced and spliced counts dynamics directly with harmonic functions (Lederer et al., 2024).

However, despite the implicit pseudotime modeling performed by some of the RNA velocity methods, there remain many challenges in attaching a physical meaning to pseudotime. Do the parameters of the trajectory model have underlying biophysical interpretations? How can we guarantee that our inferences align with our intended objectives? Are the assumptions of trajectory models satisfied to maintain the consistency of our inference? For instance, the application of trajectory inference or RNA velocity methods relies on the assumption of continuous dynamics in the data, which is not examined retrospectively. Though some heuristic scores

50

purport to distinguish between cluster-like data and trajectory-like data (Lim and P. Qiu, 2024), there is no principled approach to determine whether the data is sufficiently dynamical and whether a cluster or trajectory model is more appropriate, and the decision of applying trajectory analysis often hinges on prior knowledge and assumptions about the data.

In summary, to attach real meaning to “pseudotime” requires more than just a definition of cell-wise pseudotime. It necessitates a principled approach to statistics to ensure a meaningful inference, which is still lacking in the field of trajectory inference. Meticulous model assessment is required to ensure its relevance to the underlying biological processes and the reliability of results, which includes examining the identifiability of the model, characterizing performance to identify both ideal and failure scenarios, and establishing proper metrics for result falsification. Then pseudotime starts to have a physical meaning, which we suggest defining as “process time” to underscore its interpretation with respect to a specific cellular process.

The physical interpretation of process time is related to, but not necessarily equivalent to, physical time. Specifically, assuming that all cells share the same dynamic process, we can select a specific point along this process to serve as the starting point for all cells. At the physical sampling time, the process time denotes the relative time to that starting point, indicating how long ago in physical time the cells were at the starting point. Therefore, if the experiments establish a known starting time for when the cells enter the process, the process time should correspond to the relative physical time. On the other hand, if we could follow one cell over time, the process time would evolve in sync with physical time. In reality, where only different cells can be sampled at multiple time points, the distribution of process time should ideally evolve in parallel with physical time, provided enough cells are sampled from the same population.

Here, we build such a model and infer “process time” in a principled way with Chronocell. To strike a balance between expressiveness and identifiability, we proposed a trajectory model built on cell states (Gorin, Fang, et al., 2022). On the one hand, we incorporated different cell states so that our trajectory model is expressive enough to capture the observation that cells are generally assumed to transition through various states during development. On the other hand, we assume a constant transcription rate for each state to keep the model as simple as possible. By introducing simplifying assumptions in transcription and sequencing model, we ensure

51

model identifiability. We consider the influence of technical aspects and directly incorporate them into the distribution of counts, which eliminates the necessity for unjustified heuristic preprocessing steps that lead to unclear interpretation and biased results even in the large data and no noise limit (Gorin, Fang, et al., 2022). We undertook simulations to characterize estimation accuracy in the different parameter regimes to identify ideal and failure scenarios. Using simulations for which ground truth is known allowed us to characterize how large uncertainty and inconsistent parameter values serve as good indicators of potential unreliability in failure scenarios, which can be assessed even when ground truth is unavailable. Finally, we applied Chronocell to biological datasets. We assessed its appropriateness on different datasets and identified unsuitable ones. For suitable datasets, Chronocell revealed distinct cellular distributions over process time and yielded mRNA degradation rate estimates congruous with those obtained from mRNA metabolic labeling.

## **4.2 Challenges with the pseudotime concept Trajectory methods overview**

Single-cell genomics trajectory inference methods have mostly relied on similarity metrics: distance based methods reconstruct the trajectory based on some distance metrics in gene expression space under the assumption that cells that are more similar in gene expression space are also closer in pseudotime (Haghverdi et al., 2016; Wolf, Hamey, et al., 2019; Trapnell et al., 2014). Manifold-learning based methods draw the trajectories in a reduced dimension space based on connectivity, i.e., similarity (Campbell and Yau, 2016; Street et al., 2018). Probability/Markov chain based methods also calculate transition probabilities based on distances (Setty et al., 2019). However, pseudotime based on similarity/distance is inherently descriptive and unable to be extended to reflect physical meaning, because state spaces of dynamical processes are not isotropic. There are a few exceptions that implicitly define generative models of single-cell RNA-seq (scRNA-seq) data with pseudotime, modeling dynamics of gene expression along differentiation processes in a way that can be reformulated as driven by cell states switching models (C. Lin and Bar-Joseph, 2019). These ideas have motivated our model.

One important observation is that the usage of Markov Chain model in trajectory inference, as well as other single cell analysis, can be fundamentally flawed. This is because frequently cells are samples drawn from different chains, instead of a sequence of observations of one single chain. The Markov chain formalism is therefore not applicable to single cell studies without making further assumptions.

52

## **Circularity in pseudotime-based analysis**

Due to the exploratory nature of trajectory inference, all variables are used to fit the model, but not all variables are informative. Specifically, it is natural to assume sparsity and focus on a few "marker genes" in downstream analysis. At present, a multi-stage method is commonly employed for pseudotime-based analysis. In the initial stage, trajectory and pseudotime are fitted, followed by the second stage, where hypothesis testing is utilized to select genes that are variable along trajectories.

Ideally, with a predefined and well-parameterized model, we can construct confidence intervals for parameters using Bayesian methods or the bootstrap. However, interpretation can be difficult even for PCA loadings (Cadima and Jolliffe, 1995). As heuristic methods become more popular, the variable selection problem is highly entangled with model construction, and the question of how to perform valid inference is not straightforward. Current methods usually first perform trajectory inference, and then test whether genes expression have dependency with pseudotime using the same dataset. It is well-known that such tests are not valid and can lead to inflated false positive rates (Campbell and Yau, 2016; Lähnemann et al., 2020; Z. Ji and H. Ji, 2016; Tritschler et al., 2019). The same issue for clustering has also been well discussed in several recent studies (Zhang, Kamath, and Tse, 2019; Gao, Bien, and D. Witten, 2020; Chen and D. M. Witten, 2022). Here we briefly summarize the issue in the context of trajectory inference.

First, fitting and testing using the same dataset means that one has cherry-picked the most significant association and results are consequently biased upward, which is known as post-selection inference (Taylor and Tibshirani, 2015; Kuchibhotla, Kolassa, and Kuffner, 2022). Furthermore, even if one uses separate datasets for fitting and testing, there is an inherent circularity in the hypothesis testing. Specifically, during trajectory inference, one selects a transformation (that defines a trajectory) _𝑓_<sup>ˆ</sup> that maps a cell to a pseudotime based on its gene expression. Then, by testing whether genes expression associates with pseudotime, one is asking whether _𝑥_ associates with _𝑓_<sup>ˆ</sup> ( _𝑥_ ), which just echoes the model fitted and does not perform the hypothesis testing validly.

## **PCA as an example**

To see this circularity, consider a single component model where trajectory is replace by the first component of PCA. Denote the data by _𝑋_ , and let Y be the normalized _𝑋𝑖_ _<u>𝑗</u>_ − _𝑋_<sup>¯</sup> _<u>𝑗</u>_ data matrix, i.e. _𝑌𝑖𝑗_ = _𝑋𝑖𝑗_ − _𝑋_<sup>¯</sup> _𝑗_ for covariance PCA and _𝑌𝑖𝑗_ = ~~√~~ <u>�</u> _𝑖_<sup>(</sup><sup>_𝑋_</sup> _𝑖𝑗_<sup>−</sup><sup>_𝑋_¯</sup> _𝑗_<sup>)2for</sup>

53

correlation PCA. Write _𝑆_ = _𝑛_ <u>1</u><sup>_𝑌𝑇𝑌_=</sup><sup>_𝑉_Λ</sup><sup>_𝑉𝑇_anddenotethefirsteigenvectorin</sup> PCA by _𝑣_ (first column of V) and first eigenvalue by _𝜆_ . Then for first principal component scores, which are the latent variable _𝑧_ we want, we have _𝑧_ = _𝑌𝑣_ and _𝑛_ <u>1</u><sup>_𝑦𝑇_</sup> _𝑗_<sup>_𝑧_=</sup> _𝑛_<sup><u>1</u></sup><sup>_𝑦𝑇_</sup> _𝑗_<sup>_𝑌𝑣_=</sup> _𝑛_<sup><u>1</u>(</sup><sup>_𝑌𝑇𝑌𝑣_)</sup><sup>_𝑗_=</sup><sup>_𝜆𝑣𝑗_.If we directly perform linear regression of</sup><sup>_𝑧_on</sup> the expression of mean-centered gene _𝑦 𝑗_ , the slope is _𝑣 𝑗_ .

Even after data splitting, if we follow the normal linear regression procedure and test the null hypothesis that _𝛽_ = 0, we will derive a t-statistic that is still biased. The correct way is to account for the projection _𝑧_ = _𝑌𝑣_ and test _𝛽_ = _𝑣 𝑗_ .

## **Current solutions**

In practice, there are only a few papers that have taken this circularity into account. One possible solution is count splitting if counts number are high enough ( **Neufeld2023-lh** ). Another possible solution is data splitting, where we split the dataset into two parts, select our model using the first part and do the inference using the second. Specifically, to perform rigorous hypothesis testing and get some valid p-value, we can perform permutation test. However, it means that we need to generate sets of permuted data and perform the whole procedure of trajectory inference and DE analysis on each set. This approach does not seem to have been explored or adopted in any currently used tools.

More crucially, this kind of pseudotime-based analysis only answers data analytic questions, i.e., data summary and analysis. They are typically not concerned with goodness of fit/model selection, thus providing no information about the correctness of the fitted model.

## **4.3 Results**

## **A trajectory model generalizing cellular states**

We begin by defining the trajectory as a dynamical process underlying all cells, with potentially different lineages/branches within this process. Cells are then assumed to be sampled from various, unobserved, time points along this process. Thus, the latent variable _𝑧_ = ( _𝑡, 𝑙_ ) is introduced to account for such heterogeneity due to process time ( _𝑡_ ) and lineage ( _𝑙_ ), and _𝑧_ follows a sampling distribution determined by the specific biological system and experimental conditions. Consequently, the probability distribution of the data we obtain is a mixture of cells over time and lineage,


54

where **x** is the data and _𝜃_ is the set of parameters that define the trajectory. This is the common framework of trajectory inference, and developing a trajectory model requires defining the gene dynamics along the lineage and the process time _𝑃_ ( **x** | **z** _, 𝜃_ ), as well as the sampling distribution of cells over the process _𝑃_ ( **z** ).


<!-- Start of picture text -->
Chronocell<br>Input Model Inference Results<br>(lineages as paths in directed graph)Trajectory structure  0 𝝉 0 1 𝝉 1 𝜶 22  𝝉 2 Lineage 1 𝐴Expression model(t)Transcription rate𝜶 0  𝜶 2  z = (lineage, time)PosteriorsCell 1 E step ParametersGene 1(α,β,γ) Posteriors Probability<br>𝜶 0  𝜶 1  3 𝝉 2 Lineage 2 𝜶 1  𝜶 3<br>𝜶 3  𝜏0 𝜏1 𝜏2 t z z<br>Sampling assumption(prior for latent variable z) + Transcription𝐴(t) Splicingβ Degradationγ Cell 2 Gene 2<br>Gene Unspliced mRNA Spliced mRNA z z Parameters log1p<br>Bernoulli sampling M step<br>𝜏0 𝜏1 𝜏2 Unspliced counts Spliced counts Cell n Gene p<br>Process time<br>scRNA-seq data Genes Genes z z<br>Measurement model<br>… …<br>Cells Cells<br><!-- End of picture text -->

Figure 4.2: **Chronocell overview** . The **input** of Chronocell comprises three components: 1) the _trajectory structure_ , which outlines the states each lineage traverses as paths on a directed graph; 2) the _sampling assumption_ , which defines the prior distribution of latent variables, namely lineages and process time, with a default uniform distribution over both; and 3) the _scRNA-seq data_ , consisting of unspliced and spliced count matrices. The Chronocell **model** consists of a _expression model_ with piecewise-constant transcription rates, and a Bernoulli _measurement model_ . Each state _𝑠_ is associated with a transcription rate _𝛼𝑠_ for each gene, as well as an exit time _𝜏𝑘_ denoting the switching time to the next state, where k is the index for the time segment. The EM algorithm is used for **inference** , with each iteration alternating between E-steps and M-steps. The **results** of Chronocell primarily include the estimated parameters and posterior distributions over latent variables for each cell.

To define the dynamical process, we first state our transcription model. We consider only transcription, splicing, and degradation reactions in cells, and assume only transcription rates are time-dependent (Figure 4.2 Gene expression):


where _𝐴𝑙_ ( _𝑡_ ) is the transcription rate function for lineage _𝑙_ at time t, and _𝛽_ and _𝛾_ are the splicing, and degradation rates. The chemical master equation describing the evolving distribution of the above biochemical reaction network has an analytical solution (Jahnke and Huisinga, 2007). If we assume the initial distribution to be Poisson, the solution remains Poisson with the means ( _𝜆𝑢_ and _𝜆𝑠_ ) of _𝑈_ and _𝑆_ evolving according to the following ordinary differential equations (ODEs) of RNA velocity:

55


The modeling of transcription rate _𝐴𝑙_ ( _𝑡_ ) is motivated by the common abstraction of cellular differentiation as cell state transitions: each lineage is abstracted as a series of switches in cellular states over time. The series of switches are specified by the given trajectory structure, which includes a directed graph of cell states where each lineage corresponds to a path (Figure 4.2 Input Structure). We introduce one transcription rate per gene for each cellular state ( _𝛼_ ). Switching is assumed to be instantaneous and occurs at an unknown but fixed time ( _𝜏_ ) with the first switch leaving initial state 0 to occur at _𝜏_ 0. Without loss of generality, we consider the entire process to start at time 0 ( _𝜏_ 0=0) and have a time length of 1 (e.g. _𝜏_ 2=1 in Figure 4.2). Consequently, the transcription rate function _𝐴𝑙_ ( _𝑡_ ) of lineage l is simplified as piecewise constant functions of the process time over [0 _,_ 1] (Figure 4.2 Model). This piecewise constant function is defined in the limiting regime where transcriptional state switching (such as expression of master regulatory factors and changes of chromatin state) precedes gene expression and has a much faster time scale. Thus, the piecewise constant function serves as a reasonable approximation when the time scale of transcription rate changes is comparable to or larger than the mRNA half-life. It also directly reduces to discrete cell clusters in the fast dynamic limit, i.e., when dynamical timescale (<sup><u>1</u></sup> _𝛽_<sup>and</sup> _𝛾_<sup><u>1</u>)ismuchsmallerthansampling</sup> intervals, for example, the total time length divided by cell number, _𝑛_ , under a uniform sampling distribution. This connection to cluster models enables us to interpolate between discrete cell states and continuous dynamics.

The simple form of the transcription rate function lead to a tractable model and facilitates inference and analysis. In fact, it affords explicit solutions for the distribution and for its derivatives with respect to parameters. Ideally, gene regulatory networks involved in cell differentiation would be modeled, but with current (transcriptomic) data types it is difficult to include gene interactions and to model transcription rates as (protein-mediated) functions of other genes with accuracy. Thus, we assume that the dynamics of different genes are independent and that all correlations are absorbed into the shared latent process time. Additionally, for simplicity, we can assume all genes are fully synchronized, as in the synchronized model, where _𝜏_ is the same for all genes. However, the desynchronized model, which allows for

56

different _𝜏_ values for each gene, is also available. In summary, our trajectory model is suitable for capturing the coordinated global gene expression changes instead of the detailed gene dynamics.

After deriving an explicit distribution of _in vivo_ counts, we turn to the measurement model. We assume simple binomial sampling of each molecule, and that the average binomial sampling probability, i.e., read depth, varies between cells but remains the same for all molecules in one cell. Then, in vitro counts remain Poisson but with means adjusted by read depth. Instead of using normalized data, we estimated read depth using the total UMI counts of near-Poissonian genes that are not used for the inference, and incorporated it into the count distribution. Therefore, we arrive at an analytical form of the conditional probabilistic distributions _𝑃_ ( **x** | **z** _, 𝜃_ ) of counts from a dynamic process by specifying the trajectory structure, gene expression model, transcription rate functions, and scRNA-seq measurement model.

The remaining part of specifying the sampling distribution _𝑃_ ( **z** ) is crucial, because it breaks the scale invariance of parameters and ensures the identifiability of the model: multiplying the transcription, splicing and degradation rates by the same constant leads to the same marginal likelihood if the sampling distribution can be changed. Ideally, the specification of the sampling distribution depends on our knowledge of the studied biological system and the experimental design. For example, for stem cells that constantly divide and differentiate, we may assume a uniform sampling distribution over (0 _,_ 1] with a point mass on time 0, where the point mass represents the fraction of time that cells spend in the initial proliferative state. On the other hand, for time series data, we may assume the sampling distribution of cells were centered around their captured time points with some variances. However, in practice, since there is no obvious principled way to determine such distributions, we just assume a uniform sampling distribution over process times ( _𝑡>_ 0) by default, but the weight on time point 0 and different lineages can be identifiable and be updated in the inference.

A trajectory is thus defined with the above dynamical process and sampling distributions. With the parameterized form of the probabilistic distribution of counts, we can employ the Expectation-Maximization (EM) algorithm to estimate model parameters and posterior distributions of process times and cell lineages by maximizing Evidence Lower Bound (ELBO) with either warm start or random initialization (Section Inference). The synchronized model was used by default, where all genes share the same _𝜏_ . Since fitting the desynchronized model from scratch is more

57

challenging, it is recommended to begin the fitting process using the results from the synchronized model. For desynchronized models, we also introduce a penalty term proportional to the squared difference between gene-wise _𝜏𝑘_ and the global _𝜏𝑘_ to encourage synchronization, and the coefficient for this penalty term is set as a parameter, with a default value of 0. We tested the EM algorithm and inference on simulations generated from our trajectory model (Section Simulations). Both the synchronized and desynchronized models are identifiable, and the parameters can be recovered accurately under reasonable conditions (Figures 4.3 and 4.4). We will elaborate on these conditions in Section 3.4 “Identifying failure scenarios reveals the fragility of inference.”


<!-- Start of picture text -->
a<br>Trajectory structures in simulations<br>Structure 1 Structure 2<br>2<br>0 1 2 0 1<br>3<br>b<br>Estimation errors<br>Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean<br>mean<br>gene<br>y=0.1<br>Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>c<br>Errors vs true value<br>Structure 1<br>α0  error α1 error α2 error β error γ error<br>gene<br>Structure 2<br>α0  error α1 error α2 error α3 error β error γ error<br>gene<br><!-- End of picture text -->

Figure 4.3: **Inference accuracy of synchronized model** . **a** ) The two trajectory structures used in simulations. **b** ) Estimation errors of different parameter sets. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in Section 4.4. **c** ) Absolute errors with respect to the true values of parameters.

By having an explicitly parameterized distribution of raw counts, we can easily

58


<!-- Start of picture text -->
a Estimation errors<br>Structure 1<br>Time error α0  error α1 error α2 error τ0  error τ1  error β error γ error<br>mean mean<br>y=0.1 gene<br>Structure 2<br>Time error α0  error α1 error α2 error α3 error τ0  error τ1  error β error γ error<br>mean mean<br>y=0.1 gene<br>b<br>Errors vs true value<br>Structure 1<br>α0  error α1 error α2 error τ0  error τ1  error β error γ error<br>gene<br>Structure 2<br>α0  error α1 error α2 error α3 error τ0  error τ1  error β error γ error<br>gene<br><!-- End of picture text -->

Figure 4.4: **Inference accuracy of desynchronized model** . Estimation errors of the desynchronized model tested on simulations with trajectory structures in Figure 4.3a. **a** ) Errors of different parameter sets. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in Section 4.4. **b** ) Absolute errors with respect to the true values of parameters.

interpret results and systematically assess the model under a more principled framework. Since parameters all have biophysical meanings, we cannot only directly interpret them but also validate their accuracy by comparing them to orthogonal experiments that measure the same parameters. Furthermore, we can directly select DE genes by fold changes in transcription rates across states, after filtering genes by goodness of fit ((see Section 4.5 “Gene selection”). The performance can be quantified through parameter errors, aiding in the identification of both confident and uncertain scenarios.

Not only are the parameters and results more interpretable, but we can also compare different models systematically. Regarding false positives from clustered data, we can evaluate when a trajectory model is no longer appropriate by comparing it to a cluster model using standard model selection methods like AIC (Figure 4.5). Importantly, the posterior distributions and multiple minima of AIC scores can hint at the lack of continuity (Figure 4.5), serving as a retrospective metric when model selection methods are compromised by unaccounted noise. We also demonstrate

59

model selection on a disconnected trajectory, which includes both a single cluster and a bifurcation (Figure 4.6). Our representation of the trajectory structure as paths on a directed graph naturally includes this scenario. We compare the results of the true model with those of a cluster model and a connected structure. AIC and BIC can correctly identify the true structure when compared to the two incorrect models (Figure 4.6).


<!-- Start of picture text -->
a b<br>Negative control data Model selection<br>(4 Poisson mixtures  Trajectory AIC of 20 simulations<br>with read depth noise)<br>2 (the lower the better)<br>0 1 Trajectory model<br>is better<br>3<br>vs<br>Unspliced<br>Poisson mixture<br>Spliced model is better<br>Poisson  Trajectory<br>Genes mixtures<br>Poisson  mixtures<br>Cells<br><!-- End of picture text -->

Figure 4.5: **Inference and model selection on clusters data** . **a)** The same data from 4 Poisson mixtures as in Figure 4.1. **b)** To compare the trajectory and Poisson mixture models, AIC scores of Poisson mixtures model and trajectory model are compared on 20 simulations with different random parameter sets. Dots below y=x indicate Poisson mixture model is better.

## **Demonstrating performance of Chronocell on ground-truth simulations**

Since the true trajectory structure may differ from both our prior knowledge and the initial structure used, we first demonstrate the inference pipeline under a slightly incorrect trajectory. The inferred parameters provide insights into the true structure, and we then apply model selection to identify the correct model. Additionally, we include non-variable genes to assess the performance of the differential expression (DE) procedure.

We used a two-lineage trajectory and uniformly sampled 10,000 cells over lineages and process times with biological plausible parameters extracted from literature (Rabani et al., 2011) (Section Simulations). 100 out of 200 genes are variable (Figure 4.7a). We fit under a slightly wrong assumption of the trajectory structures and assumed all genes are variable (Figure 4.7b). For random initialization, we initialized randomly 100 times and picked the one with highest ELBO score (Figure 4.7c). We also fit with warm start by initiating the fitting process from correct cell clusters grouped by true time and lineages. Both types of initialization were able to converge to the ELBO with true parameters, and random initialization yielded a

60


<!-- Start of picture text -->
a Disconnected data  b Posterior distributions<br>(30000 cells, 200 genes)<br>True structure Cells from bifurcation Cells from cluster<br>𝝉 2 Transcription rate Densities<br>0 𝝉 0 1 𝝉 1 𝜶 22  Bifurcation 𝑎(t) 𝜶 0  𝜶 2  0 𝜏̂1=0.5 1 Densities<br>𝜶 0  𝜶 1  3 𝝉 2 𝜶 1  𝜶 3<br>4 𝜶 3 Cluster 𝜏0=0 𝜏1=0.5 𝜏2=1𝜶 4  t 0 𝜏̂1=0.5 Process time1 0 𝜏̂1=0.5 1 0 Process time𝜏̂1=0.5 1<br>c Inferred and true parameters<br>α0 α1 α2 α3                                      α3 β γ<br>d Model selection<br>True structure Wrong structures AIC/BIC values of different models<br>Disconnected 5 Clusters Connected<br>2 2 2<br>0 1 0 1 0 1 3<br>3 3<br>4 4 4<br>Model 0 Model 1 Model 2<br>Model 0 Model 1 Model 2<br>✓<br>true time<br>Cells ordered by<br>Inferred values<br><!-- End of picture text -->

Figure 4.6: **Inference and model selection on disconnected data** . **a)** The ground truth trajectory structure. A subset of cells is from a bifurcation trajectory and the other cells are from a disjoint cluster. For the bifurcation trajectory, cells start from the state 0 and jump to the state 1 at _𝜏_ 0 = 0, and then bifurcate into two lineages with different ending states (2 and 3) at _𝜏_ 1 = 0 _._ 5. The process ends at _𝜏_ 2 = 1. **b)** Heatmaps of the inferred posterior distributions for cells from both the bifurcation and the cluster. x-axis is time grids, and y-axis is cells aligned by their true times and grouped by their true lineages. The intensity of color indicates the weights of posterior distributions of cells on the grids. Heatmap of cells from _𝜏_ 0 to _𝜏_ 1 use a purple color palette. Heatmap of cells from _𝜏_ 1 to _𝜏_ 2 of first lineage use blue, and those of second lineage use red. Heatmap of cells from cluster use an orange color palette. RMSE stands for root mean square errors. **c)** Inferred parameters values compared to true values. Error is mean normalized error across genes as described in Section 4.4. **d)** AIC and BIC of the true model and two wrong models.

slightly higher ELBO compared to warm start, with a negligible difference (Figure 4.7d). For the following analysis, we used the fitting results of random initialization. The posterior distributions correctly recapitulate the time and lineages of cells, with a root mean squared error (RMSE) around 0.05 for the posterior mean of process time in comparison to the true time (Figure 4.7e). This means that the error in time of a cell is around 5% of the total time length of the trajectory in average. However, the error is not completely uniform: as cells in the second interval are closer to the steady state, they have more spread posteriors and larger errors. Since the

61

posteriors of each cell are accurate, the posteriors averaged over cells also resemble the empirical distribution of the true time (Figure 4.7f).

The parameters are also recovered accurately (Figure 4.7g). For variable genes, all parameters are identifiable, while for non-variable genes, only _𝛼_ and the ratio of _𝛽_ to _𝛾_ are identifiable. We noticed a trend that the absolute errors of _𝛼_ scale with the square root of true values, while for _𝛽_ and _𝛾_ , they scale with the true values (Figure 4.8a). This trend also appeared in other simulations (Figure 4.3b and 4.3c). Therefore, to calculate the errors of parameters, we divide the absolute error of _𝛼_ by the square root of true values and _𝛽, 𝛾_ by true values, so that errors of different genes are more comparable. We refer to them as normalized errors in the text. The parameter _𝛼_ tends to be estimated with higher accuracy compared to _𝛽_ and _𝛾_ (Figure 4.7g). This aligns with intuition because, although parameters are identifiable in our trajectory model, the Evidence Lower Bound (ELBO) is nevertheless insensitive to proportional changes in _𝛽_ and _𝛾_ , which have minimal impact on the phase portrait in the unspliced and spliced space of each gene. To confirm this, we used the true model to calculate the Fisher information matrix and the smallest eigenvalues of each gene (Figure 4.8b). The corresponding eigenvectors describe the flattest direction of the ELBO. To validate that the flattest direction primarily lies in the _𝛽_ and _𝛾_ parameters, we add the corresponding eigenvectors to the true parameters after normalizing it by the square root of eigenvalues, and calculate the new ELBO with the modified parameters. Indeed the resultant changes in ELBO are indeed small and _𝛽_ and _𝛾_ values were mainly varied (Figure 4.8c), which confirms that the _𝛽_ and _𝛾_ are harder to estimate accurately (Figure 4.7g).

To select genes whose dynamics are well-fit by the model, we evaluate their goodness of fit by comparing the gene-wise likelihood with that of clustering models (Section Gene selection). We adopt this relative likelihood criterion because absolute likelihoods of different genes are not directly comparable and clusters model serves as a natural reference point for comparison to filter genes without continuous dynamics. All 91 genes selected belong to the variable class (Figure 4.7h). The similar transcription rates of states 1 and 2 of selected genes would also suggest us that those two states could be merged into a single one, if we didn’t know the true structure (Figure 4.7i). Therefore, we applied model selection methods to compare the ground truth model and the assumed model. We generate another 20 parameter sets, fit under both models, and compute in-sample ELBO scores (ELBO), AIC, BIC, and out-of-sample ELBO scores (test ELBO). The ELBO is always better in

62


<!-- Start of picture text -->
a True structure b Assumed structure c ELBO scores vs correlation d ELBO scores<br>𝛼00 𝛼1𝜏11 𝛼232 𝛼&0 0  𝛼&11 𝜏̂1 𝛼&2𝜏̂2 2 34𝛼&3 initializationrandom<br>α 𝛼3 100 variable  𝐴(t) 𝛼&4 warm start<br>genes<br>100 non variable<br>𝜏0=0 𝜏1=0.67 𝜏2=1 t genes 0 𝜏̂1 𝜏̂2 1 t Correlation of mean  Iterations<br>process time and true time<br>e f g Variable genes<br>Posterior distributions Averaged posterior distributions α0  α1  α2  α3 α4 β γ<br>Densities<br>Non variable genes<br>0 𝜏̂1 𝜏̂2 1 α0  α1  α2  α3 α4 β/γ<br>Process time<br>0 𝜏̂1 𝜏̂2 1 0 𝜏̂1 𝜏̂2 1<br>Process time True values<br>h Genes selection i Selected genes j Model selection<br>Total genes = 200 Selected Unselected Model A 2 Chosen model<br>0 1<br>Variable  91 9 3<br>variableNon  0 100 Model B<br>α0  α1 α2  α3 α4 3<br>0 1 2<br>4 Model A Model B<br>Values Values<br>True  states<br>true time Density<br>Cells ordered by  Inferred values<br>log1p( inferred values) Frequency<br><!-- End of picture text -->

Figure 4.7: **Demonstration of inference on simulation** . **a)** The ground truth trajectory structure. Cells jump to the next state (2) from starting state (1) at _𝜏_ 0 = 0, and then bifurcate into two lineages with different ending states (3 and 4) at _𝜏_ 1. The process ends at _𝜏_ 2 = 1. Out of 200 total genes, 100 genes are non variable with the same distributions along time. **b)** The falsely assumed structure that does not know the first two states are supposed to be merged into one. All genes are assumed to vary along time. **c)** The ELBO scores of 100 random initializations (blue dots) compared to those of warm start (red line). The x-axis is the Pearson’s correlation between the mean process time of each random initialization and the true time. **d)** ELBO scores over fitting iterations of both warm start (red line) and the best random initialization (blue line), with the ELBO calculated with true parameters (gray line) as reference. **e)** Heatmaps of inferred posterior distributions. x-axis is time grids, and y-axis is cells aligned by their true times with true transcription states on the left. The intensity of color indicates the weights of posterior distributions of cells on the grids. Heatmap of cells from _𝜏_ 0 to _𝜏_ 1 use a gray color palette. Heatmap of cells from _𝜏_ 1 to _𝜏_ 2 use purple color palette. Heatmap of cells from _𝜏_ 2 to _𝜏_ 3 of first lineage use blue, and those of second lineage use red. RMSE stands for root mean square errors. **f)** The averaged posterior distributions across cells (dark blue) and true empirical distribution (gray) of process time. **g)** Inferred parameters values compared to true values. For non variable genes, only<sup>_<u>𝛽</u>_</sup> _𝛾_<sup>are identifiable and compared.Error is mean</sup> normalized error as described in the text, and the mean is computed across genes. **h)** The confusion matrix for gene selection. **i)** _𝛼_ values of selected genes over states. **j)** Two models and the distribution of the chosen one by (train) ELBO, AIC, BIC, and test ELBO, calculated on 20 samples each with a different set of parameter.

63


<!-- Start of picture text -->
a<br>Variable genes<br>α0  α1 α2  α3  α4 β γ<br>Non variable genes<br>α0 α1 α2  α3  α4 β/ γ<br>True values<br>b<br>Distribution of smallest eigenvalues<br>Variable genes Non variable genes<br>log (eigenvalues) log (eigenvalues)<br>c<br>Perturbing true parameters with eigenvectors of the smallest eigenvalues<br>i ii<br>ELBO True parameters  vs True parameters + normalized eigenvectors<br>α0 α1  α2  α3 α4 β             γ<br>True parameters  vs True parameters – normalized eigenvectors<br>α0 α1  α2  α3 α4 β             γ<br>True values<br>Absolute error<br>Frequency<br>Varied values<br><!-- End of picture text -->

Figure 4.8: **Supplementary figures for demonstration of inference on simulation** . **a** ) Absolute errors with respect to the true values of parameters. **b** ) Distribution of the smallest eigenvalues of the Fisher information matrix of each gene. **c** ) Marginal likelihood (ELBO) and varied parameters compared to true parameters. The difference between varied parameters and true parameters are the eigenvectors corresponding to the smallest eigenvalues of the Fisher information matrix, divided by the square root of the respective eigenvalues, specific to variable genes.

model B due to overfitting. All of the last three metrics (AIC, BIC, and test ELBO) favor the true model most of the time (90%) (Figure 4.7j). However, we want to emphasize that model selection worked because simulations were strictly generated under our trajectory model. In reality, if true transcription rates are far away from piece-wise constant functions, the resulting deterministic noise can introduce bias in AIC/BIC and cross-validation, leading them to prefer more complex models (Abu-Mostafa, Magdon-Ismail, and H.-T. Lin, 2012).

64

## **Identifying failure scenarios reveals the fragility of inference**

Given the accuracy on perfect data, we sought to characterize the impact of different factors on inference accuracy and identify potential failure scenarios that could lead to unreliable results. We first study the requirements on some obvious factors like the number of cells, the number of genes, and the means of counts. Relatively small numbers of cells and genes appear to be sufficient (Figures 4.9 and 4.10). As the number of cells increases, parameter errors decrease, while time errors remain the same. On the other hand, time errors decrease with an increasing number of genes while parameter errors remain the same. Additionally, counts means must be sufficiently high to enable accurate inference, which necessitates adequate sequencing depth (Figure 4.11). We notice that when the trajectory structure becomes more complex, the requirement for count means also increases: Chronocell needs higher means for similar accuracy (Figure 4.12). Furthermore, when count means are low, increasing the number of cells can actually compromise the accuracy, underscoring the critical importance of obtaining sufficient counts.


<!-- Start of picture text -->
a<br>Impact of cell numbers on inference accuracy<br>Structure 1<br>i<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>ii Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>b<br>Running time<br>(100 genes, 100 epochs on one core)<br><!-- End of picture text -->

Figure 4.9: **Impact of cell numbers on inference accuracy and running time** . **a** ) Estimation errors for datasets with varying cell numbers. The trajectory structures are the same as in Figure 4.3a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in the Section 4.4. Estimation errors of different cell numbers. **b** ) Running time of 100 epochs on a single core on datasets with varying cell numbers.

65


<!-- Start of picture text -->
Impact of gene numbers on inference accuracy<br>a Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>b Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br><!-- End of picture text -->

Figure 4.10: **Impact of gene numbers on inference accuracy** . The trajectory structures are the same as in Figure 4.3a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in the Section 4.4. **a** ) Results for trajectory structure 1. **b** ) Results for trajectory structure 2.


<!-- Start of picture text -->
Impact of mean counts on inference accuracy<br>Structure 1<br>a<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>b Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br><!-- End of picture text -->

Figure 4.11: **Impact of mean counts on inference accuracy** . Simulations of different counts mean are generated by scaling the transcription rates while keeping other parameters the same. The trajectory structures are the same as in Figure 4.3a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in the Section 4.4. **a** ) Results for trajectory structure 1. **b** ) Results for trajectory structure 2.

As we use piecewise-constant functions to approximate transcription rates, we also test how this simplification impacts results when transcription rates are, in fact, not piecewise-constant. We generate simulations using piecewise-exponential functions for transcription rates, which ranges from almost linear to almost piecewise as the rate constants increase. We fit the model with Chronocell under the piecewiseconstant assumption, and the inference accuracy remains satisfactory when the rate constants are comparable to or larger than the mRNA half-life (Figure 4.13).

66


<!-- Start of picture text -->
a Trajectory structure 3<br>2<br>1<br>0<br>4<br>3<br>5<br>b Impact of counts mean on inference accuracy<br>Time error α0  error α1 error α2 error α3 error α4 error α5 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>α ~ lognormal(μ=2,σ=1) α ~ lognormal(μ=3,σ=1)<br>c Estimation errors of 10 random parameter sets<br>(30000 cells)<br>α ~ lognormal(μ=2,σ=1)<br>Time error α0  error α1 error α2 error α3 error α4 error α5 error β error γ error<br>mean mean<br>y=0.1 gene<br>α ~ lognormal(μ=3,σ=1)<br>Time error α0  error α1 error α2 error α3 error α4 error α5 error β error γ error<br>mean mean<br>y=0.1 gene<br>d Impact of cell numbers on inference accuracy<br>(100 genes)<br>α ~ lognormal(μ=2,σ=1)<br>Time error α0  error α1 error α2 error α3 error α4 error α5 error β error γ error<br>mean mean<br>y=0.1 gene<br>α ~ lognormal(μ=3,σ=1)<br>Time error α0  error α1 error α2 error α3 error α4 error α5 error β error γ error<br>mean mean<br>y=0.1 gene<br><!-- End of picture text -->

Figure 4.12: **Impact of trajectory structure complexity on inference accuracy** . **a** ) The trajectory structure used in this figure. **b** ) Impact of counts means on inference accuracy. Datasets with increasing counts means are generated by increasing the mean parameters _𝜇_ in log-normal distributions for _𝛼_ . **c** ) Results on 10 random parameter sets with different distributions for _𝛼_ . **d** ) Impact of cell numbers on inference accuracy on simulations with different distributions for _𝛼_ .

As unaccounted noise is prevalent in scRNA-seq datasets, we then characterize the effects of noise on inference. The first type of noise is cell-wise read depth (or cell size) that influences all genes similarly. The inference is sensitive to such noise: when read depth variance is not correctly accounted for in the fitting, inference results may be highly inaccurate when its squared coefficient of variation (CV<sup>2</sup> ) exceeds 0.1 (Figure 4.14a). As the CV<sup>2</sup> typically observed in real datasets exceeds 0.1 (Figure 4.19), an accurate estimate of cellwise read depth is critical. Considering this fact, instead of simply using total counts as normalization factors, we use normalized

67


<!-- Start of picture text -->
a Exponential functions with different rate constants<br>b Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>c Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>d Structure 3<br>Time error α0  error α1 error α2 error α3 error α4 error α5 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br><!-- End of picture text -->

Figure 4.13: **Impact of non piecewise-constant transcription rate functions on inference accuracy** . Simulations are generated using piecewise-exponential functions for transcription rates and fitted under Chronocell’s piecewise-constant assumption. The three trajectory structures have been defined in Figure 4.3a and Figure 4.12a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in the Section 4.4. **a** ) One piece of the piecewiseexponential functions used for transcription rates. Different rate constants are used in the simulation to span the range from an almost linear transition to an almost step function. **b** ) Results for trajectory structure 1. **c** ) Results for trajectory structure 2. **d** ) Results for trajectory structure 3.

covariance between genes to decompose extrinsic noise (influencing all genes) and intrinsic noise (gene specific). We estimate the read depth CV<sup>2</sup> across cells from the normalized covariance between genes. Subsequently based on the read depth CV<sup>2</sup> , we subtract the extrinsic variance caused by the read depth from total variance and identify Poissonian genes whose remaining variances (intrinsic variances) are close to their means (variance _<_ 1.2 mean). We then estimate cell-wise read depth using the sum of those Poissonian genes. Different sets of genes are used for estimating the CV<sup>2</sup> of read depth and fitting trajectories. In reality, these read depth estimates correlate well with total counts number for most datasets, with one interesting exception (Figure 4.19).

On the other hand, gene specific noise seems to have less impact on inference. We added gene-wise gamma noise in simulation which generates negative binomial distributions in steady states and approximates bursting noise. Parameter errors

68


<!-- Start of picture text -->
a<br>Impact of read depth noise on inference accuracy<br>i Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>ii Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>b<br>Impact of gene-wise Gamma noise on inference accuracy<br>i Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>ii Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>c d<br>Model selection on clusters with gene-wise Gamma noise  Model selection of trajectory structure with gene-wise Gamma noise<br>Data Model comparison Data Model comparison<br>Clusters + Gamma noise Cluster AIC<br>(the lower the better) True structure Model A<br>2<br>𝜏1 2 0 1<br>0 vs 1 2 𝛼00 𝛼11 𝛼3𝛼23 Model B 3 3<br>3 Cluster 0 1 2 Model A Model B<br>Trajectory 4<br>Trajectory Frequency<br><!-- End of picture text -->

Figure 4.14: **Impact of noise on inference accuracy and model selection** . The trajectory structures are the same as in Figure 4.3a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in the Section 4.4. **a** ) Estimation errors as read depth noise increases. **b** ) Estimation errors as gene-wise Gamma noise increases. **c** ) Impact of gene-wise Gamma noise on model selection on clusters data. Same as in Figure 2 except Gamma noise with CV<sup>2</sup> 1 was added to Poisson mixtures to generate simulation data (Figure tion 4.4). **d** ) Impact of gene-wise Gamma noise on model selection of trajectory structure. Same as in Figure 3j except Gamma noise with CV 1 was added in simulation.

gradually increase as CV<sup>2</sup> of Gamma noise increases but remain reasonably small even with a CV<sup>2</sup> of 1 (Figure 4.14b). However, while it may not completely undermine the fitting process, it can lead to failures in model selection. When repeating the model selection procedures in Figs 4.5 and 4.7 after introducing Gamma noise, the AIC/BIC and cross-validation metrics favor the wrong models that were more complex than the true one (Figure 4.14c and 4.14d). This highlights the importance of providing reasonable trajectory structure to the fitting based on

69

prior knowledge, and exploring alternative methods for quality control against false positives caused by clusters.

Another probable factor in real datasets that can lead to suboptimal results is insufficient dynamics. Intuitively, for a dynamical model to be appropriately fitted, the data must capture a significant amount of transient dynamics to recapitulate the evolving processes over time, without which the data start to resemble discrete clusters. Such cases can occur in at least two possible scenarios: fast timescales and concentrated sampling distributions, both of which result in clusters in the extreme. Therefore, false positives caused by clusters are naturally included as a component of identifying unreliable results.

The first situation, fast timescales, arises when mRNA half-lives are significantly shorter than the timescale of biological processes, and thus cells are mostly near steady state and provide little information about the intermediate dynamics. By setting the length of the time interval to unity and increasing _𝛽_ and _𝛾_ , which is equivalent to increasing processes timescale with unchanged mRNA half-lives, we found that ideally, the mean value of _𝛾_ should not fall out of the range of 1 to 10, and the mean ratio of _𝛾_ to _𝛽_ over genes should not be too small (Figure 4.15). Hence, if the average half-life of spliced mRNA is approximately 30 minutes (Rabani et al., 2011), snapshot data sampled from processes involving steps exceeding 10 hours are no longer suitable.

Furthermore, given an appropriate timescale, the sampling distribution still has to cover the region where the transient dynamics occur. Imagine, for example, that all cells are from one unknown time point; there is no way for a trajectory to be inferred. Instead, a cluster should be used to fit the data. Thus, it is crucial to determine the minimum level of uniformity required in the sampling distribution and verify whether this requirement is met. By gradually changing sampling distributions from a uniform distribution to a Gaussian with a random mean, we generate datasets with sampling distributions that exhibit decreasing levels of uniformity, which was quantified using entropy (Figure 4.16a). As the sampling distribution deviates from uniformity, the errors of process time and parameters quickly increase as expected (Figure 4.16b). In fact, even when the sampling distribution is not far away from a uniform one with entropy 4, the errors are big enough that the results are completely wrong (Figure 4.16b). Further, even using the true sampling distribution as a prior for a warm start with correct initialized time cannot mitigate the lack of dynamics: the errors in parameter estimations remained substantial (Figure 4.16c). Therefore,

70


<!-- Start of picture text -->
a<br>i<br>Increasing β and γ proportionally<br>S S cell<br>U U state 1<br>S state 2<br>S U S<br>U U<br>β larger<br>ii Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>iii Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>b<br>i<br>Increasing β and γ inverse proportionally<br>S S cell<br>U U state 1<br>S state 2<br>S U S<br>U U<br>β larger<br>ii Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>iii Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.1 gene<br>trial<br>larger<br>γ<br>larger<br>γ<br><!-- End of picture text -->

Figure 4.15: **Impact of dynamic timescale on inference accuracy** . The trajectory structures are the same as in Figure 4.3a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in the Section 4.4. **a** ) **i** Schematics of phase plots with increasing timescale. **ii** Estimation errors as time scale increases. **b** ) **i** Schematics of phase plots with the ratio of _𝛾_ to _𝛽_ increasing while keeping their product constant. **ii** Estimation errors as<sup>_<u>𝛾</u>_</sup> _𝛽_<sup>increases.</sup>

sufficiently transient dynamics is an inherent requirement for trajectory inference even when perfect prior information is provided.

71


<!-- Start of picture text -->
a<br>Sampling distribution Entropy of sampling distribution<br>Uniform Gaussian Structure 1 Structure 2<br>Process time Process time Process time<br>b<br>Random initialization under uniform prior<br>Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.15 gene<br>trial<br>Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.15 gene<br>trial<br>c<br>Warm start with correct time and lineage under true prior<br>Structure 1<br>Time error α0  error α1 error α2 error β error γ error<br>mean mean<br>y=0.15 gene<br>trial<br>Structure 2<br>Time error α0  error α1 error α2 error α3 error β error γ error<br>mean mean<br>y=0.15 gene<br>trial<br>Density Density Density<br><!-- End of picture text -->

Figure 4.16: **Impact of sampling distribution uniformity on inference accuracy** . The trajectory structures are the same as in Figure 4.3a. For time, error is root mean square error. For _𝛼, 𝛽, 𝛾_ , error is mean normalized error as described in Section 4.4. **a** ) Schematics of sampling distributions used in simulation with decreasing uniformity. The sampling distributions were gradually changing from uniform distribution to Gaussian distribution. Right plot shows the entropy of the sampling distributions. **b** ) Estimation errors as uniformity decreases under uniform prior. **c** ) Estimation errors as uniformity decreases warm started with correct position under true prior. Fitting was initialized with posteriors calculated under true parameters, and empirical distribution of process time of samples were provided as prior for the sampling distribution.

In summary, a suitable dataset for fitting process time needs to contain enough dynamic information as well as limited noise. This stringent requirement for a successful trajectory inference highlights the need for suitable datasets and careful model assessment. Straightforwardly, we could make a consistency check by verifying if the remaining noise, parameter values, and uniformity of the average posterior

72


<!-- Start of picture text -->
a c<br>Probable failure scenarios AIC vs Correlation in mean process time of 20 bootstrap samples<br>i Cluster i<br>Adding<br>Gamma  Increasing<br>noise noise<br>ii Fast timescale ii Correlation Correlation<br>S S cell<br>U U state 1 Increasing<br>S state 2 β and γ<br>S U S<br>U U Correlation Correlation<br>β larger<br>iii Concentrated sampling distribution iii<br>Uniform Gaussian Decreasinguniformity<br>Process time Process time Correlation Correlation<br>b<br>AIC vs correlation in mean process time of 100 random initializations<br>i<br>Increasin<br>g noise<br>better<br>Correlation Correlation<br>ii<br>Increasing<br>β and γ<br>better<br>Correlation Correlation<br>iii<br>Decreasing<br>uniformity<br>better<br>Correlation Correlation<br>larger<br>γ<br>Density Density<br>AIC<br>AIC<br>AIC<br><!-- End of picture text -->

Figure 4.17: **Uncertainty and lack of robustness as an indicator of failure scenarios** . **a** ) Schematics of three probable failure factors: clusters data, fast timescale, concentrated sampling distribution. Two example simulations were used for each case and the gray arrows indicate the their difference. **i** The two simulations are the cluster data in Figure 2 and noisy cluster data in Figure 4.14c respectively. **ii** The two simulations are the 5th and 13th instances of structure 1 in Figure 4.15b. **iii** The two simulations are the 1st and 11th instances of structure 2 in Figure 4.16b. **b)** AIC vs. correlation of mean process time of 100 random initializations in different scenarios. Results of two example simulations were showed. The x-axis is the correlation of mean process time between each initialization and the best one. The gray arrows correspond to those in **a** ). **c** ) AIC vs correlation of mean process time of 20 bootstrap samples in different scenarios. Results of the two example simulations were presented in the same position as in **b** ). The x-axis is the correlation of mean process time between each bootstrap sample and the original one (which is the best one in **b** ). The gray arrows correspond to those in **a** ).

73

distribution fall into the appropriate range determined in simulations. However, when a result is incorrect, it may not necessarily exhibit large unexplained noise, high splicing/degradation rates, or a concentrated cellular distribution over process time, as it could inadvertently fit undesired patterns and output plausible results. Thus, inconsistency is a sufficient but not necessary indicator of unreliable results.

It turns out that the large uncertainty of results can be a better indicator. As both noise and limited dynamics tend to diminish or obscure the difference of scores like ELBO between correct and incorrect outcomes, they introduce multiple comparable maxima and make the fitting results unstable. The resultant large uncertainty can be measured by two different approaches. First, as each random initialization outputs a different ELBO/AIC score and cell ordering, we can inspect the distribution of scores with respect to a summary parameter of cell orderings, which describes the global landscape of the score function. Ideal scenarios usually give one distinct maximum of ELBO (or minimum of AIC) at the correct ordering of cells (correlation around one), while failure scenarios usually lead to multiple comparable maxima of ELBO (or minima of AIC) at different cell orderings beside the correct one (Figure 4.17b). We use average precision (AP) of the 100 random initializations to quantify the distinctiveness of the correct outcomes and summarize the uncertainty. One random initialization is considered correct if its resultant mean process time correlates well with that of the best one, e.g., a Pearson’s correlation of 0.8 (Section Uncertainty assessment). Ideal cases lead to AP close to one and low AP indicates instability but not vice versa, which means low AP is a sufficient indicator for instability (Figure 4.17b). Second, the uncertainty can also be revealed by standard bootstrap analysis. We generated 100 sets of resampled data and computed the correlation in process time between the original and each resampled set (see Section 4.5 “Uncertainty assessment”). In failure scenarios the results of original data and resampled data often differ and correlations are scattered with large variance. On the other hand, in ideal scenarios, process time estimates of resampled results agree with the original one and correlations are centered around one (Figure 4.17c).

## **Uncovering distinct underlying cellular distributions in process time**

We applied Chronocell to a variety of datasets with different anticipated sampling distributions over time. For those datasets, we estimated read depth as described in Section Read depth estimation (Figure 4.19), and then filtered genes for fitting based on their means, variances and unspliced to spliced ratios (see Section 4.5 “Real datasets preprocessing”). The trajectory structures are determined based on

74

prior knowledge. Random initialization was always performed and its uncertainty was assessed by both AP and bootstrapping. Warm start was applied as well if cell type annotations were available, which were used to initialize the fitting process. The corresponding clusters (Poisson mixtures) model was fitted with the same read depth and used for comparison. The genes were selected based on goodness of fit, in the same manner as in the simulation (see Section 4.5 “Gene selection”). Then, DE genes are selected based on the fold changes in transcription rates across states.

We first tested our method on the T cells of PBMC (Peripheral Blood Mononuclear Cells) dataset from 10x Genomics, which is typically expected to exhibit a few distinct clusters (Figure 4.20a). Indeed, though the AIC of trajectory model is lower than clusters model likely due to unaccounted noise, the scores of 100 random initializations display multiple minima: multiple different cell orderings result in similar AIC values (Figure 4.20b). The low average precision (0.28) of random initializations suggests clusters model would be more suitable for PBMC. Serving as a negative control, it confirms our ability to reject unreliable results on real datasets, even when standard model selection methods are invalidated by incorrect modeling of noise.

The second dataset contains a snapshot collection of glutamatergic neuronal lineage cells in a developing human forebrain (Figure 4.21a) (La Manno et al., 2018), which is presumed to capture cells along a continuous trajectory. However, the unstable result of random initializations indicates its unreliability, as results with reversed directions yield comparable AIC scores (Figure 4.21b), resembling simulations that lack dynamics information (Figure 4.17b). This observation is further supported by examining the cellular posterior distributions obtained through warm start with cell type annotations, where the average posterior distribution reveals that cells are concentrated around starting time _𝜏_ 0, i.e., the initial state, with a low entropy (Figure 4.21c). Therefore, both the inconsistency indicated by the concentrated posterior and instability indicated by comparable peaks of AIC suggest this is not a suitable dataset for Chronocell and likely lacks enough dynamics.

The third dataset contains erythroid lineage cells during mouse gastrulation collected from multiple time points (Figure 4.22a) (Pijuan-Sala et al., 2019). Biological time availability offers a valuable means to evaluate results by comparing the posterior distributions of cells to their corresponding physical times, which is particularly useful since real snapshot datasets lack a definitive ground truth. The AIC scores of random initializations show a clear minimum at a correct direction that align

75

### **CV**<sup>**2**</sup> **-mean relationship**


<!-- Start of picture text -->
a Forebrain<br>b<br>Erythroid<br>c Cell cycle<br>d<br>Neuron<br>e PBMC<br><!-- End of picture text -->


Figure 4.18: _𝐶𝑉_<sup>2</sup> **-mean relationship of total, unspliced and spliced counts** . **a** ) Forebrain data. **b** ) Erythroid data. **c** ) Cell cycle data. **d** ) Neuron data. **e** ) PBMC data.

with cell type annotations (Figure 4.23a), and the average precision of random initializations is 0.79 which is notably higher than those of PBMC and Forebrain datasets (Figures 4.20b and 4.21b). The process times of bootstrap samples are reasonably stable as well (Figure 4.23a). The fitted dynamics were able to explain most of the variance, leaving the CV<sup>2</sup> of unexplained noise of most genes under 1 (Figure 4.23c). Therefore, the Erythroid dataset appears to be a suitable dataset

76


<!-- Start of picture text -->
a b<br>Read depth estimates Filtered genes for fitting<br>i Forebrain i Forebrain<br>Radial Glia<br>Neuroblast<br>Immature neuron<br>Neuron<br>ii ii<br>Erythroid Erythroid<br>iii iii<br>Cell cycle Cell cycle<br>iv iv<br>Neuron Neuron<br>v PBMC v PBMC<br><!-- End of picture text -->

Figure 4.19: **Read depth estimation using normalized covariance for highly variable gene selection** . **a** ) Read depth estimation based on total counts of Poissonion genes. Cells are colored by their cell types. **b** ) Selected genes (black) for fitting plotted in the same _𝐶𝑉_<sup>2</sup> -mean plot as in Figure 4.18).

for our trajectory model. The best result from random initialization is used for analysis (Figure 4.22b), and cellular posterior distributions confirm that cells have a broad distribution over process time (Figure 4.22c). Furthermore, the posterior distributions of cells do not differ significantly until E7.5, after which they roughly progress along the process time in sync with real-time progression (Figure 4.22d). This observation aligns with the understanding that erythroid differentiation in a mouse embryo is believed to begin around embryonic day 7.5 (E7.5) (Baron, Isern,

77


<!-- Start of picture text -->
a b<br>PBMC data Chronocell<br>T cell Trajectory structure<br>𝝉" 0=0 𝝉" 1 𝝉" 2=1<br>0 1 2<br>𝜶$ 0  𝜶$ 1  𝜶$ 2<br>T cells<br>Correlation<br>PC 1 3 clusters<br>random<br>initialization<br>mixture modelPoisson<br>AIC<br>PC 2<br><!-- End of picture text -->

Figure 4.20: **Inference results for T cells from PBMC data** . **a** ) Schematics of T cells from PBMC dataset and PCA plots. **b** ) The fitted trajectory structure and AIC scores of 100 random initializations (blue dots) compared to those of three clusters (Poisson mixtures) model (yellow line). AP stands for average precision.


<!-- Start of picture text -->
a Forebrain data b Chronocell c Posterior distributions<br>(warm start)<br>Trajectory structure Cell types Densities<br>𝝉" 0=0 𝝉" 1 𝝉" 2=1<br>0 1 2<br>Human fetus 𝜶$ 0  𝜶$ 1  𝜶$ 2<br>(week 10)<br>Radial Glia<br>NeuronImmature neuronNeuroblast Correlation posterior Marginal<br>distribution<br>3 clusters Process time<br>PC 1<br>warm start<br>mixture modelPoisson<br>initializationrandom<br>AIC inferred time<br>Cells ordered in<br>PC 2<br><!-- End of picture text -->

Figure 4.21: **Inference results for Forebrain data** . **a** ) Schematics of Forebrain data and PCA plot of cells colored by cell type annotations. **b** ) The AIC scores of the trajectory and cluster models. The x-axis is the mean process time correlations of 100 random initializations (blue dots). The AIC scores of random initializations are compared to those of warm start (red line) as well as three Poisson mixture model (yellow line). AP stands for average precision. **c** ) Posterior distributions of process time of the trajectory model with warm start. Cells were ordered in y-axis by their inferred mean process time and the left bar displays their cell types using the colors in **a** ). The below histogram shows average posterior distribution averaged over cells. The entropy of the average posterior distribution was calculated using its weights on the 100 discretized time grids.

and Fraser, 2012). Although the alignment with physical time is not perfect, it still suggests that our trajectory model can successfully capture the correct trend of process time, even when assuming a uniform sampling distribution for all cells.

After applying our gene selection procedure based on relative likelihood and discarding genes with extreme values, we ended up with 24 (49%) genes (Figure

78


<!-- Start of picture text -->
a b c<br>Erythroid data Fitting structure and AICs Posterior distributions<br>𝝉" 0=0 𝝉" 1 𝝉" 2=1 Cell  Weights<br>0 1 2 types<br>Blood progenitor Erythroid 𝜶$ 0  𝜶$ 1  𝜶$ 2  mean<br>process<br>E7.0 E7.25 E7.5 E7.75 E8.0 E8.25 E8.5 time<br>Marginal<br>posterior<br>distribution<br>PC 1 Process time<br>d<br>Posterior distributions at different time points<br>Process time<br>e f<br>𝛼" of 24 selected genes Phase plots of top 5 DE genes<br>process<br>time<br>Unspliced counts<br>α0 α1 α2<br>inferred time<br>Cells ordered in<br>PC 2<br>Spliced counts<br>log1p( inferred values)<br><!-- End of picture text -->

Figure 4.22: **Inference results for Erythroid data** . **a** ) Schematics of Erythroid data and PCA plot of cells colored by cell type annotations. **b** ) The fitted trajectory structure and inferred mean process time from random initialization indicated in blue on the same PCA plot as in **a** ). **c** ) Posterior distributions of process time. Cells were ordered in y-axis by their inferred mean process time and the left bar displays their cell types using the colors in **a** ). The below histogram shows average posterior distribution over cells. The entropy of the average posterior distribution was calculated using its weights on the 100 discretized time grids. **d** ) Averaged posterior distribution across cells from different experimental time points. n is the number of cells. **e** ) _𝛼_ values of 24 selected genes over states. **f** ) Phase plots of top five DE genes of 24 selected genes. The x-axis is the raw unspliced counts and y- axis is the raw spliced counts. The blue curve is the fitted mean of product Poisson distributions of unspliced and spliced counts over process time, and its darkness corresponds to the value of process time.

4.22e). Subsequently for demonstration, we chose the top five DE genes ( _Cpox, Smim1, Abcg2, Rbpms, Prtg_ ) with the largest fold change of transcription rates, and plotted their phase portraits (Figure 4.22f). Interestingly, four of them ( _Cpox_ (Taketani, Furukawa, and Furuyama, 2001), _Smim1_ (Aniweh et al., 2019), _Abcg2_ (Zhou et al., 2005), _Rbpms_ (Rooij et al., 2017)) were reported to be directly relevant to erythroid development, which illustrates that selecting DE genes based on inferred transcription rates is a straightforward and effective approach.

79

## **a** AIC of different models and initializations


<!-- Start of picture text -->
mean<br>process<br>time<br>Correlation between mean<br>process time of each<br>initialization and cell type<br>annotations<br>AIC<br><!-- End of picture text -->

## **b** AIC vs Correlation of bootstrap samples


<!-- Start of picture text -->
Correlation between mean<br>process time of each bootstrap<br>sample and the original one<br><!-- End of picture text -->


<!-- Start of picture text -->
c<br>Remaining squared coefficient of variance<br><!-- End of picture text -->


<!-- Start of picture text -->
Remaining  𝐶𝑉 !<br>Genes frequency<br><!-- End of picture text -->

Figure 4.23: **Supplementary figures for Erythroid data** . **a** ) AIC scores and mean process time correlations of 100 random initializations (blue dots) compared to those of warm start (red line) as well as three clusters (Poisson mixtures) model (yellow line). AP stands for average precision. Mean process time of the initialization with lowest AIC is indicated in blue on the same PCA plot as in **a** ). **b** ) AIC scores and mean process time correlations of 100 bootstrap samples. The x-axis is the Pearson’s correlation between the mean process time of each bootstrap and the those of original data, i.e., the plotted one in **a** ). **c** ) Distribution of remaining squared coefficient of variance of 49 genes used in the fitting. Remaining squared coefficient of variance is calculated by dividing the remaining unexplained variance by mean squared.

Based on the results from datasets ranging from clusters to trajectories, it becomes evident that real datasets can display a spectrum of continuity in cellular process

80

time distribution. Therefore, it is critical to assess the quality of inference and verify the requirements for reliable results are indeed met.

## **Degradation rates estimates agree with metabolic labeling data**

In addition to validating the process time, we also sought to validate the inferred parameters, which motivated us to use a metabolic labeling dataset from scEU-seq, comprising human retinal pigment epithelial (RPE1) cells undergoing cell cycles (Figure 4.24a) (Battich, Beumer, et al., 2020). Metabolic labeling of new mRNA allows for the estimation of degradation rates from cells with varying labeling times, enabling a comparison with our parameter estimations.


<!-- Start of picture text -->
a b c<br>Cell cycle data Fitting structure and results Posterior distributions<br>M G1 𝝉" 0=0 𝝉" 1 𝝉" 2 𝝉" 3=1 typesCell  Densities<br>0 1 2 0 Cell  Densities<br>G2 S 𝜶$ 0  𝜶$ 1  𝜶$ 2  𝜶$ 0  opposite connect  types<br>mean  sides<br>RPE1 cells process<br>time<br>G2/M M G1 S G2/M Process<br>Average  Averaged  time<br>posterior  posterior<br>distribution distribution<br>𝜏̂1= 𝜏̂2=<br>Process time<br>d e<br>𝛼" of 84 selected genes Comparing γ estimates with metabolic RNA labeling data<br>Gene<br>α0 α1 α2 our γ estimates our γ estimates<br>inferred time<br>Cells ordered in<br>Battich et al. Schofield et al.<br>log1p( inferred values)<br><!-- End of picture text -->

Figure 4.24: **Inference results for Cell cycle data** . **a** ) Schematics of Cell cycle data and scatter plot of the Geminin-GFP and Cdt1-RFP of RPE1 cells colored by cell type annotations. **b** ) The fitted trajectory structure and inferred mean process time from random initialization indicated in blue on the same scatter plot as in **a** ). **c** ) Posterior distributions of process time. Cells were ordered in y-axis by their inferred mean process time and the left bar displays their cell types using the colors in **a** ). The below histogram shows average posterior distribution averaged over cells. The entropy of the average posterior distribution was calculated using its weights on the 100 discretized time grids. **d** ) _𝛼_ values of 84 selected genes over states. **e** ) Comparison of _𝛾_ estimates for 84 selected genes with estimates derived from metabolic RNA labeling data. CCC stands for concordance correlation coefficient. n is the number of genes for which estimates are available in each respective paper.

In the trajectory structure, we specified that the initial and final states were identical. Given our assumption that the initial state is at a steady state, capturing the cyclic nature of the cell cycle poses an additional requirement that cells must also approach a steady state in the last interval as well, which happened to be reasonably satisfied by

81

our results. In line with the expectation that cell cycle is a highly dynamic process, the random initialization provides a relatively stable result: the AIC exhibits a single minimum that aligns with the direction of cell cycle progression (Figure 4.25a), and bootstrap samples mostly align with the result of the original one (Figure 4.25b). Starting from the result of random initialization, a desynchronized model was fitted to enhance the accuracy of parameter estimations (Figure 4.25c). The resulting fit maintains alignment with the cell cycle progression (Figure 4.24b), and the CV<sup>2</sup> of the unexplained noise mostly remains below 1 for most of the genes (Figure 4.25c). The RPE1 dataset was metabolically labeled for different lengths of time but posterior distributions of RPE1 cells with different labeling times do not show significant differences, as a negative control in contrast to the erythroid data (Figure 4.25e).

The posterior distributions successfully capture the cyclic nature of the data. The cell types ordered by mean process time exhibit a cyclic pattern (Figure 4.24c); the phase plots of marker genes confirm the cycling dynamics of fitted means of unspliced and spliced counts (Figure 4.25f); the starting and ending values of fitted means of most of genes match with each other (Figure 4.25g). As both axes are cyclic, it is possible to connect the opposite edges and transform the two-dimensional cell-by-time grids posterior distributions into a torus on the surface of which the posterior distributions look like a circle (Figure 4.24c). Based on cell type annotation, total RNA counts number (Figure 4.25h), and marker genes dynamics (Figure 4.25e), we can roughly assign the three intervals to G2/M, G1/S, and S/G2 phase, and mitosis happens shortly after _𝜏_ 0.

After selecting genes by relative likelihood and discarding genes with extreme values, we ended up with 84 (46%) genes (Figure 4.24d). We compared the degradation rates of 84 selected genes to those derived by scEU-seq (Battich, Beumer, et al., 2020) and TimeLapse-seq (Schofield et al., 2018). For scEU-seq, as we neglected the changes in degradation rate along cell cycle, we used the averaged degradation rates in Figure S10C of Battich et al. We observed moderate correlations between our degradation rate estimates and the respective estimates from Battich and Schofield (Figure 4.24e), and these correlations exhibited a magnitude similar to the correlation between the Battich and Schofield estimates (Figure 4.25i), which suggests that the parameters inferred by Chronocell indeed possess a meaningful biophysical interpretation.

82

## **4.4 Discussion**

We have introduced Chronocell, a method constructed upon a trajectory model featuring biophysically meaningful parameters and a principled approach to fitting and analysis. Counts are directly modeled, estimation accuracy is characterized, and unreliable instances are discerned. We found several requirements regarding dynamics and noise that must be satisfied to obtain reliable results, which makes process time inference challenging and renders retrospective model assessment indispensable. We applied Chronocell to different kinds of real datasets, recognized inapplicable ones by assessing instability, and demonstrated meaningful interpretation of process time and parameters on applicable ones.

Of note, our trajectory model is simplified to balance interpretability and tractability. Building on the concept of cell state transitions, we have assumed piecewise constant transcription rates which describe genes with fast chromatin states switching in saturated regime, but may be unrealistic for many biological systems. Furthermore, we have assumed that splicing and degradation rates remain constant, which although reasonable for many genes, is not accurate for genes with peaked response (Rabani et al., 2011). We also did not incorporate transcriptional bursting due to the absence of an analytically determined temporal solution, and this leads to a under-dispersed distribution compared to what is typically observed in biological data. Nevertheless, this can be resolved by using numerical solutions ( **Gorin2023-ax** ). However, even with this simplified model, we have found that accurate inference imposes strict requirements on data. This question is inherently challenging and insufficiently specified due to the existence of latent variables and flexibility of the transcription rates. A more realistic model would have even more stringent requirements.

Since fitting dynamical parameters is challenging from static snapshots, physical time information could offer valuable insights when incorporated into our latent variables model. While the requirements on sampling and noise might potentially be relaxed, they would likely persist to some extent. Thus, intensely sampled time series datasets derived from well-defined cellular processes would be the ideal choice for trajectory inference. However, it remains to address the key question of how physical time should be translated into sampling distribution assumptions. The choice of sampling distribution reflects our understanding of cell heterogeneity at each time point. Should we fix the process time to physical time completely, i.e., a delta distribution? Or should we assume heterogeneity within one time point? If so, what kind of distribution should we use? There is no straightforward answer,

83

as it depends on our understanding of the process being studied. For instance, in a neuron dataset with cells sampled at five time points after stimulation, assuming homogeneous cell responses would suggest using a delta distribution, which aligns process time directly with physical time. However, if we account for heterogeneity within a time point, other distributions may be more appropriate. Furthermore, assuming different distributions (delta, exponential, uniform) can lead to different results (Figure 4.26). This underscores the necessity for a more comprehensive understanding and modeling of cell heterogeneity, and optimal experimental design for both the number and timing of the time points to generate more informative data.

We have not yet provided a benchmark against other methods. Each trajectory inference method assumes a different model, and comparing methods with different underlying models is often less informative without ground truth. For example, descriptive models use conceptually different approaches, so comparing them is an "apples to oranges" situation, as they cannot recover the true time of data under Chronocell trajectory model. On the other hand, they may be more suitable for exploratory analysis, with fewer data requirements and being less computationdemanding. Similarly, in model-based approaches, the model inherently reflects our understanding of the data, and discrepancies in results arise from differences between models. This underscores the importance of using models that are grounded in biophysical motivation. For demonstration purposes, we provide a comparison of Chronocell with some widely used trajectory inference methods, including Slingshot (Street et al., 2018), Monocle 3 (Cao et al., 2019), and diffusion pseudotime (Haghverdi et al., 2016), as well as recently published veloVI which also integrates trajectory inference with RNA velocity (Du et al., 2024). These comparisons are demonstrated on the simulated data used for illustration in Figure 4.7, as well as simulations generated by dyngen (Cannoodt, Saelens, Deconinck, et al., 2021) (Figure 4.27). We find that other methods cannot correctly recover true time on data generated under the Chronocell model (Figure 4.28). For dyngen simulation, Chronocell has comparable or better accuracy though all methods capture the correct trend but fail to recover true time accurately. For real data, benchmarking is more challenging due to the lack of ground truth. The closest approximation to ground truth is the experimental time in time series data, especially with short enough intervals and a clear start point. Despite the uncertainty of assumed cell heterogeneity discussed above, at least the inferred time of cells should proceed along with experimental time. Therefore, we also test other methods on the neuron data and find that only Monocle 3 captures the general trend of time progression (Figure 4.29).

84

In summary, our biophysically motivated model of the dynamical processes captured in single-cell data enables the inference of process times and parameters with biophysical interpretations. It presents an alternative approach to unveil continuous latent cell representations within a well-defined and rigorous framework, and highlights the limitations of what can be inferred using current snapshot single-cell genomics data.

## **4.5 Methods**

We begin by describing our trajectory model, followed by a description of the inference procedure. Next, we explain the analysis pipeline, including our gene and model selection procedure. Then, we elucidate the simulation setup. Finally, we detail the preprocessing of real datasets.

Throughout the Methods we denote data by **X** , and note that **X** corresponds to a cell by gene by species array. We use _𝑖_ to index cells, _𝑗_ to index genes, and _𝑐_ to index species. Parameters are denoted by _𝜃_ , and latent variables by _𝑧_ . _𝑝_ (·) means a probability distribution.

## **Model**

We used a simple and interpretable latent variable model for the probability distribution of the counts, with explicit biophysical meaning associated to each latent variable. We assumed cells are asynchronous, and we therefore introduced two latent variables that corresponded to the lineage and time of the cell.

Therefore, in our trajectory model, the gene expression data of each cell **x** was described as a function of latent variables **z** = ( _𝑙, 𝑡_ ) which specify the lineage _𝑙_ and time _𝑡_ of the cell. By considering a particular parametric class of gene expression dynamics that specify the distribution _𝑝_ ( **y** | **z** _, 𝜃_ ) of _in vivo_ counts **y** , and a sequencing noise model _𝑝_ ( _𝑥_ | _𝑦_ ), we mapped latent variable _𝑧_ into data space and arrived at an explicit formulation of data distribution that could be trained using the expectationmaximization (EM) algorithm. In other words, we assumed the counts of each cell **x** had the following density:


where _𝑝_ ( _𝑧_ ) is the distribution of latent variables.

85

In the following, we specify _𝑝_ ( _𝑦_ | _𝑧, 𝜃_ ), _𝑝_ ( _𝑥_ | _𝑦_ ) and _𝑝_ ( _𝑧_ ), which are based on the transcription model, measurement model and sampling measure.

## **Transcription model**

Since current transcriptomic data can be used to measure the numbers of both nascent and mature transcripts, we considered the production, processing, and degradation of individual RNA molecules in our transcription model, as in previous RNA velocity literature (La Manno et al., 2018).

The distribution of RNA counts in the reaction system (Equation4.2) is known (Jahnke and Huisinga, 2007). We assumed that the initial distribution of _𝑈_ and _𝑆_ was a product Poisson distributions, which implies that the mean parameter vector _𝜆_ = ( _𝜆𝑢, 𝜆𝑠_ ) of _𝑈_ and _𝑆_ evolved according to Equation(4.3).

The functional form of _𝐴𝑙_ ( _𝑡_ ) reflects our assumptions of gene expression during development. However, explicitly modeling transcription rates as functions of gene expressions is hard and tends to overfit. More fundamentally, we have some prior physical intuition; this function is actually _𝐴𝑙_ ( _𝜆,_ **u** _, 𝑡_ ), where **u** is some highdimensional vector of regulator concentrations. These data are not possible to collect using currently available technologies, although this constraint may change in the coming years. In principle, we can write down these equations, and even simulate them (using dyngen (Cannoodt, Saelens, Deconinck, et al., 2021) or the stochastic simulation algorithm), but we strived to start with an analytically tractable model, particularly to recapitulate and formalize the increasingly popular RNA velocity framework. Therefore, we used a phenomenological model and didn’t consider gene interactions. Rather, the effect of transcriptional regulation on each gene during development was summarized into synchronized state switching and each state had its transcription rate. This formalized transient cell types.

To be able to account for multiple lineages, we assumed cell states S = 0 _,_ 1 _, ..., 𝑆_ formed a directed graph, with each lineage represented as a path of length _𝐾_ on this graph.. The trajectory structure described the graph, and recorded the states _𝑠_ ( _𝑙, 𝑘_ ) ∈S _, 𝑙_ = 1 _, ..., 𝐿, 𝑘_ = 1 _, ..., 𝐾_ of the _𝐿_ lineages during the _𝐾_ stages. We treated the trajectory structure as known since it can typically be obtained from our previous knowledge of the data. Specifically, for lineage _𝑙_ , we assumed _𝐴𝑙_ ( _𝑡_ ) is a piecewise constant function: _𝐴𝑙_ ( _𝑡_ ) = _𝛼𝑠_ ( _𝑙, 𝑘_ ), where the cellular state index s is determined by the lineage _𝑙_ , and the time interval _𝑘_ to which _𝑡_ belongs, i.e., _𝑡_ ∈( _𝜏𝑘_ −1 _, 𝜏𝑘_ ]. The state index _𝑠_ = _𝑠_ ( _𝑙, 𝑘_ ) was determined by the trajectory structure.

86

For example, given the trajectory structure in Figure 4.2, _𝑠_ ( _𝑙_ = 1 _, 𝑘_ = 0) = _𝑠_ ( _𝑙_ = 2 _, 𝑘_ = 0) = 0, _𝑠_ ( _𝑙_ = 1 _, 𝑘_ = 1) = _𝑠_ ( _𝑙_ = 2 _, 𝑘_ = 1) = 1, _𝑠_ ( _𝑙_ = 2 _, 𝑘_ = 2) = 2 and _𝑠_ ( _𝑙_ = 2 _, 𝑘_ = 2) = 3.

Then, the parametric solution of _𝜆_ was given by


Assuming cells are at steady states at time 0, we have _𝜆𝑢_ (0) = _𝛼𝑠𝑙,_ 0 and _𝜆𝑠_ (0) = _<u>𝛽</u> 𝛾_<sup>_𝛼𝑠𝑙,_0.Therefore, for each gene, the parameters are</sup><sup>_𝜃_=(</sup><sup>_𝛼, 𝛽, 𝛾, 𝜏_).</sup>

## **Measurement model**

Next, we needed to have a measurement model that connected counts number **y** in cells to the observed counts **x** in a single-cell RNA-seq experiment.

We assumed each molecule of mRNA produces _Bernoulli_ ( _𝑞_ ) number of captured RNA molecules, which is also an good approximation of a Poisson model with low mean (Gorin and Lior Pachter, 2023; Sarkar and Stephens, 2021).The capture rate _𝑞_ for each molecule can potentially depend on factors such as cell read depth, gene-specific, and species-specific biases in mRNA capture methods. However, in our model, we assume the capture rate only varies with cell read depth (or cell size), i.e., _𝑞_ = _𝑟𝑖_ , where _𝑟𝑖_ represents the read depth (cell size) of cell _𝑖_ . With _𝑖_ as the cell index, _𝑗_ as the gene index, and _𝑐_ as the species index, we have


where _𝜆 𝑗𝑐_ is the ODE solution for species c of gene j.

87

This is equivalent to multiplying the mean of Poisson distributions by a constant _𝑐𝑖_ . Since usually only the relative value of read depth _𝑐𝑖_ can be available, we absorbed the mean of _𝑐𝑖_ into _𝛼_ and infer their product directly:

## _𝑥𝑖𝑗𝑐_ ∼ _𝑃𝑜𝑖𝑠𝑠𝑜𝑛_ ( _𝑐𝑖𝜆 𝑗𝑐_ ) _._

## **Sampling distribution**

Now that we have defined the _𝑝_ ( _𝑥_ | _𝑧, 𝜃_ ), the only remaining thing to complete _𝑝_ ( _𝑥_ | _𝜃_ ) is the sampling distribution _𝑝_ ( _𝑧_ ), which describes the prior distribution of latent variables. Given the formula of _𝑝_ ( _𝑦_ | _𝑧, 𝜃_ ), it is easy to see that the model is not identifiable if _𝑝_ ( _𝑧_ ) is not fixed, because we can change _𝑝_ ( _𝑧_ ) together with _𝛽_ and _𝛾_ easily without changing _𝑝_ ( _𝑥_ ), for example, by scaling _𝛽_ and _𝛾_ and transform _𝑝_ ( _𝑧_ ) accordingly. Therefore, we assumed _𝑡_ ∈[0 _,_ 1] and fixed a uniform prior for _𝑡_ on (0 _,_ 1]. With this given prior distribution, the model was identifiable, because the parameterized form of the means of Poisson distributions is identifiable and Poisson distribution is identifiable (Teicher, 1961). If one has information about real time, one can adjust the range and prior of _𝑡_ to be have more physical meaning. For example, for the cell cycle dataset, if one knows that the whole cycle takes 24 hours, then one can either set the range of _𝑡_ to be [0 _,_ 24], or scale the results by dividing both _𝛽_ and _𝛾_ by 24, while keeping the other parameters unchanged.

## **Connection to cluster models**

In the fast dynamic limit, as there are few cells out of steady states, transitions (edge) disappear and only states (nodes) remain, and both the weight of lineages and the length of time interval (or the weight at t=0 for state 0) determine the mixture weights of clusters. Specifically, for the state 0, its weight equals the weight at t=0, while for the state 2, its weight equals the product of the length of the second time interval ( _𝜏_ 1 _, 𝜏_ 2] and the weight of the second lineages. Thus, the Poisson mixtures model strictly belongs to the degenerate cases of our trajectory model, which connects Chronocell to biophysical cluster models like meK-Means (Tara Chari, Gorin, and Lior Pachter, 2024a), barring differences in noise models and hard/soft assignment. This does not mean that our trajectory model should be fit on cluster data, because the resulted process time is no longer meaningful. Instead, these connections allowed us to better compare the models, and determine which model was more appropriate (see Section 4.5 “Gene selection”).

88

## **Inference**

## **Chronocell overview**

**Input** The input of Chronocell are 1) trajectory structure, 2) sampling assumption, and 3) scRNA-seq count matrix. Trajectory structure is provided to Chronocell as a 2D array, with each lineage (path) represented as a row. Along with the structure, an initial guess of switching time is also needed as a starting point in the fitting. The sampling assumption refers to the prior distribution of the latent variables (process time and lineages) for each cell. This is represented as a 3D array with shape (n, l, m), where n is the number of cells, l is the number of lineages, and m is the number of time grids.

**Model** Building upon the common transcription model, we have two classes of models based on the assumption of global switch time: (1) the synchronized model, which assumes a completely synchronized switch in transcription rates across all genes; and (2) the desynchronized model, where each gene has its own switching time. The desynchronized model is more challenging to fit from scratch, so we recommend using a warm start based on the results of the synchronized model.

**Inference** We use the expectation–maximization algorithm to fit the trajectory model on the scRNA-seq count matrix.

**Output** The primary output of Chronocell consists of the parameters and posterior distribution for each cell. Other relevant information such as the Akaike Information Criterion (AIC) and the Fisher information matrix can also be calculated.

## **Maximum likelihood estimates of parameters by EM algorithm**

We use the expectation–maximization algorithm to estimate model parameters _𝜃_<sup>ˆ</sup> . For simplicity, we discretize the latent variable _𝑡_ with finite regular grid points over the interval: _𝑡_ = _𝑡_ 1 _, ...., 𝑡𝑀_ , which basically approximates a continuous measure with a discrete measure. Then, the latent variable z=(l,t) describing lineage and time is discrete, and we write<sup>�</sup> _𝑧𝑖_<sup>to denote the summation over all L lineages and M time</sup> grid points, i.e.,<sup>�</sup> _𝑧_<sup>= �</sup> _𝑙_<sup>_𝐿_</sup> =1 � _𝑚𝑀_ =1<sup>.With this, the objective function becomes</sup>

89


where i is the cell index and _𝑝_ ( _𝑥𝑖, 𝑧𝑖_ | _𝜃_ ) denotes the probability of observing _𝑥𝑖_ with the latent variable being _𝑧𝑖_ for cell i.

As log function is concave, we can use Jensen’s inequality:


Since<sup>_<u>𝑝</u>_</sup><sup><u>(</u></sup><sup>_𝑥𝑖,𝑧𝑖_</sup><sup><u>|</u></sup><sup>_𝜃_</sup><sup><u>)</u></sup> _𝑝_ ( _𝑧𝑖_ | _𝑥𝑖,𝜃_ )<sup>=</sup><sup>_𝑝_(</sup><sup>_𝑥𝑖_|</sup><sup>_𝜃_)is a constant for all</sup><sup>_𝑧𝑖_, the equality holds and</sup>


Our trajectory model makes it possible to write out _𝑝_ ( _𝑥𝑖_ | _𝑧𝑖, 𝜃_ ) explicitly:


Therefore, we could use the expectation–maximization algorithm efficiently. Specifically, in the E-step of EM algorithm, we calculated the posterior distribution _𝑝𝑖_ ( _𝑧𝑖_ | _𝑥𝑖, 𝜃_ ) based on _𝑝_ ( _𝑥𝑖_ | _𝑧𝑖, 𝜃_ ),


90

In the M-step, based on fixed _𝑝𝑖_ ( _𝑧𝑖_ | _𝑥𝑖, 𝜃_ ) and analytical form of _𝑝_ ( _𝑥𝑖_ | _𝑧𝑖, 𝜃_ ), we optimized _𝜃 𝑗_ for each gene _𝑗_ separately by maximizing


Both the value and the gradient of _𝐹𝑗_ can be written out analytically and computed efficiently. Therefore, we could use off-the-shelf quasi-Newton methods for optimizing _𝐹𝑗_ with respect to _𝜃 𝑗_ , e.g., ’L-BFGS-B’ method in minimize function provided by Scipy (Virtanen et al., 2020; Zhu et al., 1997).

In each step of EM algorithm, we alternated between the expectation and maximization steps. The implementation is based on defining the function that calculates _𝑝_ ( _𝑥𝑖𝑗_ | _𝑧𝑖, 𝜃_ ), so it would be easy to modify _𝑝_ ( _𝑥𝑖𝑗_ | _𝑧𝑖, 𝜃_ ) for different models in the future.

A warm start incorporating prior knowledge about data can help algorithm converge to the optimal _𝜃_<sup>∗</sup> quickly. If neither initial parameters nor _𝑝_ ( _𝑧_ | _𝑥_ ) is given, we use random initializations. Multiple runs with different starting points are used to avoid local minima. By default, we tried 100 different random initializations, and run 100 steps for each initialization both for random initialization and warm start.

## **Poisson mixtures model**

For fitting clusters, we used Poisson mixture models. Suppose there are S mixtures with transcription rates _𝛼 𝑗𝑠_ , _𝑠_ = 1 _, ..., 𝑆_ for each gene _𝑗_ , and each mixture is at steady state. Thus, the parameters of one gene are _𝑎 𝑗_ =<sup>_<u>𝛼</u>_</sup> _𝛽_<sup>and</sup><sup>_𝜌_=</sup> _𝛾_<sup>_<u>𝛽</u>_</sup> _𝑗_<sup>_<u>𝑗</u>_,since only</sup> the ratio is identifiable.


Similarly to the Gaussian mixture model, we could use the EM algorithm to infer parameters (including mixture weights) and posteriors.

91

## **Analysis**

## **Fisher information**

The Fisher information matrix (FIM) is defined to be


Since


we could calculate FIM numerically with the explicit form of the derivative and the posterior distribution.

## **Gene selection**

We did not use absolute likelihoods to select dynamical genes, because different genes have different scales and are not directly comparable. Instead, we noticed that the cluster model serves as a natural reference point for comparison, as genes with no dynamics can be fitted equally well, if not better, by clusters. Therefore, we decided to use the relative likelihood as a criterion for gene selection.

For trajectory model,

92


Similarly for clusters model,


We defined the gene-wise likelihood of gene j for trajectory model to be


and for clusters,


The first term is meant to represent the difference in likelihood caused by different flexibility of latent variables of two models.

For gene selection, we compared the gene likelihood of two models and selected genes whose gene likelihood of trajectory model was higher than those of the cluster model.

93

## **Uncertainty assessment**

We used uncertainty/instability to falsify results. First, we evaluated the variation of different random initializations to assess the uncertainty of the inference. This was done by performing multiple (usually 100) random initializations. Specifically, we evaluated whether the process time estimation of initializations with high ELBO scores concentrated around the correct direction. To quantify this, we classified the output of each random initialization to be correct if the process time estimates had a correlation higher than 0.8 with the reference, and we used different ELBO score thresholds to compute the precision-recall curve, which were then summarized by average precision (AP). An ideal case with high ELBO scores concentrated around correlation one led to an AP close to one while multiple comparable maxima lead to low AP.

Another approach to assess uncertainty is through bootstrap resampling. The same inference procedure is applied to the resampled data, and the variation in the resultant process time serves as an indicator of instability. Specifically, we calculate the correlation of process time between the original and the resampled data and interpret instability as large variance of the correlation.

## **Simulations**

We randomly generated parameters for 200 genes and sampled 2000 cells by default unless otherwise specified. Cells were sampled uniformly over process time and lineages. We then fitted the model with the correct trajectory structure and synchronized model if not stated otherwise.

For the simulation parameters, we assumed that the transcription parameters ( _𝛼_ , _𝛽_ , _𝛾_ ) followed the log-normal distribution _𝑙𝑜𝑔𝑛𝑜𝑟𝑚𝑎𝑙_ ( _𝜇, 𝜎_ ), where _𝜇_ is the mean and _𝜎_ is the standard deviation of the variable’s natural logarithm. We attempted to derive realistic parameters for the distributions from the literature. Hence, we assumed _𝛽_ ∼ _𝑙𝑜𝑔𝑛𝑜𝑟𝑚𝑎𝑙_ (2 _,_ 0 _._ 5) _, 𝛾_ ∼ _𝑙𝑜𝑔𝑛𝑜𝑟𝑚𝑎𝑙_ (0 _._ 5 _,_ 0 _._ 5) so that unspliced to spliced ratio was around 0.2 and their distributions resembled those determined from metabolic labeling datasets (Rabani et al., 2011). The _𝛼_ were assumed to follow _𝑙𝑜𝑔𝑛𝑜𝑟𝑚𝑎𝑙_ (2 _,_ 1), so that the mean of spliced counts were similar to those in scRNA-seq data. We assumed the read depth follows Beta distribution _𝑟_ ∼ _𝐵𝑒𝑡𝑎_ ( _𝜇_ = 4<sup><u>1</u></sup><sup>_, 𝑣_=</sup> 641<sup>),where</sup><sup>_𝜇_wasthemeanand</sup><sup>_𝑣_thevariance.Forsimulations</sup> with Gamma noise, we multiplied the mean of Poisson distribution _𝜆_ by a random variable following Gamma distribution with mean 1 and variance 0.5.

94

For simulations under the desynchronized model, gene-wise _𝜏𝑘_ was sampled from a uniform distribution on [ _𝑇𝑘_ −<sup><u>Δ</u></sup> 2<sup>_<u>𝜏</u>,𝑇𝑘_+</sup><sup><u>Δ</u></sup> 2<sup>_<u>𝜏</u>_], where</sup><sup>_𝑇𝑘_corresponds to the global</sup><sup>_𝜏𝑘_</sup> in the synchronized model, and Δ _𝜏_ was the smallest interval length ensuring that _𝜏𝑘_ retains its order.

To vary the sampling distributions, we generated a Gaussian distribution with a random mean and standard deviation 0.05. We then sampled both from the Gaussian and the uniform distribution, and blended them together in different proportions. The percentages of time sampled from a Gaussian ranged from 0 to 1, increasing by 0.1 increments.

To characterize the time errors, we calculate root mean squared error (RMSE) for the posterior mean of process time in comparison to the true time. To calculate the errors of parameters, we divide the absolute error of _𝛼_ by the square root of true values and _𝛽, 𝛾_ by true values, so that errors of different genes are more comparable. We refer to these as normalized errors throughout the text.

## **Real datasets preprocessing**

Cov( _𝑋𝑎,𝑋𝑏_ <u>)</u> To estimatethesquaredcoefficientofvariationofthereaddepth _𝜉_ := E � E[ _𝑋_ ] E[ _𝑌_ ] � _𝑎,𝑏_<sup>,</sup> we calculated the covariance matrix of all genes with nonzero means, which was divided by the mean squared and averaged across gene pairs to calculate the mean normalized covariance as an estimate of _𝜉_ . We then selected Poissonian genes whose variances are close to baseline variance with reasonably large mean ( _𝑣𝑎𝑟<_ 1 _._ 2( _𝜇_ + _𝜉𝜇_<sup>2</sup> ) _, 𝜇>_ 0 _._ 01). However, as some genes can be co-regulated and, therefore, correlated, we calculated the mean normalized covariance of Poissonian genes and repeated selected new Poissonian genes until the mean normalized covariance no longer changed. This typically occurred after two iterations. Finally, we normalized the sum of counts of the selected Poissonian genes by their mean to obtain the relative read depth estimates, which were then used as fixed parameters during the fitting process.

Based on simulations of factors of informativeness of the data, including numbers of cells and genes, the average mean of _𝛼_ parameters as well as _𝛽_ and _𝛾_ ratio, we determined the procedure of filtering genes for fitting: we applied count mean thresholds (0.02 for unspliced and 0.1 for spliced), filtered out genes with a small unspliced to spliced ratio (<sup>_<u>𝑈</u>_</sup> _𝑆_<sup>_<𝑒_−4),andfinally,selectedgeneswithavariance</sup> larger than 1.2 times the baseline variance, i.e., _𝑣𝑎𝑟>_ 1 _._ 2( _𝜇_ + _𝜉𝜇_<sup>2</sup> ), where _𝜇_ is the mean, _𝑣𝑎𝑟_ is the variance, and _𝜉_ is the read depth CV<sup>2</sup> . For cell cycle data, we

95

also constrained genes to the Gene Ontology term "cell_cycle" (GO:0007049). We occasionally adjusted the variance threshold to 1.5 in order to end up with 50–200 genes. Then trajectory and Poisson mixture models were fitted on those genes.

## **Use of other methods**

We have also used dyngen to generate simulation data (Cannoodt, Saelens, Deconinck, et al., 2021). We use a bifurcation backbone for generation of 10000 cells and 200 genes following its vignette.

For Monocle 3 and diffusion pseudotime, we always provide the correct root cells whose simulation times are 0 for simulations. For real dataset, we set to the cells from the cell type that is expected to be the progenitor. In Monocle 3, when the cells form disconnected clusters, only cells on the partition that includes the root cell has finite pseudotime. We only consider those cells and discard other cells with infinite pseudotime for comparison with simulation time. For slingshot, we manually set the true start cluster based on the simulation time for simulation and the cell type in real datasets. For veloVI, we use the mean latent time across genes for comparison with simulation time.

96


<!-- Start of picture text -->
a b c<br>AIC of different models and  AIC vs Correlation of bootstrap  ELBO over iterations for<br>initializations samples desynchronized model<br>mean<br>process<br>time<br>start from<br>synchronized<br>model result<br>Iterations<br>d f<br>Remaining squared coefficient of  Dynamics of marker genes<br>variance<br>process<br>time<br>Remaining  𝐶𝑉 !<br>Process time<br>e<br>Posterior distributions of cells with different labeling time<br>Process time<br>g h i<br>Starting and ending values of fitted means Total counts number γ estimates of metabolic labeling experiments<br>Unspliced Spliced<br>Gene<br>Starting values( t=0) G2/M M G1 S G2/M Schofield et al.<br>ELBO<br>Unspliced<br>Genes frequency<br>Spliced<br>Probability<br>Ending values (t=1) Relative number Battich et al.<br><!-- End of picture text -->

Figure 4.25: **Supplementary figures for Cell cycle data** . **a** ) AIC scores and mean process time correlations of 100 random initializations (blue dots) compared to those of warm start (red line) as well as three clusters (Poisson mixtures) model (yellow line). AP stands for average precision. Mean process time of the initialization with lowest AIC is indicated in blue on the same PCA plot as in **a** ). **b** ) AIC scores and mean process time correlations of 100 bootstrap samples. The x-axis is the Pearson’s correlation between the mean process time of each bootstrap and the those of original data, i.e., the plotted one in **a** . **c** ) ELBO scores over iterations for desynchronized model. The fitting started with the best random initializations result of synchronized model. **d** ) Distribution of remaining squared coefficient of variance of 182 genes used in the fitting. Remaining squared coefficient of variance is calculated by dividing the remaining unexplained variance by mean squared. **e** ) Averaged posterior distribution across cells with different labeling times. n is the number of cells. **f** ) Dynamics of three marker genes. The blue curve is the fitted mean of product Poisson distributions of unspliced and spliced counts over process time, and its darkness corresponds to the value of process time. Cells’ raw counts (gray) are plotted against their corresponding process times. **g** ) Starting and ending values of fitted mean of Poisson distributions. **h** ) Total counts over process time of cells colored by cell type annotations. **i** ) Comparison of _𝛾_ estimates from two metabolic RNA labeling papers for 84 selected genes. Estimates of 67 genes are available in both papers. CCC stands for concordance correlation coefficient.

97


<!-- Start of picture text -->
a Assumed sampling distributions b Mean process time on PCA c Mean process time of cells from<br>i Delta distribution mean process  different experimental times<br>time (h)<br>Time  (h) Experimental time (h)<br>ii Exponential distribution Trajectory structure mean process<br>𝝉" 0=0 𝝉" 1 𝝉" 2=2h time (h)<br>0 1 2<br>𝜶$ 0  𝜶$ 1  𝜶$ 2<br>warm start<br>Time  (h) Experimental time (h)<br>iii Uniform distribution mean process<br>time (h)<br>Experimental time (h)<br>Time  (h)<br>Density<br>Mean process time (h)<br>Density<br>Mean process time (h)<br>Density<br>Mean process time (h)<br><!-- End of picture text -->

Figure 4.26: **Inference results of different sampling distribution assumption for Neuron data** . Fitting was warm started from delta distribution at physical time under different sampling distribution priors using the shown trajectory structure. **a** ) The assumed sampling distribution. For **iii** , uniform distribution is assumed for cells from all time points. **b** ) The fitted trajectory structure and inferred mean process time indicated in blue on the PCA plot. **c** ) Violin plots of mean process time of cells with different labeling times. Three blue bars represent the mean and extremes.

98


<!-- Start of picture text -->
a dyngen simulation b Chronocell<br>0.3<br>0.2 Edge Trajectory structure<br>sA−>sB<br>0.1 sB−>sBmid<br>0.0 sBmid−>sC 3 4<br>sBmid−>sD<br>−0.1 sC−>sEndC 0 1 2<br>sD−>sEndD<br>−0.2 5 6<br>−0.4 −0.2 0.0 0.2 0.4<br>comp_1<br>c Monocle 3 d Slingshot e Diffusion pseudotime f veloVI<br>1.00<br>0.75<br>0.50<br>0.25<br>RMSE = 0.23<br>0.00<br>0.00 0.25 0.50 0.75 1.00<br>True time<br>comp_2<br>Monocle 3 pseudotime<br><!-- End of picture text -->

Figure 4.27: **Results of Chronocell compared to other methods on simulations generated by dyngen** . Chronocell, Monocle 3 (Cao et al., 2019), Slingshot (Street et al., 2018), diffusion pseudotime (Haghverdi et al., 2016) and veloVI (Du et al., 2024) are applied on simulation generated using dyngen (Cannoodt, Saelens, Deconinck, et al., 2021). Inferred time is plotted against true time, where x-axis is the true simulation time normalized between 0 and 1 and y-axis is corresponding inferred time normalized between 0 and 1. RMSE stands for root mean square error of inferred time. **a** ) The dyngen simulation projected into the first two principal component spaces. A bifurcation backbone is used. **b** ) The fit trajectory structure and results of Chronocell. **c** ) The result of Monocle 3. **d** ) The result of Slingshot. **e** ) The result of diffusion pseudotime. **f** ) The result of veloVI.


<!-- Start of picture text -->
a Monocle 3 b Slingshot c Diffusion pseudotime d veloVI<br>1.00<br>0.75<br>0.50<br>0.25<br>RMSE = 0.26<br>0.00<br>0.00 0.25 0.50 0.75 1.00<br>True time<br>Monocle 3 pseudotime<br><!-- End of picture text -->

Figure 4.28: **Results of other methods on Figure 2 simulation** . Monocle 3 (Cao et al., 2019), Slingshot (Street et al., 2018), diffusion pseudotime (Haghverdi et al., 2016) and veloVI (Du et al., 2024) are applied on simulation data used in Figure 2. Inferred time is plotted against true time, where x-axis is the true simulation time and y-axis is corresponding inferred time normalized between 0 and 1. RMSE stands for root mean square error of inferred time.

99


<!-- Start of picture text -->
a Monocle 3 b Slingshot c Diffusion pseudotime d veloVI<br><!-- End of picture text -->

Figure 4.29: **Results of other methods on Neuron data** . Monocle 3 (Cao et al., 2019), Slingshot (Street et al., 2018), diffusion pseudotime (Haghverdi et al., 2016) and veloVI (Du et al., 2024) are applied on Neuron data used in Figure 4.26 to generate violin plots comparing inferred time to experimental time. In these plots, the x-axisrepresents theexperimental time, whilethe y-axisshows the corresponding inferred time.

100

_C h a p t e r 5_

---

[← AN EXTRINSIC NOISE MODEL FOR NORMALIZATION](08-an-extrinsic-noise-model-for-normalization.md) · [Up: contents](index.md) · [FUTURE DIRECTIONS →](10-future-directions.md)
