---
title: '[INTERPOSING VOICES]'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kun6rj21hno-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [INTERPOSING VOICES]

**Source:** `recordings/kun6rj21hno-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: If they were uniform. Yeah. So did everyone get that? So the maximum occurs if fx i and j-- they're both uniform, so they're a quarter for every base at both positions. That's the maximum entropy in the background distribution.**

19

**But then if fx y ij equals 1/4, for example, x equals y-- or in our case, we're not interested in that. We're interested in x equals complement of y. C of y is going to be the complement of y. And 0 otherwise for x not equal complement of y.**

**OK, so for example, if we have only the dinucleotides AT, CG, GC, and TA occur, and each of them occurs with a frequency of 1/4, then you'll have four terms in the sum because, remember, the 0 log 0 is 0. So you'll have four terms in the sum, and each of them will look like 1/4 log 1/4 over a 1/4 times 1/4.**

**And so this will be 4, so log 2 of 4 4 is 2. And so you have four terms that are each 1/4 times 2. And so you'll get 2.**

**Well, this is not a sum. These are the four terms. These are the individual nonzero terms in that sum. Does that make sense? Everyone get this?**

**So that's why this is a useful measure of co-variation. If what's in one column really strongly influences what's in the other column, and there's a lot of variation in the two columns, and so you can really see that co-variation well, then mutual information is maximized. And that's basically what we just said, is written down here.**

**So it's maximal. They don't have to be complementary. It would achieve this maximum of 2 if they are complementary, but it would be also if they had some other very specific relationship between the nucleotides. So if you're going to use this, the way you would use it is take your multiple alignment, calculate the mutual information of each pair of columns-- so you actually have to make a table, i versus j, all possible pairs of columns-- and then you're going to look for the really high values.**

**And then when you find those high values, when you look at what actual bases are tending to occur together, you'll want to see that they're bases that are complementary to one another. And another thing that you'd want to see is you'd want to see that consecutive positions in one part of the alignment are co-varying with consecutive positions in another part of the alignment in the right way, in this**

20

**sort of inverse complementary way that RNA likes to pair.**

**Does that make sense? So in a sort of nested way in your multiple alignment, if you saw that this one co-varied with that, and then you also saw that the next base covaried with the base right before this one, and this one co-varies with that one, that starts to look like a stem. It's much more likely that you have a three-base stem than that you just have some isolated base pair out in the middle of nowhere. It turns out it takes a few bases to make a good thermodynamically stable stem, and so you want to look for blocks of these things.**

**And so this works pretty well. Yeah, actually, one point I want to make first is that mutual information is nice because it's kind of a useful concept and it also relates to some of the entropy and relative entropy that we've been talking about in the course before. But it's not the only statistic that would work in practice. You can use any measure of basically non-independence between distributions. A chi square statistic would probably work equally well in practice.**

**And so here is a multiple alignment of a bunch of sequences. And what I've done is put boxes around columns that have significant**

**mutual information with other sets of columns. So for example, this set of columns here at the left-- the far left-- has significant mutual information with the ones at the far right. And these ones, these four positions co-vary with these four, and so forth. So can you tell, based on looking at this pattern of co-variation, what the structure is going to be?**

**OK, let's say we start up here. The first is going to pair with the last, with something at the end. Then we're going to have something here in the middle that pairs with something else nearby. Then we have something here that pairs with something else nearby, then we have another like that.**

**Does that make sense? So that there's these three pairs of columns in the middle-these two, these two, and these two-- and then they're surrounded by this thing, the first pairing with the last. And so it's a clover leaf, so that's tRNA. Yeah?**

21

|**AUDIENCE:**|**So with that previous slide, this table here, you could create a co-variation matrix.**<br>**How would that-- or, and it could be--**|
|---|---|
|**PROFESSOR:**|**How does that co-variations matrix-- how do you convert it to this representations?**|
|**AUDIENCE:**|**I'm just wondering how this would go up. Like let's say you took the co-variation**<br>**matrix--**|
|**PROFESSOR:**|**Oh, what would it look like?**|
|**AUDIENCE:**|**--and visualized it as a heat map--**|
|**PROFESSOR:**|**In the co-variation matrix.**|
|**AUDIENCE:**|**Yeah. What would it look like in this particular example?**|
|**PROFESSOR:**|**Yeah, that's a good question. OK, let's do that. I haven't thought about that before,**<br>**so you'll have to help me on this. So here's the beginning.**|
||**We're going to write the sequence from 1 to n in both dimensions. And so here's the**<br>**beginning, and it co-varies with the end. So this first would have a co-variation with**<br>**the last, and then the second would co-vary with the second to last, and so forth. So**<br>**you get a little diagonal down here. That's this top stem here.**|
||**And then what about the second stem? So then you have something down here**<br>**that's going to co-vary with something kind of near by it. So block two is going to co-**<br>**vary with block three. And again, it's going to be this inverse complementary kind of**<br>**thing like that.**|
||**It's symmetrical, so you get this with that. But you only have to do one half, so you**<br>**can just do this upper half here. So you get that. So it would look something like**<br>**that.**|
|**AUDIENCE:**|**So with the diagonal line orthogonal to the diagonal of the matrix--**|
|**PROFESSOR:**|**Yeah, that's because they're inverse complementary.**|


22

**AUDIENCE: OK. PROFESSOR: That make sense? Good question. But we'll see an example like that later actually, as it turns out. All right, so here's my question for you. You're setting this non-coding RNA. It has some length. You have some number of sequences. They might have some structure. Is this method going to work for you, or is it not? What is required for it to work? For example, would I want to isolate this gene-- this non-coding RNA gene-- just from primates, from like human, gorilla, chimp, orangutan, and do that alignment? Or would I want to go further? Would I want to go back to the rodents and dog, horse-- how far do you want to go? Yeah, question. AUDIENCE: I think we a need a very strong sequence alignment for this, so we cannot go very far, because if you don't have a high percentage homology, then you will see all sorts of false positives. PROFESSOR: Absolutely. So if you go too far, your alignment will suffer, and you need an alignment in order to identify the corresponding columns. So that puts an upper limit on how far you can go. But excellent point. Is there a lower limit? Do you want to go as close as possible, like this example I gave with human, chimp, orangutan? Or is that too close? Why is too close bad? Tim? AUDIENCE: Maybe if you're too close, then the sequence is having to [INAUDIBLE] to give you enough information [INAUDIBLE]. PROFESSOR: Yeah, exactly. They're all the same. Actually, you'll get 1 times 1 over 1 in that mutual information statistic, which log of that is going to be 0. There's zero mutual information if they're all the same.**

**So there has to be some variation, and the structure has to be conserved. That's**

23

**key. You have to assume that the structure is well conserved and you have to have a good alignment and there has to be some variation, a certain amount of variation.**

**Those are basically the three keys. Secondary structure has a more highly conserved sequence. Sufficient divergence so that you have these variations, and sufficient number of homologues you have to get good statistics, and not so far they your alignment is bad. Sorry about that. Sally?**

**AUDIENCE: It seems like another thing that we assume here is that you can project it onto a plane and it will lie flat. So if you have some very important, weird folding that allows you to, say, crisscross the rainbow thing.**

**PROFESSOR: Yeah, crisscross the rainbow. Yeah, very good question. So in the example of tRNA, if you were to do that arc diagram for tRNA, it would look like another big arc-- that's the first and last-- and then you have these three nested arcs. Nothing crisscrossing.**

**What if I saw-- [INAUDIBLE]-- two blocks of sequence that have a relationship like that? Is that OK? With this method, the co-variation, that's OK. There's no problem there. What does this structure look like?**

**So [INAUDIBLE] you have a stem, then you have a loop, and then a stem. So this is 1 pairs with 3. That's 1. That's 3.**

**Then you've got 2 up here, but 2 pairs with 4. So here's 4 over here, so 4 is going to have to come back up here and pair with 2. This is 2 over here.**

**So that is called a pseudoknot. It's not really a knot because this thing doesn't go through the loop, but it kind of behaves like a knot in some ways. And so do these actually occur in natural RNAs? Yes, Tim is nodding.**

**And are they important? Can you give me an example where they are important biologically?**

---

[← AUDIENCE: [INAUDIBLE]](02-audience-inaudible.md) · [Up: contents](index.md) · [AUDIENCE: [INAUDIBLE] →](04-audience-inaudible.md)
