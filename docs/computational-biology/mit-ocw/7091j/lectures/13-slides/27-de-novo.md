---
title: de novo
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# de novo

**Source:** `lectures/13-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- When there is no suitable homology model: – Monte Carlo search for backbone an **g** les

      - Choose a short region (3‐9 amino acids) of backbone

      - **Set torsion angles to those of a similar peptide in PDB**

      - Accept with metropolis criteria

   - **36** , **000 MC steps**

   - Repeat entire process to get 2,000 final structures

   - Cluster structures

   - Refine clusters

45

## How has modeling changed during the CASP challenges?


46

### **Improvement over the last decade: Percentage of residues successfully modeled**

**% of residues modeled that were not in best template**

**CASP10 results compared to those of previous CASP experiments** **<u>Andriy Kryshtafovych, Krzysztof Fidelis, John Moult</u>** DOI: 10.1002/prot.24448


Each point represents the best model for a target


CASP10 and CASP9 are similar, much better than CASP5.


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof  Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." _Proteins: Structure, Function, and Bioinformatics_ 82, no. S2 (2014): 164-74.

**Target difficulty ‐** based on structural and sequence similarity of a target to proteins of known structure

47

## Overall Prediction Accuracy

## Did Not Improve

**CASP10 results compared to those of previous CASP experiments DOI: 10.1002/prot.24448**


##### **Global distance test GDT TS**


=overall accuracy of a **model** average % of Cα atoms in the prediction close to **corresponding atoms in** the target structure


**‐ Perfect model: 90 100 Random model: 20‐30**


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof  Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." _Proteins: Structure, Function, and Bioinformatics_ 82, no. S2 (2014): 164-74.

**Target difficulty** is based on structural and sequence similarity of a target to proteins of known structure

48

## Overall Prediction Accuracy Did Not Improve

**CASP10 results compared to those of previous CASP experiments DOI: 10.1002/prot.24448**


**Why is the trend line the same?**


**Are targets getting harder in other ways? Multi‐domain,**


#### **‐ multi chain etc. ,**


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Kryshtafovych, Andriy, Krzysztof  Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." _Proteins: Structure, Function, and Bioinformatics_ 82, no. S2 (2014): 164-74.

**Target difficulty** is based on structural and sequence similarity of a target to proteins of known structure

49

Free modeling results **_de novo_** (no template)

50

---

[← Homology](26-homology.md) · [Up: contents](index.md) · [Free Modelin g in Flux →](28-free-modelin-g-in-flux.md)
