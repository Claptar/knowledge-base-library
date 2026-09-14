---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kx-hks-szm-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/kx-hks-szm-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**N + 1?**

**PROFESSOR: N + 1, right, because you can either inherit zero, or up to n genes from dad. And it gets you n plus 1 different levels. OK.**

**So, what's the probability then-- well, I'll ask a different question. What's the expected value of the quantitative phenotype of a child? Just looking at this.**

**If dad's one and mom's zero, and you have a collection of genes and you do a coin flip each time, you're going to get half your genes from mom and half your genes from dad. Right.**

**And so the expected trait value is 0.5. So for these added traits, you're going be at the midpoint between mom and dad. Right. And what is the probability that you inherit x copies of dad's genes?**

**Well, that's n choose x, times 1 minus .5 n to the minus x times 0.5 to the x. A simple binomial. Right. So if you look at this, the probability of the distribution for the children is going to look something like this, where this is the mean, 0.5.**

**And the number of distinct values is going to be n plus 1. Right. So the expected value of x is 0.5 and turns out that the expected value, or the variance of x minus 0.5, which is the mean squared, is going to be 0.25 over n.**

8

**So I can show you this on the next slide. So you can see, this could be ethanol production, it could be growth rate, what have you. And you can see that the number of genes that you're going to get from dad follows this binomial distribution and gives you a spread of different phenotypes in the child's generation, depending upon how many copies of dad's genes that you inherit.**

**But does this make sense to everybody? Now would be a great time to ask any questions about the details of this. Yes?**

**AUDIENCE: Can you clarify what x is? Is x the fraction of genes inherited-PROFESSOR: The number of genes you inherit from dad. The number of genes. So it would zero, one, two, up to n.**

**AUDIENCE: Shouldn't the expectation of n [INAUDIBLE] x be n/2?**

**PROFESSOR: I'm sorry. It is supposed to be n/2. But the last two expectations are some of the number of genes you've inherited from dad. Right, that's correct. Yeah, this slide's wrong. Any other questions? OK.**

**So this is a very simple model but it tells us a couple of things, right. Which is that as n gets to be very large, the effect of each gene gets to be quite small.**

**So something could be completely heritable, but if it's spread over, say 1,000 genes, then it will be very difficult to detect, because the effect of each gene would be quite small. And furthermore, the variance that you see in the offspring will be quite small as well, right, in terms of the phenotype. Because it's going to be 0.25/n in terms of the expected value.**

**So as n gets larger, the number genes that contribute to that phenotype increase, the variance is going to go down linearly. OK. So we should just keep this in mind as we're looking at discovering these sort of traits and the underlying QTLs that can be used to predict them.**

**And finally, I'd like to point out one other detail which is that, if genes are linked, that is, if they're in close proximity to one another in the genome and it makes it very**

9

**unlikely there's going to be crossing over between them, then they're going to act as a unit. And if they act as a unit, then we'll get marker correlation. And you can also see, effectively, that the effect size of those two genes is going to be larger.**

**And in more complicated models, we obviously wouldn't have the same effect size for each gene. The effect size might be quite large for some genes, might be quite small for some genes. And we'll see the effects of marker correlation in a little bit.**

**So the way we're going to model this is we're going to-- this is a definition of the variables that we're going to be talking about today. And the essential idea is quite simple.**

**So the phenotype of an individual-- so p sub i is the phenotype of an individual, is going to be equal to some function of their genotype plus an environmental component. This function is the critical thing that we want to discover.**

**This function, f, is mapping from the genotype of an individual to its phenotype. And the environmental component could be how well something is fed, how much sunlight it gets, things that can greatly influence things like growth but they're not described by genetics.**

**But this function is going to encapsulate what we know about how the genetics of a particular individual influences a trait. And thus, if we consider a population of individuals, the phenotypic variance is going to be equal to the genotypic variance plus the environmental variance plus two times the covariance between the genotype in the environment.**

**And we're going to assume, as most studies do, that there is no correlation between genotype and environment. So this term disappears. So what we're left with is that the observed phenotypic variance is equal to the genotypic variance plus the environmental variance.**

**And what we would like to do is to come up with a function f, that best predicts the genotypic component of this equation. There's nothing we can do about**

10

**environmental variance. Right. But we can measure it. Does anybody have any ideas how we could measure environmental variance? Yes?**

**AUDIENCE: Study populations in which there's some kind of controlled environment. So you study populations that one population is one with a homogeneous. And another one was a completely different one.**

**PROFESSOR: Right. So what we could do is we could use controls. So typically what we could do is we could study in environments where we try and control the environment exactly to eliminate this as much as we possibly can, for example. As we'll see that we also can do things like study clones, where individuals have exactly the same genotype. And then, all of the variance that we observe-- if this term vanishes because the genotypes are identical, it is due to the environment.**

**So typically, if you're doing things like studying humans, since cloning humans isn't really a good idea to actually measure environmental variance, right, what you could do is you can look at identical twins. And identical twins give you a way to get at the question of how much environment variance there is for a particular phenotype.**

**So in sum, this is replicates what I have here on the left-hand side of the board. And note that today we'll be talking about the idea of discovering this function, f, and how well we can discover f, which is really important, right. It's fundamental to be able to predict phenotype from genotype. It's an extraordinarily central question in genetics. And when we do the prediction, there are two kinds of-- oh, there's a question?**

**AUDIENCE: Could you please explain again why the co-variance drops out or it goes away.**

**PROFESSOR: Yeah, the co-variance drops out because we're going to assume that genotype and environment are independent. Now if they're not independent, it won't drop out. But making that assumption-- and of course, for human studies you can't really make that assumption completely, right?**

**And one of the problems in doing these sorts of studies is that it's very, very easy to get confounded. Because when you're trying to decompose the observed variance and height, for example.**

11

**You know, there's what mom and dad provided to an individual in terms of their height, and there's also how much junior ate, right. And whether he went to McDonald's a lot, or you know, was going to Whole Foods a lot. You know, who knows, right?**

**But this component and this component, it's easy to get confounded between them and sometimes you can imagine that genotype is related to place of origin in the world. And that has a lot to do with environment. And so this term wouldn't necessarily disappear.**

**OK. So there are two kinds of heritability I'd like to touch upon today. And it's important that you remember there are two kinds and one is extraordinarily difficult to recover and the other one is in some sense, a more constrained problem, because we're much better at building models for that kind of heritability estimate.**

**The first is broad-sense heritability, which describes the upper bound for phenotypic prediction given an arbitrary model. So it's the total contribution to phenotypic variance from genetic causes. And we can estimate that, right. And we'll see how we can estimate it in a moment.**

**And narrow-sense heritability is defined as, how much of the heritability can we describe when we restrict f to be a linear model. So when f is simply linear, as the sum of terms, that describes the maximum narrow-sense heritability we can recover in terms of the fraction of phenotypic variance we can capture in f.**

**And it's very useful because it turns out that we can compute both broad-sense and narrow-sense heritability from first principles-- I mean from experiment. And the difference between them is part of our quest today.**

**Our quest is, to answer the question, where is the missing heritability? Why can't we build an Oracle f that perfectly predicts phenotype from genotype?**

**So on that line-- I just want to give you some caveats. One is that we're always talking about populations when we're talking about heritability because it's how**

12

**we're going to estimate it.**

**And when you hear people talk about heritability, oftentimes they won't qualify it in terms of whether it's broad-sense or narrow-sense. And so you should ask them if you're engaged in a scientific discussion with them.**

**And as we've already discussed, sometimes estimation is difficult because of matching environment and eliminating this term, the environmental term can be a challenge when you're out of the laboratory. Like when you're dealing with humans.**

**So, let's talk about broad-sense heritability. Imagine that we measure environmental variants simply by looking at environmental twins or clones, right.**

**Because if we, for example, take a bunch of yeast that are genotypically identical. And we grow them up separately, and we measure a trait like how well they respond to a particular chemical or their growth rate, then the variance we see from each individual to individual is simply environmental, because they're genetically identical. So**

**we can, in that particular case, exactly quantify the environmental variance given that every individual is genetically identical. We simply measure all the growth rates and we compute the variance. And that's the environmental variance. OK?**

**As I said for humans, the best we can do is identical twins. Monozygotic twins. You can go out and for pairs of twins that are identical, you can measure height or any other trait that you like and compute the variance. And then that is an estimate of the environmental component of that, because they should be genetically identical.**

**And big H squared-- broad-sense is always capital H squared and narrow-sense is always little h squared. Big H squared, which is broad-sense heritability is very simple then.**

**It's the phenotypic variance, minus the environmental variance, over the phenotypic variance. So it's the fraction of phenotypic experience that can be explained from genetic causes. Is that clear to everybody? Any questions at all about this? OK.**

13

**So, for example, on the right-hand hand side here, those three purplish squares have three different populations, which are genotypically identical. They have two genes, a little a, a little a, big A, a little A, and big A, big A. And each one is a variance of 1.0. out So since there are genetically identical, we know that the environmental variance has to be 1.0.**

**On the left-hand side, you see the genotypic variance. And that reminds us of where we started today. It depends on the number of alleles you get of big A, as to what the value is.**

**And when you put all of that together, you get a total variance of 3. And so big H squared is simply the genotypic variance, which is 2, over the total phenotypic variance, which is 3. So big H squared is 2/3. And so that is a way of computing broad-sense heritability.**

**Now, if we think about our models, we can see that narrow-sense heritability has some very nice properties. Right. That is, if we build and add a model of phenotype, to get at narrow-sense heritability.**

**So if we were to constraint f here to be linear, it's simply going to be a very simple linear model. For each particular QTL that we discover, we assign an effect size beta to it, or a coefficient that describes its deviation from the mean for that particular trait. And we have an offset, beta zero.**

**So our simple linear model is going to take all the discovery QTLs that we have-take each QTL and discover which allelic form it's in. Typically it's considered either in zero or one form. And then add a beta j, where j is the particular QTL deviation from mean value. Add them all together to compute the phenotype. OK.**

**So, this is a very simple additive model and a consequence of this model is that if you think about an F1 or a child of two parents, as we said earlier, a child is going to inherit roughly half of the alleles from mom and half of the alleles from dad.**

**And so for additive models like this, the expected value of the child's trait value is**

14

**going to be the midpoint of mom and dad. And that can be derived directly from the equation above, because you're getting half of the QTLs from mom and half of the QTLs from dad.**

**So this was observed a long time ago, right, because if you did studies and you looked at the deviation from the midpoint of parents for human height.**

**You can see that the children fall pretty close to mid-parent line, where the y-axis here is the height in inches and that suggests that much of human height can be modeled by a narrow-sense based heritability model.**

**Now, once again, narrow-sense heritability is the fraction of phenotypic variance explained by an additive model. And we've talked before about the model itself. And little h squared is simply going to be the amount of variance explained by the additive model over the total phenotypic variance.**

**And the additive variance is shown on the right-hand side. That equation boils down to, you take the phenotypic variance and you subtract off the variance that's environmental and that cannot be explained by the additive variance, and what you're left with is the additive variance.**

**And once again, coming back to the question of missing heritability, if we observe that what we can estimate for little h squared is below what we expect, that gap has to be explained somehow. Some typical values for theoretical h squared.**

**So this is not measured h squared in terms of building a model and testing it like this. But what we can do is we can theoretically estimate what h squared should be, by looking at the fraction of identity between individuals.**

**Morphological traits tend to have higher h squared for the fitness traits. So human height has a little h square of about 0.8. And for those ranchers out there in the audience, you'll be happy to know that cattle yearly weight has heritability of about 0.35.**

**Now, things like life history which are fitness traits are less heritable. Which would**

15

**suggest that looking at how long your parents lived and trying to estimate how long you're going to live is not as productive as looking at how tall you are compared to your parents. And there's a complete table that I've included in the slides for you to look at, but it's too small to read on the screen.**

**OK, so now we're going to turn to computational models and how we can discover a model that figures out where the QTLs are, and then assigns that function f to them so we can predict phenotype from genotype. And we're going to be taking our example from this paper by Bloom, et al, which I posted on the Stellar site. And it came out last year and it's wonderful study in QTL analysis.**

**And the setup for this study is quite simple. What they did was, is they took two different strains of yeast, RM and BY, and they crossed them and produced roughly 1,000 F1s. And RM and BY are very similar. They are about, I think it's about 35,000 snips between them.**

**Only about 0.5% of their genomes are different. So they're really close. Just for point of reference, you know, the distance between me and you is something like one base for every thousand? Something like that. And then they assayed all those F1s. They genotyped them all.**

**So to genotype them, what you do is you know what the parental genotypes are because they sequence both parents. The mom and dad, so to speak, at 50x coverage. So they knew the genome sequence is completely for both mom and dad.**

**And then for each one of the 1,000 F1s they put them on a microarray and what is shown on the very bottom left is a result of genotype in an individual where they can see each chromosome and whether it came from mom or from dad.**

**And you can't see it here, but there are 16 different chromosomes and the alternating purple and yellow colors show whether that particular part of the genome came from mom or from dad. So they know for each individual, its source. From the left or the right strain. OK.**

16

**And they have a thousand different genetic makeups. And then they asked, for each one of those individuals, how well could they grow in 46 different conditions? So they exposed them to different sugars, to different unfavorable environments and so forth.**

**And they measured growth rate as shown on the right-hand side. Or right in the middle, that little thing that looks like a bunch of little dots of various sizes. By measuring colony size, they could measure how well the yeast were growing. And so they had two different things, right.**

**They had the exact genotype of each individual, and they also had how well it was growing in a particular condition. And so for each condition, they wanted to associate the genotype of the individual to how well it was growing. To its phenotype.**

**Now, one fair question is, of these different conditions, how many of them were really independent? And so to analyze that, they looked at the correlation between growth rates across conditions to try and figure out whether or not they actually had 46 different traits they were measuring.**

**So this is a correlation matrix that is too small to read on the screen. The colors are somewhat visible, where the blue colors are perfect correlation and the red colors are perfect anti-correlation.**

**And you can see that in certain areas of this grid, things are more correlated, like what sugars the yeast liked to eat. But suffice to say, they had a large collection of traits they wanted to estimate.**

**So, now we want to build a computational model. So our next step is figuring out how to find those places in the genome that allows us to predict, how well, given a trait, the yeast would grow. The actual growth rate.**

**So the key idea is this-- you have genetic markers, which are snips down the genome and you're going to test a particular marker. And if this is a particular trait, one possibility is that-- let's say that this marker could be either 0 or 1. Without loss**

17

**of generality, it could be that here are all the individuals where the marker is zero.**

**And here are all the markers where the marker is 1. And really, fundamentally, whether an individual has a 0 or a 1 marker, it doesn't really change its growth rate very much. OK? It's more or less identical. It's also possible that this is best modeled by two different means for a given trait.**

**That when the marker is 1, you're growing-- actually this is going to be the growth rate on the x-axis. The y-axis is the density. That you're growing much better when you have a 1 in that marker position than a zero.**

**And so we need to distinguish between these two cases when the marker is predictive of growth rate and when the marker is not predictive of growth rate.**

**And we've talked about lod likelihood tests before and you can see one on the very top. And you can see there's an additional degree of freedom that we have in the top prediction versus the bottom because we're using two different means that are conditioned upon the genotypic value at a particular marker.**

**So we have a lot of different markers indeed. So we have-- let's see here, the exact number. I think it's about 13,000 markers they had in this study. No. 11,623 different unique markers they found. That they could discover, that weren't linked together. We talked about linkage earlier on.**

**So you've got over 11,000 markers. You're going to do a lod likelihood test to compute this lod odds score. Do we have to worry about multiple hypothesis correction here? Because you're testing over 11,000 markers to see whether or not they're significant for one trait. Right.**

**So one thing that we could do is imagine that what we did was we scrambled the association between phenotypes and individuals. So we just randomized it and we did that a thousand times. And each time we did it, we computed the distribution of these lod scores.**

**Because we have broken the association between phenotype and genotype, the lod**

18

**scores which we should be seeing if we did this randomization, should correspond to essentially noise. But we would see it random. So it's a null distribution we can look at. And so what we'll see is a distribution of lod scores.**

**This is the lod. This is the probability from a null, a permutation test. And since we actually have done the randomization over all 11,000 markers, we can directly draw a line and ask what are the chances that a lod score would be greater than or equal to a particular value at random?**

**And we can pick an area inside this tail, let's say 0.05, because that's what the authors of this particular paper used and ask what value of a lod score would be very unlikely to have by chance? It turns out in their first iteration, it was 2.63. That a lod score over 2.63 had a 0.05 chance or less of occurring in randomly permuted data.**

**And since a permuted data contained all of the markers, we don't have to do any multiple hypothesis correction. So you can directly compare the statistic that you compute against a threshold and accept any marker or QTL that has a lod score greater, in this case then 2.63 and put it in your model. And everything else you can reject.**

**And so you start by building a model out of all of the markers that are significant at this particular level. You then assemble the model and you can now predict phenotype from genotype. But of course, you're going to make errors, right. For each individual, there's going to be an error.**

**You're going to have a residual for each individual that is going to be the phenotype minus the genotype of the individual. So this is the error that you're making.**

**So what these folks did was that you first look at predicting the phenotype directly, and you pick all the QTLs that are significant at that level. And then you compute the residuals and you try and predict the residuals.**

**And you try and find additional QTLs that are significant after you have picked the original ones. OK.**

19

**So why might this produce more QTLs then the original pass? What do you think? Why is it that trying to predict the residuals is a good idea after you've tried to predict the phenotype directly? Any ideas about that?**

**Well, what this is telling us, is that these QTLs we're going to predict now were not significant enough in the original pass, but when we're looking at what's left over, after we subtract off the effect of all the other QTLs, other things might pop up. But in some sense, we're obscured by the original QTLs. Once we subtract off their influence, we can see things that we didn't see before.**

**And we start gathering up these additional QTLs to predict the residual components. And so they do this three times. So they predict the original set of QTLs and then they iterate three time on the residuals to find and fit a linear model that predicts a given trait from a collection of QTLs that they discover. Yes?**

**AUDIENCE: Sorry. I'm still confused. The second round? [INAUDIBLE] done three additional times? Is that right? So the--**

**PROFESSOR: Yes.**

**AUDIENCE: Is it done on the remainder of QTL or on the original list of every--**

**PROFESSOR: Each time you expand your model to include all the QTLs you've discovered up to that point. So initially, you discover a set of QTLs, call that set one. You then compute a model using set one and you discover the residuals.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Correct. Well, residual [INAUDIBLE] so you use set one to build a model, a phenotype. So set one is used here to compute this, right. And so set one is used. And then you compute what's left over after you've discovered the first set of QTLs.**

**Now you say, we still have this left to go. Let's discover some more QTLs. And now you discover set two of QTLs. OK. And that set two then is used to build a model that has set one and set two in it. Right.**

20

**And that residual is used to discover set three and so forth. So each time you're expanding the set of QTLs by what you've discovered in the residuals. Sort of in the trash bin so to speak. Yes?**

**AUDIENCE: Each time you're doing this randomization to determine lod cutoff?**

**PROFESSOR: That's correct. Each time you have to redo the randomization and get to the lod cutoff.**

**AUDIENCE: But does that method actually work the way you expect it on the second pass, given that you have some false positives from the pass that you've now subtracted from your data?**

**PROFESSOR: I'm not sure I understand the question.**

**AUDIENCE: So the second time you do this randomization, and you again come up with a threshold, you say, oh, above here there are 5% false positives.**

**PROFESSOR: Right.**

**AUDIENCE: But could it be that that estimate is actually significantly wrong based the fact that you've subtracted off false positives before you do that process?**

**PROFESSOR: I mean, in some sense, what's your definition of a false positive? Right. I mean it gets down to that because we've discovered there's an association between that QTL and predicting phenotype. And in this particular world it's useful for doing that.**

**So it's hard to call something a false positive in that sense, right. But you're right, you actually have to reset your threshold every time that you go through this iteration. Good question. Other questions? OK.**

**So, let's see what happens when you do this. What happens is that if you look down the genome, you discover a collection. For example, this is growth in E6 berbamine. And you can see the significant locations in the genome, the numbers 1 through 16 of the chromosomes and the little red asterisks above the peaks indicate that that**

21

**was a significant lod score. The y-axis is a lod score.**

**And you can see the locations in the genome where we have found places that were associated with growth rate in that particular chemical. OK.**

**Now, why is it, do you think, that in many of those places you see sort of a rise and fall that is somewhat gentle as opposed to having an impulse function right at that particular spot?**

---

[← trait? Is that correct?](02-trait-is-that-correct.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
