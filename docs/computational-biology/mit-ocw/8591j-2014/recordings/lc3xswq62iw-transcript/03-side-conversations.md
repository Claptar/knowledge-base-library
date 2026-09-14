---
title: '[SIDE CONVERSATIONS]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/lc3xswq62iw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [SIDE CONVERSATIONS]

**Source:** `recordings/lc3xswq62iw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: It sounds like the discussion is maybe gone to completion. Let's go ahead and vote again. The question is, does the dominant eigenvalue of this system go to 0 at this point here? The trans critical bifurcation. Ready? Three, two, one. Alright. It doesn't seem like it's had much of an effect. I see that one person has been convinced of something. I don't know if he's actually convinced, of if he was just surrounded and bullied.**

**All right, so what are some different ways of thinking about this? Yes?**

**AUDIENCE: Well, one of my neighbors decided to actually just lineralize that equation at that point.**

**PROFESSOR: All right. AUDIENCE: If you were completely into you intuition, this would be a way to check.**

**PROFESSOR: Right OK. And now in general, in life, I'm a big believer when you're confronted with some question, you should first think about it, what you should guess based on whatever intuition might be available to you. And then after you have made a guess based on intuition, then you go and you do the calculation. Which in this case, linearizing around. And where do linearize around? Around the fixed point.**

12

**I would say that you really want to linearize maybe not around-- You get the same answer if you lineralize around 0, but you really want to, I think conceptually, you want to linearize around this stable fixed point. Right? Because, in some ways, it's the stable fixed point that the system is sitting in, and you want to know how is it that you're-- How is it is you're going to react when you get perturbed away from that fixed point? And you do get the same answer.**

**The thing is that it's true that the eigenvalue describing the dynamics around this unstable fixed point also goes to zero. But that's because, I think the rules of mathematics somehow say that the fixed points are going to have to do something similar. So I think you do also find the eigenvalue here as it goes to 0, but conceptually that's not the eigenvalue that you actually want to know about. Do you see why I'm saying that?**

**Again, the eigenvalue here is going to 0. We can try to explore this a little bit, but I just want to kind of tie this together and say-- These local bifurcations that you have maybe heard about, which is that this fold bifurcation, the transcritical bifurcation, and also the Hopf bifurcation.**

**So the Hopf is one that looks where you have a stable fixed point that goes-- And in terms of an unstable line, you end up getting oscillations. So that's where you have something that that's going to look like-- but now that I'm drawing this, I'm a little bit- Is there a difference between a Hopf and a pitchfork bifurcation?**

**AUDIENCE: It's whether you have oscillations or not. You can't really show that.**

**PROFESSOR: OK. So as drawn, it's either or both, or?**

**AUDIENCE: It's both.**

**PROFESSOR: OK well. I'll say that this thing also the eigenvalue goes to 0 here. Because I guess, in this-- You don't have to have oscillations in order-- And it depends on the higher dynamic systems. But again, this is another 0 eigenvalue bifurcation.**

**And so the statement is that in principle, you can use this fact that the eigenvalue**

13

**goes to 0, this thing called critical slowing down, to measure some changes in the dynamics of the system before, in this case, you get collapse, or before, in this case, you get extinction. The issue maybe is that in this transition, there really is something big that happened at the bifurcation.**

**So you really want to have an early warning signal because there's a dramatic change, and it may be difficult to reverse. Whereas here, the population size is smoothly going to 0. And once you get down to your last two California condors, you know that you're in trouble. You don't need any sort of fancy early warning indicator based on fluctuations or return time, and so forth. Instead, just the number is maybe your best measure for the health of the population.**

**So I think that yeah, maybe I won't do the linearization, but I encourage you to do it. Because, that's what's going to be relevant. In particular, what you want to know is if there's some-- If you linearize around there some, just be clear, there's some n equilibrium. OK there's some equilibrium, and then you want to ask, well OK now you want to say if your n is equal to some n equilibrium, plus some epsilon. Then, if you plug it into the N dot function, you should get an equation that is something where this epsilon dot is going to be equal to something. What should it be equal to? Something times epsilon. And what something?**

**AUDIENCE: What we've been calling lambda?**

**PROFESSOR: What we've been calling labmda. So this is saying that if you go a little bit away from the equilibrium, so small epsilon here, that epsilon-- The solution to this is an exponential, it's going to get exponential decay, assuming that lambda is what? Negative. And that's the definition of-- is When we say this is a stable fixed point, this is unstable, that's equivalent to saying that the lambda here is negative and the lambda here is positive.**

**AUDIENCE: That's a very easy argument. They exchange stability. So you know that lambda has to be completely 0.**

**PROFESSOR: Yes, this is the point. So we know that lambda here is positive lambda-- I'm sorry,**

14

**lambda here is negative, lambda here is positive. These fixed points at this point, they're going to exchange stability so that means they had to be equal. And where they exchange is when it crosses. So they both-- Well, I guess independently this went-- We should be able to draw this, although I'm a little bit worried that once I try to draw something I'm going to get confused. But this is a useful exercise.**

**In particular, if we plot as a function of delta. So here, we have the lambdas, and we have this delta. and a delta equal to r what's going to happen is that we're going to get the one guy's going to go like this. Something like that. Given, that the fixed points went from stable to unstable, unstable to stable, so they had to cross 0. So if they both cross 0 at that point, they're going to be equal n zero. You guys agree?**

**AUDIENCE: Do we know that the eigenvalues are going to change linearly with the death rate?**

- **PROFESSOR: No. So in general, they don't. I'm trying to think if close to the bifurcation, whether I can say. The mathematicians I'm sure can say something. I'm not going to.**

- **AUDIENCE: Does this also mean that whenever we're on a steady state, approaching bifurcation, we'll always see the critical slowing down? If it's a stable fixed point at a critical value.**

- **PROFESSOR: I think that the statement is that in principle, critical slowing down occurs. But that does not mean that you'll necessarily be able to see it. Because it could be, there's just too much noise, or this, or that.**

- **AUDIENCE: So something that I was thinking about related to that is-- So in this case, it seems like everything about the system, the fluctuations, or anything, should be getting very small, as you approach that.**

- **PROFESSOR: In principle, the fluctuations are supposed to grow. Although this is assuming that the strength of the noise is constant. And in this case, the strength of the noise may not be constant, because if it's demographic noise, and the size of your population is going down. This is actually subtle then, I think.**

**And when we typically talk about these dynamics, we're assuming that there's an**

15

**added noise source that is independent of the variable. But if it's demographic fluctuations you're talking about, that that won't be true.**

**I think that it's also useful to draw, to get some intuition around this, based on this idea of an effective potential. So these are one-dimensional systems, which means you can always write down an effective potential. And in this case, what it's going to look like is-- This is some u effective as a function of the population size. And up here, we have some stable state here that corresponds to something that looks like this. So it starts out maybe at k. What happens is, as the death rate increases, this thing kind of turns-- Or, maybe I didn't quite make it.**

**So what you see is that as the death rate here-- So, as we go down the death rate is going up. So that what happens is the effective potential, describing the dynamics of the population near the equilibrium is broadening out. So you can think about the dynamics as being equivalent to an overdamped particle in effective potential.**

**So for example, for those of you that have studied single molecule biophysics kinds of things, this could be thought of as a [? poly-centered ?] bead that's trapped in a the laser trap. And as you turn down the power of your laser, then the spring constant describing the dynamics of that B in the trap, it gets weaker and weaker. So the potential broadens, and that means that for fixed injection noise-- fixed temperature-- you get these effects, where the fluctuations will increase in magnitude, and you get an increase in this autocorrelation time. Because for example, the bead in the trap, the autocorrelation time is indeed just equal to the relaxation time of the bead in the trap.**

**And the bifurcation occurs right at this point here, where you see that this local potential is, or the local minimum, is disappearing. That's when this stable fixed point is gone. And then you just kind of fall off here. And that's what leads to this collapse, which I have covered up. That leads to the bifurcation.**

**And you should, for example, be able to draw an effective potential here as well. But I'll let you play with it.**

16

**But you can see the location of this unstable fixed point shifting as well. I'm not sure how good my drawing is. Because in principal, this unstable fixed point should have to come together. I'm not sure if that's very clear in my drawing.**

**Just to summarize this discussion, I think there are a few ways that you can think of these early warning indicators. And there's a diagram that I like to make, that I think makes things more clear, for me, at least. Which is that if you look at this population as a function of time, it goes. And if there's an environment quality as a function of time. If the environment has a perturbation, then the population will shrink, and then you'll get recovery. And this thing here tells you about the time for recovery. And this basic phenomenon critical slowing down tells you that as the tipping point approaches, as you approach the bifurcation, that time to recover from this perturbation is going to grow.**

**Of course, the other thing that you can say is that even in the absence of a defied perturbation, even if the environment is constant over time, there could just a natural noise in the system that will fluctuate, just like temperature, for the bead in the trap. And principle, then you can measure the size of the fluctuations, the variance, as well as the autocorrelation time tau, which is, for civil systems, equal to t. And this also grows as you approach the bifurcation**

**AUDIENCE: Is it [? clear ?] that-- Because the perturbation [INAUDIBLE] that you're talking about is I think n [INAUDIBLE] perturbed n into epsilon, and then it relaxes the steady state. Is it [INAUDIBLE] to perturb the environment?**

**PROFESSOR: Yeah, right. So that's a good question. What I've been talking about is a situation where you really literally pull it away, and then you let go. And that's equivalent for in the bead in the trap, that you pull the bead away, and then you let go, and you watch it come back.**

**The situation in the case of the environment is that, if it's a kind of a sudden shift-- It could be anything, it could be a brief change in-- Well it could just be delta. So it could be that over some period of time, the death rate increases, or some period of time, the growth rate decreases. Or it could be that for-- The perturbations don't**

17

**have to be bad, they can also be good, and you actually get the same. The principal for small perturbations to go, it's the same thing anyway.**

**So these are early warning indicators of an impending transition that are based on temporal indicators. And one of the things that we've been excited about in my group is actually just trying to measure these things in a well controlled laboratory population. Since in our case, we're using yeast that are engaging in what you might call a group hunting behavior, where they secrete an enzyme that breaks down sugar, and that kind of leads to this cooperative growth. And at least in that case, we can experimentally measure an increase in all of these things as we approach this bifurcation.**

**The other thing you might think about is what happens for spatially extended populations? We'll talk more about spatial populations on Thursday, but just while we're here, it's useful to think about it. So instead of thinking about just n as a function of time, now you want to think about density of population. So one thing that people talked about is that-- Sorry, this is not a function of time, it's now a function of position x. Density is a function of position. Now, environment is a function of position. If you have a uniform environment over position or space, then in principle you can look at density fluctuations. And this is something that people have talked about.**

**One of things that we have argued is that there should be a spatial analog to this recovery time. So that corresponds to a situation where you have environment as a function of position. Like for example, we have a sharp boundary, or just a region of poor quality. And in that case, you can look at the density as a function of position, and you get some linked scale here.**

**So the statement here is that, just because you're in a region of high quality doesn't mean that you're at your equilibrium density, because if you're close to a poor region, so if you're close to hunting grounds, then you'll get local depletion of the population. You have to get some distance away from a bad region before you get your equilibrium. That distance or recovery length tells you about the quality of the**

18

**environment. And it's the quality of the environment at this region, the good region. Where you are.**

**At least in the laboratory, this is something that's actually much easier to measure than other things. Because, this is a deterministic phenomenon. You don't have to measure fluctuations over time with a high quality time series. You don't have to wait for a perturbation in time, like a drought, and look at recovery. Instead, you just take advantage of natural variations in quality of the environment over space, position, and then you measure profiles.**

**We have a collaboration with a professor at the University of Pisa who does field ecology experiments with these algal mats on intertidal communities, on islands in the Mediterranean. And we have a [? pronates ?] that we can measure this in those island communities as well.**

**Are there any questions about this stuff before we switch gears? Yes?**

**AUDIENCE: In that example, is it-- How much control can you have over actually [? saying ?] the quality to the environment?**

**PROFESSOR: So in that manipulation, what they did was they basically go in and they-- So there these, they're like miniature forest somehow. So they're little-- They have alternative stable states. What they actually do, they go and they like chip away at the rock to remove the things. And they do it over some range. So they experimentally basically make it a challenging environment. And apparently, they have permission to do this. So don't try that at home without asking the proper authorities. Any other questions about this?**

**So I think that the nice thing about studying all these dynamics just for a single population, is that it really clarifies the essential ingredients, in order to get things like sudden transitions. Of course, in natural populations, we have many, many species and tracking in lots of complicated ways. But we would like to understand those things, but I think since it's so complicated, you kind of like, oh anything can happen, and you get a little bit discouraged from thinking deeply about it. Because,**

19

**you just think it's going to be too complicated to try to understand. I very much like the idea of trying to really hone your intuition on the simplest possible situation like this, and then bringing that intuition to more complicated or complex situations. Yeah?**

**AUDIENCE: Can you partially [? adjust ?] But what I want to ask you is whether any of this can be applied to human society?**

**PROFESSOR: Oh, yeah. So whether this could be applied to human society. It's a good question. People certainly try to. I think you'll always have to decide what we mean by apply. I would say that this basic idea that there could be these feedback loops that can lead to sudden transitions in complex systems. I think this is a very robust phenomenon, in the sense that I think if you have strong enough interactions, then I think you kind of expect it to be true.**

**Another question is whether you could quantitatively predict when that's going to happen. There was a recent article written in science or nature about potential tipping points in human society on a global scale. Things in terms of productivity of crops. And so they have a question mark about, they say 2050, question mark, collapse maybe. I say it's very important to be thinking about these things in. But the question is what to do, whether given the uncertainties and your knowledge of where these tipping points might occur, it's always hard to know whether you could make a strong argument saying, oh we have to stop fishing here because it's going to collapse.**

**There's always uncertainty in your decision making. But certainly in the context of climate regime shifts, people are worried about these sorts of feedback loops and the North Atlantic Oscillation and so forth. And I'm not at all an expert for that, so I don't know whether we should be worried. But it's at least good to remember that systems can respond in dramatic ways to small changes. And then, you have to decide what to do with that knowledge, and I think that's more of a judgement call.**

---

[← chemical warfare bacteria.](02-chemical-warfare-bacteria.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
