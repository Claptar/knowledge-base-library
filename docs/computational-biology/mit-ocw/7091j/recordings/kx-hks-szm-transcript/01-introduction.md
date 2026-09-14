---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kx-hks-szm-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/kx-hks-szm-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=kx_Hks_-SZM**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: So as you recall last time we talked about chromatin structure and chromatin regulation. And now we're going to move on to genetic analysis. But before we did that, I want us to touch on two points that we talked about briefly last time.**

**One was 5C analysis. Who was it that brought up-- who was the 5C expert here? Anybody? No? Nobody wants to own 5C. OK.**

**But as you recall, we talked about ChIA-PET as one way of analyzing any to any interactions in the way that the genome folds up and enhancers talk to promoters. And 5C is a very similar technique.**

**I just wanted to show you the flow chart for how the protocol goes. There is a cross linking. A digestion with a restriction enzyme step, followed by a proximity ligation step, which gives you molecules that had been brought together by an enhancer, promoter complex, or any other kind of distal protein-protein interaction.**

**And then, what happens is that you design specific timers to detect those ligation events. And you sequence the result of what is known as ligation mediated amplification. So those primers are only going to ligate if they're brought together at a particular junction, which is defined by the restriction sites lining up.**

**So, 5C is a method of looking at which regions of the genome interact and can produce these sorts of results, showing which parts of the genome interact with one another.**

**The key difference, I think, between chIA-PET and 5C is that you actually have to have these primers designed and pick the particular locations you want to query.**

**So the primers that you design represent query locations and you can then either**

1

**apply the results to a microarray, or to high throughput sequencing to detect these interactions.**

**But the essential idea is the same. Where you do proximity based ligation to form molecules that contain components of two different pieces of the genome that have been brought together for some functional reason.**

**The next thing I want to touch upon was this idea of the CpG dinucleotides that are connected by a phosphate bond. And you recall that I talked about the idea that they were symmetric.**

**So you could have methyl groups on the cytosines in such a way that, because they could mirror one another, they could be transferred from one strand of DNA to the other strand of DNA, during cell replication by DNA methyltransferase.**

**So it forms a more stable kind of mark and as you recall, DNA methylation where something occurred in lowly expressed genes and typically in regions of the genome that are methylated. Other histone marks are not present and the genes are turned off.**

**OK. So those were the points I wanted to touch upon from last lecture. Now we're going to embark upon an adventure, looking for the answer to, wear is missing heritability found?**

**So it's a big open question now in genetics. In human genetics, which is that we really can't find all the heritability. And as a point of introduction, the narrative arc for today's lecture is that, generally speaking, you're more like your relatives than random people on the planet.**

**And why is this? Well obviously you contain components of your mom and dad's genomes. And they are providing you with components of your traits. And the heritability of a trait is defined by the fraction of phenotypic variance that can be explained by genetics.**

**And we're going to talk today about computational models that can predict**

2

**phenotype from genotype. And this is very important, obviously, for understanding the sources of various traits and phenotypes. As well as fields such as pharmacogenomics that try and predict the best therapy for a disease based upon your genetic makeup.**

**So, individual loci in the genome that contribute to quantitative traits are called quantitative trait locis, or QTLs. So we're going to talked about how to discover them and how to build models of quantitative traits using QTLs.**

**And finally, as I said at the outset, our models are insufficient today. They really can't find all of the heritability. So we're going to go searching for this missing heritability and see where it might be found.**

**Computationally, we're going to apply a variety of techniques to these problems. A preview is, we're going to build linear models of phenotype and we're going to use stepwise regression to learn these models using a forward feature selection.**

**And I'll talk about what that is when we get to that point of the lecture. We're going to derive test statistics for discovering which QTLs are significant and which QTLs are not, to include in our model.**

**And finally, we're going to talk about how to measure narrow sense heritability and broad sense heritability in environmental variance.**

**OK. So, one great resource for traits that are fairly simple. That primarily are the result of a single gene mutation, or where a single gene mutation plays a dominant role, is something called Online Mendelian Inheritance in Man.**

**And it's a resource. It has about 21,000 genes in it right now. And it's a great way to explore what human genes function is in various diseases. And you could query by disease. You can query by gene. And it is a very carefully annotated and maintained collection that is worthy of study, if you're interested in particular disease genes.**

**We're going to be looking at more complex analyses today. The analyses we're going to look at are where there are many genes that influence a particular trait.**

3

**And we would like to come up with general methods for discovering how we can de novo from experimental data-- discover all the different genes that participate.**

**Now just as a quick review of statistics, I think that we've talked before about means in class and variances. We're also going to talk a little bit about covariances today. But these are terms that you should be familiar with as we're looking today at some of our metrics for understanding heritability.**

**Are there any question about any of the statistical metrics that are up here? OK.**

**So, a broad overview of genotype to phenotype. So, we're primarily going to be working with complete genome sequences today, which will reveal all of the variance that are present in the genome.**

**And it's also the case that you can subsample a genome and only observe certain variance. Typically that's done with microarrays that have probes that are specific to particular markers.**

**The way those arrays are manufactured is that whole genome sequencing is done at the outset, and then high prevalence variance, at least common variance, which typically are at a frequency of at least 5% in the population are queried by using a microarray. But today we'll talk about complete genome sequence.**

**An individual's phenotype, we'll say is defined by one or more traits. And a nonquantitative trait is something perhaps as simple as whether or not something is dead or alive. Or whether or not it can survive in a particular condition. Or its ability to produce a particular substance.**

**A quantitative trait, on the other hand, is a continuous variable. Height, for example, of an individual is a quantitative trait. As is growth rate, expression of a particular gene, and so forth.**

**So we'll be focusing today on estimating quantitative traits. And as I said, a quantitative trait or loci, is a marker that's associated with a quantitative trait and could be used to predict it. And you can sometimes hear about eQTLs, which are**

4

**expression quantitative trait loci. And they're loci that are related to gene expression.**

**So, let's begin then, with a very simple genetic model. It's going to be haploid, which means, of course, there's only one copy of each chromosome. Yeast is the model organism we're going to be talking about today. It's a haploid organism.**

**And we have mom and dad up there. Mom on the left, dad on the right in two different colors. And you can see that mom and dad in this particular example, have n different genes. They're going to contribute to the F1 generation, to junior.**

**And the relative color is white for mom, black for dad, are going to be used to describe the alleles, or the allelic variance that are inherited by the child, the F1 generation.**

**And as I said, a specific phenotype might be alive or dead in a specific environment. And note that I have drawn the chromosomes to be disconnected. Which means that each one of those genes is going to be independently inherited.**

**So the probability in the F1 generation that you're going to get one of those from mom or dad is going to be a coin flip. We're going to assume that they're far enough away that the probability of crossing over during meiosis is 0.5. And so we get a random assortment of alleles from mom and dad. OK?**

**So let us say that you go off and do an experiment. And you have 32 individuals that you produce out of a cross. And you test them, OK. And two of them are resistant to a particular substance.**

**How many genes do you think are involved in that resistance? Let's assume that mom is resistant and dad is not. OK. If you had two that were resistant out of 32, how many different genes do you think were involved? How do you estimate that? Any ideas? Yes?**

**AUDIENCE: If you had 32 individuals and say half of them got it?**

**PROFESSOR: Two, let's say. One out of 16 is resistant. And mom is resistant.**

5

**AUDIENCE: Because I was thinking that if it was half of them were resistant, then you would maybe guess one gene, or something like that.**

**PROFESSOR: Very good. AUDIENCE: So then if only eight were resistant you might guess two genes, or something like that? PROFESSOR: Yeah. What you say is, that if mom's resistant, then we're going to assume that you need to get the right number of genes from mom to be resistant. Right? And so, let's say that you had to get four genes from mom. What's the chance of getting four genes from mom?**

**AUDIENCE: Half to the power of four.**

**PROFESSOR: Yeah, which is one out of 16, right? So, if you, for example had two that were resistant out of 32, the chances are one in 16. Right? So you would naively think, and properly so, that you had to give four genes from mom to be resistant.**

**So the way to think about these sorts of non-quantitative traits is that you can estimate the number of genes involved. The simply is log base 2 over the number of F1s tested over the number of the F1s with the phenotype.**

**It tells you roughly how many genes are involved in providing a particular trait, assuming that the genes are unlinked. It's a coin flip, whether you get them or not. Does everybody see that? Yes? Any questions at all about that? About the details? OK.**

**Let's talk now about quantitative traits then. We'll go back to our model and imagine that we have the same set-- actually it's going to a different set of n genes. We're going to have a coin flip as to whether or not you're getting a mom gene or a dad gene. OK. And each gene in dad has an effect size of 1 over n. Yes?**

**AUDIENCE: I just wanted to check. We're assuming that the parents are homozygous for the**

6

---

[Up: contents](index.md) · [trait? Is that correct? →](02-trait-is-that-correct.md)
