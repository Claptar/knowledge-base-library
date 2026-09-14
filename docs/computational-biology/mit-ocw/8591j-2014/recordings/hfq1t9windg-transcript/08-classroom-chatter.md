---
title: '[CLASSROOM CHATTER]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/hfq1t9windg-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [CLASSROOM CHATTER]

**Source:** `recordings/hfq1t9windg-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Did you guys all decide you're comfortable? Why don't we go ahead and reconvene. It seems like it may be we're coming to consensus here. Ready? Three, two, one. So now we got a clear majority agreeing that it should be D.**

**So what happened was that over here in the original equations we had a real concentration of u divided by some k. And that was the k for repressing v. Because v is this guy that is over here. And what we did is we then just turned u divided by this k for binding this v promoter into just u. So in particular, when that concentration of u is equal to its associated k, that corresponds to half repression.**

**Same thing here. One way to think about this is just that when u is equal to 1, we're getting half of maximum possible repression. Similarly, that's what v equal to 1 means. U and v, do they have to have the same-- I mean, does u equal to 1 and v equal to 1 mean the same thing in terms of the number of the proteins in the cell? No. Not necessarily.**

**So we've allowed for the possibility that those things are measured in different real units. But in both cases, it's telling us about how the strength of repression. And u**

15

**and v equal to 1 tells us about that crossing point where the other promoter is half repressed. Are there any questions about what happened there? This is especially confusing because it doesn't enter into the equations at all.**

**Things just went away. But you know that this is the dimensionless versions of the equations because we have u here, and we're adding 1 to it. Are we allowed to add things with different units? No. Never.**

**What that means is that-- since they're being added, that means that we already know that we made-- this is the dimensionless version of the equation. And it actually then immediately tells us what u equal to 1 means.**

**So now what we want to do is we want to make sure that our intuition on this is tip top shape. In particular, we want to know if I want to change the dynamics of the system-- so let's say that we go and we spend lots of time calculating the fixed point stability, and we do everything on these equations. And then we know what we need to do is we need to change some parameter in order to get say, a toggle switch. We need to know how we do that. We need to know how the parameters in real life, or even in the context of the model, how is it that the parameters you can actually change experimentally, how is it that the affect or not the parameters in this model?**

**So the question is, let's say we increase the degradation rate of these two transcription factors u and v, which of the parameters are going to change? So I'll give you 30 seconds to think about what should be happening here. Do you need more time? Let's see where we are.**

**Ready? Three, two, one. And this is the possibility where you can put up two things. Remember our fabulous card system? So I think most people are saying it's going to be A and B are going to change.**

**So beta and gamma are capturing how cooperative that transition is. And the cooperativity is not affected by the questions of the exact concentration, or time scale and so forth. Because that has to do with the molecular nature of the interactions with the promoter. So in some ways beta gamma are the simplest**

16

**things in this system.**

**Now the question is, do alpha 1-- do they go up or do they go down? Now that I've told you that they change. If degradation rate goes up, alpha 1 and alpha 2, do they go up or do they go down? I'll give you 10 seconds to think about it.**

**Do you need more time? Let's see it. Ready? Three, two, one. It's a majority are saying it's going go down. Can somebody offer up an intuitive explanation for why this might be? [INAUDIBLE].**

**AUDIENCE: The degradation rate goes up, it means the times scale goes down. As you produce a fixed number of per unit time, the unit time gets smaller and produces less.**

**PROFESSOR: Right, so if the degradation rate goes up, that's kind of reducing this unit of time. So you just are not going to make as much protein in that unit of time. The way that I like to think about this maybe is that if the degradation rate goes up, then the real concentration of the protein should go down.**

**And that means that the repression should be less effective. And then wait, is this helping me? No, now that I'm saying this-- I don't like to think about it that way. [INTERPOSING VOICES]**

**That's right. Yeah, so-- that's right. You should decrease the sort of-- So if the degradation rate goes up, you decrease the real concentration, which it means indeed that you are at steady state. Say a less effective repressor. That means the concentration goes down in these units of how repressive are you.**

**I think the way of thinking about it was correct, just the words were not. You can also then go-- and it's useful in the context of when you actually go and you do the math of removing all these parameters, just to make sure that-- because it's easy to do this thing where you just divide everything out, and you're happy, and whistling and so forth. But at the end of the day, you really just have no sense of what happened. Of how the parameters that come out of the model are affected by the real things that you can change.**

17

**And in some ways what's funny about these equations is that essentially everything is in the alphas. Because beta and gamma, that's this cooperativity parameter. That's what it is. That's all it is. So that means that everything else ends up in the alphas.**

**So the strength of the promoter, the concentration you need to repress, the lifetime, everything rolls up in these alphas. And this is the beauty of the dimensionless equations. Is it's telling you that you don't have all these different, separate knobs. You can't change one and change another, and go into some funny regime. Because it's all rolled into one fundamental parameter, these alphas.**

**That's telling you that once you understand how these equations behave, then you in principle understand everything that could possibly happen in that simple model. But that's what's wonderful about the dimensionless equations. But the problem is that you sometimes lose track of how it's related to the real experimental things. So I would say that I very much like these dimensionless equations. They clarify things for you.**

**But you have to spend the time to make sure that you understand where all of reality went. Because it all ends up in this mathematical equation, and that simplifies things. You're not floating in a sea of symbols anymore, but it's really easy to lose track of the connection to real measurements. And that's why we want to do modeling so we can make that connection. So do the dimensionless equations, but make sure that you play with them a bit so you know what changes when you change what.**

**And we'll actually see a bit later, some other cases where it's actually quite tricky to figure out what's happening. On exams I always want to just ask a equation like this, if this parameter goes off-- and then the TAs always say, it's too hard of an question. I feel like it's like the most basic thing you would want from an equation like this. Is that if you increase the strength of this--**

**But it actually is-- it's surprisingly difficult. So maybe this year I'll convince the TAs that it's an OK question. Are there any questions about where we are right now?**

18

**So what I want to do for the last half hour is talk about stability analysis. The first context in which stability comes up in this class is indeed in this toggle switch. But it's not-- I would say-- the most satisfying application of it in some ways. Just because you end up with equations that all you can do is plot them. And it's useful to be able to recapitulate, to understand how the figures from that paper come about.**

**But at the same time it's not always-- after you find the solution, you don't feel so happy about it either. Because in terms of complexity as a function of time, things always start out simple. And then in the course of the calculations things get complicated. And the problems that are fun to solve are the cases where it comes simple again. This one-- it never quite converges.**

**I do want to talk about the stability analysis so that you can understand the calculation that was in the notes. But also so that you can just get some more intuition about some of the other problems that we're going to be solving in the next few weeks. Just to make sure that we're all talking about the same thing, it's useful to start by just making sure that in a one dimensional problem, we understand what we mean by stability. We're going to be fast.**

**X equals 0 is stable if and only if what? I'll give you 10 seconds. Ready? Three, two, one. All right.**

**So this is always-- So there's actually a fair number of answers here. And this is tricky because the temptation is always to jump into the two dimensional stability analysis, or the n dimensional stability analysis. And the thing is that we have to make sure that we are completely comfortable with a one-- talked about one dimension before you talk about multiple dimensions, because then everything is lost. I'm not going to have you guys discuss, the but it's going to be C. Many people are saying A or other things. There is a context in which this guy comes in. But let's just make sure.**

**So x equal to 0. Now first of all, is this thing-- is x equals 0, is it always a fixed point**

19

**of the system? Yes. So fixed point means that if you go right there, then in principle you don't move off it. So it doesn't say anything about whether it's stable or unstable. But if x equals zero, then indeed x dot is equal to 0. So that's a fixed point.**

**But if you have positive x-- in order for that to be stable, you have to have a negative change in x. So if you talk about the behavior as a function of time, this function of x here. If you start out above 0, the definition of stable is if you go a little bit away, you should come back. And that means that x dot has to be negative. So if positive x-- and similarly if x is negative, you want it to be stable, then you need the x dot to be positive.**

**So this is-- A less than 0. Now there is a context in which a stability condition looks something a little bit more like this. And can somebody say when it is that you get something to look-- condition around 1? Yes?**

**AUDIENCE: Discreet.**

**PROFESSOR: Yeah, in discrete maps then indeed the condition for stability looks something like this. If you have something that looks the x of t plus 1, is equal to axt, then if the condition for x equal to 0 being stable is for indeed a to be less than 1. Or it's in this case it's really the magnitude of a being less than 1. Because in that case you might get hopping. But then the condition is around the 1 thing, whereas here 0 [INAUDIBLE] indeed.**

**Solution is different-- it's going to go exponentially to-- so x is a function of time is just going to be some x naught e to the-- and is it at, or a is less than 0. It's just at, right? And in this case, we just have one dimension. So the eigenvector [INAUDIBLE] is really just x. There's just one eigenvalue, and a is indeed the eigenvalue.**

**So the stability for x equals 0 to be stable is that all-- and in general, for n dimensions, is that you need all the eigenvalues to be less than 0. And in this case, a is indeed the eigenvalue. And you need that to be less than 0.**

**So if you're not comfortable with this, or you got something other than C, then I think**

20

**it's essential that you take the time now to go over all of these ideas. First in one dimension. Make sure you're all comfortable with that. But then to look again at these two dimensional, high dimensional stability analyses. Because if these things you're finding tricky just because it's been a while since you looked at this stuff, that's fine. But if you don't spend the time to iron out now, then everything gets much more painful later.**

**I highly recommend Strogatz's book on dynamical systems. It's a beautiful book with just as clear as a textbook could be. So that book is available at various libraries and reading rooms and so forth. So it's a great reference.**

**Now we want to do is generalize this idea to think about in n dimensions. So now what we have a vector x. And there's going to be some matrix A that-- oh, and x dot. So the change in this vector x is going to be described by a linear set of equations, so that they can be specified by some matrix.**

**To determine the stability, we're going to then look at the eigenvalues of this matrix. Now in many cases in this class, what we're going to do is we're going to find that some set of non-linear equations has a fixed point somewhere, and then we're going to linearize around that fixed point to convert into a linear problem that looks like this. But for now what we're going to do-- the general statement is for n n dimensions. You want all the eigenvalues-- lambda I in particular-- to be the real part to be less than 0. And that has to be true for all the eigenvalues.**

**We're going to be talking about the conditions in a two dimensional system where there are in principles and shortcuts, but it's all the same thing. It's all that you need. The real part of all the eigenvalues be less than 0 for the fixed point be stable.**

**So for now what we're going to do is we're just going to imagine that we have-assume we have two dimensional problem. This vector x, we're going to write as x and y. So we can write the dynamics like this. This is x. This is x dot, y dot.**

**And this is really the same thing as saying that x dot can be described by some ax plus by, and y dot is some cx plus dy. And so we want to be as comfortable as we**

21

**can with all the possible things that could happen in these two linear and differential equations. And particularly we want to know what the condition for 0, 0 being stable? 0, 0 is stable if and only if-- now there's a rule that you found in your reading having to do with the trace and the determinant.**

**So trace is the sum of these two. Determinant is product minus the product here. Now this is not the kind of thing that you have to memorize. But it's useful to know that there is a simple rule, because it allows you to quickly determine whether something could possibly be stable. And you don't have to memorize it, but you should be able to figure it back out later.**

**So what we have is the trace of this thing being less than 0-- so I'm going to give you some options. Now of course, you can always look at your notes and that is not going to help you. You're not being graded on your answers right now. I'm going to encourage you to try and think about it and see if you can recapitulate what this thing should be. So it's less than, greater than--**

**So for example you can start to think about-- you should be able to write down some equation that you know is stable. And figure out, OK, what conditions would it satisfy. That's a common, useful trick to be able to do in life. To dredge these things out of memory. Do you understand the question?**

**I'm going to give you 30 seconds because it's well worth trying to figure out what this rule should be. So from the reading you know there's some rule about the trace and the determinant. And indeed they both have to be true in order-- this is an and sign. May be an and sign.**

**Do you need more time? It's OK if you haven't actually been able to recapitulate this. But it's useful to think about it. Should we go ahead and vote just to see? I'm just curious where we are.**

**Ready? Three, two, one. So we have a lots of B's. And can somebody give me an example of a matrix A that really ought to be stable? Yeah?**

**AUDIENCE: Negative identity.**

22

**PROFESSOR:**

**Negative identity, OK. So if the matrix A is something that's minus 1 here. 0, 0 minus 1. Then x and y are uncoupled. x decays exponentially, y decays exponentially. Now we can just directly say, well, this, the trace is definitely negative, and the determinant's positive.**

**It's 1 minus 0. So that gets us here. Because I think there are many situations in life that are like this, where you know that there's some rule and you can't remember what it is. You don't need to actually remember, once you know that there's the rule, then you can figure out what it had to have been.**

**This is not a proof. The proof is only a few lines. You can do it, but the point is that this kind of situation comes up a lot. It's useful to just have simple things that you know what the answer has to be, and then that allows you to figure out where things were.**

**And indeed what you'll find is that for a two dimensional system, this condition that the trace of the matrix is less than 0 and the determinant is larger, that is equivalent to the statement that the real part of both eigenvalues is less than 0. And there's the derivation is simple, and it's in your notes. Are there any questions about where we are right now?**

**So what I want to just say a few more things about the trajectories here. Can somebody explain the notion of what's an intuitive statement about the eigenvectors that you get out here? Why do we like eigenvectors? What are they useful for?**

**AUDIENCE: Decoupling the differential equations.**

**PROFESSOR: Right, so they're decoupling, and there's a sense that-- I guess the way I like to think about this is that you have a fixed point say, like this. Now if these things are stable, that means the arrows are all say coming in. Are these eigenvalues-- are they purely real, or are they complex? Reminder, somebody?**

**Real and negative. There's no imaginary component. This is a stable fixed point with real negative eigenvalues. Now the idea of these eigenvectors is that these are**

23

**the two directions in which if you start out on one of them, you'll stay on them.**

**And in general then you can-- any other trajectory you can decompose as a combination of the pads on the two. The position as function of time can always described as the sum of the eigenvectors where you grow or you shrink along each eigenvector exponentially. Now for this thing to be stable, all these lambda I's are going to be negative. We have this property that-- that the dynamics of this matrix kind of keep you along the direction of the eigenvector.**

**What this is saying is that if you start somewhere random, that is off one the eigenvectors, then you can decompose the trajectory along each. But I just want to highlight that it's often useful to draw what these things end up looking like. Now I want to make sure I get this one correct. I'm a little bit worried I'm going to do something funny.**

**So here-- we're going to say this is v1 and this is v2. So this direction is one eigenvector, this direction is the other. So let's imagine that the trajectories look like this. The question is which eigenvalue is closer to 0?**

**Is it A eigenvector v1, or B eigenvector-- So this is really lambda 1 verses lambda 2. 1 is closer to 0 than is 2. Which of the eigenvalues is closer to 0? I'll give you 20 seconds to think about this because it's useful to be able to extract these things from the trajectories.**

**Do you need more time? And it's fine if you don't really understand how you can get to this question from this figure, then go ahead and flash C, D, or E, just so I know where we are. Let's vote. Ready? Three, two, one.**

**All right, so there's at least a majority are saying that it's going to be lambda 2. Can somebody offer why that is? Yes?**

**AUDIENCE: I sort of see it as whichever one is bigger is going to be more effective at squeezing things toward the origin along that axis.**

**PROFESSOR: OK and bigger-- and you're saying more negative, in this case, you're saying? Yes,**

24

**right. So yeah that's right. So there's some notion that lambda 1 has to be more negative than lambda 2 because you first collapse along the direction of eigenvector 1, and then you slowly come in along the direction of eigenvector 2. That's saying that you have these two exponential decays, and the directional on the eigenvector 1 is more rapid than the directional on eigenvector 2.**

**I think in many of these cases in dynamical systems, differential equations, it's hugely valuable to be able to draw the trajectories. So in many cases, what we're going to do over the course of the semester is we're going to have a simple pair of differential equations that are going to be two proteins, or they're going to be rabbits and foxes or whatever. So we're going to locate where the fixed points are. And then we're going to figure out the stabilities and the eigenvectors.**

**And then we can really understand the entire dynamics of the system without solving the full thing, without using a computer. But just by figuring out where the fixed points are, and then the dynamics around there. Then you can basically understand all the dynamics of the system. But you have to make sure that you develop intuition of how systems behave near their fixed points.**

**Now this is a case where both of the eigenvalues were real. But of course, if you have complex eigenvalues, if you do the calculations, you'll see that the eigenvalues are going to be a complex conjugates of each other. And there you get spirals. So trajectories might look like so.**

**So there are two qualitatively different ways that the fixed point can be stable. You can have spiraling through a state of the fixed point, or you can come in via these straight lines. Of course, the specific trajectories in some cases, can be curved. And so if you look at a particular trajectory, sometimes even these can look a little bit spirally, so be careful. Those are the two basic ways it works.**

**There's a simple way of getting a sense of the dynamics of a system, as a function of the trace and the determinant. So what we have-- something here. If you go ahead and you do the calculation, what you find is that the two eigenvalues are going to be described by this. And then the basic dynamics are going to be the**

25

**following. So down here, you have a case where the eigenvalues are real, and they're of opposite sign. And in this case, is that stable or unstable?**

**Unstable. So in order for it to be stable, all the eigenvalues have to have negative real components. So if they have opposite sign, one of them is going to be positive. So this is all unstable down here.**

**Over here you have a case where the eigenvalues are real, greater than 0. So in this case, the trajectories are also coming out somehow. All right, here, this is the case where they are real, but now both less than 0. So this is again, this is like what we drew here, where everything is stable coming in. And up here is where we get the spirals.**

**But over here, it's the real part is less than 0. So this is where we have the spirals coming in, whereas over here, the real part is greater than 0 and we have spirals coming out. Oh, I'm sorry. Uh, that would have been useful. So this is in the trace of A and this is in the determinant.**

**So these are the variety of possible outcomes when you have a two dimensional system that's already a linear two dimensional system. And this is indeed consistent with it, to have a stable fixed point, you need to have the trace less than 0, and the determinant greater than 0. So it's in this quadrant.**

**Now it's-- finally it's useful to-- so let's just for now, stick with the linear system. And just imagine a case where we have in this A-- so remember it's A, B, C, and D. So we saw one way in which this thing could be stable. Was that if b and c were both equal to 0, so there's no cross interaction, but a and d were both less than 0, then it's all trivially stable. Now the question is, if something that looks like this, a is equal to minus 2 and d is equal to plus 1.**

**Questions is, could such a system be stable? So I'm seeing some nods. And on the face of this, you say, oh, that's a little bit surprising. Because d being plus 1, what that's saying is that y on its own is unstable. So if you start out with no x and no y, and you add a little bit of y, y starts growing exponentially.**

26

**So y on its own is unstable, but x is stable its own. And the trace being less than 0-that's saying that there's some sense in which if y is unstable on its own, then x has to somehow be more stable than y is unstable. Because the sum of those things still has to be negative. Now that was necessary, but not sufficient, in order to have stability. Because we also need to have a condition on the determinant.**

**Now so the trace of a here-- that's minus 1. That's less than 0. OK, that's great. Now the determinant-- now it's going to be a times d. That's minus 2.**

**But then we also have to say minus b times c, right? And this thing has to be greater than 0. So what you see here is that b and c-- they have to have opposite signs order for this thing to work, in order for the origin to be stable. And the product has to somehow be strong. Now this makes sense, because of course, if b and c, or even for matter, just one of them were 0, then it would be impossible to get the stability.**

**But for example, if we have some situation where we have some x that's inhibiting itself-- that's a here-- but then y is activating itself. So y here is somehow on its own, unstable. Then what you need is you need maybe something that looks like this. Some cross activation and or repression. And what's interesting is that it doesn't matter which of the two, b or c is negative.**

**You can get actually, the origin to be stable in either way. But in this situation, you need the direction of the regulation to be in opposite directions. And if you'd like, you could then play with-- you could think for example about the directions of these trajectories around the origin, and so forth. But it's useful, I think, to play with the simplest toy systems that you can imagine, just so that you can get a sense of what are the basic ingredients that you need in order to get stability in something like this.**

**Because once you start doing the whole linearization around the fixed point, and then calculating traces and determinants, you're not going to have it. You're going to lose all your intuition about that about things at that stage. So it's useful to make sure that you nail things down in this context. We are out of time, so I'll let you go.**

27

---

[← AUDIENCE](07-audience.md) · [Up: contents](index.md)
