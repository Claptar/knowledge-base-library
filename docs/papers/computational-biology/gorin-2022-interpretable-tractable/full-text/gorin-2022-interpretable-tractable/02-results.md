---
title: Results
source: https://doi.org/10.1038/s41467-022-34857-7/
source_file: sources/papers/gorin-2022-interpretable-tractable/gorin-2022-interpretable-tractable.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `gorin-2022-interpretable-tractable.jats` from [papers/gorin-2022-interpretable-tractable](https://doi.org/10.1038/s41467-022-34857-7/) — papers · gorin-2022-interpretable-tractable, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Results

## Transcription rate variation accounts for empirically observed variance {#Sec3}

If we would like to understand and fit available transcriptomic data—especially multimodal data sets that report the numbers of both nascent and mature transcripts inside single cells^(33,34)—what kind of models of transcription should we consider? Given that single cell RNA counts are often low, we would like our models to be able to account for the production, processing, and degradation of individual RNA molecules. From experiments in living cells, these processes are known to be random³⁵. Crucially, the molecule counts are low enough that the variation in molecule numbers should be explicitly described by a stochastic model³⁶.

The theoretical framework associated with the chemical master equation (CME)^(37–43) can be used to define discrete and stochastic models of cellular processes. The *constitutive* model of transcription, which assumes RNA is produced at a constant rate, is one particularly simple and well-studied example. It can be defined via the chemical reactions

$$\begin{array}{l}\varnothing \mathop{\to }\limits^{K}{{{{{{{{{\mathcal{N}}}}}}}}}}\mathop{\to }\limits^{\beta }{{{{{{{{{\mathcal{M}}}}}}}}}}\mathop{\to }\limits^{\gamma }\varnothing,\end{array}$$

where ${{{{{{{{{\mathcal{N}}}}}}}}}}$ denotes nascent RNA, ${{{{{{{{{\mathcal{M}}}}}}}}}}$ denotes mature RNA, *K* is the transcription rate, *β* is the splicing rate, and *γ* is the degradation rate. It predicts^(44,45) that the long-time probability ${P}_{ss}^{{{{{{{\rm{con}}}}}}}}({x}_{N},{x}_{M})$ of observing ${x}_{N}\in {{\mathbb{N}}}_{0}$ nascent RNA and ${x}_{M}\in {{\mathbb{N}}}_{0}$ mature RNA in a single cell is Poisson, so that

$${P}_{ss}^{{{{{{{\rm{con}}}}}}}}({x}_{N},\,{x}_{M})=\frac{{\left(\frac{K}{\beta }\right)}^{{x}_{N}}{{{{{{{\rm{e}}}}}}}}^{-K/\beta }}{{x}_{N}!}\frac{{\left(\frac{K}{\gamma }\right)}^{{x}_{M}}{{{{{{{\rm{e}}}}}}}}^{-K/\gamma }}{{x}_{M}!}.$$

While mathematically tractable, a model like this is too simple to fit existing data. Most observed eukaryotic RNA count distributions are ‘overdispersed’: they have a higher variance than Poisson distributions with the same mean⁴⁶.

One way to account for overdispersion is to assume that different cells in a population have different transcription rates, but that each individual cell otherwise follows the constitutive model. For various choices of transcription rate distribution, one can obtain results that look much closer to eukaryotic transcriptomic data. For example, one reasonable choice (which has been explored by other authors⁴⁷) is to assume that the transcription rate *K* is gamma-distributed with shape parameter *α* and scale parameter *θ*, i.e., *K* ~ Γ(*α*, *θ*). The long-time/steady-state probability of observing *x*_(*N*) nascent and *x*_(*M*) mature RNA would then be described by the Poisson-gamma *mixture* model

$${P}_{ss}^{{{{{{{\rm{mix}}}}}}}}({x}_{N},\,{x}_{M})=\int\nolimits_{0}^{\infty }{{{{{{{\rm{d}}}}}}}}K\,\frac{{K}^{\alpha -1}\,{{{{{{{\rm{e}}}}}}}}^{-K/\theta }}{{\theta }^{\alpha }\,{{\Gamma }}(\alpha )}\,{P}_{ss}^{{{{{{{\rm{con}}}}}}}}({x}_{N},\,{x}_{M}).$$

The marginal distributions of this joint distribution will be negative binomial rather than Poisson, allowing us to actually fit observed single-cell data. But this approach—which is equivalent to the post-hoc fitting of negative binomial distributions—is not biophysically interpretable. What is the biological meaning of the parameters *α* and *θ*? And why do different cells have different transcription rates? Is it really reasonable to assume, as we have here, that these rates are ‘frozen’, and remain as they are for all time in a given cell?

## Interpretable and tractable modeling framework for transcription rate variation {#Sec4}

We propose a class of transcriptional models that balance interpretability and tractability, and generalize the mixture model. Although various biological details underlying transcription may be complicated, we assume they can be captured by an effective transcription rate *K*(*t*) which is stochastic and varies with time. This transcription rate randomly fluctuates about its mean value, with the precise nature of its fluctuations dependent upon the fine biophysical details of transcription. Mathematically, we assume that *K*(*t*) is a continuous-valued stochastic process described by an (Itô-interpreted) stochastic differential equation (SDE)

$$\dot{K}(t) =\, [{{{{{{{{{\rm{mean}}}}}}}}}}\,{{{{{{{{{\rm{reversion}}}}}}}}}}]+[{{{{{{{{{\rm{noise}}}}}}}}}}]\\    =\, A-BK(t)+[{{{{{{{{{\rm{noise}}}}}}}}}}]$$

for some coefficients *A* and *B*, where [mean reversion] denotes a deterministic term that drives the transcription rate towards its mean value, and [noise] denotes a model-dependent term that introduces stochastic variation. The transcription rate *K*(*t*) is coupled to RNA dynamics as in the constitutive model:

$$\begin{array}{l}\varnothing \mathop{\to }\limits^{K(t)}{{{{{{{{{\mathcal{N}}}}}}}}}}\mathop{\to }\limits^{\beta }{{{{{{{{{\mathcal{M}}}}}}}}}}\mathop{\to }\limits^{\gamma }\varnothing .\end{array}$$

This reaction list defines a master equation model that couples discrete stochastic RNA dynamics to the continuous stochastic process *K*(*t*) (Fig. 1b). Although this model class is not completely realistic (for example, there is no feedback), it is fairly flexible, and can recapitulate empirically plausible negative binomial-like RNA count distributions. To guarantee this, we will specifically consider candidate models for which the steady-state distribution of *K*(*t*) is a gamma distribution.

Other kinds of transcriptional models can also be viewed as special cases of this model class. The constitutive model (Eq. (1)) is a degenerate case that arises from the limit of no noise and fast mean-reversion, and the mixture model arises from the limit of slow transcription rate variation. We will see later that the popular bursting model of RNA production, which describes intermittent production of multiple nascent transcripts at a time^(1,48–51) is also a degenerate case. For the rest of this paper, we examine two specific cases of this model class more closely: the gamma Ornstein–Uhlenbeck (Γ-OU) model and Cox–Ingersoll–Ross (CIR) model, which are depicted in Fig. 1c. In particular, we will motivate the underlying biophysics, solve the models, outline major similarities and differences, and discuss how and when they can be distinguished given transcriptomic data.

Coupling upstream variability to transcriptional CMEs has been studied before (e.g., by Dattani and Barahona⁵²), but usually in a way that assumes either that *K*(*t*) takes on a finite set of values (for example, gene switching⁵³), or that the distribution of *K*(*t*) is a priori known, rather than defined by a stochastic dynamical system like Eq. (4). We attempt to build on these studies by treating *K*(*t*) as a continuous stochastic dynamical variable on the same footing as nascent and mature RNA counts.

## A. Gamma Ornstein–Uhlenbeck production rate model {#Sec5}

Transcription rate variation may emerge due to mechanical changes in DNA that make producing RNA more or less kinetically favorable. Each nascent RNA produced by an RNA polymerase induces a small amount of mechanical stress/supercoiling in DNA, which builds over time and can mechanically frustrate transcription unless it is relieved. Because topoisomerases arrive to relieve stress (Fig. 1c), there is a dynamic balance between transcription-mediated stress and topoisomerase-mediated recovery, models of which can recapitulate gene overdispersion and bursting^(23,25).

We can simplify the detailed mechanistic model of Sevier, Kessler, and Levine while retaining crucial qualitative aspects. For example, we can model transcriptional catalysis at a promoter ${{{{{{{{{\mathcal{G}}}}}}}}}}$ by a reservoir of RNA polymerase ${{{{{{{{{\mathcal{P}}}}}}}}}}$:

$${{{{{{{{{\mathcal{P}}}}}}}}}}+{{{{{{{{{\mathcal{G}}}}}}}}}}\mathop{\to }\limits^{{k}_{{{{{{{\rm{ini}}}}}}}}}{{{{{{{{{\mathcal{P}}}}}}}}}}+{{{{{{{{{\mathcal{G}}}}}}}}}}+{{{{{{{{{\mathcal{N}}}}}}}}}},$$

where *k*_(ini) is the rate of transcription initiation. Next, we assume that *k*_(ini) is proportional to the DNA relaxation state: if the DNA is in a stressed, twisted state, polymerase binding events are less likely to succeed. We propose that relaxation continuously decreases due to transcription-associated events, and that topoisomerases randomly arrive to increase relaxation according to an exponential law. The direct proportionality between the amount of DNA relaxation and *k*_(ini) is a coarse, first-order approximation valid when *k*_(ini) is small. This approximation may be biophysically justified by appealing to the prevalence of DNA compaction in eukaryotic cells. If the concentration *p* of RNA polymerase is high and its variation is low, we find (see Section 3.2.1 in the Supplementary Note) that the overall transcription rate *K*(*t*) can be modeled by the SDE

$$\dot{K}(t)=-\ \kappa K(t)+\epsilon (t;a,\theta ),$$

where *ϵ*(*t*; *a*, *θ*) is an infinitesimal Lévy process (a compound Poisson process with arrival frequency *a* and exponentially distributed jumps with expected size *θ*) capturing random topoisomerase arrival. This is the gamma Ornstein–Uhlenbeck (Γ-OU) model of transcription⁵⁴. It naturally emerges from a biomechanical model with two opposing effects: the continuous mechanical frustration of DNA undergoing transcription, which is a first-order process with relaxation rate *κ*, and the stochastic relaxation by topoisomerases that arrive at rate *a*. The scaling between the relaxation state and the transcription rate is set by a gain parameter *θ* ∝ 〈*p*〉, where 〈*p*〉 is average polymerase concentration; its coefficient of proportionality includes the coefficient of the aforementioned first-order expansion of *k*_(ini) as a function of the amount of DNA relaxation.

The Γ-OU model is perhaps better known in finance applications, where it has been used to model the stochastic volatility of the prices of stocks and options^(55–58). Its utility as a financial model is largely due to its ability to capture asset behavior that deviates from that of commonly used Gaussian Ornstein–Uhlenbeck models, such as skewness and frequent price jumps.

## B. Cox–Ingersoll–Ross production rate model {#Sec6}

Alternatively, transcription rate variation may be due to non-negligible fluctuations in the concentration of a regulator ${{{{{{{{{\mathcal{R}}}}}}}}}}$. We can encode these fluctuations by defining a multi-state promoter ${{{{{{{{{\mathcal{G}}}}}}}}}}$ activated by ${{{{{{{{{\mathcal{R}}}}}}}}}}$:

$$\varnothing \mathop{\to }\limits^{a}{{{{{{{{{\mathcal{R}}}}}}}}}}\mathop{\to }\limits^{\kappa }\varnothing \\ {{{{{{{{{{\mathcal{G}}}}}}}}}}}_{off}+{{{{{{{{{\mathcal{R}}}}}}}}}} {\mathop{\rightleftarrows }\limits^{{{k}_{on}}}_{{k}_{off}}}{{{{{{{{{{\mathcal{G}}}}}}}}}}}_{on}\\ {{{{{{{\mathcal{G}}}}}}}}_{on} \mathop{\to }\limits^{{k}_{ini}}{{{{{{{\mathcal{G}}}}}}}}_{on}+{{{{{{{\mathcal{N}}}}}}}},$$

where *a* is the ${{{{{{{{{\mathcal{R}}}}}}}}}}$ production rate and *κ* is the ${{{{{{{{{\mathcal{R}}}}}}}}}}$ degradation rate. If the number of regulator molecules *r*(*t*) is very large, we can accurately approximate regulator birth and death dynamics as a real-valued stochastic process using the framework associated with the chemical Langevin equation (CLE)^(39,59). Under the assumptions of rapid, weak binding, the effective transcription rate *K*(*t*) ≔ *θr*(*t*) satisfies the SDE

$$\dot{K}(t)=a\theta -\kappa K(t)+\sqrt{2\kappa \theta K(t)}\,\xi (t)$$

where *ξ*(*t*) is a Gaussian white noise term and *θ* = *k*_(ini)*k*_(on)/*k*_(off) (see Section 3.3.1 in the Supplementary Note). This is the Cox–Ingersoll–Ross (CIR) model of transcription⁵⁴.

Although the CIR model is most familiar as a description of interest rates in quantitative finance^(60–62), it has been previously used to describe biochemical input variation based on the CLE, albeit with less discussion of the theoretical basis and limits of applicability^(63–66).

## The models are interpretable and unify known results {#Sec7}

Qualitatively, the distribution shapes predicted by the Γ-OU and CIR models interpolate between Poisson and negative binomial-like extremes, with behavior controlled mostly by two of the transcription noise parameters: the mean-reversion rate *κ* and the gain parameter *θ* (Fig. 2a). Remarkably, where one is in this landscape of qualitative behavior is independent of the mean transcription rate 〈*K*〉 = *aθ*/*κ*, since *a* can vary to accommodate any changes in *κ* or *θ*. It is also independent of the steady-state distribution of transcription rates, which is the same (i.e., Γ(*a*/*κ*, *θ*)) in all cases. We find that the details of how the transcription rate fluctuates in time strongly impact the shape of RNA count distributions, a fact which may have previously gone underappreciated.

![](https://doi.org/10.1038/s41467-022-34857-7/)

Summary of the qualitative behavior of the Γ-OU and CIR models.
**a** Qualitative behavior can be visualized in a two-dimensional parameter space, with *κ*/(*κ* + *β* + *γ*) on one axis and the gain ratio *θ*/(*θ* + *a*) on the other. The four limits discussed in the text correspond to the four corners of this space. When *a* ≫ *θ*, we obtain Poisson-like behavior (green). When *a* ≪ *θ*, we obtain overdispersed distributions (orange). **b** Dynamics of limiting models. The Γ-OU and CIR models were simulated using four parameter sets close to the limiting regimes; transcription rates are visualized using trajectories and cell cartoons, where transcription rate is a logarithmic function of cell color. Ten thousand samples from the joint RNA count distribution are depicted in the rightmost column. Both models reduce to the constitutive model in the fast reversion and low gain limits, where the transcription rate *K*(*t*) is effectively constant in time and identical for all cells in the population. Both reduce to the mixture model in the slow reversion limit, so that *K*(*t*) is inhomogeneous across the population but constant in time for individual cells. In the high gain limit, the Γ-OU and CIR models yield different heavy-tailed distributions, with the CIR limiting model appearing to be uncharacterized. In both cases, *K*(*t*) exhibits sporadic large fluctuations within single cells.

When *κ* is very fast, the transcription rate very quickly reverts to its mean value whenever it is perturbed, so it is effectively constant, and we recover the constitutive model. When *κ* is very slow, the transcription rates of individual cells appear ‘frozen’ on the time scales of RNA dynamics, and we recover the mixture model discussed earlier. When *θ* is very small, fluctuations in underlying biological factors (DNA relaxation state or regulator concentration) are significantly damped, so *K*(*t*) is also effectively constant in this case.

Interestingly, while the two models agree in the aforementioned limits, their predictions markedly differ in the large *θ* limit, where fluctuations are amplified and predicted count distributions become increasingly overdispersed. The Γ-OU model predicts that nascent RNA is produced in geometrically distributed bursts in this limit, recapitulating the conventional model of bursty gene expression^(35,51). However, the CIR model predicts a previously uncharacterized family of count distributions with heavier tails than their Γ-OU counterparts. The difference is shown in Supplementary Fig. 4. This deviation is a consequence of state-dependent noise: while the number of topoisomerases which arrive to relieve stress does not depend on the current relaxation state of the DNA, birth-death fluctuations in the number of regulators tend to be greater when there are more regulator molecules present. We illustrate the four limiting regimes of interest in Fig. 2b, present their precise quantitative forms in Section 2.5, and derive them in Section 5 in the Supplementary Note.

Another lens through which to view qualitative behavior is the squared coefficient of variation (*η*² ≔ *σ*²/*μ*²), which quantifies the amount of ‘noise’ in a system. We derived the exact result that (see Section 2.4.2 in the Supplementary Note), consistently with previous studies^(29,30,32), the total noise can be written as a sum of ‘intrinsic’ (due to the stochasticity inherent in chemical reactions) and ‘extrinsic’ (due to transcription rate variation) contributions. For both models,

$${\eta }_{N}^{2} =\, \frac{1}{{\mu }_{N}}+\frac{\theta }{\langle K\rangle }\frac{1/\kappa }{1/\kappa+1/\beta }\\ {\eta }_{M}^{2} =\, \frac{1}{{\mu }_{M}}+\frac{\theta }{\langle K\rangle }\frac{1/\kappa }{1/\kappa+1/\beta }\frac{1/\kappa }{1/\kappa+1/\gamma }\frac{1/\kappa+1/(\beta+\gamma )}{1/\kappa },$$

where ${\eta }_{N}^{2}$ and ${\eta }_{M}^{2}$ quantify the amount of noise in nascent and mature RNA counts, and *μ*_(*N*) and *μ*_(*M*) denote the average number of nascent and mature RNA. In the ‘overdispersed’ regimes, where *θ* is large or *κ* is small, the extrinsic noise contributions become significant, but not in a way that maps cleanly onto the space depicted in Fig. 2a. For example, the fraction of extrinsic noise for nascent RNA is

$${({{{\rm{extrinsic}}}} \ {{{\rm{fraction}}}})}_N \ \colon = \ \frac{\eta_N^2 - \frac{1}{\mu_N}}{\eta_N^2}=\frac{\theta}{\theta+\kappa+\beta}$$

whose relative size in different overdispersed regimes changes depending on the splicing rate *β*. The behavior of the extrinsic noise fraction as a function of the parameters is summarized in Supplementary Fig. 5.

## The models are analytically tractable {#Sec8}

Using a suite of diverse theoretical approaches—including path integral methods, generating function computations, a correspondence between the Poisson representation of the CME and SDEs, and tools from the mathematics of stochastic processes—we were able to exactly solve the Γ-OU and CIR models. This includes computing all steady-state probability distributions *P*_(*ss*)(*x*_(*N*), *x*_(*M*)), first-order moments, second-order moments, and autocorrelation functions.

A central idea in all of our calculations is to consider transforms of the probability distribution—variants of the generating function—instead of the distribution itself. Once a generating function is available, the distribution can be obtained by computationally inexpensive Fourier inversion. The joint generating function *ψ*(*g*_(*N*), *g*_(*M*), *h*, *t*) is defined as

$$\psi \ \colon =\ \mathop{\sum }\limits_{{x}_{N}=0}^{\infty }\mathop{\sum }\limits_{{x}_{M}=0}^{\infty }\int\nolimits_{0}^{\infty }{{{{{{{\rm{d}}}}}}}}K\,{g}_{N}^{{x}_{N}}{g}_{M}^{{x}_{M}}{{{{{{{{\rm{e}}}}}}}}}^{{{{{{{{\rm{i}}}}}}}}hK}\,P({x}_{N},\,{x}_{M},\,K,\,t),$$

with ${g}_{N},{g}_{M}\in {\mathbb{C}}$ both on the complex unit circle, $h\in {\mathbb{R}}$, and *P*(*x*_(*N*), *x*_(*M*), *K*, *t*) encoding the probability density over counts and transcription rates. As these rates are not usually observable, and the previous body of work treats stationary distributions, we are most interested in *ψ*_(*ss*)(*g*_(*N*), *g*_(*M*)), the probability-generating function (PGF) of *P*_(*ss*)(*x*_(*N*), *x*_(*M*)). We find it most convenient to report our results in terms of ${\phi }_{ss}({u}_{N},\,{u}_{M}) \, \colon = \, \log {\psi }_{ss}({g}_{N},\,{g}_{M})$, the log of the PGF with an argument shift *u*_(*N*) ≔ *g*_(*N*) − 1 and *u*_(*M*) ≔ *g*_(*M*) − 1.

The solution of the Γ-OU model is

$${\phi }_{ss}({u}_{N},\,{u}_{M})=\langle K\rangle \int\nolimits_{0}^{\infty }\frac{{U}_{0}(s;{u}_{N},\,{u}_{M})}{1-\frac{\theta }{\kappa }{U}_{0}(s;{u}_{N},\,{u}_{M})}{{{{{{{\rm{d}}}}}}}}s,$$

where *U*₀(*s*; *u*_(*N*), *u*_(*M*)) is obtained by solving the characteristic ODEs obtained from the generating function⁶⁷:

$$\frac{{{{{{{{\rm{d}}}}}}}}{U}_{2}}{{{{{{{{\rm{d}}}}}}}}s}  \,=\,-\gamma \,{U}_{2},\qquad \qquad\! {U}_{2}(0)={u}_{M},\\ \frac{{{{{{{{\rm{d}}}}}}}}{U}_{1}}{{{{{{{{\rm{d}}}}}}}}s}  \,=\,\beta \,({U}_{2}-{U}_{1}),\quad \quad {U}_{1}(0)\,=\,{u}_{N},\\ \frac{{{{{{{{\rm{d}}}}}}}}{U}_{0}}{{{{{{{{\rm{d}}}}}}}}s}  \,=\kappa \,({U}_{1}-{U}_{0}),\quad \quad {U}_{0}(0)=0.$$

This system of linear first-order ODEs can be solved analytically⁵⁰, and the generating function can be obtained by quadrature. The solution to the CIR model is

$${\phi }_{ss}({u}_{N},\,{u}_{M})=\langle K\rangle \int\nolimits_{0}^{\infty }{U}_{0}(s;{u}_{N},{u}_{M})\,{{{{{{{\rm{d}}}}}}}}s,$$

where *U*₀(*s*; *u*_(*N*), *u*_(*M*)) is obtained from analogous ODEs:

$$\frac{{{{{{{{\rm{d}}}}}}}}{U}_{2}}{{{{{{{{\rm{d}}}}}}}}s}    \,=\,-\gamma \,{U}_{2},\qquad \qquad \qquad\!\! {U}_{2}(0)={u}_{M},\\ \frac{{{{{{{{\rm{d}}}}}}}}{U}_{1}}{{{{{{{{\rm{d}}}}}}}}s} \,=\,\beta \,({U}_{2}-{U}_{1}),\qquad \qquad {U}_{1}(0)={u}_{N},\\ \frac{{{{{{{{\rm{d}}}}}}}}{U}_{0}}{{{{{{{{\rm{d}}}}}}}}s}    \,=\,\kappa ({U}_{1}-{U}_{0})+\theta \,{U}_{0}^{2},\quad {U}_{0}(0)=0.$$

While the above ODEs have an exact solution, it is cumbersome, and preferable to evaluate numerically. We derive these solutions in Section 3, and validate them against stochastic simulations in Section 6 in the Supplementary Note.

## Summary statistics cannot distinguish between the models {#Sec9}

The tractability of these two models allows us to analytically compute common (steady-state) summary statistics. Despite the models’ distinct biological origins, their means (*μ*_(*N*) and *μ*_(*M*)), variances (${\sigma }_{N}^{2}$ and ${\sigma }_{M}^{2}$), covariances, and autocorrelation functions (*R*_(*N*)(*τ*) and *R*_(*M*)(*τ*)) match exactly (Table 1; see Section 4 in the Supplementary Note). This means that such summary statistics cannot be used as the basis for model discrimination. More fundamentally, it implies that experimental technologies that only report averages—such as RNA sequencing without single-cell resolution—cannot possibly distinguish between noise models.

Molecular distribution moments

| Moment | Value |
|----|----|
| 〈*K*〉 | $\frac{a\theta }{\kappa }$ |
| *μ*_(*N*) | 〈*K*〉/*β* |
| *μ*_(*M*) | 〈*K*〉/*γ* |
| ${\sigma }_{N}^{2}-{\mu }_{N}$ | $\frac{{\mu }_{N} \ \theta }{\kappa+\beta }$ |
| ${\sigma }_{M}^{2}-{\mu }_{M}$ | $\frac{{\mu }_{M} \ \theta }{\kappa+\gamma }\cdot \frac{\beta }{\kappa+\beta }\cdot \frac{\kappa+\beta+\gamma }{\beta+\gamma }$ |
| Cov(*X*_(*N*), *K*) | $\frac{\langle K\rangle \ \theta }{\kappa+\beta }$ |
| Cov(*X*_(*M*), *K*) | $\frac{\langle K\rangle \ \theta }{\kappa+\gamma }\cdot \frac{\beta }{\kappa+\beta }$ |
| Cov(*X*_(*N*), *X*_(*M*)) | $\frac{\langle K\rangle \ \theta }{(\kappa+\beta )(\kappa+\gamma )}\cdot \frac{\kappa+\beta+\gamma }{\beta+\gamma }$ |
| *R*_(*N*)(*τ*) | ${{{{{{{\rm{e}}}}}}}}^{-\beta \tau }+\frac{{{{{{{{{{\rm{Cov}}}}}}}}}}({X}_{N},K)}{{\sigma }_{N}^{2}}\frac{\left[{{{{{{{\rm{e}}}}}}}}^{-\kappa \tau }-{{{{{{{\rm{e}}}}}}}}^{-\beta \tau }\right]}{\beta -\kappa }$ |
| *R*_(*M*)(*τ*) | ${{{{{{{\rm{e}}}}}}}}^{-\gamma \tau }+\beta \,\frac{{{{{{{{{{\rm{Cov}}}}}}}}}}({X}_{N},{X}_{M})}{{\sigma }_{M}^{2}}\,\frac{\left[{{{{{{{\rm{e}}}}}}}}^{-\beta \tau }-{{{{{{{{\rm{e}}}}}}}}}^{-\gamma \tau }\right]}{\gamma -\beta }+\beta \,\frac{{{{{{{{{{\rm{Cov}}}}}}}}}}({X}_{M},K)}{{\sigma }_{M}^{2}}$ |
|  | $\,\times \left[\frac{{{{{{{{{\rm{e}}}}}}}}}^{-\beta \tau }}{(\beta -\gamma )(\beta -\kappa )}+\frac{{{{{{{{{\rm{e}}}}}}}}}^{-\gamma \tau }}{(\gamma -\beta )(\gamma -\kappa )}+\frac{{{{{{{{{\rm{e}}}}}}}}}^{-\kappa \tau }}{(\kappa -\beta )(\kappa -\gamma )}\right]$ |

## Models can be distinguished using multimodal count data {#Sec10}

Even if our two models did not have identical first and second order moments, the shortcomings of moment-based model discrimination are becoming increasingly clear⁶⁸. Does the situation improve if we compare whole count distributions? To establish that the Γ-OU and CIR models are in principle discriminable, we performed an in silico experiment: first, (i) we generated noise-free synthetic data from the CIR model for many different parameter sets; then (ii) we compared the goodness-of-fit of each model to this synthetic data.

We chose to quantify the relative goodness-of-fit of each model via the *Bayes factor*, which is the ratio of the likelihood of each model given the data. Concretely, we computed the log Bayes factor

$${\log }_{10}{{{{{{{{{\rm{BF}}}}}}}}}} \ \colon =\ {\log }_{10}\left[\frac{P({{{{{{{{{\rm{data}}}}}}}}}}|{{{{{{{{{\rm{CIR}}}}}}}}}})}{P({{{{{{{{{\rm{data}}}}}}}}}}|{{\Gamma }}{{{{{{{{{\rm{-OU}}}}}}}}}})}\right]$$

for each of the synthetic data sets we considered. A log Bayes factor of close to zero means that neither model is preferred, while a log Bayes factor of magnitude at least 2—i.e., one model is at least a hundred times more likely than the other—is commonly considered decisive evidence that one model is superior, and will be used as our criterion for distinguishability.

Because we expect that model distinguishability primarily depends on distribution ‘shape’ (e.g., Poisson-like or negative binomial-like), and because shape appears to be controlled by where a parameter set resides in the two-dimensional space depicted in Fig. 2, we chose 100 parameter sets that uniformly cover this space. Parameters which do not strongly control distribution shape (the average transcription rate, splicing rate, and degradation rate) were held fixed.

For each parameter set, we generated 100 synthetic data sets, and averaged the corresponding log Bayes factors over them to account for sampling noise (Fig. 3a). We varied the number of cells per synthetic data set, and computed Bayes factors using (i) full joint distributions, (ii) nascent distributions only, and (iii) mature distributions only. As expected, distinguishability is higher when data sets have more cells, when multimodal data is used, and when the data are overdispersed rather than Poisson-like. Data from ≈ 1000 cells is required for the models to be distinguishable in most of parameter space. Using multimodal data instead of nascent or mature counts only can improve distinguishability by about an order of magnitude (Fig. 3b) on average. Changing the ground truth model (here, CIR) or values of the parameters held fixed (〈*K*〉, *β*, *γ*) does not qualitatively change the results (Supplementary Fig. 6).

![](https://doi.org/10.1038/s41467-022-34857-7/)

Model distinguishability and parameter inference.
**a** Log Bayes factors show models are distinguishable in most of parameter space. Plotted are the average log Bayes factors capped at 2 (a common threshold for decisive evidence in favor of one model). **b** Models are often strongly distinguishable. A slice of the 1000 cell row of the previous plot (without the cap at 2) for a moderate value of *κ*/(*κ* + *β* + *γ*). Using both nascent and mature data is better than using either individually, usually by at least an order of magnitude. **c** It is easy to distinguish the Γ-OU and CIR models from trivial models. Same axes as in (**b**). Discriminability of Γ-OU and CIR models versus Poisson and mixture models for a somewhat small value of *κ* (*κ*/(*κ* + *β* + *γ*) = 0.1), where discriminability is expected to be difficult. **d** Nascent and mature marginal distributions for the Γ-OU (red) and CIR (blue) models for a maximally distinguishable parameter set. Histograms show synthetic data (5000 cells), while the smooth lines show the exact results. **e** Bayesian inference of noise model parameters. We sampled the posterior distribution of the parameters of the Γ-OU model (assuming it is known that *β* = 1, *γ* = 1.7, and 〈*K*〉 = 10), given a synthetic data set of 1000 cells. Posteriors are presented in both the qualitative regimes space, and in terms of the original parameters. For very Poisson-like data, posteriors are broad in both spaces, because *κ* is no longer identifiable. MAP: mode of posterior, avg: average of posterior, true: true parameter values.

We would also like each model to be individually discriminable from ‘trivial’ models; one advantage of using Bayes factors to quantify discriminability here is that they automatically penalize model complexity. Using the same data sets, we compared each model with the constitutive and mixture models, and found generally strong distinguishability (Fig. 3c), with particularly high Bayes factors when comparing against the constitutive model.

How different are the predictions of the Γ-OU and CIR models when they are maximally distinguishable? For the parameter set with the maximum log Bayes factor, we found that the predicted distributions are still visually alike (Fig. 3d). This illustrates that, while probabilistic inference using whole distributions may succeed at performing model discrimination, many naïve approaches, such as those based on moments or single marginals, may fail.

## Accurate parameter recovery is possible {#Sec11}

Even if one can distinguish between the two noise models, it is possible that the biophysically interesting parameters controlling transcription rate variation (e.g., *κ* and *θ*) cannot be precisely inferred from steady-state RNA count data. In fact, ambiguity is fairly expected, since qualitative behavior only strongly depends on certain parameter ratios near limiting regimes (see Fig. 2 and Section 2.5 in the Supplementary Note). For example, when the gain ratio *θ*/(*θ* + *a*) is small, each model predicts Poisson-like RNA count distributions, which are not very sensitive to the value of *κ*.

To illustrate the conditions under which parameter recovery appears to be possible, we performed an in silico parameter recovery experiment with two parameter sets: one which is overdispersed, as transcriptomic data tends to be, and another which is very Poisson-like. For each parameter set, a noise-free synthetic data set of 1000 cells was generated from the Γ-OU model, and then a Bayesian parameter recovery analysis was performed to construct a posterior distribution of parameters that could have generated the data. One advantage of a Bayesian approach is that, in addition to obtaining a point estimate of the most likely parameter set given the data, one obtains a measure of uncertainty from the spread of this distribution.

We find that, in the typical scenario (overdispersed data), the posterior is fairly tight in both the qualitative regime space and in the original parameter space (Fig. 3e). Both *κ* and *θ* are fairly identifiable, allowing us to be optimistic that it is possible to infer biophysical parameters related to transcription rate variation from single-cell data. In the pessimistic scenario (Poisson-like data), model predictions appear to be ‘sloppy’ with respect to *κ*, as expected, yielding a broad distribution of possible *κ* and *θ* values.

## Multimodal count distributions in sequencing datasets suggest distinct modes of transcriptional regulation {#Sec12}

Even if the Γ-OU and CIR models can be distinguished and fit to data in principle, can they be distinguished and fit in practice? Real transcriptomic data feature additional noise due to technical errors⁶⁹, and possibly confounding influences due to phenomena like cell growth and division⁷⁰. One can also face serious model misspecification problems, where one finds that even though one model fits better than others, none of them fit particularly well.

To show that these models may be observed and distinguished in real datasets, we analyzed single-cell transcriptomic data with tens of thousands of genes from the glutamatergic neurons of four mice⁷¹ (31,649 genes after pseudoalignment yielding unspliced and spliced RNA counts^(72,73)). Because neurons generally do not grow or divide, their gene expression dynamics should not be confounded by the effects of cell growth and division. To guard against spurious conclusions related to both technical noise and model misspecification, we used a multi-step filtering procedure based on neuron subtypes from a single mouse dataset to choose genes to examine (“Methods” and Section 8 in the Supplementary Note).

We fit the Γ-OU and CIR models to the 80 genes that passed the filtering step (Fig. 4a) to data from four mice, using gradient descent to find the maximum likelihood parameter set, and using likelihood ratios for model selection. We discarded all results with absolute log-likelihood ratios above 150, as they appeared to reflect failure to converge to a satisfactory optimum (Supplementary Figs. 8–37). The likelihood ratios for the remaining 73 genes are depicted in Fig. 4b (points). To ensure that the likelihood ratios we obtained were not distorted by the omission of uncertainty in estimates, or potentially suboptimal fits, we further fit twelve of the genes using a Bayesian procedure like the one used in Fig. 3e, demonstrating the distribution of Bayes factors in the same axes (horizontal markers).

![](https://doi.org/10.1038/s41467-022-34857-7/)

Genes from comparable single-cell RNA sequencing datasets can be consistently assigned to a particular biophysical model of transcription.
**a** By fitting models in the limiting regimes and calculating model Akaike weights, visualized on a ternary diagram, we can obtain coarse gene model assignments (colors: regimes predicted by the partial fit; red: Γ-OU-like genes; blue: CIR-like genes; violet: mixture-like genes; gray: genes not consistently assigned to a limiting regime). **b** Likelihood ratios for selected genes are consistent across biological replicates, and favor categories consistent with predictions (colors: regimes predicted by the partial fit; points: likelihood ratios; horizontal line markers: Bayes factors; vertical lines: Bayes factor ranges; Bayes factor values beyond the plot bounds have been omitted. *n* = 4 biologically independent animals, with 5343, 6604, 5892, and 4497 cells per animal). **c** The differences between model best fits are reflected in raw count data (title colors: predicted regimes; lines: model fits at maximum likelihood parameter estimates; line colors: models; histograms: count data). **d** Non-distinguishable genes tend to lie in the slow-reversion and high-gain parameter regime; distinguishable genes vary more, but tend to have relatively high gain (colors: predicted regimes, large dots: genes illustrated in panel (**c**). Genes with absolute log-likelihood ratios above 150 have been excluded).

The predictions from the coarse filter were largely concordant with the results from the full model, suggesting that it is effective for selecting genes of interest from transcriptome-wide data. The model assignments were typically consistent among datasets. Although orthogonal targeted experiments are necessary to identify whether the proposed models effectively recapitulate the live-cell transcriptional dynamics, the reproducibility of the findings suggests directions and candidate genes for such investigations. Finally, the Bayes factors were largely quantitatively consistent with the likelihood ratios, suggesting that the approximations made in the gradient descent procedure do not substantially degrade the quality of the statistical results. However, we did observe several discrepancies between likelihood ratios and Bayes factors, confirming that the more computationally facile gradient descent procedure does not perfectly recapitulate the full Bayesian fit (cf. results for Ccdc39 and Birc6), possibly due to substantial omitted uncertainty in some genes’ parameters.

Five example fits are depicted in Fig. 4c, with the corresponding gene names color-coded according to the best-fit model (red: Γ-OU, blue: CIR, purple: mixture). The results for all genes and datasets are shown in Supplementary Figs. 8–37. Model discrepancies mostly appear to be due to differences in probability near distribution peaks. Interestingly, only either the nascent marginal or mature marginal exhibits obvious visual differences between model fits in some of the genes depicted here, further motivating the use of multimodal data.

The location of each best-fit parameter set in the qualitative regimes space is shown in Fig. 4d. Most Γ-OU fits exist in the top right corner, suggesting we are effectively fitting a standard geometric burst model in these cases. Nonetheless, there are a number of genes for which the parameter sets reside somewhere in the center, indicating that the full complexity of the Γ-OU or CIR models is necessary to describe the corresponding data.

The likelihood ratio procedure yields results that are (i) similar to the distribution shapes observed in the raw data, up to possible numerical errors; (ii) broadly consistent with the predictions from the reduced model fit, although some discrepancies do occur, particularly for ‘mixture-like’ genes that exhibit higher identifiability under the full model; (iii) qualitatively consistent between datasets; and (iv) largely, but not perfectly, coherent with a full Bayesian procedure. Therefore, the distributions associated with the proposed models can be distinguished in practice. Further, these differences can be probed using a range of tools, some more approximate and suited to genome-wide exploratory analysis, others more statistically rigorous and suited to detailed study of specific gene targets.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Discussion →](03-discussion.md)
