---
title: STUDENT
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/14m9mw-qmhg-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STUDENT

**Source:** `recordings/14m9mw-qmhg-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**So I'm guessing all of [INAUDIBLE] that selection is absent.**

**Right, right. This is ignoring selection. That's a good point.**

**So think about this. And let me if other questions come up.**

**So this actually came up the other day when we were talking about DNA substitution models. So Kimura and others have observed that transitions occur much more often than transversions, maybe two to three times as often, and so proposed a matrix like this. And now you can use what you know about stationary distributions to solve for the limiting or stationary distribution of this matrix. And actually, you will find it's still symmetrical. It's a little bit more complicated now, but you'll still get that 1/4, 1/4.**

**But then more recently others have observed that really, dinucleotides matter in terms of mutation rates, particularly in vertebrates So what's special about vertebrates is that they have methylation machinery that methylates CPG dinucleotides on the C.**

**And that makes those C's hypermutable. They mutate at about 10 times the rate of any other base. And so you can give a higher mutation rate to C, but that doesn't really capture it. It's really a higher mutation rate of C's that are next to G's. And so you can define a model that's 16 by 16, which has dinucleotide mutation rates. And that's actually a better model of DNA sequence evolution. And it's just the math gets**

19

**a little hairier if you want to calculate stationary distribution. But again, it can be done.**

**And it's actually pretty easy to simulate. Knowing that it will converge to the stationary, you can just run the thing many times. And you'll get to the answer. And there's even been strand-specific models proposed, where there are some differences between how the repair machinery treats the two DNA strands that are related to transcription coupled repair. So you actually get some asymmetries there. And this is a reasonably rich area. And you can look at some of these references.**

**All right, so one more topic, while we're on evolution-- this is very classical. But I just wanted to make sure that everyone has seen it. If you are looking specifically at protein coding sequences, exons, and you know the reading frame, you can just align them.**

**And then you can look at two different types of substitutions. You can look at what are called the nonsynonymous substitutions, so changes to the codons that change the underlying amino acid, the encoded amino acid. And you define often a term that's either called Ka or dN, depending who you read, that is the fraction of nonsynonymous substitutions divided by nonsynonymous sites.**

**And in this case let's do synonymous first. So you can also look at the other changes. So these are now synonymous changes which are base changes to triplets that do not change the encoded amino acid. So in this case, there are three of those.**

**And a lot of evolutionary approaches are just based on calculating these two numbers. You count synonymous changes. You divide by synonymous sites, count non-synonymous substitutions, divide by non-synonymous sites. And so what do we mean synonymous site?**

**Well if you have only amino acids that are fourfold, that have fourfold degenerate codons, which is all of them are like that in this case, then for example GG-- or let's see what's up here. Yeah, CC anything codes for proline. Do we have any of those?**

20

**Actually, these are not all fourfold degenerate. I apologize.**

**But glycine, for example-- so GG anything is glycine. So in this triplet, this triplet here, there's one synonymous site. The third side is a synonymous site. You can change that without changing the amino acid. But the other two are nonsynonymous.**

**So to do first approximation, you take non-synonymous substitutions and divide by the number of codons-- I'm sorry, the number of codons times 2, since there are two non-synonymous positions in each codon. And you take synonymous substitutions, divide by the number of codons. OK, does that make sense? One per codon.**

**OK and so what do you then do with this? You can correct this value using-basically this is the Jukes-Cantor correction that we just calculated, this 3/4 log 1 minus 4/3. That applies to codon evolution as well as individual base evolution.**

**And what people often do with this is they calculate Ka and Ks for a whole gene. Let's say you have alignments of all human genes to their orthologs in mouse-- that is, the corresponding homologous gene in mouse. And you calculate Ka Ks. And then you can look at those genes where this ratio is significantly less than 1, or around 1, or greater than 1. And that actually tells you something about how that-the type of selection that that gene is experiencing.**

**So what would you expect to see-- or if I told you we've got two genes and the Ka/Ks ratio is much less than 1. It's like 0.2. What would that tell you? Or what could you infer about the selection that's happening to that gene? Ka/Ks is much less than 1. Any ideas? Julianne, yeah.**

**STUDENT: The protein sequence is important-- or the amino acid sequence.**

**PROFESSOR: Yeah, exactly. The amino acid sequence is important. Because you assume that those synonymous sites and non-synonymous sites-- they're going to mutate at the same rate, right? The mutation processes don't know about protein coding. So what you're seeing is an absence, a loss, of the non-synonymous changes.**

21

**80% of those non-synonymous changes have been kicked out by evolution. You're only seeing 20%. And you're using, assuming the non-synonymous are neutral-- I'm sorry. I seem to have trouble with these words today. But you assume that the synonymous ones are neutral. And then that's calibrates everything. And then you see that the non-synonymous are much lower. Therefore you must have lost-these ones must have been kicked out by evolution.**

**So the amino acid sequence is important. And it's optimal in some sense. The protein works-- the organism does not want to change it. Or changes to that protein sequence make the protein worse. And so you don't see them. And that's what you see for most protein coding genes in the genome-- a Ka/Ks ratio that's well below one. It says we care what the protein is. And it's pretty good already. And we don't want to change it.**

**All right, what about a gene that has a Ka/Ks ratio of around 1? Anyone have an idea what would that tell you about that gene? There are some-- Daniel? STUDENT: The sequence is-- it doesn't particularly matter. Maybe it's a non-coding, nonregulatory patch of DNA. I assume there must be something. PROFESSOR: Yeah, so it could be that it's not really protein coding after all. It's non-coding. Then this whole triplet thing we were doing to it is arbitrary. So you don't expect any particular distribution. That's true. Any other possibilities? Yeah, Tim.**

**STUDENT: Could be that there are opposite forces that are equilibrating. For example, we're taking the unit of the G. But maybe in one half of the G there's a strong selective pressure for non-synonymous and in the other half it's strong selective pressure for synonymous. Alternatively, it could be in the same par of the gene, but it's involved in two different processes. It's diatropic. So in one process it's selecting this one thing.**

**PROFESSOR: Yeah, or one period of time, if you're looking at 10 million years of evolution, it could have been for this first five million years it was under negative selection, and then it was under positive. And it averages out. Yes, all those things are possible, but kind**

22

**of unusual.**

**And so maybe if you saw that the-- if you plotted Ka/Ks along the gene and you saw that it was high in one area and low in another, then that would tell you that you probably shouldn't be taking the average across the gene. And that would be a good thing to look for.**

**But what if-- again, so we said if Ka/Ks is near 1 it could be that it's not really a protein coding gene at all. That's certainly possible. It could also be though that it's a pseudogene. Or it's a gene that is no longer needed by the organism. It still codes for protein, but the organism just could care less about its function.**

**It's something that maybe evolved in some other time. It helps you adapt to when the temperature gets below minus 20. But it never gets below minus 20 anymore. And so there's no selection on it, or something like that. So neutral indicates-- this is called neutral evolution.**

**And then what about a gene which has a Ka/Ks ratio significantly greater than 1? Any thoughts on what that might mean and what kind of genes might happen to-yes, what's your name?**

**STUDENT: Simona.**

**PROFESSOR: Simona, go ahead.**

**STUDENT: It might be a gene that's selected against, so something that's detrimental to the cell or the organism.**

**PROFESSOR: It's detrimental-- so the existing protein is bad for you, so you want to change it. So it's better to change it to something else. That's true. Can you think of an example where that might be the case?**

**STUDENT: A gene that produces a toxin.**

**PROFESSOR: A gene that produces toxin. You might just lose the gene completely if it produced a toxin. Any other examples you can think of or other people? Yeah, Jeff.**

23

**STUDENT: Maybe a pigment that makes the organism more susceptible to being eaten by a predator. PROFESSOR: OK, yeah if it was a polar organism and it happened to have this gene that made the fur dark and it showed up against the snow, or something like that. And you can imagine that. Or a very common case is, for example, a receptor that's used by a virus to enter the cell. It probably had some other purpose. But if the virus is very virulent, you really just want to change that receptor so that the virus can't attack it anymore. So you see this kind of thing is much rarer. It's only less than 1% of genes probably are under positive selection, depending on how you measure it and what time period you look at. But it tends to be really recent, really strong selection for changing the protein sequence. And the most common-- well, probably the most common-- is these immune arms races between a host and a pathogen.**

**But there are other cases too. You can have very strong selection where-- well, I don't want to-- basically where a protein is maladapted, like the organism moves from a very cold environment to a very warm environment. And you just need to change a lot of stuff to make those proteins better adapted. Occasionally you can get positive selection there. Yeah, go ahead.**

**STUDENT: So the situation where K or Ks is 1-- could it be possible that the mRNA is under selection?**

**PROFESSOR: Yeah, so that basically we have always been implicitly assuming that the synonymous substitution rate was neutral. But it could actually be it's not neutral. That's under negative selection too. And it happens that they balance. That's also possible.**

**So for that, to assess that, you might want to compare the synonymous substitution rate of that gene to neighboring genes. And if you find it's much lower, that could indicate that the coding sequences-- the third base of codons is under selection-could be for splicing, maybe. It could be for RNA secondary structure, translation,**

24

**p g, y y , ,**

**different other-- that's a good point.**

**So yeah, you guys have already poked holes in this. This is a method. It gives you something. You'll see it used. It gives you some inferences. But there are cases where it doesn't fully work. OK, good.**

**So in the remaining time I wanted to do some examples of comparative genomics. So as I mentioned before, these are chosen to just give you some examples of types of things you can learn about gene regulation by comparing genomes again, often by using really simple methods, just blasting all the genes against each other or things like this. And also, if you do choose to read some of these papers, it can give you some experience looking at this literature in regulatory genomics.**

**So the papers I've chosen-- we'll start with Bejerano et al from 2002, who basically sought to identify regulatory elements that are things that are under evolutionary constraint. That's all he was trying to find. Didn't know what their functions were. But they turned out to be interesting nonetheless, which is maybe a little surprising.**

**And then this other work from Eddy Rubin's lab and others-- Steve Brenner's lab-actually characterized some of these extremely conserved regions and assessed their function. And then Bejerano came back a few years later and actually had a paper about where these extremely conserved regions actually came from.**

**So we'll talk about those. Then we'll look at some papers that have to do with inferring the regulatory targets of a transacting factor. And the factors that we'll consider here will be microRNAs, mostly, Either trying to understand what the rules are for microRNA targeting and these Lewis et al papers, or trying to identify the regulatory targets in the genome.**

**And then, time permitting, we'll talk about a few other examples of slightly more exotic things. Graveley identified a pair-- or pairs-- of interacting regulatory elements through a clever comparative genomic approach. And then I'll talk about these two examples at the end if there's time, where a new class of transacting factors was inferred from the locations of the encoded genes in the genome. And**

25

**also an inference was made about the functions of some repetitive elements from, again, looking at the matching between these elements and another genome.**

**All right, so first example-- Bejerano "Ultraconserved elements." So they defined, in a fairly arbitrary way, ultraconserved elements as unusually long segments that 100% identical between human, mouse, and rat. This was in 2000-- I'm sorry, I might have the wrong-- it's either 2004 or 2002. I forget.**

**This was basically when the first three mammalian genomes had been sequenced, which were human, mouse, and rat. And there were whole genome alignments. So they basically said let's try to use these whole genome alignments to find what's the most conserved thing in mammals. So they wanted to see if there's anything 100% conserved. And so they did statistics to say what's an unusually long region of 100% identity.**

**Any ideas how you would do that calculation, what kind of statistics you would use? They used a really simple approach. What they did was they took one megabase segments of the genome, assuming it might vary across the genome. They took ancestral repetitive elements-- so repetitive elements that were inserted, that were present in mouse, rat, and human-- and assumed that they were neutrally evolving, they were not under selection.**

**And then therefor you could look at the number of differences and get an idea what the background rate of mutation is. And they use that. And they found that that rate was-- this is from their supplementary data-- that was never greater than 0.68. And so they just said well, if we have a probability of-- I'm sorry. One is heads.**

**So if they're all three the same-- yeah, so if we have a probability of 0.7 of heads, meaning that they're all three the same, then the chance that you have 200 heads in a row would be 1 minus P P to the 200, just like [INAUDIBLE] trials. And you can just multiply that times the size of the genome. And you say it's extremely unlikely that you'll ever see anything where there's 200 identical nucleotides in a row. So that's what they defined as an ultraconserved element.**

26

**So it all seems very silly for now, until you actually get to what they find. So they looked at where are these elements around the genome. They found about 100 overlapped exons of known protein coding genes, 100 are in introns, and the remainder are in intergenic regions.**

**So then they looked at well what kind of genes contain exons with overlapping-- or contain ultraconserved elements that overlap exons? Those are type 1 genes. And what kind of genes are next to the intergenic ultraconserved elements, to try to get some clues about the function of these elements.**

**And so they did this early gene ontology analysis. And what they found was that the ultraconserved elements that overlapped exons tended to fall in genes that encoded RNA-binding proteins, particular splicing factors, by an order of magnitude more frequent. And then the type 2 genes, the ones that were next to these intergenic ultraconserved regions, tended to be transcription factors. In particular, homeobox transcription factors were the most enriched class.**

**So this gave them some clues about what might be going on. Particularly the second class was followed up by Eddy Rubins's lab at Berkeley. And they tested 167 extremely conserved sequences. So some of them were these ultraconserved elements. And some of them were just highly conserved, but not quite 100% conserved.**

**And they had an assay where they have a reporter. It's a lacZ with a-- you take a minimal promoter, fuse in to lacZ, and then you take your element of interest and fuse it upstream. And then you do staining of whole mount embryos. And you say what pattern of gene expression does this element drive, or does it drive a pattern of gene expression?**

**And so 45% of the time it drove a particular pattern of gene expression. So it functioned as an enhancer. And these are the types of patterns that they saw. So they saw often forebrain, sometimes midbrain, neural tube, lim, et cetera. So many of these things are enhancers that drive particular developmental patterns of gene expression. So that out to be actually-- that was a pretty good way to identify**

27

---

[← different comments. And then we'll try to summarize. Go ahead.](02-different-comments-and-then-we-ll-try-to-summarize-go-ahead.md) · [Up: contents](index.md) · [developmental enhancers. →](04-developmental-enhancers.md)
