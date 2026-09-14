---
title: 'Exam #1, Fall 2012'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/exams/01-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Exam #1, Fall 2012

**Source:** `exams/01-exam.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## <u>Instructions</u>

- 1) Please do not open the exam until instructed to do so. 2) This exam is closed‐book and closed‐notes. 3) Please do all problems.

- 4) Use the back of sheets if you need more space. 5) Please write clearly

Name:

## <u>Scores</u>

1 (out of 13):

- 2 (out of 15):

- 3 (out of 15):

4 (out of 10):

5 (out of 20):

- 6 (out of 15):

- 7 (out of 12):

Total (out of 100):

1

Fall 2012 Systems Biology, Exam #1

## **1) Response time (13 points)**

a)  Define the response time to be the time necessary to get half way from one equilibrium concentration to a new equilibrium concentration.  For simple regulation of a stable protein, how does the ON response time compare to the OFF response time?  (3 pts)

b)  One way to speed the response time is to actively degrade a protein.  In this case, how does the ON response time compare to the OFF response time?  (3 pts)

c) In the case of negative autoregulation, how does the ON response time compare to the OFF response time? (3 pts)

‐ d) The coherent type 1 FFL with OR logic leads to a delay when turning ON or when turning OFF?  Explain briefly.  (4 pts)

2

Fall 2012 Systems Biology, Exam #1


a.  If _m_ is the mRNA concentration and _p_ is the protein concentration then what network motif do the above equations describe? (3 pts)

b.  What does time t = 1 correspond to? (2 pts)

c.  How many fixed points are there?  Solve for the location of each fixed point. (4 pts)

d.  Calculate the stability of each fixed point. Does this system oscillate? (6 pts)

3

Fall 2012 Systems Biology, Exam #1

**3)  Basic model of gene expression (15 points)**


a.  What is the mean number of mRNA in the cell? (3 pts)

b. What is the mean number of proteins in the cell? (3 pts)

c. Draw a histogram of the probability distribution of mRNA in the cell assuming that all four rates in the model above are equal to 20 sec‐1. (3 pts)

d.  We found in class that the probability distribution of protein number _x_ in the cells is given by a gamma distribution: (6 pts)


i)  What is _a_ in words, and what is it in terms of the rates given in the model above?

ii)  What is _b_ in words, and what is it in terms of the rates given in the model above?

4

Fall 2012 Systems Biology, Exam #1

**4)  Analysis of network motifs (10 points).** For this problem, an arrow will signify either positive or negative regulation.  In Uri Alon’s book/paper, he studied the transcriptional network of _E. coli_ , which had N = 424 nodes (genes) and E = 519 edges (interactions).

Consider the sub‐graph corresponding to X ‐> Y ‐> Z.

a. Given a random Erdos‐Renyi network, how many of these sub‐graphs do you expect to see? (5 pts)

b.  Given an expectation of observing <NG> of these sub‐graphs, what is the standard deviation that would be observed in different ER networks? (3 pts)

c.  Was this a network motif in Uri’s transcription network?  (2 pts)

5

Fall 2012 Systems Biology, Exam #1

## **5) Probing gene expression in live cells, one protein molecule at a time (20 points total)**


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

a.  In subplot (D), what are the authors trying to show? (3 pts)


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

b.  In this figure, what is the difference between the three plots? (2 pts)

c.  In the middle plot, how many protein “bursts” are there?  What is the number of proteins produced in each burst?  (4 pts)

6

Fall 2012 Systems Biology, Exam #1


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

d.  Consider the black fits in each of the two plots above analyzing bursts of protein production. (8 points)

Figure A:

1. Name of distribution:

2. Equation describing distribution:

3. Approximate parameter value(s) in the fit:

## Figure B:

   1. Name of distribution:

   2. Equation describing distribution:

   3. Approximate parameter value(s) in the fit:

- e.  What was the (approximate) mean number of mRNA molecules per protein burst?  (3 pts)

7

Fall 2012 Systems Biology, Exam #1

## **6)  Stochastic reactions (15 points)**

Consider the protein invertase that can either hydrolyze a molecule of sucrose at rate ksuc =  10 sec<sup>‐1</sup> or a molecule of raffinose at rate kraff = 2 sec<sup>‐1</sup> .

a)  What is the probability density function _p(ti)_ for the time that each chemical reaction will occur?  Please draw the two probability density functions on the same plot and label the x‐axis with the relevant timescales. (4 pts)

b)  What is the cumulative probability distribution for each chemical reaction _P(t)_ , defined as the probability that the reaction occurs by time _t_ ?  Once again, please draw the two cumulative probability distributions on the same plot and label the x‐axis and y‐axis. (3 pts)

8

Fall 2012 Systems Biology, Exam #1

c) What is the probability that neither of these two reactions has occurred by time _t_ ? (3 pts)

d) What is the probability density function for the time before the first of the two reactions takes place? Please comment on how to interpret the result. (2 pts)

e) The previous calculation suggests a possible scheme for simulating stochastic chemical kinetics.  Given the probability distribution for the first reaction to occur, we next need a way to estimate which of the reactions it was that occurred.  What is the probability that sucrose is hydrolyzed before raffinose?  (3 pts)

9

Fall 2012 Systems Biology, Exam #1

## **7)  Equilibrium binding (12 points).**

Assume that molecules A and B can bind to each other reversibly with dissociation constant K.

a)  If [B]T = 2K, what is the fraction of A bound in the limit of low concentrations of A?  (3 pts)

b)  What is the fraction of A bound when [A]T = [B]T = 2K?   (3 pts)

c)  What is the equation describing the fraction of A bound as a function of [A]T in the limit of [A]T >> [B]T > K?  (4 pts)

d)  Plot approximately what the fraction of A bound looks like as a function of [A]T assuming that [B]T = 2K.  (2 pts)

10

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 7.32/7.81J/8.591J: Systems Biology](01-7-32-7-81j-8-591j-systems-biology.md) · [Up: contents](index.md)
