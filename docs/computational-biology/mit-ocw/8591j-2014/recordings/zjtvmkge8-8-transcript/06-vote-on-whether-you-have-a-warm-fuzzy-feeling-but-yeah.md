---
title: vote on whether you have a warm fuzzy feeling. But, yeah?
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/zjtvmkge8-8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# vote on whether you have a warm fuzzy feeling. But, yeah?

**Source:** `recordings/zjtvmkge8-8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: Could you also have just some sort of Z1 required for transcription?**

**PROFESSOR: Ah, yes. So you could have a cascade in that way. And that's a really good question. That would work. But there's a problem, which is that it's super slow. Because there's a characteristic timescale for each of these things, which is this cell generation time. And here when I say you want it after the other, what I'm saying is you might want it a few minutes after the other. So in the context of development, in some cases some things really are very slow. Then that is actually what happens. There's a long cascade of one activating two, activiating--**

**But in the context of this, you really want something that's just delayed by five minutes each, or maybe even just a couple minutes each. And in that case, because really the range over which you can have this sort of delay like this, from the beginning to the end, I mean this is still-- it might be one to two, say cell generations/lifetimes. So you just can't get much more of a dynamic range. Otherwise you're going to be in trouble.**

**Because you can't have this be too close to the top. Otherwise if you're a little bit off, you're off. So we really maybe we should just even say one generation. So that's kind of how much of a delay you might reasonably be able to get from this mechanism. And indeed, and that's as much as you would want for something like this.**

**So this is great. When I first read this, I was like, oh. I was feeling it. Now the question is, after this carbon source, or the need to make our gene or whatnot, after it goes away, then we'll stop making these proteins. And the question is, is this what we call a FIFO queue, or a LIFO queue?**

**LIFO, LIFO? It's been a long time. I have a lot of faces that are like, what are talking about? So this is a First in, first out. Have you guys really not-- you never took any of these computer science classes where they talked about this? And this is a Last in, first out.**

24

**So just to be clear, what this means at the grocery store is that a first in, first out, or a last in, in first out.**

**AUDIENCE: First in, first out.**

**PROFESSOR: It's a first in, first out. Right? If you get in line first, you get out first, hopefully. And when that doesn't happen, you get very annoyed, and so forth. But last in, first out, this is for example what happens in your inbox. So you have a stack of paper. People are giving you things you're supposed to sign or fill out. And the pile kind of comes up, and then you handle things on top of the pile first. So the things that get stuck at the bottom you never get to them. And that's because that's a last in, first out queue.**

**And so different, depending on-- well and in computer science, then they can choose these things. And it's relevant and so forth. But there are many situations where this sort of idea appears. And so the question is, in the single input module, do we have a first in, first out, or a last in, first out queue? I'll give you 15 seconds to think about this. Yeah, question?**

**AUDIENCE: What do you mean by in and out?**

**PROFESSOR: So in and out, what I mean is that the concentration of each of these Z's, these guys they were produced in some order. Right? So first we started producing Z1, then Z2's and then so forth up to Zn. And what I want to know is what order will the concentration kind of go away in?**

**And you might want to look at this figure. Because it's going to be super useful. Any other questions about what I-- all right, so in and out refers to concentrations going up, and then going down.**

**Let's go ahead and vote. Ready, three, two, one. See, I mean people learned what FIFO and LIFO queues were. And now already we can use it. So this is a last in, first out queue. And in general, which kind of queue do we like? We like LIFO queues more. Well, OK, you could argue. But in this actuation would we like a FIFO or LIFO queue? I'll give you 10 seconds. In a biosynthetic pathway, would you want**

25

**a LIFO or a FIFO queue?**

**Yeah, and if you're totally confused by everything I'm saying, you can do the-- flash all the letters, numbers, whatever. All right. Ready, three, two, one. All right. So there's some disagreement we got. But now a majority of people are saying that although the single input module gives us a LIFO queue, what we might really like is a FIFO queue. And can somebody say why that would be?**

**AUDIENCE: We don't want that much intermediates.**

**PROFESSOR: Right. We don't want to pile up those intermediates. So just for the same reason that we wanted to start with Z1, and then get Z2 and so forth. And the reason that was because there's no point in having Z2 until after we have Z1. Because there's nothing for Z2 to do. It would be wasted energy to make it.**

**In the same way, when we're getting rid of these proteins, we would actually like to get rid of them first this one and then later.**

**AUDIENCE: Why? There's no point in having Z2 if you don't have Z1. You technically want to get rid of them in the other way. Because then if the carbon source shows up again, you want to have--**

**PROFESSOR: Well yeah, carbon source showing up again. I think that's a separate argument. So the reason that we-- the statement is really just that if we first get rid of Zn. Then we are just going to pile up molecule n minus 1.**

**AUDIENCE: So the metabolism is down.**

**PROFESSOR: That's right. That's right. So you can just think about the flow of those of the metabolites and the molecules in there. And you kind of want to first get rid of this. So then we stop making this. And then we kind of travel on down. So there are many contexts in which you would perhaps really like to have a FIFO queue. And indeed, one of the things that had been studied previously was the flagellar biosynthesis pathway. So E. coli and many other bacteria, they make these flagella that allows them to swim.**

26

**We're going to talk a lot about that in coming weeks. But in this context what had been found actually is that it is indeed a FIFO queue. So when they first start to make these little flagella, they make. And it's a big complicated, machine. Right? But they make it in the order that it's transported and put in the membrane. But then when it is taken away, when you stop making the flagella components, then it's again in the same order as they were made in, which kind of makes sense.**

**Now the question is, how might we be able to do that. So let me explain it. The basic answer is via an extension of these feed-forward loops. So it's what we call a multioutput feed-forward loop.**

**What we have here is we have some X, and it is going to come to Y. And then Y again is going to do this thing to Z1 and Z2, and all the others. But it's a feedforward loop, because we also have X coming in here as so. And I think that we do want to have these be AND gates. Let me just make sure I'm not-- no here's it's an OR gate.**

**So we're going to assume that all of these inputs are combined via an OR gate. And what we have is we have some K1, K2, et cetera, up to Kn. Then we have another set of K's which are K1 primes, K2 prime, Kn prime. So we have a set of K's corresponding to how X interacts with the promoter at the Z. We have different set of K primes that tells us how Y interacts with the promoter at Z.**

**And the question is how can we get a FIFO order.**

**I'm going to illustrate some options. And you can think about it while I do it.**

**AUDIENCE: Are those associations or dissociations?**

**PROFESSOR: These are dissociation constants. So these are again, this can be thought of as the concentration of the active protein which it starts being effective in sending a signal to Z. Question?**

**AUDIENCE: Would you not like [INAUDIBLE]?**

27

**PROFESSOR:**

**I hope not. Because otherwise I'm going to be in trouble. Maybe for now let's, assume that I've written the right thing. And then we'll find out soon enough. Does everyone understand the question here? I'll just give you another 15 seconds to think about it.**

**All right. Do you need more time? All right. Just a little bit more then.**

**All right. Let's go ahead and give it a go. Ready, three, two, one. OK. So we got a majority B, but some C's. All right. So let's try to figure this out. So what we assume is that X comes and it's going to do this. And then it's going to do this. And we can just have two values for now, K1 and K2. So this is X. Now we're going to have Y.**

**And we can talk about-- this is also X star Y. We'll assume that we always have these things. So Y is also going to come. It'll be activated here at some time, which we don't-- it's going to be delayed by a little bit, right? Maybe.**

**So that's what Y is going to do. Now we want to know about Z1 and Z2, right? Well, the idea here is that it's going to be the K, the regular K1 and K2 that determine the order that it appears. We have an OR gate. Y is going to be delayed. So it's really, the important thing is what the normal K's do in terms of turning on Z's. Yes?**

**And this is especially true because Y is again delayed. Because it has its own threshold for turning on. So since Y is delayed, it won't really have a chance to influence the behavior of the X's. And actually I should have drawn this delayed too, as well.**

**So it's the order of the K's that determine how Z is turned on. But it's the order of the K primes that tell us how the Z's are turned off. And that's again because Y is delayed relative to X. And we have an OR gate.**

**So indeed, in this case, if we have like this, and we want things to be in the opposite order with respect to Y. So if we wanted K1 to be less than K2, then we actually want say Kn to be-- I'm sorry. We want K1 here, and then we want Kn down below.**

**And the heart of this is really because of the fact that X is also regulating Y with**

28

**some other constant Ky. And this is going to tell us how much Y is delayed relative to X. But the heart of this is that since Y is delayed, it's really the dynamics of X at the beginning that tell us how the Z's are turned on. But it's the dynamic of the Y and the K primes, K1 prime, Kn prime, that tell us the order at which those Z's are going to be turned off.**

**So with the proper choice of orderings of K's and K primes is you can then get a FIFO queue. With that I think we should quit. Please read Sunney Xie's paper very carefully, because it's going to be focused on a lot over the next lecture. All right. Have a good weekend.**

29

---

[← PROFESSOR](05-professor.md) · [Up: contents](index.md)
