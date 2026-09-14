---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/exbo08-78iu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/exbo08-78iu-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Right. So we have a minus Km times what? Times p0, right. So this is because if we start out down here at P0. Now we have Km. So I was just about to violate my rule and just write down an equation without drawing this thing. So it's Km times p0. That's a way you lose probability, but you can also gain probability at a rate that goes as gamma m times P1.**

**So that's how this probability is going to change over time. But we have a different equation for you for p1, for p2, for p3, for p4, all the way, in principle, to p1,683,000, bla bla bla, right? So that's problematic, because if we have to actually in our program code up 100,000,000 equations, or it could be worse. Then we're going have trouble with our computers. So you always have to have some notion of what you should be doing.**

**And this also highlights that it's really important to have some intuitive notion of what's going on in your system before you go and you start programming, because in that case-- well, you're likely to write down something that's wrong. You won't know if you have the right answer, and you might do something that doesn't make any sense. So you have to have some notion of what the system should look like before you even start coding it. My question is, how many of these equations should we simulate?**

**OK. Let's just see where we are. Ready. 3, 2, 1. OK. So I'd say that we have, it's**

13

**basically between C and D. Yeah. I would say some people are maybe more careful than I am. Can one of the Ds maybe defend why they're saying D?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: The mean is 100, and when you say-- I mean, I think that whatever you're thinking is correct, but I think that the words are a little dangerous. And why am I concerned about-- you said-- is the mean 100 for all time?**

**AUDIENCE: [INAUDIBLE] and steady state.**

**PROFESSOR: And steady state. Right. I think that was the-- for long times, the mean number of mRNA will, indeed, be 100. So the mean number of m, in this case, will be Km divided by gamma m, which is going to be equal to 50 divided by that. That gets us 100. Now will it be exactly 100? No. It's going to be 100 plus or minus what? Plus or minus 10. Right. Because this distribution at steady state is what?**

**AUDIENCE: It's Poisson.**

**PROFESSOR: It's Poisson. What's the variance of a Poisson distribution? It's equal to the mean. So for Poisson, the variance is equal to the mean. Variance is the square of the standard deviation, which means that this is going to be plus or minus 10. That's kind of the typical width of the distribution. So what it means is that at equilibrium, we're going to be at 100 and it's going to kind of look like this. So this might be 2 sigma, so this could be 20. But each of these is 10.**

**So if you want to capture this, you might want to go out to a few sigma. So let's say you want to go out to 3 sigma, then you might want to get out to 130 maybe. So then, if you want to be more careful you go out to 140 or 150. But this thing is going to decay exponentially, so you don't need to go up TO 1,000, because the probability's going to be 0 0 0. Certain once you're at 200 you don't have to worry about it.**

**But of course, you have to remember the initial condition we started at 50. So we started at this point, which means we definitely have to include that equation.**

14

**Otherwise we're in trouble. Now how much do we have to go to below 50 Any-AUDIENCE: My guess would be that it would be not much more than the [? few ?] times 5, because if it were already at equilibrium that would be the mean. But it's not, and so the driving force is still going to push it back to [INAUDIBLE]. PROFESSOR: That's right. So it's going to be a bias random walk here, where it's going to be sort of maybe twice as likely at each step to be moving right as to be moving left. That means it could very well go to 49, 48. But it's not really going to go below 40, say. Of course you have to quantify these things if you want to be careful. But certainly I would say going from, I don't know, 35 to 135 would be fine with me. You would get full credit on your problem set. So we'll say-- I'm going to make this up-- from 35 to 135, 134 just so it could be 100 equations. So I'd say I'd be fine with 100 equations. So you would simulate the change in the probabilities of P35 to P134, for example. So although in principle, the master equation specifies how the probabilities for an infinite number of equations are going to change, you only need to simulate a finite number of them depending upon the dynamics of your system. Yes. Thank you for the question, because it's a very important practical thing. AUDIENCE: So in practice, you don't know what the solution is, which is sort of why you would [INAUDIBLE]. Do you explain your range and see if the solution changes? PROFESSOR: So the question is, in this case, it's a little bit cheating because we already kind of knew the answer. We didn't know exactly how the time dependence was going to go. How is it that the mean is going to change over time on average? Exponentially, right? So on average you will start at 50. You exponentially relax to 100. But in many cases, we don't know so much about the system. And I'd say that what, in general, you can do is, you have to always specify a finite number of equations. But then what you can do is, you can put in, like, reflecting boundary conditions or so on the end, so you don't allow probability to escape.**

**But then what you can do is you can run the simulation, and if you have some**

15

**reasonable probability to any of your boundaries, then you know you're in trouble and you have to extend it from there. So you can look to say, oh, is it above 10 to the minus 3 or 4, whatever. And then if it is, then you know you have to go further. Any other questions about how-- you're actually going to be doing simulations of this, so these are relevant questions for you. All right.**

**So that's the master equation. But I'd say the key, key thing to remember is that it tells you how to calculate the deterministic evolution of the probability of these states given some potentially complicated set of interactions.**

**Now, a rather orthogonal view to the master equation is to use the Gillespie algorithm, or in general, to do direct stochastic simulations of individual trajectories. Yeah. Question before we go.**

**AUDIENCE: So if we just set it to 0, the probabilities outside the range we think we need, would we be losing probability?**

**PROFESSOR: So the question is whether we're somehow losing probability. So what I was proposing before is that you always want probabilities to sum to 1. Otherwise it's not our probability and the mathematicians get upset. And the key thing there is that you want to start with-- you have to include all the states that have probability at the beginning.**

**So in that sense, you're given an initial distribution, and you have to include all those states. Otherwise you're definitely going to do something funny. You start out with a normalized probability distribution. And then I guess what I was proposing is that you have a finite number of equations, but you don't let the probability leave or come in from those ends.**

**And if you do that, then you will always have a normalized probability distribution. Of course, at the ends you've kind of violated the actual equations, and that's why you have to make sure that you don't have significant probability at any of your boundaries. Does that answer? Not quite?**

**AUDIENCE: Because I'm wondering if [INAUDIBLE].**

16

---

[← probabilities are 0 above some number?](06-probabilities-are-0-above-some-number.md) · [Up: contents](index.md) · [PROFESSOR →](08-professor.md)
