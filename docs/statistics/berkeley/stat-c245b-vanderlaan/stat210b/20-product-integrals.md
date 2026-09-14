---
title: Product Integrals
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Product Integrals

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Our treatment is based on section 3.9 of van der Vaart and Wellner. For an excellent overview, see _www.math.uu.nl/people/gill/Preprints/prod_ _~~i~~ nt_ ~~0~~ _.pdf_

Definition: Let _D_ [0 _, b_ ] denote the space of cadlag functions on (0 _, b_ ]. The _product integral_ of _A ∈ BVM ⊂ D_ [0 _, b_ ] is a function _φ_ ( _A_ ) _∈ D_ [0 _, b_ ] denoted by _φ_ ( _A_ )( _t_ ) = Π0 _<s≤t_ (1+ _dA_ ( _s_ )). It is defined by limmax _i |ti−ti−_ 1 _|→_ 0 Π _i_ (1+ _A_ ( _ti_ ) _−A_ ( _ti−_ 1)), where the limit is taken over partitions 0 = _t_ 0 _< t_ 1 _< ... < tn_ = _t_ with sup0 _≤s≤b_ min1 _≤i≤n |ti − s| →_ 0. It can be shown that the limit exists and is unique, and doesn’t depend on which sequence

12

of partitions ( _t_ 0 _, t_ 1 _, ..., tn_ ) is chosen, so _φ_ ( _A_ ) is well-defined. For _s < t_ , _φ_ ( _A_ )( _s, t_ ] is notation for<sup>_<u>φ</u>_</sup><sup><u>(</u></sup><sup>_A_</sup><sup><u>)(</u></sup><sup>_t_</sup><sup><u>)</u></sup> _φ_ ( _A_ )( _s_ )<sup>.</sup>

Another way to represent the product integral is as follows.

**Theorem 0.8.** _For A ∈ BVM ⊂ D_ (0 _, b_ ] _, the product integral φ_ ( _A_ ) _∈ D_ [0 _, b_ ] _is equal to the unique solution of the Volterra equation φ_ ( _A_ )( _t_ ) = 1 + �0 _t_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_s−_)</sup><sup>_dA_(</sup><sup>_s_)</sup><sup>_,for_</sup> 0 _≤ t ≤ b._

Suppose that _a_ 1 _, ..., an, b_ 1 _, ..., bn_ are real numbers. It is easy to check by induction that Π<sup>_n_</sup> _i_ =1<sup>_ai−_Π</sup><sup>_n_</sup> _i_ =1<sup>_bi_= �</sup><sup>_n_</sup> _i_ =1<sup>(Π</sup><sup>_i_</sup> _j_<sup>_−_</sup> =1<sup>1</sup><sup>_aj_)(</sup><sup>_ai−bi_)(Π</sup> _k_<sup>_n_</sup> = _i_ +1<sup>_bk_).For</sup><sup>_n ≤_2, it is just algebra to check</sup> that _a_ 1 _a_ 2 _− b_ 1 _b_ 2 = ( _a_ 1 _− b_ 1) _b_ 2 + _a_ 1( _a_ 2 _− b_ 2). For _n >_ 2, let ˜ _a_ 2 = Π<sup>_n_</sup> _i_ =2<sup>_ai_and ˜</sup><sup>_b_2= �</sup><sup>_n_</sup> _i_ =2<sup>_bi_.</sup> Then Π<sup>_n_</sup> _i_ =1<sup>_ai−_Π</sup><sup>_n_</sup> _i_ =1<sup>_bi_=</sup><sup>_a_1</sup><sup>_a_˜2</sup><sup>_−b_1˜</sup><sup>_b_2=(</sup><sup>_a_1</sup><sup>_−b_1)˜</sup><sup>_b_2+</sup><sup>_a_1(˜</sup><sup>_a_2</sup><sup>_−_˜</sup><sup>_b_2)=(</sup><sup>_a_1</sup><sup>_−b_1) �</sup><sup>_n_</sup> _i_ =2<sup>_bi_+</sup> _a_ 1 � _ni_ =2<sup>(Π</sup><sup>_i_</sup> _j_<sup>_−_</sup> =2<sup>1</sup><sup>_aj_)(</sup><sup>_ai−bi_)(Π</sup> _k_<sup>_n_</sup> = _i_ +1<sup>_bk_) = �</sup> _i_<sup>_n_</sup> =1<sup>(Π</sup><sup>_i_</sup> _j_<sup>_−_</sup> =1<sup>1</sup><sup>_aj_)(</sup><sup>_ai−bi_)(Π</sup> _k_<sup>_n_</sup> = _i_ +1<sup>_bk_).This</sup><sup>_telescoping_</sup> _trick_ for representing differences of products can be generalized to differences of product integrals with the following result, known as the _Duhamel equation_ .

**Theorem 0.9.** _Suppose that A, B ∈ BVM ⊂ D_ [0 _, b_ ] _. If φ denotes the product integral, then φ_ ( _B_ )( _t_ ) _− φ_ ( _A_ )( _t_ ) = �0 _t_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_B_)(</sup><sup>_u, t_]</sup><sup>_d_(</sup><sup>_B −A_)(</sup><sup>_u_)</sup><sup>_._</sup>

We will need a further result before we can give the Hadamard derivative of the product integral. This can be proven by integration by parts. See problem 3.9.8 of van der Vaart and Wellner.

**Theorem 0.10.** _Suppose that A, B ∈ BVM ⊂ D_ [0 _, b_ ] _. Recall that φ_ ( _A_ ) _, φ_ ( _B_ ) _∈ D_ [0 _, b_ ] _. For d ∈ D_ [0 _, b_ ] _, ∥d∥∞ denotes_ sup0 _≤t≤b |d_ ( _t_ ) _|. If φ denotes the product integral, then ∥φ_ ( _B_ ) _− φ_ ( _A_ ) _∥∞ ≤ C_ ( _M_ ) _∥B − A∥∞ for a constant C_ ( _M_ ) _depending on M . Thus, product integration is uniformly continuous._

We are now ready to provide the main result on product integration.

**Theorem 0.11.** _φ_ : ( _BVM , ∥·∥∞_ ) _⊂_ ( _D_ [0 _, b_ ] _, ∥·∥∞_ ) _→_ ( _D_ [0 _, b_ ] _, ∥·∥∞_ ) _is Hadamard differentiable at A ∈ BVM ⊂ D_ [0 _, b_ ] _, with Hadamard derivative dφA_ ( _α_ )( _t_ ) = �0 _t_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_A_)(</sup><sup>_u, t_]</sup><sup>_dα_(</sup><sup>_u_)</sup><sup>_,_</sup> _where φ denotes the product integral._

**sketch of proof** : Suppose a scalar sequence _tn →_ 0 and _αn ∈ D_ [0 _, b_ ] _→ α ∈ D_ [0 _, b_ ]. _− ∥_<sup>_<u>φ</u>_</sup><sup><u>(</u></sup><sup>_A_</sup><sup><u>+</u></sup><sup>_tnα_</sup> _tn_<sup>_n_</sup><sup><u>)</u></sup><sup>_−φ_</sup><sup><u>(</u></sup><sup>_A_</sup><sup><u>)</u></sup> �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_A_)(</sup><sup>_u, ·_]</sup><sup>_dα_(</sup><sup>_u_)</sup><sup>_∥∞_</sup>

= _∥ t_<sup><u>1</u></sup> _n_ �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_A_+</sup><sup>_tnαn_)(</sup><sup>_u, ·_]</sup><sup>_d_(</sup><sup>_A −A_+</sup><sup>_tnαn_)</sup><sup>_−_</sup> �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_A_)(</sup><sup>_u, t_]</sup><sup>_dα_(</sup><sup>_u_)</sup><sup>_∥∞_</sup> = _∥_ �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_An_)(</sup><sup>_u, ·_]</sup><sup>_dαn_(</sup><sup>_u_)</sup><sup>_−_</sup> �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_A_)(</sup><sup>_u, t_]</sup><sup>_dα_(</sup><sup>_u_)</sup><sup>_∥∞_</sup>

If _αn_ or _α_ is replaced with _α_ ˜, the error in each integral is bounded by a constant times _∥αn − α_ ˜ _∥∞_ or _∥α − α_ ˜ _∥∞_ respectively, which can be shown with integration by parts. By choosing _α_ ˜ of bounded variation close to _α_ (and thus _αn_ for sufficiently large _n_ ) it suffices to show that _∥_ �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_An_)(</sup><sup>_u, t_]</sup><sup>_dα_˜(</sup><sup>_u_)</sup><sup>_−_</sup> �0 _·_<sup>_φ_(</sup><sup>_A_)(</sup><sup>_u_)</sup><sup>_φ_(</sup><sup>_A_)(</sup><sup>_u, t_]</sup><sup>_dα_˜(</sup><sup>_u_)</sup><sup>_∥∞→_0.</sup> This follows because _φ_ ( _An_ ) converges uniformly to _φ_ ( _A_ ) by the previous theorem. □

13

---

[← Note on Integration Theory](19-note-on-integration-theory.md) · [Up: contents](index.md) · [Product Integrals and Cumulative Hazards →](21-product-integrals-and-cumulative-hazards.md)
