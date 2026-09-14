---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/d5nmra2hkg4-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/d5nmra2hkg4-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**From the previous slide, could you clarify what the letter R and the letter S are?**

**PROFESSOR: Yes, sorry about that. R would be the odd ratio-- so it's the ratio of the probability of generating that sequence under the foreground model-- the plus model, we're calling it-- divided by the probability under the background, or minus, model. And then, I think I pointed out last time that when you get products of probabilities, they tend to get very small. This can cause computational problems. And so if you just take the log, you convert it into a sum. And so we'll often use score, or S, for the log of the odds ratio. Sorry, should have marked that more clearly.**

**So Markov models can improve performance, when there is dependence, and when you have enough data to estimate the increased number of parameters. And it doesn't just have to be dependence on the previous base-- you can have a model where the probability of the next base depends on the two previous bases. That would be called a second-order Markov model, or in general, a K-order Markov model.**

**Sometimes, these dependencies actually occur in practice. With five-prime splice sites, it's a nice example, because there's probably a couple thousand of them in the human genome, and we know them very well, so you can make quite complex models and have enough data to train them. But in general, if you're thinking about modeling a transcription factor binding site, or something, often you might have dozens or, at best, hundreds of examples, typically. And so you might not have enough to train some of the larger model.**

4

**So how many parameters do you need to fit a K-order Markov model? So question first, yeah? AUDIENCE: [INAUDIBLE] If you're comparing the first-order Markov models with W M M, what is W M M? PROFESSOR: Weight matrix, or position-specific probability matrix. Just a model of independence between the two. Coming back to this case. So let's suppose you are thinking about making a K-order Markov model, because you do some statistical tasks and you find there's some dependence between sets of positions in your motif. How many parameters would there be? So if you have an independence model, or weight matrix or positionspecific probability matrix, there are four parameters at each position, the probabilities of the four bases. This will be only three free parameters, because the fourth one-- but let's just think about it as four, four parameters times the width of the motif. So if I now go to a first-order Markov model, now there's more parameters, because I have these conditional probabilities at each position. So how many parameters are there? For a first-order Markov? How many do I need to estimate? Yeah, Kevin?**

**AUDIENCE: I think it would be 16 at each position.**

**PROFESSOR: Yeah, 16 at each position, except the first position, which has four. OK, and what about a second-order Markov model, where you condition on the two previous positions? 64, right? Because you have two possible bases you're conditioning on, that's 16 possibilities times 4. And so in general, the formula is 4 to the k plus 1. This is really the issue-- if you have only 100 sequences, and you need to estimate 64 parameters at each position, you don't have enough data to estimate those. So you shouldn't use such a high order model.**

**All right, so let's think about this-- what could happen if you don't have enough data**

5

**to estimate parameters, and how can you get around that? So let's just take a very simple example. So suppose you were setting a new transcription factor. You had done some sort of pull-down assay, followed by, say, conventional sequencing, and identified 10 sequences that bind to that transcription factor.**

**And these are the 10 sequences, and you align them. You see there is sort of a pattern there-- there's usually an A at the first position, and usually a C at the second, and so forth. And so you consider making a weight matrix model. Then you tally up-- there's eight A's, one C, one G, and no T's at the first position. So how confident can you be that T is not compatible with binding of this transcription factor? Who thinks you can be very confident?**

**Most of you are shaking your head. So if you're not confident, why are you not confident? I think-- wait, were you shaking your head? What's the problem here? It's just too small a sample, right? Maybe T occurs rarely. So suppose that T occurs at a frequency of 10%, what's the probability of that in natural sequences? And we just have a random sample of those. What's the probability we wouldn't see any T's in a sample of size 10? Anyone have an idea? Anyone have a ballpark number on this? Yeah, Simona?**

**AUDIENCE: 0.9 to the 10th. PROFESSOR: 0.9 to the 10th, OK. And what is that? AUDIENCE: 0.9 is the probability that you grab one, and don't see a T, and then you do that 10 times. PROFESSOR: Yeah, exactly. In genera it's a binomial thing, but it works out to be 0.9 to the 10th. And that's roughly-- this is like a Poisson. There's a mean of 1, so it's roughly E to the minus 1, so about 35% chance that you don't see any T's. So we really shouldn't be confident. T probably doesn't have a frequency of 0.5, but it could easily have a frequency of 10% or even 5%, or even 15%. And you might have just not seen it. So you don't want to assign a probability 0 to T. But what value should you assign**

6

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [for something you haven't seen? Sally? →](03-for-something-you-haven-t-seen-sally.md)
