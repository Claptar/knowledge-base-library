---
title: Integrating diverse data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Integrating diverse data

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

© American Association for the Advancement of Science. All rights reserved. This content is excluded from

our Creative Commons license. For more  information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." scien _ce_ 302, no. 5644 (2003): 449-53.

109

108


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

109

##### **likelihood ratio =**

_if > 1 classify as true if < 1 classify as false_


##### **log likelihood ratio =**


Prior probability is the same for all interactions --does not affect ranking

##### **Ranking function =**

_M_  _P_ <u>(</u> _Data_ <u>|</u> _true_ <u>_</u> _PPI_ <u>)</u> _P_ <u>(</u> _Observationi_ <u>|</u> _true_  PPI_ <u>)</u> = log   _PPI P Observation PPI_  _P_ ( _Data_ | _false_ _ ) <sup>∏</sup> _i_ ( _i_ | _false_ _ )

110

Protein pairs in the essentiality data can take on three discrete values (EE, both essential; NN, both non-essential; and NE, one essential and one not)


<!-- Start of picture text -->
P ( f | pos )<br>Likelihood=L=<br>P ( f | neg )<br>81,924/573,734<br>1,114/2150<br><!-- End of picture text -->

111


112


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

113


Fully connected → Compute probabilities for all 16 possible combinations


> © American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

> Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

114


##### Interpret with caution, as numbers are small


> © American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

115


<!-- Start of picture text -->
TF=FP<br><!-- End of picture text -->


<!-- Start of picture text -->
prediction<br>based on<br>single data<br>type all have<br>TP/FP<1<br>.<br>A Bayesian Networks Approach<br>."  Science  302,<br> P ( Data | true _ PPI ) <br>log  <br> P ( Data | false _ PPI ) <br><!-- End of picture text -->

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ronald, Haiyuan Yu, et al. "A Bayesian Networks Approach for Predicting Protein-protein Interactions from Genomic Data." _Science_ 302, no. 5644 (2003): 449-53.

How many gold-standard events do we score correctly at different likelihood cutoffs?

116

---

[← Requirement of Bayesian Classification](62-requirement-of-bayesian-classification.md) · [Up: contents](index.md) · [Summary →](64-summary.md)
