---
title: 14 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 slides

**Source:** `lectures/14-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LECTURE 14

The Poisson process

- Readings: Start Section 6.2.

# Lecture outline

- Review of Bernoulli process

- Definition of Poisson process

# Bernoulli review

   - Discrete time; success probability _p_

   - Number of arrivals in _n_ time slots: binomial pmf

   - Interarrival times: geometric pmf

   - Time to _k_ arrivals: Pascal pmf

   - Memorylessness

- Distribution of number of arrivals

- Distribution of interarrival times

- Other properties of the Poisson process

# Definition of the Poisson process


<!-- Start of picture text -->
t 1 t 2 t 3 !<br>x x x x x x x x x x x<br>0<br>Time<br><!-- End of picture text -->

- Time homogeneity: _P_ ( _k, τ_ ) = Prob. of _k_ arrivals in interval of duration _τ_

# PMF of Number of Arrivals _N_


<!-- Start of picture text -->
t 1 t 2 t 3 !<br>x x x x x x x x x x x<br>0<br>Time<br><!-- End of picture text -->

   - Finely discretize [0 _, t_ ]: approximately Bernoulli

   - _Nt_ (of discrete approximation): binomial

- Numbers of arrivals in disjoint time intervals are independent

- Small interval probabilities: For VERY small _δ_ :

1 _− λδ,_ if _k_ = 0; _P_ ( _k, δ_ ) _≈_  _λδ,_ 0 _,_ ifif _kk_ = 1; _>_ 1 _._ – _λ_ : “arrival rate”


1

# Example

- You get email according to a Poisson process at a rate of _λ_ = 5 messages per hour. You check your email every thirty minutes.

- Prob(no new messages) =

- Prob(one new message) =

# Interarrival Times

- _Yk_ time of _k_ th arrival

- Erlang distribution:


<!-- Start of picture text -->
λ k y k− 1 e −λy<br>fYk ( y ) = ( k − 1)! , y ≥ 0<br>flr (l)<br>r = 1<br>r = 2<br>r = 3<br>l<br>0<br><!-- End of picture text -->

Image by MIT OpenCourseWare.

- Time of first arrival ( _k_ = 1): exponential: _fY_ 1( _y_ ) = _λe_<sup>_−λy_</sup> _, y ≥_ 0

- Memoryless property: The time to the next arrival is independent of the past

# Bernoulli/Poisson Relation


<!-- Start of picture text -->
! ! ! ! ! ! ! !<br>n = t / !<br>x x x np   =" t<br>0 Time p  ="!<br>Arrivals<br><!-- End of picture text -->


<!-- Start of picture text -->
POISSON BERNOULLI<br>Times of Arrival Continuous Discrete<br>Arrival Rate λ /unit time p /per trial<br>PMF of # of Arrivals Poisson Binomial<br>Inte rarrival Time Distr. Exponential Geometric<br>Time to k -th arrival Erlang Pascal<br><!-- End of picture text -->

# Merging Poisson Processes

- Sum of independent Poisson random variables is Poisson

- Merging of independent Poisson processes is Poisson


<!-- Start of picture text -->
Red bulb flashes<br> (Poisson)<br>All  flashes<br>"1  (Poisson)<br>"2<br>Green bulb flashes<br> (Poisson)<br><!-- End of picture text -->

- What is the probability that the next arrival comes from the first process?

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2010

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
