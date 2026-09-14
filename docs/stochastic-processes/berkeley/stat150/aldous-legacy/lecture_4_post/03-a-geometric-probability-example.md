---
title: A “geometric probability” example.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_4_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_4_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A “geometric probability” example.

**Source:** [`lecture_4_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_4_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Saying that a random point in the plane is **uniform** on a set _A_ is saying that the joint density function of its coordinates ( _X , Y_ ) is


Let’s do some calculations in the case where _A_ is the top half of the unit disc. In particular, we will calculate E _Y_ by first considering E( _Y |X_ ).

David Aldous Lecture 4


David Aldous Lecture 4


We can now calculate


David Aldous Lecture 4


**Example: Likelihood of your team winning, at halftime.**

Most team sports are decided by point difference – points scored by home team, minus points scored by visiting team. Write

_X_ 1 = point difference in first half

_X_ 2 = point difference in second half

so

- home team wins if _X_ 1 + _X_ 2 _>_ 0

- _•_ visiting team wins if _X_ 1 + _X_ 2 _<_ 0

- tie if _X_ 1 + _X_ 2 = 0.

- A reasonable probability model assumes

- (i) _X_ 1 and _X_ 2 are i.i.d. random variables.

If the teams are equally talented, then assume

- (ii) _X_ 1 has symmetric distribution, that is the same distribution as _−X_ 1. Finally, let me simplify the math by making an unrealistic assumption

(iii) the distribution of _X_ 1 is continuous.

David Aldous Lecture 4


So ties cannot happen, and by (ii) P(Home team wins) = 1 _/_ 2. This is the probability before the game starts. At half time we know the value of _X_ 1, so there is a conditional probability P(Home team wins _| X_ 1). This is different in different matches, so we can ask _What is the distribution of_ P(Home team wins _| X_ 1) _?_ First I show some data from baseball.

David Aldous Lecture 4


In this match the initial “price” (perceived probability of home team winning) was close to 50%, and halfway through the game it was about 64%. I have these “halfway through the game” numbers for 30 matches where the initial “price” was close to 50%

David Aldous Lecture 4


<!-- Start of picture text -->
proportion probability<br>of data<br>0 50 price 100<br><!-- End of picture text -->

**Figure.** Empirical distribution function for the baseball data, compared with the uniform distribution.

David Aldous Lecture 4


Write _F_ ( _x_ ) for the distribution function of each _Xi_ .

---

[← Conditional expectation as a random variable.](02-conditional-expectation-as-a-random-variable.md) · [Up: contents](index.md) · [and this says →](04-and-this-says.md)
