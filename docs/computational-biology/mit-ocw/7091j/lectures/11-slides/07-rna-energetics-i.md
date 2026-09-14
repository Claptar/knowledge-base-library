---
title: RNA Energetics I
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# RNA Energetics I

**Source:** `lectures/11-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Free energy contributions from:


<!-- Start of picture text -->
G  A  G<br>>  ><br>• base pairing:<br>C  U  U<br><!-- End of picture text -->

• base stacking:

**G** p **A | | C** p **U**

are combined in Doug Turner’s Energy Rules: Matrix for each X,Y stacking on each possibly base pair or free end


<!-- Start of picture text -->
5' --> 3'<br>UX<br>AY<br>3' <-- 5’<br>X<br>Y A  C  G  U<br> A  .  .  .  -1.30<br>C  .  .  -2.40  .<br>G  .  -2.10  .  -1.00<br>U  -0.90  .  -1.30  .<br><!-- End of picture text -->

34

### RNA Energetics II

Other Contributions to Folding Free Energy

- Hairpin loop destabilizing energies

   - a function of loop length

- Interior and bulge loop destabilizing energies - a function of loop length

- Terminal mismatch and base pair energies

35

RNA Energetics III Folding by Energy Minimization

A more complex dynamic programming algorithm is used - similar in spirit to the Nussinov base pair maximization algorithm Gives:

- minimum energy fold

- suboptimal folds (e.g., five lowest ΔG folds)

- probabilities of particular base pairs

• full partition function

Accuracy: ~70% of base pairs correct

36

---

[← RNA Energetics I](06-rna-energetics-i.md) · [Up: contents](index.md) · [Links & References →](08-links-references.md)
