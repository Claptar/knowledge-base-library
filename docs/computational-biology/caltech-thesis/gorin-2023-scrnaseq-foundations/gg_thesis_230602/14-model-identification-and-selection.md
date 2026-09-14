---
title: MODEL IDENTIFICATION AND SELECTION
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MODEL IDENTIFICATION AND SELECTION

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A considerable fraction of the variability in single-cell datasets arises from cellto-cell and time-dependent variation in the transcription rates. These sources of variation control distribution shapes. We seek to apply the models developed in Chapter 4 to obtain insights into this variability and explain distributional differences through mechanisms. By carefully analyzing candidate models, we can characterize the prospects for model selection: for example, if different transcriptional models produce nearly identical distributions, selection is impossible and the choice of model is somewhat arbitrary.

Therefore, the probabilistic analysis of transcriptomic data entails two key challenges: the identification of parameters consistent with the data under a particular model (statistical inference) and the discrimination between distinct hypotheses (model selection). To understand how well we can distinguish different parameter regimes and models, we analyze the models’ distributions and compare them using simulated and biological data.

### **<u>7.1 The role of multimodal data in inference</u>**

This section adapts a portion of [115] by G.G., J.J.V., and L.P. The descriptions and mathematical foundations adapt a portion of [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P. G.G. and J.J.V. performed the model development and mathematical analysis. G.G. conceptualized, designed, and implemented the case study shown here.

Portions of this case study recapitulate the methods and conclusions of [103] by G.G. and L.P. G.G. and L.P. conceptualized this study. G.G. designed and implemented the analysis.

More interestingly, such analysis can guide the design of experiments: models may be indistinguishable based on some kinds of data, but not others. This perspective has guided the interest in characterizing noise behaviors [204, 205]: distributions provide strictly more information than averages, and allow us to distinguish between regulatory behaviors. Similarly, multivariate distributions provide more information than marginal distributions. Obtaining _different_ data (multiple molecular modalities) is qualitatively more useful than obtaining more data (a larger number of cells) or better data (observations less corrupted by noise).

83


Figure 7.1: The stochastic analysis of biological and technical phenomena facilitates the identification and inference of transcriptional models.

**a.** A minimal model that accounts for intrinsic (single-molecule), extrinsic (cell-to-cell), and technical (experimental) variability: one of three time-varying transcriptional processes _𝐾_ generates molecules, which are spliced with rate _𝛽_ , degraded with rate _𝛾_ , and observed with probability _𝑝_ . Given a set of observations, we can use statistics to narrow down the range of consistent models. **b.** Overdispersed regimes are not mutually identifiable given a single modality (likelihood computed using nascent RNA data for 200 simulated cells; Γ-OU ground truth; red point: true parameter set in the mixture-like regime; color: log-likelihood of data, yellow is higher, 90th percentile marked with magenta hatching; blue: an illustrative parameter set in a burst-like parameter regime with a similar nascent marginal but drastically different joint structure).

**c.** The mixture-like and burst-like regimes become mutually identifiable with multimodal data (likelihood computed using bivariate RNA data for 200 simulated cells; all other conventions as in **b** ). **d.** Nascent marginal and joint distributions at the points indicated in **b** and **c** . Nascent distributions nearly overlap.

**e.** - **f.** Given a location in parameter space, models are easier to distinguish using multiple modalities. However, the performance varies widely based on the location in parameter space and the specific candidate models, and decreases with drop-out (Γ-OU Akaike weights under Γ-OU ground truth, average of _𝑛_ = 50 replicates using 200 simulated cells; color: Akaike weight of correct model, yellow is higher, regions with weight < 0.5 marked with black hatching; large circles: illustrative parameter sets; smaller circles: distributions obtained by applying _𝑝_ = 50%, 75%, and 85% dropout to illustrative parameter sets while keeping the averages constant).

**g.** The telegraph model has a well-distinguishable bimodal limit when the process autocorrelation is slower than RNA dynamics, which improves its identifiability (lines: the three candidate models’ nascent marginal distributions at the olive point in **e** and **f** ).

**h.** In the bursty limit, the three models look qualitatively similar, limiting identifiability (lines: the three candidate models’ nascent marginal distributions at the pink point in **e** and **f** ).

84

We illustrate this key point by considering three transcriptional drivers coupled to a two-stage RNA process ( _𝑛_ = 2). The transcription rate is time-varying, with rate _𝐾_ . Each biological molecule has a probability _𝑝_ of being observed in the final dataset, which amounts to evaluating the generating functions at _𝑝𝑢𝑁_ and _𝑝𝑢𝑀_ . The processes and their physical interpretations are shown in Figure 7.1a.

First, we consider two models that provide an explanatory framework for the extrinsic noise model described in Section 4.6.3. As biological distributions are overdispersed, it appears reasonable to propose that transcription rates _𝐾_ vary between cells, and the gamma model for _𝐾_ produces plausible negative binomial count distributions. However, this approach has some gaps in its physical motivation: what is the biological meaning of this distribution’s parameters? And is it really reasonable to assume that the rates are “frozen,” and remain as they are for all time in a given cell?

To account for possible time variation, we introduce a class of transcriptional models that balance interpretability and tractability, and generalize the mixture model. Although various biological details underlying transcription may be complicated, we assume they can be captured by an effective transcription rate _𝐾𝑡_ , which is stochastic and varies with time. This transcription rate randomly fluctuates about its mean value, with the precise nature of its fluctuations dependent upon the fine biophysical details of transcription. To guarantee that they can recapitulate the mixture model, we consider stochastic differential equation _𝐾𝑡_ with a gamma steadystate distribution.

These models’ functional forms have previously been used in biology [89, 140, 228, 242, 325], but a key point has been underexplored: the resulting RNA distributions are _not_ generally Poisson-gamma, and directly depend on the details of the transcriptional process dynamics. In other words, the trajectory shapes matter a great deal, and to accurately represent this form of “extrinsic” stochasticity, we need to specify the precise functional form for _𝐾𝑡_ . Conversely, given a set of candidate models, we may be able to distinguish them on the basis of RNA count distributions. As the stochastic differential equation driver models have identical count expectations and variances, we need to bring to bear the theoretical framework laid out in Chapter 4 to compute full probability mass functions.

The first candidate model is the gamma Ornstein–Uhlenbeck (Γ-OU) process ( _𝑁_ = 1,

85

_𝑚_ = 1) [241]:


where the mean-reversion term − _𝜅𝑦𝑡_ represents DNA winding, which makes RNA polymerase binding less favorable and causes the transcription rate to decrease, whereas the compound Poisson process jump term _𝐿𝑡_ represents the arrivals of topoisomerases, which increase propensity for transcription by exponentially distributed jumps. In the parlance of Chapter 4,


where _𝑎_ is the arrival frequency and _𝜃_ is the average jump size.

The second candidate model is the Cox–Ingersoll–Ross (CIR) process ( _𝑁_ = 1, _𝑚_ = 1) [62]:


where _𝑊𝑡_ denotes the Brownian motion, the drift term _𝑎_ is the production rate of a regulator, _𝜅_ is its degradation rate, and _𝜃_ — essentially, a “process gain” — relates the concentration of the regulator to the activity of the promoter. To derive this identity, we assume that the regulator is present at high concentration and rapidly equilibrates with the bound species. This system is characterized by the parameters and operators


The stationary distribution of the Γ-OU and CIR processes is gamma, with shape _𝑎_ / _𝜅_ and scale _𝜃_ , i.e., mean _𝑎𝜃_ / _𝜅_ and variance _𝑎𝜃_<sup>2</sup> / _𝜅_ . In addition, their autocorrelation function is _𝑒_<sup>−</sup><sup>_𝜅𝑡_</sup> .

Finally, the third candidate model is the more conventional telegraph process ( _𝑁_ = 2, _𝑚_ = 0) [219], which describes the Markovian activation and deactivation of a gene. This system is characterized by


86

The stationary distribution of this process is Bernoulli scaled by _𝑘_ init, with mean _𝑘𝑘_ onon+ _𝑘𝑘_ <u>initoff</u><sup>and variance</sup> ( _𝑘𝑘_ onon _𝑘_ +off _𝑘_ off _𝑘_ <u>init</u><sup>2</sup> )<sup>2.Its autocorrelation function is</sup><sup>_𝑒_−(</sup><sup>_𝑘_on+</sup><sup>_𝑘_off)</sup><sup>_𝑡_[95].</sup>

Even if the true averages of the transcriptional strength and molecular abundances are fixed, the systems can exhibit a wide variety of distribution shapes and statistical behaviors. This variety can be summarized by a two-dimensional parameter space, ranging over (0 _,_ 1). The “timescale separation” governs the relative timescales of the transcriptional and molecular processes; if it is high, the transcriptional process is faster than RNA turnover. The “noise intensity” governs the variability in the transcriptional process: if it is high, the process exhibits substantial variability that translates to overdispersion in the RNA distributions. The bottom edge of this parameter space produces Poisson distributions of RNA, the top left corner produces Poisson mixtures of the law of _𝐾_ , and the top right corner yields bursty dynamics that do not typically have simple analytical solutions [113].

For the two-species SDE driver models, the reduced parameters take the following form:


Equation 7.6 is defined with reference to the process parameters of the Γ-OU and CIR drivers [113]. It remains to define _𝜅_ , _𝜃_ , and _𝑎_ in terms of _𝑘_ on, _𝑘_ off, and _𝑘_ init for the telegraph process. The correct identification is:


These definitions are not arbitrary, as they endow the system with lower moments that match the SDE formulation: autocorrelation function _𝑒_<sup>−</sup><sup>_𝜅𝑡_</sup> , mean _𝑎𝜃_ / _𝜅_ , and variance _𝜃𝜇𝐾_ . In addition, the system has the correct geometric burst limit ( _𝑘_ init _, 𝑘_ off →∞) with burst size _𝜃_ / _𝜅_ → _𝑘_ init/ _𝑘_ off and burst frequency _𝑎_ → _𝑘_ on [233]; this limit matches the Γ-OU one. Therefore, given x, y, _𝜇𝐾_ , _𝛽_ , and _𝛾_ , we can construct the parameters of the underlying transcriptional driver.

Although different x _,_ y regimes reflect very different transcriptional kinetics, they can produce indistinguishable distributions. Figure 7.1b demonstrates the likelihood landscape of a dataset generated from the Γ-OU transcriptional model, evaluated

87

using the nascent marginal and _𝑝_ = 1 (no technical noise). The mixture-like true parameters are indicated by a red point and the top decile of likelihoods is indicated by hatching. The Γ-OU model has a gamma stationary distribution, which produces approximately Poisson-gamma, or negative binomial, RNA marginals in this regime. However, the bursty regime, indicated by a blue point, also yields a negative binomial-like marginal (reported in Equation 7.8), preventing us from identifying the kinetics. On the other hand, if we evaluate likelihoods using the entire two-species dataset, we obtain the landscape in Figure 7.1c: the symmetry is broken, and the parameters can be localized to the mixture-like regime. The source of this improved performance is evident from examining the distributions, shown in Figure 7.1d. The nascent marginals are essentially identical; no amount of purely nascent count data can distinguish between them. However, the bivariate distributions show subtle differences, such as higher nascent/mature correlations in the true regime, which can be used for inference.

In addition, the timescale separation and noise intensity determine the model distinguishability. Figure 7.1e demonstrates the average Akaike weight landscape of datasets generated from the Γ-OU model, computed using the nascent distribution at the same coordinate. We indicate the region _𝑤𝜛 >_ 1/2 by hatching. As the Akaike weight may be interpreted as a posterior model probability [38], this threshold gives even odds for choosing the correct model, on average. The intermediate regime, indicated by a large olive green point, tends to yield fairly high Akaike weights, translating to good model identifiability. On the other hand, the burst-like regime, indicated by a large pink point, provides considerably less ability to distinguish the models. As expected, the situation improves somewhat when using bivariate data (Figure 7.1f): the Akaike weights increase throughout the parameter space, and the bursty regime data move closer to even odds for model selection. To illustrate the source of the identifiability challenges, we plot the nascent marginals of the models at the two points. In the intermediate regime, the Γ-OU and CIR models yield moderately different distributions, whereas the telegraph model is immediately distinguishable by its bimodality (Figure 7.1g). In contrast, in the bursty regime, the distributions are all unimodal and less identifiable (Figure 7.1h); the Γ-OU and telegraph marginals are particularly similar, as they converge to the same negative binomial limit.

Interestingly, this formulation fully characterizes the effect of certain forms of technical noise. If the transcriptional and observed molecular averages are fixed, but

88

the experiment fails to capture some molecules, the distributions are identical to those obtained by deflating the transcriptional noise intensity. In other words, even though technical noise affects the molecules, its theoretical effects are indistinguishable from decreasing the variability of the transcriptional process. As the noise levels increase, the RNA distributions are pushed toward the indistinguishable Poisson limit at the bottom edge of the reduced parameter space. We quantify how rapidly the information degrades by plotting smaller circles in Figure 7.1e-f to indicate the effect of 50%, 75%, and 85% dropout, in that order from top to bottom. This result is an extremely general and fundamental consequence of the form of the solution (Section A.8.4).

In sum, in certain overdispersed regimes, candidate drivers _are_ mutually distinguishable, and the identification of transcriptional models is qualitatively and quantitatively facilitated by the collection of multimodal data. In addition, by exploiting the mathematical structure of the ODEs defining the transcriptional processes, we find that the impact of the simplest form of drop-out noise can be conceptualized as the reduction of the transcription rate scale, rendering these parameters non-identifiable.

### **7.2 The identification of transcriptional driving** **<u>processes</u>**

This section adapts a portion of [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P. The analysis was conceptualized by J.J.V. and G.G., designed by J.J.V., M.F., and G.G., and implemented by G.G. and M.F.

Even if the Γ-OU and CIR models can be distinguished and fit to data in principle, can they be distinguished and fit _in practice_ ? Real transcriptomic data feature additional noise due to technical errors, and possibly confounding influences due to phenomena like cell growth and division [283]. One can also face serious model misspecification problems, where one finds that even though one model fits better than others, none of them fit particularly well.

To show that these models may be observed and distinguished in real datasets, we analyzed single-cell transcriptomic data with tens of thousands of genes from the glutamatergic neurons of four mice [321]. Because neurons generally do not grow or divide, their gene expression dynamics should not be confounded by the effects of cell growth and division. To guard against spurious conclusions related to both technical noise and model misspecification, we used a multi-step filtering procedure based on a neuron subtypes from single mouse dataset to choose genes to examine.

As we are primarily interested in demonstrating whether the novel solutions for

89


Figure 7.2: Genes from comparable single-cell RNA sequencing datasets can be consistently assigned to a particular biophysical model of transcription. **a.** By fitting models in the limiting regimes and calculating model Akaike weights, visualized on a ternary diagram, we can obtain coarse gene model assignments (colors: regimes predicted by the partial fit; red: Γ-OU-like genes; blue: CIR-like genes; violet: mixture-like genes; gray: genes not consistently assigned to a limiting regime).

**b.** Likelihood ratios for selected genes are consistent across biological replicates, and favor categories consistent with predictions (colors: regimes predicted by the partial fit; points: likelihood ratios; horizontal line markers: Bayes factors; vertical lines: Bayes factor ranges; Bayes factor values beyond the plot bounds have been omitted. _𝑛_ = 4 biologically independent animals, with 5,343, 6,604, 5,892, and 4,497 cells per animal).

**c.** The differences between model best fits are reflected in raw count data (title colors: predicted regimes; lines: model fits at maximum likelihood parameter estimates; line colors: models; histograms: count data).

**d.** Non-distinguishable genes tend to lie in the slow-reversion and high-gain parameter regime; distinguishable genes vary more, but tend to have relatively high gain (colors: predicted regimes, large dots: genes illustrated in panel **c** . Genes with absolute log-likelihood ratios above 150 have been excluded).

90

Γ-OU and CIR models can be supported by data, we fit the two models’ (distinct) burst-like limits, where x _,_ y → 1 and (identical) mixture-like limits, where x → 0 and y → 1, using _Monod_ , assuming no technical noise, to five glutamatergic neuron subtypes from a single mouse. The burst-like limit of the Γ-OU model is given in Section 4.6.2, the mixture-like limit is given in Section 4.6.3, while the burst-like limit of the CIR model has the following generating function:


where _𝑏_ = _𝜃_ / _𝜅_ and _𝑈𝑁_ takes the usual form in Equation 4.55 (Section A.8.2). This somewhat degenerate<sup>5</sup> limit describes driving by a process with infinitely many jumps in each finite time interval. Although this driver has been encountered before in the mathematical finance literature [292], the solution does not appear to have been previously reported [20, 22].

We computed the Akaike weights of the three limits for all genes (results for one subtype shown in Figure 7.2a). Finally, we selected genes that most consistently agreed with the distributions in these limits (colored points in Figure 7.2a), and extracted the genes with the best fits to the optimal models.

We fit the Γ-OU and CIR models to the 80 genes that passed the filtering step to glutamatergic neuron data from four mice, using gradient descent to find the maximum likelihood parameter set, and computed the likelihood ratios for the models (Equation 3.45), discarding poorly fit genes. The likelihood ratios for the remaining 73 genes are depicted in Figure 7.2b (points). To ensure that the likelihood ratios we obtained were not distorted by the omission of uncertainty in estimates, or potentially suboptimal fits, we further fit twelve of the genes using a Bayesian procedure, displaying the distribution of Bayes factors (Equation 3.46) in the same axes (horizontal markers).

The predictions from the coarse filter were largely concordant with the results from the full model, suggesting that it is effective for selecting genes of interest from transcriptome-wide data. The model assignments were typically consistent among datasets. Although orthogonal targeted experiments are necessary to identify whether the proposed models effectively recapitulate the live-cell transcriptional dynamics, the reproducibility of the findings suggests directions and candidate genes for such investigations. Finally, the Bayes factors were largely quantitatively consistent with the likelihood ratios, suggesting that the approximations made in the gradient descent procedure do not substantially degrade the quality of the statis-

91

tical results. However, we did observe several discrepancies between likelihood ratios and Bayes factors, confirming that the more computationally facile gradient descent procedure does not perfectly recapitulate the full Bayesian fit (cf. results for _Ccdc39_ and _Birc6_ ), possibly due to substantial omitted uncertainty in some genes’ parameters.

Five example fits are depicted in Figure 7.2c, with the corresponding gene names color-coded according to the best-fit model (red: Γ-OU, blue: CIR, purple: mixture). Model distinctions mostly appear to be due to differences in probability near distribution peaks. Interestingly, only either the nascent marginal or mature marginal exhibits obvious visual differences between model fits in some of the genes depicted here, further motivating the use of multimodal data.

The location of each best-fit parameter set in the qualitative regimes space is shown in Figure 7.2d. Most Γ-OU fits exist in the top right corner, suggesting we are effectively fitting a standard geometric burst model in these cases. Nonetheless, there are a number of genes for which the parameter sets reside somewhere in the center, indicating that the full complexity of the Γ-OU or CIR models is necessary to describe the corresponding data.

Despite the models’ simplicity, the results suggest that single-cell RNA sequencing data may be sufficiently rich to enable Bayesian model discrimination between superficially similar regulatory schema. Certain genes demonstrate reproducible differences between the two considered SDE drivers, which may imply differences in the underlying regulatory motifs. Interpreting the specific biochemical meaning of the findings is challenging without accounting for features which have been omitted in the discussion thus far, such as technical noise and additional complexities in downstream processing of RNA. Nevertheless, fine details of transcription — including DNA mechanics and gene regulation — appear to have signatures in single-cell data, and a model-based, hypothesis-driven paradigm can help identify them. Further, these fine details can be probed using a range of tools, some more approximate and suited to genome-wide exploratory analysis, others more statistically rigorous and suited to detailed study of gene targets.

### **7.3 RNA processing**

This section adapts a portion of [114] by G.G., S.Y., and L.P. The theoretical results and data analyses were conceptualized, designed, and implemented by G.G. Although we have largely considered Markovian processes, this model class may

92

not be sufficient to describe biology. On one hand, there is considerable evidence that bacterial and mammalian transcription is typically Markovian and bursty [65, 92, 170, 239, 244], although more sophisticated extensions have been proposed and applied [125, 170, 334]. Similarly, the results of genome-wide inhibition experiments are largely consistent with Markovian RNA degradation, with exponentially decaying RNA levels over time [255].

On theotherhand, thekineticsofsplicingandexportareratherlesswell-characterized. For computational and mathematical tractability, we typically assume that splicing is a single-step Markovian process, whereas export is rapid enough to neglect. These assumptions appear sufficient to fit data generated by single-cell RNA sequencing, but they have not been studied in detail. Indeed, they are counterintuitive: nuclear retention _is_ important [16], and previous studies have used fairly sophisticated models to describe it [86], although others have achieved reasonable results under a Markovian hypothesis [16, 127, 206]. In addition, we have elided a considerable amount of complexity by identifying nascent RNA with intron-containing molecules and mature RNA with all others (Section B.1). Indeed, we may reasonably expect that splicing often [60] occurs co-transcriptionally [74], such that intron-containing molecules are in the process of elongation. In this case, a Markovian model is _a priori_ incorrect, because elongation needs to complete before the molecule can be released and degraded [59].

These assumptions are testable using single-cell and single-nucleus RNA sequencing (snRNA-seq) datasets and the suite of models in Chapter 4. Conversely, testing them allows us to understand the qualitative differences, if any, between these data types. The splicing dynamics are relevant for all datasets, but the transport dynamics are motivated by the narrower goal of interpreting single-nucleus datasets. In singlecell datasets, we can, in principle, suppose that nuclear transport dynamics are rapid and the degradation is approximately Markovian. However, single-nucleus technologies isolate individual nuclei (Figure 7.3a), so we need to explicitly model the transport term to construct a stochastic model. First, we seek to understand whether single-nucleus data _require_ models that are substantially different from single-cell data, whether the Markovian efflux hypothesis is sufficient to describe the removal of mature molecules from nuclei. Second, we seek to characterize whether the Markovian splicing hypothesis holds. Finally, we seek to understand the extent to which single-cell and single-nucleus data allow for model identification.

We consider the standard bursty model discussed in Section 4.6.2, as well as the

93

two models shown in Figure 7.3b, which replace one or the other of the downstream Markovian processes with a deterministic one. By applying the methods in Section 4.3.2, we find that the process with delayed efflux has the log-generating function


This fairly complex expression produces the expected negative binomial nascent marginal.

On the other hand, the process with delayed splicing has the log-generating function


This generating function is separable with respect to _𝑢𝑁_ and _𝑢𝑀_ , which implies that the nascent and mature distributions are statistically independent. The mature count distribution is negative binomial, whereas the nascent one is geometric-Poisson or Pólya–Aeppli. This result generalizes the single-species case reported in [151].

We fit the three models using _Monod_ , omitting technical noise. The models were separately fit to GABAergic and glutamatergic cell types from two mouse brain samples [321], one generated using single-cell sequencing and one generated using single-nucleus sequencing, as well as single-cell and single-nucleus data from pericentral, periportal, and interzonal hepatocytes from a single human liver sample [11]. Upon fitting the MLEs, we computed the models’ likelihood ratios relative to the Markovian model.

We did not observe a systematic bias toward the delayed efflux model in either the whole-cell (Figure 7.3c) or the nuclear data (Figure 7.3d). The log-likelihood ratios were symmetric and near zero in all considered cases, suggesting the data were insufficient to strongly favor either model in any of the datasets. This result suggests that the Markovian model is broadly reasonable for nuclear transport.

In contrast, the delayed splicing model was considerably less favored, with loglikelihood ratios tending to be negative (Figure 7.3e-f). The strength of evidence against the models was lower in the single-nucleus data. This loss of statistical identifiability concords with intuition: the bursty Markovian and delayed-efflux models afford identical negative binomial nascent RNA marginals, requiring a large amount of mature RNA to distinguish the models, which the nuclear sequencing

94


Figure 7.3: The comparison of stochastic model predictions facilitates the identification of RNA processing mechanisms compatible with data. **a.** An outline of the experimental differences between single-cell and single-nucleus sequencing technologies.

**b** . The reaction schema of the considered models: DNA generates nascent RNA with transcriptional burst frequency _𝑘_ and burst size _𝑏_ , the nascent RNA are converted to mature RNA; the mature RNA are removed from the system, either by nuclear transport or by cytoplasmic degradation.

**c.** In whole-cell data, likelihood ratios do not systematically favor either the Markovian or the deterministically delayed efflux model (colors: cell types; red: Allen data; blue-green: Andrews data; lines: kernel density estimates).

**d.** In nuclear data, likelihood ratios do not systematically favor either the Markovian or the deterministically delayed efflux model (conventions as in **c** ).

**e.** In whole-cell data, likelihood ratios typically favor the Markovian model over the deterministically delayed splicing model (conventions as in **c** ).

**f.** In nuclear data, likelihood ratios typically favor the Markovian model over the deterministically delayed splicing model (conventions as in **c** ).

protocol lacks. The delayed splicing model has a different nascent marginal, and appeared to be more distinguishable from the negative binomial.

Overall, the hypothesis of Markovian, one-step splicing is useful despite its simplicity and apparent conflict with the understanding of transcriptional elongation. The simplest converse assumption — that splicing has a deterministic waiting time — produces substantially worse fits across a variety of data. On the other hand, the nucleus transport dynamics are consistent with either model, and we can say very little about them because the single-nucleus data have low mature RNA content. Nevertheless, the Markovian model appears to suffice.

95

_C h a p t e r 8_

---

[← SNAPSHOT INFERENCE](13-snapshot-inference.md) · [Up: contents](index.md) · [SEQUENCING MODEL SPECIFICATION →](15-sequencing-model-specification.md)
