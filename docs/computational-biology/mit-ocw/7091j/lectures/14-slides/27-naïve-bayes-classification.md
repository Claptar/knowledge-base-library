---
title: Naïve Bayes Classification
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Naïve Bayes Classification

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **posterior**

**likelihood**

**prior**


**likelihood ratio** = ratio of posterior probabilities _if > 1 classify as true if < 1 classify as false_

How do we compute this ?

59

##### **likelihood ratio =**

_if > 1 classify as true if < 1 classify as false_


##### **log likelihood ratio =**


Prior probability is the same for all interactions --does not affect ranking

60

##### **likelihood ratio =**

_if > 1 classify as true if < 1 classify as false_


##### **log likelihood ratio =**


Prior probability is the same for all interactions --does not affect ranking  _P_ <u>(</u> _Data_ <u>|</u> _true_ <u>_</u> _PPI_ <u>)</u>  **Ranking function =** log   _PPI_  _P_ ( _Data_ | _false_ _ ) 

61

##### **Ranking function =**

 _P_ <u>(</u> _Data_ <u>|</u> _true_ <u>_</u> _PPI_ <u>)</u>  log   _PPI_  _P_ ( _Data_ | _false_ _ ) 

We assume the observations are independent (we’ll see how to handle dependence soon)

62

##### **Ranking function =**

_M_  _P_ <u>(</u> _Data_ <u>|</u> _true_ <u>_</u> _PPI_ <u>)</u> _P_ <u>(</u> _Observationi_ <u>|</u> _true_  PPI_ <u>)</u> = log   _PPI P Observation PPI_  _P_ ( _Data_ | _false_ _ ) <sup>∏</sup> _i_ ( _i_ | _false_ _ )

We assume the observations are independent (we’ll see how to handle dependence soon)

63

##### **Ranking function =**

_M_  _P_ <u>(</u> _Data_ <u>|</u> _true_ <u>_</u> _PPI_ <u>)</u> _P_ <u>(</u> _Observationi_ <u>|</u> _true_  PPI_ <u>)</u> = log   _PPI P Observation PPI_  _P_ ( _Data_ | _false_ _ ) <sup>∏</sup> _i_ ( _i_ | _false_ _ )

We assume the observations are independent (we’ll see how to handle dependence soon)

We can compute these terms if we have a set of highconfidence positive and negative interactions .

Exactly how we compute the terms depends on the type of data.

For affinity purification/mass spec. see Collins et al. Mol. Cell. Proteomics 2007 http://www.mcponline.org/content/6/3/439.long

64


Instead of requiring an interaction to be detected in all assays, we can rank by


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Von Mering, Christian, Roland Krause, et al. "Comparative Assessment of  Large-scale Data Sets of Protein–protein Interactions." _Nature_ 417, no. 6887 (2002): 399-403.

**Comparative assessment of large-scale data sets of protein–protein interactions** von Mering, _et al. Nature_ **417** , 399-403 (23 May 2002) | doi:10.1038/nature750

65

---

[← Bayes Rule](26-bayes-rule.md) · [Up: contents](index.md) · [ROC curve →](28-roc-curve.md)
