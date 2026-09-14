---
title: 17 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/17-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 solutions

**Source:** `solutions/17-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 17 Solutions November 4, 2010

1. (a) K has a Poisson distribution with average arrival time µ = λcT


- (c) Since the conscious and subconscious responses are generated independently,

P(r conscious responses and s subconscious responses in interval T )


- (d) Let Xs = the time from the start of the exam to the time of the 1st subconscious response, and Xc = the time from the 1st subconscious response to the time of the next conscious response.

Note that Xs and Xc are independent exponentially distributed random variables with parameters λs and λc , respectively.


X = Xs + Xc. So its PDF is the convolution of the two exponential distributions. For x ≥ 0


2. (a) Since we are looking for the number of “trials” up to and including the first “success,” N is a geometric random variable with parameter p.


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

   - (b) The length of time spent driving to each intersection is exponentially distributed with pa­ rameter λ. Since the probability of Shem observing an accident at a given intersection is p, the distribution of the length of time in between accident reports is exponential but with parameter pλ (think of Poisson splitting). Thus,

      - fQ(q) = (pλ)e<sup>−qpλ</sup> , q ≥ 0.

   - (c) Since the interarrival time of accidents is exponentially distributed with parameter pλ, the number of arrivals in a given amount of time τ is a Poisson random variable with parameter pλτ . Thus, (2

   - P(m arrivals in 2 hours) = pM (m) =<sup>e</sup><sup>`−`2pλ</sup> m!pλ)<sup>m</sup> , m ≥ 0.

   - (d) We can view the radio calls to Shem and the accident reports as independent Poisson processes with arrival rates µ and pλ, respectively. When the two independent Poisson processes are joined, the resultant is a Poisson process with arrival rate µ+pλ. Furthermore, the probability of an arrival from the radio calls is µ+µpλ<sup>. Since we are interested in the</sup> number of reported accidents between two radio calls, we can view this is a shifted Geometric random variable with parameter µ+µpλ<sup>. Thus,</sup>

      - pK(k) = ( µ+pλ pλ )k( µ+µpλ<sup>),</sup> k ≥ 0.

   - (e) If we begin to observe Shem’s radio calls at some random instant in time, due to the memoryless property of Poisson interarrivals, the distribution until he recieves the next call will still be exponential with parameter µ. Also, the time from the previous call until the point at which we begin to observe Shem is also an exponential distribution with parameter µ. Thus, W = X1 + X2, where X1 and X2 have exponential distributions, i.e. W is a second order Erlang PDF.

      - fW (w) = (µ)<sup>2</sup> we−wµ

3. See problem 6.27, page 337 in the textbook.

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
