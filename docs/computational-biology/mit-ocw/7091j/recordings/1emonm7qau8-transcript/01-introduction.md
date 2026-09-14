---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/1emonm7qau8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/1emonm7qau8-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=1EMonM7qAU8**

**NARRATOR: The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high-quality educational resources for free. To make a donation, or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: All right, we should get started. So it's good to be back. We'll be discussing DNA sequence motifs. Oh yeah, we were, if you're wondering, yes, the instructors were at the awards on Sunday. It was great. The pizza was delicious.**

**So today, we're going to be talking about DNA and protein sequence motifs, which are essentially the building blocks of regulatory information, in a sense. Before we get started, I wanted to just see if there are any questions about material that Professor Gifford covered from the past couple days? No guarantees I'll be able to answer them, but just general things related to transcriptome analysis, or PCA? Anything?**

**Hopefully, you all got the email that he sent out about, basically, what you're expected to get. So at the level of the document that's posted, that's sort of what we're expecting. So if you haven't had linear algebra, that should still be accessible- not necessarily all the derivations. Any questions about that?**

**OK, so as a reminder, team projects, your aims are due soon. We'll post a slightly-there's been a request for more detailed information on what we'd like in the aims, so we'll post something more detailed on the website this evening, and probably extend the deadline a day or two, just to give you a little bit more time on the aims. So after you submit your aims-- this is students who are taking the project component of the course-- then your team will be assigned to one of the three instructors as a mentor/advisor, and we will schedule a time to meet with you in the next week or two to discuss your aims, just to assess the feasibility of the project and so forth, before you launch into it.**

**All right-- any questions from past lectures? All right, today we're going to talk about**

1

**modeling and discovery of sequence motifs. We'll give an example of a particular algorithm that's used in motif finding called the Gibbs Sampling Algorithm.**

**It's not the only algorithm, it's not even necessarily the best algorithm. It's pretty good. It works in many cases. It's an early algorithm. But it's interesting to talk about because it illustrates the problem in general, and also it's an example of a stochastic algorithm-- an algorithm where what it does is determined at random, to some extent. And yet still often converges to a particular answer. So it's interesting from that point of view.**

**And we'll talk about a few other types of motif finding algorithms. And we'll do a little bit on statistical entropy and information content, which is a handy way of describing motifs. And talk a little bit about parameter estimation, as well, which is critical when you have a motif and you want to build a model of it to then discover additional instances of that motif.**

**So some reading for today-- I posted some nature biotechnology primers on motifs and motif discovery, which are pretty easy reading. The textbook, chapter 6, also has some good information on motifs, I encourage you to look at that. And I've also posted the original paper by Bailey and Elkin on the MEME algorithm, which is kind of related to the Gibbs Sampling Algorithm, but is used as expectation maximization. And so it's a really nice paper-- take a look at that.**

**And I'll also post the original Gibbs Sampler paper later today. And then on Tuesday, we're going to be talking about Markov and hidden Markov models. And so take a look at the primer on HMMs, as well as there is some information on HMMs in the text. It's not really a distinct section, it's kind of scattered throughout the text. So the best approach is to look in the index for HMMs, and read the relevant parts that you're interested in.**

**And if you really want to understand the mechanics of HMMs, and how to actually implement one in depth, then I strongly recommend this Rabiner tutorial on HMMs, which is posted. So everyone please, please read that. I will use the same notation, to the extent possible, as the Rabiner paper when talking about some of the**

2

**algorithms used in HMMs in lecture. So it should synergize well. So what is a sequence motifs? In general, it's a pattern that's common to a set of DNA, RNA, or protein sequences, that share a biological property. So for example, all of the binding sites of the Myc transcription factor-- there's probably a pattern that they share, and you call that the motif for Myc. Can you give some examples of where you might get DNA motifs? Or protein motifs? Anyone have another example of a type of motif that would be interesting? What about one that's defined on function? Yeah, go ahead. What's your name? AUDIENCE: Dan. [INAUDIBLE] PROFESSOR: Yeah. So each kinase typically has a certain sequence motif that determines which proteins it phosphorylate. Right. Other examples? Yeah, so in that case, you might determine it functionally. You might purify that protein, incubate it with a pool of peptides, and see what gets phosphorylated, for example. Yeah, in the back? AUDIENCE: I'm [INAUDIBLE], and promonocytes. PROFESSOR: What was the first one? AUDIENCE: Promonocytes? Oh, that one? Oh, that was my name. PROFESSOR: Yeah, OK. And as to promoter motifs, sir? Some examples? AUDIENCE: Like, [INAUDIBLE] in transcription mining site. PROFESSOR: Ah. Yeah. And so you would identify those how? AUDIENCE: By looking at sequences upstream of [INAUDIBLE], and seeing what different sequences have in common? PROFESSOR: Right. So I think there's at least three ways-- OK, four ways I can think of identifying those types of motifs. That's probably one of the most common types of motifs encountered in molecular biology. So one way, you take a bunch of genes, where you've identified the transcription start site. You just look for patterns-- short sub-**

3

**sequences that they have in common. That might give you the TATA box, for example.**

**Another way would be, what about comparative genomics? You take each individual one, look to see which parts of that promoter are conserved. That can also help you refine your motifs. Protein binding, you could do ChIP-Seq, that could give you motifs.**

**And what about a functional readout? You clone a bunch of random sequences upstream of a luciferase reporter, see which ones actually drive expression, for example. So, that would be another. Yeah, absolutely, so there's a bunch of different ways to define them.**

**In terms of when we talk about motifs, there are several different models of increasing resolution that people use. So people often talk about talk about the consensus sequence so you say the TATA box, which, of course, describes the actual motif-- T-A-T-A-A-A, something like that. But that's really just the consensus of a bunch of TATA box motifs. You rarely find the perfect consensus in real promoters-- the real, naturally occurring ones are usually one or two mismatches away. So that doesn't fully captured it.**

**So sometimes you'll have a regular expression. So an example would be if you were describing mammalian 5 prime splice sites, you might describe the motif as GT, A or G, AGT, or sometimes abbreviated as GTR AGT, where R is shorthand for either appearing nucleotide-- either A or G. In some motifs you could have GT, NN, GT, or something like that. Those can be captured, often, by regular expressions in a scripting language like Python or Perl.**

**Another very common description in motifs, there would be a weight matrix. So you'll see a matrix where the width of the matrix is the number of bases in the motif. And then there are four rows, which are the four bases-- we'll see that in a moment. Sometimes these are described as position-specific probability matrices, or positionspecific score matrices. We'll come to that in a moment. And then there are more complicated models. So it's increasingly becoming clear that the simple weight**

4

**matrix is too limited-- it doesn't capture all the information that's present in motifs.**

**So we talked about where do motifs come from. These are just some examples. I think I talked about all of these, except for in vitro binding. So in addition to doing a CLIP-seq, where you're looking at the binding of the endogenous protein, you could also make recombinant protein-- incubate that with a random pool of DNA molecules, pull down, and see what binds to it, for example.**

**So why are they important? They're important for obvious reasons-- that they can identify proteins that have a specific biological property of interest. For example, being phosphorylated by a particular kinase. Or promoters that have a particular property. That is, that they're likely to be regulated by a particular transcription factor, et cetera.**

**And ultimately, if you're very interested in the regulation of a particular gene, knowing what motifs are upstream and how strong the evidence is for each particular transcription factor that might or might not bind there, can be very useful in understanding the regulation of that gene. And they're also going to be important for efforts to model gene expression.**

**So, a goal of systems biology would be to predict, from a given starting point, if we introduce some perturbation-- for example, if we knock out or knock down a particular transcription factor, or over-express it, how will the system behave? So you'd really want to be able to predict how the occupancy of that transcription factor would change.**

**You'd want to know, first, where it is at an endogenous levels, and then how its occupancy at every promoter will change when you perturb its levels. And then, what effects that will have on expression of downstream genes. So these sorts of models all require really accurate descriptions of motifs.**

**OK, so these are some examples of protein motifs. Anyone recognize this one? What motif is that? So it says X's. X's would be degenerate oppositions, and C's would cysteines. And H's [INAUDIBLE]. What is this? What does this define? What**

5

---

[Up: contents](index.md) · [protein has this? What can you predict about its function? →](02-protein-has-this-what-can-you-predict-about-its-function.md)
