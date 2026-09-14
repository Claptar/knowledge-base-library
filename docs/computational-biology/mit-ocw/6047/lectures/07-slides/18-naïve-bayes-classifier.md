---
title: Naïve Bayes Classifier
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Naïve Bayes Classifier

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**We are going to make the following assumption:** **_All features are independent given the class_**

 _P X X X Class P X Class P X Class P X Class_ ( 1, 2,..., _n_ | ) ( 1 | ) ( 2 | )... ( _n_ | ) _n P_ ( _X i_ | _Class_ )   _i_  1

**We can thus estimate individual distributions for each feature and just multiply them together!**

53

## Naïve Bayes Discriminant Function

**Thus, with the Naïve Bayes assumption, we can  now rewrite, this:**

_P_ <u>(</u> _X_ <u>1,</u> _X_ <u>2,...,</u> _X_ <u>7 |</u> _Class_ 1) _P_ <u>(</u> _Class_ 1)  _G_ ( _X_ 1,..., _X_ 7 ) log  0 _P_ ( _X_ 1, _X_ 2,..., _X_ 7 | _Class_ 2) _P_ ( _Class_ 2)

**As this:** <u></u> _P_ ( _X i_ | _Class_ 1) _P_ <u>(</u> _Class_ 1)  _G_ ( _X_ 1,..., _X_ 7 ) log  0  _P_ ( _X i_ | _Class_ 2) _P_ ( _Class_ 2)

**Which can be simply computed as the sum of log scores**

54

---

[← Getting Priors](17-getting-priors.md) · [Up: contents](index.md) · [Binary Classification Errors →](19-binary-classification-errors.md)
