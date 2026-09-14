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

**Nearby snips are linked?**

**PROFESSOR: Yeah, nearby snips are linked. That as you come up to a place that is causal, you get a lot of other things are linked to that. And the closer you get, the higher the correlation is.**

**So that is for 1,000 segregants in the top. And what was discovered for that particular trait, was 15 different loci that explained 78% of the phenotypic variance. And in the bottom, the same procedure was used, but was only used on 100 segregants.**

**And what you can see is that, in this particular case, only two loci were discovered that explain 21% of the variance. So the bottom study was grossly under powered.**

**Remember we talked about the problem of finding QTLs that had small effect sizes. And if you don't have enough individuals you're going to be under-powered and you can't actually identify all of the QTLs.**

**So this is a comparison of this. And of course, one of the things that you don't know is the environmental variance that you're fighting against. Because the number of individuals you need, depends both on the number of potential loci that you have.**

**The more loci you have, the more individuals you need to fight against the multiple hypotheses problem, which is taken care of by this permutation implicitly. And the more QTLs that contribute to a particular trait, the smaller they might be. And there you need more individuals to provide adequate power for your test.**

22

**And out of this model, however, if you look at for all the different traits, the predictive insight versus the observed phenotype, you can see that the model does a reasonably good job.**

**So the interesting things that came out of the study were that, first of all, it was possible to look at the effect sizes of each QTL. Now, the effect size in terms of fraction of variance explained of a particular marker, is the square of its coefficient. It's the beta squared.**

**So you can see here the histogram of effect sizes, and you can see that most QTLs have very small effects on phenotype where phenotype is scaled between 0 and 1 for this study.**

**So, most traits as described here have between 5 and 29 different QTL loci in the genome. They're used to describe them with a median of 12.**

**Now, the question the authors asked, was if they looked at the theoretical h squared that they computed for the F1s, how well did their model do? And you can see that their model does very well. That, in terms of looking at narrow sense heritability, they can recover almost all of it, all the time.**

**However, the problem comes here. Remember we talked about how to compute broad-sense heritability by looking at clones and computing environmental variance directly.**

**And so they were able to compute broad-sense heritability and compare that the narrow-sense heritability that they were able to actually achieve in the study. And you can see there are substantial gaps. So what could be making up those gaps? Why is it that this additive model can't explain growth rate in a particular condition?**

**So, the next thing that we're going to discover are some of the sources of this socalled missing heritability. But before I give you some of the stock answers that people in the field give, since this is part of our quest today to actually look into missing heritability, I'll put it to you, my panel of experts.**

23

**What could be causing this heritability to go missing? Why can't this additive model predict growth rate accurately, given it knows the genotype exactly? Yes.**

**AUDIENCE: [INAUDIBLE] that you wouldn't detect from looking at the DNA sequence. PROFESSOR: So epidemic factors-- are you talking about protein factors or are you talking about epigenetic effects? AUDIENCE: More of the epigenetic marks. PROFESSOR: Epigenetic marks, OK. So it might be now, yeast doesn't have DNA methylation. It does have chromatin modifications in the form of histone marks. So it might be that there's some histone marks that are copied from generation to generation that are not counted for in our model. right? OK, that's one possibility. Great. Yes. AUDIENCE: There could be more complex effects so two separate genes may come out, other than just adding. One could turn the other off. So it one's on, it could [INAUDIBLE]. PROFESSOR: Right. So those are called epistatic effects, or they're non-linear effects. They're gene-gene interaction effects. That's actually thought to be one of the major issues in missing heritability. What else could there be? Yes. AUDIENCE: [INAUDIBLE]. PROFESSOR: Right. So you're saying that there could be inherent noise that would cause there to be fluctuations in colony size that are unrelated to the genotype. And, in fact, that's a good point. And that's something that we're going to take care of with the environmental variance. So we're going to measure how well individuals grow with exactly the same genotype in a given condition. And so that kind of fluctuation would appear in that variance term. And we're going to get rid of that. But that's a good thought and I think it's important and not appreciated that there can be random fluctuations in that term. Any other ideas? So we have epistasis. We have epigenetics. We've got two E's so far. Anything else?**

24

**How about if there are a lot of different loci that are influencing a particular trait, but the effect sizes are very small. That we've captured, sort of the cream. We've skimmed off the cream.**

**So we get 70% of the variance explained, but the rest of the QTLs are small, right, and we can't see them. We can't see them because we don't have enough individuals. We're underpowered, right. We just-- more individuals more sequencing, right.**

**And that would be the only way to break through this and be able to see these very small effects. Because if the effects are small, in some sense, we're hosed. Right?**

**You just can't see them through the noise. All those effects are going to show up down here and we're going to reject them. Anything else, people can think about? Yes?**

**AUDIENCE: Could you content maybe the sum of some areas that are-- sorry, the addition sum of those guys that have low effects. Or is that not detectable by any [INAUDIBLE]? PROFESSOR: Well, that's certainly what we're trying to do with residuals, right? This multi-round round thing is that we take all the things we can detect that have an effect with a conservative cut off and we get rid of them.**

**And then we say, oh, is there anything left? You know, that's hiding, sort of behind that forest, right. If we cut through the first line of trees, can we get to another collection of informative QTLs? Yeah.**

**AUDIENCE: I was wondering if this could be an overestimate also. Like, for example, if, when you throw out the variance for environmental conditions, the environmental conditions aren't as exact as we thought they were between two yeast growing in the same set, setup.**

**PROFESSOR: Right.**

**AUDIENCE: Then maybe you would inappropriately assign a variance to the environmental**

25

**condition whereas some that could be, in fact-- something that wouldn't be explained by.**

**PROFESSOR:**

**And probably the other way around. The other way around would be that you thought you had the conditions exactly duplicated, right. But when you actually did something else, they weren't exactly duplicated so you see bigger variance in another experiment. And it appears to be heritable in some sense. But, in fact, it would just be that you misestimated the environmental component.**

**So, there are a variety of things that we can think about, right. Incorrect heritability estimates. We can think about rare variance. Now in this particular study we're looking at everything, right. Nothing is hiding. We've got 50x sequencing. There are no variants hiding behind the bushes. They are all there for us to look at.**

**Structural variants-- well in this particular case, we know structural variants aren't present, but as you know, many kinds of mammalian cells exhibit structural variance and other kinds of bizarre behaviors with their chromosomes. Many common variants of low effect. We just talked about that. And epistasis was brought up. And this does not include epigenetics, I'll have to add that to the listen. It's a good point. OK.**

**And then we talked about this idea that epistasis is the case where we have nonlinear effects. So a very simple example of this is when you have little a and big B, and big A and big B together, they both had an effect. But little a, little b, have no effect. And big A and big B have no effect by themselves. So you have a pairwise interaction between these terms. Right.**

**So this is sort of the exclusive OR of two terms and that non-linear effect can never be captured when you're looking at terms one at a time. OK. Because looking one at a time looks like it has no effect whatsoever. And these effects, of course, could be more than pairwise, if you have a complicated network or pathway.**

**Now, what the authors did to examine this, is they looked at pairwise effects. So they considered all pairs of markers and asked whether or not, taken two at a time**

26

**now, they could predict a difference in trait need. But what's the problem with this? How many markers did I say there were? 13,000, something like that.**

**All pairs of markers is a lot of pairs of markers. Right. And what happens to your statistical power when you get to that many markers? You have a serious problem. It goes right through the floor. So you really are very under-powered to detect these interactions.**

**The other thing they did was to try to get things a little bit better as they said, how about this. If we know that a given QTL is always important for a trait because we discovered it in our additive model. Well consider its pairwise interaction with all the other possible variants.**

**So instead of now 13,000 squared, it's only going to be like 22 different QTLs for a given trait times 13,000 to reduce the space of search. Obviously I got this explanation not completely clear. So let me try one more time. OK.**

**The naive way to go at looking at pairwise interactions is consider all pairs and ask whether or not all pairs have an influence on a particular trait value. Right. We've got that much? OK.**

**Now let's suppose we don't want to look at all pairs. How could we pick one element of the pair to be interesting, but smaller in number? Right. So what we'll do is, for a given trait, we already know which QTLs are important for it because we've built our model already.**

**So let's just say, for purpose of discussion, there are 20 QTLs that are important for this trait. We'll take each one of those 20 QTLs and we'll examine whether or not it has a pairwise interaction with all of the other variance. And that will reduce our search base. Is that better? OK, good.**

**So, when they did that, they did find some pairwise interactions. In 24 of their 46 traits had pairwise interactions and here is an example. And you can see the dot plot, or the upper right-hand part of this slide, how when you BYBY. You have a lower phenotypic value then when you have just any RM component on the right-**

27

**hand side.**

**So those were two different snips on chromosome 7 and chromosome 11 and showing how they interact with one another in a non-linear way. If they were linear, then as you added either a chromosome at 7 or a chromosome 11 contribution it would go up a little bit.**

**Here, as soon as you add either contribution from RM, it goes all way up to have a mean of zero or higher. In this particular case, 71% of the gap between broadsense and narrow-sense was explained by this one pair interaction.**

**So it is the case that pairwise interactions can explain some of the missing heritability. Can anybody think of anything else they can explain missing heritability? OK.**

**What's inherited? Let's make a list of everything that's inherited from the parental line to the F1s. OK. Yes.**

**AUDIENCE: I mean, because there's a lot more things inherited. The protein levels are inherited.**

**PROFESSOR: OK.**

**AUDIENCE: [INAUDIBLE] are inherited as well.**

**PROFESSOR: Good. I like this line of thinking.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: There are a lot of things that are inherited, right? So what's inherited? Some proteins are probably inherited, right? What is replicable through generation to generation as a genetic material that's inherited?**

**Let's just talk about that for a moment. Proteins are interesting, don't get me wrong. I mean, prions and other things are very interesting. But what else is inherited? OK, yes?**

**AUDIENCE: [INAUDIBLE].**

28

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [PROFESSOR →](05-professor.md)
