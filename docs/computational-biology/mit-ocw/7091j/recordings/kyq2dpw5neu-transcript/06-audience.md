---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kyq2dpw5neu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/kyq2dpw5neu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Oh.**

**PROFESSOR: Right? From our discussion today? But you're right that it might be that certain sequences are more difficult to see, but we're going to exclude that for the time being. OK?**

**So this is the probability of the reads that we see given a hypothesized genotype. And I'll just show you, that's very simple. That we have a read, let's call the read D sub j, and we have the base that we think we should see. And if the base is correct, then the probability that that's correct is 1 minus the error, right, that the machine reported. And if it isn't correct, the probability is just the error at that base that the machine reported. So we're using the error statistics from the machine and if it matches what we expect, it's 1 minus the error. And if it doesn't match, it's just simply going to be the error that's reported, OK?**

**So this is the probability of seeing a particular read given a hypothesized base that should be there. Here's how we use that, looking at all the possible bases that could be there given a hypothesized genotype. Remember, this genotype is only going to be one pair. It's only going to be AA or TT or what have you, right? So it's going to be one pair. So we're going to be testing for either one or two bases being present.**

**And finally, we want to compute the posterior of the genotype given the data we have observed, OK? So we want to compute what's the probability of the genotype given the reads that we have in our hand. This is really important. That is what that genotype likelihood is up there. It's the probability of the read set given the genotype times the probability of the genotype-- this is a prior-- over the probability of the data. This is simply Bayes' Rule. So with this, for an individual now, we can compute the posterior of the genotype given the read set. Very simple concept.**

**So in another form, you can see the same thing here, which is the Bayesian model. And we've talked about this haploid likelihood function, which was on the blackboard I showed you. And we're assuming all the reads are independent and that they're going to come equally from mom and dad, more or less, et cetera, OK? And the haploid likelihood function, once again, just is using the error statistics for the**

21

**machine. So I'm asking if the machine says this is an A and I think it's an A, then the probability that that's correct is 1 minus the error of the machine. If the two are not in agreement, it's simply the error in the machine that I'm using.**

**So this allows me now to give a posterior probability of a genotype given a whole bunch of reads. And the one part that we haven't discussed is this prior, which is how do we establish what we think is going on in the population and how do we set that? So if you look back at the slide again, you can see that we have these individuals and there's this magic step on the right-hand side, which is that somehow we're going to compute a joint estimate across all the samples to come up with an estimate of what the genotypes are in a particular SNP position.**

**And the way that we can do that is with an iterative EM procedure-- looks like this-so we can estimate the probability of the population genotype iteratively using this equation until convergence. And there are various tricks. As you'll see if you want to delve further into this in the paper I posted, there are ways to deal with some of the numerical issues and do allele count frequencies and so forth. But fundamentally, in a population we're going to estimate a probability over the genotypes for a particular position.**

**And just to keep it simple, you can think about the genotypes being 0, 1, or 2-- 0, no reference alleles present; 1, one reference allele present to that site; 2, two reference alleles present to that site, OK? So we get a probability of each one of those states for that population. Any questions at all about that? The details or anything at all? People get the general idea that what we're just doing is we're taking a bunch of reads at a particular position for an individual and computing the posterior probability of a genotype seeing all of those reads and then, when we think about the entire population-- say either the cases or the controls-- we're computing the probability over the genotypes within that population using this kind of iterative procedure.**

**OK, so going on then, if we go back to our 0, 1, 2 kind of genotype representation, we can marginalize psi, which is the probability of the reference allele being in the**

22

**population, and 1 minus psi being the probability of the non-reference allele, where the capital alleles are reference and the little ones are non-reference. And then we could also for epsilon 0, epsilon 1, And Epsilon 2, those are the probabilities of the various allelic forms, the various genotypes. And actually, I think epsilon 0 should be little A, little A. Must have got the two of them flipped, but it's not really that important.**

**OK, so what do we know about a population? Who's heard about Hardy-Weinberg before? Hardy-Weinberg equilibrium? OK. So Hardy-Weinberg equilibrium says that, for example, in a population, if the allelic frequency of the reference allele is psi, right, what's the chance that an individual should be AA, big A, big A, reference, reference? In a population? Pardon? I think I heard it. Psi squared, right? We're going to assume diploid organisms, we're going to assume random mating, we're going to assume no selection, we're going to assume no bottlenecks, and so forth, right? That over time, the population will come to its equilibrium in the exchange of alleles.**

**However, if there's strong selection or if part of the population gets up and moves to a different continent or something of that sort, you can get out of equilibrium. And so one question, whenever you're doing a genetic study like this-- is your population in equilibrium or not? And we have a direct way for testing for that because we're actually estimating the genotypes, right?**

**So what we can do is this test. We can do a log likelihood test directly, right? And we can compare the probability of the observed genotypes-- these are E1 and E2, where the number indicates the number of reference copies-- over the probability of the genotypes being composed directly from the frequency of the reference allele. And this will tell us whether or not these are concordant or not. And if the Chisquare value is large enough, we're going to say that this divergence couldn't have occurred at random and therefore the population is not in equilibrium.**

**And you might say, well, gee, why do I really care if it's in equilibrium or not? I mean, you know, what relevance does that have to me when I'm doing my test?**

23

**Well, here's the issue. The issue is this-- you're going to be testing whether or not genotypes are different between a case and a control population, let's say, OK? And you have a couple different tests you can do. The first test is the test on the top and the second test is the test on the bottom. Let's look at the test on the bottom for a moment, OK?**

**The test in the bottom is saying you consider the likelihood of the data in group one and group two multiplied together over the probability of the data with the groups combined and you ask whether or not the increased likelihood-- you're willing to pay for that given the two degrees of freedom that model implies, right? Because you have to have two additional degrees of freedom to pay for that in the bottom.**

**On the other hand, in the top, you only have one degree of additional freedom to pay for the difference in simply the reference allele frequency. And so these are two different metrics you can use to test for associations for a particular SNP in two different case and control populations. The problem comes is that if the population is in equilibrium, then the bottom has too many degrees of freedom, right? Because the bottom, in some sense, can be computed directly from the top. You can compute the epsilons directly from the size if it's in equilibrium. So you need to know whether or not you're in equilibrium or not to figure out what kind of test to use to see whether or not a particular SNP is significant.**

**OK, so just a brief review where we've come to at this point. I've handed you a basket of reads. We're focusing on a particular location in the genome. For an individual, we can look at that basket of reads and compute a posterior probability of the genotype at that location. We then asked if we take all of the individuals in a given interesting population, like the cases, we could compute the posterior or the probability of the genotype over all those cases. We then can take the cases and the controls and test for associations using this likelihood ratio, OK? So that is the way to go at the question of SNPs. And I'll pause here and see if there any other questions about this.**

**OK, now there are lots of other ways of approaching structural variation. I said I**

24

**would touch upon it. There is another method which is-- we've not been here assigning what haplotypes to things or paying attention to which chromosome or mom or dad a particularly allele came from. But suffice to say-- I'll let you read this slide at your leisure-- the key thing is that, imagine you have a bunch of reads. What you can do in a particular area there's going to be a variant is you can do local assembly of the reads. We want to do local assembly because local assembly handles general cases of structural variation.**

**And if you then take the most likely cases of the local assembly supported by reads, you have the different possible haplotypes or collections of bases along the genome from the assembly. And we've already talked about, earlier in class, how to take a given sequence of bases and estimate the probability of the divergence from another string. So you can estimate the divergence of each one of those assemblies from the reference and compute likelihoods, like we did before for single bases, although it's somewhat more complex.**

**And so another way to approach this is, instead of asking about individual bases and looking at the likelihood of individual bases, you can look at doing localized assembly of the reads that handle structural variation. And if you do that, what happens is that you can recover INDEL issues that appear to call SNP variants that actually are actually induced by insertions and deletions in one of the chromosomes. So as you can see, as things get more sophisticated in the analysis of human genome data, one needs a variety of techniques, including local assembly, to be able to recover what's going on. Because of course, the reference genome is only an approximate idea of what's there and is being used as a scaffold.**

**So we've already talked about the idea of phasing, and we talked about why phasing is important, especially when we're trying to recover whether or not you have a loss of function event, right? And so the phasing part of genomics right now is highly heuristic, relies partly upon empirical data from things like the HapMap Project and is outside the scope of what we're going to talk about, because we could talk about phasing for an entire lecture. But suffice it to say, it's important.**

25

**And if you look at what actually goes on, here's a trio, mom, dad, and the daughter. You can see down at the bottom, you see mom's reads. And you see dad actually has two haplotypes. He got one haplotype from one of his parents and the other haplotype from both of his parents. And then the daughter actually has the haplotype number one from dad and no haplotype number one from mom. So you can see how these blocks of mutations are inherited through the generation in this form.**

**And finally, if you look at a VCF file, if you see a vertical bar, that's telling you that the chromosomal origin is fixed. So it tells you, for example, in this case, the one where the arrow's pointed to is that variant number one, which is the alternative variant T came from mom and a T came from dad. So VCF, when it has slashes between the two different alleles of a genotype is unphased, but you can actually have a phased VCF version. And so there's a whole phase in the GATK tool kit that does phasing.**

**And finally, we get through all this, the question is how important are the variants you discover? And so there's a variant analysis phase and it will go through and annotate all the variants. For example, this is a splice site acceptor variant which is in a protein coating gene and it's thought to be important. And so at the end of this pipeline, what's going to happen is you're going to be spitting out not only the variants but, for some of them, what their annotated function is.**

**OK, so that ends the part of our lecture where we're talking about how to process raw read data. And I encourage you to look at the GATK and other websites to actually look at the state of the art. But as you can see, it's an evolving discipline that has a kernel of principal probabilistic analysis in part of its core surrounded by a whole lot of baling wire, right, to hold it all together. And you get the reads marshalled, organized, compressed, aligned properly, phased, and so forth, OK?**

**Let's talk now about how to prioritize variants. And I just wanted to show you a very beautiful result that is represented by this paper, which came out very recently. And here is a portion of the genome. And we're looking here at-- you see here-- a**

26

**pancreatic disorder. And there is an enhancer on the right-hand side of the screen where that little red square is.**

**And recall that we said that certain histone marks were present typically over active enhancers. And so you can see the H3K4 mono-methyl mark being present over that little red box as well as the binding of two pancreatic regulators, FoxA2 and Pdx1. And within that enhancer you can see there are a whole lot of variants being called. Well, not a whole lot. There are actually five different variants being called. And in addition to those five specific SNP variants, there's also another variation that was observed in the population of a 7.6-kb deletion right around that enhancer. And if you look at the inheritance of those mutations with disease prevalence, you can see that there's a very marked correlation. That when you inherit these variants, you get this Mendelian disorder. So it's a single gene disorder really.**

**And in order to confirm this, what the authors of this study did was they took that enhancer and they looked at all the different SNPs and they mutated it. And in the upper left-hand corner, you can see that the five little asterisks note the decrease in activity of that enhancer when they mutated the bases indicated at SNP positions. The three C's on the panel on the right with the y-axis being relative interaction shows that that enhancer is interacting with the promoter of that gene. And they further elucidated the motifs that were being interacted with and the little arrows point to where the mutations in those motifs occur. So they've gone from an association with that particular disease to the actual functional characterization of what's going on.**

**I'll leave you with a final thought to think about. This is the thing that caused the brawls in the bars I told you about at the beginning of today's lecture. Let's suppose you look at identical twins, monozygotic twins, and you ask the following question. You say, OK, in monozygotic twins, the prevalence of a particular disease is a 30% correlative. That is, if one individual in a twin has the disease, there's a 30% chance that the other twin's going to get it. Now there are two possibilities here, which is that for all pairs of twins, there's a very low risk that you're going to get it, or that there are some subset of genotypes where if one twin has it, the other one's always**

27

**going to get it.**

**So the author of the study actually looked at a block of identical twin data and asked two questions. The first was if you look at the percentage of cases that would test positive, making no assumptions about genotype, using twin data, you can see the percentage of people that actually have a disease that will test positive is actually fairly low for a wide variety of diseases. All these diseases were studied in the context of identical twins. And this suggested to them that, in fact, personal genomic sequencing might not be as predictive as one might like. That is, if you have a disease, for over half of these, the test will not be positive. And furthermore, if you test negative for the disease, your relative risk-- that is, the chance you're going to get this disease to the chance you get it at random in the population-- is not really reduced that much.**

**And so, since this study relied solely on twin data and didn't make any other assumptions, it raised the question in the field of to what extent is personal genome sequencing going to be really helpful? So on that note, we've talked a lot today about the analysis of human genetic variation. I hope you've enjoyed it. Once again, on Thursday we have Ron Weiss coming. Thank you very much. This concludes lecture 20 of the formal material in the course and we'll see you in lecture. Thank you very much.**

28

---

[← [LAUGHTER]](05-laughter.md) · [Up: contents](index.md)
