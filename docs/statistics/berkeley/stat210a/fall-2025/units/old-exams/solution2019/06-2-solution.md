---
title: 2. Solution.
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Solution.

**Source:** [`units/old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) _X i_ and _Si_<sup>2arebothfunctionsof(</sup><sup>_Xi_1</sup><sup>_, . . . , Xi,n_),whicharemutually</sup> independent across _i_ = 1 _, . . . , m_ . Furthermore, _X i_ and _Si_<sup>2areinde-</sup> pendent of each other within each _i_ , as we have shown by e.g. Basu’s theorem. Hence ( _X_ 1 _, . . . , X m, S_ 1<sup>2</sup><sup>_, . . . , S_</sup> _m_<sup>2)are2</sup><sup>_m_independentrandom</sup> variables, with


As a result, _SB_<sup>2</sup><sup>_∼τ_2</sup> _m_<sup><u>+</u></sup> _−_<sup>_σ_2</sup> 1<sup>_<u>/n</u>_</sup> _χ_<sup>2</sup> _m−_ 1<sup>,anditisindependentof(</sup><sup>_S_</sup> 1<sup>2</sup><sup>_, . . . , S_</sup> _m_<sup>2)</sup> because it is a function of ( _X_ 1 _, . . . , X m_ ).

- (b) Because _X_ = _N_ ( _µ, τ_<sup>2</sup> _/m_ + _σ_<sup>2</sup> _/nm_ ), we have


As a result, _X ±_ ~~�~~ _SmB_<sup>2</sup><sup>_tm−_1(</sup><sup>_α/_2)isanexact1</sup><sup>_−α_confidenceinterval.</sup>

- (c) ( **Common mistake:** Note that we cannot use _SB_<sup>2alonetodothistest</sup> because its distribution depends on the nuisance parameter _τ_<sup>2</sup> .) Combining evidence across the within-group sample variances gives us the combined within-group variance


Because _SW_<sup>2isindependentof</sup><sup>_S_</sup> _B_<sup>2,wehave</sup>


As a result,


so we can reject the null when that statistic is above _Fm−_ 1 _,m_ ( _n−_ 1)( _α_ ).

7

- (d) Using the same logic, for _τ >_ 0 we can get an equal tailed test of _H_ 0 : _τ_<sup>2</sup> _/σ_<sup>2</sup> = _ρ_ vs. the two-sided alternative _H_ 1 : _τ_<sup>2</sup> _/σ_<sup>2</sup><sup>_̸_</sup> = _ρ_ by rejecting when _Tρ_ = _nρn_ +1<sup>_S_</sup> _B_<sup>2</sup><sup>_/S_</sup> _W_<sup>2iseitherabove</sup><sup>_a_=</sup><sup>_Fm−_1</sup><sup>_,m_(</sup><sup>_n−_1)(</sup><sup>_α/_2)</sup> or below _b_ = _Fm−_ 1 _,m_ ( _n−_ 1)(1 _− α/_ 2). Hence the acceptance region is


leading to confidence interval


- (e) Let _Xi_ = ( _Xi_ 1 _, . . . , Xin_ ) denote the _i_ th group of observations. The _Xi_ are independent multivariate Gaussians with mean _µ_ 1 = ( _µ, . . . , µ_ ) and covariance matrix Σ = _σ_<sup>2</sup> _In_ + _τ_<sup>2</sup> 11<sup>_′_</sup> (that is, the variance of _Xij_ is _σ_<sup>2</sup> + _τ_<sup>2</sup> and the within-group covariance is _τ_<sup>2</sup> ). The inverse covariance matrix has the same form: Σ<sup>_−_1</sup> = _θIn_ + _ζ_ 11<sup>_′_</sup> for some _θ_ ( _τ_<sup>2</sup> _, σ_<sup>2</sup> ) _>_ 0 _, ζ_ ( _τ_<sup>2</sup> _, σ_<sup>2</sup> ) _<_ 0.

As a result, the likelihood is


This is a full-rank three-parameter exponential family because the natu- ~~2~~ ral parameter space contains an open set, so _T_ = _i_<sup>_∥Xi∥_2</sup><sup>_,_�</sup> _i X i_<sup>_,_</sup> _X_ <u>�� �</u> is a complete sufficient statistic.

~~2~~ We have shown in class that ( _m −_ 1) _SB_<sup>2+</sup><sup>_m_</sup> _X_ ~~2~~ =<sup>�</sup> _i X i_<sup>,and(</sup><sup>_n −_</sup> ~~2~~ 1) _Si_<sup>2+</sup><sup>_n_</sup> _X i_<sup>=</sup><sup>_∥Xi∥_2.Therefore,wecanreconstruct</sup> � _X, SB_<sup>2</sup><sup>_,_�</sup> _i_<sup>_S_</sup> _i_<sup>2</sup> � from _T_ and vice-versa.

8

**3. “And if you ever saw it...” (24 points, 6 points / part).**

Some useful facts for this problem:

- For _n ∈{_ 0 _,_ 1 _, . . .}_ and _p ∈_ [0 _,_ 1]<sup>_d_</sup> with<sup>�</sup> _pi_ = 1, the multinomial density for _X ∼_ Multinom( _n, p_ ) is


An ecologist is interested in estimating the total population of reindeer in a wildlife preserve near the North Pole. She makes two visits to the preserve on two consecutive days and looks for reindeer. Each time she finds a reindeer she marks it with a unique identifying tag, so she can tell if she sees the same reindeer twice (in ecology this type of study is called a _capture-recapture_ or _mark-recapture_ study).

Assume that the same population of _n_ of reindeer is present in the preserve on both days, and each reindeer on each day has the same probability _π ∈_ (0 _,_ 1) of being seen by her, independently across the reindeer and the days (so the detections / non-detections are like 2 _n_ i.i.d. “coin flips” each with success probability _π_ ). Note that _n_ is the unknown parameter of interest and _π_ is an unknown nuisance parameter.

Let _N_ 11 denote the number of reindeer she sees both days, _N_ 10 the number she sees the first day not the second, and _N_ 01 the number she sees the second day but not the first. (Note that _N_ 00, the number of reindeer she sees on neither day, is not observed.)

- (a) Write down the likelihood for the model as a function of _N_ 01 _, N_ 10 _,_ and _N_ 11 and show that _T_ = ( _N_ 01 + _N_ 10 _, N_ 11) is a sufficient statistic for the model.

You do **NOT** need to show a sufficiency reduction from the Bernoulli model of detected/non-detected “coin flips” for each reindeer-day; after all we do not really get to observe the data for that model because we don’t know how many reindeer went undetected on both days. Just start with _N_ 01 _, N_ 10 _, N_ 11 as the data and _n_ and _π_ as the parameters.

- (b) (*) Show that _T_ is minimal sufficient (for this part you may assume we already know it is sufficient).

- (c) Define the estimator


9

Show that _n_ ˆ is consistent in the sense that _n/n_ ˆ _→p_ 1 as _n →∞_ with _π_ fixed.

- (d) Find the asymptotic distribution of _n_ ˆ from part (c) as _n →∞_ with _π_ fixed. You should center and scale appropriately so that it has a nondegenerate limiting distribution (that is, after centering and scaling it shouldn’t converge in probability to a constant).

10

---

[← 2. ANOVA with random effects (25 points, 5 points / part).](05-2-anova-with-random-effects-25-points-5-points-part.md) · [Up: contents](index.md) · [3. Solution. →](07-3-solution.md)
