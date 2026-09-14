---
title: some sort of dynamic programming.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kun6rj21hno-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# some sort of dynamic programming.

**Source:** `recordings/kun6rj21hno-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Now this one for RNA secondary structure that Nussinov came up with is a little bit different than the others. So you'll see it has a kind of different flavor. It turns out to be actually it's a little hard to get your head around at the beginning, but it's actually easier to do by hand. So let's take a look at that.**

**OK, so recursive maximization of base pairing. Now the thing about base pairing that's different from these other problems is that the first base in the sequence can base pair with the last. How do you chop up a sequence?**

**Remember with Needleman-Wunsch and with Viterbi we go from the beginning to the end, and that's a logical order. But with base pairing, that's actually not a logical order. You can't really do it that way.**

**So instead, you go from the inside out. You start in the middle of a sequence and work your way outwards in both directions. Or another way to think about it is you start with you write the sequence from 1 to n on both axes, and then actually we'll see that we initiate the diagonal all to 0's.**

**And then we think about these positions here next. So 1 versus 2. Could 1 pair with 2? And could 2 pair with 3?**

**Those are like little bits of possible RNA secondary structure. Again, we're ignoring this fact that loops have to be certain minimum. This is sort of a simplified case. And then you build outwards.**

**So you conclude that base 4 here could pair with base 5, so we're going to put a 1 there. And then we're going to build outward from that toward the beginning of the sequence and toward the end, adding additional base pairs when we can. That's basically the way the [INAUDIBLE] works.**

**And so that's one key idea, that we go from sort of close sequences, work outward, to faraway sequences. And the second key idea is that the relationship that, as you add more bases on the outside of what you've already got, that the optimal**

28

**structure in that larger portion of sequence space is related to the optimal structures of smaller portions of it in one of four different ways. And these are the four ways.**

**So let's look at these. So the first one is probably the simplest where if you're doing this, you're here somewhere, meaning you've compared sequences from position, let's say, i minus 1 to j minus 1 here. And then we're going to consider adding-actually, it depends how you number your sequence. Let me see how this is done. Sorry. i plus 1.**

**i plus 1 to j minus 1. We figured out what the optimal structure is in here, let's suppose. And now we're going to consider adding one more base on either end. We're going to add j down here, and we're going to ask if it pairs with i.**

**And if so, we're going to take whatever the optimal structure was in here and we're going to add one base pair, and we're going to add plus 1 because now it's got one additional. We're counting base pairs. So that's that first case there.**

**And then the second case is you could also consider just adding one unpaired base onto whatever structure you had, and then you don't add one. And you could go in either direction. You can go sort of toward of the beginning of the sequence or toward the end of the sequence.**

**And then the third one is the tricky one, is what's called a bifurcation. You could consider that actually i and j are both paired, but not with each other. That i pairs with something that was inside here and j pairs with something that was inside here. So your optimal parse from i to j, if you will, is not going to come from the optimal parse from i plus 1 to j minus 1. It's going to come from rethinking this and doing the optimal parse from here to here and from here to here, and combining those two.**

**So you're probably confused by now, so let me try to do an example. And then I have an analogy that will confuse you further. So ask me for that one. This was the simplest one I could come up with that has this property.**

**OK, so we said before that if you were doing the optimal from 1 to 5, that it would be the AC pairing with the GT. We do that one. And now if you notice, this guy is kind of**

29

**a similar sequence. I just added a T at the beginning and an A at the end.**

**And so you can probably imagine that the best structure of this is here, those three. You've got three pairs of this sub-sequence here. That's as good as you can do with seven bases. You can only get three pairs. And this is as good as you can do with five, so these are clearly optimal.**

**So the issue comes that if you're starting from somewhere in the middle here-- let's say you are-- let's see, so how would you be doing this? You start here. Let's suppose the first two you consider are these two. You consider pairing that T with that A.**

**You can see this is not going to go well. You might end up with that as your optimal substructure of this region. Remember, you're working from the inside out, so you're going from here to here, and you end up with that.**

**And what do you do here? You don't have a G to pair the C to, so you add another unpaired base. Now you've got this optimal substructure of a sequence that's almost the whole sequence. It's just missing the first and last bases, but it only has three base pairs.**

**So when you go to add this, you can say, oh, I can't add any more base pairs, so I've only got three. But you should consider that we've already solved the optimal structure of that, and we had two nice pairs here. We had that pair and that pair, and we already solved the substructure of the optimal structure of this portion here, and you had those three pairs.**

**And so you can combine those two and all of a sudden you can do much better. So that's what that bifurcation thing is about. So this is the recursion working out, and you can see that's the base pairing one. You can add one, or you can just add an unpaired base and you don't add anything.**

**Or you consider all the possible locations of bifurcations in-between the two positions you're adding, i and j, and you consider all the possible pairs. And you just sum up each pair and go-- I'm sorry, you don't sum them up. You consider them all,**

30

**and then you take the maximum.**

**All right, so the algorithm is to take an n by n matrix, initialize the diagonal to 0, and initialize the sub-diagonal to 0 also. Just don't think too much about that. Just do it.**

**And then fill in this matrix recursively from the diagonal up and to the right. And it actually doesn't matter what order you fill it in as long as you're kind of working your way up into the right. You have to have the thing to the left and the thing below already filled in if you're going to fill in a box.**

**And then you keep track of the optimal score, which is going to be the sum of base pairs. And then you also keep track of how you got there. What base pair did you add so that you can trace back?**

**And then when you get up to the upper right corner of this matrix, you then trace back. So here is a partially filled in this matrix. This is from that the Nature Biotechnology Review. And the 0's are filled in.**

**So here's what I want you to do at home, is print out, photocopy or whatever-- make this matrix, or make a bigger version of it perhaps-- and look at the sequence and fill in this matrix, and fill in the little arrows every time you add a base pair. It's actually not that hard. There are no bifurcations in this, so that's the tricky one. Ignore that one.**

**You'll just be adding base pairs. It'll be pretty easy. And then you can reconstruct the sequence.**

**So here it is filled in. And the answer is given, so you can check yourself. But do it without looking at the answer. And then you go to the upper right corner.**

**That means that the optimal structure from the beginning of the sequence to the end-- which, of course, was our goal all along. And then you trace back and you can see whenever you're moving diagonally here, you're adding a base pair. Remember, you add one on each end, and so you're moving diagonally and adding the base pair, and you get this little structure here.**

31

**So computational complexity of the algorithm. You could think about this but I'll just tell you. It's memory n squared because you've got to fill in this matrix, so square of the length of the sequence.**

**Time n cubed. This is bad now. And why is it n cubed? It's n cubed because you have to fill in a matrix that's n by n. And then when you do that maximization step, that check for bifurcations, that's sort of of order n, as well.**

**So n cubed-- so this means that RNA folding is slow. And in fact, some of the servers won't allow you to fold anything more than a thousand bases because they'll take forever or something like that. And it cannot handle pseudoknots. If you think through the recursion, pseudoknots will be a problem.**

**I'm going to just show you-- yeah, I'll get to this-- that these are from the viruses. Real viruses, some of them have pseudoknots like these ones shown here, and some even have these kissing loops, which is another type where the two stem loops, the loops interact. And the pseudoknots in particular are important in the viral life cycle.**

**They can actually cause programmed ribosomal frame shifting. When the ribosomes hits one of the things, normally it just denatures RNA secondary structure. When it hits a pseudoknot, it'll actually get knocked back by one and will start translating in a different frame. And that's actually useful to the virus to do that under certain circumstances.**

**That's how HIV makes the replicated polymerase, is by doing a frame shift on the ribosome using a pseudoknot. So these things are important. And there's fancier methods that use more sophisticated thermodynamic models where GC counts more than AU.**

**And I won't go into the details, but I just wanted to show you some pretty pictures here that the Zuker algorithm-- this is a real world RNA folding algorithm-- calculates not only the minimum energy fold, but also sub-optimal folds, and the probabilities of particular base pairs, summing over all the possible structures that RNA could**

32

**form, weighted by their free energy. So it's the full partition function.**

**It's not perfectly accurate. It gets about 70% of base pairs correct, which means it usually gets things right, but occasionally totally wrong. And there's a website for the Mfold server, which is actually one of the most beautiful websites in bioinfomatics, I would say. And also if you want to run it locally, you should download the Vienna RNAfold package, which has a very similar algorithm.**

**And I just wanted to show you one or two examples. So this is the U5 snRNA. This is the output of Mfold. It predicts this structure. And then this what's called the energy dot plot, which shows the bases in the optimal structure down below here and then sort of these suboptimal structures here. And you can see there's no ambiguity. It's totally confident in this structure.**

**Then I ran the lysine riboswitch through this program, and I got this. I got the minimum for energy structure down in the lower left. And then you see there's a lot of other colored dots. Those are from the suboptimal structures.**

**So it looks like this thing has multiple structures, which of course it does. So the way that this one works is, in the absence of lysine, it forms this structure where the ribosome binding sequences-- this is prokaryotic-- is exposed. And so the ribosome can enter and translate these lysine biosynthetic enzymes.**

**But then when lysine accumulates to a certain level, it can interact with the RNA and shift it's structure so that you now form this stem, which sequesters the ribosome binding sequence and blocks lysine biosynthesis. So a very clever system.**

**And it turns out that there's dozens of these things in bacterial genomes, and they control a lot of metabolism. So they're very important. And there may be some in eukaryotes, too, and that would be good.**

**If anyone's looking for a product, not happy with their current project, you might think about looking for more riboswitches. So I'm going to have to end there. And thank you guys for your attention, and good luck on the midterm.**

33

---

[← [INTERPOSING VOICES]](05-interposing-voices.md) · [Up: contents](index.md)
