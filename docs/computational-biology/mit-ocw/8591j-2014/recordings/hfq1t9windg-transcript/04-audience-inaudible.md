---
title: 'AUDIENCE: [INAUDIBLE].'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/hfq1t9windg-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE].

**Source:** `recordings/hfq1t9windg-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Yeah, In this environment the bacterium-- they might be dividing every half hour. That's the characteristic time-- if these are stable, that would be the characteristic time scale for example, for GFP to go down. And of course, that's even after it's inhibited. After you stop making GFP.**

**In this case, once you had the IPTG, the lac I is going to fall off of this promoter, and then we have to first make A. And only after we make A will we start repressing expression of the B and GFP. That's the process that you expect to take, hours, based on the generation times.**

**But this is a memory module because after we've added the IPTG, now we can, in principle, take the IPTG away, and it'll stay low. So in principle, this IPTG signal can be a transient signal. And the cells will remember that they encountered IPTG.**

6

**That's what makes this a memory. This input can be transient. Transient signal is remembered.**

**Now a big part of why this why this paper was important is because this toggle switch was constructed out of components that previously in principle, had not even ever seen each other before. So maybe that lac I and this promoter had been put together, but this whole system, this whole gene network was composed of individual components that they were synthetic. And were put together because they thought, oh this should kind of work.**

**And it's led to, I think a real flowering of, this intersection between modeling and experiment. This thing was built based on a model that told them that maybe if we do this, these things they multiplarize in order to repress and so forth. So there was a real sense in which the modeling-- and then we're going to talk more about the modeling-- on how it was essential to get an idea of how we should construct this thing, and to guide our work. Because if any of you do work in the lab, you'll know that things are hard. And often components don't behave the way you think they should and so forth.**

**Now modeling can't save you from all that pain, but at least it can guide you in the right direction so that it limits the number of things you have to try. Are there any questions about this element, before we switch over to some of the dimensionless equations that we're going to be using?**

**So the reading for today was composed of a review that these two pieces, and one of which I think might be hard for some people, and the other one might be hard for other people. For those of you with maybe more limited experimental experience in biology, maybe the review was a challenge to try to understand all of the nomenclature and the words, whereas those of you that have not played with differential equations as much recently, may have found the reading on modeling the toggle switch and stability analysis to be more challenging. We will, in some cases, do this where we have two different hopefully shorter kinds readings.**

**And hopefully they're not both hard for you, because then you'll spend a lot of time**

7

**reading. But then it will be good for you. So don't run away quite yet. But from my standpoint, it's essential that you develop intuition behind these ideas.**

**So once you have this equation that somebody gives you, you have to be able to figure out what assumptions have they made, and what should the behavior be roughly, before you go off and you do simulations and full mathematical analysis. So a lot of what we're going to do in this class, and in particular during the lectures, is to try to work on that intuition. And the first thing you need to do is make sure that you know if you don't understand something. Sometimes things look really simple, especially these dimensionless equations.**

**Part of what's attractive about them is that they are simpler. But the connection to experiments can be quite challenging. And we'll kind of see some of this.**

**So these dimensionless equations-- dimensionless equations-- I think that they're both good and bad. The good is that you can figure out what are the essential features of the model. So you can focus your attention on the essential mathematical features.**

**The disadvantage is that you might not even know which of the parameters change when you do something experimentally. So the problem is that the connection to the biology or experiments is obscured in some cases. Connection to experiments.**

**And as an example of this, what we want to do is look at these equations for the toggle switch. I know that you guys just did reading on how to get to these final pair of equations. It's important to remember that in the context of the paper, they had a model. Here are the dimensionless equations that describe our system. And we use them to design the toggle switch.**

**But just from that, you don't necessarily realize what's been done. So we want to make sure we understand it. So the equations that we want to be comfortable with are the following. So it's u dot du dt. Now here they use alpha as the rate of expression.**

**So beware, in the past, we sometimes used alpha as a rate of degradation. So fair**

8

**warning. Alpha 1 1 plus that's v beta. v to the beta minus u v dot is equal to-- here is an alpha 2 divided by 1 plus u to the gamma minus v. Now in many, many cases, we're going to get-- equations that look like this are going to pop up time and time again over the rest of this semester, and you just have to be intimately familiar with them.**

**So first of all, can somebody say why this might be capturing the dynamics of a toggle switch? I can say something. Yes, please.**

**AUDIENCE: There's some more of each u or [INAUDIBLE].**

**PROFESSOR: That's right. So the more v you have, the less production you're going to have of u, and vice versa. Now in many cases, beta and gamma are going to be something that's larger than 1. This is capturing some element of cooperativity in the repression on each side. So this thing is indeed just a u repressing a v, and vice versa.**

**Now these things are wonderfully simple equations. See that there are four parameters that are completely specifying the dynamics. Now you'll notice that the world is always to be more complicated than the four parameters. Now there are two ways in which these complications went away. One is that we are modeling a simple-- it's a simple model of a complex system.**

**But the other is that even the simple model has been simplified by going to this dimensionless version. So I want to make sure that you understood the reading to the point where at least you understand what units of concentrations, times, and so forth are in this model.**

**So first I want to ask about the effective lifetimes of proteins u and v. Of u verses v. So we'll maybe call this tau u and tau v. And I want to know which one-- and how these things are related to each other. Tau u greater than [INAUDIBLE]. DK is again, don't know.**

**Now of course in principle, the lifetimes of u and v can be anything. The question is,**

9

**once we've written down that equation, have we actually said anything about that? Have we already made in assumption or not?**

**Do you need more time? I see a fair number of quizzical faces, which may mean that even with extra time, the quizzical faces would not go away. Question. Yes?**

**AUDIENCE: Are you asking about the lifetime of individual [INAUDIBLE]?**

- **PROFESSOR: OK. All right. Yeah. So when I say effective lifetime, that's because if it's a stable protein, then the lifetime of that individual protein is maybe infinite, but you get an effective lifetime because of this dilution effect. So when I say effective lifetime in general, in this class, what I'm referring to is the sum of two effects of dilution to the cell growth, as well as actual degradation.**

**AUDIENCE: And you're saying [INAUDIBLE].**

**PROFESSOR: No. No, I'm saying given that the Collins Lab-- in their paper, wrote down those set of equations. I'm asking have they already specified anything about the effective lifetimes of these two proteins?**

**AUDIENCE: So in those equations, [INAUDIBLE]. Your question asks in units of that dimensionless time?**

**PROFESSOR: Yeah, I mean we can compare two times in some dimensionless-- yeah, we're going to also talk about that. Maybe I should have done that first. But this is a nice question because it's highlighting that you get a pair of equations, they look obvious, but then some of those basic things about the system are some how not quite clear. So I'm going talk about in this units of whatever time is being-- however time-- we're going to discuss how time is being measured in a moment as well. But however time is being measured, is there some relationship here or not?**

**Let's go ahead and vote. And it's fine, if you really do not know what I'm talking about, you can say E and that's fine. Let's see where we are. Ready, three, two, one.**

**So I would say that it's split between B's and D's. And that's great, because that**

10

**means we have something to talk about. There's broad agreement that it's one of these two.**

**So turn your neighbor. You should be able to find somebody that disagrees with you. If you can't find anybody that disagrees with you, you could think about how parameters are going to change as you vary other experimental things.**

---

[← [INAUDIBLE].](03-inaudible.md) · [Up: contents](index.md) · [[CLASSROOM CHATTER] →](05-classroom-chatter.md)
