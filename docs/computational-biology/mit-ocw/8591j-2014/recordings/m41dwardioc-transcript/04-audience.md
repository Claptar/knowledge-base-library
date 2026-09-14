---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/m41dwardioc-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/m41dwardioc-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**These scales that are your two end points [? are doubled. ?]**

**Because I think that the probability distribution does grow. I think that I'm going to side with you. So we've decided that there are not going to be as many short sticks, and there's not going to be as long sticks as compared to a log normal. Do we agree with that?**

**At least we agree that it's not going to be a log normal. So you're not going to get this huge variation of some very long sticks and some very short ones. Now, the question is how would you change this sort of model in order to generate a log normal?**

**And the answer is that what you have to do is you have to what is called some niche hierarchy or so some hierarchical breaking. Just like what led to the stone giving you a log normal is that you have to have some successive process of breaking things. So this is what they call some hierarchy model.**

**And then they key thing is that it's sequential. You have your resource axis. First, you have some rule for breaking it up. It could be that you just sample uniformly or some other probability distribution.**

**And the way that you might think about this is via-- just everything up on the board is so nice and useful. I feel bad getting rid of it. This thing is not true, so I don't mind erasing it.**

**So let's imagine some bird community in the forest. And we're going to think about where is it that the birds are getting their grub or their food to eat.**

**First, well, now the axis is somehow vertical. You could divide them up into the ground foragers as compared to the tree foragers in terms of where they're getting their food.**

**And you say, oh, well, how much of the food is on each side? Oh, well, we'll say 30% is on the ground, 70% is on the tree. This is along the stick. You cut the stick in some way, or you break the stick in some way.**

18

**But then within the tree foragers, you'd say, well, the resources might be separated. And this is really like speciation, a species is in the niche, the species are focusing on different niches. So you'd say, oh, some are going to focus on the trunk, some will focus on branches.**

**And again, this part of the stick is now broken or divided among different resource locations with some amount. But then also, you're going to get speciation in different directions here, because there's both the surface-- I don't know if you guys have ever eaten grubs-- but there's the surface grubs, and then there's also the sub-bark grubs.**

**And so you kind of do this process multiple times, where you kind of pick different branches and break them to divide up the niche. And then you end up with a log normal type distribution.**

**And this is a similar process to the crushing of the stone, because the idea is that there's sequential breaks of the stone. So the stone first breaks into maybe simply two or it could be three. First, there's one breaking. And then one of them is broken more. So given this process, you end up getting a log normal distribution. Yeah.**

**AUDIENCE: But you also have a distribution of like how far. Because I guess there are two questions. Like when you break your stick, you assume, somehow, that you uniformly break it.**

**PROFESSOR: Yeah. A lot of work has gone into the question of how it is you should break the stick. Given that you have this tree foraging stick. On a practical level, what they do is they ask, well, what probability distribution gives you the best agreement with the data? Is it uniform? Or is it, oh, it's broken like this?**

**And in some cases people say, well, it's actually tilted on one side. Well, in the context of a succession and some other environments, there's an idea that, if a species first gets somewhere, they can kind of monopolize a larger fraction of the resources then if it's divided kind of an equally at the beginning.**

19

**And that's going to effect where this probability distribution is going to break each one. But there's always this question about how constrained are the notions and so forth. And I'm agnostic on that point.**

**AUDIENCE: But you also need distribution for how many times it breaks [INAUDIBLE].**

**PROFESSOR: Yes. It's just that, if you do this process, it's like a central limit theorem type result. So you have to do it enough times so that you get to some limiting distribution. And then you could keep on doing it. In the end, we always say that species abundance is proportional to the size.**

**So we're going to scale, ultimately, to get the correct number of individuals. It's just that you have to do it some reasonable number of times so that the randomness kind of washes out, and you end up approaching that limiting behavior. Does that make sense?**

**And indeed I just want to mention a major result in this field. These niche type models successfully explained or predicted another pattern that had been observed, which is the so-called species area relationships.**

**So this is just saying that, here, we looked at 50 hectares, and we asked how many species where there. 225 species in 50 hectares. Now, the question is, if instead of looking at 50 hectares, we instead looked at 500, do you think of that the number of species we observed would have gone up, stayed the same, or gone down? Up, same, down, ready, three, two, one.**

**Up. Up. If you look at a larger area, you expect to see more species in a larger area. And people really do this. They look in some area, going from, say, they take a meter, and they count all the species. And then they go and here is 100 meters, and they count all the species.**

**And they ask, how many species do you see as a function of the area? And what people have found is that the number of species you observe it is proportional to the area to some power, where Z is around a 1/4. And of course, the area goes as some r squared. If you wanted to, you could say it goes as the square root of the**

20

**radius, whatever.**

**But the number species in some area, it grows, but it grows in a manner that is less than linear. Does that make sense? It definitely makes sense that's less the linear.**

**Because linear would be that you sample a bunch of species here, and then you look at another identical plot, you get some other species. And they were saying that, oh, that you really don't expect any of those species overlap. That would be a weird world.**

**So it very much make sense that this is less than 1. Of course, it didn't have to be this power law. But one thing that has been discovered, around the world, is that power laws are very interesting. But once again, many different microscopic processes can lead to power laws.**

**The niche models have successfully predicted or explained why it might have this scaling. But it turns out that neutral models can also predict it. And may just be that lots of spatially explicit models will give you some power law type scaling that looks kind of like this.**

**So once again, it's a question of how convinced you should be about microscopic processes based on being able to explain some data. And I think the best cure for this danger, of assuming that the microscopic assumptions are correct, because the model is able to explain something, is that, if you find some other very different set of microscopic assumptions that also explain the patterns, then it becomes clear that you have to take everything with a grain of salt.**

**And that's I think part of what's been very valuable about the neutral theory contribution to this field.**

**AUDIENCE: Does this just come from-- you assume that all the individuals are uniformly distributed and then [INAUDIBLE]?**

**PROFESSOR: There are multiple derivations of this, so it's a little bit confusing. The neutral models, that I have seen, that lead to these patterns, they basically have the**

21

**individuals randomly, either with sex or without sex, kind of diffusing around, and then they divide, deh-deh. And then you can explicitly just do the different spaces and see that you get a scaling.**

**It seems to be a surprisingly emergent feature of many of these models. And once again, it may be something that tells us less about biology than it does about math or something.**

**Any other questions about this, the base notion of this niche hierarchy type models? So I want to spend some time talking about this neutral theory in ecology. The math, in particular the derivation of this particular closed form solution, is not really so interesting or relevant. But I think it's very important to understand what the assumptions are in the model and maybe also something about the circumstances in which we think that it should apply.**

**So the basic idea is that we have, what we hope, is some metacommunity that is large. And then we have an island. So this has to do with this theory of island biogeography. We have an island over here.**

**And in the context of the nomenclature of this paper, they are some community size, size j here. This tells us about the number of individuals. And they're distributed across some number of species.**

**Now, the neutral theory, the key thing is that we assume that all individuals are identical. And once again, it's not that the neutral theorists believe that this is true. It's that they think that it may be sufficient to explain the patterns that are observed.**

**And when we say that all individuals are identical, what we mean is that the demographic parameters are the same, birth, death rates. And it's even a stronger assumption, in some ways, than that. It's assuming that the individuals are the same, the species are the same, and that there are no interactions within the species as well.**

**So there's no Alley effect, or no specific competition. So the birth, death rates are going to be independent of everything, which is an amazingly parsimonious model.**

22

**And it's kind of amazing you can get anything out of it.**

**And then we have a migration rate m. It's either a rate or a probability, depending on how you think about it. Rate or probability m. And can somebody remind us how we handle that?**

**AUDIENCE: Both just in a community? PROFESSOR: Yeah. AUDIENCE: At some probability that is proportional to the distribution of the species in the metacommunity?**

**PROFESSOR: Yeah, that's right. AUDIENCE: --transfer an individual from the metacommunity to the island.**

**PROFESSOR: Perfect.**

**AUDIENCE: We do stick to the island to make sure that number of individuals.**

**PROFESSOR: Right. So what we're going to do is we're basically going to pick a random individual, here, each cycle. This is kind of like a Moran process. We're going to pick an individual here. And we're going to kill him.**

**And then what we're going to do is, with probability m, replace that individual with one member of the metacommunity at random. So the rate coming from here will be proportional to the species abundance in the metacommunity. And with a probability of 1 minus m, what we're going to do is we're going to replace that individual with another individual in the island.**

**Now, the math kind of gets hairy and complicated. But the basic notion is really quite simple. You have a metacommunity distribution, which is going to end up being the so-called Fisher log series in this model. This describes the species abundance on the metacommunity.**

**But then on the island, we're just going to assume that there's birth, death that**

23

**occurs over here at some rate. But we don't even have to hardly think about that. From the standpoint of, say, a simulation or model, we just run multiple cycles of this, where we have j individuals.**

**And we always have j individuals, because it's like the Moran process. At every time point, we kill one individual, and we replace it, with somebody either from the same community or from the island.**

**And you can imagine that in the limit of m going to zero, what's going to happen on the island? Yeah, so you'll end up just one species, just because this is just random, like genetic drift. It's ecological drift where one species will take over. Whereas if m is large, then somehow it's more of a reflection of the metacommunity.**

**Are there any questions about what this model is looking like for now?**

**AUDIENCE: Could we talk about the Fisher log series?**

**PROFESSOR: Yeah.**

**AUDIENCE: So we would put it on the same axis as the [INAUDIBLE]?**

**PROFESSOR: Yes, this is a very, very good question. So we'll do this in just a moment. Because this is very important. I want to say just a couple things about this model. So when I read this paper, what I imagined is that it really looked like this.**

**This was Panama, and that, 30 kilometers off the coast, there was this island, BCI, Barro Colorado Island. But that's not maybe an accurate description of what the real system looks like. Does anybody know where BCI is?**

**AUDIENCE: It's in Panama.**

**PROFESSOR: Hm?**

**AUDIENCE: Panama.**

**PROFESSOR: So it is in Panama. But it's not off the coast of Panama. I guess that was my original.**

24

**AUDIENCE: It's in the canal.**

**PROFESSOR:**

**Yeah, it's in the canal. So it's an island that was created when they made the Panama Canal. So this thing was not always an island. It's been an island for 100 years. And it's in the middle of a canal. And they actually have cougars that swim back and forth from the mainland.**

**But it does make you wonder whether this is-- it's much more strongly coupled to the mainland then I imagined when I read this paper at first. I don't know what that means for all this. But certainly, you expect this to be a more or less appropriate model depending on this.**

**Because, of course, if you went and you sampled 50 hectares here, you wouldn't believe that it should have the same distribution. You'd believe it should be more like the Fisher log series. And there's some evidence that things are tilted in a way that you would expect. And we'll talk about that.**

**It's tricky. And of course, you have to decide in all this stuff, oh, what do you mean by free parameters? And actually, it seems like people can't count. And we'll talk about this in a moment, too.**

**Because, of course, constructing the model, there's some sense of free parameters that you have there. Because we could have said, oh, it's just going to be the Fisher log series, or we could have said, oh, it's going to be island. Or we could have said, oh, there's another island out here. And then that would be another distribution.**

**And not all of these things introduce more free parameters, necessarily, because you could say, oh, this is the same migration rate, or you could do something. But they are going to lead to different distributions, and you have that freedom when you're trying to explain the data. There are a lot of judgment calls in this business.**

**But let's talk about Fisher log series, because this is relevant. So the model is very similar to what we did for the master equation in the context of gene expression and the number of mRNA. So was the equilibrium or steady state distribution of mRNA in a cell, was that a Fisher log series? Yes or no, five seconds? Was the mRNA steady**

25

**state probability distribution a Fisher log series? Ready, three, two, one.**

**No. No. What was it? It was a Poisson. And you guys should review what all these distributions are, when you get them, and so forth. So what was the Difference why is it that we have some probability, P0, P1, P2? This could be mRNA or it could be number of individuals in some species with some birth and death rates.**

**What was the key difference between the mRNA model, which led to this distribution becoming Poisson, and the model that we just studied here, where it became a Fisher log series? And I should maybe write down what the Fisher log series is.**

**So this is the expected number of species with n individuals on the metacommunity. Here is the Fisher log species. There was some theta X to the n divided by n. So what's the key difference? Yeah.**

**AUDIENCE: I think that the birth and death rates are both proportional [INAUDIBLE]. PROFESSOR: Right, the birth and death rates are both proportional. AUDIENCE: In the Fisher log series. PROFESSOR: In the Fisher log series. So what we have is that b0-- and what should we call b0 in this model? AUDIENCE: [INAUDIBLE]. PROFESSOR: Well, right now, we're thinking about the metacommunity. AUDIENCE: Speciation. PROFESSOR: Speciation. b0 is speciation, which we're going to assume is going to be constant. In this model, do we have speciation on the island? No. The assumption is that the island is small enough that the rate of speciation is just negligible. So speciation plays a role in forming the metacommunity distribution, but it doesn't play a role in the model.**

**So this is speciation. But then what we assume is that b1, here, is equal to some**

26

**fundamental rate b times n, but it's b times, in this case, 1. So more broadly, bn is equal to some birth rate times n. This is saying that the individuals can give birth to other individuals.**

**Now, we're not assuming anything about sexual reproduction necessarily or not. We're just saying that the kind of rates are proportional to the numbers. So if you have twice as many individuals, the birth rate will be twice as large. This is reasonable.**

**This is Pn and this is Pn plus 1. So this is d of n plus 1 is equal to some death rate times n plus 1. So each individual just has some rate of dying. It's exponentially distributed. This again makes sense.**

**What was the key difference between our mRNA model, from before that gave the Poisson, and this model that gives the Fisher log series?**

**AUDIENCE: So with the mRNA, it's with a standard like a chemical equation where there's some fixed external input. But then the degradation is according to the amount that you have. So death is proportionate [INAUDIBLE].**

**PROFESSOR: Perfect. In both cases, the death rate is proportional to the number of either mRNA or individuals. However, in the mRNA model, what we assume is there some just constant rate of transcription, so a constant rate, per unit time, of making more mRNA. So just because there's more mRNA doesn't mean that you're going to get more mRNA.**

**But here, we assume that the birth rate is proportional to the number. So that's what leads to the difference. And so this is one of the few other cases that you can simply solve the master equation and get an equilibrium distribution.**

**And it's the same thing we do from just always, where we say, at steady state, the probability fluxes or whatever are equal. So you get that P1 should be equal to P0. and then we have a b0 divided by d1. And more broadly, we just cycle through. The probability of being in the nth state, it's going to be some P0. And then basically, it's going to b0 divided by d1, b1 divided by d2, b2, d3, dot, dot, dot, up to bn minus 1**

27

---

[← they divided by 2. That's this number.](03-they-divided-by-2-that-s-this-number.md) · [Up: contents](index.md) · [dn. →](05-dn.md)
