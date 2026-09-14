---
title: Reference
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l5-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Reference

**Source:** `recordings/l5-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. T. S. Gardner, C. R. Cantor, and J. J. Collins. Construction of a genetic toggle switch in _Escherichia coli_ . _Nature_ **403** , 339-342 (2000).

In this paper Gardner _et al._ engineered a plasmid containing two repressor genes mutually controlling each others expression. In Box 1 postulate the two equations describing the toggle switch:


Let’s derive this equation and explore which assumptions were made during the derivation. The fast equilibium reactions for this problem are:


The first two reactions model the binding of the repressors to the two promoters inhibiting transcription. We will assume that there is only one binding site for the repressor (in contrast to the lambda phage promoters). However the repressor monomers can form multimers. Repressor 1 multimerizes with γ subunits and repressor 2 with β subunits. Note that K3 and K4 are the effective association constants for multimerization. The units of K3 and K4 are (M)<sup>1-γ</sup> and (M)<sup>1-β</sup> respectively. The last two equations assume that intermediate states are not allowed. This is the Hill approximation as we discussed before (see for example [II.22]). Remember that the total number of promoter site is conserved, and the total concentration of both promoters is identical since they are on the same plasmid:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

21

Now the rate of synthesis of repressor 1 and 2 can be written as:


The rates k1 and k2 are the effective synthesis rates (including RNA polymerase binding, transcription, translation, and folding) of repressor protein 1 and 2, respectively).

Assuming a first order decay process with rate δ, the kinetic equations are:


When we introduce a dimensionless time t = tδ , equation (50) becomes:


if we use the following dimensionless concentrations:


Equation [IV.6] becomes:


Finally by defining α1 and α2 as:


we recover the ‘Box’ equation:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

22


In steady state both these equations equal zero:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

23

---

[← IV Synthetic genetic switches](01-iv-synthetic-genetic-switches.md) · [Up: contents](index.md) · [V Stability analysis →](03-v-stability-analysis.md)
