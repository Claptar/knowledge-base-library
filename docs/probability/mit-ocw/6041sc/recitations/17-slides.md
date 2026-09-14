---
title: 17 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 slides

**Source:** `recitations/17-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 17 November 4, 2010

1. Iwana Passe is taking a multiple-choice exam. You may assume that the number of questions is infinite. Simultaneously, but independently, her conscious and subconscious faculties are gen­ erating answers for her, each in a Poisson manner. (Her conscious and subconscious are always working on different questions.) Conscious responses are generated at the rate λc responses per minute. Subconscious responses are generated at the rate λs responses per minute. Assume λc = λs. Each conscious response is an independent Bernoulli trial with probability pc of being correct. Similarly, each subconscious response is an independent Bernoulli trial with probability ps of being correct. Iwana responds only once to each question, and you can assume that her time for recording these conscious and subconscious responses is negligible.

   - (a) Determine pK(k), the probability mass function for the number of conscious responses Iwana makes in an interval of T minutes.

   - (b) If we pick any question to which Iwana has responded, what is the probability that her answer to that question:

      - i. Represents a conscious response

      - ii. Represents a conscious correct response

   - (c) If we pick an interval of T minutes, what is the probability that in that interval Iwana will make exactly r conscious responses and s subconscious responses?

   - (d) Determine the probability density function for random variable X, where X is the time from the start of the exam until Iwana makes her first conscious response which is preceded by at least one subconscious response.

2. Shem, a local policeman, drives from intersection to intersection in times that are independent and all exponentially distributed with parameter λ. At each intersection he observes (and reports) a car accident with probability p. (This activity does not slow his driving at all.) Independently of all else, Shem receives extremely brief radio calls in a Poisson manner with an average rate of µ calls per hour.

   - (a) Determine the PMF for N , the number of intersections Shem visits up to and including the one where he reports his first accident.

   - (b) Determine the PDF for Q, the length of time Shem drives between reporting accidents.

   - (c) What is the PMF for M , the number of accidents which Shem reports in two hours?

   - (d) What is the PMF for K, the number of accidents Shem reports between his receipt of two successive radio calls?

   - (e) We observe Shem at a random instant long after his shift has begun. Let W be the total time from Shem’s last radio call until his next radio call. What is the PDF of W ?

3. Problem 6.27, page 337 in the textbook. Random incidence in an Erlang arrival process. Consider an arrival process in which the interarrival times are independent Erlang random vari­ ables or order 2, with mean 2/λ. Assume that the arrival process has been ongoing for a very long time. An external observer arrives at a given time t. Find the PDF of the length of the interarrival interval that contains t.

Textbook problems are courtesy of Athena Scientific, and are used with permission.

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
