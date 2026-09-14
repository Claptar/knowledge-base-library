---
title: '[LAUGHTER]'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kyq2dpw5neu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [LAUGHTER]

**Source:** `recordings/kyq2dpw5neu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**You can tell them, hey, you know, you have to know whether or not mom and dad both have got big problems or just all the problems are with mom, OK? Or dad. So you can put their mind at ease as you're finishing off the hors d'oeuvres.**

**OK, so I wanted just to tell you about phasing variants because we're about to go on to the next part of our discussion today. We are leaving the very clean and pristine world of very defined SNPs, defined by microarrays, into the wild and woolly world of sequencing data, right? Which is all bets are off. It's all raw sequencing data and you have to make sense of it-- hundreds of millions of sequencing reads.**

**So today's lecture is drawn from a couple of different sources. I've posted some of them on the internet. There's a very nice article by Heng Li on the underlying mathematics of SNP calling and variation which I've posted. In addition, some of the material today is taken from the Genome Analysis Toolkit, which is a set of tools over at the Broad, and we'll be talking about that during today's lecture.**

**The best possible case when you're looking at sequence data today is that you get something like this, all right? Which is that you have a collection of reads for one individual and you align them to the genome and then you see that some of the reads have a C at a particular base position and other of the reads have a T at that base position. And so it's a very clean call, right? You have a CT heterozygote at that position-- that is, whatever person that is is a heterozygote there. You can see the reference genome at the very bottom, right? So it's very difficult for you to read**

14

**in the back, but C is the reference allele.**

**And the way that the IGV viewer works is that it shows non-reference alleles in color, so all those are the T alleles you see there in red, OK? And it's very, very beautiful, right? I mean you can tell exactly what's going on. Now we don't know whether or not the C or the T allele are a mom and dad respectively, right? We don't know which of the chromosomes they're on, but suffice to say, it's very clean.**

**And the way that all of this starts, of course, is with a BAM file. You guys have seen BAM files before. I'm not going to belabor this. There's a definition here and you can add extra annotations on BAM files. But the other thing I wanted to point out is that you know that BAM files include quality scores. So we'll be using those quality scores in our discussion.**

**The output of all this typically is something called a variant call file or a VCF file. And just so you are not completely scared by these files, I want to describe just a little bit about their structure. So there's a header at the top telling you what you actually did. And then chromosome 20 at this base location has this SNP. The reference allele is G, the alternative allele is A. This is some of the statistics as described by this header information, like DP is the read depth. And this tells you the status of a trio that you processed.**

**So this is the allele number for one of the chromosomes, which is 0, which is a G. The other one's a G, and so forth. And then this data right here is GT, GQ, GP, which are defined up here. So you have one person, second person, third person, along with which one of the alleles, 0 or 1, they have on each of their chromosomes, OK?**

**So this is the output. You put in raw reads and what you get out is a VCF file that for bases along the genome calls variance, OK? So that's all there is to it, right? You take in your read data. You take your genome, throw it through the sequencer. You take the BAM file, you call the variants, and then you make your medical diagnosis, right?**

15

**So what we're going to talk about is what goes on in the middle there, that little step- how do you actually call the variants? And you might say, gee, that does not seem too hard. I mean, I looked at the slide you showed me with the CT heterozygote. That looked beautiful, right? I mean, that was just gorgeous. I mean, these sequencers are so great and do so many reads, what can be hard about this, after all? You know, it's a quarter to 2:00, time to go home. Not quite, OK? Not quite.**

**The reason is actual data looks like this. So these are all reads aligned to the genome and, as I told you before, all the colors are non-reference bases. And so you can see that the reads that come out of an individual are very messy indeed. And so we need to deal with those in a principled way. We need to make good, probabilistic assessments of whether or not there's a variant at a particular base. And I'm not going to belabor all the steps of the Genome Analysis Toolkit, suffice to say, here is a flow chart of all the steps that go through it. First, you map your reads. You recalibrate the scores. You compress the read set and then you have read sets for n different individuals. And then you jointly call the variants and then you improve upon the variants and then you evaluate, OK?**

**So I'll touch upon some of the aspects of this pipeline, the ones that I think are most relevant, so that you can appreciate some of the complexity in dealing with this. Let me begin with the following question. Let us suppose that you have a reference genome here, indicated by this line, and you align a read to it. And then there's some base errors that are non-reference, so it's variants calls down at this end of the read, OK? So this is the five prime, three prime. And then you align a read from the opposite strand and you have some variant calls on the opposite end of the read like this.**

**And you'll say to yourself, what could be going on here, you know? Why is it that they're not concordant, right, when they're mapped, but they're in the same region of the genome? And then you think to yourself, well, what happens if I map this successfully here correctly to the reference genome and this correctly to the reference genome here, but this individual actually had a chromosome that had a deletion right here, OK? Then what would happen would be that all these reads**

16

**down here are going to be misaligned, all of these bases are going to be misaligned with the reference. And so you're going to get variant calls. And these bases will be also misaligned with the reference, you'll get variant calls.**

**So deletions in an individual can cause things to be mapped but you get variant calls at the end. And so that is shown here, where you have reads that are being mapped and you have variant calls at the end of the reads. And it's also a little suspicious because in the middle here is a seven-base pair homopolymer which is all T's. And as we know, sequencers are notoriously bad at correctly reading homopolymers. So if you then correct things, you discover that some fraction of the reads actually have one of the T's missing and all the variants that were present before go away. So this is a process of INDEL adjustment when you are mapping the region looking for variants.**

**Now this does not occur we're talking about SNP microarrays. So this is a problem that's unique to the fact that we're making many fewer assumptions when we map reads to the genome de novo.**

**The second and another very important step that they're very proud of is essentially-- I guess how to put this politely-- finding out that manufacturers of sequencing instruments, as you know, for every base that they give you, they give you an estimate of the probability that the base is correct-- or it's wrong, actually. A so-called Phred score-- we've talked about that before. And as you would imagine, manufacturers' instruments are sometimes optimistic, to say the least, about the quality of their scores. And so they did a survey of a whole bunch of instruments and they plotted the reported score against the actual score, OK?**

**And then they have a whole step in their pipeline to adjust the scores, whether you be a Solexa GA instrument, a 454 instrument, a SOLiD instrument, a HiSeq instrument, or what have you. And there is a way to adjust the score based upon the raw score and also how far down the read you are, as the second line shows. The second line is a function of score correction versus how far down the read or number of cycles you have gone. And the bottom is adjustments for dinucleotides,**

17

**because some instruments are worse a certain dinucleotides than others.**

**As you can see, they're very proud of the upper left hand part. This is one of the major methodological advances of 1000 Genome Project, figuring out how to recalibrate quality scores for instruments. Why is this so important? The reason it's important is that the estimate of the veracity of bases figures centrally in determining whether or not a variant is real or not. So you need to have as best an estimate as you possibly can of whether or not a base coming out of the sequencer is correct, OK?**

**Now if you're doing lots of sequencing of either individuals or exomes-- I should talk about exome sequencing for a moment. Up until recently, it has not really been practical to do whole genome sequencing of individuals. That's why these SNP arrays were originally invented. Instead, people sequenced the expressed part of the genome, right? All of the genes. And they can do this by capture, right? They go fishing. They create fishing poles out of the genes that they care about and they pull out the sequences of those genes and they sequence them. So you're looking at a subset of the genome, but it's an important part.**

**Nonetheless, whether or not you do exome sequencing or you do sequencing of the entire genome, you have a lot of reads. And so the reads that you care about are the reads that are different from reference. And so you can reduce the representation of their BAM file simply by throwing all the reads on the floor that don't matter, right? And so here's an example of the original BAM file and all the reads, and what you do is you just trim it to only the variable regions, right? And so you are stripping information around the variant regions out of the BAM file and things greatly compress and the downstream processing becomes much more efficient. OK.**

**Now let's turn to the methodological approaches once we have gotten the data in as good a form as we possibly can get it, we have the best quality scores that we can possibly come up with, and for every base position, we have an indication of how many reads say that the base is this and how many reads say the base is that, OK?**

18

**So we have these raw read counts of the different allelic forms. And returning to this, we now can go back and we can attempt to take these reads and determine what the underlying genotypes are for an individual.**

**Now I want to be clear about the difference between a genotype for an individual and an allelic spectrum for a population. A genotype for an individual thinks about both of the alleles that that individual has, and they can be phased or unphased, right? If they're phased, it means you know which allele belongs to mom and which allele belongs to dad, so to speak, right? If they're unphased, you simply know the number of reference alleles that you have in that individual. Typically, people think about there being a reference allele and an alternative allele, which means that a genotype can be expressed as 0, 1, or 2, which is the number of reference alleles present at a particular base if it's unphased, right? 0, 1, or 2-- 0 mean there are no reference alleles there, 1 meaning that it's a heterozygote, 2 mean there are two reference alleles in that individual. OK?**

**So there are different ways of representing genotype, but once again, it represents the different allelic forms of the two chromosomes. And whatever form you choose, the probability over those genotypes has to sum to 1. You can think about the genotype ranging over all the possible bases from mom and from dad or over 0, 1, and 2. Doesn't really matter, depending upon which way you want to simplify the problem.**

**And what we would like to do is, for a given population-- let's say cases or controls-we'd like to compute the probability over the genotypes with high veracity, OK? So in order to do that, we'll start by taking all the reads for each one of the individuals in a population, OK? And we're going to compute the genotype likelihoods for each individual. So let's talk about how to do that.**

**Now everything I've written on the board is on the next slide. The problem is, if I put it on the slide, it will flash in front of you and you'll go, yes, I understand that, I think. This way, I'll put it on the board first and you'll look at it and you'll say, hm, maybe I don't understand that, I think. And then you'll ask any questions and we can look at**

19

**the slide in a moment, OK? But here's the fundamental idea, all right? At a given base in the genome, the probability of the reads that we see based upon the genotype that we think is there can be expressed in the following form, which is that we take the product over all the reads that we see, OK? And the genotype is going to be a composition of the base we get from mom and the base that we get from dad, or it could simply be 0, 1, and 2. We'll put that aside for a moment.**

**So what's the chance that we inherited something from a particular base from mom? It's this base over a particular read. What's the chance a particular read came from mom's chromosome? That's one half times the probability of the data given the base that we see. And once again, since it could be a coin flip whether the read came from mom or dad's chromosome, divide it by 2-- the probability of the data that we see with dad's version of that particular base.**

**So once again, for all the reads we're going to compute the probability of the read set that we see given a particular hypothesized genotype by looking at what's the likelihood or the probability of all those reads. And for each read, we don't know if it came from mom or from dad. But in any event, we're going to compute the probability on the next blackboard, this bit right here. OK? Yes?**

**AUDIENCE: So if you assume that mom and dad have a different phase at a particular base, couldn't that possibly skew the probability of getting a read from mom's chromosome or dad's chromosome?**

**PROFESSOR: A different phase?**

**AUDIENCE: So the composition of bases affect what you get. I think certain base compositions are more likely to be sequenced, for example.**

**PROFESSOR: Yes.**

**AUDIENCE: Could that bias--**

**PROFESSOR: Yes. In fact, that's why on, I think, the third slide, I said non-random genotyping error was being excluded.**

20

---

[← AUDIENCE: A megabase?](04-audience-a-megabase.md) · [Up: contents](index.md) · [AUDIENCE →](06-audience.md)
