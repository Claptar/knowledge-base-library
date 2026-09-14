---
title: 15 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 15 slides

**Source:** `lectures/15-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LECTURE 15

# Review

Poisson process — II

- Readings: Finish Section 6.2.

   - Defining characteristics

-

   - Time homogeneity: _P_ ( _k, τ_ )

      - Independence

   - Small interval probabilities (small _δ_ ):

- Review of Poisson process

- Merging and splitting

- Examples

- Random incidence


**E** [ _Nτ_ ] = var( _Nτ_ ) = _λτ_


- Time _Yk_ to _k_ th arrival: Erlang( _k_ ):


# Poisson fishing

- Assume: Poisson, _λ_ = 0 _._ 6/hour.

- Fish for two hours.

- if no catch, continue until first catch.

- a) **P** (fish for more than two hours)=

- b) **P** (fish for more than two and less than five hours)=

- c) **P** (catch at least two fish)=

# Merging Poisson Processes (again)

- Merging of independent Poisson processes is Poisson


<!-- Start of picture text -->
Red bulb flashes<br> (Poisson)<br>All  flashes<br>"1  (Poisson)<br>"2<br>Green bulb flashes<br> (Poisson)<br><!-- End of picture text -->

   - What is the probability that the next arrival comes from the first process?

- d) **E** [number of fish]=

- e) **E** [future fishing time _|_ fished for four hours]=

- f) **E** [total fishing time]=

1

# Light bulb example

- Each light bulb has independent, exponential( _λ_ ) lifetime

- Install three light bulbs. Find expected time until last light bulb dies out.

# Splitting of Poisson processes

- Assume that email traffic through a server is a Poisson process. Destinations of different messages are independent.


<!-- Start of picture text -->
USA<br>Email Traffic<br>leaving  MIT MIT p !<br>Server<br>! (1 -  p )!<br>Foreign<br><!-- End of picture text -->

- Each output stream is Poisson.

# Random incidence for Poisson

- Poisson process that has been running forever

- Show up at some “random time” (really means “arbitrary time”)

# Random incidence in “renewal processes”

- Series of successive arrivals

- i.i.d. interarrival times

   - (but not necessarily exponential)

- Example:


<!-- Start of picture text -->
x x x x x<br>Time<br>Chosen<br>time instant<br><!-- End of picture text -->

   - Bus interarrival times are equally likely to be 5 or 10 minutes

   - If you arrive at a “random time”:

   - what is the probability that you selected a 5 minute interarrival interval?

- What is the distribution of the length of the chosen interarrival interval?

- what is the expected time to next arrival?

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
