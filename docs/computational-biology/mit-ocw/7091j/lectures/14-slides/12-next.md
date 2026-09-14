---
title: Next
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Next

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PRISM Fast and accurate modeling of protein-protein interactions by combining template-interface-based docking with flexible refinement.**

Tuncbag N, Keskin O, Nussinov R, Gursoy A. http://www.ncbi.nlm.nih.gov/ pubmed/22275112

**PrePPI**

**Structure-based prediction of protein–protein interactions on a genomewide scale**

Zhang, et al. <u>http://www.nature.com/natur e/journal/v490/n7421/full/ nature11503.html</u>

24


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

## **PrePPI**

Scores potential templates without building a homology model Criteria

Geometric similarity between the protomer and template Statistics based on preservation of contact residues

**Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

25


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB) i i 3. Look for structure of a complex containing structural neighbors 2. Find structural neighbors  (NA ,NB )(avg:1,500 neighbors/structure) 4. Align sequences of MA,MB to NA,NB based on structure

###### **Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

26


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB) 2. Find structural neighbors  (NAi,NBi)(avg:1,500 neighbors/structure) 3. Look for structure of a complex containing structural neighbors 4. Align sequences of MA,MB to NA,NB based on structure

**Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

27


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB) 2. Find structural neighbors  (NAi,NBi)(avg:1,500 neighbors/structure) 3. Look for structure of a complex containing structural neighbors

4. Align sequences of MA,MB to NA,NB based on structure

**Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

28


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB) 2. Find structural neighbors  (NAi,NBi)(avg:1,500 neighbors/structure) 3. Look for structure of a complex containing structural neighbors 4. Align sequences of MA,MB to NA,NB based on structure

**Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

29


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB)

2. Find structural neighbors  (NAi,NBi)(avg:1,500 neighbors/structure)

3. Look for structure of a complex containing structural neighbors

4. Align <u>sequences</u> of MA,MB to NA,NB based on structure

**Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

30


<!-- Start of picture text -->
NA  NB<br>NA  NB<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

1. Identify interacting residues in template complex (Called NA1 NB3 in rest of paper)

31


<!-- Start of picture text -->
NA  NB<br>NA  NB<br><!-- End of picture text -->

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

1. Identify interacting residues in template complex (Called NA1 NB3 in rest of paper)

2. Predict interacting residues for the homology models

32


<!-- Start of picture text -->
NA  NB<br>NA  NB<br><!-- End of picture text -->

#### **<u>Evaluate based on five measures</u>**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

33


<!-- Start of picture text -->
Evaluate based on<br>five measures:<br>• SI M: str NA  uctural  NB<br>similarity of NA,MA<br>and NB,MB<br>NA  NB<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

34

##### **Evaluate based on five measures:**

- **SIM: structural similarity of NA,MA and NB,MB**

• **SIZ (number) COV (fraction) of interaction pairs can be aligned anywhere**

- **OS subset of SIZ at interface**

- **OL number of aligned pairs at interface**

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

35

“The final two scores reflect whether the residues that appear in the model interface have properties consistent with those that mediate known PPIs (for example, residue type, evolutionary conservation, or statistical propensity to be in protein–protein interfaces).”   ????

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

36


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB) 2. Find structural neighbors  (NAi,NBi)(avg:1,500 neighbors/structure)

3. Look for structure of a complex containing structural neighbors

4. Align sequences of MA,MB to NA,NB based on structure

5. Compute five scores

6. Train Bayesian classifier using “gold standard” interactions **Structure-based prediction of protein–protein interactions on a genome-wide scale** Nature 490, 556–560 (25 October 2012) doi:10.1038/nature11503

37


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Zhang, Qiangfeng Cliff, Donald Petrey, et al. "Structure-based Prediction of Protein-protein Interactions on a Genome-wide Scale." _Nature_ 490, no. 7421 (2012): 556-60.

1. Find homologous proteins of known structure (MA,MB) 2. Find structural neighbors  (NAi,NBi)(avg:1,500 neighbors/structure)

3. Look for structure of a complex containing structural neighbors

4. Align sequences of MA,MB to NA,NB based on structure

5. Compute five scores

6. Train <mark>Bayesian classifier u</mark> sing “gold standard” interactions We will examine Bayesian classifiers soon

38

---

[← Hotspots](11-hotspots.md) · [Up: contents](index.md) · [Outline →](13-outline.md)
