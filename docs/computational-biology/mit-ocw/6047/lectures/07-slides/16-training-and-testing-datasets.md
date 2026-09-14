---
title: Training and Testing Datasets
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Training and Testing Datasets

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The Rule

We _must_ test our classifier on a different set from the training set: the labeled test set

The Task

We will classify each object in the test set and count the number of each type of error

47

### Getting P(X|Class) from Training Set


<!-- Start of picture text -->
P(X|Class1) Class1) )<br><!-- End of picture text -->


<!-- Start of picture text -->
One Simple Approach P(X|Class1) Class1) )<br>How do we get this<br>Divide X values into bins  There are 13 data<br>from these?<br>points<br>And then we simply count<br>frequencies<br>X<br>In general, and especially for continuous distributions,<br>this can be a complicated problem: Density Estimation<br>7/13<br>3/13<br>2/13<br>1/13<br>0<br><1  1-3  3-5  5-7  >7<br><!-- End of picture text -->

48

## Distributions Over Many Features

**_Estimating P(X1,X2,X3,…,X8|Class1) can be difficult_**

- Assume each feature binned into 5 possible values

- We have 5<sup>8</sup> combinations of values we need to count the frequency for


- Generally will not have enough data

- – We will have lots of nasty zeros

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

49

---

[← Two Approaches to Classification](15-two-approaches-to-classification.md) · [Up: contents](index.md) · [Getting Priors →](17-getting-priors.md)
