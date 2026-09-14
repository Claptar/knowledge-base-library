---
title: Using epigenomic annotations for fine-mapping disease regions
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using epigenomic annotations for fine-mapping disease regions

**Source:** `lectures/20-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

30


LD: both a blessing & a curse


Observation: LD blocks in which there is no evidence for historical recombination

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

31

###### **Causal variant not known in most GWAS regions**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Smemo, S., Tena, J. J., Kim, K., Gamazon, E. R., Sakabe, N. J.,Gómez-Marín, C., . . . Nóbrega, M. A. (2014). "Obesity-associated variants within FTO form long-range functional connections with IRX3." Nature, 507(7492), 371-375. doi:10.1038/nature13138

**_LD (Linkage disequilibrium): large regions co-inherited in blocks Blessing for initial mapping (few tags), curse for fine-mapping_**

**Use functional annotations to predict causal variant(s)**

32

### Multiple lines of evidence for fine-mapping


Courtesy of Macmillan Publishers Limited. Used with permission. Ward, L. D., & Kellis, M. (2012). Interpreting noncoding genetic variation in complex traits and human disease. Nat Biotechnol Nature Biotechnology, 30(11), 1095-1106. doi:10.1038/nbt.2422. Used with permission.

Ward and Kellis, Nature Biotechnology 2012

- Epigenomic information: enhancers & linking (target genes)

- Motif information: causal variants & upstream regulators

- Evolutionary conservation: causal variants & conserved motifs

33

##### Detect SNPs that disrupt conserved regulatory motifs


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Lindblad-Toh, Kerstin, Manuel Garber, Or Zuk, Michael F. Lin, Brian J. Parker, Stefan Washietl, Pouya Kheradpour, et al. “A High-Resolution Map of Human Evolutionary Constraint Using 29 Mammals.” _Nature_ 478, no. 7370 (2011): 476–82.doi:10.1038/nature10530.

• Functionally-associated SNPs enriched in states, constraint

34

###### **Allele-specific chromatin marks: cis-vs-trans effects**


   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Maternal and paternal GM12878 genomes sequenced**

- **Map reads to phased genome, handle SNPs indels**

- **Correlate activity changes with sequence differences**<sup>35</sup>

##### **Predict effect of common, rare, somatic mutations**


###### **_All: Regulatory and epigenomic annotations_**


**_Rare/somatic: Predict TF binding disruption_**

**Richard Sallari Xinchen Wang**

**_Common: allelic activity in heterozygous lines_**

36

###### **HaploReg: public resource for dissecting GWAS**


Courtesy of the authors. License: CC BY-NC.

Source: Ward, Lucas D. and Manolis Kellis. "HaploReg: a resource for exploring chromatin states, conservation, and regulatory motif alterations within sets of genetically linked variants." Nucleic Acids Research 40, no. D1 (2012): D930-D934.

###### • **Start with any list of SNPs or select a GWA study**

   - Mine ENCODE and Roadmap epigenomics data for hits

   - Hundreds of assays, dozens of cells, conservation, motifs

   - Report significant overlaps and link to info/browser

- **Try it out: http://compbio.mit.edu/HaploReg**

Ward, Kellis NAR 2011

37

37

---

[← Using epigenomic maps to predict disease-relevant tissues](02-using-epigenomic-maps-to-predict-disease-relevant-tissues.md) · [Up: contents](index.md) · [Predicting target genes →](04-predicting-target-genes.md)
