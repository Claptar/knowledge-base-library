---
title: DETERMINATION OF BIOLOGICAL DIFFERENCES
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DETERMINATION OF BIOLOGICAL DIFFERENCES

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The theoretical (Section 8.2) and numerical (Section 5.4) tools we have introduced provide a relatively simple framework for the determination of biophysical and technical parameters consistent with data under a particular set of hypotheses about the biophysics of transcription and chemistry of sequencing. Although the parameters are often challenging to identify precisely, we have shown technical differences can be satisfactorily accounted for by assuming that that biological differences between paired samples are minimal (Section 8.3).

A probabilistic understanding of technical noise is mandatory, and omitting it leads to the serious problems outlined in Sections 8.4 and B.3. Yet it is, in many important ways, secondary: we perform experiments to learn something about the biology of living cells, rather than nuisance technical effects. To that end, the promise of the mechanistic worldview consists of providing a biophysical, rather than phenomenological, alternative to analyses of biological heterogeneity. Once we have accounted for technical effects, we can ascribe differences in expression to specific mechanisms of regulation. These insights are necessarily incomplete: we may be able to find that certain biophysical parameters have changed, but cannot determine _how_ . Nevertheless, this approach is promising in light of orthogonal work studying the relationship between regulatory mechanisms and affected parameters [210]. In addition, the biophysical approach provides an avenue to probe subtle differences in copy number distributions that would not be identifiable using standard statistical methods [72].

### **9.1 The role of multimodal data in differential expression**

This section summarizes principles originally introduced in [107] and elaborated upon in [106] by G.G. and L.P. The approach was conceptualized by G.G. The collection of multimodal data, such as nascent and mature RNA counts, provides qualitatively different and more actionable information than the quantification of a single modality, and deserves particular attention. In Section 7.1, we found that bivariate data improve the identifiability of models and distinct parameter regimes. In the context of differential expression testing, the availability of multimodal data allows us to distinguish regulation trends that would otherwise be ambiguous.

111

To see why, we can compare the single-species and two-species cases. The singlespecies model of bursty transcription


yields a negative binomial distribution with shape _𝑘_ / _𝛾_ and scale _𝑏_ . Therefore, we can identify these two parameters and no more based on steady-state measurements, regardless of the amount of data. If we observe a difference in _𝑏_ between conditions, we can confidently attribute it to a change in the burst size. However, if we observe a difference in _𝑘_ / _𝛾_ , we cannot uniquely attribute it to the turnover rate _𝛾_ or the burst frequency _𝑘_ . We can _assume_ that turnover is less likely to be modulated than the transcription rate [201], but this assumption is impossible to justify based on the data alone.

If we fit the two-species model in Section 4.6.2, we obtain estimates of _𝑘_ / _𝛽_ , _𝑘_ / _𝛾_ , and _𝑏_ . Superficially, these estimates suffer from the same problem: we cannot uniquely identify _𝑘_ , _𝛽_ , and _𝛾_ . However, this scenario is fundamentally different: it is implausible that _𝛽_ and _𝛾_ are simultaneously modulated, because these processes occur in distinct compartments. This assumption is quite a bit milder than excluding the modulation of turnover altogether. Therefore, if we observe _synchronized_ changes in _𝑘_ / _𝛽_ and _𝑘_ / _𝛾_ , with the same sign and similar magnitudes, we may treat them as evidence for the modulation of the burst frequency.

Indeed, differences in inferred normalized splicing and degradation rates demonstrate striking and pervasive correlations (third panel of Figure 9.1a), suggesting that they should appropriately be attributed to burst frequency modulation. Certain genes lie off the diagonal, suggesting that turnover modulation has a role to play in certain narrow cases. Therefore, if the approximate equality Δ log10 _𝑘𝛽_<sup>≈Δ log10</sup> _<u>𝛾𝑘</u>_ holds, we generally assume that Δ log10 _𝑘_ has a similar magnitude, but the opposite sign. We average the two to estimate the burst frequency modulation:


### **9.2 Mechanistic differential expression**

This section summarizes a portion of [107] and [106] by G.G. and L.P. The analysis was conceptualized by G.G. and L.P. and designed and implemented by G.G.

With this physical and statistical machinery in hand, we strive to generalize the identification of expression differences and ascribe them to specific mechanisms.

112


Figure 9.1: The _Monod_ mechanistic framework generalizes differential expression testing to the identification of genes with distributional differences, without requiring substantial changes in average expression.

**a.** Mouse neuron cell types show strong co-variation in normalized splicing and degradation rate differences, suggesting potential burst frequency modulation (orange dashed line: identity; black: genes retained after statistical testing; red: known glutamatergic markers; light teal: known GABAergic markers).

**b.** Differential expression analysis identifies genes that exhibit consistent inter-cell type parameter modulation in neuron populations (gray: parameters for genes not identified as differentially expressed by the _𝑡_ -test and a fold change (FC) criterion; light red: parameters identified as higher in the glutamatergic cell type; light teal: parameters identified as higher in the GABAergic cell type).

**c.** The differences between mouse glutamatergic and GABAergic cell types, computed from four independent replicates, include genes with substantial noise enhancement but little to no change in average expression, which may reflect biophysically important compensation mechanisms (light red points: genes with significantly higher noise in glutamatergic cells; light teal points: genes with significantly higher noise in GABAergic cells; gray points: all other genes; solid diagonal line: parameter combinations where burst size and frequency differences compensate to maintain a constant average expression; dashed diagonal lines: ±1 log2 expression fold change region about the constant-average expression line; vertical and horizontal lines: parameter combinations where burst size and frequency, respectively, do not change).

**d.** Differences in inferred noise behaviors reflect differences in distribution shapes (light red: glutamatergic cell type; light teal: GABAergic cell type; histograms: raw counts; lines: _Monod_ fits; top row: mature RNA marginal; bottom row: nascent RNA marginal).

**e.** Perturbation by IdU, which triggers DNA damage and repair, rarely changes expression levels, but induces genome-wide noise enhancement [40] detectable by _Monod_ (lines and gray points: as in **c** ; red points and labels: well-fit, moderateexpression genes identified as highly noise-enhanced).

113

In typical transcriptomics workflows, the determination of differences between cell types or conditions often reduces to the determination of differentially expressed (DE) genes, which exhibit statistically significant differences in their average copy numbers. However, the identification of DE genes requires careful accounting for technical covariates [187]. In addition, the data may exhibit _compensating_ mechanistic effects that change the distribution while keeping the averages constant, which would not be identifiable by standard statistical methods [69, 72, 205].

We propose that differential expression testing should be generalized to the identification of modulated parameters. We use the notation “DE-Θ” to denote criteria using Θ — which may be a data moment or an inferred biophysical parameter — as a test statistic. The mechanistic DE approach is reminiscent of negative binomial regression methods previously proposed for scRNA-seq data [9, 123, 186], but has key distinctions: the model is not assumed to be closed-form or univariate, and the differences are explained in terms of specific regulatory mechanisms rather than descriptive parameters.

If we do not have any replicates — for example, if we seek to compare the differences between cell types in a single tissue — we can essentially use outlier calling procedures on the distributions of parameter differences (the marginals of panels of Figure 9.1a) to propose DE-Θ genes. This approach complements, rather than substitutes typical statistical procedures: in the demonstrated example, many well-known marker genes for the GABAergic and glutamatergic cell types (red: glutamatergic; light teal: GABAergic) exhibit such low expression outside their characteristic cell types that their parameters cannot be accurately identified, and the differences are uninterpretable.

If we _do_ have have independent biological replicates, we can use standard statistical procedures, such as the _𝑡_ -test. We illustrate DE- _𝑏_ , DE- _𝛽_ / _𝑘_ , and DE- _𝛾_ / _𝑘_ genes with consistent parameter differences between GABAergic and glutamatergic cell types, computed from four mouse neuron datasets, in Figure 9.1b. Per Section 9.1, these differences can be particularly naturally summarized in terms of burst size and frequency differences (Figure 9.1c), in the spirit of [65, 172].

Most interestingly, we found several genes that consistently exhibited transcriptional parameter modulation but exhibited approximately constant mean mature RNA expression between cell types, and would not be identifiable by standard statistical procedures (colored points in Figure 9.1c). The discovered genes are indicated according to the cell type differences’ effect on noise: genes highlighted in red exhibit

114

more overdispersion in the glutamatergic population, whereas genes highlighted in light teal exhibit more overdispersion in the GABAergic population. These genes exhibit only minor differences in average expression, and fall fairly close to the line of expression identity (solid diagonal line in Figure 9.1c), where an increase in burst size is precisely compensated by a decrease in the burst frequency.

The differences in parameters are reflected in the data distributions and the model fits. For example, _Nin_ and _Bach2_ visually exhibit higher noise in the glutamatergic and GABAergic populations, respectively (Figure 9.1d). The mature count averages are, on the other hand, fairly close ( _Nin_ Glu: 1.7, GABA: 0.98; _Bach2_ Glu: 0.87, GABA: 1.4).

Many of the genes identified by this procedure were associated with neuronal structure and development. _Socs2_ , _Igf1r_ , _Itga4_ , and _Dpysl3_ are involved in differentiation and neurite outgrowth [152, 164, 250, 284]. _Bach2_ and _Cxxc4_ induce feedback in neuronal development, apparently to maintain differentiated status in neurons [93, 258]. _Mid2_ and _Nin_ are associated with neural development regulation through microtubule organization [18, 273]. _Egln1_ is linked to neuronal apoptosis [174]. _Fam174a_ is involved in lipid metabolism and membrane structure [142]. _Rnf152_ and _Rgmb_ are broadly implicated in neural development [55, 212, 243]. _Scg3_ appears to have a functional role in secretory granule biogenesis [177].

Some identified genes have less clear mechanistic connections to brain structure and function. _Ankrd40_ is uncharacterized and is not known to have neural functions [82], but the similar gene product _Ankrd6_ has an obscure neurodevelopmental role [288]. _Stx4a_ is localized on synaptic membranes [6]. _Slc39a11_ is a zinc transporter, involved in brain function [68]. _Mblac2_ codes for an obscure protein that may have enzymatic activity [190]. _Ccdc136_ appears to have a DNA regulatory role [194], but may be involved in neural speech pathology [3]. The role of _Crtc3_ in the rodent brain appears to be restricted to stress response [240]. _Il34_ is a microglial marker; microglia have immune and regulatory functions in the brain [15].

Although these distinctions are statistically identifiable, the import and basis of cell type differences in distribution rather than average expression is as of yet obscure. These differences appear to be associated with compensatory mechanisms and motivate further study of the role of noise in biophysical systems.

115

### **<u>9.3 Genome-wide noise modulation</u>**

This section summarizes a portion of [106] by G.G. and L.P. The analysis was conceptualized, designed, and implemented by G.G.

Such compensatory mechanisms, where substantial distributional changes are associated with only minor average expression changes, have long been explored using theoretical tools [205]. These theoretical studies have come to fruition: recent studies have found that the introduction of the modified nucleotide 5-iodo-2<sup>′</sup> - deoxyuridine (IdU) to a culture medium enhances transcriptional noise, but keeps average expression constant, hinting at a genome-wide mechanism for compensation [40, 72].

The mechanistic approach also enables the summary of such far-reaching perturbations, which move beyond the usual marker gene paradigm. Although the model required to fully recapitulate the dynamics of DNA damage repair involved in this process is sophisticated, we found that we could characterize the effects of IdU using a simple bursty model. We fit the nascent and mature data from control and IdU datasets using _Monod_ . As in Section 8.3, technical noise parameters were not readily identifiable from the 10x v2 sequencing data. We assumed the parameters were in a region we previously discovered for this technology (Figure 8.3c), and analyzed biophysical parameters under that assumption.

We found that the IdU-perturbed cell culture exhibited striking noise amplification, with very limited differences in mean expression (Figure 9.1e). This result strongly contrasts, e.g., Figure 9.1c, which shows fairly symmetric noise amplification and reduction between cell types. The asymmetry in the findings are consistent with the authors’ conclusions and orthogonal validation, which likewise found that burst size increases and burst frequency decreases in the IdU condition [40].

We selected a set of well-fit genes that exhibited particularly high modulation and had average expression greater than 1 in at least one of the conditions for further analysis, identifying _Stx7_ , _Washc5_ , _Apod_ , _Eif2ak2_ , _Ubr2_ , _Cnnm2_ , _Dram2_ , _Zfp110_ , _Cul4a_ , _Ddx19b_ , and _Yap1_ (red points in Figure 9.1c). Interestingly, two of these genes are directly related to the DNA damage activity of IdU: _Dram2_ is involved in the autophagic response to DNA damage repair, whereas _Cul4a_ is involved in the turnover of DNA repair proteins. Several other genes more generally mediate the cellular stress response: _Zfp110_ , _Eif2ak2_ , and _Yap1_ regulate apoptosis, whereas _Ddx19b_ may be active in stress granules. The role of the remaining genes is obscure: _Stx7_ and _Washc5_ are related to vesicular function, _Apod_ is involved in lipid

116

metabolism, _Ubr2_ controls ubiquitination, and _Cnnm2_ appears to be involved in ion transport [209].

We were able to partially compare our results for _Sox2_ , _Nanog_ , and _Mtpap_ , whose transcriptional parameters were computed from fluorescence data in [40, 72]. We did not observe _Sox2_ expression in either dataset. _Nanog_ was rejected by our goodness-of-fit procedure. This is, in principle, consistent with the results in Table S2 of [72], which report gene on fractions near 30-55%; this regime violates the assumptions of the bursty model (gene on fraction tending to zero). The inferred signs for _Mtpap_ parameter modulation agreed with Figure S4 of [40], although we obtained rather different magnitudes (log2 fold changes of ≈−0 _._ 3 by smFISH vs. ≈−1 _._ 5 by _Monod_ for burst frequency; ≈ 2 by smFISH vs. ≈ 1 _._ 3 by _Monod_ for burst size). Therefore, although the genome-wide trends broadly recapitulate the mechanistic explanations provided by the authors, and some of the high-noise genes appear to be implicated in DNA repair and stress, the quantitative comparison of fluorescence and sequencing data requires further analytical work.

In sum, the mechanistic DE framework offers several avenues for the identification of biophysical mechanisms. Substantial differences in expression can be quantitatively explained by the effects of transcriptional burst size and frequency modulation. In addition, differences in _distributions_ can be explained by simultaneous, and counteracting, modulation of both parameters, revealing complexity that would be lost by a simple consideration of the averages and suggesting directions for further experiments.

117

_C h a p t e r 10_

---

[← SEQUENCING MODEL SPECIFICATION](15-sequencing-model-specification.md) · [Up: contents](index.md) · [MODELING MULTI-GENE SYSTEMS →](17-modeling-multi-gene-systems.md)
