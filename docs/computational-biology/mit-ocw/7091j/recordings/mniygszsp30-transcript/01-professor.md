---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/mniygszsp30-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/mniygszsp30-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**OK. Well hello, everyone. And welcome back to Computational Systems Biology. I am David Gifford and I am delighted to be back with you today.**

**We're going to talk, today, about understanding transcription. Specifically, how we're going to understand transcription is a technique called RNA-seq. And RNA-seq is a methodology for characterizing RNA molecules through next generation sequencing.**

**And we'll talk, first, about RNA-seq principles. We'll then talk about how to take the data we learn from RNA-seq and analyze it using tools for characterizing differential gene expression and principal component analysis. And finally, we'll talk about single cell RNA-seq, which is a very important and growing area of scientific inquiry.**

**But first, let's talk about RNA-seq. How many people have heard of RNA-seq before? Fantastic. How many people have done it before? Some? Great.**

**So RNA-seq is fairly simple in concept. What we're going to do is we're going to isolate RNA species from a cell or collection of cells in the desired condition. And note that we can choose which kind of RNA molecules to isolate.**

**We can isolate molecules before any selection, which would include molecules that are precursor RNAs that have not been spliced yet, including non-coding RNAs. As you probably know, the study of non-coding RNAs is extraordinarily important. There are over 3,300 so-called long non-coding RNAs that have been characterized so far. Those are non-coding RNAs over 200 bases long. We'll be talking about those later on, when we talk about chromatin function in the genome.**

**And of course, there are the precursor messenger RNAs that are spliced, turned**

1

**into messenger RNAs that are then translated into protein. And the specifics of the RNA-seq protocol will give you various of these species depending upon what kinds of purification methodologies you use. But as you're aware, there are many isoforms that are possible in most mammalian genes.**

**This is a short summary, produced by the Burge Laboratory, of different kinds of splicing events that can occur. And the splicing events are often regulated by cisregulatory sequences that live in the introns. And these introns contain recognition sequences for splicing factors where the splicing factors can be conditionally expressed. And so you get different combinations of these exons being glued together to produce variant forms of proteins.**

**So we have to be mindful of the idea that the RNA molecules that we're going to be observing, typically, are going to be reverse transcribed. So we'll see entire transcripts that came, perhaps, from distinct exonic locations in the genome.**

**And the essential idea of RNA-seq is that we take the RNA molecules we care about-- in this case, we're going to purify the ones that have poly-A tails. We will take those molecules. We'll reverse transcribe them. We'll sequence fragments of them and then map them to the genome.**

**Now if you don't purify for poly-A tails, you get a lot of things mapping to the genome that are intronic. And so you get a lot of data that is very difficult to analyze. So typically, people, when they're looking for gene expression data, will do poly-A purification. And when you do this-- when you sequence the result of doing the reverse transcription of these RNA molecules-- and you map the results to the genome, what you find is data that looks like this.**

**This is the SOX2 gene. This is typical expression data. You can see all of the individual reads mapping to the genome, the blue in the plus strand, the pink on the minus strand. And our job is to take data like this and to analyze it.**

**Now we can take these data and we can summarize them in various formats. One way is to simply count the number of times that we see a read at a particular base,**

2

**like here, for the SMUG1 gene. And here you see something else going on, which is that we have reads from-- the sequencing experiments have been polyadenylated and purified. So we're only seeing the reads that occur over the exonic sequences, more or less. There are a few intronic reads there, scattered about.**

**The other thing that we see, which is very important, is that we see reads that are split across exons. Because the splicing event has occurred, the RNA molecule is a contiguous sequence of a collection of exons. And sometimes you'll get a read that spans an exon-exon boundary. And when we get this, you can see, in the bottom part of the slide that I'm showing you, these reads can map across the exons.**

**Typically, in order to get good performance out of something like this, we want to use reads that are about 100 bases long. And we'll use a mapper that is capable of mapping both ends of a read to account for split reads for these exon crossing events. So that gives you an idea of the kinds of data that we have. And part of the challenge now is looking at how we can determine which particular isoforms of a gene are being expressed by evaluating these data.**

**So there are two principal ways of going about this. One way is we simply take our read data, and we use the ideas that we talked about in genome assembly, and we assemble the reads into transcripts. That's typically done de novo. There are reference guided assemblers.**

**It has the benefit that you don't need a reference genome. So sometimes, when you're working with an organism that does not have a well characterized reference genome, you will de novo assemble the transcripts from an RNA-seq experiment. But it also has problems with correctness, as we saw when we talked about assembly. The other approach, which is more typically used, is to map reads, or aligned the reads, to a reference genome and identify the different isoforms that are being expressed using constraints. And ultimately, the goals is to identify the isoforms and quantitate them so we can do further downstream analysis.**

**And you'll hear about two different metrics, sometimes, in the literature, for expression. One is the number of reads per kilobase of transcript per million reads.**

3

**So you might have, for example, an RPKM metric of 1,000, which means that one out of every thousandth read is mapping to a particular gene. So it gives you a metric that's adjusted for the fact that longer genes will produce more reads.**

**An alternative metric is fragments per kilobase per million. And that's sometimes used when we're talking about paired end data. And you're considering that you're sequencing both ends of a fragment. So here we're talking about how many fragments we see for a particular gene per 1,000 bases of the gene per million fragments.**

**OK. So the essential idea, then, is to take the reads that we have-- the basket of reads-- align it to the genome, both to exons and to exon crossings, and to determine, for a given gene, what isoforms we have and how they're being expressed. So from here on in, I'm going to assume that we're talking about a gene and its isoforms. And that's OK. Because typically, we can map reads uniquely to a gene. And there are details, of course, when you have genes there are paralogs that have identical sequences across the genome where this becomes more difficult.**

**So if we consider this, once again, we're going to take our reads, we're going to map them to the genome, and we're going to look for all possible pairings of exons. What we would like to do is to enumerate all of the possible isoforms that are possible given the data that we have. And we can use junction crossing reads and other methodologies to enumerate all the possible isoforms.**

**But what we're going to assume is that we've enumerated all the isoforms. And we're going to number them 1 through n. So we have isoform 1, isoform 2, isoform 3 for a given gene. And what we want to compute for each isoform is its relative contribution to the read population we're seeing that maps to that gene.**

**So in order to do that, what we could do is use some constraints. So if I show you this picture, which suggests that we have possible splice events here for the event C in the middle, if I told you that A, C, and E were very highly covered by reeds, you might think that A, C, and E represented one isoform that was highly expressed.**

4

**And so if we think about how to use our read coverage as a guide to determining isoform prevalence, we'll be in good shape.**

**And really, that's the best evidence we have. We have two sources of evidence, right? We have our junction crossing reads, which tell us which exons are being spliced together, that helps us both compute the set of possible isoforms and estimate their prevalence. The other thing we have is the reads that actually simply cover exons. And their relative prevalence can also help us compute the relative amounts of different isoforms.**

**So in order to do this, we can think about what reads tell us. And some reads will exclude certain isoforms. So if we consider the reads that we have, we can think about reads that cross particular junctions that are inclusion reads saying that-- for example, in this case, the top reads are indicating that the middle white exon is being included in a transcript whereas the bottom reads are exclusion reads indicating that that white exon in the middle is being spliced out.**

**So what we would like to do, then, is to build a probabilistic model that takes into account what we know about what a read tells us. Because each read is a piece of evidence. And we're going to use that read like detectives. We're going to go in and we're going to try and analyze all of the different reads we see for a gene and use it to weight what we think is happening with the different isoform expressions in the pool of reads that we're observing.**

**And in order to do so, we will have to build a function that describes the probability of seeing a read given the expression of a particular isoform. So the essential idea is this-- for the next three slides, I want to build a model of the probability of seeing a read conditioned upon a particular isoform being expressed. All right? So there are three ways to approach this.**

**One is that I can see a read that I know is incompatible with a given isoform. And therefore, the probability of seeing that read given the isoform is 0. And that's perfectly fine. And this can either happen with a single ended read or with a paired end read. And it's a conditional probability. So the probability of seeing read i given**

5

**and isoform j can be 0.**

**Another possibility is that, if I have a transcript-- now recall that the transcript has been spliced. So what we're looking at is the entire sequence of the spliced isoform. And we see a read. And the read can land anywhere within that transcript. Let's assume, for the time being, we're looking at single ended read. Then, the probability of seeing that read land in that transcript is 1 over the length of the transcript-- all right-- at a particular base.**

**So this read is compatible with that transcript. And we can describe the probability in this fashion. It's also possible for us to consider paired end reads. And if we have paired end reads, we can describe a probability function that has two essential components.**

**The denominator is still the same. That is, the likelihood of the read aligning at a particular position is going to be 1 over the length of the entire transcript. The numerator is different though. We're going to compute the length of the read that we have, or the implied length of the paired end read, and ask, what's the likelihood of seeing that.**

**So we don't know the exact length, recall, of the insert. When we're looking at paired end reads, we can only estimate how long the fragment is that we're sequencing. And so we are going to have a probabilistic interpretation of how long the piece of RNA is that we actually wound up sequencing the ends of. And that is placed in the numerator, which scales the 1 over l sub j. So this gives us a probability for seeing a read in a particular transcript that accounts for the fact that we have to back both ends to that transcript. OK?**

**So we have three possibilities that we've described, one, where a particular read is incompatible with an isoform, two, where we had a single end read mapping to an isoform, which is simply 1 over the length of the isoform, and three, where we're mapping paired end reads to an isoform, which includes uncertainty about where it will map, which is the 1 over l sub j, and also uncertainty about the length of the fragment itself, which is encoded in the F function, which is a distribution over**

6

**fragment lengths.**

**OK. So once we have this structure, we can then estimate isoform expression. Now we talked before, when we talked about ChIP-seq last time, the idea of estimating proportions. And the essential idea here is that if we want to compute the probability of a read given, in this case, a mixture of isoforms, that's simply going to be-- let's see, what variable did I use? Yeah-- the estimated concentration of that isoform times the probability of the read as seen in that isoform.**

**So for an individual read, we can estimate its likelihood given this mixture. And then the product around the outside describes how to estimate the probability of the entire basket of reads that we see for that gene. And what we would like to do is to pick psi, in this case, to maximize the likelihood of the observed reads. So what psi is going to do is it's going to give us the fraction of each isoform that we see.**

**Are there any questions about the idea of isoform quantitation? Yes.**

**AUDIENCE: I'm a little lost in-- in the last full slide review, you were describing these three cases for excluded, single, and paired reads. So we're computing the different probabilities for both ends to happen in a transcript, of for just one, or--**

**PROFESSOR: It depends. The second and third cases depend upon whether we're analyzing single ended reads or paired end reads. And so we wouldn't use both of them at the same time. In other words, if you only have single ended data, you would use the second case that we showed. And if you had paired end data, you would use the third case that we showed.**

**AUDIENCE: OK.**

**PROFESSOR: Question, yes.**

**AUDIENCE: Sorry. I noticed that the single end reads case-- could you explain the intuition behind that probability [INAUDIBLE]?**

**PROFESSOR: Sure. The intuition behind that probability is that we're asking-- so here is a**

7

**transcript. And we're assuming, what is the probability of a read given that it came from this transcript. OK? What's the probability of observing a particular read? And the probability of observing it lining up at a particular position is 1 over the length of this transcript. And so the probability actually includes the idea of alignment at a particular position in the transcript. OK? So obviously, the probability's 1 if we assume it comes from here if we don't consider this fact. But if we want to ask where it lines up in the transcript, it's going to be 1 over l sub j. OK? AUDIENCE: So we assume that it's uniformly possible? PROFESSOR: That it's uniformly possible, which gets us to a good point. I'm glad you asked that question. Sometimes we would have more reads at the three prime end of a transcript than the five prime end. Can anybody imagine why? Yes. AUDIENCE: Because you're pulling on the poly-A tails. PROFESSOR: Yeah. So this actually was purified by the poly-A tail. And we're pulling on this. We're purifying by it. And if there's breakage of these transcripts as it goes through the biochemical processing, we can get shorter and shorter molecules. They all contain this bit. And the probability to contain that whole thing actually decreases. So oftentimes there is three prime bias in RNA-seq experiments one needs to be mindful of. But we're assuming, today, that there isn't such bias and that the probability's equal that it maps someplace in this transcript. OK? Does that answer your question? Yes. AUDIENCE: Sorry. I do have one more. Can you show us how that extends, then, to the paired end read and where the probability distribution-PROFESSOR: Right. So if we go to paired end reads, right, like this, this component is going to be where it aligns, right? And then, the probability of the length of this entire molecule is what I had up there before, which is-- exactly how did I do that? So this is going to be-- this is this bit, which is the implied length of this. OK? So if I map the left and the right-- this component is where the left end maps. OK? I take**

8

**the left and the right ends of the read that I have from that transcript. And it has a particular length on this transcript. OK? I'll call that length l sub j of R sub i.**

**Now remember, that is not the same as the length in the genome. That's the length in this transcript as it is spliced. OK? F is going to be the probability distribution of the length of the fragments. So let's just say that they're centered around 200 bases. OK?**

**So if this is exactly 200 bases, it's going to be quite likely. OK? But imagine that when I map this fragment, this wound up being 400 bases apart. Then, this distribution would tell is it's very unlikely that I would see a fragment that mapped here and mapped 400 bases up here, because my fragment with distribution defined by F is 200 bases.**

**So it's going to discount that, the probability of that. So this term that the probability of the read given the transcript is the component of where it's aligning times the likelihood that the implied fragment length agrees with what we think we have empirically. OK? Does that make sense? OK. Those are good questions.**

**OK. So given this framework, we can either use EM or other machine learning like frameworks to maximize psi and to learn the fraction of expression of each different isoform from the observed data given the functions that we have. And just to give you an idea, when this was done for myogenesis, a program called Cufflinks, which does this kind of process of identifying isoform prevalences, was able to identify a large number of transcripts.**

**70% of the reads were in previously annotated transcripts. But it also found 643 new isoforms of genes in this single time series. And I posted one of the papers that describes some this technology on the Stellar site. But note that certain of the genes have light coverage.**

**And what we're seeing here is that for genes are expressed in low copy numbers, it's obviously more difficult to get reads out of them. And I'm presuming, in this particular experiment-- although I can't recollect-- that the reason they don't see**

9

**that many intronic reads is they did poly-A purification. OK. So we've talked about how to take our reads, build a probabilistic model, estimate isoform prevalences. And we know how many reads are mapping to a given gene. The question now is whether or not we see differential expression of a gene in different conditions. So I'd like to turn to the analysis of differential expression unless there are any final questions about the details of RNA-seq and isoform estimation.**

**This is your chance to ask those hard questions. Yes. AUDIENCE: OK. I have a really silly question. But can you explain, really quickly, what are isoforms? PROFESSOR: What an isoform is? AUDIENCE: Yeah. PROFESSOR: Sure. An isoform is a particular splice variant of a gene. So a gene that has a particular splicing pattern is called an isoform. So imagine we have three exons, one, two, and three. And a transcript that has all three would be one isoform. And another variant that omits two would be a second isoform. So just one in three would be an isoform. And each gene has a set of isoforms it exhibits. And that depends upon how it's regulated and whether or not any splicing is constitutive-- it always happens-- or whether or not it's regulated. And so in theory, a gene with n exons has how many potential isoforms?**

**It's 2 to the n. Because you can consider each exon being included or omitted. All right. But that isn't typically the case-- that there are many fewer isoforms than that. But in general, an isoform refers to a particular splice variant of a gene. Yes. AUDIENCE: I just want to make sure I have everything correctly. When you're using single legged or pair end reads, you can get excluded ends, right? So you can get that in both cases, whether or not you're--**

10

- **PROFESSOR: Well, it depends. Once again, it's somewhat probabilistic where the reads actually hit. Because if all the reads only hit exons, and you didn't get any junctions, and none of your paired end reads crossed junctions, then you wouldn't actually have exclusion. All right?**

- **AUDIENCE: But it's possible for using both types of sequencing?**

- **PROFESSOR: Yes, it's possible with both types of sequencing. In fact, oftentimes, what people do is that they will count junction crossing reads. If you have a large enough number of reads in your sequencing, say, 100 base pairs at least, then a large number of your reads are going to be-- not a large, but a significant fraction-- will be exon crossing. And you'll be able to count the number of exon-exon junctions you have of different types.**

   - **And that will give you an estimate of how much splicing is going on and will help validate the kinds of conclusions that come out of programs like Cufflinks or MISO, which is another program from the Burge Laboratory that is used to estimate isoform prevalence. Yes.**

- **AUDIENCE: So even given this information, you can't say which exons go with which exons necessarily, except paralogs, right? Because the reads, in general, aren't long enough to span an exon. And therefore we wouldn't know, for example, that a given transcript is exons one, five, and six. You could only know that exons five and six went together.**

- **PROFESSOR: That is not strictly true if you have paired end reads and your fragments are long enough to span exons. But in general, you're correct. And that's why modern sequencing technologies that are coming down the pike that can do 25 kilobase reads are so important for doing things just like that. Yes.**

**AUDIENCE: In your diagram of the read up there, are the boxes the actual genome or RNA sequence and the line in between the artificial linker that you added when you seq ref'd?**

11

**PROFESSOR:**

**Ah, that's a good question. The question is, is this the linker and these are the actual sequences. No. What I'm drawing here is that these are the bits that we actually get to see the sequence of. We sequence from both ends of a molecule. This is the part of the fragment that we haven't sequenced because our reads aren't long enough.**

**And so the entire fragment might be 300 bases long. If this is 100 and this is 100, then the unobserved part is 100 in the middle. OK? And that's called the insert length, the entire length of the molecule.**

**And we get to choose how long these fragments are up to a maximum size. Contemporary sequencers don't really like fragments over 1,000 bases. And the performance starts falling off when you get close to that number. So people, typically, are operating in a more optimal range of fragments that are a few hundred bases long. Any other questions? OK.**

**So I wanted to briefly talk about hypothesis testing. Because we're going to be needing it for determining when things are really differentially expressed. So I'm just going to show you some data and ask you a few questions about it.**

**So here are two different scatters of data. Well, actually, it's exactly the same data. But we have two different bits to it. We have two independent Gaussians that are fit to the data, from gene one and gene two. And another fit uses two Gaussians that have a correlation structure between them.**

**And the question is whether or not the null hypothesis or the alternative hypothesis is more reasonable. And typically, when we say reasonable, we want to judge whether or not it's significant. Significance typically talks about, what's the chance that the data we saw occurred at random given the null hypothesis. So what's the chance it was generated by the null hypothesis versus the chance that it was generated by the alternative hypothesis?**

**Now the problem is that alternative hypotheses, typically, are more complex. And a more complex model will always explain data better. So we need to have a**

12

**principled way of asking the question, given that the alternative hypothesis is always going to do a better job, does it do such a better job that it can exclude the null hypothesis at a particular probability level. OK?**

**So here are two different models for these data. The null model, H0, is that they came from two independent Gaussians. The alternative model, H1, is that they came from two correlated Gaussians. And then we can ask whether or not H1 is sufficiently more likely to warrant our rejecting H0 and accepting H1.**

**Now as I said, H1 is always going to fit the data better. So the probability of that collection of points evaluated with the H1 model, fit to the data, is always going to be superior. So we need to have a way to compare the probability of the data given H1 versus the data given H0 in a way that allows us to judge the probability that the data via H0 occurred at random.**

**In this particular case, the data supports H1. And let's see why. So this is a key idea here. How many people have heard of likelihood ratio statistics before? OK. About half the class. OK. So here's the idea.**

**The idea is that what we're going to do is we're going to compute a test statistic. And the test statistic is going to be a function of the observed data. And it's 2 times the log of the probability of the observed data given H1 over the probability of the observed data given H0. OK?**

**Now we know that this is always going to have a higher value than the probability in the denominator. So this is always going to be greater than 1. So the test statistic will always be greater than 0 since we're operating in the log domain. OK?**

**The question is-- we know that this is always going to be better, even when the data was generated from H0. But when is this sufficiently better for us to believe that H0 is not true and we should accept H1? What we need is a distribution for this test statistic that occurred if H0 was true. And that distribution allows us to compute the probability that an observed value for the test statistic occurred, even in the presence-- assuming that H0 is true.**

13

**OK. So this depends upon the number of degrees of freedom difference between H1 and H0. How many degrees of freedom are there in H1 in this model up here? How many parameters do we get to pick?**

**AUDIENCE: Six.**

**PROFESSOR: Hmm? AUDIENCE: Six. PROFESSOR: Six?**

**AUDIENCE: Two means and four--**

**PROFESSOR: Two means and four coherences. And for H0?**

**AUDIENCE: Just four.**

**PROFESSOR: Four. So what's the difference in the number of degrees of freedom between H1 and H0? It's two. So the test statistic is parametrized by the difference in number of degrees of freedom. And so what we see, then, is something that looks like this.**

**We see a test statistic where this is the probability of it, on the y-axis, and the test statistic on the x-axis. But as the test statistic gets larger and larger, the probability that it occurred with H0 being true gets smaller and smaller. So let us just suppose that we took our data from our model that we observed. And we computed the test statistic at a particular value call T observed.**

**So this is the actual value that we computed out of our likelihood ratio test. What we would like to ask is, what's the probability that our test statistic is greater than or equal to T observed given that H0 is true, which means that we're going to consider all the tail of this distribution. Because we want to also consider the case where T observed was even greater than what we saw. And this gives us a way of computing the probability that H0 is true given the test statistic. And this gives us our p-value. OK?**

14

**So this is a way of, in general, comparing two probabilistic models and analyzing the significance of adding extra degrees of freedom to the model. Typically, what we'll be doing in today's lecture is asking whether or not-- if we let the means change, for example, between two conditions-- we get a sufficient improvement in our ability to predict the data that our test statistic will allow us to reject the null hypothesis that the means are the same.**

**OK. I'm going to stop here and see if there are any questions at all about this.**

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
