---
title: n -step transition probabilities
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# n -step transition probabilities

**Source:** `lectures/16-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- State occupancy probabilities, given initial state _i_ :

- belongs to a finite set, e.g., _{_ 1 _, . . . , m}_

- _X_ 0 is either given or random

- Markov property/assumption: (given current state, the past does not matter)

_pij_ = P( _Xn_ +1 = _j | Xn_ = _i_ ) = P( _Xn_ +1 = _j | Xn_<sup>=</sup><sup>_i,X_</sup> _n−_ 1<sup>_, . . . , X_</sup> 0<sup>)</sup>

- Model specification:

- identify the possible states

- identify the possible transitions

- identify the transition probabilities


<!-- Start of picture text -->
rij ( n ) = P( Xn =  j | X 0 =  i )<br><!-- End of picture text -->


<!-- Start of picture text -->
Time 0 Time  n-1 Time  n<br>1<br>r (n-1)i1 p 1j<br>i k<br>r ik(n-1)<br>pkj j<br>r im(n-1) p mj<br>m<br>...<br>...<br><!-- End of picture text -->

- Key recursion:


<!-- Start of picture text -->
m<br>rij ( n ) = � rik ( n − 1) pkj<br>k =1<br><!-- End of picture text -->

- With random initial state:


1


<!-- Start of picture text -->
Example<br>0.5 0.8<br>0.5<br>1 2<br>0.2<br><!-- End of picture text -->


<!-- Start of picture text -->
n  = 0 n  = 1 n  = 2 n  = 100 n  = 101<br>r 11( n )<br>r 12( n )<br>r 21( n )<br>r 22( n )<br><!-- End of picture text -->

   - Generic convergence questions:

- Does _rij_ ( _n_ ) converge to something?


<!-- Start of picture text -->
0.5 0.5<br>1 2 3<br>1 1<br>n odd: r 22 (n)= n even: r 22 (n)=<br><!-- End of picture text -->

- Does the limit depend on initial state?


<!-- Start of picture text -->
0.4<br>1 2 3 4<br>0.3 0.3<br>r11(n)=<br>r31(n)=<br>r21(n)=<br><!-- End of picture text -->

---

[← Finite state Markov chains](02-finite-state-markov-chains.md) · [Up: contents](index.md) · [Recurrent and transient states →](04-recurrent-and-transient-states.md)
