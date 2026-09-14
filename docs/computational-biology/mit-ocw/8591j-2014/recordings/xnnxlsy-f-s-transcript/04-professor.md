---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/xnnxlsy-f-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/xnnxlsy-f-s-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**OK, this is a very good question. So this is the differential equation format of this and that we're assuming that there are no stochastic fluctuations. And indeed, there is a large area of excitement, recently, that is trying to understand cases in which you can have, so-called, noise induced oscillations.**

**So you can have cases that the deterministic equations do not oscillate. But if you do the full stochastic treatment, then that could oscillate. In particular, if you do a master equation type formalism. And actually, I don't know, for this particular equations. Yeah, I don't know for this one.**

**But towards the end of the semester, we will be talking about explicit models in which, predator prey systems, in which the differential equation format doesn't oscillate. But then, if you do the master equation stochastic treatment, then it does oscillate. Yeah, so we will be talking about this in other contexts. But I don't know the answer for this model.**

**All right, so let's go and, maybe, try to analyze this a little bit. And this is useful to do, partly because some of the calculations are going to be very similar to what we're about to do next, which is look at stability analysis of a repressilator kind of system. All right.**

**So this thing here is some function f of m and p. And this guy here is indeed, again, some other function g of m and p. And we're going to be taking derivatives of these functions around the fixed point. And maybe I will also say there's going to be some stable point. We should just calculate what it is.**

**I'm sorry I'm making this go up and down. Don't get dizzy. So first of all, it's always good to know whether there are fixed points in any sort of equations that you ever look at. So let's go ahead and see that.**

**First of all, is m equal to 0, p equal to 0? Is that a fixed point in the system? No. Right? So if m and p are 0, then this is a fixed point. But that one's not because we get expression of the mRNA in the absence of the protein. So the origin is not a fixed point.**

11

**Now to figure out the fixed points, we just set these things equal to 0. So if m dot is equal to 0, we have 0. That's alpha 1 plus p to the n minus m. Again, 0 is this.**

**So what you can see is that, at equilibrium, we have a condition here where m is equal to p. So from this, we get m equilibrium is equal to p equilibrium. So m equilibrium over here has to be equal to p equilibrium, we just said. And that's equal to this guy here. It's alpha 1 plus p equilibrium to the n.**

**All right. And the condition for this equilibrium is then something that looks like this. Now this is maybe not so intuitive. But alpha is this non dimensional version of the strength of expression. And what this is saying is that, broadly, it's not obvious how to solve this explicitly.**

**But as the strength of expression goes up, the equilibrium here-- and I'm saying equilibrium. And that's, maybe, a little bit dangerous. We might even want to just call it-- it's a fixed point in concentration, so it doesn't have to be stable. So if we don't want to bias our thinking, different people argue about whether equilibrium should be a stable or require a stable.**

**We could just call it some p 0 if that makes you less likely to bias our thinking in terms of whether this concentration should be a stable or unstable fixed point. But for example, if we have that, in these units, if alpha is around 10, n might 2. Then, this thing gives us something. It's in the range of a couple or 2, 3.**

**I mean, you can calculate what it should be. 2, 4, maybe even exactly 2. Did that-yeah. All right, so yes. I'm just giving an example. If alpha were 10, then this equilibrium concentration or this fixed point concentration would be 2 if n were equal to 2 to give you, kind of, some sense of the numbers. And this is 2 in units of that binding affinity k, right.**

**Now the question is, well, what does this mean? Why did we do this? Why do we care at all about the properties of that fix point? OK, so this might be some p 0. And this is, again, m 0 is equal to p 0 in these units. So there's some fixed point somewhere in the middle there.**

12

**Now it turns out that the stability of that fixed point is very important in determining whether there are oscillations or not. Now the question of the generality or what can you say that's universally true about when you get oscillations and when you don't, this is, in general, a very hard mathematical problem, particularly in higher numbers of dimensions.**

**But for two dimensions, there's a very nice statement that you can make based on the Poincare-Bendixson criterion. I cannot remember how to spell that. I'm probably mispronouncing it, as well. So Poincare-Bendixson, what they showed is that if, in two dimensions, you can draw some box here such that all of the trajectories are, kind of, coming in.**

**And indeed, in this case, they do come in because the trajectories aren't going to cross 0. If you have some mRNA, then you're going to start making protein. If you have just protein, no mRNA, you're going to start making some mRNA. And we know that trajectories have to come in from out here because if the concentration of mRNA and the concentration of protein are very large then, eventually, the degradation is going to start pulling things in.**

**So if you come out far enough, eventually, you're going to get trajectories coming in. So now we have there is some domain where all the trajectories are going to come in. Now you can imagine that, somehow, the stability of this thing is very important because in two dimensions here when you have a differential equation, trajectories cannot cross each other.**

**So I'm not allowed in any sort of space like this to do something that looks like this because this would require that, at some concentration of m and p, I have different values for m dot and p dot. So it's similar to this argument we made for one dimension. But it's just generalized to two dimensions.**

**So we're not allowed to cross trajectories. Well if you have a differential equation in any dimensions, that's true. But the thing is that this constraint is a very strong constraint in two dimensions. Whereas, in three dimensions, everything kind of goes out the window because in the three dimensions, you have another axis here.**

13

**And then, these lines can do all sorts of crazy things. And that's actually, basically, why you need three dimensions in order to get chaos in differential equations because this thing about the absence of crossing is just such a strong constraint in two dimensions. Other questions about what I'm saying right now? I'm a little bit worried that I'm--**

**All right, so the trajectories are not allowed to cross. And that's really saying something very strong because we know that, here, trajectories are going to come out of the axis. And mRNA, we don't know which direction they're going to come. But let's figure out, if it were to oscillate, would the trajectories be going clockwise or counterclockwise?**

**And actually, there's going to be some sense of the trajectories even in the absence of oscillations. But broadly, is there kind of a counterclockwise or clockwise kind of motion to the trajectories? Counterclockwise, right? And that's because mRNA leads to protein.**

**So things are going to go like this. And the question is is it going to oscillate. And in two dimensions, actually-- Poincare-Bendixson-- what they say is that, if there's just one fixed point here, then the question of whether it oscillates is the same as the question of whether this is stable. So if it's stable, then there's no oscillations.**

**If it's unstable, than there are. We'll just say no oscillations and oscillations. And that's because if it's a stable point and all the trajectories are coming in, then it just looks like this. So it spirals, maybe, into a state of coexistence. Well it spirals to this point of m and p.**

**Whereas, if it's unstable, then those trajectories are, somehow, being pushed out. If it's unstable, then the trajectories are coming out of that fixed point. In which case, then that's actually precisely the situation in which you get a limit cycle oscillations.**

**So if the fixed point were unstable, it looks like this because we have some box. The trajectories are all coming in, somehow, in here. But if we have one fixed point here**

14

**and the trajectories are coming out, that means we have something that looks like this. It kind of comes out.**

**And given that these trajectories can't cross, the question is, well, what can happen in between? And the answer is, basically, you have to get a limit cycle oscillation. There are these strange situations where you can get a path that is an oscillation that's, kind of, stable from one direction and unstable from another.**

**We're not going to worry about that here. But broadly, if this thing is coming out, then you end up, in both directions, converging to a stable limit cycle oscillation. So it's a unstable fixed point, then this is the exact situation, which you get a limit cycle oscillation.**

**OK. So that means that, what we really want to do if we want to ask-- let's try to back up again. We have this pair of differential equations. We want to know will this negative auto regulatory loop oscillate. Now what I'm telling you is that that question for two dimensions is analogous to the question of figuring out whether this fixed point is stable or not. If it's stable, then we don't get oscillations. If it's unstable, then we do. Any questions about this?**

**So let's see what is is. On Tuesday, what we do is we talked about stability analysis for linear systems. We got what I hope is some intuition about that. And of course, what we need to do here is try to understand how to apply linear stability analysis to this non-linear pair of differential equations.**

**And to do that, what we need to do is we need to linearize around that fixed point. So what we have is we have these two functions, f and g. And what we want to know is around that fixed point-- so we can define some m tilde, which is m minus this m 0. And some p tilde, which is p minus p 0.**

**So when m tilde and p tilde are around 0, that's telling us that we're close to that fixed point. And we want to know, if we just go a little away from the fixed point, do we get pushed away or do we come back to where we started? Well we know that m tilde dot, which is actually equal to m dot, as well because m 0 and p 0 are the**

15

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [same. p tilde dot. →](05-same-p-tilde-dot.md)
