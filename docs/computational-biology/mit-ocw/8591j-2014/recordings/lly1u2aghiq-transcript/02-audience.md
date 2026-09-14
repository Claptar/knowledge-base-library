---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/lly1u2aghiq-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/lly1u2aghiq-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**--in the case of having one [? and the same-- ?]**

**Yes. So, if you'd like, we could put an average sign here, to say an average over time. Because in many, many cases, what we're really interested in is the fraction of time that, say, the promoter is bound, or the enzyme is bound, or whatnot. And if you have many, many, many molecules, then at any moment in time, the average is the time average. But once you're down to a single molecule, then you really want to take a time average.**

**We'll revisit this in just a moment using the math, but what's interesting is the math also can mislead you. Other questions? If somebody wants to argue forcefully what their neighbor said was right, then I'm happy to-- we will come back to this in a little bit.**

**If I want to do the fourth possibility, which is the total concentration of the enzyme, it's going to go to infinity. I'll give you, again, eight seconds to think and then get your card ready. Are you ready? Three, two, one. OK.**

**So we actually have a fair amount of disagreement, between As and Bs it seems. Go ahead and, again, turn to your neighbor, but maybe find somebody that disagrees with you. Sometimes there are pockets of people that agree one way or the other. So try to find each other.**

**Yeah, I know. I understand. You can try to figure out the expression for the fraction bound, and how that behaves. And that's actually kind of weird as well, frankly. Why don't we go ahead and reconvene, just so I can see. And maybe, let's go ahead and re-vote, so I can see if anybody convinced anybody of anything else. Ready. Three, two, one.**

**So it seems like now there's pretty good agreement. The answer to this is going to be A. There were a fair number of people that said B before. So here comes our curvy lines.**

**And so the idea here is that in the limit of the enzyme concentration going to infinity,**

9

**in that limit the fraction bound has to go to 0, because you just don't have any substrate to bind. And even if all the substrate's bound-- and indeed in this limit, what fraction of the substrate ends up being bound?**

- **AUDIENCE: All of it. PROFESSOR: All of it, right. So then, indeed, the fraction bound is just going to be the concentration of the substrate divided by the concentration of the enzyme. In the limit of the concentration of the enzyme going to infinity, then the fraction of the enzyme bound is going to go to 0. You're unhappy.**

- **AUDIENCE: I think having made an extremely eloquent argument, number 3 for B, I actually think that that answer is wrong.**

**PROFESSOR: OK. So this one, right? Yes, I mean, you had convinced me.**

**AUDIENCE: So if you take E total to 0 at fixed S-PROFESSOR: Fixed S, yes. AUDIENCE: --then the reaction rate is-PROFESSOR: You have to take the limits carefully, I think.**

**AUDIENCE: --is a ratio of the forward propensity and the backwards propensity. PROFESSOR: Yeah. I think that the clearest way to think about it is as just that single enzyme. Because, it's certainly going to have some rate of binding, and then once it's bound it's going to have some rate of falling apart. And that ratio is not a function of whether there's one enzyme-- I mean, that ratio is well-defined. The time average of the probability of that enzyme being bound is, indeed, a well-defined quantity. AUDIENCE: So can Ethan say D and it depends on the Kd?**

**PROFESSOR: Well, people always like to argue Ds. We can write down what the expression is, actually, now. And then you can decide whether you think D is justified.**

10

**We can also just try to figure out, what's the equilibrium of this thing? So the change in the complex concentration as a function of time is just going to be the rate of creation minus the rate of destruction. So there's just going to be this K forward, ES- oh sorry, these brackets are awful-- Kr, ES. And we just want to set this equal to 0, if we want to figure out what the equilibrium there is. And in one line, you can find that the fraction bound can be written as a concentration of the substrate here, divided by Kd, plus S. Is this correct from standpoint of units?**

**So there's something that you might find troubling about this expression, though. Is anybody troubled by it?**

**AUDIENCE: But it equals 0. PROFESSOR: You could say, what if E total is 0? I'd say that if E total is actually zero, now I think that's an ill-defined quantity. So, at some point, I'll side with the philosophers here. But if there is an enzyme to talk about fraction bound, then-- So it's related to this, but it's--**

**AUDIENCE: But whenever you have [INAUDIBLE] E [INAUDIBLE].**

**PROFESSOR: Right. So we've already discussed from our intuition that as E total goes to infinity, then the fraction bound is supposed to go what? To 0, we decided, right? And does this expression do that?**

**AUDIENCE: Well this is S, not S total.**

**PROFESSOR: Yes! So this is S, not S total. And once again, really easy to screw this up. Because, in many contexts, S and S total are the same thing. Especially, in context of enzyme kinetics, it's often the case that the concentration enzyme is really rather low, and then the substrate concentration is huge, so then S and S total we can really treat as being interchangeable. But here, in the general context, we can't. And this concentration of S, this thing is a function of the concentration of the enzyme.**

**So this guy here, it's a function of the total amount of substrate you have and also E total, and for that matter, Kd. So really this thing is a true statement, but it's very**

11

**misleading if you're not keeping track of what these things mean. Because, this thing is very simple, except for that it's really actually complicated because S section depends on everything right?**

**Now there's one context in which you can be safe in assuming that S and S total are the same, and that's in the limit of, for example, E total going to 0. So if you just have 1 enzyme, then this expression is, essentially, always valid. Every now and then, you might be using up one of your substrate molecules, occasionally. Right? But it's pretty safe to say that in the limit of E total going 0, when it's just in the limit of one enzyme, then it's really just described by a curve that looks like this.**

**And this curve is something that you see over, and over, and over again. And this is the fundamental reason that Michaelis Menten kinetics looks the way it does. But this is going to be very useful for us because, in many contexts that we're interested in, we want to think about, for example, the rate expression of some gene.**

**And what we want to know about is the fraction of time that it's going to be bound by, say, a transcription factor. So then, in the simplest case, we get an input-output relationship that is just given by this. Because, there's just one, or few copies, of that DNA, so it doesn't really sequester the transcription factor that's going to be binding it.**

**Do you guys understand why this is weird? A thing you have to be careful of? And more generally, I strongly recommend that, in all of these sorts of problems, it's good to just plot some things.**

**For example, the fraction bound is a function of if you vary the substrate concentration. Because, often you think that you know what's going on, and then when you just go and sit down to draw some curve, just get your intuition, you realize you don't know where it starts, you don't where it ends, you don't know what it does in between. It's embarrassing, but it's only when you sit down and try to do something like that that you realize that it's not obvious.**

**So just, for example, it's useful to imagine a situation, just between a similar E and**

12

**S, where we, for the sake of argument, say that S total is around this Kd. Now what we want to do is ask, what's the fraction bound as a function of E total? So we're going to fix total substrate, vary the enzyme concentration.**

**So we already know what the limit here should be. We go to infinity, what should this go to? 0. We know that eventually it should go to 0, and we already figured that out for any finite substrate concentration. Incidentally, on many of the exams, I will ask for plots of curves like this. So basically you want to indicate where it goes on one end, where it starts-- and where is it going to start in the limit of E total going to 0? Half. Then it's actually accurately described by that.**

**So we start here. This is 1. So we start at 1/2. And it's going to have to go in between those two, right? So what's the characteristic concentration here where something-- where it's changing a lot?**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
