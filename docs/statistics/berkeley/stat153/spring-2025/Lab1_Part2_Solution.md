---
title: STAT 153 & 248 - Time Series Lab One Spring 2025, UC Berkeley
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part2_Solution.pdf
source_file: sources/berkeley-stat153/spring-2025/Lab1_Part2_Solution.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STAT 153 & 248 - Time Series Lab One Spring 2025, UC Berkeley

**Source:** [`Lab1_Part2_Solution.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part2_Solution.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

January 24, 2025

## **Part 2: Bayesian analysis in a simple estimation problem**

**Problem 1.** _Suppose we have six observations_


_which we model as_


_where θ and σ_<sup>2</sup> _are unknown parameters. Conduct Bayesian inference on the unknown parameters θ and σ_<sup>2</sup> _. Note that the answer depends on your choice of priors for θ and σ_<sup>2</sup> _._

**Suggestion.** _Try using the following priors_


_with a large constant C, as in the last lecture._

**Solution.** _The first step is to choose priors for θ and σ_<sup>2</sup> _. Similar to the analysis of linear regression in class, we shall assume that_


_for a large constant C. These priors are supposed to capture our large prior uncertainty on the values of θ and σ. In density form, the prior density becomes:_


_The likelihood is_


1

_The posterior density of θ, σ given the observed data Y_ 1 _, . . . , Yn is therefore_


_This gives the joint posterior of θ and σ. If we want only the posterior of θ (i.e., the conditional density of θ given the data Y_ 1 _, . . . , Yn), we need to integrate the above with respect to σ. This gives the following:_


_When C is large, the integral will be basically be the same as_ 0 _to ∞, leading to:_

_The change of variable_

_gives_


_We thus get_


_When C is large, the indicator above will play no role, so we just drop it to obtain:_


_It turns out that this posterior density is related to the t-density with n−_ 1 _degrees of freedom. To see this, recall (from wikipedia for example) first that t-density with n−_ 1 _degrees of freedom is proportional to_


2

_To see the connection between_ (2) _and_ (3) _, first write (below y_ ¯ = ( _y_ 1 + _· · ·_ + _yn_ ) _/n)_

_where_


_The expression_ (4) _looks very much like the t-density_ (3) _. To see this more explicitly, let us compute the posterior density of_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θ − y_ ¯) _/s:_


_This proves that_


_where tn−_ 1 _is the t-distribution with n −_ 1 _degrees of freedom._

_With this formula, we can do any uncertainty quantification for θ based on the observed data y_ 1 = 26 _._ 6 _, y_ 2 = 38 _._ 5 _, y_ 3 = 34 _._ 4 _, y_ 4 = 34 _, y_ 5 = 31 _, y_ 6 = 23 _._ 6 _. For example, we can calculate the posterior probability that θ belongs to the interval_ [28 _,_ 32] _as_


_We can also give an interval whose posterior probability is exactly 0.95. Indeed, using the fact that_


_we obtain_


_or_


3

_If only a point estimate of θ is desired, then one can simply use the posterior mean which equals y_ ¯ = 31 _._ 35 _(this is also the posterior median and the posterior mode as the t-distribution is symmetric about 0)._

_Next, let us focus on inference for the parameter σ. To obtain the posterior density for σ, we need to integrate_ (1) _with respect to θ. This gives_


_Writing_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_yi −θ_)2= �</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_yi −y_¯)2 +</sup><sup>_n_(¯</sup><sup>_y −θ_)2</sup><sup>_,weobtain_</sup>


_Again assuming that C is large, we can calculate the integral above from −∞ to ∞. Using the formula for the normalizing constant of a normal distribution, we get_


_We thus get_


_Although this expression can be left as is, we can relate this to the χ_<sup>2</sup> _-density with a little extra simplification assuming that C is large. Indeed, if C is large, we can replace the indicator by I{σ >_ 0 _} to get_


_where s is as in_ (5) _. By a simple change of variable formula, we can now deduce that_

_which means that_


_From here, any inference can be obtained on σ. If a point estimate of σ is desired, one simple way is to just take the point estimate of_<sup><u>(</u></sup><sup>_n−_</sup> _σ_<sup>12)</sup><sup>_s_2</sup> _to be equal to the mean of χ_<sup>2</sup> _n−_ 1<sup>_whichis_</sup> _n −_ 1 _. This gives_


_One can also posterior probability of any event involving σ. One can also construct an interval for σ with posterior probability exactly_ 0 _._ 95 _._

4

---

[Up: contents](index.md)
