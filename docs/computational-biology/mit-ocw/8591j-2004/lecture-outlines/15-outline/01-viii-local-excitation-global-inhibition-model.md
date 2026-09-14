---
title: VIII Local excitation, global inhibition model
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/15-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# VIII Local excitation, global inhibition model

**Source:** `lecture-outlines/15-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this lecture we will discuss one of the most frequently used theories to model biological reactions limited by diffusion. Turing was the first to formulate this problem mathematically. Gierer and Meinhardt took Turing’s formalisms and applied it to biological problems. The model described below is therefore often called ‘the TuringGierer-Meinhardt theory’. One of the first models was defined as follows:


a and i are the concentrations of an activator and an inhibitor. The activator is produced at a constant rate ra (for example, a leaky promoter) plus a rate that depends on both a and i. The activator operates as a dimer whereas the inhibitor operates as a monomer. The synthesis rate of a is proportional to the saturation function Y to reflects the probability to have an activator dimer present and an inhibitor monomer absent:


The approximation above is valid for small concentrations of a and large concentrations of i. Ka and Ki are the association constants for the activator and inhibitor binding.

Both the activator and inhibitor molecules obey first order decay characterized by γa and γI, respectively. The last term in equations [VIII.1] reflects the one-dimensional diffusion. The diffusion coefficient of the activator and inhibitor are Da and Di. The inhibitor is synthesized at a rate proportional to a<sup>2</sup> . Apparently the activator enhances the inhibitor synthesis according to the Hill equation with nH=2. Note that again it is assumed that the concentration of a is small (with respect to Ka). The system of equations [VIII.1] is an example of a reaction-diffusion system. Let us analyze [VIII.1] in more detail.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

43

---

[Up: contents](index.md) · [Dimensionless variables →](02-dimensionless-variables.md)
