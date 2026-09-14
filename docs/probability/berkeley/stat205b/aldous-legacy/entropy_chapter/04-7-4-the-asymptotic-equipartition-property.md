---
title: 7.4 The asymptotic equipartition property
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.4 The asymptotic equipartition property

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We now jump into math theory to state a non-elementary result, and accompany it with some discussion. The basis of the mathematical theory is that we model the source of plaintext as random “characters” _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ in some “alphabet”. It is important to note that we do _not_ model them as independent (even though I use independence as the simplest case for mathematical calculation later) since real English plaintext obviously lacks independence. Instead we model the sequence ( _Xi_ ) as a _stationary process_ , which implies that there is some probability that three consecutive characters are CHE, but this probability does not depend on position in the sequence, and we don’t make any assumptions about what the probability is.

To say the setup more carefully, for any sequence of characters ( _x_ 1 _, . . . , xn_ ) there is a _likelihood_


The _stationarity_ assumption is that for each time _t_ and each sequence ( _x_ 1 _, . . . , xn_ )


Consider the _empirical likelihood_


which is the prior chance of seeing the sequence that actually turned up. The central result (non-elementary; I teach it in a graduate course as the Shannon-McMillan-Breiman theorem) is

_7.4. THE ASYMPTOTIC EQUIPARTITION PROPERTY_

109

**The asymptotic equipartition property (AEP) .** For a stationary ergodic<sup>4</sup> source, there is a number _Ent_ , called the _entropy rate_ of the source, such that for large _n_ , with high probability


The rest of this section is the mathematical discussion of the theorem that I say in class. I’m not going to attempt to translate it for the general reader, who should skip to the next section to see the relevance to coding. It is conventional to use base 2 logarithms in this context, to fit nicely with the idea of coding into bits.

For _n_ tosses of a hypothetical biased coin with P( _H_ ) = 2 _/_ 3 _,_ P( _T_ ) = 1 _/_ 3, the _most likely_ sequence is _HHHHHH . . . HHH_ , which has likelihood (2 _/_ 3)<sup>_n_</sup> , but a _typical_ sequence will have about 2 _n/_ 3 H’s and about _n/_ 3 T’s, and such a sequence has likelihood _⇡_ (2 _/_ 3)<sup>2</sup><sup>_n/_3</sup> (1 _/_ 3)<sup>_n/_3</sup> . So


Note in particular that log-likelihood behaves di↵erently from the behavior of sums, where the CLT implies that a “typical value” of a sum is close to the most likely individual value.

Recall that the _entropy_ of a probability distribution **q** = ( _qj_ ) is defined as the number


The AEP provides one of the nicer motivations for the definition, as follows. If the sequence ( _Xi_ ) is IID with marginal distribution ( _pa_ ) then for **x** = ( _x_ 1 _, . . . , xn_ ) we have


where _na_ ( **x** ) is the number of appearances of _a_ in **x** . Because _na_ ( _X_ 1 _, . . . , Xn_ ) _⇡ npa_ we find


> 4The formal definition of ergodic is hard to understand; basically we exclude a source that flips a coin to choose between “all English” and “all Russian”.

_CHAPTER 7. CODING AND ENTROPY_

110

So the AEP identifies the _entropy rate_ of the IID sequence with the _entropy E_ = _−_<sup>P</sup> _a_<sup>_pa_log</sup> 2<sup>_pa_ofthemarginaldistributions</sup><sup>_X_.</sup>

Let me mention three technical facts.

**Fact 1.** (easy). For a 1-1 function _C_ (that is, a code that can be be decoded precisely), the distributions of a random item _X_ and the coded item _C_ ( _X_ ) have equal entropy.

**Fact 2.** (easy). Amongst probability distributions on an alphabet of size _B_ , entropy is maximized by the uniform distribution, whose entropy is log2 _B_ . So for any distribution on binary strings of length _m_ , the entropy is at most log2 2<sup>_m_</sup> = _m_ .

**Fact 3.** (less easy). Think of a string ( _X_ 1 _, . . . , Xn_ ) as a single random object. It has some entropy _Ek_ . In the setting of the AEP,


Finally a conceptual comment. Identifying the entropy rate of an IID sequence with the entropy of its marginal distribution indicates that _entropy_ is the relevant summary statistic for the non-uniformness of a distribution when we are in some kind of _multiplicative_ context. This is loosely analogous to the topic of Lecture 2, the Kelly criterion, which is tied to “multiplicative” investment.

---

[← 7.3 Coding, compression and encryption](03-7-3-coding-compression-and-encryption.md) · [Up: contents](index.md) · [7.5 Entropy rate and minimum code length →](05-7-5-entropy-rate-and-minimum-code-length.md)
