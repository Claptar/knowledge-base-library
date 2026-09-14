---
title: 1.1 Probability & Information
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.1 Probability & Information

**Source:** `lectures/01-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We are used to dealing with information presented as a sequence of letters. For example, each word in English languate is composed of _m_ = 26 letters, the text itself includes also spaces and punctuation marks. Similarly in biology the blueprint for any organism is the string of bases along DNA, e.g. _AGTTCCAG· · ·_ , where at each position there is a choice of _m_ = 4 possible characters. This information is then (partly) transcribed into proteins, made of sequences of _m_ = 20 amino acids. Clearly any of these sequences is far from random and there are constraints and correlations at many scales that conspire to make them meaningful. Nonetheless, as a means to unravel such constraints, it may be helpful to start with simple models which assume that sequences are randomly generated according to some rules. Comparisons of such models with the actual sequences may then provide some insights.

As a simple example, let us consider a sequence of _N_ characters, each chosen independently with probabilities _{pα}_ , with _α_ = 1 _,_ 2 _, · · · , m_ . (This choice is sometimes referred to as IID, for _identical, independently distribute_ random variables.) Since the probabilities must be normalized, we require


The probability of finding a sequence _S_ = _{α_ 1 _, · · · , αN }_ is then given by the product of probabilities for its elements, as


How many other sequences _S_<sup>_′_</sup> have this probability? Clearly as long as the number of occurrences _{Nα}_ of each character is the same, the probability will be identical, i.e. the order of the elements does not matter in calculating the probability for this simple model. The number _N_ of possible permutations of the elements in _S_ is


This is known as the multinomial coefficient, as it occurs in the expression


where the sum is restricted so that<sup>�</sup><sup>_m_</sup> _α_ =1<sup>_Nα_=</sup><sup>_N_.Note that because of normalization, both</sup> sides of the above equation are equal 1. The terms within the sum on the right-hand side are known the _multinomial probabilities_


1

With the assumption of independence, the probability of a sequence is determined entirely by the set _{Nα}_ according to Eq. (1.5). It is easy to check that the most likely set (the mode _{Nα_<sup>_∗}_)coincideswiththeaverage(mean</sup><sup>_{⟨Nα⟩}_),andgivenby</sup>


Indeed, in the limit of large _N_ , the overwhelming number of sequences generated will have the above composition. The number of sequences with character counts _Nα_ = _pαN_ is given by Eq. (1.3). Crudely speaking, this number _N_ helps quantify the “information” contained within a sequence of length _N_ , as it indicates how many different sequences have the same composition of characters (and hence the same _a priori_ probability. We expect a good measure of information content to scale roughly linearly with the message length. (In the absence of context clues or syntax rules, a message twice as long should carry about twice as much information.) As convenient measure, and taking clues from Statistical Mechanics, we take the logarithm of Eq. (1.3), which gives


(Stirling’s approximation for _N_ ! is used for all _Nα ≫_ 1.) The above formula is closely related to the _entropy of mixing_ in thermodynamics, and quite generally for any set of probabilities _{pα}_ , we can define a _mixing entropy_


Entropy is typically envisioned as a measure of disorder, and the information content _I_ ( _{pα}_ ) (picking up a specific element amongst a jumble of possibilities) is related to _−S_ ( _{pα}_ ).

Let us illustrate the relations among entropy and information in the context of DNA. To transmit a sequence, _ACTG · · ·_ , along a binary channel we need to encode 2 _N_ bits, as there are (2<sup>2</sup> )<sup>_N_</sup> possibilities. However, suppose that from prior analysis of DNA of a particular organism, we know that a typical sequence of length _N_ has a likely composition _⟨NA⟩̸_ = _⟨NG⟩̸_ = _· · ·_ . Given _a priori_ knowledge of the probabilities _pα_ = _Nα/N_ , the number of such likely sequences is


or, upon taking the logarithm,


We gain a definite amount of knowledge by having advance insight about _{pα}_ . Instead of having to specify 2 bits per “letter” of DNA, we can get by with a smaller number. The information gained per letter is given by


If _pα_ = 1 _/_ 4, then Eq. (1.8) reduces to 0, which is consistent—we gain no information. On the other hand, if _pA_ = _pT_ = 0 and _pC_ = _pG_ =<sup><u>1</u></sup> 2<sup>,then</sup>

---

[Up: contents](index.md) · [1.2 Evolving Probabilities →](02-1-2-evolving-probabilities.md)
