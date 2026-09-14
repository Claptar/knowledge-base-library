---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/zyw2aede6wu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/zyw2aede6wu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=ZYW2AeDE6wU**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: Well, welcome back to computational systems biology. We're back here today talking about genome assembly. How many people have ever assembled a genome before? In your spare time? Anybody done any genome assembly here? One person?**

**I think genome assembly is a fascinating topic. And as you know, it's at the bedrock of all modern biology. We rely upon genome references for almost everything in terms of studying evolution, looking at the structure of genes, regulation of genes, differences between individuals. So it's really a very fundamental concept.**

**And we're going to talk today about two different ways of assembling genomes. And I think one of the takeaway messages from today's lecture is going to be that genome assembly is more of an art, in some sense, than a science. And one has to always be a little bit suspicious of a genome assembly given what you're about to learn today.**

**And, of course, genome assembly is becoming even more complex because it used to be that assembling the human genome was the big task scientifically in front of the community. But now there are billions of genomes waiting to be sequenced-- all the individuals in the world and to try and interpret them. And now you can get your genome sequence for between $5,000 and $10,000. How many people here are tempted to get their genome sequenced?**

**OK, I see about five hands-- six hands. Great. So let's look at the science behind genome assembly. The basic concept is that we're going to collect some sequence reads from the genome. And we're going to assemble them know what are called contigs for contiguous segments. And these represent uninterrupted portions of the**

1

**genome that are completely covered by reads that we believe are contiguous.**

**These contigs then will be paired together in scaffolds. And scaffolds are like contigs except that there are missing parts between the contigs in a scaffold. We don't know what those parts are. But we're able to actually glue them together by using read pairs that allow us to jump over the missing parts because we have read both ends of a molecule. But we don't know what's in the middle.**

**And then oftentimes we had physical mapping technologies where we actually can go back and assign location scaffolds to physical locations on chromosomes by using PCR sequences like sequence tag sites that physically locate a particular sequence identity to a physical location on a particular chromosome. And that provides us with a total genome map.**

**So today we're going to be talking about how to go from a hard drive full sequence reads all the way down to a set of scaffolds that include assembled contigs. And the way to think about this once again is that we start with conceptually a single copy of the genome. We amplify this. And in order to sequence it on contemporary instruments, we have to fragment it.**

**Now for those of you who were in last Friday's recitation, you heard Heng Li talking about the idea that sequence reads are getting longer. In fact, sequence reads up to 10 to 15 kilobases are now possible. And sequence reads even longer than that are going to be possible, which will greatly simplify the assembly process. But for now we're talking about the challenge of assembling short reads-- say 100 base pair reads off of contemporary sequencing instruments.**

**So we take the fragmented reads and the notion is that we know that they're going to align up like a puzzle. And all we have to do is line the reads up to recover the read sequence at the bottom-- the original genome sequence. And I should add that many of the illustrations in today's lecture are from Ben Lagmi. He was kind enough to allow me to use them for today's talk.**

**So the goal is to come up with that red sequence at the bottom from the original set**

2

**of reads but, of course, the read set that we're talking about is perhaps 200 million reads or even a billion reads as we'll see. And so it's quite a tough task to put pieces together given that we really don't know where they came from. And we don't know where they align because we don't have the red part to guide us.**

**Now today we're going to be talking about what's called de novo assembly. That means starting from scratch. You hand me your set of reads for your favorite organism. And we're going to assemble it today. That's different than what's called reference-guided assembly because, for example, if you're going to re-sequence me or you, there is a reference human genome. And it would be a simple matter to take the reads from you or I and map them back onto the reference genome as a guide to trying to reassemble our genomes.**

**However, as you can tell, if there's a large structural variation between the reference genome and our genomes, that process can fail. So we're going to be talking today about de novo assembly. And in the process of de novo assembly, oftentimes we talk about coverage, which is on average how many sequencing bases do we have for every base of the genome. Here we have for this little illustrative example coverage of about 7x.**

**Now, at the origin of the Human Genome Project, some calculations were done about how much coverage was required to cover the human genome. And we talked last time about library complexity. This is a slightly different idea, which is we want to estimate the probability the base is uncovered. So if we have the genome size as G and the number of reads as N and L is the length of a read, then N times L is the total number bases that we have. And that divided by the genome is the average coverage of a base.**

**And probably the probability that a base is not covered is the probability we're going to observe zero reads to that base, which is e to the minus lambda, roughly speaking, if we use a Poisson approximation. And therefore, the number of uncovered bases it will have is going to be roughly G times e to the minus lambda.**

**The next calculations can be thought intuitively as the following way, which is if we**

3

**have N reads, if there's going to be a gap after a read, there has to be an uncovered base after it. And so the number of gaps we're going to have in our assembly is roughly N times e to the minus lambda.**

**So this is a back of the envelop calculation. And now if we take some of our 1,000 genomes data, which we previously used and asked how well this approximation works, we see something like this where the x-axis is the total number of reads and the genome coverage in bases is shown on the y-axis. And these are all different sequencing experiments.**

**So you can see there the roughly green outline, which follows the approximately what we saw before in this Lander-Waterman rule. Could somebody tell me what they think is going on with the red lines that actually don't match up with that green line? Anybody have any ideas about why we need more reads out of those libraries to get better coverage? Yes?**

**AUDIENCE: There is probably some bias when you're amplifying them?**

**PROFESSOR: Yeah, there's probably skew in the original libraries we talked about last time. In fact, we talked about last time why the Poisson was not a great approximation for looking at libraries. And in fact, we might want to fit something like a negative binomial in this particular case.**

**So we've got our read set. And we can also talk about coverage at a particular base, which is different than average coverage just to be clear that there are two different kinds of coverage that one can think about. Here we see coverage at T of level six. And the other thing that we need to be cognizant of is that there are two reasons that we might-- two common reasons why we might actually see reads that overlap but don't agree at all positions.**

**The obvious reason is that there's an error in one of the reads. We get quality scores and so forth. And that can help us decide which is the truth. But the other possibility is that as you know, you have one of each of your chromosomes from mom one from your dad. And there could be allelic differences between these**

4

---

[Up: contents](index.md) · [chromosomes. →](02-chromosomes.md)
