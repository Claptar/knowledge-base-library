---
title: TECHNOLOGIES, DESIDERATA, AND AXIOMS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# TECHNOLOGIES, DESIDERATA, AND AXIOMS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

And should I then presume? And how should I begin?

_The Love Song of J. Alfred Prufrock_

T.S. Eliot

To begin, we need to understand what questions the current analyses attempt to treat, and how they answer them using the data at hand. Given a methodology, we can analyze or reverse-engineer its logic, “problematize” the assumptions by explicitly acknowledging them [14, 163], then investigate whether we could improve, validate, or falsify these assumptions to enhance the workflow.

### **2.1 The two perspectives on the negative binomial distribution**

This section adapts portions of [115] by G.G., J.J.V., and L.P., [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P., and [112] by G.G., M.F., T.C., and L.P. This perspective on the relationship between sequence census and mechanistic methods was conceptualized by G.G., J.J.V., and L.P.

This high-level course of action is, of course, far too generic, and requires an illustration. To that end, we introduce single-cell RNA sequencing (scRNA-seq) and present a case study to motivate mechanistic modeling. This motivation is one of many, but we find this one to be particularly compelling. Nevertheless, it does rely on some background knowledge of statistics and single-cell RNA sequencing analyses, and the reader from outside the field can skip to Section 2.2 for a qualitative summary if the case study proves too technical.

### **2.1.1 The negative binomial distribution as an effective data summary**

When we perform a single-cell sequencing experiment, we obtain a collection of reads, which represent a selection of the RNA content in living cells [332]. These reads are barcoded; by judiciously using the barcodes and the sequence information, the reads can be converted to a collection of molecule counts, integer numbers _𝑥_ cg for each cell c and gene g [196, 197]. To accomplish the goals of the downstream analysis — the typical systems biology tasks of identifying of cell types, aggregating

4

them into trajectories, discovering gene modules that consistently differ between cell types or throughout a differentiation trajectory, and visualizing low-dimensional summaries reflecting some component of the data structure — we manipulate the data in a way that reveals the “signal,” while eliminating or controlling for the “noise” of the sequencing procedure.

There is a dizzying variety of approaches to this problem. For example, we could build a graph that encodes distances between the observed cell states **x** c, then use community detection algorithms to find cliques that coarsely represent cell types, shortest traversal paths that can correspond to trajectories, and neighborhoodpreserving embeddings that summarize the graph structure in a low-dimensional visualization. Yet a naïve application of graph algorithms — essentially, a purely non-parametric, “data scientific” approach that attempts to summarize the count matrix — can be misled by the variability and noise in the data: a graph is a discrete, deterministic structure and does not “know” which data points are reliable, or how heterogeneity is to be treated. In addition, this approach restricts statistical interpretability: we can certainly claim that two cliques correspond to distinct cell types, but to justify this claim, we need to construct some measure of statistical confidence. In its simplest Platonic form, this amounts to computing an effect size (how distinct are these cell types?) and a _𝑝_ -value (would we plausibly see such a difference even if the cells were from a single cell type?). We are forced, then, to wrestle with uncomfortable questions like “what, precisely, do we mean by ‘cell type?”’ and “what is the correct noise model for the _𝑝_ -value computation?”

These uncomfortable questions lead us to adopt the methods of statistics. For example, we can axiomatize a cell type as an internally homogeneous population with a particular average expression, then use the central limit theorem [154] to compare the averages of discovered subpopulations and draw statistical conclusions [187]. This approach — which is ostensibly parametric, but does not make particularly strong assumptions about the RNA count distribution — is sensible, but its application may create further challenges. Single-cell RNA sequencing data are discrete and sparse; even if the central limit theorem holds in the limit, it may perform very poorly for realistic dataset sizes [206]. In addition, merely comparing averages prevents the discovery of biologically interesting cases where the RNA distributions change while keeping the mean constant [205]. Other strategies, such as “binarizing” the data — considering only the presence or absence of molecules, rather than the precise count value [36, 230] — are mathematically distinct, but conceptually

5

similar, as they also discard the vast majority of the data, potentially sacrificing some signal in the process.

If the central limit theorem and analogous approaches are insufficient, we can move on to parametric statistics, and improve the statistical power at the expense of possibly introducing model misspecification. Many options are available, but the discrete, positive nature of count data are a particularly natural fit for distributions on the natural numbers N0. For example, we attempt to represent an observation as a draw from a Poisson distribution:


The Poisson distribution is straightforward to evaluate as long as we know _𝜇_ cg. Of course, the problem of identifying this mean parameter is grossly underspecified: if every cell c can have an different mean, and we place no restrictions on its variation, we are unable to learn anything meaningful. We can constrain the problem further, in the most extreme case by proposing that


which implies that all of the cells are independent and identically distributed draws from a common distribution. This model is insufficient to summarize real datasets: the Poisson distribution has a variance equal to the mean ( _𝜇_ = _𝜎_<sup>2</sup> ), whereas gene count data typically have a variance higher than the mean ( _𝜎_<sup>2</sup> _> 𝜇_ ). This “overdispersion” is ubiquitous and does not seem to be explainable by, e.g., the presence of multiple cell subpopulations, because the subpopulations are, in turn, also overdispersed (as in Fig. 1a of [160]).

The next simplest model is the negative binomial:


This distribution gives us the correct support and distribution shape: the variance is


which is strictly higher than the Poisson distribution with the same mean, and can, in fact, be made arbitrarily high by tuning _𝜈_ .

Equation 2.3 is still overparametrized, and needs to be constrained to actually summarize data. There does not seem to be an obvious way to do so from first

6

principles, but analyses of pre-barcode sequencing technologies [9] have proposed that the _𝜇_ term of Equation 2.4, which coincides with the Poisson variance, should be attributed to purely technical Poisson “shot noise,” whereas the residual overdispersion should be attributed to a combination of technical and biological effects, which produce a gamma distribution of molecule concentrations. This approach commonly parametrizes _𝜇_ as the product of a large, sample-dependent, technical “library size” parameter and a small, compositional, sample and g-dependent “fractional abundance” parameter. The g-dependent “dispersion” parameter _𝜈_ is typically heavily constrained by _𝜇_ or set to a constant [9, 238].

Throughout the adoption of single-cell and single-molecule barcoding technologies, this approach has persisted with only minor modifications: there are compositional abundance and “library size” parameters, now unique to a particular cell c rather than the entire sample; there is a “dispersion” parameter, which varies less arbitrarily, if at all; if we assume the compositional gene expression is Gamma-distributed, we can summarize the dataset by using a Poisson model for the technical effects. This set of assumptions produces a tractable negative binomial distribution for the RNA copy number. The specifics of the procedure vary — for example, some studies augment the basic framework with more or less complex noise terms and linking functions, and this summary is nowhere near comprehensive — but despite these numerous variations on the theme, the basic points show up time and again [52, 116, 123, 186, 191, 247, 308].

It is useful to keep in mind that the parametric approach is only one of many. The specter of the negative binomial distribution haunts the non-parametric methods nevertheless. Very few analyses are run on raw data; typically, a workflow normalizes the data with respect to the total per-cell molecule count to account for “library size” variability; afterward, some flavor of log-transformation is applied to abundance matrix to bring the gene expression values, which vary over many orders of magnitude, to a common scale [134]. These transformations are optimal for a stabilizing high- _𝜇_ , uniform- _𝜈_ negative binomial distributions [4, 34] under the assumptions outlined above, although they may fail elsewhere [32].

### **2.1.2 The negative binomial distribution as the consequence of a biophysical model**

Although the foregoing description is tremendously oversimplified, it is conceptually in line with the picture presented in reviews [4, 134, 187]. Yet, by presenting it, we

7

have engaged in some sleight of hand: what, precisely, does the negative binomial model _mean_ ? What biophysical and chemical phenomena do its gamma and Poisson components represent? What biological assumptions do we make when we suppose that, e.g., _𝜈_ is constant across all cells, whereas _𝜇_ can vary? And can we justify these assumptions based on data external to the sequencing experiment?

To answer these questions, we can turn to the field of fluorescence transcriptomics, which uses fluorescent probes that light up when they bind to RNA, allowing us to count individual molecules [102, 233]. Yet we do not observe the gamma distributions implied by the sequencing analyses: fluorescence data are overwhelmingly overdispersed [16, 89, 102, 214, 232, 244], and negative binomial-like distributions effectively fit the observed counts [72, 91, 121, 233]. This immediately implies a problem with our interpretation of Equation 2.4: if the Poisson component _𝜇_ were a purely technical consequence of the sequencing technology, we should not observe it using fluorescence imaging. Yet we do, which suggests that it is a fundamental component of the _biology_ .

Indeed, the fluorescence transcriptomics field typically explains the overdispersion by appealing to the bursting behavior observed in live-cell measurements: transcription is discontinuous and intermittent; the production of RNA is relatively rare; however, when it _does_ take place, it produces many molecules at once [65, 92, 161, 170, 210, 293]. The effort to fully characterize these behaviors has led to mechanistic models such as


i.e., at each transcriptional event generates a random number _𝐵_ of molecules X; after some delay, the molecules are degraded. These two reactions happen at rates _𝑘_ and _𝛾_ (Section A.8.1). Although this model is highly abstracted, it can represent a variety of mechanisms, such as the switching between active and inactive transcriptional states due to activator binding [219, 233]. By setting up and solving a stochastic formulation of Equation 2.5, we obtain precisely the same negative binomial distribution as in Equation 2.3. Of course, transcriptional bursting is only a part of the whole picture, and even non-bursty genes may be overdispersed due to cell-to-cell differences in transcription rates:


where _𝐾_ is a random variable. If _𝐾_ is gamma, the stationary distribution of X is negative binomial yet again, although its parameters have a different interpretation.

8

Such models have been used to describe the variability in transcription rates observed across cell sizes [150, 214, 272, 283]. There is no reason why these phenomena should be mutually exclusive, and it appears fair to suppose that both bursting and cell-to-cell variability have some role in the control of expression.

### **<u>2.2 Motivations for mechanistic models</u>**

This section adapts portions of [115] by G.G., J.J.V., and L.P., [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P., and [112] by G.G., M.F., T.C., and L.P. This review of motivations was conceptualized by G.G. and L.P.

The essential take-away from Section 2.1 is that sequencing and fluorescence transcriptomics analyses are concerned with the same problem: the summary and interpretation of noisy RNA copy number datasets. To treat this problem, they even use similar tools, such as the negative binomial distribution. However, these superficial similarities hide profound conceptual differences: the _meaning_ attributed to these tools is different in the two subfields; single-molecule stochasticity is front and center in fluorescence transcriptomics, but sidelined and treated as purely technical in sequencing transcriptomics.

This observation is somewhat troubling: single-molecule stochasticity is ubiquitous [244], and its omission makes sequencing analyses incoherent with known biology. That said, in spite of these discrepancies, it is not accurate to claim that the scRNA-seq field has entirely neglected the results from fluorescence transcriptomics. Several articles explicitly point to transcriptional variation as a source of biological variability, and either directly use the solutions to mechanistic models [8, 69, 124] or augment them with a model of technical noise [37, 116, 159, 278, 279, 308]. However, this approach is comparatively rare, and has not yet gained traction as part of typical pipelines.

Here, it is reasonable to ask: _why_ do the theoretical foundations matter? So far, all we have demonstrated is that both subfields use similar tools, e.g., the negative binomial distribution. Even if their bases and interpretations are subtly different, the end result is much the same. What is the actual impact of adopting one or another worldview?

It turns out that these latent problems come to a head when we attempt to treat broader questions and types of data. For example, typical single-cell analyses use the _mature_ transcriptome, i.e., only the counts corresponding to exonic regions. Yet it is also possible to align to intronic regions to obtain two data matrices: the usual mature RNA matrix, as well as a _nascent_ RNA matrix, containing all counts associated

9

with intronic regions; as introns are typically removed during RNA processing, the nascent molecules represent an earlier stage in the RNA life-cycle. The usual descriptive analyses do not have a prescription for simultaneously treating these data types: single-cell analyses omit the nascent RNA; single-nucleus analyses add the two matrices; the “best” approach is controversial, and there does not appear to be a straightforward basis for choosing between the two (Section 8.3).

Yet, in the mechanistic worldview, the solution is almost trivial. There is a causal relationship between the two modalities: nascent RNA are eventually converted to mature RNA. If are confident in the premise that transcription is bursty, we can immediately write down a reasonable model that unifies the two data types:


Of course, this model is simplistic — the binary assignment may be overly reductive (Section B.1). Further, we have omitted ambiguities; for example, purely exonic reads may arise from either nascent or mature molecules (Section B.2). Nevertheless, we have successfully encoded the transcriptional biophysics and the causal relationship between the two species, and created a theoretical substrate for representing more sophisticated phenomena, such as technical variability. Indeed, a principled approach to “data integration” is only one of the benefits of adopting the mechanistic worldview, and there is a multi-faceted variety of arguments for its broader adoption.

**The biological motivation.** By investigating data through the lens of biophysical parameters, we can learn something about the mechanisms that give rise to the data, going beyond data summary to characterize the underlying biological processes. For example, finding that a gene’s burst size has changed is more interpretable and actionable than finding that a negative binomial distribution’s scale parameter has changed, even if these discoveries are mathematically identical: the former proposes a specific transcriptional mechanism. Just as valuably, this perspective allows us to _falsify_ models: if the observed distributions cannot be reproduced by a mathematical model, our conceptualization of the underlying physics is somehow incomplete and must be adjusted.

**The physical motivation.** The discovery, design, and falsification of biophysical laws deserves special mention: it is part of a broad, interdisciplinary effort to ground the study of biology in physical foundations. Its origins date back to the

10

mid-twentieth century [24, 25, 145], and recent work in this direction [201, 221] can be bolstered by the integration of genome-wide data.

**The statistical motivation, pt. I.** As discussed above, to make confident summaries and predictions, accounting for uncertainty is mandatory. Although certain alternatives, such as the central limit theorem and binarization, can help, discrete models produce more statistical power in the sparse, low-copy number limit relevant to scRNA-seq data.

**The statistical motivation, pt. II.** The statistical advantages of parametric, mechanistic models range beyond loss function book-keeping. By instantiating models and performing a thorough mathematical analysis, we can discover which features are readily identifiable, which are more challenging to infer, and which are entirely impossible to characterize given a particular type of data. For example, the models in Equations 2.5 and 2.6 produce identical distributions at steady state, so attempting to distinguish them purely based on counts of X is futile.

**The experimental motivation.** We can use the results of statistical investigations to design readouts or control experiments that answer questions of interest. For instance, the aforementioned negative binomial models _can_ be distinguished with two-species data (in the vein of Equation 2.7, and as discussed in Section 7.1). In addition, the explicit modeling of technical artifacts can provide a quantitative understanding of the differences between experimental workflows (Chapter 8).

**The synthesis motivation.** As alluded to elsewhere, if we wish to compare sequencing data to other modalities, such as fluorescence transcriptomics, we need to, on one hand, encode the premise that the underlying biology is identical, and, on the other, attribute any differences to specific technical artifacts (Section 8.2). This is easiest done through biophysical modeling.

**The control motivation.** Even if we choose not to invest all of our efforts into the analysis of mechanistic models, an understanding of common axioms lets us generate realistic simulated data to benchmark sequencing workflows. In addition, the mathematical framework allows us to systematically investigate implicit limitations and contradictions of common data analysis procedures (Sections 6.1 and 8.4).

11

**The financial motivation.** Experiments are expensive; computational data analysis is less so, but still requires non-negligible investment; theory is cheap. It is financially responsible to understand the limitations of experiments and analyses — i.e., which questions can we confidently answer based on a particular dataset? — before collecting any data, instead of discovering these limitations _post hoc_ . In addition, a thorough, physically grounded investigation of production pipelines can help identify otherwise obscure technical artifacts and prevent target-oriented industry investigations from pursuing dead ends.

**The ethical motivation.** The collection of sequencing data is necessarily invasive: it requires the isolation and destruction of living cells. In a scientific context, this entails raising and euthanizing animal test subjects. In a therapeutic context, this entails collecting samples from severely ill or deceased patients. Both of these scenarios involve complicated ethical questions, but it appears most justifiable to strive to minimize invasive procedures by making the most of fewer and smaller datasets.

**The synthetic biology motivation.** The characterization of transcriptional kinetics has an additional, longer-term perspective: the design of synthetic gene circuits. To design a system, it is essential to understand the physics of its constituent parts; for transcriptional systems, an understanding of single-molecule stochasticity is mandatory.

### **2.3 Technologies and axioms**

We are primarily interested in fitting readily available data from the commercial 10x Genomics platform [332]. We largely focus on the single-cell v3 version of the technology, which offers high-throughput short-read sequencing; however, we occasionally consider the older, lower-throughput v2 technology and the singlenucleus variant of v3 (Sections 8.3 and 9.3). We provide a conceptual overview of the 10x workflow in Sections 4.4.2 and 4.4.3. Nevertheless, we anticipate that the theoretical framework outlined here is applicable to other modalities that can be collected through sequencing, and we outline the prospects in Chapter 11.

We particularly focus on nascent and mature molecule counts. As discussed in Section B.1, this terminology is somewhat non-standard, and intended to emphasize that the modeling approach represents a generic two-stage RNA life-cycle. We adopt the bioinformatic conventions of [168, 197] to identify RNA with intronic content

12

as “nascent” and RNA without intronic content as “mature.” This identification is necessarily imperfect, but helpful, as bioinformatic pipelines for distinguishing and counting these molecular species are readily available [168, 197, 264]. In one case study, we use data from a nanopore-based technology that provides considerably more resolution and a way forward for more detailed models (Section 10.2). However, this technology has not yet seen widespread adoption, so we operate with the most readily available data types at the time. We omit the treatment of ambiguity, largely for computational purposes, but we express our reservations in Section B.2. We speculate that, in many cases, ambiguity can be elided because many nominally ambiguous purely exonic reads lie in the 3<sup>′</sup> untranslated region, which suggests they arise from fully processed, poly(A)-capped molecules [131, 217].

It remains to define a set of modeling principles and axioms. Of course, a wide variety of options are available to represent the underlying biology: we can track individual RNA bases; we can treat each molecule as continuous and track its length during production and degradation; we can treat each molecule as an interchangeable discrete entity with no internal structure; we can even take a wider view and consider molecule concentrations instead of counts. Due to the considerable success of discrete stochastic models of biology, as well as the concerning points raised in Section 2.1, we adopt the third axiom: molecules have no internal structure, and are instantaneously produced and degraded. Under certain assumptions, this can be viewed as a simplified representation of a model that _does_ represent the internal structure, focusing on a single molecular region (in the vein of 5<sup>′</sup> and 3<sup>′</sup> probes in [319]). However, the choice is mostly motivated by theoretical and computational facility. We adopt the same framework for the experimental components of the systems we study, taking advantage of the barcodes to identify individual molecules. Again, various other options exist — such as treating reads, or even accounting for the uncertainty in sequencing individual bases — but this level of detail seems somewhat excessive at this preliminary stage.

We almost exclusively consider Markov models, whose future behavior only depends on the current state, rather than any past states. The framework we set up turns out to easily generalize to non-Markov models (Section 4.3.2), and we briefly consider and compare them against some Markov candidates (Section 7.3). However, we find that the considerably simpler Markov models largely suffice, and attempt to avoid introducing additional complexity when it does not appear to be required by the data.

13

In spite of their popularity (as outlined in Section 2.1), we do not generally consider “cell size” or “library size” models that couple the distributions of different genes. The sole exception is the preliminary investigation in Section 10.3, which proposes one possible basis for such variation. This choice necessarily limits our ability to describe systematic variation in molecular copy numbers, as well as co-variation between genes. However, the current theoretical understanding of these phenomena is somewhat limited, and we hesitate to make any specific modeling assumptions about them. This aspect is also somewhat beside the point. The models we present here are the base case, where we assume these sources of variability can be neglected; if desired, this assumption can be relaxed, and the models can be augmented accordingly by conditioning on some distribution. In other words, if there is some coupling variable Θ, we marginalize over Θ to compute distributions _𝑃_ ( _𝑥_ ):


which _still_ requires computing _𝑃_ ( _𝑥_ ; Θ) at some stage. This is the component of the problem we consider here. We anticipate that a detailed understanding of these phenomena will require considerable further work.

14

_C h a p t e r 3_

---

[← INTRODUCTION AND OUTLINE](08-introduction-and-outline.md) · [Up: contents](index.md) · [MATHEMATICAL TOOLS AND PRELIMINARIES →](10-mathematical-tools-and-preliminaries.md)
