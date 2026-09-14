---
title: protein has this? What can you predict about its function?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/1emonm7qau8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# protein has this? What can you predict about its function?

**Source:** `recordings/1emonm7qau8-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: Zinc finger. PROFESSOR: Zinc finger, right. So it's a motif commonly seen in genome binding transcription factors, and it coordinates to zinc. What about this one? Any guesses on what this motif is? This quite a short motif. Yeah? AUDIENCE: That's a phosphorylation. PROFESSOR: Phosphorylation site. Yeah. And how do you know that? AUDIENCE: The [INAUDIBLE] and the [INAUDIBLE] next to it means it's [INAUDIBLE]. PROFESSOR: OK, so you even know what kinase it is, yeah. Exactly. So that's sort of the view. So, serine, threonine, and tirocene are the residues that get phosphorylated. And so if you see a motif with a serine in the middle, it's a good chance it's a phosphorylation site. Here are some-- you can think of them as DNA sequence motifs, because they occur in genes, but they, of course, function at that RNA level. These are the motifs that occur at the boundaries of mammalian introns. So this first one is the prime splicing motif.**

**So these would be the bases that occur at the last three bases of the exon. The first two of the intron here, are almost always GT. And then you have this position that I mentioned here-- it's almost always A or G position.**

**And then some positions that are bias for A, bias for G, and then slightly biased for T. And that is what you see when you look at a whole bunch of five prime ends of mammalian introns-- they have this motif. So some will have better matches, or worse, to this particular pattern. And that's the average pattern that you see.**

**And it turns out that in this case, the recognition of that site is not by a protein, per se, but it's by a ribonucleoprotein complex. So there's actually an RNA called U1 snRNA that base pairs with the five prime splice site. And its sequence, or part of its**

6

**sequence, is perfectly complimentary to the consensus five prime splice site. So we can understand why five prime splice sites have this motif-- they're evolving to have a certain degree of complementarity to U1, and in order to get officially recognized by the splicing machinery.**

**Then at the three prime end of introns, you see this motif here. So here's the last base of the intron, a G, and then an A before it. Almost all introns end with AG. Then you have a pyrimidine ahead of it. Then you have basically an irrelevant position here at minus four, which is not strongly conserved. And then a stretch of residues that are usually, but not always, pyrimidines-- called the pyrimidine track.**

**And in this case, the recognition is actually by proteins rather than RNA. And there are two proteins. One called U2AF65 that binds the pyrimidine track, and one, U2AF35 that binds that last YAG motif. And then there's an upstream motif here, that's just upstream of the 3 prime splice site that is quite degenerate and hard to find, called the branch point motif.**

**OK, so, let's take an example. So the five prime splice site is a nice example of a motif, because you can uniquely align them, right? You can sequence DNA, sequence genomes, align the CDNA to the genome, that tells you exactly where the splice junctions are. And you can take the exons that have a 5 prime splice site, and align the sequences aligned to the exon/intron boundary and get a precise motif. And then you can tally up the frequencies of the bases, and make a table like this, which we would call a position-specific probability matrix.**

**And what you could then do to predict additional, say, five prime splice-site motifs in other genes-- for example, genes where you didn't get a good CDNA coverage, because let's say they're not expressed in the cells that you analyzed-- you could then make this odds ratio here. So here we have a candidate sequence.**

**So the motif is nine positions, often numbered minus 3 to minus 1, would be the exonic parts of this. And then plus 1 to plus 6 would be the first six bases of the intron. That's just the convention that's used. I'm sure it's going to drive the computer scientists crazy because we're not starting at 0, but that's usually what's**

7

**used in the literature.**

**And so we have a nine-based motif. And then we're going to calculate the probability of generating that particular sequence as given plus-- meaning given our foreground, or motif model-- as the product of the probability of generating the first base in sequence, S1, using the column probability in the minus 3 position.**

**So if the first base is AC, for example, that would be 0.4. And then the probability of generating the second base in the sequence using the next column, and so forth. If you made a vector for each position that had a 1 for the base that occurred at that position, and a 0 for the other bases, and then you just did the dot product of that with the matrix, you get this.**

**So, we multiply probabilities. So that is assuming independence between positions. And so that's a key assumption-- weight matrices assume that each position in the motif contributes independently to the overall strength of that motif. And that may or may not be true-- they don't assume that it's homogeneous, that is you have usually in a typical case, different probabilities in different columns, so it's inhomogeneous, but assumes independence.**

**And then you often want to use a background model. For example, if your genome composition is 25% of each of the nucleotides, you could just have a background probability that was equally likely for each of the four, and then calculate the probability, S given minus, of generating that particular [INAUDIBLE] under the background model, and take the ratio of those two.**

**And the advantage of that is that then you can find sequences that are-- that ratio, it could be 100 times more like a 5 prime splice site than like background-- or 1,000 times. Or you have some sort of scaling on it. Whereas, if you just take the raw probability, it's going to be something that's on the order of 1/4 to a 1/9. So some very, very small number that's a little hard to work with.**

**So when people talk about motifs, they often use language like exact, or precise, versus degenerate, strong versus weak, good versus lousy, depending on the**

8

**context, who's listening. So an example of these would be a restriction enzyme. You often say restriction enzymes have very precise sequence specificity, they only cut-echo R1 only cuts a GAA TTC. Whereas, a TATA binding protein is somewhat more degenerate. It'll bind to a range of things. So I use degenerate there, you could say it's a weaker motif.**

**You'll often-- if you want to try to make this precise, then the language of entropy information offers additional terminology, like high information content, low entropy, et cetera. So let's take a look at this as perhaps a more natural, or more precise way of describing what we mean, here.**

**So imagine you have a motif. We're going to do a motif of length one-- just keep the math super simple, but you'll see it easily generalizes. So you have probabilities of the four nucleotides that are Pk. And you have background probabilities, qk. And we're going to assume those are all uniform, they're all a quarter.**

**So then the statistical, or Shannon entropy of a probability distribution-- or vector of probabilities, if you will-- is defined here. So H of q, where q is a distribution or, in this case, vector, is defined as minus the summation of qk log qk, in general. And then if you wanted to be in units of bits, you'd use log base 2.**

**So how many people have seen this equation before? Like half, I'm going to go with. OK, good. So who can tell me why, first of all-- is this a positive quantity, negative quantity, non-negative, or what? Yeah, go ahead.**

**AUDIENCE: Log qk is always going to be negative. And so therefore you have to take the negative of the sum of all the negatives to get a positive number.**

**PROFESSOR: Right, so this, in general, is a non-negative quantity, because we have this minus sign here. We're taking logs of things that are between 0 and 1. So the logs are negative, right? OK. And then what would be the entropy if I say that the distribution q is this-- 0100, meaning, it's a motif that's 100% C? What is the entropy of that? What was your name?**

**AUDIENCE: William.**

9

**PROFESSOR: William.**

**AUDIENCE: So the entropy would be 0, because the vector is determined in respect of the known certainty. PROFESSOR: Right. And we do the math-- you'll get, for the C term, you'll have a sum. You'll have three terms that are 0 log 0-- it might crash your calculator, I guess. And then you'll have one term that is 1 log 1. And so 1 log 1, that's easy. That's 0, right? This, you could say, is undefined. But using L'Hospital's rule-- by continuity, x log x, you take the limit, as x gets small, is 0. So this is defined to be 0 in information theory. And this is always, always 0. So that comes out to be 0. So it's deterministic. So entropy is a measure of uncertainty, and so that makes sense-- if you know what the base is, there's no uncertainty, entropy is 0. So what about this vector-- 1/4, 1/4, 25% of each of the bases, what is H of q? Anyone? I'm going to make you show me why, so-- Anyone want to attempt this? Levi? AUDIENCE: I think it's 2. PROFESSOR: 2, OK. Can you explain?**

**AUDIENCE: Because the log of the 1/4's is going to be negative 2. And then you're multiplying that by 1/4, so you're getting 1/2 for each and adding it up equals 2. PROFESSOR: Right, in sum, there are going to be four terms that are 1/4 times log of a 1/4. This is minus 2, 1/4 times minus 2 is minus 1/2, 4 times minus 1/2 is minus 2, and then you change the sign, because there's this minus in front. So that equals 2. And what about this one? Anyone see that one? This is a coin flip, basically. All right? It's either A or G. [INAUDIBLE]. Anyone? Levi, want to do this one again? AUDIENCE: It's 1.**

**PROFESSOR: OK, and why?**

10

**AUDIENCE:**

**Because you have two terms of 0 log 0, which is 0. And two terms of 1/2 times the log of 1/2, which is just negative 1. So you have 2 halves.**

**PROFESSOR: Yeah. So two terms like that. And then there's going to be two terms that are something that turns out to be 0-- 0 log 0. And then there's a minus in front. So that will be 1.**

**So a coin flip has one bit of information. So that's basically what we mean. If you have a fair coin and you don't know the outcome, we're going to call that one bit. And so a base that could be any of the four equally likely has twice as much uncertainty.**

**All right, and this is related to the Boltzmann entropy that you may be familiar with from statistical mechanics, which is the log of the number of states, in that if you have N states, and they're all equally likely, then it turns out that the Shannon entropy turns out to be log of the number states. We saw that here-- four states, equally likely, comes out to be log of 4 or 2. And that's true in general. All right, so you can think of this as a generalization of Boltzmann entropy, if you want to.**

**OK, so why did he call it entropy? So it turns out that Shannon, who was developing this in the late '40s, as developing a theory of communication, scratched his head a little bit. And he talked to his friend, John von Neumann-- none other than him, involved in inventing computers-- and he says, "My concern was what to call it. I thought of calling it information. But the word was overly used."**

**OK, so back in 1949, information was already overused. "And and so I decided to call it uncertainty." And then he discussed it with John von Neumann, and he had a better idea. He said, "You should call it entropy. In the first place, your certainly function has already been used in statistical mechanics under that name," so it already has a name. "And the second place, and more important, nobody knows what entropy really is, so in a debate, you always have the advantage."**

**So keep that in mind. After you've taken this class, just start throwing it around and you will win a lot of debates. So how is information related to entropy? So the way**

11

**we're going to define it here, which is how it's often defined, is information is reduction in uncertainty.**

**So, if I'm dealing with an unknown DNA sequence, the lambda phage genome, and it has 25% of each base, if you tell me, I'm going to send you two bases, I have no idea. They could be any pair of bases. My uncertainty is 2 bits per base, or 4 bits before you tell me anything. If you then tell me, it's the TA motif, which is always T followed by A, then now my uncertainty is 0, so the amount of information that you just gave me is 4 bits. You reduced my uncertainty from 4 bits to 0.**

**So we define the information at a particular position as the entropy before-- before meaning the background, the background a sort of your null hypothesis-- minus the entropy after-- so after you've told me that this is an instance of that motif, and it has a particular model. So, in this case, you can see the entropy is going to be entropy before. This is just H of q right here, this term. And then minus this term, which is H of p.**

**So, if it's uniform, we said H of q is 2 bits per position. And so, so the information content of the motif is just 2 minus the entropy of that motif model. In general, it turns out if the positions in the motif are independent, then the information content of the motif is 2w minus H of motif, where w is it width of the motif.**

**So for example, the entropy of the motif of-- we said the entropy of this is 2 bits, right? Therefore, the information content is what? If this is our-- let's say this is a P. This is our routine. Are you starting to generate? What is its information content? AUDIENCE: 0?**

**PROFESSOR: 0. Why is it 0? Yeah, back row.**

**AUDIENCE: Because the information content of that is 0, and then the information content of the known hypothesis, so to say, is 0. Sorry, both of them are 2. So 2 minus 2 is 0. PROFESSOR: The entropy of the background is 2, and the entropy if this is also 2. So 2 minus 2 is 0. And what about this? Let's say this was our motif, it's a motif that's either A or G.**

12

**We said the entropy of this is 1 bit, so what is the information content of this motif?**

**AUDIENCE: 1. PROFESSOR: 1, and why is it 1?**

**AUDIENCE: Background is 2, and entropy here is 1.**

**PROFESSOR: Background is 2, entropy is 1. OK? And what about if I tell you it's the echo R1 restriction enzyme? So it's GAA TTC, a six-base motif precise-- it has to be those bases? What is the information content of that motif? In the back?**

**AUDIENCE: It's 12.**

**PROFESSOR: 12-- 12 what? AUDIENCE: 12 bits.**

**PROFESSOR: 12 bits, and why is that?**

**AUDIENCE: Because the background is 2 times 6. So 6 bases, and 2 bits for each. And you have all the bases are determined at the specific [INAUDIBLE] enzyme site. So the entropy of that is 0, since 12 minus 0 is 12.**

**PROFESSOR: Right, the entropy of that motif is 0. You imagine 4,096 possible six-mers. One of them has probably 1. All the others have 0. You're going to have that big sum. It's going to come out to be 0, OK? Why is this useful at all, or is it?**

**One of the reasons why it's useful-- sorry, that's on a later slide. Well, just hang with me, and it will be clear why it's useful in a few slides. But for now, we have a description of information content.**

**So the echo R1 site has 12 bits of information, a completely random position has 0, and a short four-cutter restriction enzyme would have 2 times 4, 8 bits of information, right, and an eight-cutter. So you can see as the restriction enzyme gets longer, more information content.**

13

**So let's talk about the motif finding problem, and then we'll return to the usefulness of information content. So can everyone see the motif that's present in all these sequences?**

**If anyone can't, please let me know. You probably can't. Now, what now? These are the same sequences, but I've aligned them. Can anyone see a motif?**

**PROFESSOR: GGG GGG.**

**PROFESSOR: Yeah, I heard some G's. Right. so there's this motif that's over here. It's pretty weak, and pretty degenerate. There's definitely some exceptions, but you can definitely see that a lot of the sequences have at least GGC, possibly an A after that.**

**Right, so this is the problem we're dealing with. You have a bunch of promoters, and the transcription factor that binds may be fairly degenerate, maybe because it likes to bind cooperatively with several of its buddies, and so it doesn't have to have a very strong instance of the motif present. And so, it can be quite difficult to find. So that's why there's a real bio-informatics challenge.**

**Motif finding is not done by lining up sequences by hand, and drawing boxes-although that's how the first motif was found, the TATA box. That's why it's called the TATA box, because someone just drew a box in a sequence alignment. But these days, you need a computer to find-- most motifs require some sort of algorithm to find. Like I said, it's essentially a local multiple alignment problem. You want multiple alignment, but it doesn't have to be global. It just can be local, it can be just over a sub-region.**

**There are basically at least three different sort of general approaches to the problem of motif finding. One approach is the so-called enumerative, or dictionary, approach. And so in this approach, you say, well, we're looking for a motif of length 6 because this is a leucine zipper transcription factor that we're modeling, and they usually have binding sites around 6, so we're going to guess 6. And we're going to enumerate all the six-mers, there's 4,096 six-mers.**

**We're going to count up their occurrences in a set of promoters that, for example,**

14

**are turned on when you over-express this factor, and look at those frequencies divided by the frequencies of those six-mers in some background set-- either random sequences, or promoters that didn't turn on. Something like that. You have two classes, and you look for statistical enrichment.**

**This approach, this is fine. There's nothing wrong with this approach. People use it all the time. One of the downsides, though, is that you're doing a lot of statistical tests. You're essentially testing each six-mer-- you're doing 4,096 statistical tests. So you have to adjust the statistical significance for the number of tests that you do, and that can reduce your power. So that's one main drawback.**

**The other reason is that maybe you don't see-- maybe this protein binds a rather degenerate motif, and a precise six-mer is just too precise. None of them will occur often enough. You really have to have a degenerate motif that's C R Y G Y. That's really the motif that it binds to, and so you don't see it unless you use something more degenerate. So you can generalize this to use regular expressions, et cetera. And it's a reasonable approach.**

**Another approach that we'll talk about in a moment is probabilistic optimization, where you wander around the possible space of possible motifs until you find one that looks strong. And we'll talk about that.**

**And then they're deterministic versions of this, like me. We're going to focus today on this second one. Mostly because it's a little bit more mysterious and interesting as an algorithm. And it's also [INAUDIBLE].**

**So, if the motif landscape looked like this, where imagine all possible motifs, you've somehow come up with a 2D lattice of the possible motif sequences. And then the strength of that motif, or the degree to which that motif description corresponds to the 2 motif is represented by the height here. Then, there's basically one optimal motif, and the closer you get to that, the better fit it is. Then our problem is going to be relatively easy.**

**But it's also possible that it looks something like this. There's a lot of sort of decoy**

15

**motifs, or weaker motifs that are only slightly enriched in the sequence space. And so you can easily get tripped up, if you're wandering around randomly. We don't know a priori, and it's probably not as simple as the first example. And so that's one of the issues that motivates these stochastic algorithms.**

**So just to sort of put this in context-- the Gibbs motif sampler that we're going to be talking about is a Monte Carlo algorithm, so that just means it's an algorithm that basically does some random sampling somewhere in it, so that the outcome that you get isn't necessarily deterministic. Your run it at different times, and you'll actually get different outputs, which can be a little bit disconcerting and annoying at times. But it turns out to be useful in some cases.**

**There's also a special case of a Las Vegas algorithm, where it knows when it got be optimal answer. But in general, not. In general, you don't know for sure.**

**So Gibbs motif simpler is basically a model where you have a likelihood for generating a set of sequences, S. So imagine you have 40 sequences that are bacterial promoters, each of 40 bases long, let's say. That's your S. And so what you want to do, then, is consider a model that there is a particular instance of a motif you're trying to discover, at a particular position in each one of those sequences. Not necessarily the same position, just some position in each sequence.**

**And we're going to describe the composition of that motif by a weight matrix. OK, one of these matrices that's of width, W, and then has the four rows specifying the frequencies of the four nucleotides at that position. The setup here is that you want to calculate or think about the probability of S comma A, S is the actual sequences, and A is basically a vector that specifies the location of the motif instance in each of those 40 sequences.**

**You want to calculate that, conditional on capital theta-- which is our weight matrix. So that's going to be, in this case, I think I made a motif of length 8, and it's shown there in red. There's going to be a weight matrix of length 8. And then there's going to be some sort of background frequency vector that might be the background composition in the genome of E.coli DNA, for example.**

16

**And so then the probability of generating those sequences together with that particular locations is going to be proportional to this. Basically, use the little theta background vector for all the positions, except the specific positions that are inside the motif, starting at position AK here. And then you use the particular column of the weight matrix for those 8 positions, and then you go back to using the background probabilities. Question, yeah?**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
