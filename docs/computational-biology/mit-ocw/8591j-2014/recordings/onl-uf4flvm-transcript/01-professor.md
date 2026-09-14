---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/onl-uf4flvm-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/onl-uf4flvm-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Today what we're going to do is we're going to talk about some of the big ideas in class. Today what we're going to do is talk about pattern formation in biology, some of the different mechanisms that are employed in development and other contexts in order for organisms to figure out where to put things.**

**Now before I get into that too much, I wanted to make couple administrative type announcements. So first, we have graded the exams and we'll hand them back at the end of class today. If I try to forget then please somebody remind me.**

**What we're going to do is we're going to start by just talking about diffusion a bit more. I think that there's a fair range of different maybe experiences thinking about diffusion and what it can do for you. So we'll work on our intuition a little bit. And then I'll say something about the reading that you did from [INAUDIBLE] book about robust mechanisms for pattern formation in the context of development.**

**So simple diffusion with degradation leads to these exponential profiles that are not robust to changes in the concentration or production rate of the morphogen. Whereas if you have self enhanced degradation then this leads to power law fall off it's more robust to the concentration of this morphogen.**

**Then what we're going to do is transition to these turning patterns, reaction to fusion systems where you can have a really surprising effect, whereby in a well mixed situation these chemicals or proteins or reactants, they might just reach a stable state.**

**However, once you add diffusion, then you can start getting pattern formation, which is a very funny thing because diffusion is normally something that's smooths out profiles. Normally we think about diffusion as being something that removes**

1

**patterns and indeed that's generally what happens.**

**But following from this class of work from Alan Turing at the end of his life, he showed that it's actually in principle possible to have the emergence of patterns from diffusion. And we'll talk about some of the ways that could possibly happen.**

**So Turing patterns are already a surprising case where diffusion leads to patterns. There's another interesting phenomenon where if you add another source of noise that-- again, you think noise, demographic noise, the random creation destruction of individuals or chemicals or proteins.**

**Normally, we think this should also kind of be a force for removing patterns. But there's been a number of pieces of work over the last decade showing that in some cases, demographic noise can actually lead to patterns either in space or in time. We're going to talk more about this in the context of these so-called noise induced predator-prey oscillations.**

**But since we're talking about patterns here I will tell you something about how such noise can enhance the formations of patterns in the context of the Turing mechanism. And then we'll end by talking some about recent work of how E. coli find the center of their cell when they want to divide.**

**So you can imagine this is not an obvious thing to figure out how you might do. And we'll talk about the so-called Min system that E. coli use to find the center of the cells so they know where to septate, where to cut off and make two cells.**

**So I just want to start by making sure that when we talk about diffusion, we're all talking about the same thing. Now, hopefully for those of you that have not been thinking about diffusion so much recently, you did read the notes that Alexander Van Oudenaarden put together for Systems Biology a few years ago. I think it's useful, but in addition to the math, as maybe many of you know I'm a huge fan of graphical representations of ideas.**

**So I just want to make sure that we all agree on some of the basic ideas of how, for example, we get flux in the context of diffusion. So imagine that we have a one**

2

**dimension system where there's some chemical with concentration c. We can imagine, for example, it starts out looking like this. This is a concentration profile as a function of position x where we have maybe a box of length l. Concentration of some chemicals of function of position x in some space.**

**Now I just want to make sure that we're all thinking about the same thing. So it starts out some concentration of c1, over might be some c2. Linearly here. I just want to make sure we all agree on the magnitude of the flux at some different points.**

**So, in particular, we can think about A, B, this is capital C. So where is the magnitude of the flux largest? A, B, C. D corresponds to them being the same. E as don't know. Are there any questions about the question? Yes.**

**AUDIENCE: On the y-axis, you're plotting concentration?**

**PROFESSOR: Yes, this y-axis is the concentration is the function of position x. All right, I'll give another five seconds to think about it. All right, do you need more time? Let's vote. Ready three, two, one. OK, great. So I'd say a vast majority here are agreeing that it's going to D. The flux is going to the same everywhere.**

**Now the flux-- can somebody remind us? We'll say the flux of J. And what is it going to be? So there's a minus D times the change in c with respect to x. This was derived in the notes.**

**So this is highlighting that what leads to a flux is the change in a concentration with respect to position. And so it doesn't matter that the concentration is higher here than here, we have the same flux. And the flux is in which direction? Left, right, up, down? Three, two, one. Left, so the flux is here.**

**Minus sign-- like always, it's hard to remember from equations whether they're plus minus signs but you should be able to just remember you can draw something like this and say OK, this is a positive DCDX, so flux is going to be in the negative direction, right?**

3

**Now, what will be the change in the concentration with respect to time at this point right now? So this is change in the conservation at point b with respect to time. Is it greater than 0, equal to 0, less than 0, or can't determine? Does everybody understand the question I'm trying to ask?**

**Change in the concentration at this point with respect to time, at this time that's wrong. I'll give you 5 seconds. Ready? Three, two, one. OK. And so this, again, it's pretty good but not everyone. So it is going to be b. Can somebody explain why it's b here? Yes.**

**AUDIENCE: There's as much flux coming in as coming out on the other side?**

**PROFESSOR: That's right. So it's true that there's a net flux here coming to the left. But from the sample, if we want to know whether there's a change in the concentration at that point, we need to know what's the net number of particles moving to the left verses the net particle number there that are coming in from the right.**

**Now of course, on this left face-- if I draw a little box here-- are all the particles crossing this position? Are they all moving to the left? No. So the idea is that all the particle motion is random.**

**And indeed, there's only a slight access of particles moving to the left as compared to the right. In the sense that, if you look at the concentration there, the concentration is rather large, it's only a little bit larger to right than to the left of this plane. Which means that there's only a slight excess of particles defusing to the left as coming to the right, but that leads to a net flux of particles crossing this plane to the left.**

**So where will the concentration be changing? At this point here will the concentration be changing with respect to time? Ready three, two, one. No. So well does it change at all ever anywhere in this example? Is this a steady state profile, yes or no? Ready three, two, one.**

**AUDIENCE: No.**

4

**PROFESSOR: No. What should be the steady state profile?**

**AUDIENCE: Flat. PROFESSOR: Flat, OK. So how does that come about if the concentration is not changing any? Yeah. AUDIENCE: It'll only change at the edges. PROFESSOR: It's only changing the edges initially. Now, it's important to note that it's not that the concentration profile is not going to start looking like this. So that will not actually be how it-- eventually it's going to be flat. But it's going to smooth out on the edges. Do you guys understand what I'm trying to say? It's not that it's a line that kind of goes like this, but instead we do end up getting curvature. One more of these, and then we'll consider ourselves to be expert diffusionists. All right, so let's say the concentration as a function of position looks something like this. What I want to know is, where is DCDT maximal? We have some different points. We have A, B, C, D. Five seconds. Ready three, two, one. All right, so we finally got a lot of disagreement. I like it. Turn to your neighbor, you should be able to find somebody that disagrees with you. What is it that determines? AUDIENCE: [ALL DISCUSSING]**

**PROFESSOR: All right, did you guys all agree? You all agree on it? OK let's go ahead and reconvene. And let me see, maybe they were forming the domains of some sort. All right, ready. Wait, he says, no, no. All right, OK, one question. AUDIENCE: Is this instantaneous in some sense? PROFESSOR: Yeah. AUDIENCE: Exactly at the inset.**

5

**PROFESSOR:**

**All right, so I guess what I would say is that this is concentration profile at some time as a function of position in time. If you want to know the concentration profile some time delta t later, right? t plus delta t. Well then, it's going to be the concentration we had before then a little bit. Plus delta t times the derivative with respect to time.**

**Right, so this is the concentrate file at this time. And I want to how much is it going to change in the next delta t? And I'm assuming, of course, that I'm not adding any particles or taking any particles away. So just do the diffusion.**

**All right, let's see where we are. Ready three, two, one. OK. All right so it's we got domain, definitely some domains. All right. Well, it's going to end up being A, as I think the majority of the group is now saying. And why is it a?**

**AUDIENCE: Because of the second derivative.**

**PROFESSOR: Second derivative, right? So just what we said before is that, if we wanted to know the change of concentration with respect of time, at this point that was zero. Because the flux particle was leading that point and the flux coming in were the same. And we can also think about the second derivative.**

**So this indeed just from fix, like I said, was first law/ we got a D, so this gives second derivative c with respect to x squared. So that's a 2. What this is saying is that, to determine how rapidly this concentration is going to change at a particular point with respect of time, we need to know the curvature of the concentration with respect to position.**

**So many people were saying c here. And actually, this is where the concentration will remain exactly constant over this next delta t. And of course, if we want to know about what the concentration is going to do for a long time, then we have to do something more subtle.**

**But if we want to how the concentration is changing right now, then we just look at the curvature. And indeed, the curvature here is maximal. So concentration DCDT at this point, is it going to be greater or less than 0? Ready three, two, one.**

6

---

[Up: contents](index.md) · [PROFESSOR →](02-professor.md)
