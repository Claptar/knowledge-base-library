---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/lc3xswq62iw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/lc3xswq62iw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**In the time example, you had death, it was a death rate. Is that in a [INAUDIBLE] space?**

20

**PROFESSOR:**

**OK. So I want to be a little bit maybe more clear. The claim is that-- Like the death, the delta there that we're thinking about, that didn't have to be the perturbation. It could be, but it didn't have to be. When we're plotting the bifurcation diagram, we're assuming implicitly somehow that there's a separation of time scales, such that this delta might be changing very slowly, and then other things are changing more rapidly. So this bifurcation diagram, it's really that you're tracking it.**

**So in the context of this n as a function of delta, this thing goes like this. And the idea is that oh, slowly you're getting more and more agricultural runoff, or the temperature is increasing. Doesn't have to be human induced, by the way, it could be something else. So the idea is that the population is slowly changing like this. And then eventually maybe you get this collapse.**

**Now, a perturbation could be something that could just be a drought, or something that is independent of this delta. But the statement is that, over here-- Now I'm going to be mixing things. At low delta, the claim is that you should get a dip and then rapid recovery. As the delta gets bigger, you get maybe even a larger-- The same perturbation could [? principally ?] do a larger dip, and it takes longer to get recovery.**

**This actually brings up another point, which is that these could all be the same perturbations. So this is a case where delta is increasing as we go down. So they could be the same perturbation here. Here you survive, here you survive. But then that same perturbation that was survived here could be the same magnitude drought, just as delta increases you expect this-- This may be able to push the system past the unstable fixed point, because of a loss of resilience.**

**This is something that we've seen in a variety of different contexts. I think it's a very general phenomenon. Just because the separation here is some measure of the resilience of the population, or the ability of the population to withstand perturbations. We can see that the resilience shrinks as we get close to this bifurcation. Did that answer your question? Sort of? Not really.**

21

**AUDIENCE: No, but it answered another question. PROFESSOR: It answered another question? Oh good. I'm glad that I answered something. But what was your-- Because you were saying is it the death rate that is causing this perturbation? AUDIENCE: Well, no. I was wondering for [? per ?] space. PROFESSOR: OK. Oh yes, I forgot. Yes, I do remember that you did ask that. So the idea here is that this could be a region that we fish, and this could be region that we don't fish, for example. Or it could be that, here there's just not as much food for the organism as there are here. So just the idea is that you would need kind of a sudden sharp boundary between regions of different quality. And that's kind of the situation where you would be able to measure this recovery length.**

**And the basic reason for that, is that if the environmental quality is something that changes very slowly, then the population density will just track that. So then you can't use that to measure this recovery length.**

**Of course, the same statement is true here. That if you have environmental perturbations that are changing slowly over time, then that also can complicate this picture.**

**Any other questions about that before we move towards multispecies ecosystems? We're going to start with two species.**

**So what I'm going to do is I want to spend the rest of the class talking about LotkaVolterra populations. And we're going to move the rock, paper, scissors discussion to Thursday, because it's a nice spatial example anyways.**

**So let's think about Lotka-Volterra. Now, there's a lot. Lotka-Volterra competition model.**

**So the assumption is that we're going to make here is that we have these two species that going to be interacting, but they're going to interact in kind of the simplest way that you might imagine. Which is that, if we plot the derivative of**

22

**population size n1 as a function of time, we get something that looks like this.**

**Now the first thing that you want to do when you see something like this is just to make sense the basic equation. In particular, in the absence of the other species, what happens to these populations?**

**We're going to assume here maybe first is that r1 and r2 are both greater than 0. It's in the absence of the other species. Do these populations survive or not? Ready? Three, we're going do it A, yes, B, no, our typical. All right, absence of a species. ready? Three, two, one, survival?**

**Yeah, they survive. For sure, because I told you that these guys are greater than 0, that means-- We can think about n1. In the absence n2, what is this equation? Logistic.**

**Now, if we wanted to think about these as describing competitive interactions, what does that tell us about the sign of the betas? Are the betas greater than 0, or are they less than 0? I'll think about it for 10 seconds. All right. Do you need more time? Ready? Three, two, one. Competitive means that the betas are greater than 0.**

**And what is the assumption somehow that's going into this? And we should remember that this is a minus everything up here.**

**AUDIENCE: I guess that somehow these two things are-- there's a fixed amount of some resource, that both of these things need. PROFESSOR: OK, so there could be some fixed resource. AUDIENCE: It's basically like an effective carrying capacity. PROFESSOR: That's right, so somehow it's modulating the effect of carrying capacity. And how is it that you would describe these betas? AUDIENCE: Sort of seems like you expect that the beta should be probably less than one. [INAUDIBLE] I guess it doesn't have to be less than one. Compared to how well n1-and individual of n1 takes up some of this. This is how much [INAUDIBLE]**

23

**PROFESSOR:**

**That's right. I think that's right. Now I think we-- There's a question about how explicitly to be thinking about these resources. Because it could be, it doesn't have to be one resource. And this is of course, a very phenomenological model. It's lumping all the interact-- All of the ways in which a species interacts in just a single parameter beta. But it's somehow, the betas are telling us something about how much does a member of the other species inhibit my growth, as compared to a member of my own species?**

**Because we have this n1 here, and just this species one will naturally lead to a carrying capacity k1, you only have species one. Now, the betas are telling you something about how much overlap they have in terms of maybe [? niche ?] or so. Now, if the betas are small, it means that they're not competing with each other very much. The betas could be larger than one, and what that's saying is that a member of this other species is inhibiting my growth more than a member of my own species.**

**So the standard way to analyze these equations is to look at these isoclines. So basically, if you say, OK well n1 dot is equal to zero, what does that mean? Well, we can just see that that's equivalent to saying that it's n1 plus beta1,2 n2 is equal to k1. So this is giving us a relationship between n1 and n2.**

**What do these look like on a plane, n1 versus n2 drawings? So the parabola, it's a line. And indeed, we can think about what happens when each of these is equal to one thing or another. So if n1-- If n2 is equal to 0, this thing is going across at k1. And that makes sense, because we already decided that in the absence of n2, this thing is just following logistic growth, where the species one will grow and go to k1. And that's a stable fixed point that n1 dot has to be equal to zero. It's a fixed point, so n1 dot has to be equal to 0. And it's going to cross at this other point here where n2 is going to be some k1 over beta 1, 2. And then we end up with a line.**

**Now if we go, and we ask what n2 dot is equal to, and this is equal to 0, we're going to end up with something that looks very similar. But now it's going to be n2 plus beta 2, 1, n1 is equal to k2. This is also going to be a line.**

24

**Given what I have said, how many different qualitative outcomes can you get in this model? Where we just assume-- Where we have beta-- Overall I think we're thinking about competitive interactions. How many cases do we need to consider? Alright, it's going to be a, 0.**

**Do you guys understand what I mean by cases? No? I mean, how many different kind of qualitative outcomes can there be in terms of species one or species two winning, or can you get coexistence? Or how many different kind of qualitative outcomes can there be? And if you're confused, you can not vote, or give me an unhappy face. OK, ready? Three, two, one. So**

**We have many Es. And can somebody explain why it that this is the case, without invoking that you've already studied this and you know the answer?**

**AUDIENCE: If you add another line, completely on top, or under, or it can cross too.**

**PROFESSOR: That's right, that's right. So the next thing I was about to do is draw another line. And the reason I stopped is because there are actually four different ways in which this other line can be drawn. And basically, you can have another line that does one. You can have two. You can have three. And you can have four.**

**OK? These two cases-- So this is we'll say one. I don't know what order i did it. Two, three, and four. Two and three, in both cases we have the crossing of the lines. So maybe does that mean they're the same outcome, the same qualitative outcome? No. And what will end up happening here is that we're going to get cases of--**

**So you basically can get that species one dominates independent of starting condition, assuming that both are present at the beginning. Species two could dominate. They could coexist, or you get bistability. History dependent, mutual exclusion. I just want to draw. So this one here was the-- We had a dashed line for n1 dot and we had the solid line for this. Yes?**

**AUDIENCE: Where is [? the breaking ?] [INAUDIBLE]**

25

- **PROFESSOR: So I guess if you swap the labels, or so, you're saying? I guess in the case that if one of them is just above the other one, then you can distinguish them. So if you have a dashed line here, you have a solid line here, that means that they--**

- **AUDIENCE: How do I distinguish case 2 and case 3? [INAUDIBLE] PROFESSOR: Maybe we should try to figure out which one's which, and then we can figure it out from there. Can somebody remind us, what are these lines again? Why are we drawing them, or what do they mean? So they're not actually quite a fixed point. It's a no incline. What's the difference between these things? If we have a fixed point here, what we're saying is that both n1 dot and n2 dot are equal to 0. Fixed point means that if you start right there, you'll stay right there. We're not yet say anything about stability. And this is going to be very relevant for Sam's question.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: The axes are definitely labeled. I think I may agree, but I'm a little worried that I'm-If you're happy I'm happy. OK let's-- A fixed point of this pair of equations will be when both of the derivatives are equal 0. And that's not the line that we've drawn. The lines that we've drawn are just when one or the other one is equal to 0.**

**So what does that mean about in case four, is it possible well to have coexistence? No. Because there's no fixed one in the middle. The only case it's possible to get coexistence is either line two or line three. But that tells us there's a fixed point, it doesn't tell us about the stability of the fixed point, though. What we'll find is that in one case, it's a stable fixed point, you get coexistence. In the other case, it's an unstable fixed point, and you get bistability.**

**What we're going to do now is we're going to ask and try to figure out in which case, how do we label these things? So what we'll do is ask, first of all in line one, we want to figure out, is that a situation where we know it's not going to be coexistence are bistability, but is it going to a situation where a species one wins, or when species two wins? But, if you want, you can vote for one of the others. I don't want to constrain your choices. So it's going to be a is one wins, B, two wins, not three wins.**

26

**This is something else. I'm going to give you a minute to think about what might be going on here. So the question is put in situation one.**

**Oh no, I did that wrong. In this. For the solid line, this is what we're asking for n1 is equal to 0. This is just equal to k2.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: What's that?**

**AUDIENCE: There's other [? null ?] lines.**

**PROFESSOR: You want more [? null lines? ?] I feel like there are lots of lines up there already. AUDIENCE: Where n equals 0 [? null ?] lines. The axes are actual [? null ?] lines.**

**PROFESSOR: Yes, that's right. Yeah, that's true.**

**AUDIENCE: That helps-- I'm confused between labels.**

**PROFESSOR: Oh, I see. OK I'm hesitant to draw anything more up on the board. But it is true that the axes are also [? null ?] lines. Because we have n's up there. I'll give you another 20 seconds to try to figure out this case one. Which of the species is going to win?**

**And let's go ahead and vote, and see where we are. Ready? Three, two, one. So there's a slight majority that are agreeing that in this case, it's going to be that one is going to win. And I think that it's a little bit hard to figure it out completely, but what I will say is that in the case where we're down here, what this means is that k1 divided nu beta 1,2 is larger than k2.**

**Now the question says, what happens in the limit of-- If species two does not hurt species one? Well that's when beta 1,2 goes to 0. And that's the situation where this goes up. So this is saying that if the beta 1,2-- And then we can figure out where this line is as well, because this thing is K2 divided by beta 2,1.**

**So if species to doesn't hurt to see one, but species one really hurts species two, that's going to be the limit where species one is going to win.**

27

**We are out of time. Maybe what we'll do is start class on Thursday by-- I'll start with this on the board, and then we'll complete these four possibilities, to try to get some intuition about it. And also draw these options.**

28

---

[← [SIDE CONVERSATIONS]](03-side-conversations.md) · [Up: contents](index.md)
