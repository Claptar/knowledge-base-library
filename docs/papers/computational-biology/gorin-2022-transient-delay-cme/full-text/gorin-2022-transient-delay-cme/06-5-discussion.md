---
title: 5 DISCUSSION
source: https://doi.org/10.1101/2022.10.17.512599/
source_file: sources/papers/gorin-2022-transient-delay-cme/gorin-2022-transient-delay-cme.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-2022-transient-delay-cme.pdf` from [papers/gorin-2022-transient-delay-cme](https://doi.org/10.1101/2022.10.17.512599/) — papers · gorin-2022-transient-delay-cme, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 DISCUSSION

This report extends the solutions reported in (Gorin and Pachter, 2022a) to a broad class of delayed systems, and unifies them with the theory of switching genes outlined in (Vastola, 2021). The approach augments the toolbox of stochastic biophysical analysis: it affords generating function-based analytical solutions for systems which would otherwise be outside the purview of the standard analysis of Markov chains. The derivation of these solutions does not require the usual manipulations of master equations at several time points, merely fairly standard integrals. These solutions may be fit (e.g., through the *Monod* implementation) and used as alternative hypotheses to investigate whether the standard assumptions of memorylessness hold, whether they are violated, or whether the available data are equivocal.

In Section 3.2, we used these analytical solutions to fit several superficially similar bivariate overdispersed models to single-cell and single-nucleus data, and observed that the typical Markovian model is a strong candidate, but cannot be easily distinguished from the competing delayed-efflux model, especially in the low-spliced expression single-nucleus data. On the other hand, two alternative models are consistently judged less plausible. This suggests that the assumption of Markovian, one-step splicing is useful despite its simplicity. This investigation is far from comprehensive. We forgo modeling technical noise or identifying cell types using cell type definitions based on the spliced RNA counts introduces some degree of circularity. However, even with these limitations, the results illustrate fundamental challenges associated with single-nucleus data. To sum up, the data analysis is consistent with the following answers to the questions posed in Section 1:

- Single-nucleus data do not appear to require qualitatively different models. Both single-cell and single-nucleus data are consistent with the delayed efflux model.
- The Markovian splicing hypothesis is considerably more consistent with data than the delayed-splicing hypothesis.
- As may be expected, the low amounts of spliced RNA in nuclear data mean that only models with substantial differences in the unspliced distributions can be distinguished.

Furthermore, even when generating functions cannot be obtained, which is the typical case for systems with multiple RNA species, our method provides a simple numerical recipe for evaluating their distributions. The numerical approach is guaranteed to run in $O(N\ln N)$, can use off-the-shelf integration routines (e.g., quadrature for bursty systems and Runge–Kutta methods for switching systems), and enables the evaluation of arbitrary marginal distributions, which is not feasible for matrix- or simulation-based methods.

The approach is largely modular with respect to the specific details of the downstream processes, i.e., the causal relationships between the molecules and the Markovian or deterministic waiting times for the reactions. In Section 4, we discuss a set of extensions to even more generic systems, with waiting times described by combinations of exponential and degenerate distributions. The same generating function-based approach can be used to implement models of technical noise and molecular non-identifiability under the assumption of independent sampling (Gorin and Pachter, 2021). Although the solutions are fairly generic, they do not yet provide a route to treating more complex systems with protein translation or molecular feedback. We speculate that a sufficiently general treatment of such systems may uncover similar relationships between CMEs and DCMEs, and provide a simulation routine that can be extended to model such phenomena.

---

[← 4 METHODOLOGICAL EXTENSIONS](05-4-methodological-extensions.md) · [Up: contents](index.md) · [REFERENCES →](07-references.md)
