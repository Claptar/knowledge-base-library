---
title: 6 Cross-validation for selecting λ
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Cross-validation for selecting λ

**Source:** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The behavior of _β_<sup>ˆridge</sup> ( _λ_ ) and _β_<sup>ˆlasso</sup> ( _λ_ ) depend crucially on the choice of the tuning parameter _λ_ . One can visually tune _λ_ in order to obtain _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) _,_ ˆ _µ_<sup>lasso</sup> _t_ ( _λ_ ) that is simple (not too wiggly) and which fits the data well (for example, one can start with _λ_ = 1 and either increase or decrease _λ_ by factors of 10 until a visually appealing trend estimate is obtained). Another popular approach is to use cross-validation.

The basic idea behind cross validation is the following. First split the total set of time points _T_ = _{_ 1 _, . . . , n}_ into two disjoint groups _T_ train and _T_ test. Generally _T_ train will be much larger than _T_ test (e.g., _T_ train will contain about 80% of the data and _T_ test will contain about 20% of the data). For this split, fit the model to the time indices in _T_ train and obtain _β_<sup>ˆ</sup> train<sup>ridge(</sup><sup>_λ_)</sup> as the minimizer of


4

and _β_<sup>ˆ</sup> train<sup>ridge(</sup><sup>_λ_)astheminimizerof</sup>


Using these estimates, predict the values of _yt_ for _t ∈ T_ test:

_y_ ˆ _t_<sup>ridge</sup> ( _λ_ ) = _β_<sup>ˆ</sup> train<sup>ridge</sup> _,_ 0<sup>(</sup><sup>_λ_)+ˆ</sup><sup>_β_</sup> train<sup>ridge</sup> _,_ 1<sup>(</sup><sup>_λ_)(</sup><sup>_t−_1)+ˆ</sup><sup>_β_</sup> train<sup>ridge</sup> _,_ 2<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_2)+</sup><sup>_· · ·_+ˆ</sup><sup>_β_</sup> train<sup>ridge</sup> _,n−_ 1<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_(</sup><sup>_n−_1))</sup>

and

_y_ ˆ _t_<sup>lasso</sup> ( _λ_ ) = _β_<sup>ˆ</sup> train<sup>lasso</sup> _,_ 0<sup>(</sup><sup>_λ_)+ˆ</sup><sup>_β_</sup> train<sup>lasso</sup> _,_ 1<sup>(</sup><sup>_λ_)(</sup><sup>_t−_1)+ˆ</sup><sup>_β_</sup> train<sup>lasso</sup> _,_ 2<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_2)+</sup><sup>_· · ·_+ˆ</sup><sup>_β_</sup> train<sup>lasso</sup> _,n−_ 1<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_(</sup><sup>_n−_1))</sup> The discrepancy between the actual values of _yt_ and the predicted values can be calculated as:


This test error is for a single train-test split. One can consider multiple train-test splits and add the test errors to obtain one measure of the test error for each value of _λ_ :


and


This test error over all splits would be calculated for a set of candidate _λ_ values (e.g., _λ_ = 10<sup>_a_</sup> for _a_ = _−_ 5 _, −_ 4 _, . . . ,_ 4 _,_ 5) and then choose the value of _λ_ which gives the smallest test error (this would give one choice of _λ_ for ridge, and one choice of _λ_ for lasso).

One common choice of selecting the splits is the following:

1. **Split 1** : _T_ test is _{_ 1 _,_ 6 _,_ 11 _, . . . }_ and _T_ train is all other _t_ .

2. **Split 2** : _T_ test is _{_ 2 _,_ 7 _,_ 12 _, . . . }_ and _T_ train is all other _t_ .

3. **Split 3** : _T_ test is _{_ 3 _,_ 8 _,_ 13 _, . . . }_ and _T_ train is all other _t_ .

4. **Split 4** : _T_ test is _{_ 4 _,_ 9 _,_ 14 _, . . . }_ and _T_ train is all other _t_ .

5. **Split 5** : _T_ test is _{_ 5 _,_ 10 _,_ 15 _, . . . }_ and _T_ train is all other _t_ .

This method gives 5 different train-test splits, commonly known as 5-fold cross-validation.

5

---

[← 5 Ridge vs LASSO](05-5-ridge-vs-lasso.md) · [Up: contents](index.md)
