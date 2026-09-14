---
title: 'Stat 156 HW #5'
source: https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW5.pdf
source_file: sources/berkeley-stat156/fall-2024/HW5.pdf
licence: CC BY-NC 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat 156 HW #5

**Source:** [`HW5.pdf`](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW5.pdf) · **Licence:** CC BY-NC 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Due 11/12/2024 by 11:59 pm PT

Note that points will be deducted if you fail to

- Submit code for coding problems

- Assign pages to the corresponding problem in Gradescope

1. Recall from lecture that we can identify the effect of removing treatment on the whole population as


under _Relevance, Exclusion Restriction, Exchangeability_ and _one-sided noncompliance_ (meaning _Z_ = 0 would imply _D_ = 0). Also recall that under the same assumptions we can identify the effect of removing treatment on the treated as


Prove these two results.

2. Prove that under the standard IV assumptions of relevance (Z is associated with D), exclusion restriction ( _Y_ ( _Z_ = _z, D_ = _d_ ) = _Y_ ( _D_ = _d_ )), and exchangeable IV ( _Z ⊥⊥_ ( _D_ ( _Z_ = _z_ ) _, Y_ ( _Z_ = _z_ )), the structural equation model


implies the following two-stage model of observed data


along with the three classical IV assumptions:

1

   - (a) Relevance: _cov_ ( _D, Z_ ) _̸_ = 0

   - (b) Exclusion restriction: Z is not included in second-stage Y equation

   - (c) Exchangeable IV: _cov_ ( _Z, ν_ ) = _cov_ ( _Z, ϵ_ ) = 0.

3. In lecture we presented two identified forms of the coefficient _B_ 1 in the classical IV two-stage model. Prove this equality.


4. Assume a classical two-stage IV model with _cov_ ( _D, Z_ ) _̸_ = 0 and _cov_ ( _Z, ν_ ) = _cov_ ( _Z, ϵ_ ) = 0. Under this model, _B_ 1 equals the coefficient in a population regression of _Y_ on the predicted value from a population regression of _D_ on _Z_ . Prove this.

5. Problem 20.2 from _A First Course in Causal Inference_

6. Problem 21.7 from _A First Course in Causal Inference_

7. Problem 17.4 from _A First Course in Causal Inference_

8. Problem 17.6 from _A First Course in Causal Inference_

9. Problem 18.1 from _A First Course in Causal Inference_

10. Problem 18.2 from _A First Course in Causal Inference_

2

---

[Up: contents](index.md)
