---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/d5nmra2hkg4-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/d5nmra2hkg4-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Any questions from last time about Gibbs Sampling? No? So at the end, we introduced this concept of relative entropy. So I just wanted to briefly review this, and make sure it's clear to everyone.**

**So the relative entropy is a measure of distance between probability distributions-can be written different ways, often with this D p q notation. And as you'll see, it's the mean bit-score, if you're scoring a motif with a foreground model, pk, and a background model, qk it's the average log odd score under the motif model. And I asked you to show that under the special case where qk is 1 over 4 to the w, that is uniform background, that the relative entropy of the motif ends up being simply 2w minus 8.**

**Did anyone have a chance to do this? It's pretty simple-- has anyone done this? Can anyone show this? Want me to do it briefly? How many would like to actually see this derivation? It's very, very quick. Few people, OK. So I'll just do that really quick.**

**So summation Pk log Pk over qk equals-- so you rewrite it as a difference, the log of a quotient is the difference of the log. Of summation log Pk plus summation Pk log qk.**

**OK, and then the special case that we're dealing with here is that qk is equal to a quarter, if we're dealing with the simplest case of a one-base motif. And so you recognize that that's minus H of Pp, right? H of p is defined as minus that, so it's minus H p. And this here, that's just a quarter. Log 2 of a quarter is minus 2. You can take the minus 2 outside of the sum, so you're ending up with minus 2-- I'm sorry.**

1

**How come Sally didn't correct me? Usually she catches these things. So that's a minus there, right, because we're taking the difference. And so then we have a minus 2 that we're pulling out from this, and you're left with summation Pk. And summation Pk, it sums to 1. So that's just 1. And so this equals minus minus 2, or 2 minus H of p.**

**And there are many other results of this type that can be shown in information theory. Often there are some simple results you can get simply by using this by splitting it into different terms, and summing. So another result that I mentioned earlier, without showing, is that if you have a motif, say, of length 2, that the information content of that motif model can be broken into the information content of each position if your model is such that the positions are independent.**

**So you would have, in that case-- let's just take the entropy of a model on [? dinucleotides. ?] It that would be minus summation Pi Pj log Pi Pj, if you have a model where the two are independent, and this sum would be taken over both i and j. And so if you want to show that this is equal to-- I claim that this is equal to the i-Anyway, if you have different positions, in general-- this would be the more general term-- where you have two different compositions at the two positions for the motif. And then you can show that it's equal to basically the sum the entropies at the two positions.**

**OK, you do the same thing. You separate out the log of the sum, in terms of the sum of the logs, and then you do properties of summations until you get the answer. OK, so this is your homework, and obviously it won't be graded. But we'll check in next Thursday and see if anyone has questions with that.**

**So what is the use of relative entropy? the main use in bio-informatics is that it's a measure that takes into account non-uniform backgrounds. The standard definition of information basically works when the background is uniform, but falls apart when it's non-uniform. So if you have a very biased genome, like this one shown here which is 75% A T, then the information content using the standard method would be two bits of this motif, which is P C equals 1.**

2

**But then, that would predict, using the formula, that a motif occurs 2 to the information content-- once every 2 to the information content bases-- that would be 2 to the 2, which would be 4 bases, and that's clearly incorrect in this case. But the relative entropy, if you do it, there will be four terms, but three of them just have a 0. And then one of them has a 1, so it's 1 times log 1 over 1/8, in this case, and that's will be equal to 3. And so the relative entropy clearly gives you a more sensible version.**

**It's a good measure for non-uniform backgrounds. Questions about relative entropy?**

**All right, so then we said you can use a weight matrix, or a position-specific probability matrix, for a motif like this five-prime splice site motif, assuming independence between positions. But if that's not true, then a natural generalization would be an inhomogeneous Markov model. So now, we're going to say that the base at position k depends on the base at position k minus 1, but not on anything before that.**

**And so, the probability of generating a particular sequence, S1 to S9, is now given by this expression here, where you have for every base after the first, you have a conditional probability. This is the conditional probability of seeing the base, S2, at position minus 2, given that you saw S1 at position minus 3, and so forth. And again, you can take the log for convenience, if you like.**

**So I actually implemented both of these models. So just for thinking about it, if you want to implement this, you have parameters-- these conditional probability parameters-- and you estimate them as shown here. So remember, conditional probability of A given B is the joint probability divided by the probability of B. And so in this case, that would be the joint probability of seeing C A at minus 3, minus 2, divided by the probability of seeing C at minus 3. You could have the ratio of the frequencies, or, in this case, the counts, because the normalization constant will cancel. Is that clear?**

**So I actually implemented both the weight matrix model and a first-order Markov**

3

**model of five-prime splice sites, and scored some genomic sequence. And what you can see here, the units are in 1/10th-bit units, is that they both are partially successful in separating real five-prime splice sites-- shown in black from the background, shown in light bars-- but in both cases, it's not a perfect separation. There's some overlap here.**

**And if you zoom there, you can see that the Markov model is a little bit better. It has a tighter tail on the left. So it's generally separating the true from the decoys a little bit better. Not dramatically better, but slightly better. Yes, question?**

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
