---
title: '[LAUGHTER]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/zjtvmkge8-8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [LAUGHTER]

**Source:** `recordings/zjtvmkge8-8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So we're going to preserve not only the mean of the incoming and outgoing edges, but also the actual degree distribution. In a very concrete way, we can actually just say that each node actually does maintain the exact same number of edges. So in particular, here we say that all nodes maintain their degree distribution or maintain**

7

**number of incoming and outgoing.**

**And there was a simple algorithm for doing that. If you recall, what you can do is you can just take two edges randomly and just swap the locations. And you do that many, many times, and you end up maintaining both the incoming and the outgoing number of edges. And if you do this analysis on a degree-preserving random network, you get a seven plus or minus five. So this makes a big difference.**

**So if, for example, the experimentally-observed network had one of these feedforward loops, then what you'd see is that actually, comparing to the Erdos-Renyi, you would have said, oh well that that's a network motif. Whereas comparing to this degree-preserving, you would have said it's not. Yes.**

**AUDIENCE: I don't know why I haven't asked this before, but is it also true that this degreepreserving thing is roughly Poisson in terms of-- I mean, should we expect deviations always?**

**PROFESSOR: Yeah, it's close. But I think it ends up not being quite. But it is close.**

**AUDIENCE: So is the entire transcription network for E. coli?**

**PROFESSOR: So I think that it is, certainly now-- well you'll notice that here there are 400 genes. How many genes does E. coli have, anybody? A few thousand. So the network that we analyzed in that original paper was not the full transcription network of E. coli. AUDIENCE: How do people-- how do figure out the whole transcription network? It actually sounds pretty hard.**

**PROFESSOR: Well figuring out and any part of it is actually hard in some ways. The way that they actually annotated this particular network, I'm not sure. I mean what kind of date would you need in order to get at this? Does anybody have any-- I mean, if I asked you to do this in your lab, what would you do?**

**So you could actually use a computational program to try to actually estimate binding affinities of these proteins to the DNA. And these days actually**

8

**experimentally you can actually just measure for the entire proteome basically, just the affinity of binding to different promoters. Of course that doesn't prove that it's going to regulate expression, but that at least points you in the right direction.**

**Then you could actually, if you want, you could just experimentally go and put this protein on an inducible promoter and just see if it does regulate expression. At this stage, for something like E. coli, we have collections of strains where every gene has been removed. We have collections where every gene has been tagged. And of course, when I say every, this means that it was tried to make it for every and then of course if it's an essential gene you can't remove it. And**

**In some cases it's hard to attack a fluorescent protein, and so forth. But there are collections both E. coli and for budding yeast where this has been done. Any other questions? Can somebody say why it might be-- is this a surprise that this number is larger than this number? And in particular, would the degree-preserving random network have a larger expectation for every subgraph? No.**

**But in particular, for the feed-forward loop, can hear somebody say why we should have expected that the degree-preserving would have a larger number than the-yeah.**

**AUDIENCE: All the measures have one outgoing edge, and so [INAUDIBLE] distribution towards lower numbers of outgoing edges. And so you would expect more from forward loops.**

**PROFESSOR: I think that the explanation had the right flavor, but I think there were two inversions in there that-- like a not and a not turned into a-- Incidentally, this is a non-sequitur, but this happened to me once. The airport in San Francisco-- I was going to the airport, I got the wrong airline in my head. So I thought I was on the wrong airline, so I went to the wrong terminal, but then it turned out that I also was wrong about which airline was in which terminal, so then I was actually the right terminal even though I had just made two mistakes.**

**But you can't account on this happening all the time. But I think there were two**

9

**things that were mixed up in that explanation. Yeah. AUDIENCE: For a transcription factor, it has many outgoing-- outcoming edges. And you just have to-PROFESSOR: So in the actual network, There are some nodes with many outgoing edges. And then-AUDIENCE: You just need to have another line between. PROFESSOR: That's right. You somehow just have to add one more edge. Because x actually has two outgoing edges. So there's a sense of the feed-forward loop here-- you can think about x being some transcription factor. And then what you need is just to get- x might have many, many outgoing edges. And so to get a feed-forward loop, what you need is you need for one of those genes that are targeted to just target another one that's in that network. So if you have x that's regulating one00, then that actually that presents many opportunities to generate feed-forward loops. Yes. AUDIENCE: At the same time z, it's just going in. So wouldn't that make the [INAUDIBLE]? Is that why there's more ingoing edges than outgoing edges? PROFESSOR: Now this is a problem with verbal arguments-- you can construct anything. And indeed, I would say that this is an example. What we said is that the distribution of incoming edges is roughly kind of similar to an ER network in the sense that if the mean is one, then sometimes you get 0, sometimes one, sometimes two. And they're all kind of reasonable. So in that sense, I'd say this z node is not so unusual from the standpoint of degree-preserving network.**

**If z had one00 incoming edges, then it's certainly true what you're saying-- that the degree-preserving would then have fewer. All right. So this is the basic argument for why you might go and look at what the function of the feed-forward loop might be. I just want to say a few things about this original paper that Uri published. So it's in Science in 2002.**

**"Network motifs: Simple Building Blocks of Complex Networks." All right. So the**

10

**authors did indeed analyze both the E. coli and the yeast transcription network. But they also analyzed a number of other networks to look at these networks motifs. So they also analyzed neurons from C. elegans, the worm, where the connectome has been known for several decades now.**

**And again, they found that feed-forward loops appeared more frequently than what would be expected, based on the known model of degree preserving. And that's encouraging is that saying, oh maybe feed-forward loops really are somehow preserving some-- they're performing some useful information-processing task.**

**Of course, you always have to worry-- there's also the spatial arrangement. You can worry about a lot of things. But that's encouraging. He also analyzed food webs, where in that case feed-forward loops were not a network motif, but other things were, So that's interesting.**

**He analyzed the design of electronic circuits, a forward logic chip. I don't know that is. But then also the worldwide web, it's another network people love to analyze. And indeed, he saw some other patterns. And the idea is that in each of these contexts, the network motifs are different, depending upon the microscopic structure that's leading to it, or the function that it's maybe evolving towards, or whatnot. So it's a way of getting insight into the properties of these complex networks.**

**Are there any questions about these network-- the global network structures, before we get into the feed-forward loop in particular?**

**So first I want to just go ahead and do a few of our little concept questions. Just because you have the cards, and I think that the chapter is actually pretty nice in the sense of you can read it, and get a clear sense of what's going on.**

**But let's start by just considering this feed-forward loop, which is this coherent type 1. So now the arrows actually mean activating. So we have X going to Y. Now it's going to be going to a Z. But we have to remember that now that there are two inputs, we do have to specify how the inputs are going to be combined.**

11

**And for now what we'll do is we'll assume that it's an AND gate. And that goes to Z. As always, we're going to have to think. There's some signal x and signal y that come in here. In many, many cases, these transcription factors in addition to being regulated by another, say transcription factor, may also be responsive to some signal.**

**And there was a nice example of this in Uri's book which was how E. Coli decide whether to make the suite of proteins that are required to digest the carbon source arabinose, the sugar arabinose. But for now, let's just think about this. And we want to just make sure that we remember. And once again, it's not that you should necessarily memorize these things. But after having seen the argument once or twice, you should be able to reconstruct all of these things.**

**So I claimed that somewhere in here there's a sign sensitive delay. Now the question is, in which direction is there a delay. And so it's going to be some combination of on and off perhaps.**

**And check means that it's a delay in that direction. Well actually we should just from nothing there-- and D is don't know.**

**AUDIENCE: In that direction you mean?**

**PROFESSOR: That there's a-- this means that there's a sign. That's right. So this would be going from off to on, so turning on. So this is turning on, as compared to turning off. And we're looking at this is delay. We're talking about, this is in response to Sx changing concentration of Z.**

**Any questions about what I'm referring to in this?**

**AUDIENCE: Is there any Sy?**

**PROFESSOR: Yes. Good question I like that right Sy is present.**

**AUDIENCE: [INAUDIBLE]?**

**PROFESSOR: Right. So this is compared to simple regulation, or i.e. does the concentration of Z**

12

**immediately start to change after this Sx changes? It goes from either 0 to 1, or 1 to 0.**

**AUDIENCE: So simple regulation in this case would be erase that line between X and Y? PROFESSOR: Yes. And make the AND gate a--**

**AUDIENCE: Not an AND gate?**

**PROFESSOR: Not an AND gate, exactly, yeah. We're comparing to just if X is just directly regulating Z. Because what we want to know is, I mean what might a function of the feed-forward loop be. So I'll give you 15 seconds to think through this. Once again, it's not that you should have memorized it.**

**I don't want anybody saying that they just couldn't read my handwriting.**

**AUDIENCE: So this is for the second case we're asking?**

**PROFESSOR: I'm sorry. So this is-- I'm asking about for this feed-forward loop, the coherent type 1 with an AND gate. And I'm comparing, I'm asking is there a delay in either turning on or turning off, as compared to the simple regulation of X regulating Z. And of course, this is my [INAUDIBLE] Sx.**

**And we assume that X is already present. Do you need more time? All right, ready? Three, two, one. OK. We got a clear majority of the group actually is saying C. And so we can get at this kind of visually, graphically. I really like graphs. I think they're much nicer than equations. Different people can agree or disagree. but that's my--**

**The idea is that we have Sx. It starts out off and say turns on. So if we think about the X star, X was always around. So means that X star immediately-- so the signal immediately changes X into X star, the active version.**

**Now Y, and this is why we can even say Y star, because the signal Y is always there. It starts our here. It immediately gets the signal. So it starts coming up. But of course, this is an AND gate. Which means that you need to have both active Y and active X in order to start getting expression of Z.**

13

**So we have if we look at Z, there's something threshold at which is Y starts allowing for expression of Z. So just because we have active X, doesn't mean that we immediately start getting expression of Z. We need Y as well. So this comes up.**

**However, when the signal here goes away, X star immediately goes away. This is the separation of timescale idea. This is just a binding of a small molecule or so. What that means is that Y star-- is there a delay on Y star?**

**We're going to do a verbal. Is there a delay before Y star just starts coming down? So the question, it's going to decay exponentially once it starts going. Does it a start going immediately, or is there a delay? So the question is, is there a delay before the exponential fall off of Y star. You're going to say yes or no, ready, three, two, one.**

**AUDIENCE: No.**

**PROFESSOR: No delay. Great. And indeed over here it's the same thing, no delay because of the AND gate. Expression of Z requires both X star and Y star. So although Y star still there, since it's an AND gate, Z goes down.**

**That means that in this case we have a sign sensitive delay for turning on Z, but not for turning off Z. And of course, this can be useful, depending upon the costs and benefits of having false positives and false negatives in the signal.**

**If this AND gate were switched to an OR gate, how does this thing change? I'm going to give you 10 seconds. All right. So, question is, if I convert this to an OR gate, does it change anything or not. Do you need more time? Ready, three two one.**

**Now we got a lot of B's. Great. So in this case it's coherent type 1, feed-forward loop with an OR gate. I'm not going to go over the logic. But I encourage you, if you're confused by this, just make sure that you can reconstruct the argument.**

**From my standpoint, these equations I mean, it's good to do equations. But it's more important to be able to understand the logic here. Did you have a question?**

14

- **AUDIENCE: Yes. So how is it easy to prove experimentally what kind of gate there is? PROFESSOR: Yes. So the idea is that in many cases you can put X on an inducible promoter. You could put Y on an inducible promoter. So you can-- just some small molecule will allow you to control these. And then you can measure, say fluorescence, on Z. And that's the most direct things. It's experimentally doing it yourself.**

   - **Of course, much of the data that you see the chapter is kind of just looking at the fluorescent Z as a function of the signals that you put in. And that's certainly an argument for it. And then ultimately what you'd like is to measure things in multiple different ways, confirm that it's all consistent.**

**Any other questions about this idea of sign sensitive delay element? Yeah?**

- **AUDIENCE: Sorry. So among these 42-- these that are this type, is it possible to look at the actual genes, and see if that interrelationship actually makes sense?**

- **PROFESSOR: That's a good question. So if you look at across both E. coli and yeast, what you see is that of the feed-forward loops, about half of them are coherent type 1, which is one of the eight possible kinds of feed-forward loops. And so what you're asking is, in this case, so let's say there are 20 coherent type 1, how many of them, what fraction of them does this all makes sense? And it's a good question. I don't know.**

**I haven't looked at it. Because it's always dangerous, of course, that we find one example of the 20 where it kind of makes sense conceptually. And then we go and we test it experimentally, and see that it all works. And then we're convinced. But you're pointing out that maybe we shouldn't be convinced yet.**

**AUDIENCE: But I'm just curious. If you're proposing a functional kind of explanation, and if know what the genes are.**

- **PROFESSOR: That's right. You should be able to go and see whether it somehow make sense. And of course makes sense is always a slippery concept. Because we can always-it's not that this radically changes the logic. And then in any given circumstance you**

15

**may be say, oh well. You can kind of wave your arms and make up a story where it kind of makes sense. But then the only way to really feel comfortable with it or not, is for you yourself to go on look at them, and see how comfortable you are with each of those arguments. And I haven't actually done that.**

**So one more question in this regard. All right. So let's imagine that instead of thinking about changes in Sx, with Sy present, let's now flip things. Let's assume that Sx is present and ask about Sy turning on and off.**

**Again with the AND gate, I want to know in which direction is there a delay when turning either on or off. Now we're talking about with Sy turning on or off. Does everybody understand the question? I'll give you 10 seconds to make sure.**

**Do need more time? Let's go ahead and vote. Ready, three, two, one. All right. OK, so I'd say now it's pretty overwhelming that the group again agrees that now it'll be A. So if we have Sx equal to 1, and Sy is changing, then in this case we don't get any of these delays. So there's sort of immediate changes in Z as Sy changes. And that's because this is an AND gate. If X is already there that means that we've already satisfied this half of it. So then we're just reduced to simple regulation. This is just equivalent to Y regulating Z. So there are no delays either turning on or turning off.**

**So what you read about from Uri's book is what is that the coherent type 1 is perhaps the most common of the feed-forward loops observed in these transportation networks. The other of the feed-forward loops that is distinctly overrepresented is this incoherent type 1. So it's very similar, with the exception that now what we have is X activating Y, but now Y is going to be repressing Z. And we have X again activating Z.**

**And we're going to use an AND gate again. Its edge going to Z. For me, I find it sometimes a little bit confusing to think about a repression and an AND gate. So it is useful to make sure that we kind of understand the logic of all these things. So if we have say X star, Y star, and we can just make sure this is absence or presence, digital approximation of each of these things.**

16

**And the question is, if we have expression of Z. Now the way to just think about this is that this guy is equivalent to kind of inverting the sign of Y star. And then we have an AND gate. So this is a 0,1. That's not an AND. Well 0 is enough to give us a 0. So here we get activation. Here we don't.**

**And so we can do a similar kind of story of what we did here. Except that now instead of Y being an activator, it's now a repressor. And again, we're going to think about what happens with the signal coming in.**

**Is any difference up to this point? Let's think about it. Everything but this for a second. All right. So this is a case where we already have signal Y that's allowing, say, the Y repressor to bind. Then we make Sx appear. I want to know verbally, yes or no. Do I have to draw something new up to this point here? Ready, so what do I want to say? Is there a change from this drawing up to this point? Ready, three, two, one.**

**AUDIENCE: Yes.**

**PROFESSOR: Yes. All right. And that's because actually Z starts coming up at this point. It's very, very nerve-wracking, these quizzes, I know.**

**The idea is that here Y is now a repressor. So it's not that you need Y in order to get expression of Z. Is that once you have Y star, then you stop getting expression of Z. So it looks like maybe I'll make a-- so in this case everything's the same here. Except that in this case you start getting Z coming up. And then once Y gets up to a sufficiently high level, it starts repressing. In that case it might do something like this.**

**Now, depending upon the strength of that repression, this curve might look different. Because it could come all the way down to 0. Depending on if it's a very effective repressor. And depending upon whether it's fully repressed or only partially repressed, you might think about it as either being a pulse generator, so you get some Z, and then it goes away. Or you could think about it as a way of increasing the rate at which you're able to turn this gene on.**

17

**Because it's sort of like this negative autoregulation idea that initially you get lots of expression. And then later you stop getting as much. Of course, here you would get an overshoot. But maybe that's not all bad.**

**So in this what you might say is this is a pulse generator. And this here is a way of making t on go down. Are there any questions about the logic of what happens in this incoherent type 1? Yes?**

---

[← proteins directly.](02-proteins-directly.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
