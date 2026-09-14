---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/lly1u2aghiq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/lly1u2aghiq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So today we're going to take a little bit of a lightning tour through some basic topics on chemical enzyme kinetics, before thinking a little bit about some, what you might call, simple input-output relationships, in terms of gene expression. I've got separation of time scale, and also this basic notion that for a stable protein there's a natural time scale over which the concentration will go up or down, and that's dictated by the cell generation time. At the end, we'll then talk about different ways you get this thing of ultrasensitivity.**

**So, how is it that you can make it so that a small change in the input concentration, say the concentration of a transcription factor, might be able to lead to a large change in the output, or the gene expression of its target? We'll talk about how you can have, for example, cooperative binding at the promoter, or you can have multimerization, kind of leads to similar things here. But also, we're going to talk about this idea of molecular titration. So if you have another protein that acts as kind of a sponge, then this connect can lead to a similar effect. And this is indeed observed in various natural contexts.**

**So this is motivated by a work by Nick Buchler, B-U-C-H-L-E-R. Turns out I was down at Princeton, no sorry, I was out at Duke yesterday, and so I got to hang out with Nick and talk about this work. I had previously told him that in my first lecture in the systems biology class, we like to discuss this molecular titration effect. He was instrumental in elucidating how it worked.**

**All right so let's go ahead and get started. So hopefully you all have these cards. We're going to start out with some simple questions, just to make sure that you know how to use the complicated devices that are sitting in front of you. OK?**

1

**So what we want to do is to start by thinking about a situation where you have two molecules. We're going to call them E and S, and of course, you can imagine what these might possibly stand for in one context or another. There are two rates here that are describing the rate that these molecules, E and S, find each other, Kf. And Kr is defining the rate at which this complex is going to fall apart.**

**So there's this forward rate that is sum Kf, times concentration of E, times the concentration of S. Now I'd say for the first part of this lecture, we will indeed use the chemistry convention of concentrations here, although we will quickly get tired of these brackets and we'll just start writing the letters. And hopefully it is self evident in the context that I'm referring to a concentration rather than something else, but if you're ever confused, please ask.**

**So this is forward rate, and then the reverse rate is something similar. So we have this Kr. Now this is just the concentration of the complex ES. Many of you have spent a lot of time thinking about how we often define things. This Kd, dissociation constant, is defined as the ratio Kr over Kf. Now, just so we can practice using our cards, what we're going to ask first is what the units of this Kd thing is.**

**Now, in general, when I ask such a question, I will give you some A, B, C, D options. You can start thinking even before I write down the options. Yes? I'll encourage you to think before I start writing down options.**

**So it's either dimensionless, units of concentration, 1 over concentration, 1 over time, and I will often include at the bottom something that simply is, don't know. And that is if you're really confused about what I'm talking about, then feel free to just flash me that, and that at least tells me that I'm gibbering nonsense.**

**So there's going to be a very strict set of rules for how we do these flash cards, all right? You don't get to vote before I tell you to vote. You have to keep on thinking. If you think you know the right answer, check limits, just do whatever it is to keep on thinking.**

**And then we vote simultaneously. That way, it builds up the tension, everyone gets**

2

**excited, and then you vote. It also provides me an opportunity to make sure that I can see that everybody's participating. So if you don't vote, then you have the opportunity to tell the group what you think the answer should be and why. And the cards they're both colored, and they have letters on there, so the letters correspond to the answer. We're all on top of this? Have you had a chance to think? Or has my talking bothered you? Both. OK.**

**So what we do is I'm going to ask, do you need more time? If you need more time, just nod or something like that, and if more than a few people nod, I'll give you more time. But you guys are totally all right. OK let's see how we are. So then I'll say, OK, we're ready. And then we're going to go three, two, one, and then I want a vote by your chest.**

**You don't need to display it to the group. It's just here, and then tell me what you think. All right, ready. Three, two, one. Broadly, people know how to use the cards. And there's a clear majority of the group, although it's not 100%, that are saying that this thing is a concentration. I'd say that if the group is maybe between 25, 75% correct on these sorts of things, then I will often have you pair off in, well, in pairs. And the goal there would be to try to convince your neighbor that you're right. In this case we're a bit above 75%, so I've already indicated what the answer is. Can somebody just quickly say, why is this a concentration? Maybe in the back.**

**AUDIENCE: So, we know that both rates need to have the same dimensions--**

**PROFESSOR: Yeah, and what are the dimensions of these rates? AUDIENCE: [INAUDIBLE].**

**PROFESSOR: OK. So, there are actually different conventions, in principle, but we will often be working in numbers in most of this class, in which case it would actually just be a 1 over time. But depending on whether you're doing chemistry-- So the numerators may be ambiguous, depending, but the important thing is that they're definitely the same. These are definitely going to be the same.**

**But it is true that in an awful lot of this class, we're going to be thinking about**

3

**numbers rather than the concentrations. Because, for a lot of the class we'll be thinking about finite number fluctuations of stochastic dynamics, in which case, concentration, who knows what's going to happen?**

**But these have to have the same units, right? And the important thing here is if you look at the right, you see this guy has an extra concentration up here. So, I think this is, on the one hand, a trivial point, but it's just really easy to forget about as you move forward. Because these things, they look awfully similar, right? There's a K, little subscript something, right? So just be careful about this kind of thing. Are there any questions about what I've said so far?**

**So in these cases. I think that it's really very useful to try to get some intuition for what's going on. These are all just definitions, but you want to ask, well, what happens if concentrations of various things move around? What we want to think about is just the fraction. And the reason we call this E is because, for now, we might be calling this an enzyme and, over here, a substrate, something that the enzyme is acting on.**

**But we'll see that, in many cases, we might be thinking about one of these as being, let's say, the piece of DNA, and then this is not even the substrate. Then maybe this is the RNA polymerase that will lead to transcription. So in various contexts, we'll think about these things having different molecular identities. But for now, E and S, possibly enzyme substrate.**

**So the question is, if for now we just think, these are just two molecules of whatever sort, at some concentration, and we just want to make sure that we are on top of what's going to happen if the concentrations of each of these molecular components goes either to 0 or to infinity. I think that before you do any math in life, it's good to just think about these sorts of limits, because it helps to make sure that your intuition is correct.**

**In many, many cases, if you think about the problem before you do any math, then when you go do the math, you'll get some solution. You can check to see whether your solution is consistent with what your intuition said. And if they disagree it**

4

**means you have to update either your intuition, or the solution, or maybe both. It's possible. But at least one of them has to be updated, and that's a way of both getting better scores on your exams, but also improving your scientific intuition.**

**So, in particular, we just want to do some limits. We'll think in the context, for example, if the total concentration-- your adding of the small S-- if it goes to zero, what we're going to try to get intuition about is this fraction of E-bound. It might be the enzyme. So the fraction of this thing bound, it's defined by the concentration of the complex, divided by the concentration of the enzyme, plus the concentration of the enzyme in the complex, assuming that this is the only two places that the enzyme can be located.**

**Now, these three arrows, that, in general, means a definition. So the question is, if we come here, what happens to the fraction of this enzyme that's bound? And, again, can't be determined-- which is different from don't know. And we're going to just do a few different limits so we want to maybe go through these quickly.**

**I'll give you 10 seconds to prepare your card. All right, ready? Three, two, one. So we're pretty good. So I'd say a majority, at least, of the group is saying that in this case, the fraction bound should go to 0. Intuitively, why should that be?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: A little louder.**

**AUDIENCE: You have nothing to bind. PROFESSOR: Yeah, right. So if there's no S around at all, then you shouldn't have much of this complex, right? But you still have some enzymes. This thing should go to 0, and that kind of makes sense. And, similarly, if you add a lot, a lot of this substrate? I'll give you eight seconds.**

**AUDIENCE: So, you're moving the substrate [INAUDIBLE]. PROFESSOR: Yes, so S total, this is the total. This is if you have a test tube, and this is the amount**

5

**of this sugar that you add in there. So S total, then, is the sum of that and S.**

**Do you need more time? Ready. Three, two, one.**

**So we have maybe an island of people that disagree. At least a majority are saying, in this case, it should have to go to 1. Of course, this is a limit and a limit. It's always going to be between 0 and 1, but in the limit, it does go to 1. So if you just add so much of the substrate then you should be able to saturate that binding and drive all of that enzyme into the bound state.**

**So this one is actually, maybe, a little bit more subtle. So what if we take this limit? I'm going to give you 20 seconds to think about it, just because it's roughly three times as hard as the last one. Do you need more time? Or do you think that you have something you believe in, that you're willing to turn to your neighbor and-Let's see where we are. Ready. Three, two, one.**

**All right, so this is good. So we have a fair distribution, and this is one that reasonable people might be able to argue about. It's worth having the argument. Give yourself 30 seconds, turn your neighbor, preferably a neighbor that disagrees with you, and tell them why you said what you said. If in a pair, you've already convinced each other of something, then go ahead and look around to see if there's another pair that has maybe settled on a different answer.**

**I think that you guys are still kind of passionately arguing, but maybe we'll go ahead and convene, and try to get a sense of-- I think, from the sound of it at least, there's some disagreement about the way to think about this. In general, if you want to volunteer an opinion or an explanation, what I like to do is, I like to tell the group what your neighbor thought. So go ahead, anybody, it could be a neighbor in quotes. Anybody want to volunteer one possible explanation of how to think about this?**

**AUDIENCE: Well, what my neighbors thought was if E total is defined as E plus ES, then as E total goes to 0, then this goes to 0 over 0 at some vague, unclear--**

**PROFESSOR: Yeah, although, right. So you're saying, maybe it's all going to 0, and then this is just**

6

**philosophy. Not that I'm putting words in your neighbor's mouth. So there's a sense in which this is true, but mathematically, and actually also physically, there are welldefined ways of taking such a limit, right?**

**So if you get 0 over 0, then you can use L'Hopital's Rule, which we'll have the opportunity to pull out sometime within the class. Of course, the most difficult part of L'Hopital's Rule is knowing how to spell it. So that's one answer, the mathematical answer, that you should be able to just take this limit and so forth.**

**But I think there is another physical answer, which is that this could happen, right? And something is going to occur, right? You could, in principle, measure. And even if you just had a single enzyme there, this Fb would be the fraction of time that that enzyme is bound. So this is a well-defined experimental question and the answer should arise from these interactions.**

**But then how do we edit it-- what does it all mean? How do we figure out the answer? What's another possible view on this? Maybe in the back.**

**AUDIENCE: My neighbor thought that, if there's a non-zero concentration of S, and the concentration of E goes to 0, then all E will be bound [? at some point ?].**

**PROFESSOR: This is interesting, right? So, if there's a finite concentration of S, if E goes to 0, then you say well there's plenty of S to go around, so I should always get bound. Is that what the neighbor-- that's another option. So, so far, we've had an argument for can't be determined, it's philosophy. We've had an argument for 1. Other possibilities? This is an interesting question, because depending on how you think about it, you can convince yourself that it's anything, right? Other possible answers? No.**

**AUDIENCE: So, I don't hear the good answer. I said E because, when there isn't very much E, then it's true that a lot of people go into yes, but yeah. I don't know what to say.**

**PROFESSOR: Now, that's OK. Another take on that answer, or a different one?**

**AUDIENCE: I don't know. If I had to complete that answer, maybe something like, but there still**

7

**might not be a total large concentration of either, so there might still be a decent chance for E to be around for a while without encountering some of S.**

- **AUDIENCE 2: So the forward reaction rate will also go to 0. Even though S is very large, the forward reaction rate will also go to 0, as the concentration [INAUDIBLE].**

- **PROFESSOR: By the forward rate, it's not necessarily a variable. it's just that it depends on the substrate concentration in this case. Other takes on it? This is interesting. So I'm going to argue that the most reasonable way to view this would give you-- as long as there is some finite concentration of that substrate around, and I think that there's a very well-defined sense in which it's going to go to some finite fraction. And I think that when you're thinking about this in the context of molecular kinetics, the chemistry of you, it still is all well-defined, but the way that I think that I get the most clear intuition is just to imagine myself as being that one and only enzyme in the test tube. Now there's going to be some rate that I bind to the substrates, right? And what's going to determine that rate?**

**AUDIENCE: The concentration of the substrate?**

**PROFESSOR: The concentration of substrate, right. So if I double the substrate concentration, what should that do to the rate of me binding? It should double it, yeah.**

**And then of course there's always this Kf somewhere in there, and some units, right? But there's going to be some rate that I bind. And then when I bind again? Now I'm just an enzyme substrate. Now, instead thinking about this in the context of chemical kinetics, I can just think about this from the standpoint of an individual molecule, where I'm a complex, S-bound, and there's some rate that I fall apart. And it's just the balance of those two rates of finding a substrate and falling part that's going to lead to this fraction bound.**

**AUDIENCE: Taking what you just explained, couldn't you think about it as E always either 0 or 1, because when you're--**

**PROFESSOR: Yeah**

8

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
