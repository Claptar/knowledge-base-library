---
title: Identical and independent binding sites
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l2-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Identical and independent binding sites

**Source:** `recordings/l2-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For now let’s assume we have n identical binding sites and that binding at a given site is independent of the state of binding of all other sites. The rate constants k+ and k- characterize the binding and unbinding rates respectively. In steady state, [II.2] can now be written as:


The factor n takes into account that there are n possible binding sites available for binding the first substrate. On the other hand there is only one possibility to loose a substrate going from state P1 to Po. Similarly for j=2 we can deduce:


because there are (n-1) possibilities to add a substrate and only 2 possibilities to remove a substrate. If the intrinsic association constant K is defined as:


we find that K1 = nK and K2 = (n-1)K/2. In general, one can write:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

8


for j = 1, 2, … , n. By substituting [II.11] in [II.7] an explicit equation for r as a function of K, n, and [S] is found. We will not go through the details of the derivation. If you are interested, see for example Bisswanger (2002, p. 11-16). The final result is elegantly simple:


Note that the mathematical form of this equation is very similar to Michaelis-Menten kinetics. However this result is a steady-state (equilibrium) property while MichaelisMenten equation is not. Equation [II.12] can also be derived in a more hand waving manner. As the n binding sites are identical and independent, it is not important to view them as clustered in one protein. If [F] is the concentration of free binding site and [B] the concentration of bound sites in steady state, then the association constant for this equilibrium is given by:


The total number of sites is: n[P]=[F]+[B], this combined with [II.13] gives:

---

[← II Equilibrium binding and cooperativity](02-ii-equilibrium-binding-and-cooperativity.md) · [Up: contents](index.md) · [Non-identical and independent binding sites →](04-non-identical-and-independent-binding-sites.md)
