---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/03bvgr-vyhq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/03bvgr-vyhq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Sorry. So why should we expect that distribution?**

**PROFESSOR: Why should we expect the distribution? So one answer is that because that's what you read on Tuesday. But let's go ahead and-- yes, but let's go ahead and calculate it. That's useful.**

**The way to think about this, in some ways, there's another way to write this perhaps. Which is that imagine you have an mRNA. Now at some rate it's going to be degraded. And maybe we'll keep the degradation rate down, just for-- so there's a degradation rate. But then if you'd like, we could draw it like this. Where this is the synthesis rate for a protein. And out pops a protein.**

**And so the idea is that is here we're in some state where, OK, here we have an mRNA. Here's the state where we don't have an mRNA. Now this is the competition between those two rates that I was telling you about. There is some degradation rate for the mRNA. Or there's a synthesis rate where we go around this loop. If we come around this loop, we come back to the state with an mRNA. There still is an mRNA intact. Just out pops a protein.**

**So then what we want to do, is we want to think about what's the number of proteins that we expect, not just the mean, but the actual distribution. So it's useful in these situations to define some probability rho, which is the probability you actually, if you're here, it's the probability that you produce one protein at least. The question is, which path do you take initially.**

**Well that's just given by the ratios. So there's the rate that we take this circular path divided by the sum of these two other rates. And then what we can do is we can ask, well what is the probability that 0 proteins are produced, probability that we get 0. Well if we take this path initially, will we have 0 proteins?**

**AUDIENCE: No.**

11

**PROFESSOR: No. Right, so this probability is indeed simply equal to the probability that we do this first, which is 1 minus rho. Now what's the probably that we get 1 protein? Well, only 1? That's equal to the probability that we first take this path, and then we take this path. Well we can multiply those probabilities. Because we first take the circular path to make a protein. And then we take the degradation path. Well what's the probability we get 2? Well that's just that we come around here once, twice, and then degrade. Now if you're not seeing a pattern here, then we're in trouble. So this says the probability of n will then just be equal to rho to the n, 1 minus rho. And indeed, it's always useful in order to warm up your probability muscles, to check to make sure that this is a normalized probability distribution. So sum over all possible ends indeed goes to 1. And that's just because the sum over a bunch of rho to the n's is equal to 1 divided by 1 minus rho, which is the term there. And that goes to 1. AUDIENCE: So this is making a pretty strong assumption that they're all independent? PROFESSOR: Yep, yep. Yep. This is assuming that if you've gone around once, you return. But I've come back to the original state. AUDIENCE: But do mRNAs like actually get caught in ribosomes-PROFESSOR: There are a lot of things that can be true. And I would say that in biology and in life, what you do is you first write down the simplest possible model. And then you go and you make measurements. And you ask whether the simplest possible model can adequately explain the data. And if the answer is no, then you're allowed to start thinking about other things. Because everything's is in principle true. In that mRNA, maybe it's this or that. The question is whether it's significant. And at least from the data from Sunney's group would say that in that condition, in those cells, that those things are not significant, in the sense that you still get a geometric distribution.**

12

**Of course it could also be that those other things actually are true and are significant. But then you end up with some new parameters that describe how things look as a result of all the complexity. That's also OK in the sense that I'd say that you can get a quantitative description of the process by describing it as a geometric with just a single free parameter. And they found that the mean was four, or four or five. The mean number of proteins produced from each mRNA. But they got this geometric distribution in that paper. Yes?**

**And I'll just mention here that the mean of this is rho divided by 1 minus rho. So what you see is that as rho goes to 1, then this thing is going to diverge. And that makes sense. because as rho goes to 1, it's saying that you essentially always synthesize another protein rather than degrading.**

**And before I move on, I just want to say one more thing, which is that there are many different definitions of the geometric distribution, depending upon whether the probability of rho is the probability of terminating, or the probability of going around, and also depending on whether you're asking what is the-- here we're talking about the probability distribution for the number of proteins produced. Whereas we could have talked about the probability distribution for the number of times we go around this loop before, no, no sorry. That is for the number of proteins produced.**

**So the other way you could have defined this is the number of times where it's-- the number of cycles that you had to go before you went here, in the sense that if you first go here, you can either call that a 0 or a 1. Do you see what I'm saying? And reasonable people can disagree. But you end up getting distributions that are just a little bit different. So watch out. If you just memorize something, you might have memorized the equation for a different definition of this distribution. Does everyone understand what I tried to say there? Maybe? Yeah?**

**AUDIENCE: When there's no degradation is it still a Poisson?**

**PROFESSOR: Ah, if there's no degradation then would this be a Poisson? I mean, this would be infinity, right?**

13

**AUDIENCE: Right, [INAUDIBLE] protein, this is done independently, like there's an mRNA. [INAUDIBLE] proteins independently. PROFESSOR: OK. So I want to be clear. This is, p of n is, this is the probability distribution for number of proteins n, produced from a single mRNA. Now if there's no degradation of the mRNA, then this thing is not even, I think, defined in that the number of proteins produced from that mRNA just really goes to infinity. If you wanted to ask about the probability distribution for the number of proteins produced in some unit, some period of time that would indeed be a Poisson distribution, assuming that there's no degradation. Do you understand what I'm trying to say? AUDIENCE: So Sp is like 0? PROFESSOR: If Sp, I'm sorry. If Sp were 0? AUDIENCE: Yeah. [INAUDIBLE]. PROFESSOR: OK. And you're saying that what would be Poisson distributed? AUDIENCE: The number of proteins. PROFESSOR: Yeah, I think that actually-- no I think that-- I think that you're probably right. That as Sp goes to 0-- I'm a little bit worried that-AUDIENCE: No, no, no. Zero-th order, sorry. PROFESSOR: Oh. AUDIENCE: Not 0. [INAUDIBLE]. PROFESSOR: OK. Right, so the mRNA distribution we're about to find is indeed going to be a Poisson at steady state. And so if there's some process by which the protein distribution is really just mirroring the mRNA distribution, then it will also be Poisson. Although I think you have to be careful about how you actually implement that. Because even in the absence of this geometric bursting, different things, I think, can**

14

**happen.**

**Because for example, if there were exactly 10 proteins produced from each mRNA, then that probability distribution is a shift. But then it's no longer actually going to be Poisson, because the mean and variance are going to scale differently if you do that.**

**Let's maybe do the Poisson distribution for the mRNA first. And then we can try to touch back on this. So this is a plot of kind of geometric distribution with a mean of 3-4-ish. Is everybody happy with where we are now? OK.**

**Now from this, what we've said so far is it obvious what the distribution of proteins will be in a cell? We can say obvious, yes. Or not obvious, no. Ready, just verbal, yes? Ready or no? All right. Ready? Three, two, one.**

**AUDIENCE: No.**

**PROFESSOR: No. Right. So we've said that the distribution of size of protein bursts from single mRNA is geometric. But that doesn't mean that that's going to be the distribution of proteins in the cell. And indeed after, we're going to find that the distribution of mRNA is going to be Poisson. But even then it's not obvious what the distribution of proteins is.**

**All right. So what we want to do now is we want to introduce kind of a simple version of what's known as the Master Equation. Now you guys are going to do more reading on this for the lecture on Tuesday. Where we're going to talk about the Master Equation, as well as the Fokker-Planck approximation. Maybe the Gillespie algorithm, and so forth.**

**But I want to start by thinking about the this notion in the simplest possible context. So what we're going to do is we're going to think about the world. So we want to know the steady state, or the equilibrium distribution of mRNA numbers in the cell, given this process. So that's great. We can-- so mRNA distribution, question mark.**

**Now in this case we don't care about Sp, delta p, because the only things that are**

15

**relevant are going to be these. Now what we're going to do is we're going to think about the world in which we just defined states corresponding to the different numbers of these mRNAs.**

**So there's a state where there's 0. We can't go to the left, less than 0, but we can go to the state where there's 1, or the state where there's 2, and so forth.**

**Now the description here is supposed to be the analog of this over there. So this is trying to understand the situation where the deterministic equations would be described by m dot is equal to this some synthesis rate, minus a degradation rate that's proportional to the number, so minus delta m times m.**

**So what you can see is that the deterministic equations are very simple. We already calculated the equilibrium. So when this thing is equal to 0, then we get that m equilibrium is just going to equal to the synthesis rate divided by the degradation rate.**

**If we're away from the equilibrium in this deterministic approximation, how long is it going to take us to kind of approach our equilibrium? Verbal answer, ready? Three, two, one.**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [[STUDENTS RESPOND] →](03-students-respond.md)
