---
title: Problem 3 answers continued (3)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2018.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/final2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 3 answers continued (3)

**Source:** [`old-exams/final2018.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

15

**4. Inference in the Laplace family (15 points, 5 points / part).** Some useful facts for this problem:

   - The Laplace location family with location parameter _θ_ is given by the density _pθ_ ( _x_ ) = _f_ ( _x − θ_ ), where _f_ ( _x_ ) = 2<sup><u>1</u></sup><sup>_e−|x|_.</sup>

   - The sign function is defined as


i.i.d. Assume we observe _X_ 1 _, . . . , Xn ∼_ Laplace( _θ_ ).

- (a) Find the score test of _H_ 0 : _θ_ = 0 vs. _H_ 1 : _θ >_ 0. Give the test statistic and threshold value in terms of a quantile of a binomial distribution (for simplicity you may assume _α_ is chosen so the binomial distribution has an exact _α_ quantile, so the test need not be randomized. Also note P _θ_ ( _X_ = 0) = 0 for all _θ_ , so you don’t need to worry about what happens there).

- (b) Suppose we are not so sure about the Laplace assumption, but we do believe the data come from a symmetric location family, meaning _pθ_ ( _x_ ) = _f_ ( _x − θ_ ) for some unknown _f_ : R _→_ [0 _, ∞_ ) that integrates to 1 and is symmetric about the origin (we can think of the nonparametric family as being parameterized by ( _θ, f_ )). Show that the test from part (a) is still a valid, finite-sample test of _H_ 0 : _θ_ = 0 vs. _H_ 1 : _θ >_ 0 in this larger family.

- (c) Now consider testing _H_ 0 : _θ ≤_ 0 vs. _H_ 1 : _θ >_ 0 (note the null hypothesis now includes negative values of _θ_ ). Show that the test from part (a) is a valid and unbiased level- _α_ test for the nonparametric family from part (b).

16

---

[← Problem 3 answers continued (2)](10-problem-3-answers-continued-2.md) · [Up: contents](index.md) · [Problem 4 answers continued (1) →](12-problem-4-answers-continued-1.md)
