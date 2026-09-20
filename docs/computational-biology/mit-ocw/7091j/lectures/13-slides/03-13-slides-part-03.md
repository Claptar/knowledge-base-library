---
title: 13 slides Part 03 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/13-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 13 slides Part 03 —

How could we make quantitative predictions of binding energy for mutants?

**Figure 1**
The structures of (A) HB36 (B) HB80 in complex with HA (blue) which were provided to participants. Residues probed in the deep sequencing enrichment experiment are in orange; the remainder are in grey. Residues at the interface are represented as sticks.

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community-wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." *Proteins: Structure, Function, and Bioinformatics* 81, no. 11 (2013): 1980-7.

---

Color based on predictions
- improved
- neutral
- reduced

**Note:**
**Better at predicting deleterious mutations**

This is one of the top performers analyzing residues at the interface!

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community-wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." *Proteins: Structure, Function, and Bioinformatics* 81, no. 11 (2013): 1980-7.

---

### Top performer

**All sites**

**Interface**

### Average group

**All sites**

**Interface**

- improved
- neutral
- reduced

Color based on participant's predictions

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community-wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." *Proteins: Structure, Function, and Bioinformatics* 81, no. 11 (2013): 1980-7.

---

## What's a good "baseline" for modeling?

- Does structure/energy help?

---

## What's a good "baseline" for modeling?

- Does structure/energy help?
- Naïve model:
  - Give each mutant a score equal to the BLOSUM matrix value (-4 to 11)
  - As we vary the cutoff, how many mutations do we predict correctly?

---

## Area under curve for predictions (varying cutoff in ranking)

### BLOSUM HB36

- Predicted to be deleterious
- Predicted to be beneficial

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Comparing one of the best to BLOSUM

### BLOSUM HB36

### G21 HB36

- Predicted to be deleterious
- Predicted to be beneficial

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Area under curve for predictions (varying cutoff in ranking)

### HB36, all mutations

- First Round
- Second Round. (Given data for nine random mutations at each position)

BLOSUM

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Summary

- Best groups are only three times better than expected from a random assignment.
- Predicting the effect of mutations on polar starting positions appears to be a particular challenge.

---

## Summary

- Best approaches require explicit consideration of the effects of mutations on stability

$$\text{A} + \text{B} \rightleftarrows \text{AB}$$

$$\text{A} + \text{B}^* \rightleftarrows \text{AB}^*$$

---

## Summary

- Best approaches require explicit consideration of the effects of mutations on stability

$$\text{unfolded} \rightleftarrows \text{A} + \text{B} \rightleftarrows \text{AB}$$

$$\text{unfolded} \rightleftarrows \text{A} + \text{B}^* \rightleftarrows \text{AB}^*$$

For more details see
http://ocw.mit.edu/courses/biological-engineering/20-320-analysis-of-biomolecular-and-cellular-systems-fall-2012/modeling-and-manipulating-biomolecular-interactions/MIT20_320F12_Tpc_3_Mol_Des.pdf

---

## Summary

- Best approaches require explicit consideration of the effects of mutations on stability
- The best performing groups also modeled packing, electrostatics and solvation.
- The best methods used :
  - machine learning (G21, Fernandez-Recio, and G05s, Bates)
  - atom-level energy functions (G15, Weng)
  - coarse-grained models (G21s, Dehouck)

---

## G21

- Database of 930 ($\Delta\Delta\text{G}$,mutation) pairs
- Predict structure with FoldX (empirical force field)
- Describe each mutant with 85 features using measures from FoldX, PyRosetta, FireDoc, PyDoc, SIPPER, CHARMM, NIP/NSC and others.

---

## G21

- Train learners: random forest, neural networks, probabilistic classifiers, etc.
- Evaluate with cross-validation
- Use combined results from five classifiers:
  - Random forest
  - Decision table
  - Bayesian net
  - Logistic regression
  - Alternating decision tree

---

## Prediction Challenges

- Predict effect of point mutations
- **Predict structure of complexes**
- **Predict all interacting proteins**

---

## Predicting Structures of Complexes

- Can we use structural data to predict complexes?
- This might be easier than **quantitative** predictions for site mutants.
- But it requires us to solve a docking problem

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Docking

Which surface(s) of protein A interactions with which surface of protein B?

Courtesy of Nurcan Tuncbag. Used with permission.

N. Tuncbag

## Time is an issue

* Imagine we wanted to predict which proteins interact with our favorite molecule.
  * For each potential partner
    * Evaluate all possible relative positions and orientations
      * allow for structural rearrangements
        * measure energy of interaction
* This approach would be extremely slow!
* It's also prone to false positives.
  * Why?

---

## Reducing the search space

* Use prior knowledge of interfaces to focus analysis on particular residues
* Find ways to choose potential partners
  * What role should structural homology play?

---

## Subtilisin and its inhibitors

Although global folds of Subtilisin's partners are very different, binding regions are structurally very conserved.

Chymotrypsin Inhibitor 2

Subtilisin Inhibitor

Eglin C

N. Tuncbag

Courtesy of Nurcan Tuncbag. Used with permission.

---

## Hotspots

**Fig. 1.** Contribution of only a subset of contact residues to net binding energy. **(A)** Loss of solvent-accessible area (7) of the side chain portion of each residue in the hGHbp on forming a complex with hGH. **(B)** Difference in binding free energy between alanine-substituted and wild-type hGHbp $(\Delta\Delta G)_{\text{mut-wt}}$ at contact residues (5). Negative values indicate that affinity increased when the side chain was substituted by alanine.

Figure from Clackson & Wells (1995).

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Clackson, Tim, and James A. Wells. "A Hot Spot of Binding Energy in a Hormone-Receptor Interface." *Science* 267, no. 5196 (1995): 383-6.

---

## Hotspots

A Receptor

hGH

W104

K172

$\Delta\Delta\text{G (kcal/mol)}$
* $> 1.5$
* $0.5\text{ to }1.5$
* $-0.5\text{ to }0.5$
* $< -0.5$
* Untested

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Clackson, Tim, and James A. Wells. "A Hot Spot of Binding Energy in a Hormone-Receptor Interface." *Science* 267, no. 5196 (1995): 383-6.

Figure from Clackson & Wells (1995).

---

* Fewer than 10% of the residues at an interface contribute more than 2 kcal/mol to binding.
* Hot spots
  * rich in Trp, Arg and Tyr
  * occur on pockets on the two proteins that have complementary shapes and distributions of charged and hydrophobic residues.
  * can include buried charge residues far from solvent
  * O-ring structure excludes solvent from interface

http://onlinelibrary.wiley.com/doi/10.1002/prot.21396/full

---

## Next Lecture

**Fast and accurate modeling of protein-protein interactions by combining template-interface-based docking with flexible refinement.**

Tuncbag N, Keskin O, Nussinov R, Gursoy A.

http://www.ncbi.nlm.nih.gov/pubmed/22275112

**Structure-based prediction of protein–protein interactions on a genome-wide scale**

Zhang, et al.

http://www.nature.com/nature/journal/v490/n7421/full/nature11503.html

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← DE Shaw](02-de-shaw.md) · [Up: contents](index.md)
