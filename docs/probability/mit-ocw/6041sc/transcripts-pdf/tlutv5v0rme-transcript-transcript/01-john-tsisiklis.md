---
title: JOHN TSISIKLIS
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/transcripts-pdf/tlutv5v0rme-transcript-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# JOHN TSISIKLIS

**Source:** `transcripts-pdf/tlutv5v0rme-transcript-transcript.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

So here's the agenda for today. We're going to do a very quick review. And then we're going to introduce some very important concepts. The idea is that all information is-- Information is always partial. And the question is what do we do to probabilities if we have some partial information about the random experiments. We're going to introduce the important concept of conditional probability. And then we will see three very useful ways in which it is used. And these ways basically correspond to divide and conquer methods for breaking up problems into simpler pieces. And also one more fundamental tool which allows us to use conditional probabilities to do inference, that is, if we get a little bit of information about some phenomenon, what can we infer about the things that we have not seen?

So our quick review. In setting up a model of a random experiment, the first thing to do is to come up with a list of all the possible outcomes of the experiment. So that list is what we call the sample space. It's a set. And the elements of the sample space are all the possible outcomes. Those possible outcomes must be distinguishable from each other. They're mutually exclusive. Either one happens or the other happens, but not both. And they are collectively exhaustive, that is no matter what the outcome of the experiment is going to be an element of the sample space.

And then we discussed last time that there's also an element of art in how to choose your sample space, depending on how much detail you want to capture. This is usually the easy part. Then the more interesting part is to assign probabilities to our model, that is to make some statements about what we believe to be likely and what we believe to be unlikely. The way we do that is by assigning probabilities to subsets of the sample space. So as we have our sample space here, we may have a subset A. And we assign a number to that subset P(A), which is the probability that this event happens. Or this is the probability that when we do the experiment and we get an outcome it's the probability that the outcome happens to fall inside that event.

We have certain rules that probabilities should satisfy. They're non-negative. The probability of the overall sample space is equal to one, which expresses the fact that we're are certain, no matter what, the outcome is going to be an element of the sample space. Well, if we set the top right so that it exhausts all possibilities, this should be the case.

And then there's another interesting property of probabilities that says that, if we have two events or two subsets that are disjoint, and we're interested in the probability, that one or the other happens, that is the outcome belongs to A or belongs to B. For disjoint events the total probability of these two, taken together, is just the sum of their individual probabilities. So probabilities behave like masses. The mass of the object consisting of A and B is the sum of the masses of these two objects. Or you can think of probabilities as areas. They have, again, the same property. The area of A together with B is the area of A plus the area B.

But as we discussed at the end of last lecture, it's useful to have in our hands a more general version of this additivity property, which says the following, if we take a sequence of sets-- A1, A2, A3, A4, and so on. And we put all of those sets together. It's an infinite sequence. And we ask for the probability that the outcome falls somewhere in this infinite union, that is we are asking for the probability that the outcome belongs to one of these sets, and assuming that the sets are disjoint, we can again find the probability for the overall set by adding up the probabilities of the individual sets.

So this is a nice and simple property. But it's a little more subtle than you might think. And let's see what's going on by considering the following example. We had an example last time where we take our sample space to be the unit square. And we said let's consider a probability law that says that the probability of a subset is just the area of that subset. So let's consider this probability law. OK.

Now the unit square is the set --let me just draw it this way-- the unit square is the union of one element set consisting all of the points. So the unit square is made up by the union of the various points inside the square. So union over all x's and y's. OK? So the square is made up out of all the points that this contains.

And now let's do a calculation. One is the probability of our overall sample space, which is the unit square. Now the unit square is the union of these things, which, according to our additivity axiom, is the sum of the probabilities of all of these one element sets. Now what is the probability of a one element set? What is the probability of this one element set? What's the probability that our outcome is exactly that particular point? Well, it's the area of that set, which is zero. So it's just the sum of zeros. And by any reasonable definition the sum of zeros is zero. So we just proved that one is equal to zero.

OK. Either probability theory is dead or there is some mistake in the derivation that I did. OK, the mistake is quite subtle and it comes at this step. We're sort of applied the additivity axiom by saying that the unit square is the union of all those sets. Can we really apply our additivity axiom. Here's the catch. The additivity axiom applies to the case where we have a sequence of disjoint events and we take their union. Is this a sequence of sets? Can you make up the whole unit square by taking a sequence of elements inside it and cover the whole unit square? Well if you try, if you start looking at the sequence of one element points, that sequence will never be able to exhaust the whole unit square.

So there's a deeper reason behind that. And the reason is that infinite sets are not all of the same size. The integers are an infinite set. And you can arrange the integers in a sequence. But the continuous set like the units square is a bigger set. It's so-called uncountable. It has more elements than any sequence could have. So this union here is not of this kind, where we would have a sequence of events. It's a different kind of union. It's a Union that involves a union of many, many more sets. So the countable additivity axiom does not apply in this case. Because, we're not dealing with a sequence of sets. And so this is the incorrect step.

So at some level you might think that this is puzzling and awfully confusing. On the other hand, if you think about areas of the way you're used to them from calculus, there's nothing mysterious about it. Every point on the unit square has zero area. When you put all the points together, they make up something that has finite area. So there shouldn't be any mystery behind it.

Now, one interesting thing that this discussion tells us, especially the fact that the single elements set has zero area, is the following-- Individual points have zero probability. After you do the experiment and you observe the outcome, it's going to be an individual point. So what happened in that experiment is something that initially you thought had zero probability of occurring. So if you happen to get some particular numbers and you say, "Well, in the beginning, what did I think about those specific numbers? I thought they had zero probability. But yet those particular numbers did occur."

So one moral from this is that zero probability does not mean impossible. It just means extremely, extremely unlikely by itself. So zero probability things do happen. In such continuous models, actually zero probability outcomes are everything that happens. And the bumper sticker version of this is to always expect the unexpected. Yes?

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
