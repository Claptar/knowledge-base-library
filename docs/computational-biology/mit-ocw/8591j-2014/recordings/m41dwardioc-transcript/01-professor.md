---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/m41dwardioc-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/m41dwardioc-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Today, what we want to do is talk about something at a much higher scale than what we've thought about through most of this semester. And that's probably by design. Over the course of the semester, we started with kind of enzyme kinetics or molecular binding kind of events, and we slowly built our way up the larger and larger scales.**

**Now there's always this question about whether we're claiming that we really understand how the higher levels of organization result from the lower level interactions. And I'd say, we definitely don't understand all of it. So you shouldn't come away with that as the notion.**

**But at least one thing that I think is fascinating about this area of systems biology is that much of the framework that we use to understand, let's say, molecular scale interactions or stochastic gene expression, so these dynamics at the smaller scale, much of those ideas and such certainly transport up to these higher scales or translate up to the higher scales, where, in this case, we're using kind of master equation type formulas to try to understand relative species abundance.**

**And so I think part of what I like about this topic of neutral theory versus niche theory and so forth in ecology is that you can just see how very, very similar ideas, that we applied for studying stochastic gene expression, can also be used to try to understand why it is that some species are more common than others when you go and you count them, in this case, on an island in Panama.**

**Now, the subject is, by its nature, less experimentally focused than much of what we've done over the course the semester. And this is really a topic the tends to be a combination of mathematical theory with kind of careful counting of species in some**

1

**different areas and trying to understand what that means.**

**But it's an area that there have been a number of physicists involved in over the last 10 years. And I think that it's fascinating, because it does get to the heart of what we are looking for from a theory, what kind of evidence do we use to support a theory or to refute it.**

**So I think there are a lot of very basic issues about science that come up when we start thinking about this question of neutral theory in ecology. And since it's, for many of us, a totally new area that we don't know very much about, you can come to it with maybe fresh eyes. And you don't have the same preconceptions that you would have for many other models that you might be more familiar with in the context of molecular cell biology.**

**So the basic question that we're going to try to talk about today is just the question of why is it that, when you look out at the world, you see that there are some species that seem to be abundant and some that seem to be rare?**

**Are there other patterns that are somehow universal? And what kind of sort of lower scale processes might lead to the patterns that we observe?**

**And I think that this paper that we read is-- I mean, it's not that it's. Well, can somebody say what the actual scientific contribution of this paper was? Yes?**

**AUDIENCE: They did a calculation.**

**PROFESSOR: They did a calculation. But it's a little bit more specific than that. What is it?**

**AUDIENCE: They came up with the closed form equation?**

**PROFESSOR: That's right. Basically, there was a model of this neutral theory in ecology that we're going to explain or try to understand. You can simulate the model, but then there are possible issues associated with convergence or something of those. Although it's hard to believe that that's really such a concern. But you can simulate that model.**

2

**What they did is they just showed that you could get an analytic-y kind of expression for it. It's not a super analytic expression, but, at least, it's not a straight up simulation. You kind of numerically do something, integrate something, as compared to doing the stochastic simulation.**

**So it's not that that, in and of itself, is what you feel like-- it's not what we necessarily care so much about. But I think that it's still just a nice, short description of the model and the assumptions that go into it. And you get a little bit of a window into the debate that's going on between these two communities of kind of the neutral theory guys and the niche theory community.**

**So there's only one figure in this paper. And it's an example of the kind of data that we want to try to understand. So there's a particular pattern in terms of the relative species abundance. And we want to understand what kind of models might lead to that observed pattern.**

**But given that there's just one figure in the paper, we have to make sure that we understand exactly what is being plotted. And what I've found from experience-and, actually, even the answer to the email question that was sent out, I think, was incorrect on one of these things. So we'll talk about that some more. So beware. We'll figure it out.**

**But I think it's actually surprisingly tricky to understand what this figure is saying. But first of all, can somebody describe not what the figure is saying but just what the data is supposed to be?**

**Where do they get the data? Anything that's useful?**

**AUDIENCE: They were on an island ecosystem.**

**PROFESSOR: There's an island. It's called BCI, Barro Colorado Island.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: So it's a 50 hectare plot. Does anybody know what a hectare is?**

3

**AUDIENCE: It's a lot more than a square meter. PROFESSOR: It's a lot more than a square meter, yes, indeed. Yeah. Is this an English unit of measure? This is the kind of thing that I have to Google. But it's one hectare is equal to 10 to the 4 meters squared. That's a good thing to memorize. I AUDIENCE: Exactly or approximate? PROFESSOR: I think it's exact. I think I think it's an exact. AUDIENCE: Then it's a metric unit. PROFESSOR: Yeah, so apparently it is a metric unit. So the idea is that if you take a 100 meters by 100 meters, this is a hectare. And there's 50 of them. It's about like a half a square kilometer to give you a sense of what we're talking about. And what do they do on this plot? AUDIENCE: They count a certain number as canopy trees. So the trees that are, like, really big. PROFESSOR: And how do they decide which trees to count? Did they count every tree? AUDIENCE: No, just the ones that like formed the top layer. PROFESSOR: I think that the way that they decide-- OK. Does anybody remember how many trees were counted? AUDIENCE: [INAUDIBLE]. PROFESSOR: So there are 21,457 trees in this 50 hectare plot. They identify the species for each one of these 21,000 trees. And they assign them. And they found that there were 225 distinct species. So this is really quite an amazing data set. Because I can tell you that I would not be able to do this. This was highly skilled biologists that can distinguish 225. If they can identify these 225, that means they have to be able to identify other ones as well. And they did it for 20,000 trees.**

4

**And indeed, Barro Colorado Island is one of the major Smithsonian research institutes, where they've been tracking. They do this like every five years or so, where they do a census, where they count all of the trees. And they're also tracking many other-- it's not just trees. They're doing everything there.**

**AUDIENCE: Is there only plants? PROFESSOR: What's that? AUDIENCE: Is it only plants? PROFESSOR: No. So actually, I visited BCI, and it seemed like they were studying all sorts of things. And there were nice looking birds there. AUDIENCE: No, I mean in this census. PROFESSOR: In this census, it's only trees. And the way that they decide which of the trees to do, it's the ones that are more than 10 centimeters DBH. Anybody can guess what DBH might mean?**

**It's actually diameter at breast height. So what they do is they walk up to the tree with a ruler, and then, if it's larger than 10 centimeters, then they count it. You need to have some threshold at the lower end, otherwise you're in trouble, right? And there were plenty of trees that satisfied this requirement here.**

**Then what they do, for all of these trees, it's assigned to some species. The basic goal of this branch of biology or ecology is to try to understand the pattern, from this sort of data, where it comes from. Or first describe it, and then once you have a description of it, then you can try to understand what microscale processes might lead to the pattern.**

**And the pattern is what's plotted in figure 1. It's the only figure in the paper. I have reconstructed a rough version of it, here, for you on the board. But if you want a more accurate version, you can look at your paper.**

**Now, we want to make sure that we understand what the figure is saying. So we will**

5

**ask the following question. What is the most common number of individuals for a species in this data set? The most common/frequent number of individuals for a species to have in this data set.**

**Now, it's maybe worth just saying something a little bit more. So you notice that they were not trying to count the total number of species, altogether. And in general, all of this field of relative species abundance, to try to understand them, what you do is typically take one trophic level.**

**So some of the classic studies were of beetles in the Thames River. The idea is that it's some set of species that you think are going to be interacting, maybe competing, with each other, in some way, in the sense that they're maybe eating related things and being eaten by related things.**

**And so in this case, these are the trees in Barro Colorado Island. And you can imagine that this is useful. The fact that it's trees instead of something else means that you can actually track the individuals over time. And when you go to the island what you see is that all the trees, they're wrapped by some tag. And presumably, they have some system to tell you which species that is so that they keep records of everything.**

**But the question is, what's the most common number of individuals for species in the data set? Do you understand what I'm trying to ask? And we're going do approximate, so we'll say. Or this, can't determine.**

**We want to know, what is the mode of this distribution of the number of individuals for each of these species? Do you understand the question? I'm going to give you 20 seconds to look at this.**

**AUDIENCE: Should we just hold a blank piece of paper?**

**PROFESSOR: Oh, we don't have our-- ah.**

**AUDIENCE: [INAUDIBLE]?**

**PROFESSOR: You know, the TA always lets me down. All right, yeah. So you can do A, B, C, D, E.**

6

---

[Up: contents](index.md) · [Are we ready? →](02-are-we-ready.md)
