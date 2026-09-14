---
title: QUALITATIVE DISCUSSION OF SEQUENCING PROCEDURES AND THEIR CAVEATS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# QUALITATIVE DISCUSSION OF SEQUENCING PROCEDURES AND THEIR CAVEATS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **B.1 Notes on nomenclature and binary assignment**

This section summarizes and unifies a portion of [112] by G.G., M.F., T.C., and L.P., as well as [44] by M.C.<sup>_★_</sup> , G.G.<sup>_★_</sup> , Y.C., T.C., and L.P. This theoretical discussion was written by G.G.

In the field of microbiology, “nascent” RNA is often, but not always, used to characterize the mRNA molecules in the process of synthesis, associated to a DNA strand via an RNA polymerase complex [53, 54, 239, 319]. In this framework, the “mature” transcriptome is simply the complement of the nascent transcriptome, i.e., all molecules that are not chemically associated to a DNA strand. Therefore, the canonical definition of “nascent” RNA is equivalent to _transcribing_ RNA, which is a polymeric structure with a particular sequence.

Transcribing RNA can be observed directly through electron micrography [54]. However, more typically, it is investigated through more or less direct experimental proxies that can be scaled to many genes and cells at a time. In the single-cell fluorescence subfield, DNA or membrane staining can be used to identify bright spots localized to the nucleus, which is treated as signal from RNA at the transcription site [121, 206]; this signal may include contributions from RNA incidentally, or mechanistically, retained at a DNA locus [319]. In this strategy, “nascent” molecules are DNA-associated. Alternatively, and perhaps more commonly, transcribing molecules have been studied by using probes targeted to the 5<sup>′</sup> and 3<sup>′</sup> regions [251, 309, 318, 327], or to intronic and exonic regions [16, 252, 262, 307]. In this strategy, “nascent” molecules contain a particular region, either synthesized earlier or removed later in the RNA life-cycle.

The use of intron data as a proxy for active transcription is reminiscent of, but distinct from sequence census [316] strategies that directly study RNA sequences. These strategies, in turn, typically use chemical methods to enrich for newly transcribed RNA. For example, Reimer et al. isolate chromatin, then deplete sequences that have been post-transcriptionally poly(A) tailed [235]. Analogously, Drexler et al. use 4-thiouridine (4sU) labeling to enrich for newly synthesized molecules [76].

213

These approaches may produce conflicting results; for example, introns may be rich both in poly(A) handles [168] and 4sU targets [235], giving rise to obscure technical effects. Therefore, these “processed” or “temporally labeled” proxies are coarsely representative of transcriptional dynamics, and their quantitative interpretability is unclear as of yet.

The sequence content may be used more directly, by conceding that DNA association or localization are not easily accessible by sequence census methods, and treating splicing _per se_ . This approach has a fairly long history. Intronic quantification has been used to characterize transcriptional mechanisms in microarray datasets [326], and to characterize differentiation programs in RNA sequencing [223, 224]. In single-cell RNA sequencing, intronic content has been leveraged to identify transient behaviors from snapshot data [168], albeit with some outstanding theoretical concerns and caveats (Section 6.1). Briefly, it is, in principle, possible to coarsely classify molecules with intronic content as “unspliced” or “pre-mRNA” and aggregate all others as “spliced,” “mature,” or simply “mRNA.”

The quantification of transcripts so classified is a relatively straightforward genomic alignment problem. The multiple available implementations [80, 168, 197, 264] tend to disagree on the appropriate assignment of ambiguous sequencing reads [112, 264], obscuring a more fundamental problem: the binary classification is somewhat arbitrary [33, 76, 158, 194], and it is likely that detailed splicing graph models will be necessary in the future (as proposed Section 10.2).

We can illustrate the problem using the simplest example of a three-exon, two-intron gene, with a “parent” transcript _𝐸_ 1 _𝐼_ 1 _𝐸_ 2 _𝐼_ 2 _𝐸_ 3. It seems reasonable enough to call _𝐸_ 1 _𝐼_ 1 _𝐸_ 2 _𝐼_ 2 _𝐸_ 3 “unspliced” and to call “terminal” transcript _𝐸_ 1 _𝐸_ 2 _𝐸_ 3 “spliced.” But what of the “intermediate” transcripts _𝐸_ 1 _𝐸_ 2 _𝐼_ 2 _𝐸_ 3 and _𝐸_ 1 _𝐼_ 1 _𝐸_ 2 _𝐸_ 3? Even if we have perfect information about the sequence content, by placing intronic reads into the “unspliced” category, we conflate the parent and intermediate transcripts. On the other hand, if we place all barcodes with splice junctions into the “spliced” category, we conflate the intermediate and terminal transcripts. Adding more complexity, some isoforms may retain introns through alternative splicing mechanisms; for example, the intermediate transcripts may be exported, translated, and degraded alongside the terminal one. Of course, in practice, the “parent” transcript may not actually exist as a distinct species if _𝐼_ 1 is removed before the transcription of _𝐸_ 3 is completed. The focus on sequence is yet another step removed from the transcriptional dynamics, particularly since some of the splicing processes may

214

occur after transcriptional elongation is complete [60].

Adding yet more complexity to the modeling, “mature” — whether “off-template,” “spliced,” or “processed” — molecules are not immediately available for degradation; first, the process of nuclear export must take place. Studies that presuppose access to imaging data tend to model it explicitly [27, 86, 127, 206, 261]. However, this approach has not been applied in sequencing assays, as current technologies do not distinguish nuclear and cytoplasmic molecules. Furthermore, comparisons of paired single-cell and single-nucleus datasets are hampered by the limited characterization of the noise sources in the latter technology.

Pending the development of more sophisticated sequencing and alignment technologies, as well as the implementation of tractable models of biology, the data exploration portion of our study focuses on the “spliced” and “unspliced” matrices generated by _kallisto | bustools_ [197]. This choice is a compromise, and we adopt it after considering the following factors:

- Availability of quantification workflows: spliced and unspliced matrices are straightforward to generate.

- Model tractability: the two-stage models can be evaluated; more sophisticated models require new algorithms, because they involve underspecified, highdimensional distributions (as alluded to in Chapter 5 and Section 10.2).

- The scope of sequencing data: single-cell protocols do not yet give access to sub-cellular information, so inference of elongation or nuclear retention dynamics is acutely underspecified.

We use the terms “nascent” and “mature” to identify the unspliced and spliced RNA matrices. This choice of nomenclature is deliberate. Although it somewhat conflicts with the established microbiology literature, this terminology is intended to emphasize the models’ generality. The two-stage Markovian process is axiomatic. The specific identities assigned to the mathematical objects may range beyond counts identified by sequence census methods. They may represent the discretized and subtracted intensities of 3<sup>′</sup> , 5<sup>′</sup> , intron, or exon fluorescent probes, the counts of molecules within and outside the nuclear envelope, or polymerase counts obtained by micrography. Therefore, the terminology should be taken in the sense used for similar non-delayed models in [42, 86, 90, 91].

215

In sum, we cannot justify the two-stage model from first principles: the biology is far too complicated, and we cannot possibly assert that this simplistic model accurately represents the complex polymeric phenomena occurring in living cells. Instead, we emphasize two points.

1. The theoretical framework does not depend on these assumptions and identifications, and can be extended to account for other phenomena.

2. The two-stage model typically produces at least fair fits to the data.

This appears to be sufficient to provide a fair first-order treatment of the data at hand.

### **B.2 Notes on ambiguity**

This section reproduces a portion of the supplement to [115] by G.G., J.J.V., and L.P. This theoretical discussion was largely written by G.G., with some essential background research by J.J.V.

The binary assignment problems outlined above arise even with perfect data — but we do not typically have perfect data. In Section 4.4.3, we mathematically formalized potential ambiguities in the quantification of different transcripts, mentioning two special cases of perfect identifiability and perfect ambiguity. We did not elaborate on this model component further, as it is, at this time, less immediately actionable than other components, and requires fairly considerable bioinformatic infrastructure to integrate with analysis. In the current section, we explore this model in more detail.

Even the simplest system, shown in Figure B.1a, can contain ambiguity that limits or prevents the identification of transcriptional dynamics. In this illustrative example, we consider a gene with only one intron and two flanking exonic sequences. We suppose that quantification and assignment only consider whether the read overlaps an intron or splice junction. An intron-containing read uniquely identifies the transcript as nascent, whereas a junction-spanning read uniquely identifies the transcript as mature. On the other hand, a fully exonic read does not provide any information about the source molecule. For the sake of completeness, we use “read” as a shorthand for the union of all reads corresponding to a particular UMI: since fragmentation is random, a given UMI will be associated with reads that cover slightly different regions.

The abundance of fully exonic reads depends on the structure and poly(A) content of the source transcript, as well as the sequencing technology. For example, in Figure

216


Figure B.1: Potential sources of short-read sequencing ambiguity in a hypothetical one-intron, two-exon transcript.

**a.** Possible splicing information conveyed by reads in the hypothetical transcript (magenta: reads that only contain exonic information; dark gray: reads that contain intronic information; dark blue: reads that overlap a splice junction. Blue block: exon; gray block: present intron; line: excised intron. 3<sup>′</sup> end is toward the left).

**b.** Categories of reads that can be obtained by sequencing the transcript, assuming no endogenous poly(A) content (cyan block: technical reads and indices; dotted lines: residual inserts not observed by sequencing; red block: poly(A) sequence). **c.** Categories of reads that can be obtained by capturing a transcript at an endogenous, intronic poly(A) sequence (conventions as in **a** and **b** ).

B.1b, we consider reads that can be obtained from a gene that has little to no genomic poly(A) content (red). The unspliced molecules, as well as spliced molecules that have not yet been capped (top), cannot be observed at all. Therefore, their kinetics are not identifiable. On the other hand, the fully mature, poly(A)-tailed transcript (bottom) can be captured at the tail. This capture pattern can give rise to junction reads or formally non-identifiable exonic reads. If the 3<sup>′</sup> exon is particularly long relative to fragment length, sequenced fragments will be enriched for purely exonic reads in the 3<sup>′</sup> exon. Analogously, if fragment length and the 3<sup>′</sup> exon are long relative to read length, sequenced fragments will be enriched for exonic reads in the 3<sup>′</sup> exon. In Figure B.1c, we illustrate the analogous patterns that can emerge if the unspliced molecule has a single intronic poly(A) region. If the intron and read length are short relative to fragment length, sequencing will produce reads in the 3<sup>′</sup> exon.

To characterize transcriptional kinetics, we seek to quantify transient transcripts,

217

which may or may not be mutually identifiable. This is infeasible to optimize on an experimental level. Even in the simple example we provided for illustration, to characterize the source transcript, the transcript region, fragment, and read lengths need to reside in a regime that produces unambiguous reads. To identify the splice junction in Figure B.1b, we require fragments that are slightly longer than the 3<sup>′</sup> exon and reads that can cover the distance to the junction. However, read length cannot be changed without switching technologies; longer reads typically mean sacrificing the number of sampled cells [122, 226, 328]. In the same vein, fragmentation protocols cannot be easily interchanged, as they are optimized for a particular sequencing chemistry. Finally, even if these technical constraints were no object, it would _still_ be impossible to optimize for unambiguous capture genome-wide: intron and exon length vary over many orders of magnitude [184, 335] and require different read and fragment length regimes for different genes.

Hypothetically, it may be possible to parametrize the 𝒫<sup>_𝑎_</sup> matrix as in Section 4.4.3, and fit it alongside the biological noise parameters. This approach may not be entirely futile. For example, Equation 4.46 demonstrates the relevant generating function for two biological species and three identifiable equivalence classes: 1, unambiguous nascent, 2, unambiguous mature, 3, ambiguous. The marginal of the nascent species has a functional form distinct from the marginal of the mature species [261], which immediately implies that 𝒫1<sup>_𝑎_</sup> _,_ 3<sup>=0,𝒫</sup> 2<sup>_𝑎_</sup> _,_ 3<sup>_>_0producesdistributions</sup> functionally distinct from 𝒫2<sup>_𝑎_</sup> _,_ 3<sup>= 0, 𝒫</sup> 1<sup>_𝑎_</sup> _,_ 3<sup>_>_0.In other words, we ought to be able to</sup> distinguish the case where all ambiguous counts originate from nascent RNA from the case where they originate from mature RNA, at least in the limit of immaculate and infinite data. We do not, however, expect this approach to be practical for real datasets.

We speculate that it may be more productive to use genomic information to constrain the ambiguity properties, in a similar spirit to [131]. For example, if a read lies in the 3<sup>′</sup> untranslated region, _and_ we know there is little endogenous poly(A) content 3<sup>′</sup> of the read, then we should conclude the read is generated by priming at the poly(A) tail of a capped molecule. In other words, it may be possible to exploit the base information from the genome annotation, the fragment size distributions from orthogonal experiments, and the read size characteristic of the technology to directly construct the 𝒫<sup>_𝑎_</sup> matrix for each transcript.

We may illustrate this point in a more quantitative way. Consider the simplest case shown in Figure B.1, and further assume that poly(A) capping is rapid. Using

218

the notation in Equation 4.46, we find that 𝒫1<sup>_𝑎_</sup> _,_ 3<sup>=</sup><sup>_𝑝_(𝒻|1),i.e.,theprobabilityof</sup> sequencing a nascent molecule to obtain a read with an insert from the 3<sup>′</sup> exon. Analogously, 𝒫2<sup>_𝑎_</sup> _,_ 3<sup>=</sup><sup>_𝑝_(𝒶|2) +</sup><sup>_𝑝_(𝒸|2), i.e., the probability of sequencing a mature</sup> molecule to obtain a read with an insert from the 3<sup>′</sup> or 3<sup>′</sup> exon. It appears legitimate to propose that these probabilities are only dependent on the sequence and experimental conditions, and may be effectively approximated by exploiting polymer physics or long-read data.

On one hand, this example is somewhat trivial by design. On the other, even this simplified picture of splicing omits important features. First, we presuppose that annotations exist for all downstream transcripts. As alluded to in Section 10.2, this is not typically the case, and the identities of and causal relationships between intermediate transcripts are obscure without dedicated study. Second, we presuppose that transcripts can be described as some combination of introns and exons, which transform by the excision of introns. However, even this seemingly reasonable latent assumption ignores elongation, which has been the subject of considerable study elsewhere. For example, a “nascent” transcript may not exist as a physical object, because splicing may complete before the 3<sup>′</sup> exon is fully transcribed. A more biophysically realistic picture should take into account the fact that splicing occurs during and after elongation. In addition to these biological challenges, there is a variety of technical ones. For example, introns that have already been spliced out may, in principle, be captured and sequenced. If splicing is Markovian, this would be represented as a splitting reaction X →Y + Z, which is a splitting reaction not immediately tractable using our framework. Finally, due to a variety of technical effects, the reads themselves may have a more complex relationship to the source transcripts. These effects include strand invasion and aberrant priming, and may lead to reads containing antisense and template switch oligo sequences [1]. Formally, all of these effects can be integrated into a sufficiently complicated stochastic model. In practice, we recommend introducing complexity only when simpler models fail.

### **B.3 Notes on imputation and reconstruction**

This section reproduces a portion of the supplement to [112] by G.G., M.F., T.C., and L.P. This theoretical discussion was written by G.G.

In the current supplement, we point out that count “correction” through imputation can produce arbitrarily incorrect results. Although this result is fairly elementary, it does not appear to have been applied in the single-cell sequencing field, and raises

219

questions regarding standard imputation methods. Suppose we have a data point Dcg and the corresponding true mRNA abundance _𝑥_ cg for a particular molecular species, cell c, and gene g. Sequencing is not perfect: the data point Dcg is generated from _𝑥_ cg according to a non-deterministic schema, with an unknown probability law _𝑃_ (Dcg| _𝑥_ cg).

Two problems emerge. First, a point estimate of _𝑥_ cg based on observed Dcg is necessarily incomplete: the sequencing process induces an entire distribution of possible _𝑥_ cg. This conditional distribution is given by Bayes’ formula:


Assigning a single value is questionable, and downplays the effects of uncertainty. This remains a problem even if a theoretically optimal choice is taken, such as the point estimate


Second, the conditional distribution depends on _𝑃_ ( _𝑥_ cg), the actual ground truth distribution. This distribution is unknown and needs to be identified and fit based on the data. Therefore, any imputation procedure that assigns a point estimate without considering the underlying distribution is _a priori_ distortive.

In other words, this Bayesian argument illustrates that meaningful count correction is impossible without identifying and fitting the data-generating model, which encodes biological effects in _𝑃_ ( _𝑥_ cg) and technical effects in _𝑃_ ( _𝑥_ cg|Dcg). Count correction is strictly less powerful than parameter estimation for the biological and technical models, because count correction requires those parameters, whereas knowledge of the parameters immediately implies the entire distribution of the biological and observed variables.

This critique does not appear to apply to, e.g., the probabilistic “imputation” in _scVI_ , as the autoencoder framework reports a distribution of _𝜇_ cg, rather than a point estimate _𝑥_ cg. This approach is somewhat more coherent, as it explicitly represents stochasticity.

### **B.4 Notes on graph methods**

This section reproduces a portion of the supplement of [112] by G.G., M.F., T.C., and L.P. This theoretical discussion was written by G.G.

220

Throughout Section 6.1, we have discussed _𝑘_ -nearest neighbor ( _𝑘_ -NN) graphs in the context of RNA velocity and embeddings. As _𝑘_ -NN is ubiquitous in scRNA-seq, and its applications are manifold, a full analysis is not feasible. In this supplement, we discuss a set of purely theoretical pitfalls which may limit the utility or interpretability of such graphs, leaving validation on simulated data to future work.

A _𝑘_ -NN graph purports to reflect relationships between cells based on similarity between their transcriptomic “states.” These states are typically mature RNA copy numbers that have undergone several steps of count processing, including size-normalization, log-transformation, filtering, and projection onto the top few principal components. The determination of neighbors in this space represents an uncomfortable compromise: if there are too few dimensions, the projection may be unrepresentative of the underlying data matrix; if there are too many, it may be skewed by the “curse of dimensionality.” Such distortions are evident in Figure 6.1d.

More subtly, it is unclear that observed transcriptomic similarity between barcodes should imply similarity between cells. _In silico_ UMI counts have been filtered through the random process of sequencing; the true underlying transcriptomic state is unknown, and cannot be precisely reconstructed (as outlined above, in Section B.3). We anticipate that certain narrow problems, such as cell type identification, may be insensitive to this source of error. For example, it is possible that simulated benchmarks can provide empirical results in the vein of “assuming transcriptional dynamics are bursty, cell types are distinguished by at least ten marker genes, these marker genes have an expression differential of at least one order of magnitude, and each cell type comprises 10–20% of the entire dataset, a community detectionbased algorithm has a 80% classification accuracy according to a particular metric, which falls to 75% if a particular noise model is imposed.” However, at this time, constructing undirected _𝑘_ -NN graphs based on imperfectly observed data appears to have limited theoretical or empirical justification.

The construction of directed _𝑘_ -NN graphs, as proposed in the original RNA velocity publication [168] and extended elsewhere [171], is considerably more problematic. A directed graph implies a causal relationship between observed cell states; in the implementations of RNA velocity, this causal relationship is Markovian, with a transition rate governed by the alignment between velocities and neighbor directions. We can analyze potential issues in this reasoning by gradually increasing the complexity of the system under analysis.

221

First, suppose that the RNA dynamics and the chemistry of sequencing are nonrandom, whereas the cell observations are independent draws of _𝑦𝑁_ ( _𝑡_ ) _, 𝑦 𝑀_ ( _𝑡_ ) from an underlying (deterministic and perfectly known) trajectory, using the notation in Section 6.1.1. Intuitively, building a directed graph raises questions: one cell is not the “descendant” of another, as both cells were captured and sequenced simultaneously. In this model formulation, the observed cells do not have causal relationships at all. We can build a graph that connects each cell to the neighbors of its position at Δ _𝑡_ ; at this point, the function used to define the graph is deliberately left generic. Even in this ideal-case scenario, this graph is highly dependent on the value of Δ _𝑡_ and strictly less informative than the dynamical system parameters, as its construction _requires_ those parameters.

Next, suppose that RNA dynamics are still deterministic, but sequencing injects noise into the observations. In the ideal case, where the dynamical system and sequencing noise parameters are perfectly known, extrapolating from the current state is impossible: the true RNA abundance is unknown. At best, we may instantiate a set of trajectories conditional on all possible unobserved biological states. As before, these trajectories depend on the time horizon Δ _𝑡_ . Aggregating the trajectories by assigning a weight to a single graph edge is strictly less informative than reporting the trajectories; that, in turn, is less informative than reporting the system parameters. The question of the amount of error incurred by this approach is coarsely equivalent to the question of a hidden Markov model’s approximability by a Markov model. Omitting uncertainty due to technical noise is equivalent to assuming a hidden Markov model can be effectively described without latent states. This assumption may be approximately valid (e.g., in the limit of perfect sequencing), or grossly incorrect, with no apparent _a priori_ way of constraining error.

Suppose now that RNA dynamics of _𝑛_ molecular species are stochastic on the state space Ω = N0<sup>_𝑛_,withnoobservationnoise.IfwesampleNccells,themicrostates</sup> corresponding to these data make up a subset Ω _𝐷_ , such that |Ω _𝐷_ | ≤ Nc. If the data are generated by a biological Markov process on Ω, a process truncated to Ω _𝐷_ will either not be Markov, or fail to recapitulate features of the biological process. This generally holds when |Ω _𝐷_ | _<_ |Ω|. The extent of incurred error may vary from minimal to egregious, and cannot be constrained without further knowledge of the system.

This argument has fairly severe consequences and foundations. Defining a directed graph on Ω _𝐷_ is superfluous: Ω _𝐷_ is itself constructed out of samples from the traversal

222

of a directed graph isomorphic to the biological continuous-time Markov chain. This CTMC is isomorphic to the CME. If states **x** _𝑖,_ **x** _𝑗_ ⊆ Ω _𝐷_ ⊆ Ω have the nonzero rate _𝑘𝑖𝑗_ for the **x** _𝑖_ → **x** _𝑗_ transition, it is possible to construct an approximating CTMC on Ω _𝐷_ merely by setting the rate of the corresponding transition to _𝑘𝑖𝑗_ . However, if either one of those states is not in Ω _𝐷_ , some dynamics are lost. The question of the amount of error incurred by truncation is roughly equivalent to the question of a given infinite CTMC’s approximability on a finite subdomain. For broad classes of CME models, finite approximations can do arbitrarily well: truncation to a finite subdomain Ω _𝐷_ incurs an error governed by the amount of probability flux to and from states outside this domain, and converges (in distribution) to the true CTMC as |Ω _𝐷_ | →∞. The finite state projection algorithm [203] exploits this approach to evaluate CME solutions (Section 4.2.2.2). However, the FSP is adaptive, and expands Ω _𝐷_ on a grid until a desired precision is achieved, rather than using a relatively small set of points which do not necessarily have transitions in the underlying CTMC.

The lack of these direct transitions between observed states in Ω _𝐷_ implies that a CTMC on Ω cannot be projected down to Ω _𝐷_ . This principle can be demonstrated using a striking trivial case. Consider a three-state Markov chain:


The full state space is Ω = {0 _,_ 1 _,_ 2}. Consider a case where states 0 and 2 are observed in multiple independent chains at some time _𝑡_ , i.e., Ω _𝐷_ = {0 _,_ 2}. We wish to define a neighborhood relationship between observations in state 0 and those in state 2, and summarize it as a CTMC on Ω _𝐷_ . The following results emerge immediately.

**Even with perfect knowledge of the original CTMC, a truncated CTMC will not fully recapitulate its dynamics.** The residence time in state 0 is exponentially distributed:


The true transition from 0 to 2 has a hitting time distribution described by a hypoexponential law:


223

The transition from 0 to 2 on Ω _𝐷_ — equivalent to the residence time in state 0 — is constrained to be exponentially distributed:


As the exponential distribution has one parameter, it can match the true residence time distribution, or a single moment of the hitting time distribution, but not both. If we match the residence time distribution, the approximation becomes arbitrarily good as _𝑘_ 12 →∞ and arbitrarily poor as _𝑘_ 12 → 0. The latter case makes not observing the long-lived state 1 somewhat improbable. However, as system dimensionality grows — e.g., if multiple independent CTMCs are started — the intermediate state will be unobserved in at least one of those chains almost surely.

**Even with perfect knowledge of the original CTMC, a generic stochastic process will not fully recapitulate its dynamics.** We can define a non-Markovian process on Ω _𝐷_ that will have a hitting time distribution given by Equation B.5. However, its residence time will fail to be distributed per Equation B.4. By constraining the process to traverse only observed states, the contributions from unobserved intermediate states are omitted, with error that cannot be easily bounded.

This inability to “compress” CTMCs into a smaller domain can also be treated in a more generic way. To define transitions between states, we must assign a single number — the rate — to the transition. Intuitively, we expect that the rates of CTMCs on Ω _𝐷_ should reflect the relative probabilities of transitions between states in the original CTMC on Ω. Thus, given three states **x** _𝑖_ , **x** _𝑗_ , and **x** _𝑙_ , we would like to impose the following criterion:


where _𝑃_ refers to full CTMC’s probability of being in a state **x** _𝑗_ or **x** _𝑙_ at time _𝑡_ , conditional on being in state **x** _𝑖_ at time 0, and _𝑘_ are rates in the “compressed” CTMC. This criterion appears to be the only “natural” one, and it induces a partially ordered set, which is insufficient to even order the transition rates in the CTMC on Ω _𝐷_ .

In conclusion, graph-based methods are problematic for representing relationships between cells. They can represent certain aspects of dynamics, but inevitably contradict the underlying graph that governs the biophysical CTMC. It is possible to make them agree, albeit only by considerably expanding the graph beyond observed

224

states, recapitulating the CME. In other words, the only cell–cell graph which can quantitatively summarize Markovian biological processes is the graph underlying the CME, with an infinite number of states, remaining forever out of reach and recalling Borges’s and Carroll’s dichotomy of the map and the territory [35, 45]: “...we now use the country itself, as its own map, and I assure you it does nearly as well.”

---

[← SUPPLEMENTARY GENERATING FUNCTION DERIVATIONS](20-supplementary-generating-function-derivations.md) · [Up: contents](index.md) · [INDEX →](22-index.md)
