---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/03bvgr-vyhq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/03bvgr-vyhq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Our goal for today is to basically analyze this simple model to death. So we're first going to try to understand the deterministic behavior of this model gene expression, where we just get transcription of mRNA, and then translation of protein. And after we think we understand the mean behavior, the deterministic dynamics, then we will try to understand just stochastic behavior in this model.**

**So we're going to try to understand what's the distribution of mRNA in a cell in this simple situation. What's the distribution of protein? What's going to be the bursting behavior? Everything you can possibly think of to ask about this model, we will hopefully have asked by the end of today's class.**

**This simple model of gene expression, as was indicated in the review, is perhaps a reasonable description of gene expression in bacteria, when the gene is in some active state. So there's no repressor, for example, bound. Although maybe even in the presence of a repressor, if it's binding and unbinding, maybe you still end up getting some sort of renormalization that looks like this. But this is first order, a reasonable description of gene expression in bacteria.**

**And it's the model that was basically used in the Sunney Xie paper that we talked about on Tuesday. And hopefully this model will allow us to think a little bit more deeply about the data that they obtained in that paper.**

**As always, we want to start by understanding the basic aspects of the model. So what we're going to do, is we're going to go through a series of questions of increasing difficulty. And in some of them, we are indeed, the answers will end up being something divided by something. In which case you take advantage of your cards, and illustrate that by putting something on top, something below.**

1

**But just first in this model, what is the unit of time? So if I say t is equal to 1, or delta t is equal to 1, what am I referring to? So we're not use the cards. But in particular, the question is, is delta t equal to 1, is that a cell cycle necessarily? Yes or no, ready, three, two, one.**

**Well I guess now maybe I've complicated things by-- well, this was really going to be relevant for the later ones. All right. Now I've totally confused you. But can somebody offer why it may or may not be-- how do we think about the unit of time in this model?**

**AUDIENCE: Usually the lifetime of one of the species [INAUDIBLE].**

**PROFESSOR: Right. OK so indeed, what we often do in these non-dimensionalized models is we set something equal to 1. Have we set anything equal to 1 here? No. So in principle, we've said there's some degradation rate of the mRNA, some degradation rate of the protein. And in general, those will be given in some units involving seconds or minutes or hours. So in general, so at this stage, we have not yet-- we have not actually gotten to this sort of non-dimensionalized version of any model.**

**So in this case this is going to be something like a seconds, or minutes, or hours, whatever units we use for those degradation rates. So we have not done anything where it's the cell generation time, or the protein lifetime, mRNA lifetime, or anything like that. Here everybody happy with this statement so far?**

**So we'll go ahead and vote here. So we're going to do some A, B, C, D's. And you can always combine anything you want. So we'll go ahead and say this is the synthesis rate of the mRNA. This is the degradation rate for the mRNA, the synthesis rate for the protein, the degradation rate for the protein. And if you're just confused, you can just do this. But in general, for any of the questions we're going to do, you can do some combination of these guys by putting things in numerator and denominator. Yes?**

**AUDIENCE: Calculate the population of the cells that were hidden?**

**PROFESSOR: Yes. Question is, if you just look at the cell population, and you find it's growing**

2

**exponentially, the question is what is going to be that rate of exponential growth. Have I done something wrong already?**

- **AUDIENCE: [INAUDIBLE]? PROFESSOR: OK. But I am going to say that now for this we're going to assume that the protein is stable. So it's not actually degraded. This is to remind you of what we read about in chapter one, maybe of Uri's book, maybe chapter two. I'll give you 10 seconds to think about this.**

**Do you need more time? All right, Ready, three, two, one. OK. We got a bunch of C's and a bunch of D's and some E's. All right. So the E's are going to argue with me, presumably rather than a neighbor. OK. I think that there are enough people that are disagreeing on this to maybe go ahead, and turn. You should be able to find somebody that disagrees with you. The distribution was a bit patchy, unfortunately. Did you guys-- you guys are worried that you're not going to be able to find somebody. OK. Fine, fine. Yeah?**

**AUDIENCE: So if the protein is stable, ah, so the mRNA may not be stable? PROFESSOR: The mRNA may not be stable. AUDIENCE: Ah, OK. That makes sense. PROFESSOR: And in general which one typically has a longer lifetime? AUDIENCE: Proteins. PROFESSOR: Proteins typically have a longer lifetime. Right. So mRNA are actively degraded, typically. They're also just kind of less stable intrinsically. But what we're going to assume for now is that we're working with stable proteins. In which case the growth rate of the population will just be this effective degradation rate of the protein. So in this model, even if we say there's no active degradation of the protein, still there's going to be some effective degradation that's due to dilution. So we can say effective, if you like. So the rate of exponential growth of the population will be equal**

3

**to this effective degradation rate for the protein, if it's stable.**

**AUDIENCE: So you're talking about the population of the protein?**

**PROFESSOR: No. The growth rate of the cell population. So this is if we go in there, and you go into your spectrophotometer. And you measure population-- numbers in function of time is growing exponentially. It'll grow exponentially with this rate. Because this is what's causing the dilution.**

**In some ways if you stop making the protein, and you double the number of cells, and that means the concentration of the protein in each cell has to go down by a factor of two. So that's the statement. Are there any questions about why I'm making this argument? Yes?**

**AUDIENCE: What was the relevance of the protein being stable?**

**PROFESSOR: All right. So the relevance of the protein being stable, because this is in general, this delta, this is the effective rate. This is going to be equal to the growth rate of the population. So you might call it gamma growth plus the actual degradation. I don't want to use the same, but I'll just say plus the degradation rate. And this is a true physical degradation, true degradation rate of the protein.**

**So if it's stable, then we say that this thing is zero. So when we say stable protein, it means there's no degradation of the protein. So this physical degradation rate is zero. And then the effective degradation rate of the protein is just equal to the growth rate of the population.**

**AUDIENCE: OK, so no degradation means stable, basically?**

**PROFESSOR: Yes, sorry, yeah. Any other questions about what I mean by this? So now what we want to do is ask a few other quantities about this model. So for example, what will be the number of mRNA per cell? And this is always going to be the mean. I'll give you 20 seconds. In this model what is the mean number of mRNA per cell? All right. Ready? Three, two, one. And we**

4

**have let's say a majority of the group is saying it's A over B, which corresponds to the synthesis rate of the mRNA divided by the degradation.**

**Some people are this one? Yes, so this is indeed, synthesis rate divided by the degradation rate. Now this is saying that what happens later doesn't really matter, for the mean mRNA number. Because it's just that it's going to be made at some rate. Its lifetime is given by 1 over delta m. Now this thing, of course, is again as always, the effective degradation rate. So it's the sum of the sort of physical degradation rate, plus this dilution due to growth.**

**But in general, the true degradation, the physical degradation is much faster than the cell division rate. So this is very close to actually just the physical degradation rate. But in any case, it's just delta m, regardless. Are there any questions about why this is the way it is? Yes?**

**AUDIENCE: Does it matter whether it's only physical? Because wouldn't it be the same if it were-**

**PROFESSOR: It doesn't matter that it's only-- exactly. That's what I was trying to say. So the way that this is written, it doesn't matter whether the-- this is the answer regardless of whether the physical degradation rate is much larger than the growth rate or not. Yeah.**

**All right. What is this protein molecules per mRNA? How many protein molecules are made from each mRNA? Protein produced-- Do you need more time? Remember. This is again, the mean number of proteins produced from a single mRNA or each mRNA.**

**Let's go ahead and vote, so I can see where we are. Ready? Three, two, one. OK. So we have, I'd say, so at least a majority are saying it's going to be C over B Now. All right. So this is interesting. So this is saying that really what's happening is that there's a competition once you make an mRNA that the proteins are going to be getting fired off at some rate. But eventually it's going to be degraded.**

**It's a competition between those two rates that determines basically how many**

5

- **proteins, how many times do you fire off a protein before you get degraded. Any questions about that logic?**

- **AUDIENCE: Can you please just repeat that one more time? PROFESSOR: Sure. Right, so what we're assuming is that OK, an mRNA is produced. And that's already happened. So it doesn't matter what Sm is anymore. So now we have an mRNA. Eventually this mRNA will be degraded. But before that happens, we want to know, basically how many proteins do we expect to be made. Now if Sp and delta m are the same that means you kind of expect one protein to be made on average, before it's degraded. Or if Sp we're twice delta m, then you would get two proteins made before it was degraded. Now this is a mean statement. We're about to start thinking-- in 10 minutes, we'll think about this distribution. And so we have to be careful. But in terms of mean behavior, this thing is true.**

- **AUDIENCE: So is this different than it has been for the number of proteins per mRNA in the cell? PROFESSOR: Is this different from the number of proteins in the cell? AUDIENCE: Number of proteins per mRNA in the cell. Because then you will have to do the protein concentration over mRNA concentration.**

- **PROFESSOR: OK. Right. So this is not the same thing as asking about the ratio of the number of proteins. And we can calculate that as well. Yeah these are different. This is the number of protein molecules produced from each mRNA. So this is just talking about production. Because indeed, the degradation rates are going to be different. So then we can see what that ends up being. Any other questions about why this one is what it is? How about the number of mRNA produced per cell cycle? And for now we're going to ignore factors of log two. Do you need more time? So another 10 seconds.**

- **AUDIENCE: Produced but not degraded? PROFESSOR: Produced, yes. We're just talking about production. Because we've already**

6

**calculated a number of mRNA in the cell. But now we want to know the mean number produced. For example, this is the same as the mean number of protein bursts observed in Sunney Xie's paper. But this is just the number of mRNA produced per cell cycle.**

**All right. Let's see where we are. Ready? Three, two, one. All right. So we've got lots of A's over D's. That's sounds nice. So this is going to be some synthesis rate. But now the relevant thing is this delta p. Because that's the cell division rate. So it's barring issues of log two, it's approximately the synthesis rate of the mRNA divided by delta p. Because this is the growth rate of population.**

**Cell generation time is log two off of that. Are there any questions about that statement? All right, so this is the mean number. Now from the paper, we know how this thing is distributed. We should probably-- we're going to use a bunch of distributions over the next couple.**

**So we can-- we like exponential distributions. We like geometric distributions. We like Poisson. We like Gaussian. And we like gamma. These are various probability distributions. The question is, how is it that now, not the mean, but how is the number of mRNA produced per cell cycle distributed. Ready? Three, two, one.**

**All right. We've got some-- this side of the rooms a little bit slower, maybe. But that's OK. So maybe some people are not confident of this statement. OK. So this one ends up being Poisson. So this is indeed how the number of-- this is number mRNA per cycle.**

**Now this is-- so Poisson, in general, that's what you get if there's some probability per unit time that something's going to happen, and you want to know how many of them happen in some finite time period. That's basically the definition of a Poisson. And this is, if you recall, this is what we talked about on Tuesday. The probability observe n, it's given by this mean number. So if lambda is the mean, then we get lambda to the n, over n factorial, e to the minus lambda.**

**If you go ahead and calculate the mean of this, you indeed get lambda. So lambda**

7

**is equal to the mean, which in this case was around, well in the case of Sunney's paper, does anybody remember what that roughly was? It was around one.**

**Now what about this other one? So we also have another mRNA problem, which is that we calculated the mean number of mRNA per cell. If you look at a cell, the mean number is this. But what's the probability distribution of the number of mRNA per cell? So we probably-- I'm trying think it-- you probably don't yet know this answer.**

**This ends up also being Poisson. We're going to calculate this in a bit. But this is very confusing somehow. That both this thing and this thing, are Poisson. But they're not the same Poisson, in the sense they have different lambdas. Which one is going to be larger? This one or this one? The bottom one, right? And that's because delta m is much larger than delta p, typically.**

**So indeed, if you ask, in Sunney's paper, for example, there was just over one mRNA produced per cell cycle. But the mean number of mRNA might have been 1/30th of that. Because the degradation rate was just 1 and 1/2 minutes. What that's saying is that in a typical situation you would not see an mRNA in a cell in that condition.**

**We're going to calculate this in a moment. So don't worry if you don't see why it's a Poisson. But don't get confused. There are two different distributions that arise from the mRNA in the cell or in the cell cycle. And they're different Poissons. And I think that-- I mean I'm sure that in some deep sense there's a reason that they're the same. But it's somehow not immediately obvious.**

**So there was another one that we might have wanted to do, which is the mean number of proteins in each cell. Now this one is a bit harder. And this one is going to take full advantage of the cards that you have in front of you. So be prepared. I'm going to give you 30 seconds. Because this one you might-- well you might need a little bit more time.**

**AUDIENCE: This is hard.**

8

**PROFESSOR: Yeah. Although I think that it's useful to see that it can be a bit tricky. Because this really is the simplest possible model. We're going to talk about some models that get to be horribly complicated. And so it's useful to just make sure you can nail down the intuition on this model.**

**All right. Do you need more time? It's OK if this is escaping you at this moment. Why don't we go and see where we are? Ready? Three, two, one. All right. So you know all the naysayers on the cards, now that you've done this, you feel like it's an amazing system.**

**So it's AC over DB. So the two, the product of the synthesis rates divided by the product of degradation rates. So what we have is the synthesis rate for the mRNA divided by the degradation rate for the mRNA. Synthesis rate for the proteins divided by the degradation rate for the proteins.**

**Can somebody give us a verbal explanation for why this might have been, or why this is? Yes?**

**AUDIENCE: It's the same reasoning as the number of mRNA per cell. But instead of just a basel- like a synthesis rate doesn't depend on the concentration. You're just multiplying the synthesis rate by the number of mRNA.**

**PROFESSOR: Yeah, that's great. OK. So what you're saying is that this thing here was indeed, we calculate that was the mean number of mRNA in the cell. If you just start with something, and you have a production and degradation rate. OK. Well that means that if you had one mRNA, then indeed that's what the concentration would be, is this Sp divided by delta p.**

**But now we-- well we multiply that by the number of mRNA, and then we are set. All right. Now another question. We have a distribution, or a mean protein-- wait sorry, mean number. We have the mean number of protein produced from each mRNA, is something.**

**And the question is, is this the most likely number of proteins to observe. Is the distribution here, now this is a mean, but now we want to start thinking about the**

9

**probabilistic stochastic elements. Is this the most likely, is it like the number of proteins observed from an mRNA?**

**The question is, is this most likely. By which I mean is the probability distribution peaked here. So we're going to do an A as a yes, and B is a no. Does everybody understand the question I'm trying to ask? So an mRNA is here. There's going to be some proteins made from it. This is the mean. What I want to know is, is that we should somehow expect? In a sense, is the distribution peaked, the probability distribution peaked around this value?**

**And C is-- do I want to do a depends? Well you can always argue after. Do you need more time?**

**AUDIENCE: Is this, you're saying, is this the most likely number of proteins? PROFESSOR: Yeah. What I'm wondering is the mode there?**

**AUDIENCE: Right. But only for this quantity?**

**PROFESSOR: Only yeah. So now we're not doing means anymore. We want to know if the probability distribution of the protein produced from each mRNA is the mode around this. Ready? Three, two, one. All right. We got a lot of no's, but some yeses. So this is actually going to be a no. And this was because the probability distribution. The question is, what is the probability distribution for the number of proteins produced from each mRNA. It's going to be one of these. Ready? Three, two, one. All right. So we've got some difference. But I'd say that most of the group is saying it's going to be A or B. And indeed these are almost the same distributions. What's the difference between them?**

**AUDIENCE: One's discrete--**

**PROFESSOR: Right. So this guy's discrete. This guy is continuous. Right. Indeed when we're taking about the numbers, then we should get-- it's a geometric. But often we're kind of a little bit loose about these things. So it's not a disaster if you said**

10

**exponential. But the key thing is that the distribution looks something like-- so now I've certainly drawn it as an exponential. This is the probability of n as a function of n. Of course, the geometric thing it looks--**

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
