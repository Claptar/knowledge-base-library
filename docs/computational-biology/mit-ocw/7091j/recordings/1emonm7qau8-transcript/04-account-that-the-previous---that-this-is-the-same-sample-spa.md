---
title: account that the previous-- that this is the same sample space?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/1emonm7qau8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# account that the previous-- that this is the same sample space?

**Source:** `recordings/1emonm7qau8-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Yeah, the weight matrix, after you go through one iteration of all the sequences, you have a weight matrix. You carry that over, you don't start from scratch. You bring that weight matrix back up, and use that to score, let's say, that first sequence. Yeah, the weight matrix just keeps moving around. Moves a little bit every time you sample a sequence. AUDIENCE: So you constantly get a strong [INAUDIBLE]. PROFESSOR: Well, does it? AUDIENCE: Well, I guess-PROFESSOR: Would it constantly get stronger? What's to make it get stronger or weaker? I mean, this is sort of-- you're on the track. AUDIENCE: If it is random, then there's some probability that you're going to find this motif again, at which point it will get stronger. But, if it's-- given enough iterations, it gets stronger as long as you hit different spots at random. PROFESSOR: Yeah, yeah. That's what I'm-- I think there was a comment. Jacob, yeah? AUDIENCE: Well, you can think about it as a random walk through the landscape. Eventually, it has a high probability of taking that motif, and updating the [INAUDIBLE] direction, just from the probability of [INAUDIBLE]. PROFESSOR: OK. AUDIENCE: And given the [INAUDIBLE]. PROFESSOR: OK, let's say I had 100 sequences of length, I don't know, 30. And the width of the motif is 6. So here's our sequences. We choose random positions for the start position, and let's say it was this example where the real motif, I put it right here, and all the sequences. That's where it starts. Does this help? So it's 30 and 6, so there's 25 possible start positions. I did that to**

22

**make it a little easier.**

**So what would happen in that first iteration? What w can you say about what the weight matrix would look like? It's going to be a width, W, you know, columns 1, 2, 3, up to 6. We're going to give it 100 positions at random. The motif is here-- let's say it's a very strong motif, that's a 12-bit motif. So it's 100%-- it's echo R1. It's that.**

**What would that weight matrix look like, in this first iteration, when you first just sample the sites at random? What kind of probabilities would it have?**

**AUDIENCE: [INAUDIBLE] PROFESSOR: Equal? OK-- perfectly equal? AUDIENCE: Roughly.**

**PROFESSOR: OK. Any box? Are we likely to hit the actual motif, ever, in that first encryption? AUDIENCE: No, because you have a uniform probability, of sampling. Well, uniform at each one of the 25 positions?**

**PROFESSOR: Right. AUDIENCE: Right now, you're not sampling proportional to the likelihood. PROFESSOR: So the chance of hitting the motif in any given sequence is what? AUDIENCE: 1/25. PROFESSOR: 1/25. We have 100 sequences. AUDIENCE: So that's four out of-PROFESSOR: So on average, I'll hit the motif four times, right. The other 96 positions will be essentially random, right? So you initially said this was going to be uniform, right? On average, 25% of each base, plus or minus a little bit of sampling error-- could be 23, 24, 26. But now, you pointed out that it's going to be four. You're going to hit the motif four times, on average. So, can you say anything more?**

23

**AUDIENCE: Could you maybe have a slightly bias towards G on the first position? Slightly biased towards A on the second and third? Slightly biased towards T on the fourth and fifth. And slightly biased towards C in the sixth? So it would be slightly biased-PROFESSOR: Right, so remind me of your name? AUDIENCE: I'm Eric. PROFESSOR: Eric, OK, so Eric says that because four of the sequences will have a G at the first position, because those are the ones where you sampled the motif, and the other 96 will have each of the four bases equally likely, on average you have like 24%-plus 4 for G, right? Something like 28%-- this will be 28%, plus or minus a little bit. And these other ones will be whatever that works out to be, 23 or something like that-- 23-ish, on average. Again, it may not come out exactly like-- G may not be number one, but it's more often going to be number one than any other base. And on average, it'll be more like 28% rather than 25%. And similarly for position two, A will be 28%, and three, and et cetera. And then the sixth will be-- C will have a little bit of a bias. OK, so even in that first round, when you're sampling that first sequence, the matrix is going to be slightly biased toward the motif-- depending how the sampling went. You might not have hit any instances of motif, right? But often, it'll be a little bit-Is that enough of a bias to give you a good chance of selecting the motif in that first sequence?**

**AUDIENCE: You mean in the first iteration? PROFESSOR: Let's say the first random sequence size sample. No. You're shaking your head. Not enough of a bias because-- it's 0.28 over 0.25 to the sixth power, right? So it's like-AUDIENCE: The likelihood is still close 1. Like, that's [INAUDIBLE] ratio. PROFESSOR: So it's something like 1.1 to the sixth, or something like that. So it might be close to**

24

**2, might be twice as likely. But still, there's 25 positions. Does that make sense? So it's quite likely that you won't sample the motif in that first-- you'll sample something else. Which will take it away in some random direction. So who can tell me how this actually ends up working? Why does it actually converge eventually, if you get it long enough?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: So the information content, what will happen to that? So the information content, if it was completely random-- we said that would be uniform. That would be zero information content, right? This matrix, which has around 28% at six different positions, will have an information content that's low, but non-zero. It might end up being like 1 bit, or something. And if you then sample motifs that are not the motif, they will tend to reduce the information content, tend to bring it back toward random.**

**If you sample locations that have the motif, what will that do to the information content? Boost it. So what would you expect if we were to plot the information content over time, what would that look like?**

**AUDIENCE: It should trend upwards, but it could fluctuate.**

**PROFESSOR: Yeah. AUDIENCE: Over the number of iterations? PROFESSOR: I think I blocked it here. Let me see if I can-- Let's try this. I think I plotted it. OK, never mind. I wanted to keep it very mysterious, so you guys have to figure it out. The answer is that it will-- basically what happens is you start with a weight matrix like this. A lot of times, because the bias for the motif is quite weak, a lot of times you'll sample-- even for a sequence, what matters is-- like, if you had a sequence where the location, initially, was not the motif, and then you sample another location that's not the motif, that's not really going to change anything. It'll change things a little bit,**

25

**but not in any particular direction. What really matters is when you get to a sequence where you already had the motif, if you now sample one that's not the motif, your information content will get weaker. It will become more uniform.**

**But if you have a sequence where it wasn't the motif, but now you happen to sample the motif, then it'll get stronger. And when it gets stronger, it will then be more likely to pick the motif in the next sequence, and so on.**

**So basically what happens to the information content is that over many iterations-- it starts near 0. And can occasionally go up a little bit. And then once it exceeds the threshold, it goes like that. So what happens is it stumbles onto a few instances of the motif that bias the weight matrix. And if they don't bias it enough, it'll just fall off that. It's like trying to climb the mountain-- but it's walking in a random direction. So sometimes it will turn around and go back down.**

**But then when it gets high enough, it'll be obvious. Once you have a, say, 20 times greater likelihood of picking that motif than any other sequence, most of the time you will pick it. And very soon, it'll be stronger. And the next round, when it's stronger, you'll have a greater bias for picking the motif, and so forth. Question?**

**AUDIENCE: For this specific example, M is much greater than L minus W. How true is that for practical examples?**

**PROFESSOR: That's a very good question. There is sometimes-- depends on how commonly your motif occurs in the genome, and how good your data is, really, and what the source of your data is. So sometimes it can be very limited, sometimes-- If you do ChIPSeq you might have 10,000 peaks that you're analyzing, or something. So you could have a huge number.**

**But on the other hand, if you did some functional assay that's quite laborious for a motif that drives luciferase, or something, and you can only test a few, you might only have 10. So it varies all over the map. So that's a good question. We'll come back to that in a little bit. Simona?**

26

**AUDIENCE: If you have a short motif, does it make sense, then, to reduce the number of sequences you have? Because maybe it won't converge? PROFESSOR: Reduce the number of sequences? What do you people think about that? Is that a good idea or a bad idea? It's true that it might converge faster with a smaller number of sequences, but you also might not find it all. So generally you're losing information, so you want to have more sequences up to a certain point. Let's just do a couple more examples, and I'll come back. Those are both good questions. OK, so here's this weak motif. So this is the one where you guys couldn't see it when I just put the sequences up. You can only see it when it's aligned-- it's this thing with GGC, here. And here is, again, the Gibbs Sampler. And what happened? Who can summarize what happened here? Yeah, David?**

**AUDIENCE: It didn't converge.**

**PROFESSOR: Yeah, it didn't quite converge. The motif is usually on the right side, and it found something that's like the motif. But it's not quite right-- it's got that A, it's G A G C, it should be G G C. And so it sampled some other things, and it got off track a little bit, because probably by chance, there were some things that looked a little bit like the motif, and it was finding some instances of that, and some instances of the real motif. And yeah, it didn't quite converge.**

**And you can see this probability vectors here, they have multiple white dots in many of the rows. So it doesn't know, it's uncertain. So it keeps bouncing around. So it didn't really converge, it was too weak, it was too challenging for the algorithm. This is just a summary of the Gibb Sampler, how it works. It's not guaranteed to converge to the same motif every time. So what you generally will want to do is run it several times, and nine out of 10 times, you get the same motif. You should trust that. Go ahead.**

**AUDIENCE: Over here, are we optimizing for convergence of the value of the information content?**

27

**PROFESSOR:**

**No, the information content is just describing-- it's just a handy single number description of how biased the weight matrix is. So it's not actually directly being optimized. But it turns out that this way of sampling tends to increase information content. It's sort of a self-reinforcing kind of a thing. But it's not directly doing that.**

**However MEME, more or less, directly does that. The problem with that is that, where do you start? Imagine an algorithm like this, but where you deterministically-instead of sampling from the positions in the sequence, where it might have a motif in proportion to probabilities, you just chose the one that had the highest probability. That's more or less what MEME does. And so what are the pros and cons of that approach, versus this one? Any ideas?**

**OK, one of the disadvantages is that the initial choice of-- how you're initially seeding your matrix, matters a lot. That slight bias-- it might be that you had a slight bias, and it didn't come out being G was number one. It was actually-- T was number one, just because of the quirks of the sampling. So what would this be, 31 or something? Anyway, it's higher than these other guys.**

**And so then you're always picking the highest. It'll become a self-fulfilling prophecy. So that's the problem with MEME.**

**So the way that MEME gets around that, is it uses multiple different seeding, multiple different starting points, and goes to the end with all of them. And then it evaluates, how good a model did we get at the end? And whichever was the best one, it takes that. So it actually takes longer, but you only need to run it once because it's deterministic. You use a deterministic set of starting points, you run a deterministic algorithm, and then you evaluate.**

**The Gibbs, it can go off on a tangent, but because it's sampling so randomly, it often will fall off, then, and come back to something that's more uniform. And when it's a uniform matrix, it's really sampling completely randomly, exploring the space in an unbiased way. Tim?**

**AUDIENCE: For genomes that have inherent biases that you know going in, do you precalculate-**

28

   - **do you just recalculate the weight matrix before, to [? affect those classes? ?] For example, if you had 80% AT content, then you're not looking for-- you know, immediately, that you're going to hit an A or a T off the first iteration. So how do you deal with that?**

- **PROFESSOR: Good question. So these are some features that affect motif finding. I think that we've now hit at least a few of these-- number of sequences, length of sequences, information content, and motif, and basically whether the background is biased or not.**

**So, in general, higher information content motifs, or lower information content, are easier to find-- who thinks higher? Who thinks lower? Someone, can you explain?**

- **AUDIENCE: I don't know. I just guessed.**

- **PROFESSOR: Just a guess? OK, in back, can you explain? Lower?**

**AUDIENCE: Low information content is basically very uniform. PROFESSOR: Low information means nearly uniform-- right, those are very hard to find. That's like that GGC one. The high information content motif, those are the very strong ones, like that first one. Those are much easier to find. Because when you stumble on to them, it biases the matrix more, and you rapidly converge to that. OK, high information is easy to find.**

**So if I have one motif per sequence, what about the length of the sequence? Is longer or shorter better? Is long better? Who thinks shorter is better? Shorter-- can you explain why short?**

**AUDIENCE: Shouldn't it be the smaller the search space, the fewer the problems? PROFESSOR: Exactly, the shorter the search space, and your motif, there's less place for it to hide. You're more likely to sample it. Shorter is better. If you think about-- if you have a motif like TATA, which is typically 30 bases from the TSS, if you happen to know that, and you give it plus 1 to minus 50, you're**

29

**giving it a small region, you can easily find the TATA box. If you give it plus 1 to minus 2,000 or something, you may not find it. It's diluted, essentially.**

**Number of sequences-- the more the better. This is a little more subtle, as Simona was saying. It affects convergence time, and so forth. But in general, the more the better.**

**And if you guessed the wrong length of your matrix, that makes it worse than if you guess the right length in either direction. For example, it's six-base motif, you guess three. The information content, even if it's a 12-bit motif, there's only six bits that you could hope to find, because you can only find three of those positions. So clearly, effectively it's a smaller information content, and much harder to find. And vice versa.**

**Another thing that occurs in practice is what's called shifted motifs. Your motif is G A A T T C. Imagine in your first iteration you happen to hit several of these sequences, starting here. You hit the motif, but off by two at several different places. That'll bias first position to be A, and the second position to be T, and so forth.**

**And then you tend to find other shifted versions of that motif. You may well converge to this-- A T C C N N, or something like that-- which is not quite right. It's close, you're very close, but not quite right. And it's not as information rich as the real motif. Because it's got those two N's at the end, instead of G A.**

**So one thing that's done in practice is a lot of times, every so often, the algorithm will say, what would happen if we shifted all of our positions over to the left by one or two? Or to the right by one or two? Would the information content go up? If so, let's do that.**

**So basically, shifted versions of the motif become local, near-optimal solutions. So you have to avoid them. And biased background composition is very difficult to deal with. So I will just give you one or two more examples of that in a moment, and continue.**

**So in practice, I would say the Gibbs Sampler is sometimes used, or AlignACE,**

30

**which is a version of Gibbs Sampler. But probably more often, people use an algorithm called MEME, which is this EM algorithm, which, like I said, is deterministic, so you always get the same answer, which makes you feel good. May or may not always be right, but you can try it out here at this website.**

**And actually, the Fraenkel Lab has a very nice website called WebMotifs that runs several different motif finders including, like I said, a MEME and AlignACE, which is similar to Gibbs, as well as some others. And it integrates the output, so that's often a handy thing to use. You can read about them there.**

**And then I just wanted to say a couple words-- this is related to Tim's comment about the biased background. How do you actually deal with that? And this related to this notion of a mean bit score of a motif.**

**So if I were to give you a motif model, P, and a background model, q, then the natural scoring system, if you wanted additives scores, instead of multiplicative, you would just take the log. So log P over q, I would argue, is natural additive scores. And that's often what you'll see in a weight matrix-- you'll see log probabilities, or logs of ratios of probabilities. And so then you just add them up, and it makes life a bit simpler.**

**And so then, if you were to calculate what's the mean bit score-- if I had a bunch of instances of a motif, it will be given by this formula that's here in the upper right. So that's your score. And this is the mean, where you're sampling over the probability in using the motif model, probabilities.**

**So it turns out, then, that if qk, your background, is uniform, motif of width w-- so its probability of any w-mer, is 1/4 to the w, then it's true that the mean bit-score is 2w minus the entropy of the motif, which is the same as the information content of the motif, using our previous definition. So that's just a handy relationship. And you can do a little algebra to show that, if you want.**

**So basically summation Pk log Pk over qk-- this log, you turn that into a difference-so that summation Pk log Pk minus Pk log qk. And then you can do some**

31

**rearrangement, and sum them up, and you'll get this formula. I'll leave that as an exercise, and any questions on it, we can do it next time.**

**So what I wanted to get to is sort of this big question that I posed earlier-- what's the use of knowing the information content of a motif? And the answer is that one use is that it's true, in general, that the motif with n bits of information will occur about once every 2 to the n bases of random sequence. So we said a six-cutter restriction enzyme, echo R1, has an information content of 12 bits.**

**So by this rule, it should occur about once every to 2 to the 12th bases of sequence. And if you know your powers of 2, which you should all commit to memory, that's about 4,000. 2 to the 12th is 4 to the sixth, is 4,096. So it'll occur about once every 4 [? kb, ?] which if you've ever cut E. coli DNA, you know is about right-- your fragments come out to be about 4 [? kb. ?]**

**So this turns out to be strictly true for any motif that you can represent by a regular expression, like a precise motif, or something where you have a degenerate R or Y or N in it, still true. And if you have a more general motif that's described by weight matrix, then you have to define a threshold, and it's roughly true, but not exactly.**

**All right, so what do you do when the background composition is biased, like Tim was saying? What if it's 80%, A plus T? So then, it turns out that this mean bit-score is a good way to go. So like I said, the mean bit-score equals the information content in this special case, where the background is uniform.**

**But if the background is not uniform, then you can still calculate this mean bit-score, and it'll still be meaningful. But now it's called something else-- it's called relative entropy. Actually it has several names, relative entropy, Kullback-Leibler distance is another, and information for discrimination, depending whether you're reading the Double E literature, or statistics, or whatever.**

**And so it turns out that if you have a very biased composition-- so here's one that's 75% A T, probability of A and T are 3/8, C and G are 1/8. If your motif is just C 100% of the time, your information content by the original formula that I gave you,**

32

**would be 2 bits. However, the relative entropy will be 3 bits, if you just plug in these numbers into this formula, it will turn out to be 3 bits.**

**My question is, which one better describes the frequency of C in the background sequence? Frequency of this motif-- the motif is just a C. You can see that the relative entropy says that actually, that's stronger than it appears. Because it's a C, and that's a rare nucleotide, it's actually stronger than it appears. And so 2 to the 3rd is a better estimate of its frequency than 2 squared. So relative entropy.**

**So what you can do when you run a motif finder in a sequence of biased composition, you can say, what's the relative entropy of this motif at the end? And look at the ones that are strong. We'll come back to this a little more next time.**

**Next time, we'll talk about hidden Markov models, and please take a look at the readings. And please, those who are doing projects, look for more detailed instructions to be posted tonight. Thanks.**

33

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md)
