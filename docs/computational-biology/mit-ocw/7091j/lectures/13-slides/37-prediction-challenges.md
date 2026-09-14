---
title: Prediction Challenges
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Prediction Challenges

**Source:** `lectures/13-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• Predict effect of point mutations • **Predict structure of complexes** • Predict all interacting proteins

61


•DOI: 10.1002/prot.24356

“ **Simple** ” **challenge:** Starting with known **structure of a complex:** predict how much a **i h bi di** mutat on c anges n ng affinity.


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community ‐ wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." _Proteins: Structure, Function, and Bioinformatics_ 81, no. 11 (2013): 1980-7.

62


•DOI: 10.1002/prot.24356

- •All possible single‐point mutations at **each of 53 and 45 positions for two** proteins.

- **•Expressed on yeast**

- •High‐throughput assay based on **sequencing used to estimate changes** in binding affinity


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community ‐ wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." _Proteins: Structure, Function, and Bioinformatics_ 81, no. 11 (2013): 1980-7.

63


•DOI: 10.1002/prot.24356

### **How could we make**

### quantitative predictions of **binding energy for** mutants?


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community ‐ wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." _Proteins: Structure, Function, and Bioinformatics_ 81, no. 11 (2013): 1980-7.

64

Color based on predictions improved neutral reduced **Note: B tt t di ti e er a pre c ng deleterious mutations**

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community ‐ wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." _Proteins: Structure, Function, and Bioinformatics_ 81, no. 11 (2013): 1980-7.

This is one of the top performers analyzing residues at the interface!

•DOI: 10.1002/prot.24356

65


<!-- Start of picture text -->
Top performer<br>es<br>Allsit<br><!-- End of picture text -->


<!-- Start of picture text -->
Average group<br>improved<br>neutra l<br>reduced<br><!-- End of picture text -->


Color based on participant’s predictions


<!-- Start of picture text -->
ce<br>nterfa<br>I<br><!-- End of picture text -->


© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Moretti, Rocco, Sarel J. Fleishman, et al. "Community ‐ wide Evaluation of Methods for Predicting the Effect of Mutations on Protein–protein Interactions." _Proteins: Structure, Function, and Bioinformatics_ 81, no. 11 (2013): 1980-7.

66

•DOI: 10.1002/prot.24356

## What’s a good “baseline” for modeling?

• Does structure/energy help?

67

## What’s a good “baseline” for modeling?

- Does structure/energy help?

- • **Naïve model:**

   - Give each mutant a score equal to the ‐

   - **BLOSUM matrix value ( 4 to 11)**

   - – As we vary the cutoff, how many mutations do we pre **di** ct correct y **l ?**

68

#### Area under curve for predictions (varying cutoff in ranking)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

•DOI: 10.1002/prot.24356

**Predicted to be deleterious Predicted to be beneficial**

69

## **Comparing one of the best to BLOSUM**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu<sup>/help/faq-fair-use/.</sup>

•DOI: 10.1002/prot.24356

**Predicted to be deleterious Predicted to be beneficial**

70

#### Area under curve for predictions (varying cutoff in ranking)


<!-- Start of picture text -->
First Round<br>.<br>Second Round (Given data<br>for nine random mutations at<br>each position)<br>BLOSUM<br><!-- End of picture text -->


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

•DOI: 10.1002/prot.24356

71

---

[← Predictions](36-predictions.md) · [Up: contents](index.md) · [Summary →](38-summary.md)
