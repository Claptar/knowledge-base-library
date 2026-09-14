---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/1emonm7qau8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/1emonm7qau8-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Is this for finding motifs based on other known motifs? Or is this--**

**PROFESSOR: No, what we're doing-- I'm sorry, I should've prefaced that. We're doing de novo motif finding. We're going to tell the algorithm-- we're going to give the algorithm some sequences of a given length, or it can even be of variable lengths, and we're going to give it a guess of what the length of the motif is. So we're going to say, we think it's 8. That could come from structural reasons. Or often you really have no idea, so you just guess that you know, a lot of times it's kind of short, so we're going to go with 6 or 8, or you try different lengths. Totally de novo motif finding.**

**OK, so how does algorithm work? You have N sequences of length, L. You guessed that the motif has width, W. You choose starting positions at random-- OK, so this is a vector, of the starting position in each sequence, we're going to choose completely random positions within the end sequences. They have to be at least W before the end-- so we'll have a whole motif, that's just an accounting thing to make it simpler.**

**And then you choose one of the sequence at random. Say, the first sequence. You make a weight matrix model of width, W, from the instances in the other sequences. So for example-- actually, I have slides on this, so we'll just do it with the slides, you'll see what this looks like in a moment. And so you have instances here in the sequence, here in this one, here. You take all those, line them up, make a weight matrix out of those, and then you score the positions in sequence 1 for how well they match.**

**So, let me just do this. These are your motif instances. Again, totally random at the**

17

**beginning. Then you build a weight matrix from those by lining them up, and just counting frequencies. Then you pick a sequence at random-- yeah, your weight matrix doesn't include that sequence, typically. And then you take your theta matrix and you slide it along the sequence.**

**You consider every sub-sequence of length, W-- the one that goes from 1 to W, to one that goes from 2 to W plus 1, et cetera, all the way along the sequence, until you get to the end. And you calculate the probability of that sequence, using that likelihood that I gave you before. So, it's basically the probability generating sequence where you use the background vector for all the positions, except for the particular motif instance that you're considering, and use the motif model for that.**

**Does that make sense? So, if you happen to have a good looking occurrence of the motif at this position, here, in the sequence, then you would get a higher likelihood. So for example, if the motif was, let's say it's 3 long, and it happened to favor ACG, then if you have a sequence here that has, let's say, it's got TTT, that's going to have a low probability in this motif. It's going to be 0.1 cubed.**

**And then if you have an occurrence of, say, ACT, that's going to have a higher occurrence. It's going to be 0.7 times 0.7 times 0.1. So, quite a bit higher. So you start, it'll be low for this triplet here-- so I'll put a low value here. TTA is also going to be low. TAC, also low. But ACT, that matches 2 out of 3 to the motif. It's going to be a lot better. And then CT is going to be low again, et cetera.**

**So you just slide this along and calculate probabilities. And then what you do is you sample from this distribution. These probabilities don't necessarily sum to 1. But you re-normalize them so that they do sum to 1, you just add them up, divide by the sum. Now they sum to 1. And now you sample those sites in that sequence, according to that probability distribution.**

**Like I said, in this case you might end up sampling-- that's the highest probability site, so you might sample that. But you also might sample one of these other ones. It's unlikely you would sample this one, because that's very low. But you actually sometime sample one that's not so great.**

18

**So you sample a starting position in that sequence, and you basically-- wherever you would originally assign in sequence 1, now you move it to that new location. We've just changed the assignment of where we think the motif might be in that sequence. And then you choose another sequence at random from your list. Often you go through the sequences sequentially, and then you make a new weight matrix model.**

**So how will that weight matrix model differ from the last one? Well it'll differ because the instance of the motif in sequence 1 is now at a new location, in general. I mean, you might have sampled the exact same location you started, but in general it'll move. And so now, you'll got a slightly different weight matrix.**

**Most of the data going into it, N minus 1, is going to be the same. But one of them is going to be different. So it'll change a little bit.**

**You make a new weight matrix, and then you pick a new sequence. You slide that weight matrix along that sequence, you get this distribution, you sample from that distribution, and you keep going.**

**Yeah, this was described by Lorenz in 1993, and I'll post that paper. OK, so you sample a portion with that, and you update the location. So now we sampled that really high probably one, so we moved the motif over to that new orange location, there. I don't know if these animations are helping at all. And then you update your weight matrix.**

**And then you iterate until convergence. So you typically have a set of end sequences, you go through them once. You have a weight matrix, and then you go through them again. You go through a few times. And maybe at a certain point, you end re-sampling the same sites as you did in the last iteration-- same exact sites. You've converged.**

**Or, you keep track of the theta matrices that you get after going through the whole set of sequences, and from one iteration to the next, the theta matrix hasn't really changed much. You've converged.**

19

**So let's do an example of this. Here I made up a motif, and this is a representation where the four bases have these colors assigned to them. And you can see that this motif is quite strong. It really strongly prefers A at this position here, and et cetera.**

**And I put it at the same position in all the sequences, just to make life simple. And then a former student in the lab, [INAUDIBLE], he implemented the Gibb Sample in Matlab, actually, and made a little video of what's going on.**

**So the upper part shows the current weight matrix. Notice it's pretty random-looking at the beginning. And the right parts show where the motif is, or the position that we're currently considering. So this shows the position that was last sampled in the last round. And this shows the probability density along each sequence of what's the probability that the motif occurs at each particular place in the sequence.**

**And that's what happens over times. So it's obviously very fast, so I'll run it again and maybe pause it partway. We're starting from a very random-looking motif. This is what you get after not too many iterations-- probably like 100 or so. And now you can see your motif-- your weight matrix is now quite biased, and now favors A at this position, and so forth. And the locations of your motif, most of them are around this position, around 6 or 7 in the sequence-- that's where we put the motif in. But not all, some of them.**

**And then you can see the probabilities-- white is high, black is low-- in some sequences, it's very, very confident, the motif is exactly at that position, like this first sequence here. And others, it's got some uncertainty about where the motif might be. And then we let it run a little bit more, and it eventually converges to being very confident that the motif has the sequence, A C G T A G C A, and that it occurs at that particular position in the sequence.**

**So who can tell me why this actually works? We're choosing positions at random, updating a weight matrix, why does that actually help you find the real motif that's in these sequences? Any ideas? Or who can make an argument that it shouldn't work? Yeah? What was your name again?**

20

|**AUDIENCE:**|**Dan.**|
|---|---|
|**PROFESSOR:**|**Dan, yeah, go ahead.**|
|**AUDIENCE:**|**So, couldn't it, sort of, in a certain situation have different sub-motifs that are also**<br>**sort of rich, and because you're sampling randomly you might be stuck inside of**<br>**those boundaries where you're searching your composition?**|
|**PROFESSOR:**|**Yeah, that's good. So Dan's point is that you can get stuck in sub-optimal smaller or**<br>**weaker motifs. So that's certainly true. So you're saying, maybe this example is**<br>**artificial? Because I had started with totally random sequences, and I put a pretty**<br>**strong motif in a particular place, so there were no-- it's more like that mountain,**<br>**that structure where there's just one motif to find. So it's perhaps an easy case.**<br>**But still, what I want to know is how does this algorithm, how did it actually find that**<br>**motif? He implemented exactly that algorithm that I described. Why does it tend to**<br>**go towards [INAUDIBLE]? After a long time, remember it's a long time, it's hundreds**<br>**of iterations.**|
|**AUDIENCE:**|**So you're covering a lot in the sequence, just the random searching of the**<br>**sequence, when you're--**|
|**PROFESSOR:**|**There are many iterations. You're considering many possible locations within the**<br>**sequences, that's true. But why does it eventually-- why does it converge to**<br>**something?**|
|**AUDIENCE:**|**I guess, because you're seeing your motif more plainly than you're seeing other**<br>**random motifs. So it will hit it more frequently-- randomly. And therefore, converge**<br>**[INAUDIBLE].**|
|**PROFESSOR:**|**Yeah, that's true. Can someone give a more intuition behind this? Yeah?**|
|**AUDIENCE:**|**I just have a question. Is each iteration an independent test? For example, if you**<br>**iterate over the same sequence base 100 times, and you're updating your weight**<br>**matrix each time, does that mean it is the updating the weight matrix also taking into**|


21

---

[← protein has this? What can you predict about its function?](02-protein-has-this-what-can-you-predict-about-its-function.md) · [Up: contents](index.md) · [account that the previous-- that this is the same sample space? →](04-account-that-the-previous---that-this-is-the-same-sample-spa.md)
