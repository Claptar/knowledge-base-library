---
title: Integrating diverse data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Integrating diverse data

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

14


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

15

###### **likelihood ratio =**

_if > 1 classify as true if < 1 classify as false_


###### **log likelihood ratio =**


Prior probability is the same for all interactions --does not affect ranking

###### **Ranking function =**

 _P Data true PPI M P Observation true PPI_ <u>( | _ ) (</u> _<u>i</u>_ <u>| _ )</u> = log   _PPI P Observation PPI_  _P_ ( _Data_ | _false_ _ ) <sup>∏</sup> _i_ ( _i_ | _false_ _ )

16

Protein pairs in the essentiality data can take on three discrete values (EE, both essential; NN, both non-essential; and NE, one essential and one not)


<!-- Start of picture text -->
P ( f | pos )<br>Likelihood=L=<br>P ( f | neg )<br>81,924/573,734<br>1,114/2150<br><!-- End of picture text -->

17


18

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

19

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.


<!-- Start of picture text -->
P1-P2<br>REAL<br>Gavin  Ho  Uetz  Ito<br><!-- End of picture text -->


What do we mean by fully connected?


<!-- Start of picture text -->
P1-P2<br>REAL<br>Gavin Ito<br>Ho  Uetz<br><!-- End of picture text -->


20


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

Fully connected → Compute probabilities for all 16 possible combinations


<!-- Start of picture text -->
P1-P2<br>REAL<br>Gavin Ito<br>Ho  Uetz<br><!-- End of picture text -->


21

Fully connected → Compute probabilities for all 16 possible combinations

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.


22


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

###### Interpret with caution, as numbers are small


23


<!-- Start of picture text -->
How many gold-standard events do we   P Data true PPI <br>( | _ )<br>log  <br>score correctly at different likelihood   P ( Data | false _ PPI ) <br>cutoffs?<br><!-- End of picture text -->


<!-- Start of picture text -->
prediction<br>based on<br>single data<br>type all have<br>TP/FP<1<br>© American Association for the Advancement of Science. All rights reserved.<br>This content is excluded from our Creative Commons license. For more<br>information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach<br>for Predicting Protein-protein Interactions from Genomic Data."<br>TF=FP<br>Science  302, no. 5644 (2003): 449-53.<br><!-- End of picture text -->

24

---

[← Requirement of Bayesian Classification](10-requirement-of-bayesian-classification.md) · [Up: contents](index.md) · [Outline →](12-outline.md)
