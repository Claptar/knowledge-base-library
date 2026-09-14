---
title: Lecture 37 — shuffling
source: https://www.stat.berkeley.edu/~aldous/150/lecture_37_shuffling.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_37_shuffling.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 37 — shuffling

**Source:** [`lecture_37_shuffling.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_37_shuffling.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 37: A model for card shuffling


David Aldous

October 29, 2014


The usual scheme is called a **riffle shuffle** . [demo]


<!-- Start of picture text -->
a α<br>b a<br>c β<br>d γ<br>α δ<br>β b<br>γ c<br>δ ϵ<br>ϵ ζ<br>ζ d<br><!-- End of picture text -->

As with coin tossing, the point is that a human can’t do exactly the same physical action each time. Unlike coin tossing, we need an explicit probability model for what a human does.


The model we use is called the GSR (Gilbert-Shannon-Reeds) model, and there are 3 equivalent ways to describe the model.

_When dividing the deck, suppose a Binomial_ (52 _,_ 1 _/_ 2) _number of cards go to the left hand. And suppose that at each stage, the chance that the next drop is from the left or right hand is proportional to the number of cards remaining in that hand._

Roughly speaking, this models a “quite good” card shuffler. This description is equivalent to

_all possible riffle shuffles are equally likely._

The question we study is

**How many shuffles are needed for the deck to become “completely random”?**


[board] connection with Markov chain theory – STAT 150.

For the GSR model we can give an analysis which doesn’t depend on any general theory.


We can record a particular shuffle as a sequence of 0s and 1s, in this case 1011100110


<!-- Start of picture text -->
0 1<br>0 0<br>0 1<br>0 1<br>1 1<br>1 0<br>1 0<br>1 1<br>1 1<br>1 0<br><!-- End of picture text -->

In the GSR model, every possible sequence of 0s and 1s is equally likely. So we can imagine (hypothetically, as math) a **reversed shuffle** in which we create IID random 0s and 1s as in the right diagram, and then get to the left diagram by pulling out the 0-cards (in order) and placing the pile of 0s on top of the remaining pile of 1s.


# 4 “shuffles of a 5-card deck


<!-- Start of picture text -->
1001 0100 0100 1001 0010<br>@� �� J� �� @� ��<br>01001011 @@� � 00101001 �@ �� 10011101 J� � 00101011 @@� � 01001001<br>0010 HHH� 1011 �HHH�@@ � 0010 @���@@ � JJ 0100 HHH� 1011<br>1101 1101 1011 1101 1101<br><!-- End of picture text -->

Left-to-right represents 4 “radix sort” steps; right-to-left represents 4 riffle shuffles.

Reading left-to-right, if we start with cards named ABCDE and use random bits, the 4 “radix sort” steps get us to configuration DBACE. _conditional on all 5 of the 4-bit numbers being different, the right hand configuration in uniform random on all orderings of the deck._ But this works the same way right-to-left. We can implement the 4 riffle shuffles by using random bits which define a random integer: then _conditional on all these 5 integers being different, the 4 riffle shuffles get the deck into uniform random order._


Consider _k_ shuffles of an _n_ -card deck. We need to calculate P( _n k_ -bit numbers **not** all different) _._

But this is just the birthday problem with 2<sup>_k_</sup> days, and the probability


when this is small. Fixing a large _n_ , this becomes small when _k ≈_ 2 log2 _n_ , so this is a sufficient number of shuffles to mix an _n_ -card deck.

Details of argument above in (undergrad-level) Aldous - Diaconis.


Bayer – Diaconis ( _Trailing the dovetail shuffle to its lair_ , 1992) gave a precise analysis (harder calculation by different method) for a 52-card deck;

number shuffles k 4 5 6 7 8 9 non-uniformity d(k) 1.000 0.924 0.614 0.334 0.167 0.085

Here _d_ ( _k_ ) is “variation distance from uniformity”. [board] This work has entered popular science as “7 shuffles are enough” – try a Google search.

See also the book _Magic Tricks, Card Shuffling and Dynamic Computer memories_ by S. Brent Morris.

---

[Up: contents](index.md)
