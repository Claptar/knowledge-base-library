---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/klrpm-beeoi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/klrpm-beeoi-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Yeah, this is amazing. So you use lice. There have been a number of studies doing this, and apparently, there was a researcher in Germany, who was at the Max Planck Institute for genomics or something, and his son came home with a note saying-- and actually this happened to me recently, they got an email that there's a lice outbreak to stay out of preschool, so watch out when you're going by the play area-- so he got this note back from his son's preschool that said, oh yeah, there's a lice outbreak, so this is what you have to watch out for.**

**But it said, oh, there's a different species of lice that inhabits our clothing as our hair. All right, so I'd say this is one of those things that you could just read that and say, oh, well whatever. Or if you're a geneticist you read that and say, oh, I can use this to figure out when humans started wearing clothes, right? Because presumably the species that specializes in living in our clothing was probably not there or had not yet speciated before we had clothes.**

**Course, you can imagine ways that this could fail, but it's a neat hypothesis. So then you can go and you can basically sequence the species of lice that lives in our clothing as compared to the kind that lives in our hair, and you can ask, how many neutral mutations accumulated along these different lineages.**

**Now, you can imagine that based on, since we just did this very nice study, we know that it should be more than 30,000 years and it should be less than 7 million, probably, hopefully. Although, it's always possible that our ancestral state was wearing clothes and that the chimpanzees stopped wearing clothes. But we'd be surprised if that were the case. All right, so this is basically just asking about head lice versus clothing lice. And the original study by this researcher Max Planck estimated 70,000 years, but then just a couple years ago there was another publication from a professor at the University of Florida that estimated 170,000.**

**So there still is a fair range, but I guess the most recent estimate we'd have to say is 170,000. Which is neat. I don't know-- it's not that it changes, necessarily, how I go about my daily life, but I really love this idea that it's a very basic question that your**

23

**toddler son might ask you-- something that you'd think that might be totally unknowable in the sense that we would never have any way of getting any estimate all, right? But using some clever theoretical ideas together with data on this accumulation of neutral mutations allows one to at least make a ballpark estimate of something that there's no physical record of except in the DNA of our louses. Is that a word?**

**AUDIENCE: It's lice.**

**PROFESSOR: It's just lice? All right. Are there any questions about this point? So this is all neutral mutation, but of course we'd like to move beyond these neutral mutations to try to understand how non-neutral mutations spread. I'm not going to do the derivation, because the derivation is in your book, and you just read about it. But I do want to just make sure that we understand what this equation is telling us.**

**So first of all we're going to assume that A has some relative fitness r. So r is defined as basically the relative fitness of of A, or the fitness of A divided by the fitness of B. So r is greater than 1 means that A is advantageous. Less than 1 means it's deleterious. And what we're told is that x sub i, which is the probability that A fixes, is equal to this expression. If A fixes, given i A individuals and N minus i B individuals.**

**AUDIENCE: So I guess that this assumes that they die at the same rate [INAUDIBLE].**

**PROFESSOR: That's right. That's right. The assumption is that we're placement is unbiased, purely random, and it's only birth that is different by a factor of r. And so I think that this is, on one level, wonderful. It's kind of a simple expression describing a lot of information of the dynamics of the stochastic process. On another level, the problem is that you look at it, and I think it's easy to have like absolutely zero intuition for what this thing does. So what I always like to do when a student comes to my office and says, oh I derived something great for our project. You take a few limits to get a sense of what's going on with it. At half-time you find that it's not true. But at least it's a way of developing intuition for what's happening.**

24

**All right, so what are limits that this thing should behave--**

- **AUDIENCE: It should be 0 if there's no A. PROFESSOR: Right, so x of 0 should be equal to 0, is what you're saying. If you have 0 individuals, you should have 0 probability of fixing, independent of your fitness, right? All right, that sounds like a reasonable thing to check. And does it work? So r to the 0 is equal to 1. So that's 1, so it's 1 minus 1-- 0. Yep. Yes?**

- **AUDIENCE: r goes to infinity independently of what you start with in step zero, then you expect A to fix?**

- **PROFESSOR: That's right. So the limit of xi for any i other than 0-- as r goes to infinity, this should be equal to 1. All right, so let's see. If r goes to infinity, you get 0-- this is also 0-- 1 divided by 1 is equal to 1-- all right. Did everybody agree with that? And that makes sense just that if A is just super, super fit, then it should fix. And of course, what's tricky here is that r has to be surprisingly large before this thing ends up being true. This limit is great, and it's correct and true, but it's also a little bit dangerous because-- well we'll see that even things that you think of as being very beneficial mutations typically do not fix. So this is the danger, but at least the limit is still true. Any other limits that we think ought to happen?**

**AUDIENCE: If an i goes to N? PROFESSOR: An i goes to N? OK, right. This is the opposite of this one. This is just saying that if you already have fixed then you fixed. Indeed, if i is equal to N-- that works. Any other limits that you believe should be true, think should be true? AUDIENCE: The one we already checked for r equals one? PROFESSOR: Yes. Indeed. So if it's neutral-- so the limit as r goes to 1 of xi should be equal to what? AUDIENCE: i/N.**

25

**PROFESSOR: Should be equal to i/N. So this one is a little bit less obvious, because if you set r equal to 1, does this mean that it's equal to 0? And what's the problem? [INTERPOSING VOICES] PROFESSOR: Well, OK, but even that statement's not true. It's not even necessarily close to 0. AUDIENCE: [INAUDIBLE] L'Hopitals? PROFESSOR: Right. This is the L'Hopitals. There was another context already were L'Hopitals came up, right? Maybe? OK, so the problem is that if you set r equal to 1 here, then you get 0. So then you think, oh, the answer is 0. But you have to be more careful than that, because this also is equal to 0. And so L'Hopital's-- L-H- -- is it above the H? AUDIENCE: No, that looks right. PROFESSOR: Is it good? AUDIENCE: Yes. PROFESSOR: All right. You're French, right? I mean, sort of. He's from Quebec, so I don't know what that question-- how it's interpreted.**

**So this [INAUDIBLE] looks all right. See, what you just have to do is then you take the derivative with respect to r for both the numerator and the denominator, and then you see what ha-- but you take the limit again. And sometimes you have to apply L'Hopital's rule multiple times, right? So what we write here is this is the limit as r goes to 1, and we take the derivative of the numerator respect to r. So we get out an i, 1 over r to the i plus 1, maybe? And here we get out an N.**

**All right, so we took the derivatives back to r here. But we left it as a limit because we might need to apply it again, right? Just because after you take the derivative you're not guaranteed that it's going to work out fine, but in this case it does. Because already, this limit, we're allowed to just set equal to 1 because nothing blows up. So this is indeed equal to i/N. N. And the important point here is that it's**

26

**not necessarily approximately equal to 0. It could be anywhere between 0 and 1 depending what i and N are.**

**PROFESSOR:**

**So that means that this expression here captures the dynamics, actually, for all i, r, N within the Moran process. This thing is simply just true in this model. There are no approximations yet. There is, however, one approximation that is very useful to make, which is the approximation of what happens when r is approximately 1.**

**In particular what we're going to ask is, if we define something called a selection coefficient, that is 1 plus s, the idea here is that in many cases-- well for Thursday we're going to read a paper that I think this is quite interesting. And where they were analyzing the appearance of these mutations that would allow bacteria to survive in some environment to do better.**

**And typical selection coefficients here are kind of 1% to 3%. So the mutations that appear and that allow one of these cells to do better in this new environment, convert an advantage that was on the order of 1% or 2%, or so. Which means that s here would be like 0.01, 0.02. Which means that for basically all the situations that you see in the laboratory and so forth, what you really want to know is what happens for small s. So for s, much less than 1. So where r is approximately equal to 1.**

**And in this case, we can say xi, well-- and we actually are going to want to ask about x sub 1. So that's a 1 now. And the reason for that is that we want to know, are there some rate that new mutations will appear in the population? When they appear they'll be present in a single individual, and we want to know what is the probability that one individual-- let's say has a beneficial mutation, well, the probability it'll fix-- so we want to know is for s, much less than 1, but larger than 0.**

**So far, it's a beneficial mutation of modest effect. What's the probability that it will fix? Well the idea here is that r to the N is going to be much larger than 1, because N is often a big population.**

**Now in that situation, this is just approximately equal to 1 over r. And r, we've**

27

**already decided it can be expressed as 1 plus the selection coefficient. Now this is something that you want to be able to simplify in your sleep. 1 divided by 1 plus s is approximately equal to 1 minus 1 minus s. And this is indeed approximately equal to s.**

**This is saying that in the Moran process, if a beneficial mutation appears in the population with selection code coefficient s, that might be 1% to 3%, then it has a 1% to 3% probability of surviving. Because this is the probability of fixing, but in this situation fixation and survival are the same thing, because we're just considering this one mutation. So it's the only thing that we're considering is the fate of this one mutation of the population.**

**We're going to assume for now that you can't get new mutations in the population to compete with. And then either you go extinct, or you take over the population. And what's surprising here is that even if it's a fact that you think it was big, like 3%, 4%. I would love to get such a mutation. But still, in a population in the Moran process, or really in any other model like this, it will typically go extinct.**

**Now, it's worth saying that depending upon the model that you're using, you'll get different numbers in here. In this case, the probability of fixation or survival is 1 times s. But in some other models and it depends on the branching process. It could be two times s. But it's something of order unity times s.**

**AUDIENCE: And so we say that if s is equal to 0, then x of 1 should be--**

---

[← thing.](05-thing.md) · [Up: contents](index.md) · [[INTERPOSING VOICES] →](07-interposing-voices.md)
