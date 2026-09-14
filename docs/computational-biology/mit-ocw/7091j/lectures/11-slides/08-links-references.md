---
title: Links & References
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Links & References

**Source:** `lectures/11-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The Mfold web server:

http://mfold.rna.albany.edu/?q=mfold/rna-folding-form The Vienna RNAfold package (free for download) http://www.tbi.univie.ac.at/~ivo/RNA/

**RNA folding references:**

M. Zuker, et al.  In _RNA Biochemistry and Biotechnology_ (1999)

D.H. Mathews et al. _J. Mol. Biol._ **288** , 911-940 (1999) Vienna package by Ivo Hofacker

37

RNA Secondary Structure Prediction by Energy Minimization Summary

- Assumes folding energy decomposable into independent contributions of small units of structure

- Algorithms are guaranteed to find minimal free energy structure defined by the model

- In practice, algorithms predict ~70% of bp correct

- Errors result from

   - imprecision of the model/parameters

   - differences between _in vitro_ and _in vivo_ conditions

   - _in vivo_ structure may not always have minimum free energy

38

###### Sample Mfold Output (Human U5 snRNA)


<!-- Start of picture text -->
5’  3’<br><!-- End of picture text -->


<!-- Start of picture text -->
dG = -34.6 kcal/mol<br><!-- End of picture text -->

###### Minimum free energy structure

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

© Washington University. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### Energy dot plot

39

Energy dot plot for a lysine riboswitch

© Washington University. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

40

###### Function of the lysine riboswitch


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Lysine interacts with the junctional core of the riboswitch and is specifically recognized through shape-complementarity within the elongated binding pocket and through several direct and K+-mediated hydrogen bonds to its charged ends.

Controls expression of enzymes involved in biosynthesis and transport of lysine

Serganov et al. Nature 2008. Caron et al PNAS 2012

41

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← RNA Energetics I](07-rna-energetics-i.md) · [Up: contents](index.md)
