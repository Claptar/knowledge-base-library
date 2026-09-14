---
title: 7 Cross-validation for selecting λ
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEleven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Cross-validation for selecting λ

**Source:** [`LectureEleven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The behavior of _β_<sup>ˆ</sup> ridge( _λ_ ) and _β_<sup>ˆ</sup> lasso( _λ_ ) depend crucially on the choice of the tuning parameter _λ_ . One can visually tune _λ_ in order to obtain _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) _,_ ˆ _µ_<sup>lasso</sup> _t_ ( _λ_ ) that is simple (not too wiggly) and which fits the data well (for example, one can start with _λ_ = 1 and either increase or decrease _λ_ by factors of 10 until a visually appealing trend estimate is obtained). Another popular approach is to use cross-validation. The basic idea behind cross validation is the following. First split the total set of time points _T_ = _{_ 1 _, . . . , n}_ into two disjoint groups _T_ train and _T_ test. Generally _T_ train will be much larger than _T_ test (e.g., _T_ train will contain about 80% of the data and _T_ test will contain about 20% of the data). For this split, fit the model to the time indices in _T_ train and obtain _β_<sup>ˆ</sup> train<sup>ridge(</sup><sup>_λ_)</sup> as the minimizer of


and _β_<sup>ˆ</sup> train<sup>lasso(</sup><sup>_λ_)astheminimizerof</sup>


Using these estimates, predict the values of _yt_ for _t ∈ T_ test:

_y_ ˆ _t_<sup>ridge</sup> ( _λ_ ) = _β_<sup>ˆ</sup> train<sup>ridge</sup> _,_ 0<sup>(</sup><sup>_λ_)+ˆ</sup><sup>_β_</sup> train<sup>ridge</sup> _,_ 1<sup>(</sup><sup>_λ_)(</sup><sup>_t−_1)+ˆ</sup><sup>_β_</sup> train<sup>ridge</sup> _,_ 2<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_2)+</sup><sup>_· · ·_+ˆ</sup><sup>_β_</sup> train<sup>ridge</sup> _,n−_ 1<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_(</sup><sup>_n−_1))</sup>

and

_y_ ˆ _t_<sup>lasso</sup> ( _λ_ ) = _β_<sup>ˆ</sup> train<sup>lasso</sup> _,_ 0<sup>(</sup><sup>_λ_)+ˆ</sup><sup>_β_</sup> train<sup>lasso</sup> _,_ 1<sup>(</sup><sup>_λ_)(</sup><sup>_t−_1)+ˆ</sup><sup>_β_</sup> train<sup>lasso</sup> _,_ 2<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_2)+</sup><sup>_· · ·_+ˆ</sup><sup>_β_</sup> train<sup>lasso</sup> _,n−_ 1<sup>(</sup><sup>_λ_)ReLU(</sup><sup>_t−_(</sup><sup>_n−_1))</sup> The discrepancy between the actual values of _yt_ and the predicted values can be calculated as:


This test error is for a single train-test split. One can consider multiple train-test splits and add the test errors to obtain one measure of the test error for each value of _λ_ :


and


This test error over all splits would be calculated for a set of candidate _λ_ values (e.g., _λ_ = 10<sup>_a_</sup> for _a_ = _−_ 8 _, −_ 7 _, . . . ,_ 7 _,_ 8) and then choose the value of _λ_ which gives the smallest test error (this would give one choice of _λ_ for ridge, and one choice of _λ_ for lasso).

One common choice of selecting the splits is to take the test data in **Split** _i_ to be the _i_ -th 20% of the times _t_ and training data to consist of the data for all other times _t_ i.e., the test data in **Split** 1 corresponds to the first 20% of the data, test data in Split 2 corresponds to the second 20% of the data etc.

This method gives 5 different train-test splits, commonly known as 5-fold cross-validation.

5

---

[← 6 Ridge vs LASSO](06-6-ridge-vs-lasso.md) · [Up: contents](index.md)
