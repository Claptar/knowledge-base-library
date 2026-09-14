---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/14m9mw-qmhg-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/14m9mw-qmhg-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Why don't we get started? So today we're going to talk about comparative genomics. And first, a brief review of what we did last time. So last time we talked about global alignment of protein sequences, including the Needleman-Wunsch and Smith-Waterman algorithms. And we talked about gap penalties a little bit and started to introduce the PAM series of matrices which are well described in the text.**

**So what I wanted to do is just briefly go over what I started to talk about at the end, about Markov models of evolution. Because they're relevant, not only for the PAM series, but also for some other topics in the course. A short unit on molecular evolution we're going to do today. And then they also introduce hidden Markov models that will come up later in the course.**

**So the example that we gave of a Markov model was DNA sequence evolution in successive generations where the observation here is that the base at a particular position at generation n+1 here depends on the base at that generation and the base at generation n. But conditional on knowing the base at generation n, you don't learn anything from knowing what that base was at generation n-1. That's the essence of the Markov properties. So here's the formal definition, as we saw before.**

**Any questions on this? And I asked you to review your conditional probability if it was rusty, because that's very relevant.**

**OK so in this example you might, if you had a random variable x that represented the genotype at a particular locus, let's say the apolipoprotein locus, and it had alleles A and a, then you might write something like the probability that Bart's genotype is a homozygous given his grandfather's genotype and his dad's genotype is equal to just the conditional probability given his father's genotype. So those are**

1

**the sorts of things that you can do with Markov chains**

**So when you're working with Markov chains matrices are extremely useful. So another thing that will be helpful in this part of the course and then again in Professor Fraenkel's part, where he's talking-- he'll use also some ideas from linear algebra-- is to review your basics of matrices and vector multiplication.**

**OK so, if you now make a model of molecular evolution where sn is-- so s is this variable that represents a particular base in the genome and is the generation. And then to describe the evolution of this base over time, we're going to imagine that its evolution is described by a Markov chain.**

**And a Markov chain can be described by, in this case, a 4 by 4 matrix, since there are four possible nucleotides at generation i, for example, and four possible at generation i plus one. And you simply need to specify what the conditional probability that the base will be, of any possible base, at the next generation, given what it is at the current generation.**

**So here's the matrix up here. And it describes, for example, the probability of going from a c to an a. So then in general you might know that that base is a g at the first generation. But in general you won't necessarily know what base it is if you're modeling events that may happen in the future. So the most general way of describing what's happening at that base is a vector of probabilities of the four possible bases-- so qa, qc, qg, qt, with those probabilities summing up to 1.**

**And so then it turns out that with this notation that the content of the vector at generation n plus 1 is equal to simply the vector at generation n multiplied on the right by the matrix, just using the standard vector matrix multiplication. So for example, if we have vectors with four things in them, and we have a 4 by 4 matrix, then to get this term here in this vector you multiply-- you basically take the dot product of this vector times this first column.**

**The vector times the first column will give you that entry. And this times this column will give you that entry in the vector, and so forth. And you can see that the way this**

2

**makes sense, the way the matrix is defined, that first column tells you the probability that you'll have an a at the next generation, conditional on each of the four bases at the previous generation. And so you just multiply by the probabilities of those four bases times the appropriate conditional probability here. And those are all the ways that you can be an a generation, n plus 1.**

**And so it's also true that if you want to go further in time, so from generation n to generation n plus k-- k is some integer-- then this just corresponds to sequential multiplication by the matrix k-- I'm sorry, by the matrix p. So qn plus 1 equals q times p. And then qn plus 2 will equal q-- I'm sorry. That's a really bad q, but-- qn plus 1 times p, which will equal q times p squared, where p squared means matrix multiplication, again using the standard rules of matrix multiplication that you can look up.**

**So one of the things you might think about here is what happens after a long time? If you start from some vector q-- for example, q is 0010. That is, it's 100% chance of g. What would happen if you run this matrix on that over a long period of time. And we'll come back to that question a little bit later.**

**So thinking about the Dayhoff matrices-- and again, I'm not going to go into detail here, because it's well described in the text. Dayhoff looked at these highly identical alignments, these 85% identical alignments, and calculated the mutability of each residue and these mutation probabilities for how often each residue changes into each other one and then scaled them so that on average the chance of mutating is 1% and then took these probabilities, these frequencies, of mutation m, a, b, divided by the frequency of the residue b, took the log, and then just multiplied by two just for scaling purposes, and came up with a-- and then rounded to the nearest integer, again for practical purposes.**

**And that's how she came up with her PAM 1 matrix. And then you can use matrix multiplication to derive all the successive PAM series. Just multiply the PAM1 matrix times itself to get the PAM2 and recalculate the scores.**

**So if you actually use PAM matrices in practice there are some issues. And these**

3

**are also well described in the text. And the fundamental problem seems to be that the way the proteins evolve over short periods of time and the way they evolve over long periods of time is somewhat different. And basically this model, this Markov model of evolution, is not quite right, that things don't-- what you see in a short periods of time-- it does not match long periods of time.**

**And why is that? A number of possible reasons. But keep in mind that in addition to proteins simply changing their amino acid sequence, other things can happen in evolution. You can have insertions and deletions that are not captured by this Markov model. And you can also have birth and death of proteins. A protein can evolve according to this model for millions of years. And then it can become unneeded, and just be lost, for example.**

**So real protein evolution is more complicated. And so about 20 years ago or so Henikoff and Henikoff decided to develop a new type of matrix. And the way they did it was to identify these things called blocks, which are regions of reasonably high similarity, but not as high as Dayhoff required.**

**So there were many more-- Dayhoff was working the '70s. They were working in the '90s. So there were many more proteins available. And they could identify, with confidence, basically a much larger data set, including more distantly related, but still confidently alignable, protein sequences. And they derived new parameters.**

**And in the end this matrix they came up with called BLOSUM62 seems to work well in a variety of contexts when comparing moderately distantly related proteins or quite distantly related proteins. If you're comparing very similar proteins it almost doesn't matter. Any reasonable matrix will probably give you the right answer. But when you're comparing the more distant ones, that's where it becomes challenging.**

**And so this is the BLOSUM62 matrix here. And you can see it's similar to the PAM matrices in that-- I think we showed PAM 250 last time-- in that you have a diagonal with all positive numbers. And it's also similar in that, for example, trytophan down here has a higher positive score than others. It's plus 9. And cysteine is also one of the higher ones. But those are less extreme.**

4

**And basically, maybe over short periods of evolutionary time, you don't change your cysteine. But over longer periods there is some rewiring of disulfide bonding, and so cysteines can change. Something like that may be going on.**

**So we've just talked about pairwise sequence alignments. But in practice you often have, especially these days you often have, many proteins though. So you want to align three or five or 10 different proteins together to find out which residues are most conserved, for example. And so basically the principles are similar to pairwise alignment.**

**But now you want to find alignments that bring the greatest number of single characters into register. So if you're aligning three proteins, you really want to have columns where all three are the same residue, or very similar residues. And you need to then define scoring systems, define gap penalties, and so forth.**

**This is also reasonably well described in the text. I just wanted to make one comment about the sort of computational complexity of multiple sequence alignment. So if you think about pairwise sequence alignment, say with NeedlemanWunsch or Smith-Waterman, with a sequence of length-- let's say you're aligning one protein of sequence length n to another of life n, what is the computational complexity of that calculation in using this big O notation that we've talked about? Let's just say standard gap penalties, linear gap penalties. Anyone? Or does it matter? Yeah, go ahead.**

**STUDENT: n squared.**

**PROFESSOR: It's n squared. So even though this has gaps, with local-- with ungapped it was also n squared, or n times n, So why is it that gaps don't make it worse? Or do they? Any thoughts on that?**

**STUDENT: You put a constant number of gaps in the sequence. So it's just stating the essence of the complexity should still be n squared.**

**PROFESSOR: You put a constant number of gaps? The-- I mean, yeah-- let's just hear a few**

5

---

[Up: contents](index.md) · [different comments. And then we'll try to summarize. Go ahead. →](02-different-comments-and-then-we-ll-try-to-summarize-go-ahead.md)
