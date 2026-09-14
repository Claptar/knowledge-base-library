---
title: Inference on the Order of a Normal Mixture
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/chenMixtExample.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/section/chenMixtExample.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Inference on the Order of a Normal Mixture

**Source:** [`section/chenMixtExample.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/chenMixtExample.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
Jiahua Chen a , Pengfei Li b & Yuejiao Fu c
```

```
a Department of Statistics, University of British Columbia, Vancouver, BC, Canada, V6T 1Z2
b Department of Statistics and Actuarial Sciences, University of Waterloo, Waterloo, ON,
Canada, N2L 3G1
```

```
c Department of Mathematics and Statistics, York University, Toronto, ON, Canada, M3J 1P3
Accepted author version posted online: 04 Jun 2012.Version of record first published: 08 Oct
2012.
```

```
To cite this article: Jiahua Chen, Pengfei Li & Yuejiao Fu (2012): Inference on the Order of a Normal Mixture, Journal of the
American Statistical Association, 107:499, 1096-1105
```

```
To link to this article: http://dx.doi.org/10.1080/01621459.2012.695668
```

#### `PLEASE SCROLL DOWN FOR ARTICLE`

```
Full terms and conditions of use: http://amstat.tandfonline.com/page/terms-and-conditions
```

```
This article may be used for research, teaching, and private study purposes. Any substantial or systematic
reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to
anyone is expressly forbidden.
```

```
The publisher does not give any warranty express or implied or make any representation that the contents
will be complete or accurate or up to date. The accuracy of any instructions, formulae, and drug doses should
be independently verified with primary sources. The publisher shall not be liable for any loss, actions, claims,
proceedings, demand, or costs or damages whatsoever or howsoever caused arising directly or indirectly in
connection with or arising out of the use of this material.
```

_Supplementary materials for this article are available online. Please go to www.tandfonline.com/r/JASA_


# **Inference on the Order of a Normal Mixture**

### _Jiahua CHEN, Pengfei LI, and Yuejiao FU_

Finite normal mixture models are used in a wide range of applications. Hypothesis testing on the order of the normal mixture is an important yet unsolved problem. Existing procedures often lack a rigorous theoretical foundation. Many are also hard to implement numerically. In this article, we develop a new method to fill the void in this important area. An effective expectation-maximization (EM) test is invented for testing the null hypothesis of arbitrary order _m_ 0 under a finite normal mixture model. For any positive integer _m_ 0 ≥ 2, the limiting distribution of the proposed test statistic is _χ_ 2<sup>2</sup> _m_ 0<sup>.Wealsouseanovelcomputerexperimenttoprovideempiricalformulasforthetuning</sup> parameter selection. The finite sample performance of the test is examined through simulation studies. Real-data examples are provided. The procedure has been implemented in R code. The _p_ -values for testing the null order of _m_ 0 = 2 or _m_ 0 = 3 can be calculated with a single command. This article has supplementary materials available online.

KEY WORDS: Chi-squared limiting distribution; Computer experiment; EM test; Likelihood ratio test; Order selection; Tuning parameter; Unequal variance.

#### _1. INTRODUCTION_

Normal mixture models have been used for a wide range of scientific investigations. The number of components in, or the order of, the finite normal mixture model often has important scientific implications; see chapter 6 of McLachlan and Peel (2000). Hypothesis testing for the order of a normal mixture is an important problem. The order under null hypothesis is often proposed to represent some default proposition with scientific significance; the rejection of which usually leads to propositions of greater interest. We give two motivating examples as follows.

_Example 1._ Finite normal mixture is often used to assess the impact of possible underlying genotypes that display continuous or quantitative variation in the population (Schork, Allison, and Thiel 1996; McLachlan and Peel 2000). If the phenotype or quantitative trait is mainly influenced by a gene with two alleles _A_ and _a_ , there are three possible genotypes that an individual can possess: _AA_ , _Aa_ , and _aa_ . Suppose the trait values associated with individuals possessing _AA_ , _Aa_ , and _aa_ are distributed as _N_ ( _θ_ 1 _, σ_ 1<sup>2),</sup><sup>_N_(</sup><sup>_θ_2</sup><sup>_, σ_</sup> 2<sup>2),and</sup><sup>_N_(</sup><sup>_θ_3</sup><sup>_, σ_</sup> 3<sup>2),respectively.</sup> Then, the population quantitative trait has a three-component normal mixture distribution


where _α_ 1, _α_ 2, and _α_ 3 are the proportions of individuals possessing the genotypes _AA_ , _Aa_ , and _aa_ , respectively. A competing genetic model arises when the genotypes _AA_ and _Aa_ have the same phenotypes; this leads to a two-component normal mixture model. See Roeder (1994) for a genetic example on sodium-lithium countertransport (SLC) activity in red blood cells.

Jiahua Chen is Professor, Department of Statistics, University of British Columbia, Vancouver, BC, Canada V6T 1Z2 (E-mail: _jhchen@stat.ubc.ca_ ). Pengfei Li is Assistant Professor, Department of Statistics and Actuarial Sciences, University of Waterloo, Waterloo, ON, Canada N2L 3G1 (E-mail: _pengfei.li@uwaterloo.ca_ ). Yuejiao Fu is Associate Professor, Department of Mathematics and Statistics, York University, Toronto, ON, Canada M3J 1P3 (E-mail: _yuejiao@mathstat.yorku.ca_ ). The authors thank the editor, the associate editor, and three referees for constructive comments and suggestions that lead to significant improvements in the article. The research is supported by the Natural Sciences and Engineering Research Council of Canada and by a start-up grant from the University of Waterloo.

Geneticists may suspect the existence of a major gene and if it exists, whether or not it is dominant. They may also want to know whether or not the quantitative trait is actually affected by several genes (Schork, Allison, and Thiel 1996). The above questions can be addressed through hypothesis tests. The null order of 1 represents the default proposition that the suspected gene does not exist; the rejection of this supports the existence of a major gene. Another null order could be 2; rejection suggests that the gene is not dominant. The rejection of a null order of 3 or less suggests the existence of several relevant genes.

_Example 2._ Miloslavsky and van der Laan (2003) and Pavlic, Brand, and Cummings (2001) provided an example where a normal mixture model is used to describe the observed change in the characteristic of interest in treated patients. It is suspected that the treatment has no effect on a subgroup of the patients. At the same time, one or more groups potentially respond to the treatment differentially.

The questions of interest include whether the nonresponsive group really exists; if yes, whether the people in this group respond to the treatment in a homogeneous way. The latter information will be useful to estimate the proportion of the nonresponsive group, which is of clinical importance. Again these questions can be addressed by hypothesis tests. A null order of 1 represents the nonexistence of nonresponsive groups and a null order of 2 implies that the responsive subgroup is homogeneous.

Designing effective hypothesis test methods for the order of finite mixture models goes back to Hartigan (1985) and Ghosh and Sen (1985). Both investigated the use of a likelihood ratio test for a null hypothesis of order 1, namely homogeneity. The former article reveals the impact of nonregularity of the mixture models, and the latter gives the limiting distribution of the likelihood ratio test statistic under a separation condition. Chernoff and Lander (1995) obtained the limiting distribution of the likelihood ratio test statistic for homogeneity under a binomial mixture model without separation conditions. DacunhaCastelle and Gassiat (1999) and Liu and Shao (2003) obtained

**© 2012 American Statistical Association Journal of the American Statistical Association September 2012, Vol. 107, No. 499, Theory and Methods DOI: 10.1080/01621459.2012.695668**

**1096**

_Chen, Li, and Fu: Inference on the Order of a Normal Mixture_

_1097_

the limiting distribution of the likelihood ratio test statistic for general-order null hypotheses under a compact parameter space and other assumptions. However, their elegant theoretical results are not applicable to finite normal mixture models because of the violation of several crucial conditions. Under the normal mixture model, the likelihood function is unbounded (Hathaway 1985), the Fisher information on mixing proportion can be infinity (Chen and Li 2009), and the model is not strongly identifiable (Chen 1995). Charnigo and Sun (2004) developed a D-test for homogeneity. Li and Chen (2010) developed an expectationmaximization (EM) test for assessing the order of finite mixture models with single-parameter component distributions. It is effective and easy to use for Poisson mixture models or for normal mixture models with known component variance.

Chen and Chen (2003) obtained a specific result for the likelihood ratio test under an unknown but equal component variance finite normal mixture model for homogeneity. Yet the stochastic limiting distribution is hard to implement in applications. Lo, Mendell, and Rubin (2001) aimed to develop a general theory that can be used to test the number of components (or the order) in finite normal mixture models. However, Jeffries (2003) observed that the conditions required by Lo, Mendell, and Rubin (2001) are generally not met when the null hypothesis holds. Therefore, their result is not proven and may be incorrect, according to Jeffries (2003). McLachlan (1987) proposed a resampling approach to the assessment of the _p_ -value of the likelihood ratio test in testing the number of components. The idea cannot be directly applied to finite normal mixture models because of the unbounded likelihood function. The method in Chen and Li (2009) is applicable only to the test of homogeneity in normal mixture models.

In sharp contrast to the hypothesis test, there have been important developments on the order selection procedure for estimating the order of normal mixture model; see Leroux (1992); Richardson and Green (1997); Keribin (2000); Ishwaran, James, and Sun (2001); James, Priebe, and Marchette (2001); Miloslavsky and van der Laan (2003); Woo and Sriram (2006); and Chen and Khalili (2008).

In general, order selection procedures search for a simple model that adequately describes the real world. Hypothesis test is used to check the validity of scientific claims. For instance, an insurance company may be interested in dividing drivers into homogeneous subgroups to device a most profitable insurance product for each group. Thus, searching for the most suitable number of subgroups is the problem of interest. It fits perfectly into the order selection framework. In Examples 1 and 2, the order is linked to scientific propositions. In this case, conclusion of the hypothesis test on the order of the mixture model has direct scientific interpretations. It fits perfectly into the hypothesis test framework.

In summary, testing the order of the finite normal mixture model is an important yet arguably unsolved problem. In this article, we propose a new likelihood-based EM test for the order of finite normal mixture models. The new method first applies a penalty function on the component variance to obtain a bounded penalized likelihood. It then assesses the improvement of prespecified higher-order models over the null models. By tactically placing these higher-order models and using the EM iteration, the new method quickly locates the direction and degree of im-

provements in terms of the penalized likelihood. The evidence against the null order is hence assessed and quantified. We show that the new test statistic has a simple chi-squared limiting distribution. The penalty function contains a tuning parameter that affects the precision of the test. We solve the tuning problem via a novel computer experiment and provide an easy-to-use data-dependent formula. Simulation results show that the new method has accurate Type I errors and adequate power. Software implementing the test has been developed in the R language (R Development Core Team 2008) and is available as the online supplementary materials.

The organization of the article is as follows. In Section 2, we set up the testing problem, introduce the new EM test procedure, and present asymptotic results. In Section 3, we give empirical formulas for the tuning parameter through designed computer experiments. The simulation results are presented in Section 4, and the application examples are in Section 5. Section 6 presents a discussion, and the proofs are given in the online supplementary materials.

#### _2. TEST FOR THE ORDER OF A NORMAL MIXTURE MODEL_

Let _f_ ( _x_ ; _θ, σ_ ) be the normal density function with mean _θ_ and variance _σ_<sup>2</sup> . The finite normal mixture model with order _m_ has density function


where the _αh_ ’s are the mixing proportions with<sup>�</sup><sup>_m_</sup> _h_ =1<sup>_αh_= 1,</sup> the _θh_ ’s and _σh_ ’s are component parameters, and _�_ is called the mixing (or latent) distribution and takes the form


Here _I_ (·) is the indicator function. Suppose we have a random sample _X_ 1 _, . . . , Xn_ of size _n_ from the above normal mixture model. The goal of this article is to develop an effective procedure for testing the following null and alternative hypotheses:


for some given positive integer _m_ 0. The true order of a finite mixture model is defined as the smallest number of components such that all component densities are different and all mixing proportions are nonzero. We restrict our attention to the most practical situation where all the component mean parameters are different. The testing problem where two normal mixture components have the same mean is less interesting in applications but more challenging technically. Our asymptotic result is applicable only to finite normal mixture models with distinct component means.

One hypothesis test problem of Example 1 is to test _H_ 0 : _m_ = 2 versus _H_ A : _m_ = 3 under normal mixture models. Our new method designed for _H_ 0 : _m_ = 2 versus _H_ A : _m >_ 2 is still applicable and effective. A more powerful test tailor-made specifically for _H_ 0 : _m_ = 2 versus _H_ A : _m_ = 3 could be possible, but we are not aware of any such methods in the literature.

_Journal of the American Statistical Association, September 2012_

_1098_

#### _2.1 The New EM Test Statistic_

We start by constructing a likelihood-based consistent estimator _�_<sup>ˆ</sup> 0 of the mixing distribution under the null hypothesis. Given a random sample, the log-likelihood function of the mixing distribution is


This likelihood function diverges to positive infinity when some component variance goes to 0. Thus, the maximum likelihood estimator of _�_ is known to be inconsistent. This is a crucial difference between the finite normal mixture model and other finite nonnormal mixture models. To overcome this technical difficulty, a penalty function is often introduced. Let _X_ ¯ = _n_<sup>−1 �</sup><sup>_n_</sup> _i_ =1<sup>_Xi_and</sup><sup>_s_</sup> _n_<sup>2=</sup><sup>_n_−1 �</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_Xi_−</sup><sup>_X_¯)2. Define</sup>


for some _σ_ ˆ<sup>2</sup> -dependent smooth penalty function _pn_ ( _σ_<sup>2</sup> ; _σ_ ˆ<sup>2</sup> ) of _σ_<sup>2</sup> , so that it goes to negative infinity when _σ_ goes to either 0 or infinity. Let _�_<sup>ˆ</sup> 0 be the maximum point of _ℓn_ ( _�_ ) under the null hypothesis. According to Chen, Tan, and Zhang (2008), _�_<sup>ˆ</sup> 0 is a consistent estimator of _�_ under _H_ 0, with some mild conditions on _pn_ (·; ·). One recommended choice is


We use _an_ = 1 _/n_ to obtain _�_<sup>ˆ</sup> 0 and this choice satisfies the conditions in Chen, Tan, and Zhang (2008).

In principle, one could compute the maximum point _�_<sup>ˆ</sup> A of _ℓn_ ( _�_ ) under the alternative model, and construct a penalized likelihood ratio test statistic 2{ _ℓn_ ( _�_<sup>ˆ</sup> A) − _ℓn_ ( _�_<sup>ˆ</sup> 0)} for the purpose of testing the order. This approach does not work as expected for several reasons. First, it is technically challenging to find its finite sample or limiting distributions. Second, because the Fisher information with respect to the mixing proportion can be infinity (Chen and Li 2009), the limiting distribution may not even exist.

To overcome these difficulties, we introduce a new EM test. The test statistic has to be defined in several steps that may appear complex and unmotivated. With the help of the computer software, the actual data analysis is simple. In particular, the test statistic has a simple limiting distribution that is essential for obtaining the _p_ -value. We will explain the motivation behind each step after the statistic is completely defined.

Let _θ_<sup>ˆ</sup> 0 _h_ and _σ_ ˆ0 _h_ be the constituent entries of _�_<sup>ˆ</sup> 0 defined earlier. Without loss of generality, assume _θ_<sup>ˆ</sup> 01 ≤ _θ_<sup>ˆ</sup> 02 ≤· · · ≤ _θ_<sup>ˆ</sup> 0 _m_ 0 . We first give the four key ingredients of the EM test.

The first ingredient is _m_ 0 intervals defined as _Ih_ = ( _ηh_ −1 _, ηh_ ], _h_ = 1 _, . . . , m_ 0, where _η_ 0 = −∞, _ηm_ 0 = ∞, and _ηh_ = ( _θ_<sup>ˆ</sup> 0 _h_ + _θ_ ˆ0 _h_ +1) _/_ 2, _h_ = 1 _, . . . , m_ 0 − 1.

The second ingredient is a special class of mixing distributions of order 2 _m_ 0 defined as


for some vector **_β_** = ( _β_ 1 _, . . . , βm_ 0 )<sup>_τ_</sup> such that _βh_ ∈ (0 _,_ 0 _._ 5]. The third ingredient is a modified penalized likelihood function defined on _�_ 2 _m_ 0 ( **_β_** ):

_pln_ ( _�_ ) = _ln_ ( _�_ )


where _pn_ ( _σ_<sup>2</sup> _, σ_ ˆ<sup>2</sup> ) was defined earlier, and _p_ ( _β_ ) will be chosen as a unimodal continuous function that goes to −∞ when _β_ goes to 0. We recommend _p_ ( _β_ ) = log(1 −|1 − 2 _β_ |). Note that the penalty term _pn_ ( _σh_<sup>2;</sup><sup>_σ_ˆ</sup> 0<sup>2</sup> _h_<sup>) depends on</sup><sup>_�_ˆ0, and prevents</sup><sup>_ln_(</sup><sup>_�_)</sup> from attaining its maximum value at mixing distributions with some _σh_<sup>2= 0. Further, the level of penalty,</sup><sup>_an_, in</sup><sup>_pn_(</sup><sup>_σ_</sup> _h_<sup>2;</sup><sup>_σ_ˆ</sup> 0<sup>2</sup> _h_<sup>) will</sup> be experimentally tuned so that the related statistical procedures have desirable properties. This issue will be discussed in detail in Section 3. To clarify, the _an_ value used to get _�_<sup>ˆ</sup> 0 is not tuned because it leads to a sufficiently accurate _�_<sup>ˆ</sup> 0 for our purpose.

The fourth ingredient is a finite set of numbers from (0 _,_ 0 _._ 5], denoted by _B_ . For example, _B_ = {0 _._ 1 _,_ 0 _._ 3 _,_ 0 _._ 5}. If _B_ contains _J_ elements, then _B_<sup>_m_0</sup> contains _J_<sup>_m_0</sup> vectors of **_β_** . For each **_β_** 0 ∈ _B_<sup>_m_0</sup> , we compute


where the maximization is with respect to **_α_** = ( _α_ 1 _, . . . , αm_ 0)<sup>_τ_</sup> _,_ **_θ_** 1 = ( _θ_ 11 _, . . . , θ_ 1 _m_ 0 )<sup>_τ_</sup> , **_θ_** 2 = ( _θ_ 21 _, . . . , θ_ 2 _m_ 0 )<sup>_τ_</sup> , **_σ_** 1 = ( _σ_ 11 _, . . . , σ_ 1 _m_ 0 )<sup>_τ_</sup> , and **_σ_** 2 = ( _σ_ 21 _, . . . , σ_ 2 _m_ 0 )<sup>_τ_</sup> . The EM algorithm with multiple initial values are used to search for _�_<sup>(1)</sup> ( **_β_** 0). Note that _�_<sup>(1)</sup> ( **_β_** 0) is a member of _�_ 2 _m_ 0 ( **_β_** 0). When all the four ingredients are ready, the EM iteration leads to the EM test as follows. Let **_β_**<sup>(1)</sup> = **_β_** 0. Suppose we have _�_<sup>(</sup><sup>_k_)</sup> ( **_β_** 0) already calculated with **_α_**<sup>(</sup><sup>_k_)</sup> , **_θ_**<sup>(</sup> 1<sup>_k_),</sup><sup>**_θ_**(</sup> 2<sup>_k_),</sup><sup>**_σ_**(</sup> 1<sup>_k_),</sup><sup>**_σ_**(</sup> 2<sup>_k_),and</sup> **_β_**<sup>(</sup><sup>_k_)</sup> available. The calculation for _k_ = 1 has been illustrated with **_α_**<sup>(1)</sup> , **_θ_**<sup>(1)</sup> 1<sup>,</sup><sup>**_θ_**(1)</sup> 2<sup>,</sup><sup>**_σ_**(1)</sup> 1<sup>,</sup><sup>**_σ_**(1)</sup> 2<sup>, and</sup><sup>**_β_**(1) being constituent entities</sup> of _�_<sup>(1)</sup> ( **_β_** 0). A more appropriate notation might be


For simplicity, we use the compact notation _�_<sup>(1)</sup> ( **_β_** 0) and more generally, _�_<sup>(</sup><sup>_k_)</sup> ( **_β_** 0).

For each _i_ = 1 _, . . . , n_ and _h_ = 1 _, . . . , m_ 0, let


and

We then proceed to obtain _�_<sup>(</sup><sup>_k_+1)</sup> ( **_β_** 0) by setting


_Chen, Li, and Fu: Inference on the Order of a Normal Mixture_

_1099_

and


The computation is iterated a prespecified number of times, _K_ . For each **_β_** 0 ∈ _B_<sup>_m_0</sup> and _k_ , we define


The retooled EM test statistic, for a prespecified _K_ , is then defined to be

The new EM test rejects the null hypothesis when EM _n_<sup>(</sup><sup>_K_)</sup> exceeds some critical value.

We now give the motivation behind the complex definition. In the usual likelihood ratio test, the likelihood will be maximized over the whole parameter space. The degree of improvement in the log-likelihood value over the best possible null model is used for the test. The literature tells us that such a statistic has complex stochastic behavior even in simple situations (DacunhaCastelle and Gassiat 1999; Liu and Shao 2003). Based on this observation, our first two ingredients confine the primary candidate alternative models to a relatively simple subset of mixing distributions _�_ 2 _m_ 0 ( **_β_** ). The optimal mixing distribution within _�_ 2 _m_ 0 ( **_β_** 0) has simple asymptotic properties when the null hypothesis is true for any fixed **_β_** 0. This leads to _Mn_<sup>(1)(</sup><sup>**_β_**</sup> 0<sup>), which</sup> also has a simple limiting distribution. In principle, _Mn_<sup>(1)(</sup><sup>**_β_**</sup> 0<sup>)</sup> can be directly used for testing the order of the finite normal mixture model.

However, _Mn_<sup>(1)(</sup><sup>**_β_**</sup> 0<sup>) is overly dependent on an arbitrary choice</sup> of **_β_** 0. This leads to the fourth ingredient, _B_<sup>_m_0</sup> , which contains a number of **_β_** vectors that fill the space evenly. Hence, EM<sup>(1)</sup> _n_ measures the amount of improvement in the log-likelihood over many representative alternative models. Any specific alternative model is likely reasonably approximated by one mixing distribution in ∪{ _�_ 2 _m_ 0 ( **_β_** ) : **_β_** ∈ _B_<sup>_m_0</sup> }.

The EM iteration further expands the range of alternative models being investigated. It checks the amount of possible further improvement in the log-likelihood from a few iterations. With the help of the third ingredient, the simple limiting distribution of EM<sup>(1)</sup> _n_<sup>is not destroyed by a finite number of iterations.</sup> Thus, we obtain a new test that is highly effective yet simple to implement.

#### _2.2 Asymptotic Distribution_

The asymptotic distribution of EM<sup>(</sup> _n_<sup>_K_)</sup> is obtained with the careful choice of two penalty functions _p_ ( _β_ ) and _pn_ (·; ·):

- C 1. _p_ ( _β_ ) is a continuous function such that it is maximized at _β_ = 0 _._ 5 and goes to negative infinity as _β_ goes to 0 or 1. Further, _p_ (0 _._ 5) = 0.

- C 2. For any given _σ_ 2<sup>2</sup><sup>_>_0,</sup><sup>_pn_(</sup><sup>_σ_</sup> 1<sup>2;</sup><sup>_σ_</sup> 2<sup>2) is a smooth function of</sup> _σ_ 1<sup>2and is maximized at</sup><sup>_σ_</sup> 1<sup>2=</sup><sup>_σ_</sup> 2<sup>2. Further,</sup><sup>_pn_(</sup><sup>_σ_</sup> 2<sup>2;</sup><sup>_σ_</sup> 2<sup>2) = 0.</sup>

- C 3. For any given _σ_ 1<sup>2</sup><sup>_>_0 and</sup><sup>_σ_</sup> 2<sup>2</sup><sup>_>_0,</sup><sup>_pn_(</sup><sup>_σ_</sup> 1<sup>2;</sup><sup>_σ_</sup> 2<sup>2) =</sup><sup>_o_(</sup><sup>_n_).</sup> C 4. For any given _σ_ 2<sup>2</sup><sup>_>_0,thereexistsa</sup><sup>_c >_0suchthat</sup> _pn_ ( _σ_ 1<sup>2;</sup><sup>_σ_</sup> 2<sup>2) ≤4(log</sup><sup>_n_)2 log(</sup><sup>_σ_1),when</sup><sup>_σ_1≤</sup><sup>_c/n_and</sup><sup>_n_is</sup> large.

- C 5. For any given _σ_ 1<sup>2</sup><sup>_>_0 and</sup><sup>_σ_</sup> 2<sup>2</sup><sup>_>_0,</sup><sup>_p_</sup> _n_<sup>′(</sup><sup>_σ_</sup> 1<sup>2;</sup><sup>_σ_</sup> 2<sup>2) =</sup><sup>_op_(</sup><sup>_n_1</sup><sup>_/_4).</sup> Here, _pn_<sup>′(</sup><sup>_σ_</sup> 1<sup>2;</sup><sup>_σ_</sup> 2<sup>2)isthepartialderivativeof</sup><sup>_pn_(</sup><sup>_σ_</sup> 1<sup>2;</sup><sup>_σ_</sup> 2<sup>2)</sup> with respect to _σ_ 1<sup>2.</sup>

Examples of functions satisfying the above mathematical conditions were given earlier. Since the user has the freedom to choose the penalty functions, these conditions are not restrictive as long as such functions exist. The utility of _p_ ( _β_ ) is to restore some level of identifiability to finite mixture models. The penalty _pn_ ( _σ_<sup>2</sup> ; _σ_ ˆ<sup>2</sup> ) prevents fitted mixing distributions with degenerate component variances. Conditions C2−C4 make _�_<sup>ˆ</sup> 0 a consistent estimator of _�_ as shown by Chen, Tan, and Zhang (2008). Condition C5 allows a particularly simple limiting distribution to be presented below. Its proof is given in the online supplementary materials.

_Theorem 1._ Let EM<sup>(</sup> _n_<sup>_K_)</sup> be defined as in (3) based on a random sample of size _n_ from the finite normal mixture model (1). Assume that the penalty functions in the definition of EM<sup>(</sup> _n_<sup>_K_)</sup> satisfy C1–C5, and the set _B_ in the definition of EM<sup>(</sup> _n_<sup>_K_)</sup> contains the real number 0 _._ 5. Under the null hypothesis _H_ 0 (2) that the order of the finite normal mixture model _m_ = _m_ 0 and for any fixed finite positive integer _K_ ,


in distribution as the sample size _n_ →∞.

The definition of EM<sup>(</sup> _n_<sup>_K_)</sup> involves a few tuning parameters; they must be determined for each application. In the next section, we give some recommendations based on experience and computer experiments. The results are implemented in the R code so that an approximate _p_ -value and other statistics can be obtained with a single command. The code is also given in the online supplementary materials.

#### _3. PENALTY FUNCTION RECOMMENDATIONS_

To apply the EM test, we must specify the set _B_ , the number of iterations _K_ , and the penalty functions _p_ ( _β_ ) and _pn_ ( _σ_<sup>2</sup> ; _σ_ ˆ<sup>2</sup> ). Based on our experience, we recommend choosing _B_ = {0 _._ 1 _,_ 0 _._ 3 _,_ 0 _._ 5}, _K_ = 3, and _p_ ( _β_ ) = log(1 −|1 − 2 _β_ |). For the penalty function _pn_ ( _σ_<sup>2</sup> ; _σ_ ˆ<sup>2</sup> ), we recommend


This function satisfies Conditions C2–C5 when _an_ = _op_ ( _n_<sup>1</sup><sup>_/_4</sup> ). That is, any choice of _an_ of this order does not change the first-order asymptotic property given in Theorem 1. Tuning _an_ further for computing _�_<sup>(</sup><sup>_K_)</sup> ( **_β_** 0) improves the precision of the level of the EM test.

In the spirit of the Bartlett correction (Bartlett 1953), we wish to choose the value of _an_ such that


when the sample is from a null model. This can be challenging or even impossible because _an_ may depend on the unknown distribution of the sample. Instead, we develop through computer experiments an empirical formula for _an_ based on the sample size, the data, and the null hypothesis, so that _E_ {EM<sup>(</sup> _n_<sup>_K_)}and</sup> 2 _m_ 0 are close.

Given a mixing distribution _�_ 0 and a sample size, we simulate the value of _E_ {EM<sup>(</sup> _n_<sup>_K_)}asafunctionof</sup><sup>_an_andfindthevalue</sup>

_Journal of the American Statistical Association, September 2012_

_1100_

_a_ ˆ _n_ that solves _E_ {EM<sup>(</sup> _n_<sup>_K_)} = 2</sup><sup>_m_0.Weregard</sup><sup>_a_ˆ</sup><sup>_n_oritsfunction</sup> as a dependent variable and ( _n, �_ 0) as explanatory variables. Through exploratory data analysis, we build a regression model between _a_ ˆ _n_ and some covariates based on ( _n, �_ 0). We therefore obtain an empirical formula in the form of


In applications, we first compute _�_<sup>ˆ</sup> 0 and then choose a tuning parameter according to _an_ = _g_ ( _n, �_<sup>ˆ</sup> 0) for the EM test.

We present the results of the computer experiments for the two most important cases, _m_ 0 = 2 and _m_ 0 = 3, in the following two subsections. They cover most application examples we are aware of in the literature, including those given in Section 1. If necessary, formulas can be obtained for _m_ 0 = 4 or higher in the same way. Although the tuning formulas are obtained via deliberate computer experiments and careful design, their application is no more complex than a few lines of R code.

#### _3.1 Empirical Formulas for an With m 0_ = _2_

We carry out pilot experiments for many choices of representative normal mixture models of order _m_ 0 = 2. We find that when _an >_ 0 _._ 35, the averages of the EM test are smaller than 2 _m_ 0 = 4. For the designed experiment, we choose three levels for the sample size _n_ : 100, 300, 500; two levels for the mixing proportions: ( _α_ 1 _, α_ 2) = (0 _._ 25 _,_ 0 _._ 75) _,_ (0 _._ 5 _,_ 0 _._ 5); three levels for the component means: ( _θ_ 1 _, θ_ 2) = (−1 _._ 5 _,_ 1 _._ 5) _,_ (−2 _,_ 2) _,_ (−2 _._ 5 _,_ 2 _._ 5); and two levels for the component variances: ( _σ_ 1 _, σ_ 2) = (1 _,_ 1) _,_ (1 _._ 5 _,_ 0 _._ 75). A full factorial design with 3 × 2 × 3 × 2 = 36 level combinations is implemented. We use 1000 repetitions at each level combination to obtain _a_ ˆ _n_ . The results are reported in Table 1.

We transform _a_ ˆ _n_ into _y_ = log{ _a_ ˆ _n/_ (0 _._ 35 − _a_ ˆ _n_ )} to restrict the fitted value of _an_ to the interval (0, 0.35). We then search for sensible functions of _n_ and _�_ 0 to serve as covariates. It turns out that _n_<sup>−1</sup> and the average misclassification rate _ω_ 12 discussed by Maitra and Melnykov (2010) are good choices. Based on a two-component normal mixture model, an observation _X_ from component 2 is misclassified into component 1 with probability


Similarly, let _ω_ 2|1 be the opposite misclassification rate and _ω_ 12 be the average misclassification rate. Regressing _y_ with respect to the covariates _n_<sup>−1</sup> and _ω_ 12 gives


Table 2. Simulated _a_ ˆ _n_ values under normal mixtures with _m_ 0 = 3

||(_σ_1_, σ_2|_, σ_3)=(1|_,_1_,_1)|(_σ_<br>(0_._|1_, σ_2_, σ_3) <br>75_,_1_._5_,_0_._|=<br>75)|
|---|---|---|---|---|---|---|
|(_θ_1_, θ_2_, θ_3)|_n_=100|_n_=300|_n_=500|_n_=100|_n_=300|_n_=500|
|(−4,0,4)|0_._098|0_._155|0_._16|0_._092|0_._12|0_._131|
|(−4,0,5)|0_._119|0_._197|0_._21|0_._106|0_._14|0_._159|
|(−5,0,5)|0_._144|0_._225|0_._259|0_._123|0_._164|0_._181|
|(−4,0,6)|0_._131|0_._213|0_._232|0_._119|0_._164|0_._179|
|(−5,0,6)|0_._153|0_._236|0_._276|0_._138|0_._212|0_._237|
|(−6,0,6)|0_._167|0_._268|0_._289|0_._112|0_._194|0_._252|


with _R_<sup>2</sup> = 0 _._ 78. From this, we derive an empirical formula for _an_ with _m_ 0 = 2:


Its effectiveness will be illustrated in simulation studies.

#### _3.2 Empirical Formulas for an With m 0_ = _3_

For _m_ 0 = 3, we develop an empirical formula for _an_ by considering the following three factors: component mean, component variance, and sample size. We include only one set of mixing proportions, ( _α_ 1 _, α_ 2 _, α_ 3) = (0 _._ 33 _,_ 0 _._ 33 _,_ 0 _._ 34). We use 1000 repetitions at each level combination to obtain the ˆ _an_ values. The specification of the 6 × 2 × 3 = 36 full factorial design and the results are given in Table 2.

Next, we regress the response _y_ = log{ _a_ ˆ _n/_ (0 _._ 35 − _a_ ˆ _n_ )} with respect to three covariates: _n_<sup>−1</sup> , log{ _ω_ 12 _/_ (1 − _ω_ 12)}, and log{ _ω_ 23 _/_ (1 − _ω_ 23)} _,_ where _ω_ 12 and _ω_ 23 are the average of the misclassification probabilities between the first two components and the last two components, respectively. The fitted coefficients for log{ _ω_ 12 _/_ (1 − _ω_ 12)} and log{ _ω_ 23 _/_ (1 − _ω_ 23)} are not significantly different. They are hence replaced by a single covariate log{ _ω_ 12 _ω_ 23 _/_ (1 − _ω_ 12)(1 − _ω_ 23)}, and the resulting model becomes


with _R_<sup>2</sup> = 0 _._ 89. Therefore, the empirical formula for _an_ with _m_ 0 = 3 is


Table 1. Simulated _a_ ˆ _n_ values under normal mixtures with _m_ 0 = 2

||(_σ_1|_, σ_2)=(1|_,_1)|(_σ_1_, σ_2|)=(1_._5_,_|0_._75)|
|---|---|---|---|---|---|---|
|(_θ_1_, θ_2)|_n_=100|_n_=300|_n_=500|_n_=100|_n_=300|_n_=500|
||||(_α_1_, α_2)=|(0_._5_,_0_._5)|||
|(−1.5,1.5)|0.107|0.134|0.183|0.093|0.128|0.169|
|(−2.0,2.0)|0.160|0.179|0.226|0.145|0.179|0.166|
|(−2.5,2.5)|0.233|0.301|0.230|0.181|0.196|0.259|
|||(|_α_1_, α_2)=|(0_._25_,_0_._75|)||
|(−1.5,1.5)|0.082|0.098|0.139|0.087|0.095|0.093|
|(−2.0,2.0)|0.128|0.170|0.153|0.108|0.123|0.134|
|(−2.5,2.5)|0.190|0.210|0.241|0.174|0.164|0.211|


We next illustrate the effectiveness of the empirical formulas by simulation.

#### _4. SIMULATION STUDY_

The purpose of the simulation is two-fold: to assess the accuracy of the proposed asymptotic approximation in finite samples and to examine the power of the EM test. The EM test is calculated based on the recommendations for _B_ , _K_ , and the two penalty functions _p_ ( _β_ ) and _pn_ ( _σ_<sup>2</sup> ; _σ_ ˆ<sup>2</sup> ).

We first test _H_ 0 : _m_ = 2. In total, we choose 12 null models with order 2 as specified in Table 3. For each null model

_Chen, Li, and Fu: Inference on the Order of a Normal Mixture_

_1101_

Table 3. Parameter specifications for 12 null models with order 2

|(_α_1_, α_2)|(0.5,0.5), (0.2,0.8)|
|---|---|
|(_θ_1_, θ_2)|(−1.25,1.25), (−1.75,1.75), (−2.25,2.25)|
|(_σ_1_, σ_2)|(1,1), (1.2,0.6)|


under two sample sizes, 200 and 400, we calculate the simulated Type I error rates based on 5000 repetitions. The simulation results for two significance levels, 5% and 1%, are summarized in Figure 1. The plots show that the observed levels are close to their targets in most cases. To check the power of the EM test, we choose eight alternative models as specified in Table 4. The power of the EM test under each alternative model is calculated based on 1000 repetitions. The simulation results are also summarized in Table 4. The power of the EM test is much larger than the level, and increases as the sample size increases.

Next, we test _H_ 0 : _m_ = 3. In total, we choose 12 null models with order 3 as specified in Table 5. Figure 2 shows that the observed levels are close to their nominal levels in most cases. We again choose eight alternative models as specified in Table 6. The power of the EM test is calculated based on 1000 repetitions and the results are summarized in Table 6. Clearly, as the sample size increases, the power increases. Further, when the component means under the alternative models become far away from one another, the power of the test increases.

#### _5. APPLICATION EXAMPLES_

#### _5.1 SLC Data_

Geneticists often study SLC activity in red blood cells, since it relates to blood pressure and the prevalence of hypertension. Furthermore, SLC activity is easier to study than blood pressure; see Example 1 and Roeder (1994).

Suppose the SLC activity is determined by a simple mode of inheritance compatible with the action of a single gene with two alleles. If each observation was composed of the sum of a genetic component and a normally distributed measurement error, then the SLC measurements would follow one of two competing genetic models, namely the simple dominance model or the additive model, corresponding to either a two-component or a three-component normal mixture model. Hence, there is a need to test the null hypothesis _m_ 0 = 2.

The data consist of red blood cell SLC activity measured for 190 individuals. We apply the EM test for _H_ 0 : _m_ = _m_ 0 = 2. The constituent entries of _�_<sup>ˆ</sup> 0 are


With _�_<sup>ˆ</sup> 0, the estimated average overlap probability _ω_ 12 between the two groups is 0.211. Applying the empirical formula in (4), we get _an_ = 0 _._ 068 and EM<sup>(1)</sup> _n_<sup>= 4</sup><sup>_._595</sup><sup>_,_EM(2)</sup> _n_<sup>= 4</sup><sup>_._637</sup><sup>_,_and</sup> EM<sup>(3)</sup> _n_<sup>= 4</sup><sup>_._657, with corresponding</sup><sup>_p_-values 0.331, 0.327, and</sup> 0.324, respectively. Therefore, the simple dominance model is not rejected.


<!-- Start of picture text -->
n=200: Significance level=5% n=400: Significance level=5%<br>K=1 K=2 K=3 K=1 K=2 K=3<br>n=200: Significance level=1% n=400: Significance level=1%<br>K=1 K=2 K=3 K=1 K=2 K=3<br>6.0 6.0<br>5.5 5.5<br>5.0 5.0<br>4.5 4.5<br>4.0 4.0<br>3.5 3.5<br>Simulated type I errors Simulated type I errors<br>3.0 3.0<br>2.5 2.5<br>1.4 1.4<br>1.2 1.2<br>1.0 1.0<br>0.8 0.8<br>Simulated type I errors Simulated type I errors<br>0.6 0.6<br><!-- End of picture text -->

Figure 1. Simulated Type I errors of EM<sup>(</sup> _n_<sup>_K_)</sup> for _m_ 0 = 2.

_Journal of the American Statistical Association, September 2012_

_1102_

Table 4. Parameters and powers of EM test in eight alternative models for testing against _H_ 0 : _m_ = 2 at the 5% level

||||_n_=200|||_n_=400||
|---|---|---|---|---|---|---|---|
|Alternative|models|EM<sup>(1)</sup><br>_n_|EM<sup>(2)</sup><br>_n_|EM<sup>(3)</sup><br>_n_|EM<sup>(1)</sup><br>_n_|EM<sup>(2)</sup><br>_n_|EM<sup>(3)</sup><br>_n_|
|(_α_1_, α_2_, α_3)|(_σ_1_, σ_2_, σ_3)|||(_θ_1_, θ_2_, θ_3)=|(−2.5,0,2.5)|||
|(1/3,1/3,1/3)|(1,1,1)|25_._3|25_._5|25_._8|64_._5|64_._8|64_._8|
|(0.4,0.2,0.4)|(1,1,1)|22_._7|23_._1|23_._2|51_._1|51_._2|51_._3|
|(1/3,1/3,1/3)|(0.6,1.2,0.6)|99_._1|99_._1|99_._1|100_._0|100_._0|100_._0|
|(0.4,0.2,0.4)|(0.6,1.2,0.6)|98_._8|98_._8|98_._8|100_._0|100_._0|100_._0|
|(_α_1_, α_2_, α_3_, α_4)|(_σ_1_, σ_2_, σ_3_, σ_4)|||(_θ_1_, θ_2_, θ_3_, θ_4)|=(−3,−1,1,3)|||
|(0.25,0.25,0.25,0.25)|(1,1,1,1)|19_._6|19_._9|20_._0|43_._7|43_._9|44_._1|
|(0.35,0.15,0.15,0.35)|(1,1,1,1)|32_._9|33_._2|33_._5|70_._2|70_._2|70_._2|
|(0.25,0.25,0.25,0.25)|(0.6,1.2,1.2,0.6)|40_._1|40_._4|40_._5|59_._7|60_._0|60_._2|
|(0.35,0.15,0.15,0.35)|(0.6,1.2,1.2,0.6)|100_._0|100_._0|100_._0|100_._0|100_._0|100_._0|


The above analysis was accomplished with an R function that we have developed

#### _>_ emtest.norm(x, 2)

where _x_ denotes the SLC data vector and 2 is the null order; see the online supplementary materials for more details.

Roeder (1994) analyzed the data and concluded that a threecomponent normal mixture is most suitable. The difference between the two conclusions may be due to the equal-component variance assumption in Roeder’s analysis. We may examine the equal-variance assumption by testing the hypothesis _H_ 0 : _σ_ 1 = _σ_ 2 versus _H_ A : _σ_ 1̸ = _σ_ 2 _._ Under the null hypothesis, the penalized likelihood ratio test statistic _Rn_ = 2{sup _H_ A _ℓn_ ( _�_ ) − sup _H_ 0 _ℓn_ ( _�_ )} converges in distribution to _χ_ 1<sup>2(Chen,Tan,and</sup> Zhang 2008). For the SLC data, we find that the penalized likelihood ratio test statistic for testing the variance equality in the two-component normal mixture is 6.37. Calibrated by the _χ_ 1<sup>2</sup> distribution, the _p_ -value is 1.2%, which suggests strong evidence against the equal-variance assumption.

If _σ_ 2<sup>2≫</sup><sup>_σ_</sup> 1<sup>2inatwo-componentmixture,afittingbasedon</sup> the equal-variance assumption may split the second component into several to compensate for the overdispersion. This is probably why Roeder’s method favors a three-component mixture while the EM test favors a two-component mixture. This is visually supported by Figure 3, where we have included the two-component fitting with unequal variances and the threecomponent fitting with equal variances. The two-component fitting with unequal variances provides a slightly better fit, especially in the region where the SLC measurement is in the neighborhood of 4.

The correctness of the simple dominant mode cannot be determined solely by statistical analysis. However, for the first time, we have a way to quantify the support of this mode.

Table 5. Parameter specifications for 12 null models with order 3

|(_α_1_, α_2_, α_3)|(1/3,1/3,1/3),|(0.25,0.5,0.25)|
|---|---|---|
|(_θ_1_, θ_2_, θ_3)|(−3.5,0,4.5),|(−4.5,0,4.5)|
|(_σ_1_, σ_2_, σ_3)|(1,1,1), (0.6,1|.2,0.6), (0.6,0.6,1.2)|


#### _5.2 Adulteration in Wine Production_

A normal mixture model is used by Monetti et al. (1996) to estimate the proportion of adulterated musts and establish classification regions for the acceptance or rejection of a given wine sample. Experience shows that the characteristics of the genuine samples have a normal distribution. There is no prior information on the distribution of the characteristics of the adulterated samples. A two-component normal mixture model was found to be suitable for three characteristics of the wine samples. Possible heterogeneity within the adulterated samples was not explored by these authors. This information can be important for forming the classification regions and estimating the prevalence of adulterated samples.

One would like to investigate whether or not a two-component normal mixture model is suitable for the characteristics of wine samples. Monetti et al. (1996) gave data for four variables ( _scyllo_ -inositol, _myo_ -inositol, two D/H ratios) suitable for discovering adulterations via added sugar from plants other than grapes. The data consist of 344 observations. We use the EM test for the null hypotheses _m_ 0 = 2 and _m_ 0 = 3 for logtransformed _scyllo_ -inositol and _myo_ -inositol measurements and untransformed D/H measurements. The results are summarized in Table 7. Our results show that the order _m_ 0 = 3 is most appropriate for the first three characteristics. Monetti et al. (1996) suggested _m_ 0 = 2 on the basis of the nature of the problem, not rigorous hypothesis tests. They did not discuss the possibility of modeling the data with _m_ 0 = 3. We find that _m_ 0 = 1 is most appropriate for the fourth characteristic, which is consistent with their analysis. Using this characteristic to test _m_ 0 = 2 is for illustration only, and testing _m_ 0 = 3 is not necessary and omitted.

According to our result, we fit a three-component multivariate normal mixture model based on the first three characteristics: log-transformed _scyllo_ -inositol and _myo_ -inositol measurements and untransformed D/H _I_ measurement. The component with the largest mean value in each characteristic corresponds to the genuine samples. It has the proportion 69.2%, which is different to the value 75.8% in Monetti et al. (1996) obtained from a twocomponent multivariate mixture. Since the three-component mixture is more suitable for the data, we expect that 1−69.2% = 30.8% is a more precise estimate of the prevalence of

_Chen, Li, and Fu: Inference on the Order of a Normal Mixture_

_1103_


<!-- Start of picture text -->
n=200: Significance level=5% n=400: Significance level=5%<br>K=1 K=2 K=3 K=1 K=2 K=3<br>n=200: Significance level=1% n=400: Significance level=1%<br>K=1 K=2 K=3 K=1 K=2 K=3<br>6.0 6.0<br>5.5 5.5<br>5.0 5.0<br>4.5 4.5<br>4.0 4.0<br>3.5 3.5<br>Simulated type I errors Simulated type I errors<br>3.0 3.0<br>2.5 2.5<br>1.4 1.4<br>1.2 1.2<br>1.0 1.0<br>0.8 0.8<br>Simulated type I errors Simulated type I errors<br>0.6 0.6<br><!-- End of picture text -->

Figure 2. Simulated Type I errors of EM<sup>(</sup> _n_<sup>_K_)</sup> for _m_ 0 = 3.

adulteration. Based on the fitted three-component model, we can further calculate the posterior probability that a given sample belongs to a genuine sample, which can be used to establish classification regions for the acceptance or rejection of a given wine sample.

#### _5.3 Differential Gene Expression_

In microarray experiments, the expression levels of a large number of genes are obtained to identify those differentially expressed over usually two samples. A _t_ -test can be used to identify individual differentially expressed genes. Because the number

of genes in such high-throughput experiments is huge, controlling the Type I error familywise is no longer sensible. Instead, geneticists favor the notion of controlling the false discovery rate (Benjamini and Hochberg 1995). Among many recipes for controlling this rate, Efron (2004) used a finite normal mixture to classify the genes into null and alternative subgroups based on the _z_ -scores derived from the individual _t_ -tests. Determining the order of the normal mixture model is a necessary step of such analysis. Often, the order is based on the genetic background (Efron 2004; McLachlan, Bean, and Ben-Tovim Jones 2006). In addition, an order selection procedure can be used (Chen and Khalili 2008).

Table 6. Parameters and powers of EM test in eight alternative models for testing against _H_ 0 : _m_ = 3 at the 5% level

||||_n_=200|||_n_=400||
|---|---|---|---|---|---|---|---|
|Alternative|models|EM<sup>(1)</sup><br>_n_|EM<sup>(2)</sup><br>_n_|EM<sup>(3)</sup><br>_n_|EM<sup>(1)</sup><br>_n_|EM<sup>(2)</sup><br>_n_|EM<sup>(3)</sup><br>_n_|
|(_θ_1_, θ_2_, θ_3_, θ_4)|(_σ_1_, σ_2_, σ_3_, σ_4)||(_α_1_,_|_α_2_, α_3_, α_4)=(|0.25,0.25,0.25,0|.25)||
|(−4.5,−1.5,1.5,4.5)|(1,1,1,1)|17_._5|19_._0|19_._2|52_._4|52_._6|52_._8|
|(−6,−2,2,6)|(1,1,1,1)|93_._2|93_._7|94_._0|100_._0|100_._0|100_._0|
|(−4.5,−1.5,1.5,4.5)|(0.6,1.2,0.6,1.2)|84_._6|85_._3|85_._7|99_._6|99_._6|99_._6|
|(−6,−2,2,6)|(0.6,1.2,0.6,1.2)|99_._9|99_._9|99_._9|100_._0|100_._0|100_._0|
|(_θ_1_, θ_2_, θ_3_, θ_4_, θ_5)|(_σ_1_, σ_2_, σ_3_, σ_4_, σ_5)||(_α_1_, α_|2_, α_3_, α_4_, α_5)=|(0.2,0.2,0.2,0.2|,0.2)||
|(−5,−2.5,0,2.5,5)|(1,1,1,1,1)|9_._1|10_._1|10_._4|27_._5|28_._2|28_._4|
|(−6,−3,0,3,6)|(1,1,1,1,1)|38_._4|40_._2|40_._7|84_._3|84_._5|84_._6|
|(−5,−2.5,0,2.5,5)|(0.6,1.2,0.6,1.2,1)|42_._3|44_._5|44_._8|82_._6|82_._7|83_._0|
|(−6,−3,0,3,6)|(0.6,1.2,0.6,1.2,1)|80_._7|81_._9|82_._3|99_._5|99_._5|99_._5|


_Journal of the American Statistical Association, September 2012_

_1104_


Figure 3. Histogram for 190 SLC measurements: two-component mixture fitting with unequal variances and three-component mixture fitting with equal variances. The online version of this figure is in color.

The EM test provides another rigorous approach. We analyze the prostate cancer dataset of Singh et al. (2002). This data consists of the gene expression levels of 6033 genes for 52 prostate cancer patients and 50 normal control subjects. The main objective of the study was to find the genes that are differentially expressed between the prostate cancer patients and the normal control subjects. The 6033 _z_ -scores, transformed from the two-sample _t_ -test statistics, can be downloaded from _http://www-stat.stanford.edu/˜brad_ . Positive _z_ -scores indicate higher expression levels among prostate cancer patients, whereas negative _z_ -scores indicate higher expression levels among normal control subjects. If the gene is not differentially expressed, theoretically, the corresponding _z_ should follow _N_ (0 _,_ 1).

Following Efron (2004), we apply the normal mixture to model the 6033 _z_ -scores. Two-component or three-component normal mixture models have a natural interpretation here. The two-component normal mixture implies the existence of nondifferentially expressed genes and one of the overexpressed genes (large positive component mean) and underexpressed genes (small negative component mean), while the three-component normal mixture implies the existence of all three gene types.

Table 7. EM statistics and _p_ -values for adulteration data analysis

||_m_0||=2|_m_0|=3|
|---|---|---|---|---|---|
|Characteristic|EM<sup>(3)</sup>||_p_-value|EM<sup>(3)</sup>|_p_-value|
|_scyllo_-inositol|15.96||0.003|10.78|0.096|
|_myo_-inositol|24.35||0.000|7.06|0.315|
|D/H_I_|14.04||0.007|4.51|0.609|
|D/H_II_|1.79||0.775|–|–|


We use the EM test to check if the two-component normal mixture provides an adequate fit to the _z_ -scores. We first test the null hypothesis of order 2. The EM test statistics are EM<sup>(1)</sup> _n_<sup>= 12</sup><sup>_._997</sup><sup>_,_EM(2)</sup> _n_<sup>= 12</sup><sup>_._998</sup><sup>_,_andEM(3)</sup> _n_<sup>= 12</sup><sup>_._999.The</sup> corresponding _p_ -values are around 0.011. Therefore, there is strong evidence to reject the null hypothesis of order 2. We further apply the EM test to test the null hypothesis of order 3. The constituent entries of _�_<sup>ˆ</sup> 0 are


which results in _ω_ 12 = 0 _._ 154 and _ω_ 23 = 0 _._ 228, and further _an_ = 0 _._ 100. The EM test statistics are EM<sup>(1)</sup> _n_<sup>= 9</sup><sup>_._334</sup><sup>_,_EM(2)</sup> _n_<sup>=</sup> 9 _._ 361 _,_ and EM<sup>(3)</sup> _n_<sup>= 9</sup><sup>_._380. The corresponding</sup><sup>_p_-values are 0.15.</sup> Hence, the null hypothesis of _m_ 0 = 3 is not rejected at the 5% level, and a three-component normal mixture is adequate for the data.

According to the fitting of the three-component normal mixture model, the 6033 genes can be classified into three groups: underexpressed (around 0.6%), nondifferentially expressed (around 98.5%), and overexpressed (around 0.9%). The estimate of the proportion of nondifferentially expressed genes is 0.985, which is close to the estimate 0.984 obtained by Efron (2010, p. 85). Strong evidence for the existence of both overexpressed and underexpressed genes may help prostate cancer researchers to devise validation experiments accordingly.

#### _6. DISCUSSION_

Hypothesis testing on the order of normal mixture is an important but unsolved problem. This article comes up with a novel recipe to create an effective solution. The carefully designed recipe is possible only with a thorough understanding of a large number of existing ingredients. The assembly of these ingredients is itself a formidable task because of the many unyielding properties of the finite normal mixture models. The significance of the contribution is that this is the first valid and effective hypothesis test for this long-standing problem. The procedure comes with an automated tuning strategy and an easy to use R function. A single command can give the users the test statistics and the corresponding asymptotic _p_ -values.

The referees and the associate editor raised some important issues regarding the use of the EM test. Clarification of which may also help general readers. We address three of them as follows.

The first one is on the multiple test issue. In applications, an inference goal should be unambiguously established before the data analysis. Our examples clearly violate this principle due to illustrative nature. Suppose the inference goal is to test _m_ = 2 against the alternative _m >_ 2 at the 5% level period. Then, we should conclude with an EM test for this pair of hypotheses. If instead, one is curious on the lowest order with adequate fit and _m <_ 2 is ruled out a priori. One should then spend the level of the test in a sequential manner. For example, one may use 3% to test _m_ = 2 against _m >_ 2. If the test is significant, we then use 2% to test _m_ = 3 against _m >_ 3.

_Chen, Li, and Fu: Inference on the Order of a Normal Mixture_

_1105_

The second one is on scientific implication. A _m_ 0-component model could be rejected for various reasons, not necessarily because the actual distribution is a normal mixture with more components. A call for accepting a specific alternative model should only be made based on scientific principles. The EM test provides valuable numerical evidence to support such conclusions.

The third one is the choice of _K_ . The purpose of the usual EM algorithm is more on accurately locating the maximum point of the likelihood function, less on its maximum value. The slow rate of convergence is often observed because the likelihood function is flat near the maximum point, especially in finite mixture model applications. In this article, we focus on its maximum value and the EM algorithm achieves a very good precision after a few iterations. Empirical evidences suggest that _K_ = 3 is satisfactory. A slightly larger _K_ does not improve the power property because EM<sup>(</sup> _n_<sup>_K_)</sup> may merely increase in the third decimal place. Iterate until convergence invalidates the asymptotic conclusion.

##### _[Received October 2011. Revised April 2012.]_

#### _REFERENCES_

- Bartlett, M. S. (1953), “Approximate Confidence Intervals. I,” _Biometrika_ , 40, 12–19. [1099]

- Benjamini, Y., and Hochberg, Y. (1995), “Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing,” _Journal of the Royal Statistical Society,_ Series B, 57, 289–300. [1103]

- Charnigo, R., and Sun, J. (2004), “Testing Homogeneity in a Mixture Distribution via the _L_<sup>2</sup> -Distance Between Competing Models,” _Journal of the American Statistical Association_ , 99, 488–498. [1097]

- Chen, H., and Chen, J. (2003), “Tests for Homogeneity in Normal Mixtures With Presence of a Structural Parameter,” _Statistica Sinica_ , 13, 351–365. [1097]

- Chen, J. (1995), “Optimal Rate of Convergence in Finite Mixture Models,” _The Annals of Statistics_ , 23, 221–234. [1097]

- Chen, J., and Khalili, A. (2008), “Order Selection in Finite Mixture Models With a Non-Smooth Penalty,” _Journal of the American Statistical Association_ , 103, 1674–1683. [1097,1103]

- Chen, J., and Li, P. (2009), “Hypothesis Test for Normal Mixture Models: The EM Approach,” _The Annals of Statistics_ , 37, 2523–2542. [1097,1098]

- Chen, J., Tan, X., and Zhang, R. (2008), “Inference for Normal Mixtures in Mean and Variance,” _Statistica Sinica_ , 18, 443–465. [1098,1099,1102]

- Chernoff, H., and Lander, E. (1995), “Asymptotic Distribution of the Likelihood Ratio Test That a Mixture of Two Binomials Is a Single Binomial,” _Journal of Statistical Planning and Inference_ , 43, 19–40. [1096]

- Dacunha-Castelle, D., and Gassiat, E. (1999), “Testing the Order of a Model Using Locally Conic Parametrization: Population Mixtures and Stationary ARMA Processes,” _The Annals of Statistics_ , 27, 1178–1209. [1096,1099]

- Efron, B. (2004), “Large-Scale Simultaneous Hypothesis Testing: The Choice of a Null Hypothesis,” _Journal of the American Statistical Association_ , 99, 96–104. [1103,1104]

- ——— (2010), _Large-Scale Inference: Empirical Bayes Methods for Estimation, Testing, and Prediction_ (Institute of Mathematical Statistics Monographs, Vol. I), Cambridge: Cambridge University Press. [1104]

- Ghosh, J. K., and Sen, P. K. (1985), “On the Asymptotic Performance of the Log-Likelihood Ratio Statistic for the Mixture Model and Related Results,” in _Proceedings of the Berkeley Conference in Honor of J. Neyman and J. Kiefer_ (Vol. 2), eds. L. LeCam and R. A. Olshen, Monterey, CA: Wadsworth, pp. 789–806. [1096]

- Hartigan, J. A. (1985), “A Failure of Likelihood Asymptotics for Normal Mixtures,” in _Proceedings of the Berkeley Conference in Honor of J. Neyman and J. Kiefer_ (Vol. 2), eds. L. LeCam and R. A. Olshen, Monterey, CA: Wadsworth, pp. 807–810. [1096]

- Hathaway, R. J. (1985), “A Constrained Formulation of Maximum-Likelihood Estimation for Normal Mixture Distributions,” _The Annals of Statistics_ , 13, 795–800. [1097]

- Ishwaran, H., James, L. F., and Sun, J. (2001), “Bayesian Model Selection in Finite Mixtures by Marginal Density Decompositions,” _Journal of the American Statistical Association_ , 96, 1316–1332. [1097]

- James, L. F., Priebe, C. E., and Marchette, D. J. (2001), “Consistent Estimation

of Mixture Complexity,” _The Annals of Statistics_ , 29, 1281–1296. [1097]

- Jeffries, N. O. (2003), “A Note on Testing the Number of Components in a Normal Mixture,” _Biometrika_ , 90, 991–994. [1097]

- Keribin, C. (2000), “Consistent Estimation of the Order of Mixture Models,” _Sankhya_ , 62, 49–66. [1097]

- Leroux, B. (1992), “Consistent Estimation of a Mixture Distribution,” _The Annals of Statistics_ , 20, 1350–1360. [1097]

- Li, P., and Chen, J. (2010), “Testing the Order of a Finite Mixture Model,” _Journal of the American Statistical Association_ , 105, 1084–1092. [1097]

- Liu, X., and Shao, Y. (2003), “Asymptotics for Likelihood Ratio Tests Under Loss of Identifiability,” _The Annals of Statistics_ , 31, 807–832. [1096,1099]

- Lo, Y., Mendell, N. R., and Rubin, D. B. (2001), “Testing the Number of Components in a Normal Mixture,” _Biometrika_ , 88, 767–778. [1097]

- Maitra, R., and Melnykov, V. (2010), “Simulating Data to Study Performance of Finite Mixture Modeling and Model-Based Clustering Algorithms,” _Journal of Computational and Graphical Statistics_ , 19, 354–376. [1100]

- McLachlan, G. J. (1987), “On Bootstrapping the Likelihood Ratio Test Statistic for the Number of Components in a Normal Mixture,” _Journal of the Royal Statistical Society,_ Series C, 36, 318–324. [1097]

- McLachlan, G. J., Bean, R. W., and Ben-Tovim Jones, L. (2006), “A Simple Implementation of a Normal Mixture Approach to Differential Gene Expression in Multiclass Microarrays,” _Bioinformatics_ , 22, 1608–1615. [1103]

- McLachlan, G. J., and Peel, D. (2000), _Finite Mixture Models_ , New York: Wiley. [1096]

- Miloslavsky, M., and van der Laan, M. J. (2003), “Fitting of Mixtures With Unspecified Number of Components Using Cross-Validation Distance Estimate,” _Computational Statistics and Data Analysis_ , 41, 413–428. [1096,1097]

- Monetti, A., Versini, G., Dalpiaz, G., and Reniero, F. (1996), “Sugar Adulterations Control in Concentrated Rectified Grape Musts by Finite Mixture Distribution Analysis of the Myo- and Scyllo-Inositol Content and the D/H Methyl Ratio of Fermentative Ethanol,” _Journal of Agricultural and Food Chemistry_ , 44, 2194–2201. [1102]

- Pavlic, M., Brand, R., and Cummings, S. M. (2001), “Estimating Probability of Non-Response to Treatment Using Mixture Distributions,” _Statistics in Medicine_ , 20, 1739–1753. [1096]

- R Development Core Team (2008), _R: A Language and Environment for Statistical Computing_ , Vienna: R Foundation for Statistical Computing. Available at _http://www.R-project.org_ . [1097]

- Richardson, S., and Green, P. J. (1997), “On Bayesian Analysis of Mixtures With an Unknown Number of Components,” _Journal of the Royal Statistical Society,_ Series B, 59, 731–792. [1097]

- Roeder, K. (1994), “A Graphical Technique for Determining the Number of Components in a Mixture of Normals,” _Journal of the American Statistical Association_ , 89, 487–500. [1096,1101,1102]

- Schork, N. J., Allison, D. B., and Thiel, B. (1996), “Mixture Distributions in Human Genetics,” _Statistical Methods in Medical Research_ , 5, 155–178. [1096]

- Singh, D., Febbo, P. G., Ross, K., Jackson, D. G., Manola, J., Ladd, C., Tamayo, P., Renshaw, A. A., D’Amico, A. V., Richie, J. P., Lander, E. S., Loda, M., Kantoff, P. W., Golub, T. R., and Sellers, W. R. (2002), “Gene Expression Correlates of Clinical Prostate Cancer Behavior,” _Cancer Cell_ , 1, 203–209. [1104]

- Woo, M., and Sriram, T. N. (2006), “Robust Estimation of Mixture Complexity,” _Journal of the American Statistical Association_ , 101, 1475–1485. [1097]

---

[← Journal of the American Statistical Association](01-journal-of-the-american-statistical-association.md) · [Up: contents](index.md)
