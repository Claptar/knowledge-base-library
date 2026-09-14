---
title: INTRODUCTION AND OUTLINE
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# INTRODUCTION AND OUTLINE

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Truth is in a well.

Democritus

_via_ Diogenes Laërtius _via_ Robert Drew Hicks

The past decade has seen enormous investment in the development and application of single-cell RNA sequencing, driven by inexpensive sequencing and advances in microfluidics. This widespread adoption of the technology has been matched by a profusion of analysis methods. Yet, in my view, the experimental advances have far outstripped the theory and interpretation: typical analyses use data science approaches, which are somewhat _ad hoc_ and motivated by computational convenience. Although this approach is not an impediment _in principle_ , in practice it has led to a crisis of best practices: different analyses produce different results, with no straightforward way to decide on the “best” strategy. I argue that these tensions stem from a reliance on data science at the expense of physical modeling. Whatever the analyses do, they should be coherent with known biophysics; conversely, if they violate physical constraints, they can catastrophically fail. Although this principle of this strategy is deceptively simple, its adoption has been surprisingly limited, in spite of the arsenal of plausible and tractable models previously developed for fluorescence transcriptomics.

The thesis attempts to unify these fields, and develop sequencing analyses that encode physical models. This project requires fairly extensive mathematical machinery, as well as a sound intuition for the physics of gene expression and sequencing. In Chapter 2, I motivate the need for mechanistic models and delineate their scope. In Chapter 3, I introduce fundamental mathematical tools. In Chapter 4, I use these tools to define a set of tractable models that combine biological and technical phenomena. In Chapter 5, I discuss strategies and challenges surrounding the practical implementation of these models. In Chapter 6, I review a common workflow, analyze its weaknesses, and use its pitfalls as a case study to motivate a more principled alternative. In Chapters 7–9, I treat the questions of model identification, inference,

2

and interpretation using a combination of real and simulated data. In Chapters 10 and 11, I consider the models’ compatibility with gene co-expression and further experimental modalities. Finally, in Chapter 12, I summarize promising avenues for further research. Throughout the thesis, I occasionally refer to Appendix A, which contains certain useful derivations too tedious or detailed for the body of the text, and Appendix B, which discusses some of the caveats of modeling sequencing data. Very occasionally, I provide endnotes, which explicate certain qualitative insights that are only obliquely or implicitly referenced in the underlying articles.

Although broad, this thesis is not meant to be exhaustive. It is not and cannot be a review of single-cell RNA sequencing analysis methods. I have attempted to dedicate sufficient space to certain key touchpoints, but the field changes by the week, and a full survey cannot stay relevant. Worse: a review risks meeting methods on their own terms, accepting their premises, and equivocating. I have found it more fruitful to question narrow foundational assumptions; when these assumptions fail, analyses that rely on them become suspect. The thesis does not and cannot review the sprawling fields of biophysics or quantitative cell biology. It does not strive to serve as a first-principles treatment of stochastic transcriptional biophysics; I treat many deep results as a _fait accompli_ , and elide the usual theoretical niceties, leaving some pedagogical gaps.

It is not even a comprehensive account of my Ph.D. work. As I have generally attempted to be thorough, and fully treat the minutiae of derivations for my own and readers’ benefit, the body of the work summarized here covers, at last count, over six hundred pages across a dozen reports. Although the theoretical investigations have culminated in a common mathematical framework, which admits the individual projects as special cases, the technical details of implementation cannot be so summarized. Therefore, the thesis is not self-contained, except insofar as I unify the idiosyncrasies of my evolving notation and outline the occasionally non-obvious connections between the projects’ goals. These projects, in turn, represent only a sampling of scientific questions; many others, as deserving, are omitted or given merely passing mention. But the Ph.D. is finite, and I am satisfied that the questions this thesis raises will eventually be considered and answered, either by my colleagues or by other researchers at the emerging interface of physics and bioinformatics.

3

_C h a p t e r 2_

---

[← LIST OF TABLES](07-list-of-tables.md) · [Up: contents](index.md) · [TECHNOLOGIES, DESIDERATA, AND AXIOMS →](09-technologies-desiderata-and-axioms.md)
