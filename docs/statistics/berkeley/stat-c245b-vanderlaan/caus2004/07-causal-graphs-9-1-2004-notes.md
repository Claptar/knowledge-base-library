---
title: Causal graphs, 9/1/2004 Notes.
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Causal graphs, 9/1/2004 Notes.

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In point treatment studies we are interested in studying the causal effect of treatment on outcome of interest. Let A denotes the treatment and Y the outcome variables respectively. Other covariates X1, X2, . . . , Xm are also collected from the patients in the study, requiring adjustment of the causal effect for the covariates. In some situations, the set of causal assumptions on the random variables is known before the study begins and can be represented in the form of a causal graph.

Before we proceed to give a formal definition of this concept, we introduce the notation using the causal graph in fig. 1 as an example. There are 5 variables in this hypothetical study - X1, X2, X3, A and Y , which are represented in the graph as vertices. Directed edges represent causal dependence (of which the statistical conditional dependence is a special case), thus Y is causally dependent on A, X1 and X3; X2 is dependent on X1, etc. We define PA (X) to be the set of all random variables Z in the graph which have a direct arrow going into the node X. In other words PA (X) is the set of parent nodes of vertex X, i.e. all those vertices in the causal graph that have a directed edge that ends in X. For example PA (Y ) = {A, X1, X3} and PA (X1) = ∅. Loops are not allowed, which is equivalent to requiring that the causal graph is DAG (directed acyclic graph).

**Definition 1.** A causal graph G for the set of R.V. (X1, X2, . . . , Xm, A, Y ) in a point treatment study is a DAG defining a set of causal assumptions:


Figure 1. Example of a causal graph with three covariates.

for some deterministic functions fi, i = 1, . . . , m, fA and fY , and ϵi, i = 1, . . . , m, ϵA and ϵY are random variables called (exogenous) errors satisfying the following assumptions ϵi ⊥ PA (Xi) , ϵA ⊥ PA (A) , ϵY ⊥ PA (Y ).

Note that the causal graphs just assumes that nodes are certain functions of parents-nodes and exogenous error variables, but it assumes nothing about the functional form of these deterministic functions. However, in practice, if one aims to estimate these unknown deterministic functions, then, by the curse of dimensionality, one will parameterize each of these functions with a set of parameters such as coefficients of linear/logistic regression models. The causal graph can involve unmeasured variables: that is, A, Y or X1, . . . , Xm can be subject to missingness or (right-)censoring. In this case one views the causal graph as a set of assumptions on the full-data random vector being the collection of nodes in the causal graph: thus, in this case the causal graph does not make any assumptions about the conditional distribution of censoring/missingness variables, given the full data X<sup>F ULL</sup> ≡ (X1, . . . , Xm, A, Y ). Specifying the whole DAG is usually hard in practice. Given such a DAG it is now possible to identify a causal effect of one node on another node in the graph from the distribution/density of the full-data X<sup>F ULL</sup> = (X1, . . . , Xm), A, Y . In addition, if the observed data is O = Φ(C, X<sup>F ULL</sup> ) for some known function Φ of a censoring variable C and X<sup>F ULL</sup> (this is the most general definition of a censored/missing data structure), and one assumes that the conditional distribution of C, given X<sup>F ULL</sup> , satisfies coarsening at random (see e.g., van der Laan, Robins, 2002, for literature overview and definitions), then one can often identify from the observed data distribution the full data distribution X<sup>F ULL</sup> , and thereby the wished causal effects. To understand what variables in the graph can be completely missing (i.e., they are not observed on any subject in the sample) while still having coarsening at random and (thereby) identification of the wished causal effect is an interesting problem, and area of research.

In class we we will present an alternative counterfactual approach exists that does not require full specification of a causal graph, but, does only require knowing which variables are pre-treatment, but does also need to assume that there are no unmeasured confounders.

Once we have the causal graph we can identify from the distribution of X<sup>F ULL</sup> the counterfactual distribution P (Ya = y) which is the marginal distr. of Y when treatment is set at level A = a. If the interest is only in the effect of A on Y , all covariates connected to A only through an undirected path that includes Y should be ignored. One important issue in the study of causal graphs is what’s the minimal subset of covariates that is sufficient to identify the counterfactual distribution of Ya; related to this is the question of what’s the minimal set of confounders that needs to be stratified upon in a point treatment study.

**Definition 2.** A set of edges connecting two vertices A and Y is called a back-door path if ∃X s.t. X ∈ PA (A) and there is a undirected path between X and Y . A vertex in a back-door path is called a collider if the path edges incident with this vertex are incoming (i.e. having their direction towards the vertex). A confounding between A and Y is present if ∃a back-door path with no colliders connecting A and Y .

For example, there are two back-door paths present in fig. 1 - A → X1 → Y and A → X2 → X3 → Y .

3

How to find the likelihood of the data given a causal graph? Using the chain rule for factoring the joint likelihood of discrete R.V. (Z1, Z2, . . . , Zd):


together with the conditional dependence between variables implied by the causal graph P (Zi|Z1, . . . , Zi−1) = P (Zi|PA(Zi)), we obtain:


When applying this to a single observation in a point-treatment study with discrete R.V. (X1, X2, . . . , Xm, A, Y ) we obtain:


Assuming that each of the functional relationships in definition 1 is parameterized as a (e.g., linear) regression in the parent nodes with known (or up till a finite dimensional parameter) conditional distribution of the error-term, given the parent-nodes, we can express the joint probability in 2 as a function of an unknown parameter vector (e.g., the collection of node-specific regression coefficients), which represents now a parametric model and for the density/likelihood of X<sup>F ULL</sup> .

One can estimate the unknown parameters with the maximum likelihood estimator obtained by maximizing the likelihood<sup>�n</sup> i=1<sup>P(XF ULL= xF ULL</sup> i ) of an observed sample x<sup>F ULL</sup> i , i = 1, . . . , n. Typically, this can be carried out with standard software (e.g. implementations of generalized linear regression).

Given the causal graph and its estimated functional relations, one can now define the distribution of Ya as the distribution one obtains by fixing the treatment variable A = a in the system of equations defined by the node-specific equations, and generating all nodes accordingly.

**Example 1.** The causal graph in this example is specified in fig. 2.


Figure 2. Another example of a causal graph with three covariates.

Assuming continuous distr. for all R.V in the causal graph, the density for a single observation can be written as follows:

(3) f (X1, X2, X3, A, Y ) = f (X3) f (A|X3) f (X2|A) f (Y |A, X1, X3) f (X1|A) . Now let’s find the counterfactual distribution for A = a:

4

- (1) Erase f (A|PA (A)) from 3. This is equivalent to performing an incision to the graph in fig. 2 that removes both vertex A and the edges incident to A (fig. 3);

- (2) Set A = a in all functions where A belongs to the parents’ set;

- (3) Define fa (X1, X2, X3, Y ) = f (X3) f (X2|A = a) f (Y |A = a, X1, X3) f (X1|A = a) ; (4) Integrate out X1, X2 and X3 in fa (X1, X2, X3, Y ) to get the counterfactual density fa (Y ).


Figure 3. Graph from example 1 after incision of A.

**Example 2.** This is how Pearl defined the counterfactual probability distribution fa (Y ). Hence, if A has two levels - treatment (a = 1) and control (a = 0), and the causal parameter (or effect) of interest is the treatment difference, one needs to calculate the quantity Ef1 (Y ) − Ef0 (Y ).

The above method for doing causal inference can be summarized as follows. Using standard software we can do maximum likelihood estimation to fit the functional forms of each node in the causal graph, thus estimating the parameters in each functional relationships in def. 1. Subsequently, given the maximum likelihood estimator of the unknown parameters, we can identify corresponding estimates of the treatment specific disstribution of (Ya, X1a, . . . , Xma) by Monte-Carlo simulation for each choice of treatment level a.

If the functions in def. 1 are parameterized using flexible regression functions, one can employ dataadaptive model selection methods such as cross-validation or penalized likelihood methods. Such methods provide tools to decide data adaptively how flexible the parametrization should be. Clearly, if the number of parameters is larger than the sample size n, then the maximum likelihood estimator of the unknown parameter vector becomes too variable or ill defined, and thereby our estimate of the treatment specific distribution is too variable as well. That is, the size/dimension/complexity of the model needs to be data dependent. An important research area is the development of methods which data adaptively selects models for the purpose of estimating a particular parameter (such as in our case, the causal effect of treatment on the outcome Y ) of interest.

To estimate the variability of the estimates of the causal parameters, (non-) parametric bootstrap is usually employed. This involves resampling repeatedly n observations from the actual sample (nonparametric bootstrap) or from a fit of the true probability distribution of the data (parametric bootstrap).

Is it possible to make a choice between different causal graphs based exclusively on the data from a study? Short answer is, “No”. Consider a simple causal graph with 2 R.V. X1, X2, where the true causal graph and data generating distribution is: X1 → X2, X1 ∼ N �µ1, σ1<sup>2</sup> � and X2 = X1 + c. If we would choose between the only two possible causal graphs X1 → X2 and X1 ← X2 the one with the largest corresponding fitted likelihood (with the second model assuming X1 = X2 + c′, X2 ∼ N �µ2, σ2<sup>2</sup> �, and µ2, σ2 estimated from the data generated using the true data distribution) we’ll get that approximately 50% of the time we pick the wrong causal graph. In general, if all nodes (A, Y, X1, . . . , Xm) are discrete valued, then all possible causal graphs of X<sup>F ULL</sup> give the same corresponding fitted maximum likelihood estimate of the distribution of

5

X<sup>F ULL</sup> , if we use for all causal graphs the nonparametric model (that is, do not assume any parametric form for the functional relations). In this case, the causal-graph specific maximum likelihood is completely flat in the choice of causal graph. Consequently, any variability in the causal-graph specific maximum likelihood values across causal-graphs is NOT due to changes in the causal graphs, but it is due to the fact that different parametrized causal graphs result in different statistical models for X<sup>F ULL</sup> , and one might approximate the true distribution of X<sup>F ULL</sup> better than another. For example, if in truth X1 → X2, and the conditional mean of X1, given X2 happens to be linear in X2, then a wrong causal graph X2 → X1 with corresponding linear normal regression assumption X1 ∼ N (betaX2, σ<sup>2</sup> ), will likely give a higher maximum likelihood value then a correct causal graph X1 → X2 with corresponding assumption X2 is exponential with λ(X1) = βX1.

---

[← 3. What is the parameter of interest in causal inference?](06-3-what-is-the-parameter-of-interest-in-causal-inference.md) · [Up: contents](index.md) · [Lecture of September 8, 2004 →](08-lecture-of-september-8-2004.md)
