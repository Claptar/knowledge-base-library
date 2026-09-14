---
title: Non-identical and interacting binding sites
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l2-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Non-identical and interacting binding sites

**Source:** `recordings/l2-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

How would the analysis above change if the two binding sites are non-identical? The ligand binding to the two binding sites is now characterized by the rate constants k±1, k±2, k±3, and k±4 (Fig. 4) and the four intrinsic association constants Kj=k+j/k-j (j=1,2,3,4). In this case there are four states of the protein-ligand complex: nothing bound, site 1 bound, site 2 bound, and two sites bound. The principal of detailed balance (thermodynamic equilibrium) does not allow any net fluxes between states. Therefore:


Rewritting (31) gives:


The saturation function is given by:


Note that [II.27] is independent of K4 as expected because of the detailed balance equation [II.26].

If we define


The saturation function can be written in the same form as for the identical interacting binding sites:


In the limit K1=K2 we find x=x and ’ β=β’ (identical interacting sites). In the limit K1=K3 and K2=K4 we recover the independent binding case:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

13


’

In the case we can write β as:


Note that β’= 1 for identical sites and β’< 1 for non-identical sites. This implies that binding curves exhibiting negative cooperativity could arise from a protein that has independent binding sites or from a protein that has two interacting sites in which the second binding event is less likely that the first.

---

[← Identical and interacting binding sites](05-identical-and-interacting-binding-sites.md) · [Up: contents](index.md) · [Further reading on enzyme kinetics and cooperativity →](07-further-reading-on-enzyme-kinetics-and-cooperativity.md)
