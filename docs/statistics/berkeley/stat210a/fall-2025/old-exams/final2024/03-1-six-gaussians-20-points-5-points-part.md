---
title: 1. Six Gaussians (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Six Gaussians (20 points, 5 points / part).

**Source:** [`old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

_•_ Recall that the Gaussian density function for _Z ∼ N_ ( _θ, σ_<sup>2</sup> ) is


Assume that we observe Gaussian random variables _X_ 1 _, . . . , X_ 6 where _Xi ∼ N_ ( _θi, σ_<sup>2</sup> ), independently. Different parts of the question will assume _σ_<sup>2</sup> _>_ 0 is known or unknown.

(a) Assume it is known that _σ_<sup>2</sup> = 1. Suppose we want to test the null hypothesis:


against the alternative that _θ_ is any other vector in R<sup>6</sup> . Suggest a _χ_<sup>2</sup> test statistic and specify the degrees of freedom.

(b) Continue to assume _σ_<sup>2</sup> = 1 and consider the following estimator for _θ_ :

_δ_ ( _X_ ) = _γ ·_ � _X_ 1 _, X_ 23 _, X_ 23 _, X_ 456 _, X_ 456 _, X_ 456� _,_ where _γ ∈_ [0 _,_ 1] is a fixed constant, _X_ 23 =<sup>_<u>X</u>_</sup><sup><u>2+</u></sup> 2<sup>_<u>X</u>_</sup><sup><u>3</u></sup> , and _X_ 456 =<sup>_<u>X</u>_</sup><sup><u>4+</u></sup><sup>_<u>X</u>_</sup> 3<sup><u>5+</u></sup><sup>_<u>X</u>_</sup><sup><u>6</u></sup> . Give an unbiased estimator for the MSE of _δ_ ( _X_ ).

- (c) Now, assume that _σ_<sup>2</sup> is unknown, but it _is_ known that _θ_ 2 = _θ_ 3 and _θ_ 4 = _θ_ 5 = _θ_ 6. That is, what in part (a) was a null hypothesis to be tested is now a modeling assumption. Suggest a confidence interval based on the Student’s _t_ -distribution for the parameter _g_ ( _θ_ ) = _θ_ 4 _− θ_ 3. Specify the degrees of freedom.

- (d) Under the same assumptions as part (b), now suppose that we want to test the null hypothesis _H_ 0 : _θ_ 1 = _θ_ 2 = _· · ·_ = _θ_ 6 against the alternative that _θ_ is any other vector in R<sup>6</sup> with _θ_ 2 = _θ_ 3 and _θ_ 4 = _θ_ 5 = _θ_ 6. Suggest an _F_ test statistic and specify the degrees of freedom.

2

---

[← Final Examination: QUESTION BOOKLET](02-final-examination-question-booklet.md) · [Up: contents](index.md) · [Problem 1 answers continued (1) →](04-problem-1-answers-continued-1.md)
