---
title: questions?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/c95294-vvqy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# questions?

**Source:** `recordings/c95294-vvqy-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**All right. So we're going to take a slight turn here in the course lecture and move away from a purely computational approach and actually look at how interaction measurements are made. One of the big changes of the last decade or so is that we've gone from an era when interactions were measured pairwise to interactions being measured in bulk. So through high throughput measurements. And we'll see that that leads us to some statistical problems which eventually bring us back to some computational issues as well.**

**So if you want to measure all the proteins that interact in an organism, turns out to be, obviously, very difficult. One big advance that's helped with this is the idea of tagging proteins and using mass spectrometry to figure out what they interact with. So in these two sets of papers, which were some of the early ones being done in yeast, they took one protein at a time and attached a tag to it. And I'll talk about exactly what those tags are, but those are labels that allow you to attach it to a solid support.**

**And then by attaching to a solid support, you could then purify any proteins that stuck to protein one here. And then after you purify them, you can run them out on a gel, cut them out, and figure out what the identity of those interacting proteins were by mass spec. So this sounds very labor intensive, but it's still a lot faster than anything that came before it. And with this approach, they were able to go through entire genomes, proteomes I should say, and figure out all the interacting partners for very, very large fractions of all the proteins there.**

**So with this approach, what kinds of proteins do you think are likely to be false positives? Any thoughts? Yes.**

**AUDIENCE: Proteins stuck on the column that has nothing to do with interaction [INAUDIBLE].**

**PROFESSOR: Exactly. So one thing that can be quite problematic are proteins that stick to the column regardless of which protein you put there. And we'll see an approach to getting rid of that. Other kinds of problems? A variant of that. Thoughts?**

11

**What about proteins that tend to stick to other proteins non-specifically, right? Those are going to be quite problematic too. And what are the likely false negatives in an approach like this? The proteins that really do interact with the blue one but aren't picked up. Yes. AUDIENCE: Weak interaction partners [INAUDIBLE] PROFESSOR: Weak interaction partners, things, particularly with short half lives. Because you do a lot of washing, so it's going to be dependent on half-life. Very good. What else? Yeah. AUDIENCE: Maybe something that interacts in tag region? PROFESSOR: Something interacts in the tag region, right. So something interacts right around here would be lost because this would sterically interfere. Very good. Anything else? What about the concentration of proteins. How does that influence whether they show up here? All right. So if I have a very high concentration protein, it may interact even though naturally it doesn't. They never see each other. They're in different compartments. But when [INAUDIBLE] and do this. But low abundance proteins are going to be quite problematic because there'll be very little of them in these complexes compared to the high abundance proteins. It won't be detected by this method. They will never get to the mass spec, and so on. So we've got both false positives and false negatives in these approaches.**

**Now, one of the things that came up was proteins that stick non-specifically to the column. And there was a clever approach in one of these early papers that got picked up to avoid that. And this is called tandem affinity purification, or TAP-tags. And the idea is the following.**

**We have some gene. And we use homologous recombination-- this was done in yeast where this is easy-- to insert this sequence, which codes for the following. A piece of protein of no particular function, as far as anyone knows, a spacer, followed by this calmodulin-binding protein, followed by a protease recognition site, and then**

12

**by protein A.**

**So once this protein gets expressed-- and it gets expressed in it's native levels because you're inserting this into the genome. So it's not on an exogenous promoter. It's in its normal position. Whatever that protein was, then has it as C terminus all these pieces. So how does that help?**

**In the purification, we start with something, IgG IGG, that binds to protein A. So now that's what attaches us to the solid support. And attached to the solid support will be all those things that are nonspecific binders.**

**And so if I have some nonspecific binder that just likes my solid support, it'll be here. Nonspecific. And if I just acid washed everything off the column and ran my gels with that, or boiled it off in SDS, I would get the nonspecific protein too. But what they do instead is they instead cleave here with a very specific protease that recognizes this site. It's called a tobacco etch virus protease. It has a very long recognition sequence. You can make sure it doesn't cut anywhere in any other protein.**

**And so now, instead of alluding non-specifically with acid or detergent, you allude specifically with TEV, and then this part of the protein will fall off. And then you do a second purification that relies on this piece of the protein. So you pull out only the things that you want that have the CBP, the calmodulin binding protein, by having different kind of solid support that has calmodulin attached to it.**

**And so through this process, you can get rid of a lot of nonspecific binders. It doesn't help you with the false negatives, right? You've made the wash conditions even harsher so you're going to lose more proteins. But you'll pick up fewer false positives.**

**And then finally, the last purification procedure actually uses EGTA, which is a chelating agent. So this interaction between CBP and calmodulin depends on calcium. EGTA sucks the calcium out of that interaction. And so it's, again, a very specific way of alluding rather nonspecific one, like heat, salt, acid, or detergent.**

13

**So this has been one technology, affinity purification followed by mass spec, that's given us a lot of information on protein-protein interactions. And a computing technology that's also contributed quite a lot is called yeast two-hybrid.**

**So in this approach, you have a reporter gene that normally is not going to be transcribed. It has at a design DNA binding site, a DNA binding protein, and your bait protein. And you want to figure out every protein that can interact with this prey. So the prey now is attached to an activation domain.**

**If these two proteins don't interact, the activation domain never gets recruited to this reporter, there's no transcription. But if the green protein and the blue protein interact, then the activation domain is going to be recruited to this promoter and it's going to turn on transcription, and then you'll get a signal.**

**So what are some of the advantages of this approach? It doesn't require you to purify anything. So it should be much more sensitive to low abundance proteins. So that's definitely an advantage.**

**It'll pick up a lot of those transient interactions. You may not get continuous activation, but you'll get transient activation. And if you've set the conditions up properly, you can pick up the transient activation.**

**But it has its own biases, so none of these techniques are going to be perfect. It's going to be biased against proteins that don't express well. This is, as the name implies, typically done in yeast. So if you have human proteins and you express them in yeast, or plant proteins that you express in yeast, there could be some proteins that just will not express well in that organism.**

**What else can be a problem? Some proteins don't do well in the nucleus, right? So if you're interested in interactions with membrane proteins, it's going to be very hard to get them to express in the nucleus, and therefore, you'll never pick up those interactions.**

**OK. So we've got these two different technologies-- the affinity capture mass spec**

14

---

[← C95294 vvqy transcript Part 02 —](02-c95294-vvqy-transcript-part-02.md) · [Up: contents](index.md) · [and the two-hybrid. Questions on those technologies? Yes. →](04-and-the-two-hybrid-questions-on-those-technologies-yes.md)
