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

**Less than 0, right? Now, it's true that only the curvature at a particular point and matter is to know how the concentrations going to change over this next delta t. But if you want to know about what's going to happen over longer periods of time, than you have to worry about more of the global structure.**

**And what's true is that this local maximum may quickly go away. So you don't have to wait very long before this thing gets smooth and then DCDT will-- the magnitude will go to 0. And sometimes this big hump will stick around longer, but because of the curvature, this has the maximal magnitude of DCDT.**

**And it makes sense that the concentration is going to go down because the net flux here is to the right and to the left. And so there's a net flux, particles leaving, concentration is going to come down. Now are there any questions about what we've said?**

**If you find this discussion confusing, I would strongly encourage you to get together with a friend and just draw some random lines, curves, and just make sure you understand where diffusion is going to pull things and so forth. No questions?**

**All right, I just want to say a few things about the so-called French flag model in development. This is perhaps the most famous. Does everybody know what the French flag looks like? What's that? All right. There are three stripes and some orientation.**

**No, but the idea here is just that a simple way to specify a structure across one axis is to have a defusing chemical or generally a protein. And then based on the concentration of that protein or morphogen, you can just have the tissue read out what it's supposed to be, or what it's supposed to do.**

**So the idea here is that, you have some morphogen that starts maybe on one end of an embryo and then diffuses. So we end up with some curve that tells us about the morphogen concentration as a function of position. This is a functional position. So this is along the embryo.**

**Now the general challenge in the context of development is asking-- we started this**

7

**embryo with many different cells, they're all genetically identical, and they all start out maybe without any positional information. They don't know where they are. But what that means is they don't know they need to develop into a head or a tail or something in between.**

**Now what often happens is that you can have a deposition often by the mother so you have a maternal deposition of, say, RNA that leads to expression of some morphogen on one end and then it diffuses. And based on the concentration you can say what part of the body you should be developing into.**

**So the idea is you just have these thresholds that might be some M1, M2. All right, now all the cells over here know that they should maybe develop into a head. Over here, they're going to develop into the mid body. And over down here it could be the low body, for example.**

**So just from the concentration that a cell feels at a particular location. So if you had a cell right here, you just say OK the concentration of morphogens between M1 and M2 and then from that you know what l you're supposed be.**

**Now if you have no degradation within the body. Let's just imagine you say, that at one end is 0. We're told morphogen concentration is M0. And let's say that the other end, we know the morphogen concentration is going to be 0. Let's say there's a lot of degradation at an end. If there's no degradation in between, what should the profile look like given these?**

**So, no. All right. So just diffusion with these boundary conditions. I'm going to draw some options and hopefully you can close your eyes and imagine what it should be. All right, we know that starts out M0 over L is equal to 0. Is it closer to A, B, C, or D? Do you understand what I'm asking? Yes.**

**AUDIENCE: That is a steady state.**

**PROFESSOR: This is the steady state concentration profile of the morphogen given there's no degradation in the interior. Ready three, two, one. All right. So at least a majority are agreeing it's going to be B. Although, there's a significant minority that's saying A.**

8

**This is why I'm bring this up because, we're so used to seeing exponential profiles and think that you should always be getting them. And I want to be clear why it's an exponential profile. That's the thing we start with, and for example this model in [INAUDIBLE] book.**

**Noori's book, you get exponential profiles as a result of first order degradation. Whereas if you don't have any degradation in the interior, then we say, OK, DCD-well, do we want to use C or M now? We'll use M, just because now we're thinking very particularly for morphogen.**

**All so DMDT. We want to know the steady state profile. We set this thing equal to 0. Integrate twice. Right, so we're going to get-- morphogen profile should just be some Ax plus B, OK? My line's kind of crappy, I'm sorry. However, when we have first order degradation, then we get these exponential profiles. Are there any questions about--?**

**AUDIENCE: Is it possible to have [INAUDIBLE]?**

**PROFESSOR: Yeah, right. What does this require?**

**AUDIENCE: The morphogen is generated into halves. X equals 0 and then--**

**PROFESSOR: Degraded it at--**

**AUDIENCE: Disappearing.**

**PROFESSOR: Yeah. Right. That's what I'm saying, is that when I said that at the end it was a 0, this means that we have degradation at this point. Any time that the morphogen reaches the end of the embryos, it gets degraded. So it's not degradation inside if it's only degradation here.**

**And this of course a situation where you have constant flux throughout the embryo, constant rate of production of the morphogen, constant rate of degradation over here. But when you have this first order degradation-- if we're told that instead-well, maybe.**

9

**So, if in addition to having diffusion, you also have this first order degradation. Now remember M is a function of both x and t, right? And this is the situation where we get exponential profiles.**

**Now in Murray's book, he often discusses this where the boundary condition is that you have some concentration M0 at one end. And then we get an exponential profile here. What was the characteristic length scale? This is something we should be able to figure out. You should, of course, be able to solve the equations, but you should be able to figure it out from our favorite approach of dimensional analysis. What's the units of things here? So units of D is what? Length squared over time. Units of alpha? So this is a morphogen concentration over a time. This is a morphogen concentration. So this thing has to be one over time.**

**So the length scale is then going to have to go as the square root of D over L. And indeed, if you solve it, it's exactly equal to that, but this dimensional analysis just told us that it had to scale like that. So this is telling us about a characteristic length of which this morphogen profile is going to fall off. This is the characteristic length L.**

**Incidentally, you'll see many cases of things that look like this. So if there's first order rate that's something is either degraded or is uptaken or whatnot, then together with diffusion, you'll get an exponential profile with a [INAUDIBLE] length scale that's given by this ratio. And you'll see this in many different contexts of, for example, nutrients going into a biofilm. If you have cells picking up nutrients then it's not that it's being degraded, but it's being imported. Then you'll have a similar process.**

**This is a nice, fine situation except for what was the problem that [INAUDIBLE] pointed out? It's not robust. It's not robust against what? Initial condition. Yes, but I think we have to be a little more specific on that. Right, it's not robust to changes in M0.**

**Incidentally, in most context, I think for mathematical simplicity, it's useful to just have a banner condition where M0 is constant. But in general, is that what the**

10

**mother is going to be fixing necessarily? What would the mother typically be fixing? What was that?**

**AUDIENCE: Production rate.**

**PROFESSOR: Production rate. How do we figure out what the production rate is in this situation? That's right, the flux ware. That's right. The production rate is the flux right at or just to the right of 0.**

**Incidentally, where's the flux maximal here? Is it maximal at A, B, or C? Ready three, two, one. You can do it verbally. Fun. A. Right. And that's because the profile steepest here and then shallows out. So flux is decreasing here. And that's because some of the morphogen is being degraded.**

**So indeed, we can figure out the production rate. Right. This is equal to the flux, which is equal to minus DCDX at that location. Right, so the morphogen profile M is a function of x is some M0e to the minus x over L, where L is given by this character of lengthscale, right?**

**So if we ask what's DMDX? Well, it's going to be-- we get a minus M0 over L. Evaluated at x equal to 0 just makes that go away, so we end up with this. So you figure out what flux is, right?**

**Yeah, so, it's just an extra couple terms, it's fine. But that would be what would typically be constant because there might be some RNA deposit there or if it's actually transcription off of the genes at in the cells in this location and then it's based on whether there's one or two copies and so forth.**

**So this is all fine, except that this thing is not robust. It changes in M0 or this production rate. Whereas in many cases, what we seek experimentally is that if we, for example, have the production rate, then the profile that we see out here is somehow remarkably similar. Yes?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Right. Yeah, OK. So I'd say that in many cases, it's not that it's directly this M**

11

**squared business. But there are a number of cases in Drosophila, where they actually do see this. In many cases, it was a self enhanced degradation but not that it was directly, it was via binding to a receptor.**

**So this was seen in patch lists together. I want to remember which were the models that-- I'm worried I'm always doing it get so it's like patchless and frizzled, or-- are there any Drosophila people here that came up with these crazy names?**

**All right, yeah, so I always got confused which are the morphogens and which are the receptors in these situations. But I'd say that it is something that's observed in number of different contexts, at different stages of development, both in Drosophila and-- they see this in the wing as well as in the body.**

**And so in different stages I think it is signature. But I'm very much not a developmental biologist. All right so the proposal that [INAUDIBLE] suggests as a way to make this thing more robust is to somehow change this term.**

**Now, the goal in all this was to have some degradation rate. And he writes it as F is a function concentration M. In principle, this thing could be a function of the position x, but he doesn't want that. And why was it that he didn't want that? Yeah.**

**AUDIENCE: Because we already know [INAUDIBLE].**

**PROFESSOR: Yes, right. So the whole goal is that we want to start with some situation where we don't know where we are as a function of position x. And then from that get some spatial information. So we really want something that's not a function of x in there. Because then we've already solved the problem that we're trying to address.**

**And so one proposal is indeed just to have something that-- and this is very much a phenomenological approach-- which is to have this thing be self enhanced degradation. So the idea is that here if we have the morphogen profile that looks something like this.**

**There are multiple ways you can have something that looks like this. So if along the way to degradation, if the morphogen actually binds the receptor, but then activates**

12

**the degradation. And this is seen, for example, in Drosophila. This is Hedgehog and Patched. So R is-- in this case, you have the morphogen is diffusing outside the cells. It binds to the receptor, and then the receptor activates imported degradation of the morphogen.**

**So it's not that the morphogen is directly leading to its own degradation, but it's via some network here. And there was another one that they talk about, which is that, when the degradation is mediated by 2. These look like this, and this is in context. And this is again Drosophila, but you could probably guess what this thing does. And so it is a wing development as well.**

**If you write down an actual model of one of these things, and you could play with it and see where you're going to get something that's going to look like an M squared type term. But the nice thing about this phenomenological approach is it kind of gives you a sense of the kinds of effects that you should be looking for that will enhance the robustness of the pattern.**

**Now the key thing in this whole discussion to remember is that if you have a profile here, if you change, it's just somehow translationally invarion in the sense that since there's no information about where you are here, these patterns can kind of slide over. So if you change the boundary condition M0, that's just equivalent to sliding this over some distance and you could figure out where everything has to go.**

**And that's true not just for the exponential profile, but for any of the profiles. And that's just because there's no information about what's going on once you're inside the embryo. Can somebody give the intuitive explanation for why some sort of self enhanced degradation like this might make the pattern more robust?**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [AUDIENCE: Decrease faster [INAUDIBLE]. →](03-audience-decrease-faster-inaudible.md)
