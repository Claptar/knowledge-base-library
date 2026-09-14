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

**Do you also need to multiply like natural probabilities--**

**PROFESSOR: Ah, Yes, yes, indeed. So that sorry, times mn times m of n plus 1. So it's the kind of probably flux so we have to equalize.**

**So this is nice because this gives us a ratio of things. In particular, this tells us that the probability of being in the n plus 1 divided by the probability of being n, and this is at equilibrium. Is going to be fn divided by gn plus 1. Which is this synthesis rate. And then down here is going to be this degradation rate times, in this case, n plus 1.**

**So this is useful. Because for example, if we start at m, we could say that m1 over m0-- well maybe we'll even put the m0 over on the right. So then m1, what is that equal to? That's going to be synthesis rate divided degradation rate, times m0.**

**But then we also know that m2, well that's going to be again, synthesis rate divided by degradation rate. And we're going to get a squared. But then now we have to divide by 1/2 times m0.**

**Continuing on, m3 we get Sm over delta m cubed, divided by 1 over 3 times 2 times m0. So in general, we get the probability of being in the nth state, is going to be this thing. We'll call it lambda for now. Lambda to the n, divided by n factorial, times m0.**

**Now what's the-- and I'll-- remember lambda here we've defined it to be the ratio Sm over delta m. Now if we sum over all these probabilities, what should we get?**

**AUDIENCE: 1.**

19

**PROFESSOR: 1. Right, if we sum over this thing, what does that equal to? It's what? AUDIENCE: Eta lambda. PROFESSOR: Eta lambda, right? So just remember in this world-- the sum over lambda to the n, n factorial, from n equal to 0 to infinity, this is indeed the definition of e to the lambda. So what that means is that the normalization condition is that m0 has to be equal to e to the minus lambda, which is indeed a Poisson distribution. I'll raise it up a little bit. So this is saying, OK, to back up. If we just have constant rate of creation of something, constant rate of degradation of that thing, on a per item basis, per unit basis, then you end up getting a Poisson distribution, at equilibrium for the number of that thing, in this case, the number of mRNA in the cell.**

**Questions about why that is? What happened? How we calculate it? AUDIENCE: Could you explain why [INAUDIBLE]? PROFESSOR: Sure. So this is basically f of n. And this is basically this g of n. But remember here n is the number of proteins or the number of mRNA. So then that's in the context of the master equation, then m and n are there. You get n by the current number of m. Does that make sense? Yes? AUDIENCE: I'm confused how you changed m0 to the e to the minus lambda. PROFESSOR: OK. Well let's just do it. So mn, this is the probability that we observe n mRNA. And we know that the sum over mn, so all these probabilities from n equal to 0 to infinity, has to be equal to 1. Something has to happen. Well let's do this sum. This is equal to the sum of lambda to the n, over n factorial m0. But m0, is this a function of n? No. m0 is just, this is just the probability at equilibrium that you have 0 mRNA. So we can just pull this thing out. This is just some number, some probability.**

**Now the statement is that while this thing, this is the definition of e to the lambda. So**

20

**in general, so e to the x we often write is equal to 1, plus x, plus x squared over 2, plus dot, dot, dot. So this thing is indeed just equal e to the lambda. So what we know is that this is still 1. So m0 times e to the lambda, is equal to 1, so m0 is to the minus lambda.**

**Any other questions about how we got here? What's going on? Yes? AUDIENCE: The plot of the solution to the adjoining equation, that would be like the mean value, that would be the behavior of the mean values?**

- **PROFESSOR: That Is the expected behavior of the mean value over time. In this case, fn and gn are both linear functions of the number of the mRNA. Which means that in the context of the master equation, if you ask about the expectation of mn, this quantity is indeed equal to-- it has the same behavior as, over time, as the deterministic equations.**

**So if f and g are nonlinear, then actually you get a deviation. But in this case, it is indeed the same. What it means that if you compare the stochastic and the deterministic trajectories, what you would see is that this thing is going to be a little bit jagged, or whatnot. And then even at equilibrium it's going to come up and down a little bit. I'm trying to add a little bit of jaggedness because it's discrete.**

**But the deterministic equation here is what you would get if you average together an infinite number of these stochastic trajectories. Because another one might have come down here. Does that answer?**

**AUDIENCE: Is m playing a double role? Like in that deterministic equation, m is the concentration of mRNA?**

- **PROFESSOR: I think that I'm-- yeah I think that I should-- my nomenclature I think was not very good. I've used two different things. And now that I'm doing this, I think that I should have-- I should have just called it p of n, or maybe I should've used n here. I think I was trying to be consistent with some of the previous, but I think it was a mistake. Yes?**

21

- **AUDIENCE: Are you plotting stochastic? PROFESSOR: I'm plotting-- OK, so no, I'm not. So this is if you run an actual stochastic trajectory. Then at any moment in time, you just have one-- there's some number of mRNA. Whereas the sum over the mn's, this is talking about the probability distribution of the entire thing. So really if you started here, the master equation would give you some distribution for the n's, some distribution for m's. And so if you looked at these over time, than the mean of these distributions is indeed equal to the deterministic behavior. Yes?**

- **AUDIENCE: Is it possible to recover, like how would we recover the differential equation from the master equation? Is that possible? Maybe that would help.**

- **PROFESSOR: Yeah. I think that in the end, there's going to be a one-to-one relationship from, I guess, this differential equation to the master equation. I'm trying to think of any weird case or something funny's going to happen. Is something funny going to happen?**

- **AUDIENCE: No. But like the easy way is just to write them all in terms of the distribution. And you can just differentiate the whole sum. And in that sum, we express the [INAUDIBLE] with your last equation. [INAUDIBLE].**

- **PROFESSOR: Right. But I think this is the much more mathematical way. I mean because I think that actually, I mean, from the differential equation, you actually from the terms here, you can actually construct the master equation. And I think by the same way, you can go from the master equation, and I think that there's going to be a unique differential equation that would have gotten you to that master equation. So I think just from the terms you can do it.**

**You could also do like moment generating functions to get to how things change. But I mean I think that it's really from this, for example, I think it tells you that that was the differential equation. Does that--**

**I mean it's sort of-- the way that we typically do things these things, is that we have**

22

**a differential equation, and then we construct the master equation. So then we already knew what the differential equation was. But I think just from the terms in your master equation, you can say, all right. This was the differential equation that it started with.**

**Any other questions about what happened here? So we have, I think, a fair number, a fair knowledge of what's going on here now. We know that the equilibrium distribution of mRNA in the cell is going to be Poisson. We also know that the distribution of the number of mRNA produced per sell cycle is also Poisson. But it's a different Poisson from the first one.**

**We know that the number of proteins produced per mRNA is going to be geometrically distributed. The one thing that we have not yet done is to ask about the distribution of protein in the cell. So let's say something about that.**

**I'm not going to do the whole derivation. Because it's harder. But I encourage you to-- even the continuous version of the derivation is definitely harder than this. But then the discrete derivation is even worse.**

**So what we're going to talk about, and the way we'll typically maybe think about this from the standpoint of this class is the continuous approximation to-- oh, that might have ended up being useful. Well it's OK. Is the continuous approximation to the real answer.**

**And in particular, just the way that the exponential is the continuous approximation of the geometric distribution, in the same way you can think about the equilibrium distribution of protein in the cell. In this model is going to be gamma distributed. But gamma is a continuous distribution. But it's a continuous analog of the negative binomial.**

**So let me just make sure I'm-- and Sunney Xie actually has a nice PRL paper where he derives the gamma distribution. But even earlier actually Paulson had derived this negative binomial distribution, the discrete version of the solution.**

**So this is the number of protein per cell. We already know the mean. So this is**

23

**approximately distributed as a gamma. A gamma is a distribution that requires two parameters to describe. So a Poisson can be described by single parameter. Gamma is typically described by two.**

**And b is going to be the burst size, whereas a is the mean number of bursts per cell cycle, which is the same as the mean number of mRNA produced, so mean number of bursts.**

**So the gamma of this a, b. All right. So the gamma of a is the gamma function. It's equal to-- now is it a minus 1 factorial? I always get the-- is it a minus 1 or a plus 1 factorial. Anybody remember this? Yeah, a minus 1.**

**I mean it's like a lot of things. You look at this equation. It doesn't really mean a whole lot. But I think that a reasonable way to think about this is the gamma is approximately what you get when you add together a different exponentials with length scale, given by b.**

**When you add probability distributions, you have to do a convolution. So in some ways, the way to think about it, and this kind of makes sense. Because what is happening is that it takes something of order cell division time for these proteins to go away. Because they're stable.**

**Now each-- and so then what you want to know is how many proteins are kind of produced over the course of a cell cycle. Well that actually you can get at by asking how many bursts are there going to be. And then how big are the bursts?**

**So indeed, the mean here is equal to a times b. And the variance is equal to a times b squared. So for example, if you have a single exponential distribution, with burst size b, then this is what you get. So this is the probability that you get n proteins. And this is this function of n. So for a single burst, this is exponentially distributed. So this is the continuous version.**

**Now if we add together multiple of these bursts, this is really saying that we sample from this distribution, say twice. And then we add the resulting value. So this is a convolution. You guys will have an opportunity to practice this on your problem sets.**

24

**But what happens is that you end up getting something that looks like-- it's going to go. So it increases linearly. If you added three of them together this increase is quadratic. And it kind of goes like that. So this thing becomes kind of-- it goes from a distribution where it's peaked at 0, to something that's peaked at a nonzero value.**

**Now you can ask, for example, what happens as for a large a, if you have many bursts, what does this thing look like? Oh, I wish I hadn't erased my probability distributions. So what are the gamma converged to for large a? A normal distribution. Right? So that's the central limit theorem.**

**If you take any well-behaved probability distribution, you add it. You sample from it many times. Then you end up getting a Gaussian. If you don't remember that very well, then this is something to read about over the weekend. Just like the Poisson is also going to go to-- for large lambda, the Poisson also looks like a Gaussian.**

**Can somebody give an explanation, an intuitive explanation for why that should be? Why it-- yes?**

**AUDIENCE: Because in a Poisson distribution, you can't have anything negative.**

**PROFESSOR: OK. So a Poisson distribution can't have anything-- but now I feel like you're arguing against me. Because a Gaussian has negative values, right?**

**AUDIENCE: Right. So when the mean is really small, only have [INAUDIBLE].**

**PROFESSOR: OK. Yeah. All right. So what you're saying is that Poisson for small lambda it can't go negative. OK. No I think that that's true. Yeah, and so somehow the probability distribution is somehow piling up, as you say. What are some other ways of thinking about this?**

**AUDIENCE: [INAUDIBLE]. Because if you have a low lambda that means it's a Poisson. And then I'm just imagining stretching out. [INAUDIBLE].**

**PROFESSOR: OK. So I think that's fair. Another way we can think about this, is let's say that we have some process that's occurring randomly over some period of time. And this**

25

**could be say, mRNA production. And here this is just the number that we observe here, this is going to be a Poisson, with some mean lambda.**

**Now let's just say that I take another one, same process, same period of time. How is this guy going to be distributed? So this also Poisson of lambda. Now let's say I take this probability distribution, and I take this probability distribution. And I convolve them. I'm going to do the calculation of my head. I did it.**

**So for those of you who haven't done convolutions-- whatever. Yes, what's the new distribution going to be? Poisson 2 lambda. And why does that have to be?**

**AUDIENCE: That line was sort of-- you put it by n.**

**PROFESSOR: Yeah. That's right. This line, I just kind of like I just made it up. I could have just said, oh. Well it's the same process occurring over here. So we have to have the mean. It's still is going to be a Poisson process. And the mean has to be the-- well we just had twice the length. And indeed, for independent probability distributions, means always add. So this all consistent will all the things we know. So this has to be a Poisson of 2 lambda. If I add another segment on here, it has to Poisson of 3 lambda.**

**But what you see is that we see that Poisson of n lambda, which is the sum over many Poissons. Poissons are well-behaved probability distributions. You add them together, you're going to have to get a Gaussian. So you can see that the Poisson has to become Gaussian for large lambda. And indeed it does.**

**So there's a comment about this in the--**

**AUDIENCE: It's a little bit more complicated than this because obviously you always just divide from lambda [INAUDIBLE]. Like you would have to say that Poisson lambda is just like a combination of S--**

**PROFESSOR: OK. You're saying that if I do this calculation backwards, I'm going to get into trouble. Because if I try to break them--**

**AUDIENCE: So if you require lambda to be-- you have to have like a significant probability of**

26

---

[← [STUDENTS RESPOND]](03-students-respond.md) · [Up: contents](index.md) · [getting at least one candidate, right? →](05-getting-at-least-one-candidate-right.md)
