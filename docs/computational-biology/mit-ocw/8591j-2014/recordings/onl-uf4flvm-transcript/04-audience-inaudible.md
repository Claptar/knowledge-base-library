---
title: 'AUDIENCE: [INAUDIBLE].'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/onl-uf4flvm-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE].

**Source:** `recordings/onl-uf4flvm-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: So this is just saying, OK, the complex is formed as a result of binding of the inhibitor and the morphogen. It's proportional to concentration those two things, at that particular position at the particular time. And just remember that any time that you create something, if you have binding at two things together, then you have to consider these things going away. And it's not they're being degraded, it's just that they're forming this complex. So in these equations you just have to be very careful about keeping track of which things are really going away and which things are just changing form. Yeah?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Right. You're saying why that there's not a minus term? So this is an assumption. And I think this is a kind of thing that you have to be clear about in any of these, because that's always going to occur at some rate. And the assumption is that this is dominant. And then just be clear in words, what is this thing?**

15

**AUDIENCE: [INAUDIBLE]. PROFESSOR: Right. The protease. And you're saying cleaving inhibitor. AUDIENCE: Yeah, cleaving the compacts by degrading the [INAUDIBLE]. PROFESSOR: Right. So at a rate proportional to the Proteus concentration-- the complex concentration-- this complex goes away. Now the question is we have to figure out where it went or what happened, right? Well we have a minus alpha c here but then we have a plus alpha c here. But this isn't the morphogen right. This is at the rate that the complex somehow is being disappeared by the protease, the morphogen is appearing. But then, we don't have the same term here. And that's how you know that what the protease is doing is it's degrading the inhibitor as part of the complex. So by looking at these equations, you can actually figure out what are the assumptions that have been made of what the biology is that's being captured here. But in many cases, there are assumptions of what's big and what's small. And then what's this thing here? Somebody else that has not yet-- do these equations look familiar? Yes, please.**

**AUDIENCE: It's the protease [INAUDIBLE]. PROFESSOR: That's right. It's the protease degrading the inhibitor when the inhibitor is not down to the morphogen. Now of course, what the authors did next is they searched numerically across parameter space over [INAUDIBLE] magnitude, and they found that for some parameter regime there was a robust pattern of the morphogen developed in here. There's no reason for you to necessarily remember which thing it was. But what they found is that if this term went away and this term went away, then you end up getting a robust profile of the morphogen against changes in the overall morphogen inhibitor concentration.**

**Now this is pretty weird, I would say. I don't know, do you think-- is this one weird?**

16

**Weirdness is in the eye of the beholder. But I would say it's not so shocking. Can somebody say verbally what this would correspond to?**

**AUDIENCE: The protease doesn't degrade the inhibitor on its own.**

- **PROFESSOR: That's right, the protease doesn't degrade the inhibitor on its own, only when it's part of the complex with the morphogen. And independently there was experimental data already indicating that was true. So you could have if you want to just written the model without that, because there was already evidence for that.**

**But as I said, this is a pretty weird thing. And so, this would be saying that, for some reason, diffusion of the morphogen on its own is very small. In particular, small compared diffusion of the morphogen when it's a complex. Now can somebody say why I might think that's weird? You don't have to believe it's weird.**

**AUDIENCE: You'd think bigger is better.**

**PROFESSOR: That's right. Exactly. This is saying, well, when it's complex, it's bigger, it's somehow diffusing faster. So this would not happen do the simple Stokes type drag. This would have to be biology. Somebody's biology is allowed to do anything that doesn't violate the laws of physics.**

**Indeed, later there was experimental evidence of something like this was actually happening. And you could imagine having either from sort of active transport type dynamics for the complex, or from binding type dynamics of the morphogen.**

**I think the key thing to take from this example is just that, in general, we would like biological function-- biology would like biological function to be robust to things that are often fluctuating or varying. And that's one way to try to make guesses about what might be happening in the system.**

**This sort of computational exercise is not all a proof that this has to be what's happening. They wrote down a particular model-- it could have been that there are other terms they're not aware of and so forth. But it's at least a way of generating hypotheses that you can go and test.**

17

**And quite generally, I'd also say that its essential for all of us as consumers of models to be able to look at some of these equations and figure out what it is that they've assumed.**

**I want to move on to this idea of pattern formation via the reaction diffusion or Turing-type patterns. And I think it's really important to start by just acknowledging that this is really a surprising finding, that it's even possible for this to happen.**

**Because this is a situation where you have a couple chemicals-- or proteins, or reacting elements-- and if you just mix them, if you have them in some well mixed tube, they reach some steady state. Whereas somehow if you allow diffusion, then you can get these patterns. And I would say based on my intuition at least, I would not have thought that this would be possible.**

**And this really just is because if you can just imagine, you start with some profile. Now there's some structure here. But diffusion's going to actually cause this to come down, and this to come up. So diffusion acts to remove these spatial patterns. But somehow in some prime regimes, if you have coupled reactions that are activating and inhibiting each other, then you can actually get these spatial patterns.**

**And as you read about, there's some idea that you need to have a local activation and a global inhibition. But ultimately the mathematical-- you always have to go and think about more carefully about the math, and would be indicated just by those words. This is at least a way to guide your thinking a little bit.**

**But ultimately what matters are around this stable what would be the stable fixed point, you have to actually look at these derivatives and so forth. And the derivatives can be subtle I would say. Just because you think of something as activator inhibitor doesn't mean that it's going to have that role around the fix point that you're studying. So this is just a caution.**

**What I want to do is just give you, for example, one example of a simple model that does experience these Turing patterns. And in an appropriate regime. And this Levin-Segel model of pattern formation.**

18

**And this was published in 1976, and it was actually meant as a model of predatorprey interactions in ecology. We'll talk significantly more about predator-prey interactions in a few weeks. But I just want to write down what they said.**

**And this is a simplified model of their stuff. So it's actually trying to think about some plankton herbivore before interactions. And this is derivative with respect to time. We're going to follow the nomenclature of a paper by Butler and Goldenfeld a few years ago, because they're the ones who thought about the demographic noise enhancing the patterns.**

**PROFESSOR: All right, so we have [? phi ?] and [? phi. ?] First of all, who's eating whom? All right, we're going to say it verbally. Who is the predator? Ready three, two, one.**

**AUDIENCE: Herbivore.**

**PROFESSOR: Herbivore. Herbivores are not what they used to be. So indeed, the herbivore benefits from the presence of the plankton. So nobody cares about plankton, I guess.**

**So this corresponds to the predator-prey type interaction. So there's some death rate. So let's see, the herbivore or the predator. And then what you see is there's these two growth terms for the plankton. So there's this term, which would be kind of simple, exponential growth. And then this term, which is actually some sort of super exponential growth.**

**There's some sense in which the plankton benefit each other. And this was originally introduced because of something called predator satiation. But it's just a general reflection of the fact that in many cases, individuals benefit from the presence of other individuals. And in particular, this is known as the ally effect, and we'll spend time talking about this in a few weeks as well in the context of populations and ecology. For now, I just want to use this as an example of a model that gives you these Turing patterns.**

19

**So if you want to, you can go ahead and ask, well, what happens if we just have a well mixed situation? If everything is not a function of x, but it's still can to be a function of time. You can solve these equations, and you can find what the steady states are equal to. So there is indeed a steady state stable coexistence of the predator and the prey in a well mixed situation.**

**However, if you then go and you analyze the stability of different spatial modes, what you'll find is that in some situations, particular wavelength or wave vectors become unstable. And it's just over some range of wavelengths, and that corresponds to the wave length of the Turing patterns that you'll see.**

**If you're curious about these things in more depth, I encourage you to attend Mehran Kardar's class Statistical Physics in Biology, he is an expert on these topics and I think is a wonderful clear lecturer.**

**Now there's going to be some condition for these things leading to Turing patterns. Now from your reading, do you think it's going to be mu--? So this is Turing patterns require-- I'll give you 30 seconds to think about what. Do you need more time? I'm not sure where we are. Maybe another 15 seconds just to--**

**Let's see where we are. Ready three, two, one. OK, we're all over the place. I think we're uniformly distributed between A, B, and C. So there's an idea that you're supposed to have so-called local activation and global inhibition. Why don't we turn to a neighbor and see if you can figure out what's going on.**

**OK, why don't we reconvene, I'm curious where you're thinking is. Let's go ahead and vote. Ready three, two, one. OK, so we have many, many C's. The idea that some mu has to be much less the nu. Yes. I want to make sure. All right, mu is telling us about the diffusion coefficient of the prey. Nu is the diffusion coefficient of the predator.**

**So what you want is to have local activation. And the thing that's activating itself is the plankton. So you can see that that's like, for example, psi squared term. And from the stand point of a spatial situation, you can say, all right, well, let's say we**

20

**have some region with a lot of this prey. Well, it's able to activate itself, so it kind of comes up. And as it does that, it is creating more of the predator, phi.**

**But because the predator has a larger diffusion coefficient-- well, it's obviously going to grow here. But it will also diffuse away. And that's this global inhibition of neighboring regions. Now of course, these are just words, you have to take it a little bit of a grain of salt.**

**But if you can actually do this calculation analytically, and derive in this model the condition for Turing patterns to emerge as a function of everything. And for example, if you have b 1/2, p 1. So for unity type parameters, then the requirement to get Turing patterns is that nu over mu is the greater than 27.8.**

**The key thing though is that this thing is much larger than 1. So a general thing that emerges in these Turing patterns is that you need this so-called inhibiting type partner to have a much larger effective diffusion coefficient than the activating partner.**

**Now the problem with this is that this thing is indeed much larger than 1, which limits the overall usefulness of this is a mechanism. Because if it really is simple diffusion, how much bigger would the-- let's say, low Reynolds number regime, these are just molecules experience diffusion. How much bigger does the-- this is so confusing.**

**So this is big and this is little, right? So how much bigger does the activator-- they're too many things to keep track of here. It's because I don't have anything written down. So that's the activator. So this one's the activator, and this one's the inhibitor. And the inhibitors has to diffuse much more than the activator. So the inhibitor has to be much smaller than the activator.**

**OK good, so how much bigger does the activator have to be than the inhibitor for this to be true? Does it scale as this 28 or 28 squared or 28 cubed? In terms of radius, how much? Scales linearly, remember? Einstein equation, you guys had fun thinking about on the exam. KT over gamma.**

**This would require, for example, the activator to be 30 times bigger in terms of**

21

**radius. And the inhibitor, in order to have this emerge just as a result of diffusion, simple diffusion. And that's just not a typical thing for just a range of protein sizes. But you could imagine putting up various ways to make this happen.**

**But there is a very nice development that I mentioned, which is that there's another surprising aspect in these problems, which is that in many cases, demographic noise can lead to patterns-- -- or maybe you might call them quasi-patterns. But things that, for all intents and purposes, look like some of this pseudo-periodic. So there's a pseudo-Turing pattern, maybe.**

**And indeed, if you actually do this simulation with those parameters where you do the explicit demographic fluctuations-- i.e. you take into account that this corresponds to a prey giving birth. This corresponds to a predator eating a prey, random events just like what we've done in the context of a Gillespie simulation.**

**Then what you find is that with demographic fluctuations or demographic noise, then the condition here nu over mu has to be only 2.48. And indeed in Butler and Goldenfeld, they derive these things using field theoretic approaches. There was a 2011 paper and also 2008 or 2009.**

**The nice thing here is that what you see is that in the presence of these demographic noise that will be there, the difference in diffusivity that are required is not nearly as large as when you're thinking about the mean field equations. Are there any questions about this before we talk about center fighting in E. coli? Yeah.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: OK, now you're thinking about the actual plankton-herbivore. I think there are many things to say. One of them would just be that maybe the patterns that you see between actual plankton and actual herbivores is not due to the Turing mechanism.**

**For the Turing mechanism to be at play to generate spatial patterns, it requires that this inhibitor do something equivalent to diffusion more rapidly. It has to have to move away more rapidly.**

22

---

[← AUDIENCE: Decrease faster [INAUDIBLE].](03-audience-decrease-faster-inaudible.md) · [Up: contents](index.md) · [AUDIENCE: [INAUDIBLE]. →](05-audience-inaudible.md)
