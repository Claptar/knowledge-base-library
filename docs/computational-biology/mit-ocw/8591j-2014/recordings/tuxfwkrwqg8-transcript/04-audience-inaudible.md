---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/tuxfwkrwqg8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/tuxfwkrwqg8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Yeah, it's maybe 30 microns. So there's this idea that a cell might go like this for 30 microns. And it takes about a second for it to do that. But then that's a run. But then it'll engage in some random tumble that leads it to go some other direction, and then another tumble, and then it kind of goes a different direction, and so forth. So these are runs and tumbles.**

**Now, the nice thing here is that you can see that to measure this concentration over here, the change of concentration across the cell went as a, which might only be 1 or 2 microns, whereas here now the E. coli can measure a change in a concentration over tens of microns. So it's in some ways like a longer antenna that allows it to pick up the signal better.**

**There's a comment about what happens here in the sense that if you imagine you have a cell, it's a few microns in size, flagella is pushing it, it's going at 30 microns per second. The question is, if at some time it stops spinning its flagellum, how far will it coast? And this is after stopping swimming.**

**OK, so we'll do an approximate, so 10 micron maybe. How many microns does a cell coast after it stops swimming?**

21

**AUDIENCE: This is a bacterial cell? PROFESSOR: This is a bacterial cell. This is E. coli, and this is, we'll say, 3 microns in size. Ready- three, two, one. All right, OK, so everybody says-- and is this actually the right answer? AUDIENCE: No. PROFESSOR: No, it's not. So this is the closest, it's true. But none of these things are true. So how far does it coast? [INTERPOSING VOICES]**

**PROFESSOR: Right, yeah, so it's some ridiculous-- I mean, and this is really, really weird. This guy-- 30 microns a second. So this is 10 times its body length every second. It's really shooting along. But the moment that it stops swimming, it stops moving. So it's none of these things. It was 1 angstrom or less than an angstrom?**

**AUDIENCE: 0.1. PROFESSOR: OK, 0.1 angstroms, which this is 10 to the minus five microns. OK, so it's orders of magnitude smaller than you would ever imagine. And that's because our intuition comes from kind of our length scales where if I were swimming this fast, I would keep on drifting after I stopped swimming. But that's not the world that bacteria live in. And that's because of the low Reynolds number.**

**The Reynolds number is much, much less than 1. So this thing is the dimensionless number that quantifies the relative importance of inertial forces to viscous forces. Now there was some discussion of the Reynolds number in your reading. I maybe won't get into too much detail about it. But what I'll say is that if anybody wants to talk about a way of thinking about the Reynolds number, maybe you can ask me after class, and I can explain to you why this weird expression can be thought of as the ratio of the inertial to viscous forces.**

**But I want to think a little bit more about the strategy that these cells are following,**

22

**which is, why is it that a run is of the length scale that it is? In particular, why not go further? We already said that its ability to measure concentration is somehow-- if you did a direct measurement, it would scale with the size of the cell. In this case, it sort of scales like the length of the run. So why not run for 10 times longer, 100 times longer, so you can get a really good measurement of a gradient?**

**AUDIENCE: Because if you're going the wrong way, then you'd go 10 times longer.**

**PROFESSOR: OK, so it could be just if you're going the wrong way. Although then we could maybe even be just more sensitive in that. Because what's striking is that even when it's going in the right direction, it still tumbles. The difference between the run lengths and the correct and incorrect directions are kind of modest, I guess.**

**So maybe we could come up with a different strategy where we say, all right, well, if I feel like things are getting worse, I'll tumble quickly. But if I feel like things are going great, maybe then I'll go in the same direction, and I'll measure that gradient really finely so I can get precisely the right direction. So I guess the question is, is there anything that's going to limit how useful it is to go swimming, even in a good direction, in principle? Yeah.**

**AUDIENCE: So it's so small that collision with actual molecules can randomize its direction as it goes along, and it sort of loses memory.**

**PROFESSOR: And this is a weird thing, that not only does diffusion act kind of in a linear sense on the center of mass position of an object, but it also acts rotationally, which means that the cell and other objects in liquid lose their orientational order. What that means is that if this cell starts swimming in one direction, it's actually the case that after a few seconds, it forgets where it was going. So you can't actually collect information about the gradient in that direction, because you're actually going in a different direction from what you were a few seconds ago.**

**This is actually a pretty tough limitation that these cells are facing. On the one hand, they're small, so it's really hard to measure gradients. On the other hand, every few seconds, they get turned around. And if you imagine trying to navigate in that kind**

23

**of situation, it would be pretty hard.**

**Now, I want to make sure that we understand how to figure out what the timescale is that this orientational order is lost in. And again, we're going to use dimensional analysis, because I love it. And I can tell that you guys are big fans as well.**

**OK, so I will tell you something that hopefully-- how much do I want to tell you? What I'll tell you is this, that the diffusion coefficient for angular fluctuations is defined just the way it is for diffusion coefficient for the center of mass. Given that, the question is, if I have a sphere-- again, size a-- now I want to know, how does the typical correlation time, the time to randomize, randomize orientation, how does it scale with the radius?**

**So it could be that this timescale tau could go a to the 0. And you should be starting to think. All right, do you need more time?**

**All right, why don't we go and see where the group is. And it's OK if you've not figured it out. Make your best guess. Ready-- three, two, one. OK, so I'd say it might be a slight majority B. But then actually there are fair numbers spread around.**

**Yeah, there's A, B, C's, D's, and E's. All right, maybe I'll give you a minute to talk to your neighbor. And I'm just going to give you an extra hint, which is it's good to look at the units of the diffusion coefficient, which is why I wrote this equation.**

**Yes, no? You did that. You're like, that's what we did. Well, I'll give you another minute. Because I think that it's important to work through this at least some way mentally.**

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [[INTERPOSING VOICES] →](05-interposing-voices.md)
