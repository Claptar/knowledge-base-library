---
title: fancier situations.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/3eizij6qncy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# fancier situations.

**Source:** `recordings/3eizij6qncy-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**It is worth saying, though, that this approach, I mean it looks very physics-y, in the sense that physicists like simple equations where we add diffusion and so forth. But this is not what a physicist came up with.**

**These are classic ideas in evolution and ecology. The solution to this was originally done by Fisher. So this was in the 1920s or so. So a long time ago, originally to try to understand not the spread of a population but the spread of a beneficial allele in a spatial population.**

**And once again, this highlights the deep connections between evolution and ecology. You can have a genetic wave in space of a of a beneficial mutant spreading, or you can have a population wave of an invasive species or whatnot, and you end up getting very similar dynamics.**

**So the basic idea, here, is that, if you look at the density as a function of position. If start with, there's one individual. What's going to happen? It's going to start dividing, right? So we kind of get up. And it's going to come up. And eventually it's going to saturate at this carrying capacity, K.**

**And then you end up getting these spreading population waves that look like this. And the reason we're calling it a wave is because the shape of this front is the same over time. So it can really to be described as some function x minus vt.**

**And we are going to, maybe, typically assume that we're in a situation where we don't have to think about the left and the right, because it's just too complicated. So we'll just imagine it being that it's at saturation here, and then we're looking at some front that's moving to the right.**

**Now, by dimensional analysis, we should be able to figure out what the velocity is going to be. Remember how much we liked dimensional analysis in this class? Yes. So what we're going to do is I'll give you some characters that you're going to be able to use in your quest.**

27

**So we can use r, K, D. I'll give you a square root in case you find it useful. And you can raise something to the second power as well. So what you can do is you're going to set up your cards so that when I look at it, from the left to the right, it will describe the velocity of this wave.**

**I'll give you 30 seconds. So this is dimensional analysis for this wave velocity.**

**All right, do you need more time? Yes? OK, that's fine.**

**All right, let's go ahead and vote. Construct your answer, remember, from me, from left to right. Ready, three, two, one. All right. We have trouble. A key skill is being able to imagine yourself in someone else's shoes. So if I'm viewing-- but that's OK.**

**So we have, here, this is kind of units of 1 over time. This is what length squared over time. Whereas this is a density. If we want something that is a length over time, then we're going to end up having to take r times D and take a square root.**

**So this should be DAC, which is a square root of-- of course, it depends on how you're entering it into your calculator, if you have scientific calculator or something else, maybe. And indeed, it ends up, there's a 2 here. So this is the velocity. Yes?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: I see what you're saying. But it ends up not being true. These derivative signs don't have any units. So this still has units of a density divided by a length squared. So for unit purposes, you just look at this thing and at this. This squared does mean there's a length squared in the denominator, but this squared doesn't do anything. So D is still a length squared over time.**

**So this is the famous Fisher velocity. There are some mathematical subtleties to all of this that we're not really going to get into. I don't know. I'm having trouble-velocity. There are a few features to highlight.**

**If the organism grows faster, the wave is going to spread faster. That make sense? If it has a larger mobility, it also moves faster. That makes sense. Of course, the**

28

**velocity is given by both of those things. So this wave coming out really is a population level property.**

**Because it's not just growth. It's not just motion. It's a result of the coupled division and diffusion that leads to this population wave spreading. Importantly, to first order, it doesn't depend on the carrying capacity, at least within the deterministic regime.**

**AUDIENCE: It's interesting that, if the reproductive rate goes to 0, suddenly the population stops spreading.**

**PROFESSOR: So first of all. You'd say, oh, it would be sort of surprising if it really kept on spreading in the absence of growth. But what you're pointing out is that, if you just, at one moment, turn off division, then there will still be diffusion. It'll still keep on going.**

**But this is the velocity of a wave when it's a wave. When it's described by a function like this. So it's true that you could turn off division, and it'll still diffuse. But then the shape is changing as well.**

**I'm going to draw a few lines describing possible populations. Now, let's assume that they have the same motion, diffusion. I want to know, which one has the largest velocity? Is it A, B, C, D? It's the same diffusion. Per capita growth rate as a function of the density for three different organisms.**

**Ready, three, two, one. All right, so I'd say we have a fair number of B's, D's. It seems like it's B versus D. Now, this is tricky because D, we have not explicitly considered here.**

**But it turns out that the answer is B. Certainly, between these three, these are all really logistic growth functions. And so from the standpoint of here, it's just this r. And r is the division rate at 0 cell density. The per capita growth rate at 0 cell density is what determines the velocity in a Fisher wave.**

**And indeed, that's true even if there's no decrease in the growth up right until you get to some carrying capacity. And indeed, all of these cases, the division rate and**

29

**the growth rate that's relevant for the velocity is when it hits this axis.**

**And indeed, all of these waves are described as Fisher or pulled waves. Because there's a sense that the entire wave is determined by the front of the wave. So we drew this profile. I didn't do that very well.**

**Here, this is an exponential. And the exponential actually is what's pulling this wave. There ends up being a characteristic length scale here that is the square root of D/r. So this is the length scale of the exponential.**

**And the velocity and the length scale are only functions of the division rate in the limit below cell density or low density of organism. The shape of what goes on here changes, indeed, the bulk properties of the wave, but doesn't change the velocity.**

**And I just want to make one comparison of all this to-- because there's another qualitatively different kind of wave, which is a so-called pushed wave. And that's what happens if you have an Allee effect, particularly like a strong Allee effect. If this thing looks-- like this is certainly possible. This is an Allee effect.**

**Now, if you just said, oh, the only thing that matters is the growth rate at low cell density, you would say, oh, this thing cannot possibly expand. Although it turns out that it still is possible. And in this situation, it would be called a push wave, where your profile somehow maybe looks kind of similar.**

**But instead of it being the front of the wave that's pulling the wave, it's diffusion around the bulk. Because the bulk is the part that is actually happily growing. Because the front, here, in this case, is dying. Yet it still is possible to have a positive velocity.**

**And so this is, then, a qualitatively different kind of population expansion. So cooperatively growing populations expand very differently from logistically growing populations. And one of things that the reading in Physics Today talked about is these different rates of loss of heterozygocity and so forth in different populations.**

**And as you might expect, the pulled waves have a smaller effective population size**

30

**than the pushed waves, because, here, the relevant population is at the front if it's a low density. Whereas here, the relevant population is the bulk that's at high density. With that, I think we should quit. But I will see you on Tuesday. And we'll talk about this neutral theory in ecology. Thanks.**

31

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md)
