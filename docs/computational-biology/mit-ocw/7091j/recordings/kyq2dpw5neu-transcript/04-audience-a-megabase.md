---
title: 'AUDIENCE: A megabase?'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kyq2dpw5neu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: A megabase?

**Source:** `recordings/kyq2dpw5neu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**A megabase. Little low. How many centimorgans long is the human genome? All right? Anybody know? 3,000? 4,000? Something like that? So maybe 50 to 100 megabases between crossover events, OK? So if these markers are very closely organized along the genome, the likelihood of a crossover is very small. And therefore, they're going to be in very high LD, right? And a way to measure that is with the following formula, which is that if you link the two locuses-- we have L1 and L2 here. And now we're talking about the population instead of a particular individual. If the likelihood of the capital allele A is piece of A and the probability of the big B allele is piece of B, then if they were completely unlinked, then the likelihood of inheriting both of them together with would be piece of A times piece of B, showing independence.**

**However if they aren't independent, we can come up with a single value D which allows us to quantify the amount of disequilibrium between those two alleles. And the formula for D is given on the slide. And furthermore, if it's more convenient for you to think about in terms of r-squared correlation, we can define the r-squared correlation as D squared over PA, QA, PB, QB, as shown in the lower left hand part of this slide, OK? This is simply a way of describing how skewed the probabilities are from being independent for inheriting these two different loci in a population. Are there any questions at all about that, the details of that? OK.**

**So just to give you an example, if you look at chromosome 22, the physical distance on the bottom is in kilobases, so that's from 0 to 1 megabase on the bottom. And you look at the r-squared values, you can see things that are quite physically close, as we suggested earlier, have a high r-squared value. But there are still some things that are pretty far away that have surprisingly high r-squared values. There are recombination hot spots in the genome. And it's, once again, a topic of current**

9

**research trying to figure out how the genome recombines and recombination is targeted. But suffice it to say, as you can see, it's not uniform.**

**Now what happens as a consequence of this is that you get regions of the genome where things stick together, right? They're all drinking buddies, right? They all hang out together, OK? But here's what I'm going to ask you-- how much of your genome came from your dad? Half. How much came from your dad's dad?**

**AUDIENCE: A quarter.**

**PROFESSOR: And from your dad's dad's dad?**

**AUDIENCE: An eighth.**

**PROFESSOR: An eighth, OK? So the amount of your genome going back up the family tree is falling off exponentially up a particular path, right? So if you think about groups of things that came together from your great, great grandfather or his great, great grandfather, right, the further back you go, the less and less contribution they're going to have to your genome. And so the blocks are going to be smaller-- that is, the amount of information you're getting from way back up the tree.**

**So if you think about this, the question of what blocks of things are inherited together is not something that you can write an equation for. It's something that you study in a population. You go out and you ask, what things do we observe coming together? And generally, larger blocks of things are inherited together, occur in more recent generations, because there's less dilution, right? Whereas if you go way back in time-- not quite to where the dinosaurs roamed the land, but you get the idea-- the blocks are, fact, quite small.**

**And so, the HapMap project went about looking at blocks and how they were inherited in the genome. And what suffices to know is that they found blocks-- here you can see three different blocks. And these are called haplotype blocks and the things that are colored red are high r-squared values between different genetic markers. And we talked earlier about how to compute that r-squared value. So those blocks typically are inherited together. Yes?**

10

**AUDIENCE: Are these blocks like fuzzy boundaries?**

**PROFESSOR:**

**No. Well, remember in this particular example, we're only querying at specified markers which are not necessarily at regular intervals along the genome. So in this case, the blocks don't have fuzzy boundaries. As we get into sequencing-based approaches, they could have fuzzier boundaries. But haplotype blocks are typically thought to be discrete blocks that are inherited, OK? Good question. Any other questions? OK.**

**So I want to impress upon the idea that this is empirical, right? There's no magic here in terms of fundamental theory about what things should be haplotype blocks. It's simply that you look at a population and you're look at what markers are drinking buddies and those make haplotype blocks and you empirically categorize and catalog them-- which can be very helpful, as you'll see.**

**And thus, when we think about genetic studies, when we think about the length of shared segments, if you're thinking about studying a family, like a trio-- a trio is a mom, a dad, and a child, right? They're going to share a lot of genetic information, and so the haplotype blocks that are shared amongst those three individuals are going to be very large indeed. Whereas if you go back generations, the blocks-- like the second cousins or things like that-- the blocks get smaller. So the x-axis on this plot is the median length of a shared segment. And as an association study, which is taking random people out of the population, has very small shared blocks indeed, OK? And so the techniques that we're talking about today are applicable almost in any range, but they're particularly useful where you can't depend upon the fact that you're sharing a lot of information along the genome proximal to where the marker is that's associated with a particular disease.**

**Now the other thing that is true is that we should note that the fact that markers have this LD associated with them means that it may be that a particular marker is bang on-- what's called a causative SNP. Or something that, for example, sits in the middle of a gene causing a missense mutation. Or it sits right in the middle of a protein binding site, causing the factor not to bind anymore. But also it could be**

11

**something that is actually a little bit away, but is highly correlated to the causative SNP. So just keep in mind that when you have an association and you're looking at a SNP, it may not be the causative SNP. It might be just linked to the causative SNP. And sometimes these things are called proxy SNPs.**

**OK, so we've talked about the idea of SNPs and discovering them. Let me ask you one more question about where these SNPs reside and see if you could help me out. OK, this is a really important gene, OK? Call it RIG for short, OK? Now let us suppose that you know that there are some mutations here. And my question for you is, does it matter whether or not the two mutations look like this or the mutations look like this, in your opinion?**

**That is, both mutations occur in one copy or on one chromosome of the gene, whereas in the other case, we see two different SNPs that are different than reference, but they're referring in both mom and dad alleles. Is there a difference between those two cases? Yeah?**

**AUDIENCE: In terms of the phenotype displayed?**

**PROFESSOR: In terms of the phenotype, sorry.**

**AUDIENCE: It depends.**

**PROFESSOR: It depends?**

**AUDIENCE: Yes.**

**PROFESSOR: OK.**

**AUDIENCE: So if it causes a recessive mutation, then no, because other genes will be able to rescue it. But if it's dominant, then it'll still--**

**PROFESSOR: It's actually the other way around. If it's recessive, this does matter.**

**AUDIENCE: Oh, I see.**

**PROFESSOR: Because in this case, with the purple ones, you still have one good copy of the**

12

**gene, right? However, with the green ones, it's possible that you have ablated both good copies of the gene, this really important gene, and therefore, you're going to get a higher risk of having a genetic disorder. So when you're scanning down the genome then-- you know, we've been asking where are there differences from reference or from between cases and controls down the genome, but we haven't asked whether or not they're on mom or dad, right? We're just asking, are they there?**

**But it turns out that for questions like this, we have to know whether or not the mutation occurred in only in mom's chromosome or in both chromosomes in this particular neighborhood, all right? This is called phasing of the variants. Phasing means placing the variants on a particular chromosome. And then, by phasing the variants, you can figure out some of the possible phenotypic consequences of them. Because if they're not they phased, in this case, it's going to be much less clear what's going on.**

**So then the question becomes, how do we phase variants, right? So phasing assigns alleles to the parental chromosomes. And so, the set of alleles along a chromosomes is a haplotype. We've talked about the idea of haplotypes. So imagine one way to phase is that if I tell you, by magic, in this population you're looking at, here are all the haplotypes and these are the only ones that exist. You look in your haplotypes and you go, aha, this haplotype exists but this one does not, right? That this is a haplotype-- this two purples together is a haplotype, and this green without one is another haplotype. So you see which haplotypes exist-- that is, what patterns of inheritance of alleles along a chromosome you can detect. And using the established empirical haplotypes, you can phase the variants, OK?**

**Now the other way to phase the variants is much, much simpler and much better, right? The other way to phase variants is you just have a single read that covers the entire thing, right? And then the read, it will be manifest, right? The read will cover the entire region and then you see the two mutations in that single region of the genome. The problem we're up against is that most of our reads are quite short and we're reassembling our genotypes from a shattered genome. If the genome wasn't**

13

**shattered, then we wouldn't have this problem.**

**So everybody's working to fix this. Illumina has sort of a cute trick for fixing this. And PacBio, which is another sequence instrument manufacturer, can produce reads that are tens of thousands of bases long, which allows you to directly phase the variants from the reads. But if somebody, once again, comes up to you at the cocktail party tonight and says, you know, I've never understood why you have to phase variants. You know, this is a popular question I get all the time.**

---

[← [LAUGHTER]](03-laughter.md) · [Up: contents](index.md) · [[LAUGHTER] →](05-laughter.md)
