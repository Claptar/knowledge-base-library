---
title: The Exponential with Censoring
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Exponential with Censoring

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can write the likelihood for one observation as:

_L_ ( _λ_ ) = [ _f_ (1 _− G_ )( _T_<sup>˜</sup> )]<sup>∆</sup> [ _SdG_ ( _T_<sup>˜</sup> ]<sup>1</sup><sup>_−_∆</sup> = [ _λ_ exp( _−λT_<sup>˜</sup> )(1 _− G_ ( _T_<sup>˜</sup> ))]<sup>∆</sup> [exp( _−λT_<sup>˜</sup> ) _dG_ ( _T_<sup>˜</sup> )]<sup>1</sup><sup>_−_∆</sup> _l_ ( _λ_ ) = log _L_ ( _λ_ ) = ∆[log( _λ_ ) _− λT_<sup>˜</sup> ] _−_ (1 _−_ ∆) _λT_<sup>˜</sup> + _C_ , where _C_ does not depend on _λ_ . _U_ ( _λ_ ) = _dλd_<sup>_l_(</sup><sup>_λ_) = ∆</sup><sup>_/λ −T_˜.</sup>

Since scores have mean zero, this implies _λ_ = _E_ ∆ _/ET_<sup>˜</sup>

Setting the score for _n_ observations to zero, we see the mle is _λn_ = ∆ _n/T_ ˜ _n_ , where ∆ _n_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>∆</sup><sup>_i_,</sup> _T_ ˜ _n_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_T_˜</sup><sup>_i_,anditisthemlebecause</sup><sup>_U_isstrictlydecreasingin</sup> _λ_ , so the log-likelihood is strictly concave.

So for _f_ ( _x, y_ ) = _x/y_ , with continuous gradient [1 _/y, −x/y_<sup>2</sup> ], a first-order Taylor expansion about ( _E_ ∆ _, ET_<sup>˜</sup> ), and the fact that _∥_ (∆ _n, T_ ˜ _n_ ) _−_ ( _E_ ∆ _, E_ ˜ _T_ ) _∥→_ 0 in probability by LLN,<sup>_<u>√</u>_</sup> _<u>n</u>_ <u>(</u> _λn − λ_ ) =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _f_ (∆ _n, T_ ˜ _n_ ) _−_ _<u>f</u>_ ( _E_ ∆ _, E_ ˜ _T_ )) =<sup>_√_</sup> _<u>n</u>_ <u>($$∆</u> _n − E_ ∆$$(1 _/ET_<sup>˜</sup> + _op_ (1)) + $$ _T_ ˜ _n − E_ ˜ _T_ $$( _−E_ ∆ _/_ ( _E_ ˜ _T_ )<sup>2</sup> + _op_ (1))). As<sup>_√_</sup> _<u>n</u>_ <u>(∆</u> _n − E_ ∆),<sup>_√_</sup> _<u>n</u>_ <u>(</u> _T_ ˜ _n − E_ ˜ _T_ ) = _Op_ (1) by the CLT, this linearlization gives the influence curve _IC_ ( _O|P_ ) = (∆ _− E_ ∆) _/ET_<sup>˜</sup> _−_ ( _E_ ∆)( _T_<sup>˜</sup> _− ET_<sup>˜</sup> ) _/_ ( _ET_<sup>˜</sup> )<sup>2</sup> .

---

[← Identifiability and Estimation in Survival Analysis](23-identifiability-and-estimation-in-survival-analysis.md) · [Up: contents](index.md) · [ML Consistency →](25-ml-consistency.md)
