---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/zjtvmkge8-8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/zjtvmkge8-8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Phosphorylate, yeah. It's all about phosphorylation, yes. Indeed, phosphorylate-- so you need, if you want to be fast, you can't be changing overall protein concentrations. You have to change protein state. Right, and phosphorylation is kind of the classic way of doing that. so I just want to highlight that for speed you need just to do kind of protein networks.**

**So we're not actually going to be reading the chapter analyzing these map kinase cascades, and so forth. But if you're interested in such things, I very much encourage you do so. It's also nice chapters, maybe not as nice as the first four, which is part of why we're not reading them. But it's a very important insight, in the sense that we've spent a lot of time talking about transcription networks, just because there's a lot of, I think, simple, beautiful things that you can say about them. Whereas they are intrinsically limited in terms of speed.**

**So for much of what a cell needs to do, it has to already have the proteins there. And then you can take advantage of these rapid processes. So we talked about Sx rapidly binding, changing the state of X. From the standpoint of transcription networks, we just draw this as a straight line. It's rapid. But what that's saying is that if you just change states of proteins, then you can do a lot of information processing rather rapidly. And you don't have to do just a simple thing of Sx binding X. You can also have proteins regulating each other, and performing logic functions at the protein-only level.**

**What I want to do for the last 20 minutes is say something about temporal programs that can be implemented with sort of larger network motifs. And in particular this is material basically from chapter five of the book, which again we're not to be reading. I think it's again, it's beautiful but it's really simple. So I think that in 20 minutes we can cover it just fine.**

**So for many cases, for example, in the context of metabolic pathways, it might be the case that you have some protein we'll call them Z's. So you'll have some protein Z1 that does something. So that catalyzes-- so we might have some molecule one that's converted into module two, by Z1, converted into molecules three by Z2.**

21

**So many metabolic pathways have this structure where there are a series of enzymes that are doing something to the product of the previous enzyme. Now the question is, let's say that this is some carbon source and we didn't before. But now it's appeared in our environment. So what we would like is we'd like to start digesting that carbon source. Or in the flip side, maybe we have to make some complex molecule or an amino acid or so. And so then what we're doing is we're building something up, coming down.**

**Now in either case, if before you weren't making these Z proteins, but now you want them, a question is, maybe you could just make them all at the same time. But maybe it would be better to make some of them first, and some of them later. What do you think?**

**Let's say for the sake of argument that you would want to have some first, and some later, which ones would you want first?**

**AUDIENCE: The ones that you use first?**

**PROFESSOR: Yeah, the ones you need first. So you'd maybe want to first have Z1, then Z2, et cetera. It's a trivial statement, but you might not actually think about it. And the question is how might we be able to do this.**

**Well there's a very simple thing called a single input module. The idea here is there's some transcription factor X, which actually does this fabulous thing where it creates all these guys. Interestingly, this also often has autoregulation in order to, for example, stabilize the concentration of it.**

**But the reason it's called a single input module is because the network motif is saying not just that X makes many Z's. That actually you can't actually argue that that's a network motif, from the standpoint of a degree preserving network. Because of course, this is just saying well some nodes activate many other nodes. And in a degree preserving network that's always still going to be true, right?**

**But you can say that such a thing is a network motif, when you say that these Z's**

22

**are only regulated by X. So that happens somehow more frequently than what you would expect.**

**Although now that I just said that, I'm a little bit worried that even the degree preserving would-- I think you have to be a little more subtle in defining your null model in that case. But I'll just say that this happens more frequently than you might expect, which is that you have one transcription factor, say activating many, many different proteins. And this makes sense.**

**Because if all these Z's are involved in the same metabolic program, then when you want Z1, you also want Z2, and you also want Z3. So this makes a lot of sense. But what is a little bit less obvious perhaps, is that it's possible to do this such that you first make one, and then you make the other.**

**And the way that you can do this is just by, you have different activation thresholds, K1, K2, et cetera, up to Kn for each of these. So then if X is turned on, so let's say that you first see something. So this you actually have to have X start at 0, and then grow over time. But then if you just have different thresholds, the question is where should I draw K1, and where should I draw-- Do I draw K1 the low position or the high position?**

**Low. Perfect. All right. So we say K1. Here's K2. Here is Kn. And then there might be some others in between. So the idea is that X grows over time. Then you first activate expression of gene one, and then gene two, and so forth. And then the proteins will naturally appear in the proper order. And there's actually beautiful data in chapter five illustrating this in the context of our gene biosynthesis.**

**So it's quite neat to see that it's not just-- of course, it's easy to think up this idea. And say, oh yeah. Maybe the cell might want to do this. But then it's quite cool when you see that actually in some cases, the cell actually really does do this. And you can actually see that they're expressed sequentially, in the same order as they appear in the biosynthetic pathway.**

**So this kind of gives you a warm, fuzzy feeling inside. I'm not going to make you**

23

---

[← AUDIENCE](04-audience.md) · [Up: contents](index.md) · [vote on whether you have a warm fuzzy feeling. But, yeah? →](06-vote-on-whether-you-have-a-warm-fuzzy-feeling-but-yeah.md)
