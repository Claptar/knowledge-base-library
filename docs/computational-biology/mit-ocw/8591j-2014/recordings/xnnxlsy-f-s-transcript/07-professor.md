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

**So in the paper they talk about leakage in the negative--**

**OK, right. So in the paper, they talk about various things, including things such as leakage. It terms out that leakage in an expression only inhibits oscillations though. So in some sense, if you're trying to get oscillations, leakage is a problem, actually. And that's why they use this especially tight-- well we're going to talk about that in a few minutes.**

**They use an especially tight version of these promoters to have low rates of leakage in a synthesis. But what might you need in order to get oscillations in negative autoregulation? Did you have-- have delay. Yes indeed. And that's something that they mentioned in the Elowitz paper is if you add explicit delay.**

**So for example, if instead of having the repression depend on--OK, I already erased everything. But instead of having the protein, for example, being a function of the mRNA now, maybe if you said, oh, it's a function of the mRNA five minutes ago. And that's just because maybe it takes time to make the protein. Or it takes time for this or that. You could introduce an explicit delay like that.**

**Or you could even, instead, have a model where you just have more steps. So what you do is you say, oh, well yeah, sure. What happens is that, first, the mRNA is made. But then, after the mRNA is made, then you have to make the peptide chain. Then, the that peptide chain has to fold. And then, maybe, those proteins have to multimerize.**

**Indeed, if you right down such a model then, for some reasonable parameters, you can get oscillations just with negative auto regulation. And indeed, I would say that over the last 10 years, probably, the reigning king of oscillations in the field of system synthetic biology is Jeff Hasty at San Diego. And he's written a whole train of beautiful papers exploring how you can make these oscillators in simple G network.**

**So he's been focusing in E. coli. There's also been great work in higher organisms in this regard. But let's say, Hasty's work stands out in terms of really being able to take these models and then implement them in cells and, kind of, going back and**

19

**forth. And he's shown that you can generate oscillations just using negative auto regulation if you have enough delays in that negative feedback loop.**

**Are there any questions about where we are right now? I know that we're supposed to be talking about the repressilator. But we first have to make sure we understand the negative auto regulation. So everything that we've said, so far, in terms of the models was all known.**

**But what Michael wanted to do is ask whether he could really construct an oscillator. And he did this using these three mutual reppressors. We'll say x, y, and z just for now. x represses y, represses z, represses x. And has a nice model of this system that helped him guide the design of his circuits.**

**So experiments-- as most of us who have done them know-- experiments are hard. So if you can do a week of thinking before you do a year of experimental biology, then you should do that. And what were the lessons that he learned from the modeling that guided his construction of this circuit? Yeah?**

**AUDIENCE: Lifetime of mRNA.**

**PROFESSOR: Right. So you want to have similar lifetime of the mRNA and the protein. And this is, somehow, similar to this idea that you need more delay elements because if you have very different lifetimes, then the more rapid process, somehow, doesn't count. It's very hard to increase the lifetime of the mRNA that much in bacteria. So instead, what he did is he decreased the lifetime of the proteins of the transcription factors. In this case, x, y, and z. And you mentioned the other thing that he maybe did.**

**AUDIENCE: He introduced the leakage, but he didn't mention that that was--**

**PROFESSOR: That's right. So I guess, he knew that leakage was going to be a problem. I.e, that you want tight repression. So he used these synthetic promoters that both had high level of expression when on but then very low level of expression when being repressed.**

**He made this thing. And in particular, he looked at it in a test tube. He was able to**

20

**use, in this case, IPDG to synchronize them. And he looked at the fluorescence in the test tube. So the fluorescence is reporting on one of the proteins. We can call it x if we'd like. But fluorescence is kind of telling about the state.**

**And if it starts out, say, here, he saw a single cycle. Damped oscillations, maybe. So the question is, why did this happen? So why is it that, in the test tube, he didn't see something that looked very nice? Oscillations.**

**Noise. And in particular, what kind of noise? Or what's going on? Desynchronization, exactly. So the idea is that, even if you start out with them all synchronized-- you give it IPDG pulls, and they're synchronized in some way-- it may be that, at the beginning, all of them are oscillating in phase with each other.**

**But over time, random noise, phase drift, and the different oscillators leads to some of them come down and come back up. And then, others are slower. You start averaging all these things together. And it leads to damped oscillations at the test tube level within the bulk. Yes?**

**AUDIENCE: So what do you mean in the test tube? Like, you just take all these components and put it--**

**PROFESSOR: Sorry, when I say test tube, what I mean is that you have all the cells. So they still are intact cells. But it's just many cells. So then, the signal that you get the fluorescence is some average over all or sum overall. The fluorescence you get from all those cells.**

**So there's a sense that this is really what you expect given the fact that they're going to desynchronize. Of course, the better the oscillator in the sense that the lower the phase drift, then maybe you can see a slower rate of this kind of desynchronization. But this is really what you, kind of, expect.**

**All right. So that's what, maybe, led him to go and look at the single cell level where he put down single cells on this agar pad and just imaged as the cells oscillated and divided. Now there are a few features that are important to note from the data. The first is that they do oscillate.**

21

**That's a big deal because this was, indeed, the first demonstration of being able to put these random components together like that and generate oscillation. But they didn't oscillate very well. So they said, oh, maybe 40% of the cells oscillated. And I have no idea what the rest of the cells were doing.**

**But also, even the cells that were oscillating, there was a fair amount of noise to the oscillation. And the latter half of this paper has a fair amount of discussion of why that might be. And they allude to the ideas that had been bouncing around and from the theoretical computational side demonstrating that it may be that the low numbers of proteins, genes involved here could introduce stochastic noise into the system and, thus, lead to this kind of phase drift that was observed experimentally.**

**I think that this basic observation that Michael had that he got oscillations, but they were noisy. That is probably what led him to start thinking more and more about the role of noise in G networks and so forth and led, later, to another hugely influential paper that is not going to be a required reading in this class but is listed under the optional reading, if you're interested. But we'll really get into this question of noise more a couple weeks from now.**

**Were there any other questions about the experimental side of this paper? I wanted to analyze maybe a little bit of simple model of the repressilator. So the model that they used to help them design this experiment involved all three proteins, all three mRNAs.**

**And what that means is that, when you go and you do a model, you're going to end up with a six by six matrix. And I don't have boards that are big enough. So what I'm going to do instead is I'm going to analyze just the protein only version model of the repressilator. All right.**

**So what we have here is three proteins. p1 2 3 p1 dot. And we have degradation of this protein. And we're going to analyze the symmetric version, just like what Michael did. So that means we're assuming that all the proteins are equivalent. I'm sure that's not true because these are different promoters and different everything.**

22

**But this gives us the intuition. So it's minus p1. And this is protein 1 is repressed by trajectory protein 3. Protein 2 is going to be repressed by protein 1. And then protein 3 is going to be repressed by protein 2.**

**So this is what you would call the protein only model of the repressilator. Now just as before, the fixed points are when the pi dots are equal to 0. And we get the same equation that we, basically, had before where the equilibrium or the fixed point, again, is going to be given by something that looks like this. So it's the same requirement that we had before.**

**Now the question is, how can we get the stability of that internal fixed point? It's worth mentioning here that now we have three proteins. So the trajectories are in this three dimensional space. So from a mathematical standpoint, determining the stability of that internal fixed point is actually not sufficient to tell you that there has to be oscillations or there cannot be oscillations because these trajectories are, in principal, allowed to do all sorts of crazy things in three dimensions.**

**But it turns out that it still ends up being true here that when this internal fixed point is stable, you don't get oscillations. And when it's unstable, you do. But that, sort of, didn't have to be true from a mathematical standpoint.**

**All right. Now since this is now going to be a 3 by 3 matrix, we're going to have to calculate those eigenvalues. Now how many eigenvalues are there going to be? Three? OK. So this thing I've written in the form of a matrix to help us out a little bit. But in particular, we're going to get the same thing that we had before, which is the p1 tilde.**

**So these are deviations, again, from the fixed point. And we got this matrix that's going to look like this. Minus 1, again, 0. It's the same x that we had before conveniently still on the board. So this is just after we take these derivatives.**

**And then, we have p1 tilde, p2 tilde, and p3 tilde. Now what we need to know is, for this Jacobian, what are going to be the eigenvalues? For this thing to be stable, it requires what? What's the requirement for stability of that fixed point? That p0?**

23

**AUDIENCE: [INAUDIBLE]. PROFESSOR: OK. Right. For two dimensions, this trace and determinant condition works. It's important to say that that only works for two dimensions, actually, the rule about traces and determinants. So be careful. So what's the more general statement? Yeah.**

**AUDIENCE: Negative eigenvalues.**

**PROFESSOR: Exactly. So in order for that fixed point to be stable, it requires that all the eigenvalues have real parts less than 0. So in order to determine the stability of the fixed point, we need to ask what are the eigenvalues of this matrix. And to get the eigenvalues, what we do is we calculate this characteristic equation, this thing that we learned about in linear algebra and so forth.**

**What we do is we take-- all right, this is the matrix A, we'll say. This is matrix A. And what we want to do is we want to ask whether the determinant of the matrix A minus some eigenvalue times the identity matrix. We want this thing to be equal to 0. So this is how we determine what the eigenvalues are.**

**And this is not as bad as it could be for general three by three matrices because a lot of these things are 0. So this thing is just this is the determinant of the following matrix. So we have minus 1 minus lambda 0. This thing x that's, in principle, bad.**

**Minus 1 minus lambda 0. Getting 0 x minus 1 minus lambda. Now to take the determinant three by three matrix, remember, you can say, well, this determinant is going to be equal to-- we have this term. So this is a minus 1 plus a lambda times the determinant of this matrix.**

**And then, we just have that's this. The product of these minus the product of these. So this just gives us this thing again. So this is actually just minus 1 plus lambda cubed. Next term, this is 0. That's great. We don't need to worry about that.**

**The next one, we get plus. We have an x. Determining here, we get, again, x squared. So this is just an x cubed. We want the same equal to 0. So we actually**

24

**get a very simple requirement for the eigenvalues, which is that 1 plus the eigenvalues cubed is equal to this thing x cubed.**

**Now be careful because, remember, x is actually a negative number. So watch out. So I think that the best way to get a sense of what this thing is is to plot it. Of course, it's a little bit tempting here to just say, all right, well, can we just say that 1 plus lambda is equal to x?**

**No. So what's the matter with that? I mean, it's, sort of, true, maybe, possibly. Right. So the problem here is that we're supposed to be getting three different eigenvalues. Or at lease, it's possible to get three different eigenvalues. So this is really specifying the solution for 1 plus lambda on the complex plane.**

**So the solution for 1 plus lambda we can get by thinking about this is the real part of 1 plus lambda. And this is the imaginary part of 1 plus lambda. And we know that one solution is going to be out here at x. This distance here is the magnitude of x.**

**Now the others, however, are going to be around the complex plane similar distances where we get something that looks like this. So these are, like, 30, 60, 90 triangle. So this is 30 degrees here because what you see is that, for each of these three solutions for 1 plus lambda, if you cube them, you end up with x cubed.**

**So this guy, you square it. Cube. You end up back here. This one, if you cube it, you start out here, squared, and then cubed comes back out here. Same thing and this goes around somehow. All right, so there are three solutions to this 1 plus lambda. And there are these points here.**

**Now, of course, it's not 1 plus lambda that we actually wanted to know about. It was lambda. But if we know what 1 plus lambda is, then we can get what lambda is. What do we have to do? Right, we have to slide it to the left.**

**So this is the real axis. This is the imaginary axis. 1. So we have to move everything over 1. Now remember, the requirement for stability was that all of the eigenvalues have real parts that were negative. That means the requirement for stability of that**

25

**fixed point is that all three of these fixed points are in the left half of the plane.**

**So what you can see is that, in this problem, the whole question of stability and whether we get oscillations boils down to how big this thing is. What's this distance? If this distance is more than 1, then we subtract 1, we don't get it into the left part of the plane. OK, I can't remember which case I just gave.**

**But yeah, we need to know whether this thing is larger or smaller than 1. And that has to do with the magnitude of x. So if the magnitude of x-- do you guys remember your geometry for a 30, 60, 90 triangle?**

**All right, so if the magnitude of x-- and this is indeed the magnitude of x. This short edge on a 30, 60, 90 is half the long edge, right? So what we can say is that this fixed point stable, state fixed point, is if and only if the magnitude of x is what?**

**Lesson two. OK. That's nice. And if we want, we could plug in-- just to ride this out. This is n alpha p 0 n minus 1.**

**So it's useful, once you get to something like this, to try to just ask, for various kind of values, how does this play out? What does the requirement end up being? And a useful limit is to think about what happens in the limit of very strong expression? So strong expression corresponds to what?**

---

[← AUDIENCE](06-audience.md) · [Up: contents](index.md) · [AUDIENCE →](08-audience.md)
