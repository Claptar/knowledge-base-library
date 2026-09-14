---
title: Functional Derivatives
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Functional Derivatives

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If _φ_ : _R →R_ , it is easy to define what is meant by _φ_ being differentiable at a point. If _φ_ : ( _l_<sup>_∞_</sup> _, ∥· ∥F_ ) _→R_ , or more generally, _φ_ : ( _D, ∥· ∥_ ) _→_ ( _E, ∥· ∥_ ), obviously the usual definition of differentiability does not apply.

A heuristic is that if _φ_ : ( _D, ∥· ∥_ ) _→_ ( _E, ∥· ∥_ ) is differentiable at _P ∈ D_ , then the derivative of _φ_ at _P_ (denoted _dφP_ ) is a continuous linear map _dφP_ : ( _D, ∥·∥_ ) _→_ ( _E, ∥·∥_ ) that is a linear approximation to _φ_ at _P_ .

Unfortunately, there is ambiguity about how to define a derivative map between general spaces. The three most important types of derivatives are listed below.

_Definitions_ : If there is a continuous linear map _dφP_ : ( _D, ∥· ∥_ ) _→_ ( _E, ∥· ∥_ ) such that _Rem_ ( _h_ ) = _∥φ_ ( _P_ + _h_ ) _− φ_ ( _P_ ) _− dφP_ ( _h_ ) _∥_ for _h ∈ D_ , then _φ_ is ( _Gateaux_ , _Hadamard_ , _Frechet_ ) differentiable at _P_ if _Rem_ ( _ϵh_ ) _/ϵ →_ 0 uniformly over _h_ for _h_ in any (singleton of _D_ , compact subset of _D_ , bounded subset of _D_ ) respectively.

Note that Frechet differentiability is stronger than Hadamard differentiability, which is stronger than Gateaux differentiability. If the Frechet derivative exists, it is equal to the Hadamard derivative, and if the Hadamard derivative exists, it is equal to the Gateaux derivative.

Note that for _φ_ : _R_<sup>_k_</sup> _→R_ , the Gateaux derivative corresponds to the directional derivative, and the Frechet and Hadamard conicide and are equal to the total derivative. When _k_ = 1, all three derivatives are the same, and coincide with the ordinary definition of a derivative. This is because the Gateaux derivative at _x_ in the direction _h_ is given by _dϵd_<sup>_φ_(</sup><sup>_x_+</sup><sup>_ϵh_)</sup><sup>_|ϵ_=0=</sup><sup>_φ′_(</sup><sup>_x_)</sup><sup>_h_.Thus,</sup><sup>_dφx_isthelinearmapmap</sup><sup>_h→φ′_(</sup><sup>_x_)</sup><sup>_h_.</sup> But when _k >_ 1, it is possible for the directional derivative to be defined in every direction, but for the total derivative to not exist.

Note that the derivative depends on what norm is chosen for both spaces _D_ and _E_ . Generally a strong norm in _D_ and a weak norm in _E_ makes it easier for the derivative to exist.

6

The Hadamard derivative is thought to be the most useful in empirical process theory, as Frechet differentiability is too hard to establish in many cases, but Gateaux differentiability is not strong enough to imply desired results. Because the Hadamard derivative is so useful, it is convenient to rephrase Hadamard differentiability in another form.

**Theorem 0.3.** _A map φ_ : ( _D, ∥· ∥_ ) _→_ ( _E, ∥· ∥_ ) _is Hadamard differentiable at P ∈ D with derivative dφP_ : ( _D, ∥· ∥_ ) _→_ ( _E, ∥· ∥_ ) _if dφP is a continuous linear map such that_ _<u>φ</u>_ <u>(</u> _P_ <u>+</u> _tnhtnn_ <u>)</u> _−φ_ <u>(</u> _P_ <u>)</u> _→ dφP_ ( _h_ ) _for all scalar sequences tn →_ 0 _and hn ∈ D → h ∈ D._

Often we are interested in functionals defined on a space of probability distributions, so that _φ_ ( _P_ ) is an unknown parameter and _φ_ ( _Pn_ ) is an estimator. But notice that the definition of the derivative requires specifying a normed space. So what normed space should we choose to include all probability distributions? Should we think of _P_ and _Pn_ as members of ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ )? If so, for what _F_ ? One common choice is to think of _P_ and _Pn_ as distribution functions (which are monotone right-continuous functions with left limits) and define the domain _D_ of _φ_ to be the space of _cadlag_ functions. Cadlag is a french acronym for _continuous from the right with limits from the left_ , and as the name implies, it is the space of all real-valued right-continuous functions with left limits. The most common norm used for the space of cadlag functions is the supremum norm.

Once differentiability has been established (any of the three kinds), actually finding the derivative is easy, because _dφP_ ( _h_ ) = _dϵd_<sup>_φ_(</sup><sup>_P_+</sup><sup>_ϵh_)</sup><sup>_|ϵ_=0.Therightsideisjustthe</sup> derivative of a real-valued function of _ϵ_ , evaluated at zero, so it can often be found using high school calculus. _Example_ : Consider _φ_ defined on the space of cadlag functions with supremum norm, by _φ_ ( _F_ ) = �0 _t_ 1 _−F_ <u>1(</u> _s−_ )<sup>_dF_(</sup><sup>_s_).This is an important functional in survival analysis, repre-</sup> sents the _cumulative hazard_ when _O ∼ P_ , and _F_ is the cumulative distribution function of _P_ . Evaluating _dϵd_<sup>_φ_(</sup><sup>_P_+</sup><sup>_ϵh_)</sup><sup>_|ϵ_=0weseethattheGateauxderivativeat</sup><sup>_F_inthedi-</sup> rection _h_ is given by _dφF_ ( _h_ ) = �0 _t_ 1 _−F_ <u>1(</u> _s−_ )<sup>_dh_(</sup><sup>_s_) +</sup> �0 _t_ (1 _−hF_ <u>(</u> _s_ ( _−s−_ <u>)</u> ))<sup>2</sup><sup>_dF_(</sup><sup>_s_).TheHadamard</sup> derivative of the cumulative hazard function will be important later when we analyze the well-known Kaplan-Meier estimator.

Finally, there is a generalization of the well-known chain rule for Hadamard differentiation.

**Theorem 0.4.** _Suppose φ_ : _D → E has Hadamard derivative dφP at P ∈ D and that ψ_ : _E → F has Hadamard derivative dψφ_ ( _P_ ) _at φ_ ( _P_ ) _∈ E. Then the composition ψ_ ( _φ_ ) : _D → F has Hadamard derivative dψφ_ ( _P_ )( _dψP_ ) _at P ._

_→_ **proof** : Consider a scalar sequence _tn →_ 0. For _hn ∈ D → h_ , _kn ≡_<sup>_<u>φ</u>_</sup><sup><u>(</u></sup><sup>_P_</sup><sup><u>+</u></sup><sup>_tnh_</sup> _tn_<sup>_n_</sup><sup><u>)</u></sup><sup>_−φ_</sup><sup><u>(</u></sup><sup>_P_</sup><sup><u>)</u></sup> _<u>ψ</u>_ <u>(</u> _<u>φ</u>_ <u>(</u> _P_ <u>+</u> _tnhn_ <u>))</u> _−ψ_ <u>(</u> _<u>φ</u>_ <u>(</u> _P_ <u>))</u> = _dφP_ ( _h_ ), by the Hadamard differentiability of _φ_ at _P_ . Hence, _tn_ _<u>ψ</u>_ <u>(</u> _<u>φ</u>_ <u>(</u> _P_ <u>)+</u> _tntknn_ <u>)</u> _−ψ_ <u>(</u> _<u>φ</u>_ <u>(</u> _P_ <u>))</u> _→ dψφ_ ( _P_ )( _dφP_ ( _h_ )) by the Hadamard differentiability of _ψ_ at _φ_ ( _P_ ), thus proving the desired result. □

7

We now state the main result, which is called the _functional delta method_ .

**Theorem 0.5.** _For D and E normed spaces, suppose φ_ : _D → E has Hadamard derivative dφP at P ∈ D, and that for Xn, X ∈ D,_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Xn − P_ ) = _⇒ X. If X is Borel measurable and separable, then_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _φ_ ( _Xn_ ) _− φ_ ( _P_ )) = _⇒ dφP_ ( _X_ ) _. Further, ∥_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _φ_ ( _Xn_ ) _− φ_ ( _P_ )) _− dφP_ (<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Xn − P_ )) _∥ converges in distribution (so also in outer probability) to zero._

**proof** : Taken from page 374 of van der Vaart and Wellner. By the almost sure representation theorem, there exist _Yn_ = _d √n_ <u>(</u> _Xn − P_ ), _Y_ = _d X_ such that _∥Yn − Y ∥→_ 0 almost surely. Thus<sup>_√_</sup> _<u>n</u>_ <u>(</u> _φ_ ( _Xn_ ) _− φ_ ( _P_ )) = _d_ _<u>φ</u>_ <u>(</u> _P_ <u>+</u> _Yn_ 1 _<u>//</u>_<sup>_<u>√</u>_</sup><sup>_~~<u>√</u>~~_</sup> _<u>nn</u>_ <u>)</u> _−φ_ <u>(</u> _P_ <u>)</u> _→a.s. dφP_ ( _Y_ ) = _d dφ_ ( _X_ ), by the Hadamard differentiability of _φ_ , using 1 _/_<sup>_√_</sup> _<u>n</u>_ in place of _tn_ . This proves the first part. The second part follows by considering the map _ψ_ : _D →_ ( _E, E_ ) defined by _ψ_ ( _d_ ) = ( _φ_ ( _d_ ) _, dφP_ ( _d_ )), with Hadamard derivative ( _dφP , dφP_ ). From this Hadamard differentiability, it follows that (<sup>_√_</sup> _<u>n</u>_ <u>(</u> _φ_ ( _Xn_ ) _− φ_ ( _P_ )) _,_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _dφP_ ( _Xn_ ) _− dφP_ ( _P_ )) = _⇒_ ( _dφP_ ( _X_ ) _, dφP_ ( _X_ )), and then apply the continuous mapping theorem to the difference of the two coordinates. □

---

[← The Ordinary Delta Method](10-the-ordinary-delta-method.md) · [Up: contents](index.md) · [Basics of convergence in Distribution →](12-basics-of-convergence-in-distribution.md)
