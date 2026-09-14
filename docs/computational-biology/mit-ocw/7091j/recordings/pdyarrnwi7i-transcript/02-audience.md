---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/pdyarrnwi7i-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/pdyarrnwi7i-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**Well, because they can form [INAUDIBLE].**

**OK. Yeah. So maybe you don't put your tryptophans and your cysteines into your protein by chance, or you only put them when you want them, when there's enough space for a tryptophan. And when you substitute something smaller, it leaves a gap. It leaves a 3D spatial gap. And so you don't want that. You don't get good packing.**

**When you have cysteines, they form disulfide bonds. If you change it to something that's non-cysteine, it can form that anymore. That could be disruptive to the overall fold. So those ones tend to be more conserved in protein sequence alignments, absolutely.**

**Whereas, for example, if you look at these hydrophobics, the MILV group down here, they all have positive scores relative to each other. And that says that, basically, most the time when those are used-- I mean, there are sometimes when it went really matters. But a lot of time, if you just want a transmembrane segment, you can often substitute any one of those at several positions and it'll work equally well as a transmembrane segment.**

**So these are not random at all. There's some patterns here. So let's go back to this algorithm. So now, if we're going to implement this recursion, so we fill on the top row and the left column, and then we need to fill in this first. I would argue the first interesting place in the matrix is right here.**

**And we consider adding a gap here. When you move vertically or horizontally, you're not adding a match or adding a match. So from this position, this is sort of the beginning point. It doesn't actually correspond to a particular position in the protein. We're going to add now the score for VV.**

**And we said that VV, you look it up in that PAM matrix, and it's plus 4. So we're going to add 4 there to 0. And so that's clearly bigger than minus 16, which is what you get from coming above or coming from the left. So you put in the 4.**

**And then you also, in addition to putting that 4 there, you also keep the arrow. So there's that red arrow. We remember where we came from in this algorithm.**

23

**Because someone said something about backtracking-- I think Chris-- so that's going to be relevant later.**

**So we basically get rid of those two dotted arrows and just keep that red arrow as well as the score. And then we fill in the next position here. And so to fill in this, now we're considering going to the second position in sequence one, but we're still only at the first position in sequence two. So if we match V to V, then we'd have to add, basically, a gap in one of the sequences. Basically it would be a gap in sequence two. And that's going to be minus 8.**

**So you take 4, and then plus minus 8, so it's negative 4. Or you could do minus 8 and then plus negative 2, if you want to start from a gap and then add a DV mismatch there, because minus 2 was the score for a DV mismatch. Or again, you can start from a gap and then add another gap.**

**OK, does that make sense? So what is the maximum going to be? Negative 4. And the arrow is going to be horizontal, because we got some bonus points for that VV match, and now it's carrying over. We're negative, but that's OK. We're going to just keep the maximum, whatever it is.**

**All right, so it's minus 4, and the horizontal arrow. And then here's the entire matrix filled out. And you'll have a chance to do this for yourself on problem set one. And I've also filled in arrows. I haven't filled in all the arrows, because it gets kind of cluttered. But all the relevant arrows here are filled in, as well as some irrelevant arrows.**

**And so then, once I fill this in, what do I do with this information? How do I get an actual alignment out of this matrix? Any ideas? Yeah, what's your name? AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah, so what he said is start at the bottom right corner and go backwards following the red arrows in reverse. Is that right? So why the bottom right corner? What's special about that?**

24

**AUDIENCE: [INAUDIBLE]. PROFESSOR: Yeah. It's a score of the optimal alignment of the entire sequence one against the entire sequence two. So that's the answer. That's what we define as the optimal global alignment. And then you want to know how you got there. And so how did we get there? So the fact that there's this red arrow here, what does that red arrow correspond to specifically? AUDIENCE: [INAUDIBLE]. PROFESSOR: Right. In this particular case, for this particular red arrow, remember the diagonals are matches. So what match is that? AUDIENCE: [INAUDIBLE]. PROFESSOR: Yeah, that's a Y to Y match, right? Can everyone see that? We added Y to Y, which was plus 10, to whatever this 13 was and got 23. OK, so now we go back to here. And then how do we get here? We came from up here by going this diagonal arrow. What is that? What match was that? That's a cysteine-cysteine match. And then how do we get to this 1? We came vertically. And so what does that mean? AUDIENCE: [INAUDIBLE]. PROFESSOR: We inserted a gap, in which sequence? The first one. The second one? What do people think? Moving down. AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah, the top one. And so that got us to here. Here's a match, plus 2 for having a serine-serine match. Here's a plus 3 for having a D to E mismatch. But remember, that's those are chemically similar, so they get a positive score. And then this is the V to V.**

**So can you see? I think I have the optimal alignment written somewhere here,**

25

**hopefully, there. That's called the trace back. And then that is the alignment.**

**OK, we align the Y to the Y, the C to the C. Then we have basically a gap in this top sequence-- that's that purple dash there-- that's corresponding to that L. And you can see why we wanted to put that gap in there, because we want these S's to match, and we want the C's to match. And the only way to connect those is to have a gap in the purple.**

**And the purple was shorter than the green sequence anyway, so we kind of knew that there was going to be a gap somewhere. And good. And that's the optimal alignment. So that's just some philosophy on Needlemen-Wunsch alignments.**

**So what is semi-global alignment? You don't see that that commonly. It's not that big a deal. I don't want to spend too much time on it. But it is actually reasonable a lot of times that, let's say you have a protein that has a particular enzymatic activity, and you may find that the whole, the bulk of the protein is well conserved across species.**

**But then at the N and C termini, there's a little bit of flutter. You can add a few residues or delete a few residues, and not much matters at the N and C termini. Or it may matter not for the structure but for, you know, you're adding a single peptide so it'll be secreted, or you're adding some localization signal. You're adding some little thing that isn't necessarily conserved.**

**And so a semi-global alignment, where you use the same algorithm, except that you initialize the edges of the dynamic programming matrix to 0, instead of the minus 8, minus 16 whole gap, and go to 0. So we're not going to penalize for gaps of the edges.**

**And then, instead of requiring the trace back to begin at the bottom right, Smn, you allow it to begin at the highest score in the bottom row or the rightmost column. And when you do the trace back as before, these two changes basically find the optimal global alignment but allowing arbitrary numbers of gaps at the ends and just finding the core match.**

26

**It has to go basically to the end of one or the other sequences, but then you can have other residues hanging off the end on the other sequence, if you want, with no penalty. And this sometimes will give a better answer, so it's worth knowing about. And it's quite easy to implement.**

**Now what about gapped local alignments? So what if you have two proteins? Do you remember those two proteins where we had the two diagonal? I guess they were diagonal lines. How where they? Something like that. Anyway, diagonal lines like that.**

**So where in this protein on the vertical, there is a sequence here that matches two segments of the horizontal protein. So for those two, you don't want to do this global alignment. It'll get confused. It doesn't know whether to match this guy to this or this other one to the sequence. So you want to use a local alignment. So how do we modify this Needleman-Wunsch algorithm to do local alignment? Any ideas? It's not super hard. Yeah, go ahead.**

**AUDIENCE: If the score is going to go negative, instead of putting a negative score, you just put 0, and you start from where you get the highest total score, rather than the last column or last row. Start your traceback from the highest score.**

**PROFESSOR: So whenever you're going negative, you reset to 0. Now what does that remind you of? That's the same trick we did write previously with ungapped local alignment. So you reset to 0. And that's as a no penalty, because if you're going negative, it's better just to throw that stuff away and start over. We can do that because we're doing local alignment. We don't have to align the whole thing. So that's allowed.**

**And then, rather than going to the bottom right corner, you can be anywhere in the matrix. You look for that highest score and then do the traceback. That's exactly right. So it's not that different.**

**There are a few constraints, though, now on the scoring system. So if you think about the Needleman-Wunsch algorithm, we could actually use a matrix that had all positive scores. You could take the PAM250 matrix. And let's say the most negative**

27

**score there is, I don't know, like minus 10 or something, and you could just add 10, or even add 20 to all those score. So they're all positive now. And you could still run that algorithm. And it would still produce more or less sensible results.**

**I mean, they t wouldn't be as good as the real PAM250, but you would still get a coherent alignment out of the other end. But that is no longer true when you talk about the Smith-Waterman algorithm, for the same reason that an ungapped local alignment, we had to require that the expected score be negative, because you have to have this negative drift to find small regions that go in the positive.**

**So if you have this rule, this kind of permissive that says, whenever we go negative we can just reset to 0, then you have to have this negative drift in order for positive scoring stuff to be unusual. All right, so that's another constraint there. You have to have negative values for mismatches-- I mean, not all mismatches. But if you took two random residues in alignment, the average score has to be negative. I should probably rephrase that, but more or less.**

**And here's an example of Smith-Waterman. So you right zeroes down the left side and across the top. And that's because, remember, if you go negative, you reset to 0. So we're doing that.**

**And then you take the maximum of four things. So coming from the diagonal and adding the score of the match, that's the same as before. Coming from the left and adding a gap in one sequence, coming from above and adding a gap in the other sequence, or 0. This "or 0" business allows us to reset to 0 if we ever go negative.**

**And when you have a 0, you still keep track of these arrows. But when you have a 0, there's no arrow. You're starting it. You're starting the alignment right there. So that's Smith-Waterman.**

**It's helpful. I think on problem set one, you'll have some experience thinking about both Needleman-Wunsch and Smith-Waterman. They sort of behave a little bit differently, but they're highly related. So it's important to understand how they're similar, how they're different.**

28

**And what I want to focus on for the remainder of this lecture is just introducing the concept of amino acid similarity matrices. We saw that PAM matrix, but where does it come from? And what does it mean? And does it work well or not, and are there alternatives?**

**So we could use this identity matrix. But as we've heard, there are a number of reasons why that may not be optimal. For example, the cysteines, we should surely score them more, because they're often involved in disulfide bonds, and those have major structural effects on the protein and are likely to be conserved more than your average leucine or alanine or whatever.**

**So clearly, scoring system should favor matching identical or related amino acids, penalize poor matches and for gaps. And there's also an argument that can be made that it should have to do with how often one residue is substituted for another during evolution. So that commonly substituted thing should have either positive scores or less negative scores than rarely substituted things.**

**And perhaps not totally obvious, but it is if you think about it for a while, is that any scoring system that you dream up carries with it an implicit model of molecular evolution for how often things are going to be substituted for each other. So it's going to turn out that the score is roughly proportional to a [INAUDIBLE] score for the occurrence of that pair of residues, divided by how often it would occur by chance, something like that.**

**And so that if you assign positive scores to things, to certain pairs of residues, you're basically implying that those things will commonly interchange during evolution. And so if you want to have realistic, useful scores, it helps to think about what the implicit evolutionary model is and whether that is a realistic model for how proteins evolve.**

**So I'm going to come to Dayhoff. And so unlike later matrices, she had an explicit evolutionary model, like an actual mathematical model, for how proteins evolve. And the idea was that there are going to be alignments of some proteins. And keep in mind, this was in 1978. So the protein database probably had like 1,000 proteins in**

29

**it, or something. It was very, very small.**

**But there were some alignments that were obvious. If you see two protein segments of 50 residues long that are 85 identical, there's no way that occurred by chance. You don't even need to do statistics on that. So you're sure.**

**So she took these very high confidence protein sequence alignments, and she calculated the actual residue residue substitution frequencies, how often we have a valine in one sequence as a substitute for a leucine. And it's actually assumed it's symmetrical. Again, you don't know the direction. And calculated these substitution frequencies.**

**Basically estimated what she called a PAM1 one matrix, which is a matrix that implies 1% divergence between proteins. So there's, on average, only a 1% chance any given residue will change. And the real alignments had greater divergence than that. They had something like 15% divergence.**

**But you can look at those frequencies and reduce them by a factor of 15, and you'll get not exactly 15 but something like 15. And you'll get something where there's a 1% chance of substitution. And then once you have that model for what 1% sequence substitution looks like, turns out you can just represent that as a matrix and multiply it up to get a matrix that describes what 5% sequence substitution looks like, or 10% or 50% or 250%.**

**So that PAM250 matrix that we talked about before, that's a model for what 250% amino acid substitution looks like. How does that even make sense? How can you have more than 100%? Is anyone with me on this? Tim, yeah.**

**AUDIENCE: Because it can go back. So it's more likely, in some cases, that you revert rather than [INAUDIBLE].**

**PROFESSOR: Right. So a PAM10 matrix means, on average, 10% of the residues have changed. But a few of those residues might have actually-- so maybe about 90% won't have changed at all. Some will have changed once, but some might have even changed twice, even at 10%.**

30

**And when you get to 250%, on average, every residue has changed 2 and 1/2 times. But again, a few residues might have remained the same. And some residues that change-- for example, if you had an isoleucine that mutated to a valine, it might have actually changed back already in that time. So it basically accounts for all those sorts of things. And if you have commonly substituted residues, you get that type of evolution happening.**

**All right. So she took these protein sequence alignments-- it looks something like this-- and calculated these statistics. Again, I don't want to go through this in detail during lecture, because it's very well described in the text. But what I do want to do is introduce this concept of a Markov chain, because it's sort of what is underlying these Dayhoff matrices. So let's think about it.**

**We'll do more on this next time. But imagine that you were able to sequence the genomes of cartoon characters with some newly developed technology and you chose to analyze the complicated genetics of the Simpson lineage. I'm assuming you all know these people. This is Grandpa and Homer eating doughnut and his son, Bart.**

**So imagine this is Grandpa's genome at the apolipoprotein A locus. And a mutation occurred that he then passed on to Homer. So this mutation occurred in the germ line, passed on to Homer. And then when Homer passed on his genes to Bart, another mutation occurred here, changing this AT pair to a GC pair in Bart.**

**So this, I would argue, is a type of Markov chain. So what is a Markov chain? So it's just a stochastic process. So a stochastic process is a random process, is sort of the general meaning. But here we're going to be dealing with discrete stochastic processes, which is just a sequence of random variables.**

**So X1 here is a random variable that represents, for example, the genome of an individual, or it could represent the genotype, in this case, at a particular position, maybe whether it's an A, C, G, or T at one particular position in the genome. And now the index here-- one, two, three, and so forth-- is going to represent time.**

31

**So X1 might be the genotype in Grandpa Simpson at a particular position. And X2 might be the genotype of Homer Simpson. And X3 would be the genotype in the next generation, which would be Bart Simpson. And what a Markov chain is is it's a particular type of stochastic process that arises commonly in natural sciences, really, and other places all over the place.**

**So it's a good one to know that has what's called the Markov property. And that says that the probability that the next random variable, or the genotype at the next generation, if you will-- so Xn plus 1 equals some value, j, which could be any of the possible values, say any of the four bases, conditional on the values of X1 through Xn, that is the entire history of the process up to that time, is equal to the conditional probability that Xn plus 1 equals j given only that little xn equals some particular value.**

**So basically what it says that if I tell you what Homer's genotype was at this locus, and I tell you what Grandpa Simpson's genotype was at that locus, you can just ignore Grandpa Simpson's. That's irrelevant. It only matters what Homer's genotype was for the purpose of predicting Bart's genotype. Does that make sense?**

**So it really doesn't matter whether that base in Homer's genome was the same as it was in Grandpa Simpson's genome, or whether it was a mutation that's specific to Homer, because Homer is the one who passes on DNA to Bart. Does that make sense?**

**So you only look back one generation. It's a type of memoryless process, that you only remember the last generation. That's the only thing that's relevant. And so to understand Markov chains, it's very important that you all review your conditional probability.**

**So we're going to do a little bit more on Markov chains next time. P A given B, what does that mean? If you don't remember, look it up in the Probability and Statistics, because that's sort of essential to Markov chains.**

**So next time we're going to talk about comparative genomics, which will involve**

32

**some applications of some of the alignment methods that we've been talking about. And I may post some examples of interesting comparative genomic research papers, which are going to be optional reading. You may get a little more out of the lecture if you read them, but it's not essential.**

33

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md)
