---
title: AUDIENCE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/xnnxlsy-f-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/xnnxlsy-f-s-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**I'm still not understanding. So the value of p can not oscillate?**

**Right. So we're saying is that, right, p simply cannot oscillate in this situation where we have a differential equation describing p with-- if we just have p dot as a function of p and we don't have a second order. A p double dot, for example. So if we just have a single derivative with respect to time and some function of p over here, what that means is that, if p is specified, then p dot is specified.**

**And that's inconsistent with any sort of oscillation because any oscillation's going to require that, at this is given value of p-- this concentration of p-- in this case, the concentration's going down. Here, it's going up. So here, this is-- from that standpoint-- a multi valued function. OK? And other questions about this statement?**

**Even if I just written down some other function of p over here, this statement would still be true. And it's valuable to be able to have some intuition about what are the essential ingredients to get this sort of oscillation. And for simple harmonic motion, right there we have the second derivative, first derivative, and that's what allows oscillations there.**

**OK, so we can, maybe, write down a more complicated model of a negative auto regulation. And then, try to ask the same thing. Might this new model oscillate? And this looks a little bit more complicated. But we just have to be a little bit careful.**

**All right, so this is, again, negative auto-regulation. What we're going to do is we're going to explicitly think about the concentration of the mRNA. OK. And that's just because when a gene is initially transcribed, it first makes mRNA. And then, the mRNA is translated into protein. Right?**

6

**So what we can do is we can write down something that looks like this. M dot derivative of m with respect to time. It's going to be-- all right, so this is the concentration of mRNA. And p is the concentration of protein. OK?**

**All right, and what you can see is that the protein is now repressing expression of the mRNA. mRNA is being degraded. But then, down here, this is a little bit funny. But what you can see is that, if you have more mRNA, then that's going to lead to the production of protein. Yet, we also have a degradation term for the protein. Yes?**

**AUDIENCE: Why are we multiplying the degradation rate of the protein times some beta, as well?**

**PROFESSOR: That's a good question. OK, you're wondering why we've pulled out this beta. In particular-- right. OK, perfect. OK, yeah. This is very important. And actually, this gets in-- once again-- to this question of these non-dimensional versions of equations. Mathematically, simple. Biologically, very complicated. Well, first of all, what is that we've used as our unit of time in these equations?**

**AUDIENCE: The life of mRNA.**

**PROFESSOR: Right. So it's based on the lifetime of the mRNA because we can see that there's nothing sitting in front of this m. And if we want to, then, allow for a difference in the lifetime mRNA and protein, then we have to introduce some other thing, which we're calling beta.**

**So beta is the ratio of-- well which one's more stable? mRNA or protein, often, typically?**

**AUDIENCE: Protein.**

**PROFESSOR: Proteins are, typically, more stable. So does that mean that beta should be larger or smaller than 1? OK, I'm going to let you guys think about this just make sure we're all-- OK, so the question is beta, A, greater than 1? Typically, much greater. Or is it, B, much less than 1, given what we just said?**

7

**All right, you think about it for 10 seconds. All right. Are you ready? Three, two, one. All right, so most people are saying B. So indeed, beta should be much less than 1. And that's because beta is the ratio of the lifetime.**

**So you can see, if beta gets larger, that increases the degradation rate of the protein. What do I want to say? So beta is the ratio of the lifetime in the mRNA through the lifetime of the protein. Yes?**

**AUDIENCE: So I get why we have to--**

**PROFESSOR: Yeah. No, I understand. No, I understand you. I'm getting to your question. First, we have to make since of this because the next thing is actually even weirder. But I just want to be clear that beta is defined as the lifetime of mRNA over the lifetime of the protein.**

**What's interesting is, actually, there's a typo or mistake in the elements paper, actually. So if you look at figure 1B or so-- yeah, so figure 1B, actually. It says that beta is the protein lifetime divided by the mRNA lifetime. So you can correct that, if you like.**

**So beta's is the mRNA divided by the lifetime of the protein. OK, so I think that we understand why that term is there. But the weird thing is that we're doing p minus m over here. Right? And it feels, somehow, that that can't be possible. You know, that it shouldn't be beta times m over here because it feels like it's under determined. Right?**

**OK. So it's possible I just screwed up. But does anybody want to defend my equation here? How might it be possible that this makes any sense that you can just have the one beta here that you pull out, and it's just p minus m over here?**

**AUDIENCE: I think it's an assumption of the model where they choose the lifetime of the protein and the mRNA to be similar.**

**PROFESSOR: Well no because, actually, we have this term beta, which is the lifetime of mRNA divided by lifetime of protein. So we haven't assumed anything about this beta. It**

8

**could be, in principle, larger than one. Smaller, actually. So it's true that given typical facts about life in the cell, it's true that you expect beta be much less than 1. But we haven't made any assumption.**

**Beta is just there. It could be anything. Right? So yeah, it's possible we've made some other assumption. But what is going on. Yes?**

**AUDIENCE: Is it the concentration is scaled by the amount of necessary--**

**PROFESSOR: Yes, that's right because, remember, you can only choose one unit for time. And we've already chosen that to get this to be just minus m here. But you get to choose what's the unit of concentration for, both, mRNA and for protein. Can somebody remind us what the unit of concentration is for protein? AUDIENCE: The dissociation constant of the protein to the-PROFESSOR: That's right. So it's this dissociation constant. And more generally, it's the protein concentration, which you get half maximal repression. And depending on the detailed models, it could be more complicated. But in this phenomenological realm, if p is equal to 1, you get half repression. And that's our definition for what p equal to 1 means. So we've rescaled out that k. So what we've really done is that there's some unit for the concentration of mRNA that we were free to choose. And it was chosen so that you could just say p minus m. But what that means is that it requires a genius to figure out what m equal to 1 means, right? It doesn't quite require a genius. But what do you guys think it's going to depend on? Yes? AUDIENCE: It's going to depend on this ratio of lifetimes, as well. PROFESSOR: Yes, right. So beta is going to appear in there. So I'll give you a hint, there are three things that determine it. AUDIENCE: Transcription, or the speed of transcription.**

- **PROFESSOR: Translation, yes. So the translation efficiency. So each mRNA, it's going to lead to**

9

**some rate of protein synthesis. So yeah, the translation rate or efficiency is going to enter.**

**There aren't that many other things it could be. But yeah, I mean, this is tricky. And it's OK if you can't just figure it out here because this, I think, is pretty subtle. It turns out it also depends on that k parameter because there's some sense that-- m equal to 1-- what it's saying is that that's the amount of mRNA that you need so that, if the protein concentration where 1, you would not get any change in the protein concentration.**

**And given that now I had to invoke p in there and p is scaled by k, so then k also ends up being relevant for this mRNA. So you can, if you'd like, go ahead and start with a original, reasonable set of equations. And then, get back to this.**

**But I think, once again, this just highlights that these non-dimensional versions of the equations are great. But you have to be careful. You don't know what means what. All right? Are there any questions about what we've said so far?**

**OK. Now what we've done is we have now a protein concentration. We have mRNA concentration. And what I'm going to ask for now is, for these sets of equations, is it mathematically possible that they could, maybe, oscillate? Yes. I mean, we're going to find that the answer is that these actually don't oscillate. But have to actually do the calculation if you want to determine that.**

**You can't just say that it's impossible based on the same argument here. And that's because, if you think about this in the case of there's some mRNA concentration. Some protein concentration. What we want to know is do things oscillate in this space. And they could.**

**I mean, I could certainly draw a curve. It ends up not being true for these particular sets of equations. But you can't a priori, kind of, dismiss the possibility. Yes?**

**AUDIENCE:**

**That's like a differential equation. But if you write down the stochastic model of that, would that--**

10

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md) · [PROFESSOR →](04-professor.md)
