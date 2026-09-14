---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/exbo08-78iu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/exbo08-78iu-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So I was not suggesting that you set the probabilities equal to 0. I was suggesting that you do what's kind of like what the equations actually here, which is that you don't allow any probability to leave. There's no probably flux on this edge.**

**So for example, out at P134, I would just say, OK, well, here's the probability that you have 134 mRNA. And in principle there are these two arrows, but you can just get rid of them. So now any probability that enters here can only come back. And I've somehow violated my equations. But if P134 is essentially 0, then it doesn't matter.**

**So instead of looking at these probabilities evolve kind of as a whole, we can instead look at individual trajectories, right? So the idea here is that if we start with the situation-- actually, we can take this thing here. So we know that at steady state it's going to be 100. Starts out at 50. And in this case, with the master equation you say, OK, well, you start out with all the probability right here.**

**So you have kind of a delta function at 50. But then what happens is this thing kind of evolves, and over time this thing kind of spreads until you have something that looks like this, where you have a Poisson distribution centered around 100. And this Poisson distribution's going to be very close to a Gaussian, because you have a significant number.**

**So the master equation tells you how this probability distribution evolves. Now this is the number m and this is kind of the frequency that you observe it. So we can also kind of flip things so we instead plot the number m on the y-axis. And we already said the deterministic equations will look like this. And the characteristic time scale for this is what?**

**1 over mm, right? So this thing relaxes to the equilibrium, time scale determined by the degradation time of the mRNA. So these are things that should be really-- you want to be kind of drilled into your head, and I'm trying to drill, so you'll hear them again and again.**

**Now the master equation, indeed, since everything's linear here, the expectation**

17

**value over the probability distributions actually does behave like this. So the mean of the distributions as a function of time look like that. And in some ways, if we were to plot this, we would say, OK, well, first of all it's all here. Then it kind of looks like this. So this is somehow how those probability distributions are kind of expanding over time.**

**Now for an individual trajectories, if we run a bunch of stochastic simulations, we'll get something that on average looks like this, but it might look like this. A different one might look like this, and so on, although they shouldn't converge there because that's not consistent.**

**And if you did a histogram at all those different times of the individual stochastic trajectories, you should recover the probability distribution that you got for the master equation.**

**So this is a powerful way just to make sure that, for example, your simulations are working, that you can check to make sure that everything behaves in a consistent way.**

**Now there's a major question, though, of how is it that you should generate these stochastic trajectories? And the sort of most straightforward thing to do is to just divide up time into a bunch of little delta t's, and just ask whether anything happened. So let me--**

**So what we want to do is we want to imagine we have maybe m chemical species. So now these are different m's and n's. Be careful. m chemical species, they could be anything, could be proteins, they could be small molecules, something. And there are n possible reactions.**

**And indeed, in some cases people want to study the stochastic dynamics of large networks. So you could have 50 chemical species and 300 different reactions. So this could be rather complicated. And these m chemical species have, we'll say, numbers or if you'd like, in some cases it could be concentrations, Xi, so then the whole thing can be described as some vector X.**

18

**And the question is, how should we assimilate this? The so-called, what we often call the naive protocol-- and this is indeed what I did in graduate school because nobody told me that I wasn't supposed to do it-- is that you divide time into little time segments delta t.**

**Small delta t. And you just do this over and over. And for each delta t you ask, did anything happen? If it did, then you update. If not, you keep on going. Now the problem with this approach-- well, what is the problem with this approach?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Yeah. Time is continuous. So one problem is that, well, you don't like discrete time. That's understandable. But I'm going to say, well, you know, the details-- a delta t may be small, so you won't notice. I'm saying, if I said delta t being small, then I'm going to claim that you're not going to notice that I've--**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: But then the simulation is slow, right? So there's a fundamental trade-off here. And in particular, the problem with this protocol is that for it to behave reasonably, delta t has to be very small. And what do I mean by very small, though?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: That's right. For this to work, delta t has to be such that unlikely for anything to happen. But this is already a problem, because that means that we're doing a lot of simulations, and then just nothing's happening. How do we figure out what that probability is?**

**So in particular, we can ask about-- well, given possible reactions, we'll say with rates rs of i. So the probability that the i'th reaction occurs is equal to r i times delta t for small delta t, because each of these reactions will occur kind of at a rate-they're going to be exponential distributions of the times for them to occur. This is a Poisson process because it's random.**

19

**Now what we want to know is the probability that nothing is going to happen because that's how we're going to have set delta t. Well, what we can imagine is, then we say, well, what's the probability that is, say, not reaction 1 and not 2 and dot dot dot. OK. Well, and this is in some time delta t.**

**Well, actually, we know that if the fundamental process just looks like this, then we're going to get exponential distributions for each of those. So we end up with e to the r1, and indeed, once we write an exponential, we don't have to write delta t. This is just some time t. For this to be true requires a delta t is very small. But if we want to just ask, what's the probability that reaction 1 has not happened in some time t, this actually is, indeed, precisely equal to e to the r1t. Yeah, details.**

**And this is e to the minus r2t dot dot dot minus. And we go up to n, r to the nt, because each of those chemical reactions are going to be exponentially distributed in terms of how long you have to wait for them to happen.**

**And what's neat about this is that this means that if you just ask about the probability distribution for all of them combined by saying that none of them have happened, this is actually just equal to the exponent of minus-- now we might pull the t out and we just sum over ri.**

**So this is actually, somehow, a little bit surprising, which is that each of those chemical reactions occur, and they're occurring at different rates. Some of them might be fast, some of them might be slow. The ri's can be different by orders of magnitude. But still, over these hundreds of chemical reactions, if the only thing you want to know is, oh, what's the probability that none of them have happened, that is also going to end up-- that's going to decay exponentially.**

**And this actually tells us something very interesting, which is that if we want to know the distribution of times for the first thing to happen, that's also going to be exponentially distributed. And it's just exponentially distributed with a rate that is given by the sum of these rates. Now that's the basic insight behind this GIllespie algorithm, where instead of dividing things up into a bunch of little times delta t, instead what you do is you ask, how long am I going to have to wait before the first**

20

**thing happens? And you just sample from an exponential with this rate r that is the sum of the rates.**

**Maybe it's even worth saying that, OK, so there's the naive algorithm where you just divide a bunch of delta t's, you just take a little steps, you say, OK, nothing, nothing, nothing, nothing, and then eventually something happens, and then you update, you keep on going.**

**There's the somewhat less naive algorithm, which is exact, so it's not the same concerns, the j hat which is that you could just sample from n different exponentials, each with their own rates, and then just take the minimum of them and say, OK, that's the that happened first, and then update from that. And that's an exact algorithm.**

**But the problem is that you have to sample from possibly many different exponentials. And that's not a disaster, but again, it's computationally slow. So the Gillespie algorithm removes the requirement to from those n exponentials, because instead what you do is you just say, the numbers, or the concentrations, give all of the ri, give you all the rates.**

**And then what you do is you sample from an exponential with rate r, which is the sum over all the ri. That tells you, when is the first reaction going to occur. And then what you do is you ask, well, which reaction did occur? Because you actually don't know that yet. And there, it's just the probabilities of each of them. So the probabilities Pi is just going to be the ri divided by the sum over the ri, so this big R.**

**So it may be that you had 300 possible chemical reactions, but you only have to do two things here. And they're both kind of simple, right? You sample from one exponential, gives you how long you had to wait for something to happen. And then you just sample from another simple probability thing here that just tells you which of the n possible chemical reactions was it that actually occurred. And of course, the chemical reactions that were occurring at a faster rate have a higher probability of being chosen.**

21

**So this actually is an exact procedure in the sense that there's no digitization of time or anything of the sort. So this actually is computationally efficient and is exact, assuming that your description of the chemical reactions was accurate to begin with.**

**So then what we do is we update time. This is in some ways-- when you do computations, when you actually do simulations-- this is maybe the annoying part about the Gillespie algorithm, which is that now your times are not equally spaced, and so then you just have to make sure you remember that, you don't plot something that's incorrect. Because your times are going to hop at different time intervals. But that's doable. You have to update your time and you have to update your abundances. And then what you do is repeat.**

**I think the notes kind of allude to this Gillespie algorithm but are not quite explicit about what you actually do to go through this process. For the simulations that you're going to do in this class, I would say that you don't get the full benefits of the Gillespie in the sense that you're not going to be simulating hundreds of differential equations with hundreds of different things. But it's in those complicated models that you really have to do this kind of Gillespie approach, as compared to even this somewhat better model, which is you sample from the different exponentials.**

**Are there any questions about why this might work, why you might want to do it? Yes.**

**AUDIENCE: What do you mean by sample the exponentials?**

**PROFESSOR: Right. What I mean is that you go to Matlab and you say, random-- I'm sort of serious, but-- sorry, I'm trying to get a new-- All right. So you the exponential. So it's a probability distribution. So this is the probability is a function of time and then t. And it's going to look something like this. This thing is going to be some-- given that, in general, it's going to be the probability t is going to be e to the minus rt. And then do I put r here or do I put 1 over r?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Is it 1 over r? Well, what should be the units of a probability distribution? 1 over**

22

**time, in this case. It's 1 over whatever's on this x-axis, because if you want to get the actual, honest to goodness probability-- so if you want the probability that t is, say, between t1 and t1 plus delta t. If you want an actual probability, then this thing is equal to the probability density at t1, in this case, times delta t. So that means thing has to have a 1 over time, and that gives us r here.**

**So this is probability density, and what I'm saying is that when I say sample from this probability distribution, what it means is that it's like rolling a die, but that it's a biased die because it's continuous thing over the time. But just like when you have a six-sided die and I say, OK, sample from the die, you're playing Monopoly, you throw the die and you get 1, 2, 3, 4, 5, 6. And you do that over and over again.**

**Same thing here. You kind of roll the die and see what happens. And indeed, you're going to get some practice with probability distributions on the homework that you're doing right now because you're asked to demonstrate that you can sample from a uniform distribution, which something that's just equally probable across the unit line, and do a transformation and get an exponential distribution.**

**And it used to be that everybody knew all these tricks because you had to kind of know them in order to do computation. But now, Matlab, or whatever program you use, they know all the tricks, so you just ask it to sample from an exponential with this property and it does it for you. But you still need to know what it's doing.**

**So just to be clear, what is the most likely time that you're going to get out from the exponential? 0. It has a peak here but the mean is over here. Any other questions about how the Gillespie algorithm works?**

**Can somebody tell me how a protein burst arises? So we had this original question about whether there were protein bursts in that model that I wrote down, where we just had m dot is equal to--**

**Now what we said was that the master equation would not-- the protein burst would somehow be there are but you would never see them, or somehow the protein burst would influence how the mean and everything have evolved, but you wouldn't**

23

**actually see any big jumps. But then we said, oh, but if you did a stochastic simulation, you would. So the claim here is that the Gillespie algorithm, what I've just told you here, will lead to protein bursts. When I make that statement, what is it that I actually mean?**

**If we do a Gillespie of this, will the-- OK, let's just hold on. Let me do a quick vote. Will we have cases where delta n is greater than 1? If I go through this process, if I'm using the Gillespie and I'm tracking how mRNA and protein number are changing over time, will I get these things, protein bursts, where delta n is larger than 1 in one of these time cycles?**

**Ready? 3, 2, 1. So most of the group is saying that it's going to be no. But again, it's mixed. So can somebody say why we don't get--**

**AUDIENCE: [INAUDIBLE] It seems like the structure of the simulation is to make sure [INAUDIBLE].**

**PROFESSOR: That's right. Yeah. So the simulation as written-- you could imagine some sort of phenomenological version of this where you allowed, actually, for protein bursts. But as kind of specified is that we ask, what's the time for one thing to happen? But the claim somehow is, OK, well, we can still get protein bursts from this. And how does that happen?**

**AUDIENCE: You can have the rate for something happening increase suddenly, and that would happen if we go from m equals 0 to m equals 1-PROFESSOR: Yeah, for example, if we didn't have an mRNA before and we got an mRNA. What it means that if you look at n as a function of time during one of these protein bursts-before, I was drawing it just hopping up, but really, in the context of the Gillespie, it would be that it would hop, hop. So there would be little time jumps. So this is a protein burst, but it's really before this mRNA is degraded, you get 1, 1, 1, 1.**

**So each of these as is delta n of 1. So this is whatever, 6, 7. And then what can happen is that we get the mRNA degraded. And so then we're going to get a slower thing where it-- looks like that. So the Gillespie, everything is being created and**

24

**destroyed in units of 1. But it could be that the time interval over this burst is just very short, so then it goes up very quickly, but then it's slower to go away.**

**So what I want to do in just the last 15 minutes is talk a bit about the Fokker-Planck approximation. I would say that all these different approaches are useful to varying degrees in terms of actually doing simulations, doing analytic calculations, getting intuition. And the Fokker-Planck approach, I'd say it's more or less useful for different people depending on what you're doing.**

**So the basic idea, as kind of you answered in the pre-class reading, is that in cases where n is large enough that you don't feel like you need to take into account the discrete nature of the molecules, yet at the same time it's not so large that you can totally ignore the fluctuations, then the Fokker-Planck approach is nice because it allows you to get some sense of what's going on without all of the crazy details of, for example, the master equation. And then it also, because of this idea of an effective potential, it allows you to bring all the intuition from that into your study of these gene circuits.**

**Now I'm not going to go through the whole derivation, but if you have questions about that, please come up after class and I'm happy to go through it with you, because it's sort of fun. But the notes do go over it. I think that's what's perhaps useful to just remind ourselves of is how it maybe leads to a Gaussian with some width depending upon the shapes of the production degradation curves.**

**So the basic notion here is that, depending on the f's and g's, the production degradation terms, we get different shaped effective potentials. So in general we have something that looks like-- we have some n dot, there's some fn, and then there's a minus gn.**

**So for example, for something that is just simple expression, in the case of-- let's just imagine now that there is-- if you want we can say it's a protein where it's just some k minus gamma n. Or if you'd like, we could say, oh, this is mRNA number. But something that's just simple production, and then first order degradation.**

25

**The question is, how do we go about understanding this in the context of the Fokker-Planck approximation? And it turns out that you can write it in what is essentially a diffusion equation where you have some probability flux that's moving around. And within that realm, you can write that the probability distribution of the number is going to be something that-- so there's going to be some constant. There's f plus g. And these are both functions of n. And then you have e to the minus [INAUDIBLE]**

**So the idea here is that this behaves as some effective potential. Of course, it's not quite true because f and g also are functions of n, they're are not in here. But this is the dominant term because it's in the exponential. And here phi n is defined as the following. So it's minus this integral over n of the f minus g and f plus g dn that we integrate over n prime.**

**And we're going to kind of go through what some of these different f's and g's might look like to try to get a sense of why this happened. It is worth mentioning that you can do this for any f and g when it's just in one dimension, so you just have n. Once you have it in two dimensions, so once you actually have mRNA and protein, for example, you're not guaranteed to to be able to write it as an effective potential. Although I guess if you're willing to invoke a vector potential, then maybe you can.**

**But in terms of just a simple potential, then you can do it one dimension, but not necessarily in more. And I think that, in general, our intuition is not as useful when you have the equivalent of magnetic fields and so forth here anyway.**

**What I want to do is just try to understand why this thing looks the way it does for this simple regulation case. And then we're going to ask if we change one thing or another, how does it affect the resulting variance.**

**So for unregulated expression, such as here, if we look at the production and degradation as a function of n, fn is just some constant k, whereas gn is a line that goes up as gamma n. Now in this situation, if you do this integral-- and really, what you can imagine is what this integral looks like right around that steady state, because that's kind of what we want to know, if we want to something about, for**

26

**example, the width of a distribution.**

**Well, there's going to b e two terms. In the numerator there's an f minus g. In the denominator there's an f plus g. Now f minus g is actually equal to 0 right at that steady state, and that's why it's a steady state, because production and degradation are equal. Now as you go away from that location, what you're doing is you're integrating the difference between the f and the g.**

**And you can see that around here these things are separating kind of-- well, everything's a line here. And indeed, even if f and g were not linear, close to that steady state they would be linear. What we can see is that as you're integrating, you're integrating across something that is growing linearly. That's what gives you a quadratic. And that's why this effect of potential ends up behaving as if you're in a quadratic trap.**

**Now I encourage you to go ahead and do that integral at some point. I was planning on doing it for you today, but we are running out of time. Once again, I'm happy to do it, just after class. And indeed, what you can see is that because you're integrating across here, you end up getting a quadratic increase in the effective potential. And if you look at what the variance of that thing is, you indeed find that the variance is equal to the mean here.**

**So what I want to ask in terms of trying to get intuition is, what happens if we pull these curves down? So in particular, let's imagine that we have a situation where-I'm going to re-parameterize things, so again, we're kind of keeping the number of the equilibrium constant. But now what I'm going to do is I'm going to have an fn that looks like this, and gn looks like-- now gn is going to be some 1/2 of lambda, and this fn is equal to k minus 1/2 of gamma n.**

**Now the question is, in this situation, what will be the variance over the mean? Well, first of all, the variance over the mean here was equal to what? Although should we do vote? Here are going to be some options.**

**Question is variance over the mean in this situation. I'm worried that this is not going**

27

**to work, but let's just see where are. Ready, 3, 2, 1. All right. So I'd say that at least broadly, people are agreeing that the variance over the mean here is equal to 1.**

**And again, this is the situation that we've analyzed many times, which is that in this situation we get a poisson, where the poisson only has one free parameter, and that parameter specifies both the mean and the variance. So for a poisson, the variance of the mean is indeed equal to 1. So the Fokker-Planck approximation actually accurately recapitulates that.**

**Now the question is, what will the variance over the mean be in the situation that I've just drawn here? So I'm going to give you a minute to try to think about what this means. And there are multiple ways of figuring it out. You can look at, maybe, the integral. You can think about the biological intuition to make at least a guess of of what it should do.**

**The question is, if the production rate and the degradation rate look like this, what does that mean for the variance over the mean? So I'll give you a minute to kind of play with it.**

**Why don't we go ahead and vote, just so I can get a sense of where we are? And also, it's OK if you can't actually figure this out or you're confused. But go ahead and make your best guess anyways, because it's also useful if you can guess kind of the direction it'll go, even if you can't figure out its magnitude.**

**So let's vote. Ready, 3, 2, 1. OK. So it's a mixture now, I'd say, of A, B, C, Ds. Yeah, I think this is, I think, hard and confusing. I maybe won't have-- all right. I'll maybe say something. It may be that talking to each other won't help that much.**

**OK, so in this case, what's relevant is both the f minus g and the f plus g. And it turns out that f minus g actually behaves the same way, because at the fixed point, or at the equilibrium, it starts at 0 and then it actually grows in the same way as you go away from it. The difference is the f plus g, where that's very much not equal to 0. And f plus g at the equilibrium, this f plus g here is around 2k, whereas f plus g over here is around 1k.**

28

**What that means is that in both cases you have a quadratic potential. But here the quadratic potential actually ends up being steeper. So if this were unregulated, then over here we still get a quadratic, but it's with steeper walls. So actually here, this, the variance over the mean, ends up being 1/2.**

**It's useful to go ahead and just play with these equations to see why that happens. And I think that's a nice way to think about this is, in this limit, where we pull this crossing point all the way down to 0, now we have something that looks kind of like this. So very, very low rate of degradation.**

**But then also the production rate essentially goes to 0 when we're at this point. So we could still parameterize as k over gamma if we want, with some-- but we could just think about this as being at 100 of these mRNAs, say. But then we're changing the production degradation rate.**

**And the variance over the mean here-- does anybody have a guess of where that goes? In this case it actually goes to 0. And this is an interesting situation, because really, in the limit where there's no degradation, and it's all at the production side, what it's saying is that you produce, you produce, you produce, until you get to this number, which might be 100, and then you simply stop doing anything. You're not degrading, you're not producing. In that case all the cells will have exactly 100, maybe, mRNA.**

**And what the Fokker-Planck kind of formalism tells you is that just because production and degradation rates are equal, f minus g is equal to 0, doesn't mean that-- that tells you that that's the equilibrium, but it doesn't tell you how much spread there's going to be around the equilibrium. If f and g are each larger, that leads to a larger spread because there's more randomness, whereas here, f and g are both essentially 0 at that point. What that means is that you kind of just pile up right at that precise value.**

**We are out of time, so I think we should quit. But I am available for the next half hour if anybody has any questions. Thanks.**

29

---

[← AUDIENCE: [INAUDIBLE]](07-audience-inaudible.md) · [Up: contents](index.md)
