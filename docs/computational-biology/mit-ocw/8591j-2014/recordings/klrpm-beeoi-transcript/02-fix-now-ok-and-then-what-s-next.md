---
title: fix. Now, OK, and then what's next?
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/klrpm-beeoi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# fix. Now, OK, and then what's next?

**Source:** `recordings/klrpm-beeoi-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- **AUDIENCE: So there are i individuals that are type A, so the probability that this one individual [INAUDIBLE] will fix.**

- **PROFESSOR: And then there is one ingredient in that argument that you didn't say, but I'm sure is in your mind. Which is, how is it that the probability-- so among these N individuals, right? One of them will eventually fix. And what's the probability that each one will be the lucky ancestor for all of the population?**

**AUDIENCE: So it's equally distributed.**

- **PROFESSOR: Yeah. It's just 1 over N, right? So the idea is there are N individuals in the population, they're all identical. We know that eventually one of them is going to take over the population, just due to random stochastic dynamics. What that means is that each individual has a probability of 1 over N of taking over the population. And this is very important. So each individual has a 1 over N probability of fixing. And that's assuming that everybody in the population has the same fitness. And that's just by symmetry. But then of course, you can also say, well, you know if the probability of each individual is 1 over N, then the probability that one of these i individuals takes over is going to be i over N.**

- **AUDIENCE: The generalization [INAUDIBLE] reproducing organisms is that [INAUDIBLE] organisms every individual is probably the ancestor of [INAUDIBLE]. Like ever individual takes [INAUDIBLE].**

**PROFESSOR: OK, all right. OK, now you want to allow for recombination. Is that-AUDIENCE: I mean, yeah.**

**PROFESSOR: Right, OK. So yes, there are several important aspects of sex. But one of the major ones is the recombination. And so if you have enough recombination, then everybody will contribute-- well, everybody. Then there will be-- then many, many individuals will contribute to the [? lineage. ?]**

11

**What you often will hear people talk about is the ancestral Adam and the ancestral Eve. And that-- and what are people referring to about that? Yes, in the back. AUDIENCE: An individual with the-- an individual that [INAUDIBLE] early on [INAUDIBLE]. PROFESSOR: Yes, right. So there's this idea-- OK, so I don't want to get too much into the sexual-sexually reproducing populations because that's covered more in other classes. And it's a totally different models you would typically use.**

**But I think the simplest way to think about some of this is just that there's some part the genome that does not have recombination in the same way. So it's simpler. What part of the genome is that in us?**

**AUDIENCE: Y chromosome.**

**PROFESSOR: Right. So the Y chromosome, and that means that in principle you could track the dynamics along the male lineages. So there are all these studies, whatever, Genghis Khan, maybe lots of us are descendants of. Right, because he had lots of wives, or something like that. So his Y chromosome supposedly occupies a non negligible fraction of the population.**

**OK, so but then what about-- what's the other, yeah, so on the female side? What would be the equivalent?**

**AUDIENCE: Mitochondria.**

**PROFESSOR: Mitochondria. Right. So in principle, you can-- so I think for an awful lot of these studies you can-- the genetics are much simpler for those two lineages. Because you don't have the recombination. AUDIENCE: So why is the mitochondria-- I mean, you say that it's the most obvious thing. PROFESSOR: OK, yeah-AUDIENCE: I've never heard that. PROFESSOR: Yeah, OK, OK, right. So--**

12

**AUDIENCE: I mean, we don't have to--**

**PROFESSOR: OK, well, you're right. So basically the situation is that we have cells, and most of the genome is in the nucleus. But then, but the mitochondria actually have their own mitochondrial DNA. And then the issue is, OK, well, what happens? You know, here's the birds and the bees talk for you guys, all right? Right, so the sperm comes, fertilizes the egg. And the vast majority of the mitochondria come from, or were in the egg, as compared to the mitochondria from the sperm.**

**And I don't-- does anybody know if any of the sperm mitochondria actually contribute? Are they selectively-- does something happen to them?**

**AUDIENCE: They don't have any.**

**PROFESSOR: Oh, they just don't have any? All right, whoo. All right, well, OK. OK, well that solves that problem. OK.**

**AUDIENCE: Wait.**

**PROFESSOR: Is that not your-- all right, well-- all right, this is the kind of thing that somebody could maybe Wikipedia this while we're going. But that's the basic idea, though. All right, does anybody have any questions about these two statements? Probability that A fixes, probability that B fixes? Incidentally, you should be able to draw-- these are random. From this point moving forward, am I more likely-- OK, so given where i is here, am I more likely to fix B or A? Ready, three, two, one.**

- **AUDIENCE: B.**

**PROFESSOR: B. Does that mean that my first step is more likely to be in the direction of B than in A? Yes or no. Ready, three, two, one.**

**AUDIENCE: No.**

13

**PROFESSOR: No. OK, so this is a random lock. All right, it doesn't always take steps, but sometimes it goes up and then down. All right, so it's going to- now I'm-- you know, I understand it's not to-- you know, whatever. OK.**

**But the idea is that once it hits 0 or 1 here in terms of the fraction, then you stay where you are. These are absorbing boundaries. But every now and then it's going to hit there.**

**Before we get going too much more in this, I want to mention something about time in this model. Because time is a little bit of a funny entity here. So here's the question. How long-- and long is funny-- but how long does one-- I don't know. Do we want to call this an iteration or a cycle? On iteration of the model?**

**And what I mean by that is that in units of something that would be like real time, you know what I mean? Is it a second, a generation time-- so this would be like a cell generation time. Or don't know, something.**

**OK, I'll give you 15 seconds. Can you guys all read this? Seconds, generation time, N times generation time, or 1 over N times generation time.**

**AUDIENCE: What do we want [INAUDIBLE]?**

**PROFESSOR: Yeah, well let's say that I-- let's just imagine that I was using this to model the dynamics of the neutral drift dynamics of some bacteria in my test tube in the lab. Right, so let's say I have one of these tubridostats. So I-- question is, how long does this last in the units of-- right. Or equivalent, how many iterations do I have to go to get through some period of time in the lab.**

**So I grow my bacteria in my turbidostat, say. And I do it for 100 hours. Now your advisor says, OK, go do a simulation, so you get something. And your advisor goes, all right, do a simulation, use the Moran process. You guys are going to be doing this, so this is not entirely hypothetical.**

**But right, so your advisor says, go simulate this process. Right? So the question is, how many iterations do you have to do to make it equivalent to that 100 hours that**

14

**you did in the lab? How do you-- how do you make a connection between a model, well, this model, and something that actually happens in your laboratory? Ready? Three, two, one. OK, all right, so we got a majority of the group agreeing that it's going to be D. Can somebody just say why this is? AUDIENCE: [INAUDIBLE] one cell [INAUDIBLE].**

**PROFESSOR: Right, so each iteration, there's only one cell out of N that actually divide, right? And that means that if you want, like for example, everybody to have had a chance, roughly, to divide, you need to go N iterations. And it also makes sense, if you ask-let's imagine you have a test tube with a million bacteria. Now it's going to take some time before one of them divides. Now the question is, if you had 10 million bacteria in your test tube, you have to wait 1/10 as long before the first one divides. So the amount of real time that elapses in each one of these iterations goes as 1 over N, where N is the population size. So I got some unhappy looks, so that means that I expect an unhappy question. Maybe. OK, well, if you don't ask the question, then in the teaching evaluations you're not allowed to write that you did not like the explanation of time in the Moran process. AUDIENCE: [INAUDIBLE] [LAUGHTER] PROFESSOR: Well, that worked. A little bit too well. AUDIENCE: [INAUDIBLE] question, just a clarification. PROFESSOR: Yeah. AUDIENCE: So an iteration is when one cell or thing increases? PROFESSOR: Right. OK, an iteration in this model is both of these things. So it's a birth, and a death, or a replacement. So it's one duration here, another-- so each iteration involves one birth and one replacement. Yeah.**

15

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
