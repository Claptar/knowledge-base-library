---
title: and control study.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kyq2dpw5neu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# and control study.

**Source:** `recordings/kyq2dpw5neu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**And then we'll talk about how to use whole genome read data to detect variation between humans and some of the challenges in that, because it does not make as many assumptions as the microarray studies, and therefore is much, much more complicated to process. And so we're going to take a view into the best practices of processing human read data so you can understand what the state of the art is.**

**And then we're going to turn to a study showing how we can bring together different threads we've talked about in this subject. In particular, we've talked about the idea that we can use other genomic signals such as histone marks to identify things like regulatory elements. So we're going to talk about how we can take that lens and focus it on the genome to discover particular genomic variants that have been revealed to be very important in a particular disease.**

**And finally, we'll talk about the idea that what-- the beginning we're going to talk about today is all about correlation. And as all of you go forward in your scientific career, I'm hopeful that you'll always be careful to not confuse association or correlation with causation. You're always respected when you clearly articulate the difference when you're giving a talk saying that this is correlated, but we don't necessarily know it's causative until we do the right set of experiments.**

**OK, on that note, we'll turn to the computational approaches we're going to talk about. We'll talk about contingency tables and various ways of thinking about them when we discuss how to identify whether or not a particular SNP is associated with a disease using various kinds of tests. And then we talk about read data, and we'll talk about likelihood based tests. How to do things like take a population of individuals and their read data and estimate the genotypic frequencies at a particular locus using that data in toto using EM based techniques. OK? So let us begin then.**

**Some of the things we're not going to talk about include non-random genotyping failure, methods to correct for population stratification, and structural variants and copy number variations. Point three we'll just briefly touch on, but fundamentally they're just embellishments on the fundamental techniques we're talking about, and**

2

**so I didn't really want to confuse today's discussion.**

**Now a Mendelian disorder is a disorder defined by a single gene, and therefore, they're relatively easy to map. And they also tend to be in low frequency in the population because they're selected against, especially the more severe Mendelian disorders. And therefore, they correspond to very rare mutations in the population.**

**By point of contrast, if you thought about the genetics we discussed last time, if you think about a trait that actually perhaps is influenced by 200 genes and maybe that one of those genes is not necessary or sufficient for a particular disease. As a consequence, it could be a fairly common variant and it's only if you're unlucky enough to get all the other 199 variants will you actually come down with that syndrome. And therefore, you can see that the effect of variation in the human genome is inversely related to its frequency-- that fairly rare variants can have very serious effects, whereas fairly common variants tend to have fewer effects.**

**And in the first phase of mapping human variation, people thought that common variants were things that had an allelic frequency in the population of 5% or greater. And then to burrow down deeper, the 1000 Genomes Project surveyed a collection of different populations. And therefore, if you thought that a variant was prevalent in the population at frequency of 0.5%, how many people would have in the 1000 Genomes Project roughly? Just make sure among you we're phase-locked here. 0.5%, 1,000 people--**

**AUDIENCE: 5.**

**PROFESSOR: 5, great. OK. Good. Now of course, these are three different populations or more, and so it might be that, in fact, that variant's only present in one of the population. So it just might be one or two people that actually have a particular variant. So the idea is that the way that you design SNP chips to detect single nucleotide polymorphisms, otherwise known as "SNPs," is that you do these population-based sequencing studies and you design the array based upon all of the common variants that you find, OK? And therefore, the array gives you a direct readout in terms of the variation, in terms of all of these common variants. That's where we'll**

3

**start today. And where we'll end today is sequencing based approaches, which make no assumptions whatsoever and just all hell breaks loose. So you'll see what happens, OK?**

**But I wanted just to reinforce the idea that there are different allelic frequencies of variants and that as we get down to rarer and rarer alleles, right, we have larger effects. But these higher frequency alleles could also have effects even though they're much smaller.**

**OK, so let's talk about how these variants arise and what they mean in terms of a small little cartoon. So long, long ago, in a world far, far away, a mutation occurred where a base G got mutated to a base A, OK? And this was in the context of a population of individuals-- all happy, smiling individuals because they all actually do not have a disease. And our story goes, what happens is that we had yet another generation of people who are all happy, smiling because they do not have the disease. Right? Yes, I do tell stories at night, too.**

**And then another mutation occurred. And that mutation caused some subset of those people to get the mutation and for them to get the disease. So the original mutation was not sufficient for people to get this genetic disease. It required a second mutation for them to get the genetic disease, OK? So we got at least two genes involved in it.**

**OK, the other thing that we know is that, in this particular case, some of the people have the disease that don't have this mutation. And therefore, this mutation is not necessary. It's neither necessary nor sufficient. Still, it is a marker of a gene that increases risk. And that's a fundamental idea, right, that you can increase risk without being necessary or sufficient to cause a particular genetic disorder. OK? And so you get this association then between genotype and phenotype, and that's what we're going to go looking for right now. We're on the hunt. We're going to go looking for this relationship.**

**So in certain older individuals-- hopefully, not myself in the future-- what happens is that your maculus, which is the center of your eye, degenerates as shown here. And**

4

**you get this unfortunate property where you can't actually see in the center of your field of vision. It's called age-related macular degeneration. So to look for the causes of this, which is known to be genetically related, the authors of the study collected a collection-- a cohort, as it's called-- of these European-descent individuals, all who are at least 60 years old, to study the genetic foundations for this disorder. And so they found 934 controls that were unaffected by age-related macular degeneration and 1,238 cases, and they genotyped them all using arrays.**

**Now the question is, are any of the identified SNPs on the array related to this particular disorder? So I'll give you the answer first and then we'll talk about a couple of different ways of thinking about this data, OK? So here's the answer. Here's a particular SNP, rs1061170. There are the individuals with AMD and the controls. And what you're looking at up here, these numbers are the allelic counts, all right? So each person has how many alleles? Two, right? That's double the number of individuals. And the question is, are the C and T alleles associated with the cases or controls significantly?**

**And so you can compute a Chi-square metric on this so-called contingency table. And one of the things about contingency tables that I think is important to point out is that you hear about marginal probabilities, right? And people probably know that originally derived from the idea of these margins along the side of a contingency table, right? If you think about the marginal probability of somebody having a C allele, regardless of whether a case or control, it would be 2,192 over 4,344, right?**

**So the formula for computing the Chi-square statistic is shown here. It's this sort of scary-looking polynomial. And the number of degrees of freedom is 1. It's the number of rows minus 1 times the number of columns minus 1. And the P-value we get is indeed quite small-- 10 to the minus 62. Therefore, the chance this happened at random-- even with multiple hypothesis correction, given that we're testing a million SNPs-- is indeed very, very low. This looks like a winner. Looks like we've got a SNP that is associated with this particular disease.**

**Now just to remind you about Chi-square statistics-- I'm sure people have seen this**

5

**before-- the usual formulation is that you compute this Chi-square polynomial on the right-hand side, which is the observed number of something minus the expected number of something squared over the expected number or something, right? And you sum it up over all the different cases. And you can see that the expected number of As is given by the little formula on the left. Suffice to say, if you expand that formula and manipulate it, you get the equation we had on the previous slide. So it's still that fuzzy, friendly Chi-square formula you always knew, just in a different form, OK?**

**Now is there another way to think about computing the likelihood of seeing data in a contingency table at random, right? Because we're always asking, could this just be random? I mean, could this have occurred by chance, that we see the data arranged in this particular form? Well, we've another convenient way of thinking about this, which is we could do Fisher's Exact Test, which is very related to the idea of the hypergeometric test that we've talked about before, right? What are the chances we would see exactly this arrangement?**

**Well, we would need to have, out of a plus b C alleles, we'd have 8 of them be cases, which is the first term there in that equation. And of the T alleles, we need to have c of them out of c plus d be there. And then we need to have a plus b plus c plus d choose a plus c-- that's the total number of chances of seeing things. So this is the probability of the arrangement in the table in this particular form. Now people- I'll let you digest that for one second before I go on.**

**So this is the number of ways on the numerator of arranging things to get the table the way that we see it over the total number or ways of arranging the table, keeping the marginal totals the same. Is that clear? So this is the probability, the exact probability, of seeing the table in this configuration. And then what you do is you take that probability and all of the probabilities for all the more extreme values, say, of a. And you sum them all up and that gives you the probability of a null hypothesis. So this is another way to approach looking at the chance a particular contingency table set of values would occur at random.**

6

**So if people talk about Fisher's Exact Test-- you know, tonight at that cocktail party. "Oh yeah, I know about that. Yeah, it's like the hypergeometric. It's no big deal." You know? Right.**

**All right. So now let us suppose that we do an association test and you do the following design. You say, well, I've got all my cases. They're all at Mass General and I want to genotype them all. And Mass General is the best place for this particular disease, so I'm going to go up there. I need some controls but I'm running out of budgetary money, so I'm going to do all my controls in China, right? Because I know it's going to be less expensive there to genotype them.**

**And furthermore-- as a little aside, I was once meeting with this guy who is like one of the ministers of research in China. He came to my office. I said, so what do you do in China? And he said, well, I guess the best way to describe it is that I'm in charge of the equivalent of the NSF, DARPA, and the NIH. I said, oh. I said, would like to meet the president? Because I'd be happy to call MIT's president. I'm sure they'd be happy to meet with you. He said, no. He said, I like going direct. So, at any rate, I told him I was working in stem cell research. He said, you know, one thing I can say about China-- in China, stem cells, ethics, no problem.**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[LAUGHTER] →](03-laughter.md)
