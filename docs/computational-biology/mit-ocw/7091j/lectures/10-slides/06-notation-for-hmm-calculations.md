---
title: Notation for HMM Calculations
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Notation for HMM Calculations

**Source:** `lectures/10-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Random vector of observable<br>data (DNA bases)<br>Random vector of hidden states<br>P ( H  = h 1,..., hn , O  = o 1,..., on )<br>Specific hidden state values<br>Specific sequence of bases<br>Another specific set of hidden state values<br>P ( H  = h  ʹ′ 1,..., h  ʹ′  n , O  = o 1,..., on )<br><!-- End of picture text -->

21

Reversing the Hidden/Observable Conditioning (Bayes’ Rule)

_P_ ( _H_ = _h_ 1, _h_ 2 ,..., _hn_ | _O_ = _o_ 1, _o_ 2 ,..., _on_ ) Conditional Prob: P(A|B) = P(A,B)/P(B)

_P_ <u>(</u> _H_ = _h_ 1,..., _hn_ <u>,</u> _O_ = _o_ 1, ..., _on_ <u>)</u> = _P_ ( _O_ = _o_ 1,..., _on_ )

_P_ <u>(</u> _H_ = _h_ 1,..., _hn_ <u>)</u> _P_ <u>(</u> _O_ = _o_ 1 <u>,...,</u> _on_ | _H_ = _h_ 1,..., _hn_ <u>)</u> = _P_ ( _O_ = _o_ 1,..., _on_ )

- _P_ ( _O_ = _o_ 1 ,..., _on_ ) a bit tricky to calculate, but is independent of _h1,…, hn_ so can treat as a constant and simply maximize

- _P_ ( _H_ = _h_ 1,..., _hn_ , _O_ = _o_ 1,..., _on_ )

22

Inferring the Hidden from the Observable (Viterbi Algorithm)

_H_<sup>_opt_</sup> = _h_<sup>_opt_</sup> _h_<sup>_opt_</sup> _h_<sup>_opt_</sup> Want to find sequence of hidden states 1<sup>,</sup> 2<sup>,</sup> 3<sup>,...</sup> that maximizes joint probability: _P_ ( _H_ = _h_ 1,..., _hn_ , _O_ = _o_ 1,..., _on_ ) (optimal “parse” of sequence)

<u>Solution:</u> Define _R_<sup>(</sup> _h_ )= probability of optimal parse of the _i_ subsequence 1..i ending in state h

( _h_ ) ( _h_ ) Solve recursively, i.e. determine _R_ 2 in terms of _R_ 1 , etc.

23


© source unknown. All rights reserved. This content is excluded from our Creative Commons license For more information, see http://ocw.mit.edu/help/faq-fair-use/.


© Lan56 on wikipedia. Some rights reserved. License: CC-BY-SA. This content is excluded from our�Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### Andrew Viterbi, an MIT BS/MEng student in E.E. - founder of Qualcomm

24


<!-- Start of picture text -->
“Initiation<br>Rabiner notation<br>CpG Island HMM<br>probabilities” πj<br>Pgg = 0.99999 Pig = 0.001<br>Pg = 0.99, Pi = 0.01<br>Genome<br>Pii = 0.999<br>“Transition<br>probabilities” aij Pgi = 0.00001 Island<br>…<br>A      C       T       C       G      A       G      T       A<br> C  G  A  T<br>“Emission<br>Probabilities” bj(k) CpG Island:  0.3  0.3  0.2  0.2<br>Genome: 0.2  0.2  0.3  0.3<br><!-- End of picture text -->

probability of optimal parse of the the state at t-1 that resulted in δt(i) ψt(i) subsequence 1..t ending in state i the optimal parse of 1..t ending in i


N no. of states T length of sequence

Viterbi Algorithm

Rabiner 1989

26

---

[← Hidden Markov Model Example](05-hidden-markov-model-example.md) · [Up: contents](index.md) · [Viterbi Example →](07-viterbi-example.md)
